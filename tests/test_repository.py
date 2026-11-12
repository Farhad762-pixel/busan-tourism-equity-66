import csv
import math
from pathlib import Path
import tempfile
import unittest

from fastapi.testclient import TestClient

from scripts.verify_repository import check_saved_summaries, validate_attractions, validate_historical_exports
from src.analysis.metrics import gini, hhi, ranked_exposure
from src.api.main import app, Recommendation, _equity_ranking
from src.clean_attractions import export_attractions, SOURCE


class DatasetTests(unittest.TestCase):
    def test_historical_export_structure_not_provenance(self):
        reports = validate_historical_exports()
        self.assertEqual(len(reports), 18)
        self.assertTrue(all(not row['errors'] for row in reports))

    def test_cleaner_does_not_overwrite_existing_data(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / 'attractions.csv'
            export_attractions(SOURCE, output)
            with output.open(encoding='utf-8', newline='') as handle:
                self.assertEqual(len(list(csv.DictReader(handle))), 207)
            before = output.read_bytes()
            with self.assertRaises(FileExistsError):
                export_attractions(SOURCE, output)
            self.assertEqual(before, output.read_bytes())

    def test_attraction_integrity_and_json_projection(self):
        report = validate_attractions()
        self.assertEqual(report["status"], "pass", report["errors"])
        self.assertEqual(sum(report["district_counts"].values()), 207)

    def test_saved_tables_are_internally_consistent_not_reproduced(self):
        report = check_saved_summaries()
        self.assertTrue(report["exposure_table_matches_lambda_0_8_gini"])
        for row in report["policy_checks"]:
            self.assertTrue(row["gain_arithmetic_matches"])
            self.assertTrue(row["retention_arithmetic_matches"])
        for row in report["accessibility_checks"]:
            self.assertTrue(row["same_query_count"])


class MetricTests(unittest.TestCase):
    def test_known_concentrations(self):
        self.assertAlmostEqual(gini([1, 1, 1, 1]), 0)
        self.assertAlmostEqual(gini([0, 0, 0, 1]), .75)
        self.assertAlmostEqual(hhi([1, 1, 1, 1]), .25)
        self.assertAlmostEqual(hhi([0, 0, 0, 1]), 1)
        self.assertEqual(gini([0, 0]), 0)
        self.assertEqual(hhi([0, 0]), 0)

    def test_exposure_weights_reset_per_query(self):
        shares = ranked_exposure([["A", "B"], ["B"]], ["A", "B", "C"])
        total = 2 + 1 / math.log2(3)
        self.assertAlmostEqual(shares["A"], 1 / total)
        self.assertAlmostEqual(shares["B"], (1 + 1 / math.log2(3)) / total)
        self.assertEqual(shares["C"], 0)
        self.assertEqual(ranked_exposure([], ["A"]), {"A": 0})
        with self.assertRaises(ValueError):
            ranked_exposure([["unknown"]], ["A"])

    def test_reject_invalid_metrics(self):
        for values in ([], [-1, 1], [float("nan")], [float("inf")]):
            for metric in (gini, hhi):
                with self.assertRaises(ValueError):
                    metric(values)


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def get(self, path, **params):
        response = self.client.get(path, params=params)
        self.assertEqual(response.status_code, 200, response.text)
        return response.json()

    def test_health_docs_schema_and_attractions(self):
        self.assertEqual(self.get('/api/health')['status'], 'ok')
        response = self.client.get('/docs')
        self.assertEqual(response.status_code, 200)
        self.assertIn('SwaggerUIBundle', response.text)
        schema = self.get('/openapi.json')
        self.assertEqual(len(schema['paths']), 5)
        self.assertEqual(len(self.get('/api/attractions')), 207)
        filtered = self.get('/api/attractions', district='Yeongdo-gu')
        self.assertEqual(len(filtered), 13)
        self.assertTrue(all(x['district'] == 'Yeongdo-gu' for x in filtered))

    def test_sample_query_rankings_and_candidate_boundary(self):
        query = 'sea cafe photography'
        baseline = self.get('/api/recommend/baseline', query=query, limit=207)
        self.assertEqual(baseline, sorted(baseline, key=lambda r: -r['relevance_score']))
        self.assertEqual(baseline[0]['id'], 2140)
        self.assertAlmostEqual(baseline[0]['relevance_score'], .242851, places=6)
        self.assertEqual(self.get('/api/recommend/baseline', query=query), baseline[:10])
        positive = [r for r in baseline[:50] if r['relevance_score'] > 0]
        self.assertEqual(len(positive), 9)
        for weight in (0, .2, 1):
            equity = self.get('/api/recommend/equity', query=query, limit=10, equity_weight=weight)
            self.assertEqual({r['id'] for r in equity}, {r['id'] for r in positive})
            for row in equity:
                self.assertGreater(row['relevance_score'], 0)
                self.assertAlmostEqual(row['final_score'], (1-weight)*row['relevance_score']+weight*row['equity_score'])
                self.assertEqual(row['equity_measure'], 'prototype_attraction_distribution_proxy')
            comparison = self.get('/api/compare', query=query, limit=10, equity_weight=weight)
            self.assertEqual(comparison['baseline'], baseline[:10])
            self.assertEqual(comparison['equity_aware'], equity)
            self.assertEqual(comparison['baseline_unique_districts'], len({r['district'] for r in baseline[:10]}))
            self.assertEqual(comparison['equity_aware_unique_districts'], len({r['district'] for r in equity}))
        self.assertEqual(self.get('/api/recommend/equity', query='zzzznomatchingterm'), [])

    def test_nonpositive_and_top50_boundary(self):
        def rec(i, score):
            return Recommendation(id=i, name='test', district='test', latitude=35, longitude=129, address='', relevance_score=score)
        self.assertEqual([r.id for r in _equity_ranking([rec(1,.5),rec(2,0),rec(3,-.5)],10,.2)], [1])
        self.assertEqual(len(_equity_ranking([rec(i,.5) for i in range(51)], 100, .2)), 50)

    def test_input_validation(self):
        for endpoint in ('/api/recommend/baseline', '/api/recommend/equity', '/api/compare'):
            for params in ({}, {'query':' '}, {'query':'sea','limit':0}):
                self.assertEqual(self.client.get(endpoint, params=params).status_code, 422)
        for weight in (-1, 1.01, 'nan'):
            self.assertEqual(self.client.get('/api/recommend/equity', params={'query':'sea','equity_weight':weight}).status_code, 422)


if __name__ == '__main__':
    unittest.main()

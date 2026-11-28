"""No-network verification of KTO full-panel export and record validation."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from collect_kto_full_panel import check_json, make_audit, month_range


class KtoBatchTests(unittest.TestCase):
    def create(self, root, metric="food_spending_demand", month="202201",
               code="1106", district="26710", value="72.81", count=1):
        param = "tarSvcDemIxCd" if metric != "spending_per_visit_intensity" else "tarExpDsIxCd"
        value_field = "tarSvcDemIxVal" if metric != "spending_per_visit_intensity" else "tarExpDsIxVal"
        item = {"baseYm": month, "signguCd": district, param: code, value_field: value}
        result = {"api_response": {"response": {"header": {"resultCode": "0000"},
                    "body": {"totalCount": count,
                    "items": {"item": [item]} if count else {}}}}}
        filename = root / f"{month}_{district}_{metric}.json"
        filename.write_text(json.dumps(result), encoding="utf-8")
        return filename

    def test_48_months_and_rollover(self):
        self.assertEqual(len(list(month_range("202201", "202512"))), 48)
        self.assertEqual(list(month_range("202212", "202301")), ["202212", "202301"])
        with self.assertRaises(ValueError):
            list(month_range("202213", "202302"))

    def test_service_and_intensity_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            a = self.create(root)
            b = self.create(root, metric="spending_per_visit_intensity", code="2203", value="89.32")
            for file, metric, expected in [(a, "food_spending_demand", "72.81"),
                                          (b, "spending_per_visit_intensity", "89.32")]:
                status, row, message = check_json(file, "202201", "26710", metric)
                self.assertEqual(status, "valid", message)
                self.assertEqual(row["index_value"], expected)
            self.assertEqual(check_json(a, "202202", "26710", "food_spending_demand")[0], "invalid")
            self.assertEqual(check_json(a, "202201", "26110", "food_spending_demand")[0], "invalid")

    def test_missing_and_empty_handled_separately(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.create(root)
            empty = self.create(root, metric="shopping_spending_demand", code="1105", count=0)
            self.assertEqual(check_json(empty, "202201", "26710", "shopping_spending_demand")[0], "empty")
            r = make_audit(root, "202201", "202201")
            self.assertEqual(r["status_counts"]["valid"], 1)
            self.assertEqual(r["status_counts"]["empty"], 1)
            self.assertEqual(r["status_counts"]["missing"], 62)
            self.assertEqual(r["validated_rows"], 1)
            self.assertTrue((root / "kto_busan_indices_202201_202201.csv").exists())


if __name__ == "__main__":
    unittest.main()

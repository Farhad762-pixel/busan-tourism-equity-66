#!/usr/bin/env python3
"""Reproduce archived 33-query equity reranking from a private district-score input.

The 48-query benchmark is a DEVELOPMENT benchmark, not held out.
Public GitHub does not contain private source-derived economic scores.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from statistics import mean

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[2]
FIELDS = ("main_title", "subtitle", "place", "district", "address", "transport_info")
LAMBDAS = (0.0, 0.5, 0.8, 1.0, 2.0)


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def weight(rank):
    return 1 / math.log2(rank + 1)


def gini(values):
    xs = sorted(values)
    total = sum(xs)
    return (sum((2 * i - len(xs) - 1) * v for i, v in enumerate(xs, 1)) /
            (len(xs) * total)) if total else 0


def compute(attractions, queries, signals_rows):
    if len(attractions) != 207 or len(signals_rows) != 16:
        raise ValueError("Expected exactly 207 attractions and 16 district signals")
    signals = {r["district"]: float(r["economic_undercapture"]) for r in signals_rows}
    if len(signals) != 16 or any(not math.isfinite(v) or not 0 <= v <= 1
                                 for v in signals.values()):
        raise ValueError("Invalid or repeated economic signal")
    if set(row["district"] for row in attractions) != set(signals):
        raise ValueError("District mismatch")
    candidate = {r["district"] for r in signals_rows
                 if r["recommendation_candidate"].strip().lower() == "true"}
    eligible = [q for q in queries if q["valid_for_main_audit"].strip().lower() == "true"]
    if len(queries) != 48 or len(eligible) != 33:
        raise ValueError("Expected frozen 48-query development benchmark, 33 eligible")
    text = [" ".join(row.get(field) or "" for field in FIELDS) for row in attractions]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(text)
    rankings = {lam: [] for lam in LAMBDAS}
    for query in eligible:
        scores = cosine_similarity(vectorizer.transform([query["query"]]), matrix)[0]
        ordered = sorted(range(len(attractions)), key=lambda i: -float(scores[i]))
        positive = [i for i in ordered if scores[i] > 0]
        if len(positive) < 5:
            raise ValueError("Unexpected low-match eligible query: " + query["query"])
        for lam in LAMBDAS:
            candidates = sorted(positive[:50], key=lambda i: -float(scores[i]) *
                                (1 + lam * signals[attractions[i]["district"]]))[:10]
            rankings[lam].append([
                (attractions[i]["district"], float(scores[i]), weight(rank))
                for rank, i in enumerate(candidates, 1)])
    output = []
    for lam in LAMBDAS:
        query_lists = rankings[lam]
        flat = [r for recs in query_lists for r in recs]
        total = sum(w for _, _, w in flat)
        weights = {dist: 0.0 for dist in signals}
        for dist, _, w in flat:
            weights[dist] += w
        output.append({
            "lambda": lam,
            "query_count": len(query_lists),
            "recommendations": len(flat),
            "mean_relevance": mean(mean(score for _, score, _ in r) for r in query_lists),
            "undercapture_exposure": sum(w for d, _, w in flat if signals[d] > 0) / total,
            "candidate_exposure": sum(w for d, _, w in flat if d in candidate) / total,
            "yeongdo_seogu_exposure": sum(w for d, _, w in flat
                                         if d in {"Seo-gu", "Yeongdo-gu"}) / total,
            "exposure_gini": gini([w / total for w in weights.values()]),
            "district_coverage": sum(w > 0 for w in weights.values())
        })
    for row in output:
        row["relevance_retained"] = row["mean_relevance"] / output[0]["mean_relevance"]
        row["undercapture_gain_pp"] = 100 * (
            row["undercapture_exposure"] - output[0]["undercapture_exposure"])
    return output


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--attractions", type=Path,
                   default=ROOT / "data/processed/busan_attractions.csv")
    p.add_argument("--benchmark", type=Path,
                   default=ROOT / "experiments/equity/benchmark/development_queries.csv")
    p.add_argument("--signals", type=Path,
                   default=ROOT / "data/private/teos_primary_2024_2025.csv")
    p.add_argument("--expected", type=Path,
                   default=ROOT / "experiments/equity/results/rq3_policy_summary.csv")
    p.add_argument("--output", type=Path, default=ROOT / "work/rq3_reproduced")
    args = p.parse_args()
    paths = {name: getattr(args, name) for name in (
        "attractions", "benchmark", "signals", "expected")}
    for name, file in paths.items():
        if not file.is_file():
            p.error(f"Required {name} missing: {file} (private inputs must be supplied separately)")
    actual = compute(read_rows(args.attractions), read_rows(args.benchmark),
                     read_rows(args.signals))
    expected = read_rows(args.expected)
    if len(expected) != len(actual):
        raise SystemExit("Archived policy count mismatch")
    columns = ("mean_relevance", "undercapture_exposure", "candidate_exposure",
               "yeongdo_seogu_exposure", "exposure_gini", "relevance_retained",
               "undercapture_gain_pp")
    for a, b in zip(actual, expected):
        if float(b["lambda"]) != a["lambda"]:
            raise SystemExit("Policy lambda mismatch")
        for k in columns:
            if abs(a[k] - float(b[k])) > 1e-7:
                raise SystemExit(f"REPRODUCTION FAILED: lambda={a['lambda']} {k}")
        for k in ("query_count", "recommendations", "district_coverage"):
            if a[k] != int(b[k]):
                raise SystemExit(f"REPRODUCTION FAILED: lambda={a['lambda']} {k}")
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "rq3_policy_summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(actual[0]))
        writer.writeheader()
        writer.writerows(actual)
    hashes = {k: hashlib.sha256(file.read_bytes()).hexdigest() for k, file in paths.items()}
    (args.output / "input_hashes.json").write_text(
        json.dumps({"sha256": hashes, "verification": "all five policies match to 1e-7"},
                   indent=2) + "\n", encoding="utf-8")
    print("VERIFIED: 33 eligible queries, five policies, all archived summary values")
    print("lambda=0.8 exposure gain (pp):", round(actual[2]["undercapture_gain_pp"], 6))
    print("lambda=0.8 relevance retained:", round(actual[2]["relevance_retained"], 8))


if __name__ == "__main__":
    main()

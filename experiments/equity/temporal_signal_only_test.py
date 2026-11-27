#!/usr/bin/env python3
"""Historical-only score-specificity test. Requires a PRIVATE combined research JSON.

Measures persistence of a constructed *economic indicator*, NOT real tourist
relevance, business income or causal impact. Do not commit provider source data.
"""
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from sklearn.linear_model import LinearRegression


def compute(database):
    j = json.loads(Path(database).read_text(encoding="utf-8"))
    monthly = j["datasets"]["foreign_tourism_monthly"]["records"]
    attractions = j["datasets"]["attractions"]["records"]
    districts = sorted({r["district"] for r in monthly})
    if len(monthly) != 768 or len(attractions) != 207 or len(districts) != 16:
        raise ValueError("Expected 16 districts x 48 months and 207 attractions")
    if len({(r["district"], r["month"]) for r in monthly}) != 768:
        raise ValueError("Duplicate or missing district-month keys")
    counts = Counter(r["district"] for r in attractions)
    if set(counts) != set(districts):
        raise ValueError("District mismatch")
    values = defaultdict(lambda: defaultdict(lambda: [0.0, 0.0]))
    for row in monthly:
        period = "old" if int(row["year"]) <= 2023 else "new"
        v = float(row["foreign_visitors"])
        s = float(row["foreign_spending_million_krw"])
        if not np.isfinite(v) or not np.isfinite(s) or v < 0 or s < 0:
            raise ValueError("Invalid input")
        values[period][row["district"]][0] += v
        values[period][row["district"]][1] += s
    scores = {}
    for period in ("old", "new"):
        total_v = sum(v for v, _ in values[period].values())
        total_s = sum(s for _, s in values[period].values())
        scores[period] = []
        for d in districts:
            v, s = values[period][d]
            if v <= 0 or total_v <= 0 or total_s <= 0:
                raise ValueError("Undefined spending-to-activity share ratio")
            scores[period].append(max(0.0, 1.0 - (s / total_s) / (v / total_v)))
    historical = np.array(scores["old"])
    later = np.array(scores["new"])
    catalog = np.array([counts[d] for d in districts]).reshape(-1, 1)
    # All mapping parameters below are learned ONLY from 2022-2023.
    predicted_count = np.clip(LinearRegression().fit(catalog, historical).predict(catalog), 0, 1)
    predicted_mean = np.repeat(historical.mean(), len(districts))
    def mae(pred):
        return round(float(np.mean(np.abs(later - pred))), 6)
    return {
      "status": "exploratory, proxy-specific, NOT independent validation or spending effect",
      "district_count": len(districts),
      "historical": "2022-2023",
      "later_evaluation": "2024-2025",
      "mae_historical_city_average": mae(predicted_mean),
      "mae_historical_catalog_count_mapping": mae(predicted_count),
      "mae_historical_economic_signal_direct": mae(historical),
      "pearson_historical_later": round(float(np.corrcoef(historical,later)[0,1]),6),
      "limitations": [
        "Later-period target is the SAME constructed economic score, not actual SME income",
        "207-attraction catalog reflects saved snapshot, not certified as-of-2023 supply",
        "16 districts, one city; no independent tourist relevance or real-world causality",
        "Original provider data reuse and provenance still require source review"
      ]
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--database", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    x = ap.parse_args()
    result = compute(x.database)
    x.output.parent.mkdir(parents=True, exist_ok=True)
    x.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

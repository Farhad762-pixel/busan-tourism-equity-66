"""Reproduce a single-query API prototype demonstration, not the archived RQ3 study."""

import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.api.main import compare_recommendations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", default="sea cafe photography")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--equity-weight", type=float, default=0.20)
    parser.add_argument("--output", type=Path, default=ROOT / "work/mvp_demo.json")
    args = parser.parse_args()
    if not args.query.strip() or args.limit < 1 or not 0 <= args.equity_weight <= 1:
        parser.error("Use a nonblank query, positive limit and equity weight between 0 and 1")
    comparison = compare_recommendations(args.query, args.limit, args.equity_weight)
    # Only small derived ID/score outputs are saved, not source descriptions/images.
    payload = dict(experiment="single_query_attraction_distribution_prototype",
                   software={"python": platform.python_version(), **{
                       name: importlib.metadata.version(name)
                       for name in ("fastapi", "scikit-learn", "numpy", "scipy", "pydantic")}},
                   query=args.query, limit=args.limit, equity_weight=args.equity_weight,
                   data_sha256=hashlib.sha256((ROOT / "data/processed/busan_attractions.csv").read_bytes()).hexdigest(),
                   text_fields=["main_title", "subtitle", "place", "district", "address", "transport_info"],
                   baseline=[dict(id=r.id, district=r.district, relevance_score=r.relevance_score) for r in comparison.baseline],
                   equity_aware=[dict(id=r.id, district=r.district, relevance_score=r.relevance_score,
                                      equity_score=r.equity_score, final_score=r.final_score, equity_measure=r.equity_measure)
                                 for r in comparison.equity_aware],
                   baseline_unique_districts=comparison.baseline_unique_districts,
                   equity_aware_unique_districts=comparison.equity_aware_unique_districts,
                   limitation="Not the 33-query economic-undercapture study; no measured spending or travel effect")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"Baseline: {len(comparison.baseline)}, prototype: {len(comparison.equity_aware)}; saved {args.output}")


if __name__ == "__main__":
    main()

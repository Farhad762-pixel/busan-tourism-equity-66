#!/usr/bin/env python3
"""Recompute descriptive human relevance pilot summaries from privately held ratings.

Public source script: No private participant data is included with this repository.
Zero means cannot judge; exclude zero from rating summaries and policy comparison.
"""
from pathlib import Path
from collections import defaultdict
import csv
import math
import statistics
import json

OUT = Path(__file__).resolve().parent
KEY = OUT / "source/RESEARCHER_ONLY_POLICY_KEY.csv"
A = OUT / "source/Reviewer_A.csv"
B = OUT / "source/Reviewer_B.csv"

def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def write_csv(name, rows, fields):
    output = OUT / "results"
    output.mkdir(parents=True, exist_ok=True)
    with (output / name).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

def weight(rank):
    return 1.0 / math.log2(rank + 1)

def dcg(scores):
    return sum((2 ** (value - 1) - 1) * weight(rank)
               for rank, value in enumerate(scores, 1))

def weighted_mean(pairs):
    return sum(weight(rank) * value for rank, value in pairs) / sum(weight(rank) for rank, _ in pairs)

def main():
    if not all(p.exists() for p in (KEY, A, B)):
        raise SystemExit(
            "Private source files missing. Keep Reviewer_A.csv, Reviewer_B.csv and "
            "RESEARCHER_ONLY_POLICY_KEY.csv in experiments/human_relevance/source/ "
            "(never commit this directory)."
        )
    key = read_csv(KEY)
    a = {row["item_id"]: row for row in read_csv(A)}
    b = {row["item_id"]: row for row in read_csv(B)}
    assert len(key) == len(a) == len(b) == 61
    assert {x["item_id"] for x in key} == set(a) == set(b)
    rows = []
    for k in key:
        item_id = k["item_id"]
        ra, rb = int(a[item_id]["rating_1_to_5"]), int(b[item_id]["rating_1_to_5"])
        ca, cb = int(a[item_id]["confidence_1_to_3"]), int(b[item_id]["confidence_1_to_3"])
        assert 0 <= ra <= 5 and 0 <= rb <= 5
        assert 1 <= ca <= 3 and 1 <= cb <= 3
        paired = ra > 0 and rb > 0
        rows.append(dict(
            item_id=item_id, search=k["tourist_search"], rating_A=ra, rating_B=rb,
            rating_mean=(ra + rb) / 2 if paired else None, paired=paired,
            baseline_rank=k["baseline_rank"], equity_rank=k["equity_rank"]
        ))
    both = [r for r in rows if r["paired"]]
    n = len(both)
    xa, xb = [r["rating_A"] for r in both], [r["rating_B"] for r in both]
    exact = sum(x == y for x, y in zip(xa, xb)) / n
    near = sum(abs(x - y) <= 1 for x, y in zip(xa, xb)) / n
    matrix = [[sum(x == i and y == j for x, y in zip(xa, xb))
               for j in range(1, 6)] for i in range(1, 6)]
    marginal_a = [sum(row) for row in matrix]
    marginal_b = [sum(matrix[i][j] for i in range(5)) for j in range(5)]
    obs = sum(((i - j) / 4) ** 2 * matrix[i][j]
              for i in range(5) for j in range(5)) / n
    exp = sum(((i - j) / 4) ** 2 * marginal_a[i] * marginal_b[j] / n
              for i in range(5) for j in range(5)) / n
    kappa = 1 - obs / exp

    groups = defaultdict(list)
    for r in rows:
        groups[r["search"]].append(r)
    summary, policies = [], []
    for search, items in sorted(groups.items(), key=lambda kv: kv[0].casefold()):
        jointly = [r for r in items if r["paired"]]
        ava = [r["rating_A"] for r in items if r["rating_A"] > 0]
        avb = [r["rating_B"] for r in items if r["rating_B"] > 0]
        complete = len(jointly) == len(items)
        summary.append(dict(
            search=search, n_items=len(items), rated_A=len(ava), rated_B=len(avb),
            paired_count=len(jointly), cannot_judge_A=len(items) - len(ava),
            cannot_judge_B=len(items) - len(avb),
            mean_A=round(statistics.mean(ava), 4),
            mean_B=round(statistics.mean(avb), 4),
            paired_mean=round(statistics.mean(r["rating_mean"] for r in jointly), 4) if jointly else "",
            exact_agree_count=sum(r["rating_A"] == r["rating_B"] for r in jointly),
            full_rank_valid=int(complete)
        ))
        p = dict(search=search, fully_judged=complete, n_union=len(items),
                 reason="" if complete else "At least one 0 (cannot judge)")
        if complete:
            for label, rank_col in (("baseline", "baseline_rank"), ("equity", "equity_rank")):
                ranking = sorted(
                    ((int(r[rank_col]), r["rating_mean"]) for r in items if r[rank_col]),
                    key=lambda pair: pair[0]
                )
                scores = [score for _, score in ranking]
                ideal = dcg(sorted((r["rating_mean"] for r in items), reverse=True)[:10])
                p[label + "_weighted_mean"] = weighted_mean(ranking)
                p[label + "_ndcg"] = dcg(scores) / ideal if ideal else 0
                p[label + "_list_size"] = len(ranking)
            p["human_weighted_delta"] = p["equity_weighted_mean"] - p["baseline_weighted_mean"]
            p["ndcg_delta"] = p["equity_ndcg"] - p["baseline_ndcg"]
        policies.append(p)
    write_csv("search_level_summary.csv", summary, list(summary[0]))
    fields = ["search", "fully_judged", "n_union", "reason", "baseline_weighted_mean",
              "equity_weighted_mean", "human_weighted_delta", "baseline_ndcg", "equity_ndcg",
              "ndcg_delta", "baseline_list_size", "equity_list_size"]
    write_csv("policy_comparison_complete_case.csv", policies, fields)
    complete = [p for p in policies if p["fully_judged"]]
    stats = dict(
        n_items=len(rows), n_queries=len(groups),
        rated_A=sum(r["rating_A"] > 0 for r in rows),
        zero_A=sum(r["rating_A"] == 0 for r in rows),
        rated_B=sum(r["rating_B"] > 0 for r in rows),
        zero_B=sum(r["rating_B"] == 0 for r in rows),
        mean_A=statistics.mean(r["rating_A"] for r in rows if r["rating_A"] > 0),
        mean_B=statistics.mean(r["rating_B"] for r in rows if r["rating_B"] > 0),
        n_paired=n, exact_pct=100 * exact, within_1_pct=100 * near,
        mean_abs_diff=statistics.mean(abs(x-y) for x,y in zip(xa,xb)),
        quadratic_kappa=kappa, n_fully_judged=len(complete),
        fully_judged_queries=[p["search"] for p in complete],
        excluded_queries=[p["search"] for p in policies if not p["fully_judged"]],
        baseline_human_weighted_mean=statistics.mean(p["baseline_weighted_mean"] for p in complete),
        equity_human_weighted_mean=statistics.mean(p["equity_weighted_mean"] for p in complete),
        human_retention=(statistics.mean(p["equity_weighted_mean"] for p in complete) /
                         statistics.mean(p["baseline_weighted_mean"] for p in complete)),
        baseline_ndcg=statistics.mean(p["baseline_ndcg"] for p in complete),
        equity_ndcg=statistics.mean(p["equity_ndcg"] for p in complete),
        n_incomplete=len(groups) - len(complete),
        n_major_disagree=sum(abs(x-y) > 1 for x,y in zip(xa,xb))
    )
    (OUT / "results" / "statistics.json").write_text(
        json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    main()

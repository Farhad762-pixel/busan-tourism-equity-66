# Human-rated recommendation relevance — exploratory pilot

**Date:** 2026-11-13 · **Status:** completed small pilot, NOT a final user study.

This experiment asked two independent volunteers (as reported by the researcher) to judge how relevant attractions were to six tourist searches, using the union of the baseline and economic-equity recommendation top lists. Reviewers were shown item descriptions without the recommendation policy or rank. Each provided a 1–5 relevance score or **0 = cannot judge**, plus confidence 1–3.

## Public results

- [Professor-ready methodological report](../../docs/research/HUMAN_RELEVANCE_PILOT_2026-11-13.md)
- [Search-level aggregate ratings](results/search_level_summary.csv)
- [Complete-case baseline/equity comparison](results/policy_comparison_complete_case.csv)
- [Machine-readable aggregate statistics](results/statistics.json)
- [Calculation script](compute_human_pilot.py) — requires *separately held private* A/B response files and ranking key.

## Scope and interpretation

- **61** distinct query-attraction pairs across six searches; both reviewers responded to all 61.
- **52** had both reviewers supply a valid 1–5 rating.
- **3 of 6 searches** were completely judgeable and enter the strict full-ranking comparison.
- On those three, baseline human-rated rank-weighted relevance was **3.849/5**; equity policy λ=0.8 was **3.859/5**.
- Difference **+0.010/5**, not evidence of statistical superiority or equivalence. The earlier **99.06%** TF-IDF similarity retention is a different metric over 33 valid queries, not a human study.
- The pilot exposes relevance problems for "local market" and "photography walk"; a larger held-out evaluation is needed.

## Reproduction

The public script uses only standard-library Python and expects privately stored files:

```text
experiments/human_relevance/
  compute_human_pilot.py
  source/                         # NOT publicly committed
    Reviewer_A.csv
    Reviewer_B.csv
    RESEARCHER_ONLY_POLICY_KEY.csv
```

The original private source files and script have already been rerun in an isolated directory, reproducing the published aggregate JSON and CSVs. Future collaborators can rerun only after receiving the inputs through an approved private mechanism.

**Privacy and ethics:** Do not put individual ratings, confidence scores, policy/rank key, original respondent files, or workbook with item-level tabs on public GitHub. Check voluntary consent, relevant ethics/IRB requirements and your supervisor's guidance before disseminating human-subject findings. No identifying demographics are present in the public aggregates.

**Limits:** Two reviewers, six searches, 0="cannot judge" is excluded, and complete-case exclusion may bias results. No actual spending, travel or satisfaction was measured.

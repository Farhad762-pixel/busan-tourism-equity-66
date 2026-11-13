# Human relevance evaluation — exploratory six-search pilot

**Project:** Algorithmic Visibility and Tourism Spending Inequality: Economic-Equity-Aware Tourism Recommendation for Busan  
**Pilot completed:** 13 November 2026  
**Status:** Exploratory two-reviewer pilot, **not final validation**.

## Motivation

The saved offline re-ranking experiment retained 99.06% of baseline **TF-IDF similarity relevance** over 33 queries at λ=0.8. Text similarity is not the same as a person's judgment of tourist relevance. This pilot therefore evaluates relevance as judged by two people on a smaller six-query sample.

## Design

Six searches were selected using a recorded random seed (20261113) from six of the eligible intent categories. The 61 distinct query–attraction pairs represent the union of top results from baseline and equity-aware recommendations. Each reviewer saw searches and attraction metadata but not algorithm/policy labels or ranking positions.

Each item received relevance 1–5, with **0 = cannot judge**, and confidence 1–3. Zero is treated as **missing**, never imputed or recoded as low relevance. Each score is independently retained in the researcher's private records.

Only searches where **both** reviewers provided valid ratings for **every** item in that search's two-policy union enter the strict policy-ranking comparison. Per-search rank-weighted means use `1/log2(rank+1)`. nDCG@10 uses the highest-rated elements of the **judged union** for the ideal ordering; it does not assess the entire original attraction collection.

## Data completeness

| Measure | Reviewer A | Reviewer B |
|---|---:|---:|
| Items answered | 61 | 61 |
| Valid 1–5 ratings | 54 | 59 |
| Cannot judge (0) | 7 | 2 |
| Average of valid ratings | 2.96/5 | 3.00/5 |

There were **52** items with two valid 1–5 judgments. Reviewer averages use different judged subsets, so a comparison between reviewers' averages is not a within-item rater-effect estimate.

## Inter-reviewer agreement (52 paired usable items)

- Exact agreement: **18/52 (34.6%)**.
- Difference ≤1 rating point: **41/52 (78.8%)**.
- Mean absolute difference: **0.942** rating points.
- Quadratic-weighted Cohen's κ: **0.490** (descriptive; sensitive to category prevalence).
- **11** jointly judged items differed by at least two points.

## Search-level findings

| Search | Total items | Both rated 1–5 | Mean paired relevance /5 | Full policy comparison |
|---|---:|---:|---:|---|
| Night view | 5 | 5 | 4.20 | Yes |
| Korean history | 10 | 10 | 3.75 | Yes |
| Ocean view | 9 | 9 | 3.61 | Yes |
| Art village | 12 | 11 | 2.91 | No |
| Photography walk | 13 | 8 | 2.31 | No |
| Local market | 12 | 9 | 2.22 | No |

Means use only items with two valid ratings. The weak market and photography results suggest a semantic mismatch and/or incomplete attraction descriptions, **not** proven consumer dissatisfaction.

## Strict fully judged policy comparison (3 of 6 searches)

| Outcome | Baseline | Equity-aware (λ=0.8) |
|---|---:|---:|
| Rank-weighted human relevance /5 | **3.849** | **3.859** |
| nDCG@10 vs ideal within judged union | **0.818** | **0.849** |

The rank-weighted human relevance difference was **+0.010/5** (equity/baseline ratio 100.26%). The difference is tiny and **has not been established as statistically meaningful**. Three queries were excluded for having one or more cannot-judge entries, making complete-case selection important.

Do not equate this comparison to the earlier 99.06% TF-IDF retention over the separate, larger, 33-query evaluation. This pilot does **not** establish equality, non-inferiority, superiority or real tourist satisfaction.

## Limitations and research safeguards

1. Only two reviewers and six searches; no representative sample of foreign tourists.
2. Reviewer independence and consent are based on the researcher's collection workflow, not independently validated in the saved files.
3. Multiple attraction records had missing, vague or ambiguous descriptive text.
4. The strict complete-case comparison includes only three queries and may be selected by the pattern of missing judgments.
5. No route-based travel times, observed visits, revenue or causal effects were tested.
6. Check with the supervisor about ethics/IRB approval, consent and participant data handling before journal publication.

## Next iteration

- Improve intent/type filtering (especially local markets) and verified metadata for photography/walking queries.
- Review the 11 substantial disagreement cases **privately**, without revising submitted scores.
- Reserve a **new, held-out** set of tourist searches and attraction candidates before algorithm tuning.
- Recruit more blinded independent judges, preregister metrics and missing-data rules when practical, and report uncertainty.

## Public result files

- [Search-level aggregates](../../experiments/human_relevance/results/search_level_summary.csv)
- [Policy comparison over complete-case queries](../../experiments/human_relevance/results/policy_comparison_complete_case.csv)
- [Summary statistics](../../experiments/human_relevance/results/statistics.json)
- [Researcher-only reproducibility instructions](../../experiments/human_relevance/README.md)

**Publication restriction:** Raw respondent spreadsheets, pair-level ratings, private ranking key and analysis workbook with item-level tabs remain outside this public repository.

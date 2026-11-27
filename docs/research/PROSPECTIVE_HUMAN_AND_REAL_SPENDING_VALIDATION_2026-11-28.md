# Prospective evidence validation — human relevance and real spending (28 November 2026)

## Current decision

Three distinct research claims have different requirements:

| Claim | Current status |
| --- | --- |
| Economic undercapture ranking beats geographic balancing | **Not demonstrated**; V2 economic policy 63.74% vs inverse attraction-count 64.43% on previously used development queries; later economic score-weighted exposure practically tied |
| Search V2 yields genuinely useful tourist recommendations | **Not independently validated**; no new human V2 judgments. Search V2 returns no strict-supported attraction for 19/36 prior development searches |
| Recommendation algorithm causes greater local spending | **Not identifiable from existing data**; the 2022–2025 Busan panel contains no treatment/control exposure to the experimental recommender or observed post-treatment outcomes |

## What has been created outside public GitHub

A privacy-conscious, offline three-policy pilot app (A relevance, B attraction count, C historical economic) using earlier development queries; anonymous voluntary chosen-item/rating/optional *self-reported* post-visit spending export; separate human blind-rating forms; descriptive analysis with tests; and a professor-ready evidence protocol. The offline pilot does not verify receipts or identify actual economic impact. **Source-derived attraction descriptions, participant data, private combined JSON and raw Data Lab exports are intentionally not committed publicly.**

## Required confirmatory relevance experiment

1. Freeze genuinely new tourist queries provided by travelers before algorithms are run, with hash and protocol.
2. Compare fixed A/B/C rankings with identical candidates and matched relevance budgets, select parameters on development only.
3. Obtain independent blind judgments with 1–5 ratings and 0='cannot judge' and decide a missing-data rule in advance.
4. Report mean human nDCG@10, all-query coverage including zero-result queries, uncertainty and interrater agreement.

## Required real-world spending experiment

1. After supervisor/IRB decision, deploy a real randomized assignment service for consenting tourists (not an offline demo) with one fixed A/B/C treatment per participant/trip.
2. Measure *post-exposure* district spending with valid consented, attributable evidence (e.g., verified de-identified receipts or merchant transaction records), with documented missingness and no raw identifiers in public records.
3. Preregister control comparisons C vs B and C vs A, primary district-spending estimand, follow-up window, sample-size/power method, and intention-to-treat analysis.
4. Only use causal impact wording if the trial is actually run and its identification/measurement standards met; a self-reported amount or a change in aggregated district spending alone is insufficient.

## Publication position

The best supported present manuscript is a reproducible **offline economic-equity-aware attraction re-ranking feasibility study**, reporting mixed comparator results and no claim of tourist satisfaction or spending impact.

Related examples of evaluation standards:
- https://doi.org/10.1007/s10791-020-09371-3
- https://doi.org/10.1002/aaai.12051
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10138512/

**Never convert the three 'not established' statuses to 'completed' without new human/field observations.**

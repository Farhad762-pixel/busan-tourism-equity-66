# Search V2 + economic re-ranking: exploratory development results (28 November 2026)

**Status:** A local repeatable experiment using the researcher's saved combined JSON and the November 28 offline V2 retrieval snapshot. These are **NOT independent human relevance results**, **NOT an untouched hold-out**, and **NOT real tourist visits or spending changes**. These aggregate metrics are being proposed for supervisor review only.

## What was done

- 207 official Busan attractions; 768 district-month observations for 16 districts (2022–2025).
- New V2 source-evidence-aware **strict supported results only**, same candidate pool for all four ranking policies, up to 50 candidates and top 10 displayed.
- District economic signal derived from 2022–2023 visitor/spending shares. Targeting assessed against the same indicator recomputed for 2024–2025 (retrospective alignment, not a measured effect on 2024–2025 spending).
- Original 48 research development searches used for selecting each policy's largest lambda in 0–2 (step 0.05) passing >=99% of the *model's own V2 search score* on development queries.
- **36 previously inspected** natural-language queries used for diagnostic comparison, **not new untouched queries**.
- Policies: (A) relevance only; (B1) inverse catalog attraction count; (B2) inverse baseline developmental district exposure; (C) historical economic-under-capture weighting.
- Rank-weighted exposure uses `1/log2(rank+1)`. No real-time routes, tourist clicking, independent relevance judgment or local-business income measured.

## Actual results on the 36 inspected searches

| Algorithm | Selected lambda | Exposure to districts with later positive undercapture | V2 model-score retention | Exposure Gini | Queries with >=1 supported match |
|---|---:|---:|---:|---:|---:|
| A — Relevance only | 0 | 54.65% | 100.00% | 0.4638 | 17/36 |
| B1 — Inverse attraction count | 1.95 | **64.43%** | 99.97% | 0.4481 | 17/36 |
| B2 — Exposure balancing | 1.90 | 60.63% | 99.91% | **0.4201** | 17/36 |
| C — Economic historical score | 0.65 | 63.74% | 99.98% | 0.4652 | 17/36 |

A total of **19/36** queries returned *no strict source-supported* attraction, and only **5/36** had >=5 supported attractions. The policy comparisons re-rank **67** supported recommendation placements in total. All four share exactly the same candidate availability.

## Falsifiable conclusion — economically weighted model is NOT clearly superior here

- On the later economic-score-weighted exposure index, C minus B1 is only **+0.000098** (descriptive paired query-bootstrap 95% interval **[-0.00343, +0.00341]**, 1,500 resamples). **No reliable difference is established.**
- C minus B2 on that same index is **+0.02990** (descriptive interval **[+0.00605, +0.05765]**), but the index itself is defined using the economic score and thus favors economic targeting by construction.
- B2 yields lower exposure Gini than C; C does **not** improve every ranking objective.
- A random assignment diagnostic (500 shuffled historical district labels) suggests the historical score has specific later-period alignment. But both measures belong to the same indicator family: this is **not independent economic welfare validity**.
- Original archived +13.74 percentage-point exposure gains and 99.06% TF-IDF text-similarity retention belong to the **old TF-IDF** retrieval experiment and are **not V2 results**.
- Critically, **V2 model-score retention does not establish human relevance or tourist satisfaction.**

## Independent relevance protocol is prepared but not completed

In the separate local evidence pack, a browser-only blind-rating form presents query/title/English place/official subtitle without policy names, district economic weights, or ranking positions. A quick pilot has 12 development queries and 69 query–attraction pairs; the full development form contains all 36 queries and 201 pairs. The key linking policies to attraction ranks is private and should never be given to raters. No participant judgments have been fabricated or collected.

When actual independent reviewers submit ratings (with appropriate supervisor consent/ethics review), the offline scoring script requires two separate anonymous reviewer codes and computes fixed-denominator top-10 human relevance and nDCG@10 on complete judged unions.

**Publication gating:** improve attraction source coverage; collect independently rated relevance on genuinely new and frozen tourist searches; compare all policies on matched candidates and independently rated quality; validate the economic proxy against credible external economic context; report uncertainty, null results and limitations. A null finding against a geographic baseline can be scientifically useful if rigorously tested.

**Reproduction note:** Local analyst scripts and aggregate figure files are included in the researcher-facing evidence pack provided in the conversation, not yet all committed to GitHub. The local snapshot from the prior search-quality ZIP and the GitHub review implementation may differ; rerun on the chosen final code before merging. Private tourism source data and participant responses remain outside public GitHub.
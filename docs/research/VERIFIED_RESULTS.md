# Verified research findings (snapshot: November 2026)

This page summarizes computations from the saved research checkpoint and separately rerun offline experiment. Values are **simulated recommendation measurements**, not measured downstream tourist behavior.

## Data quality and scope

- **16** Busan districts; **48** months (Jan 2022–Dec 2025); **768** unique district-month observations.
- **207** official attractions with coordinates and district labels.
- RQ2/RQ3 benchmark: **33** eligible queries drawn from 48 predefined, across **12** tourist-intent categories.

## RQ1 — Visitor/spending association

- Haeundae-gu: **29.89%** of recorded foreign tourism spending over 2022–2025.
- Busanjin-gu: **26.89%**; combined **56.78%**.
- Pooled district-month Pearson visitor/spending correlation: **0.5726**; Spearman **0.7242**.
- These are descriptive, not evidence that recommendations caused geographic inequality.

## RQ2 — Baseline visibility audit

The saved baseline experiment reported Pearson **0.4566** between district exposure share and existing spending share, and Pearson **−0.3975** between exposure and the undercapture indicator. Associations are across districts in the controlled model.

## RQ3 — Main policy comparison

| Policy | Exposure to undercapturing districts | Gain vs baseline (percentage points) | Text relevance retained | Exposure Gini |
| --- | ---: | ---: | ---: | ---: |
| Baseline λ=0 | 56.41% | 0.00 | 100.00% | 0.3263 |
| λ=0.5 | 65.95% | +9.55 | 99.65% | 0.3070 |
| **λ=0.8** | **70.14%** | **+13.74** | **99.06%** | **0.2983** |
| λ=1.0 | 71.53% | +15.13 | 98.62% | 0.2975 |
| λ=2.0 | 77.01% | +20.60 | 95.68% | 0.3279 |

At λ=0.8, exposure to the five screened candidate districts changed **30.06% → 39.01%** (+8.95 percentage points), and Seo-gu + Yeongdo-gu changed **15.95% → 21.38%** (+5.44 points). Total district coverage stayed **15/16** in both baseline and λ=0.8.

Positive undercapture exposure gain was observed across all **12** eligible tourist categories. These categories have unequal query counts, so the result is descriptive.

**Important:** A +13.74 percentage-point *exposure* gain does not mean a +13.74% revenue gain. Text similarity retained is not user satisfaction.

## RQ3 — 15 km straight-line accessibility sensitivity

| Origin | Baseline undercapture exposure | Equity exposure | Gain (percentage points) |
| --- | ---: | ---: | ---: |
| Busan Station | 64.16% | 74.72% | +10.56 |
| Seomyeon Station | 61.89% | 73.82% | +11.93 |
| Haeundae Station | 49.52% | 60.15% | +10.64 |

The eligible query count varies by origin (30, 32, 27 respectively). These are **distance limits**, not route-based convenience measures. Check raw comparison tables in the local GitHub-ready archive before final publication.

## Next needed evidence

Independent tourist relevance judgments, actual travel times, larger/multilingual benchmarks, scholarly literature review, source redistribution terms, and supervisor review.

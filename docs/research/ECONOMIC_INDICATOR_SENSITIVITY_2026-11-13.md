# RQ3 economic-undercapture sensitivity, 13 November 2026

**Status:** supplementary offline robustness test from the saved research checkpoint. Not independent validation and not observed tourism impact.

## Study held constant
- 207 official Busan attractions; 33 previously eligible tourist searches.
- TF-IDF cosine baseline, positive-match eligibility, top 50 re-ranking pool, up to 10 displayed results, rank weight 1/log2(rank+1).
- Economic bonus: `relevance × [1 + 0.8 × max(0, 1 − spending_share / visitor_share)]`.
- Only the years and population used to **calculate district economic scores** changed.

## Result summary

| Economic signal | Gain for positive-undercapture districts | Gain for original five candidate districts | Baseline text relevance retained | District-exposure Gini after |
|---|---:|---:|---:|---:|
| 2024–2025, all districts (main) | **+13.74 percentage points** | +8.95 pp | **99.06%** | 0.2983 |
| 2022–2023, all districts | +13.08 pp | +8.10 pp | 99.20% | 0.3207 |
| 2022–2025, all districts | +13.73 pp | +8.94 pp | 99.06% | 0.3035 |
| 2024–2025, Gangseo excluded from economic normalization | +14.10 pp | +9.83 pp | 99.04% | 0.3181 |

Baseline district-exposure Gini was **0.3263** in each scenario. The initial five districts were held fixed for comparison: Dong-gu, Geumjeong-gu, Nam-gu, Seo-gu and Yeongdo-gu. In the Gangseo stress test, Gangseo was excluded from **economic-share denominator calculations and assigned zero bonus**, but its attractions stayed eligible for ranking.

## Scientific interpretation
The directional gain in **simulated rank-weighted exposure** persists when the economic period or Gangseo normalization is changed, with at least 99% of baseline **text-similarity** relevance retained. However, the amount of Gini reduction changes, indicating sensitivity in the precise geographic distribution. The main 2024–2025 experiment reproduces the archived numerical results.

**Do not infer:** additional visits, visitor satisfaction, actual income for small businesses, effects caused by airport traffic, or a reduction in economic inequality. Estimated foreign visitor activity is not a count of unique tourists and foreign-card consumption is not all spending. This was evaluated with the same 33 development queries, not an untouched test set. The direct effect of airport-related activity remains unverified.

## Next steps
1. Supervisor review of measure validity, data-source definitions and private-data reuse rights.
2. Ethics/consent approval as applicable, followed by real responses in the new blinded human-rating evaluation.
3. Independent held-out queries and integration of the verified results into the final manuscript.

This is an **append-only research progress note**, supplementing, not overwriting, earlier RQ3 results. Reproducible local script and CSV exports were prepared separately; underlying original raw data were not published.

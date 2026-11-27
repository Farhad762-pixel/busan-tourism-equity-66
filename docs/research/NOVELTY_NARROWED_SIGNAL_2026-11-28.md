# Added economic-signal specificity test — 28 November 2026

**Paper:** Algorithmic Visibility and Tourism Spending Inequality: An Economic-Equity-Aware Re-ranking Framework for Busan.

**Finding:** In the saved 16-district dataset, the 2022–2023 economic-undercapture indicator matches the 2024–2025 undercapture pattern much more closely than an attraction-count-only baseline calibrated using 2022–2023 data. No later-period outcomes were used to set the three predictors.

| Predictor from pre-2024 information | MAE against later undercapture (smaller is better) |
|---|---:|
| Historical citywide average | **0.290758** |
| Attraction-count model fit on historical period | **0.239215** |
| Historical economic-undercapture score directly | **0.060933** |

This is a new **within-indicator, cross-period stability and specificity diagnostic**: the outcome is the same spending-share versus visitor-activity-share proxy recalculated later. It is **not** a measure of external welfare, true business need, a field outcome, independent tourist satisfaction, or proof of a unique first algorithm. One catalog snapshot is used; as-of-2023 item availability is not independently confirmed.

**Reproduce:** `python experiments/equity/temporal_signal_only_test.py --database /private/path/busan_research_database.json --output /tmp/summary.json`. Do not commit that private JSON without license review.

**Already reproduced old offline result:** economic policy λ=0.8 reallocates simulated exposure to positive-undercapture districts from **56.41% to 70.14%** with **99.06% retained TF-IDF cosine score** on 33 development queries. With newer retrieval, the economic policy is **not superior** to catalog-count balancing (63.74% versus 64.43% undercapturing-district exposure). Its text score does not measure real human preference.

**Closest literature, which limits novelty claims:** [Hong et al., 2023](https://doi.org/10.2298/CSIS220620002H) already uses card transactions in tourism recommendation; [Salmony et al., 2026](https://doi.org/10.3233/FAIA250570) already includes economic sustainability criteria in POI evaluation; [Sánchez et al., 2023](https://doi.org/10.1007/s10618-022-00913-5) studies geographic recommender bias; [Onder et al., 2026](https://doi.org/10.1177/13548166261488140) describes the contingent chain from algorithmic visibility to spending. A targeted search does not prove worldwide novelty.

**Defensible candidate contribution:** Testing a specific within-city district economic-undercapture **policy signal** in an interpretable Busan attraction re-ranking framework, with controlled offline trade-offs and retrospective indicator specificity compared with attraction availability. The claim is an empirical **feasibility study**, not demonstrated spending increase.

**Still genuinely unresolved:** blinded human judgments; independent fresh tourist searches; source-reuse rights and professor methodological approval; actual transit/route feasibility; and real randomized tourist exposure followed by consented, verified spending outcomes if causal spending impact is asserted. These cannot be inferred from historic district spending or fabricated ratings. 

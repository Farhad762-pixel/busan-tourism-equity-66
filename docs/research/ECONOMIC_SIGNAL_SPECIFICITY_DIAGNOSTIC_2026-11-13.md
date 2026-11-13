# Economic-signal specificity and retrospective temporal targeting (13 November 2026)

**Paper:** Economic-Equity-Aware Re-ranking for Intra-Urban Tourism Recommendations: Evidence from Busan, South Korea

**Status:** An **exploratory diagnostic** for the existing single research paper; it does not claim worldwide novelty, observed tourist impact, or a new invention in ranking fairness. Original research files and previous versions are preserved.

## A narrower contribution

Tourism and Korean card-transaction recommendation, multistakeholder urban-POI re-ranking, geographic fairness and exposure constraints are existing topics (Hong, Chung & Koo 2023; Merinov & Ricci 2024/2026; Sánchez, Bellogín & Boratto 2023; Lopes et al. 2024). We ask a more specific question: **Does a district visitor-activity-share versus foreign-card-spending-share mismatch signal direct more simulated exposure to economically undercapturing districts than a simple attraction-catalog diversification control?**

The original claim that economic-need re-ranking increases attention to economic-need districts is partly built into the algorithm. Independent controls make it more interesting and falsifiable, though **these controls do not establish real economic value**.

## Data and method

- Historical information: 2022–2023 district estimated foreign-visit activity and recorded foreign-card tourism consumption.
- Later measurement: the **same type** of district score recomputed for 2024–2025. It is used to **evaluate alignment**, not as observed tourist spending changes.
- Unchanged prior model: 207 official Busan attractions, **33 previously used development search queries**, TF-IDF relevance, 50 positive-relevance candidates, at most 10 top recommendations, logarithmic rank discount and λ = 0.8.
- Comparator: inverse official attraction-catalog count, normalized to [0,1], applied in the same multiplier at the same λ. This is only a simple diversification control; alternative fairness algorithms may perform differently.
- Negative control: 2,000 seeded random reassignments of historical economic-need scores among 16 district labels, preserving the values but removing their geographic correspondence.
- All outputs are **offline rank simulations**. The scores and search policy were already seen during prior development, so this is **not** prospective independent validation.

## New exploratory outputs

| Ranking policy | Rank-weighted exposure to districts with positive 2024–2025 undercapture | TF-IDF relevance retained | 2024–2025 score-weighted exposure index |
|---|---:|---:|---:|
| Relevance-only baseline | 56.41% | 100.00% | 0.3700 |
| **2022–2023 economic signal** | **69.49%** | **99.20%** | **0.4704** |
| 2024–2025 economic signal (contemporaneous comparison) | 70.14% | 99.06% | 0.4695 |
| Inverse attraction-count control | 63.35% | 99.61% | 0.4115 |

The historic economic-score model increased the share of later-positive-need districts by **13.08 percentage points** versus the baseline. The simple catalog-supply control gained **6.94 percentage points** at the same nominal λ. Equal λ does not guarantee equal reduction in relevance, so this is **not** a definitive comparison of algorithm efficiency.

Across 16 districts, historical versus later economic-undercapture scores had Pearson correlation **0.971** and Spearman correlation **0.967**. This indicates stability of the constructed score, **not predictive validity of later spending or a causal effect**.

For 2,000 random label assignments the mean *later-score-weighted exposure index* was **0.3727**, with the empirical central 95% interval **[0.3219, 0.4274]**. The actual 2022–2023 score produced **0.4704**. The adjusted fraction of random assignments at least as high was **1/2001 (~0.0005)**. This is an **informal randomization diagnostic, not a causally interpretable p-value**: the same score family is used across periods, the 33 searches and λ were development choices, and ranking outcomes are not human outcomes.

## Refined gap statement for the paper

> This research does not introduce urban tourism fairness or credit-card-informed recommendation. It evaluates a **specific district economic-undercapture construction** as a ranking policy signal and contrasts its *retrospective, later-period targeting specificity* against an attraction-supply re-ranking rule and randomized district assignments in a controlled Busan attraction recommender. The resulting contribution is a transparent feasibility study, not a claim that algorithmic exposure has increased local economic benefits.

## Relevant prior work

1. Hong, M., Chung, N., & Koo, C. (2023). *Tourism Recommendation based on Word Embedding from Card Transaction Data.* [doi:10.2298/CSIS220620002H](https://doi.org/10.2298/CSIS220620002H)
2. Merinov, P., & Ricci, F. (2026). *Positive-sum impact of multistakeholder recommendations for urban tourism.* [doi:10.1016/j.asoc.2026.114582](https://doi.org/10.1016/j.asoc.2026.114582)
3. Sánchez, P., Bellogín, A., & Boratto, L. (2023). *Bias characterization, assessment, and mitigation in location-based recommender systems.* [doi:10.1007/s10618-022-00913-5](https://doi.org/10.1007/s10618-022-00913-5)
4. Lopes, R., Alves, R., Ledent, A., Santos, R.L.T., & Kloft, M. (2024). *Recommendations with minimum exposure guarantees: A post-processing framework.* [doi:10.1016/j.eswa.2023.121164](https://doi.org/10.1016/j.eswa.2023.121164)
5. Salmony, M.Y., Moreno, A., & Valls, A. (2026). *Towards Sustainable Tourism: A Novel Comprehensive Hierarchical Multi-Criteria Evaluation Framework for Points-of-Interest Recommendations.* [doi:10.3233/FAIA250570](https://doi.org/10.3233/FAIA250570)
6. Tokarchuk, O., & Gabriele, R. (2026). *Placebo analysis for causal inference in tourism.* [doi:10.1016/j.tourman.2025.105360](https://doi.org/10.1016/j.tourman.2025.105360)

**Full-text review and citation-chain searches are still required** before claiming this exact problem has not been studied elsewhere.

## Next steps
1. Validate source definitions and source-data reuse permissions; keep original tourism data private for now.
2. Ask the supervisor whether this narrower empirical contribution is meaningful, and compare to stronger geographic fairness baselines under matched human-rated relevance.
3. Collect genuine second-round blinded human ratings only after ethics/consent approval where applicable. No ratings from that round have been filled in or generated.
4. Test the fixed protocol on new, untouched searches (the old 33 and later 12 exploratory queries are already development material).
5. Do not describe the scores as unique tourist counts, realized spending, downstream demand or PR-ready field outcomes.

The local reproduction script consumes the privately held checkpoint ZIP and outputs **derived aggregate summaries**; it is not necessary to publish restricted source data in order to share this research note.

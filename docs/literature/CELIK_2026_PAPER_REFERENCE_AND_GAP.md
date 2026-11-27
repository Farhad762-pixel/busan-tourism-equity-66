# Close-paper evidence note: Çelik et al. (2026) and the Busan economic-equity study

**Evidence status:** Original 12-page PDF read and Table 2 and conclusion checked on 27 Nov 2026. This note is a structured reference, **not** an independently established literature-wide novelty claim or new Busan experiment.

## Full bibliographic reference

Çelik, F., Banerjee, A., & Wörndl, W. (2026). *Sustainable Tourism through Locality-Aware Recommendations.* In *Joint Proceedings of the ACM UMAP 2026 Workshops* (CEUR Workshop Proceedings, Vol. 4206, pp. 379–390). https://ceur-ws.org/Vol-4206/UMAP4GOOD-5.pdf

Proceedings table of contents: https://ceur-ws.org/Vol-4206/

## Paper question in very simple language

Can a recommendation system show more restaurants associated with geographically local Yelp reviewers, while still producing useful recommendations?

**Do not confuse:** *locality* (reviewer activity concentrated in a city) with *economic undercapture* (spending share relative to visitor-activity share). Neither directly measures a restaurant's income or need.

## Findings that the original paper supports

| Claim | Exact original source | Plain meaning and safe interpretation |
|---|---|---|
| A continuous, city-relative locality signal is derived from Yelp reviewers' geographic review histories | Abstract; §3.2, PDF pp. 1, 4–5 | Authors calculate restaurant-locality using reviewer behavior; they do not verify actual residence or business profitability |
| Locality added to popularity and proximity using a weighted, transparent ranking function | §3.3–3.4, PDF pp. 5–6 | A tunable score changes which restaurants appear near the top |
| Locality and popularity are weakly correlated: Pearson r=0.027, Spearman rho=0.075 | §5, PDF p. 8 | The locality variable is not simply their popularity proxy under these correlation measures |
| At top-10 balanced beta=.5, adding alpha=.2: EPC 0.0035 to 0.0085 (+142.9%); nDCG 0.0352 to 0.0258 (-26.7%) | Table 2, PDF p. 9 | Novelty improves, while held-out interaction ranking quality declines; not an economic benefit estimate |
| Same condition: locality share 0.04 to 0.50; item coverage 0.0194 to 0.0215; geographic spread 1.43 to 1.33 km | Table 2, PDF p. 9 | Local orientation and catalog coverage rise slightly, but spread decreases in THIS condition; higher locality weight does not improve every metric |
| Very high alpha can sharply reduce item coverage and nDCG | Table 2 and §5, PDF pp. 9–10 | Aggressively prioritizing a policy signal can create undesirable side effects |

**Do not claim:** their nDCG metric is directly comparable to Busan TF-IDF similarity retention. They measure different things.

## Authors' explicitly stated limitations (§6, PDF p. 10)

1. **Only one platform and location:** Yelp restaurants in Philadelphia.
2. **Only one POI type:** Restaurants; it is not a general evaluation of all tourist attractions.
3. **Classical weighted ranker:** The size and interaction of locality effects could differ under more sophisticated learned geo-aware systems.
4. **Only offline evaluation:** User satisfaction and real business outcomes were **not** established.
5. **Future work proposed by authors:** Other cities, platforms and POI types; learned context-dependent weights; user and provider studies to test downstream reactions.

## Connection to the existing Busan paper

| Comparison | Çelik et al. (2026) | This Busan research |
|---|---|---|
| Policy objective | Locality-oriented venue exposure | District economic-undercapture-oriented attraction exposure |
| Unit / data | Restaurant reviews from Philadelphia | 207 official Busan attractions; district visitor and foreign-card-spending aggregates |
| Ranking base | Popularity and proximity | TF-IDF attraction/query relevance |
| Ranking modification | Weighted additive standardized locality | Multiplicative relevance × (1 + lambda × district undercapture) |
| Evaluation | Offline nDCG, novelty, coverage, locality, GeoSpread | Archived simulated exposure, TF-IDF retention, exposure Gini and district coverage |
| Real economic effects | Not evaluated | Not evaluated |
| Human validation | Real-user satisfaction study not performed | Two-person pilot exploratory only |

Busan's archived result at lambda=0.8 is **56.41% -> 70.14%** in simulated exposure to undercapturing districts (+13.74 percentage points), with **99.06% retained TF-IDF similarity** and exposure Gini **0.3263 -> 0.2983**. These are summary-table findings that still require full source/script reproducibility. **They do not imply a 13.74% revenue gain.**

## What is (and is not) a research gap?

**NOT supportable:** “Nobody has re-ranked POIs for sustainable tourism”, “This is the first algorithm that improves geographic equity”, “Çelik et al. proved lower revenue for local restaurants”, or “Our study solves the missing economic outcome validation”.

**Candidate gap requiring broader literature verification:** Does a district-level economic-undercapture signal derived from visitor-activity and foreign-card-spending shares add a defensible, independent policy-relevant objective to a relevance-preserving urban attraction ranker, beyond simpler geographic exposure balancing?

**Next discriminating experiment:** Compare (A) relevance-only TF-IDF, (B) a geography/exposure-balancing baseline with no spending data, and (C) the economic-undercapture multiplier. Freeze NEW held-out tourist queries before model changes, use the same candidate set and independent human relevance assessments, and compare rank-weighted district exposure, attraction and district coverage, relevance, and travel-time feasibility. This experiment is **proposed, not completed**.

## Draft-ready citation sentences

- **Prior work:** “Çelik et al. (2026) show that a continuous review-based locality feature can be integrated into an interpretable urban POI ranking system, with measurable trade-offs between locality-oriented discovery and held-out ranking quality.”
- **Limitation:** “Their evaluation is limited to Yelp restaurants in Philadelphia and does not establish real-world user satisfaction or business revenue effects.”
- **Differentiation:** “Unlike a venue-review-based locality measure, the Busan study considers a district-level proxy defined by the difference between estimated foreign visitor activity and recorded card-spending shares; this change in policy signal requires further validation against simpler exposure-balancing criteria.”

## Professor discussion questions

1. Is economic-undercapture a defensible proxy for the policy goal, given different spending sectors and visitor counting definitions?
2. What extra baseline would best establish incremental value from the spending signal?
3. What size and rubric of blinded human judgments are feasible before submission?
4. How to describe economic opportunity without claiming realized economic effects?

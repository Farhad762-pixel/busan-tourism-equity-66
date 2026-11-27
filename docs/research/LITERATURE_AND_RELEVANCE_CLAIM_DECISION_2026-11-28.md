# Literature novelty and relevance claim decision — 28 Nov 2026

**Review type:** Targeted literature verification and technical evidence audit. This is **not** an independent professor review, a systematic literature review, or a completed human evaluation. This file is added to a draft review branch; `main` and original saved RQ3 results are preserved.

## Verdict — three separate questions

**1. Does the economic policy change simulated attraction visibility? YES (development evidence).** The saved combined Busan JSON and 33-query TF-IDF benchmark reproduce the historical lambda=0.8 result: positive-undercapture district exposure rises from 56.4063% to 70.1443% (+13.7380 percentage points) with 99.0600% retained TF-IDF similarity. This is not economic impact.

**2. Is the economic policy better than simple geographic balancing? NOT ESTABLISHED.** For 36 previously inspected natural-language queries in the experimental Search V2, the 2022–23 economic ranking achieved 63.74% of simulated exposure to districts with later (2024–25) positive undercapture, compared with 64.43% for inverse attraction-count balancing, 60.63% for baseline-exposure balancing and 54.65% for relevance only. The economic later-score-weighted metric was practically tied with inverse attraction-count. Exposure Gini was lowest for baseline-exposure balancing. Only 17/36 new-but-already-inspected queries returned any strict source-supported attractions; 19/36 returned none. V2 model-score retention is not independent relevance.

**3. Is the algorithm uniquely novel or independently useful for tourists? NOT ESTABLISHED.** Already published work includes local business exposure/sustainability ranking (Patro et al., 2020), geographic POI bias mitigation (Sánchez et al., 2023), card-transaction-based Korean tourism recommendation (Hong et al., 2023, two papers), locality-aware re-ranking (Çelik et al., 2026), urban tourism stakeholder simulations (Merinov & Ricci, 2026), a multi-criteria sustainability framework explicitly including economic criteria (Salmony et al., 2026), a tourism platform for marginal territories (Generosi et al., 2025), and Busan tourism attraction/spending analysis (Park et al., 2025). A plausible **narrow candidate contribution** remains the specific district-level visitor-activity/foreign-card-spending *relative undercapture* policy signal evaluated in a transparent Busan attraction re-ranker. Targeted literature checks cannot establish global first use.

## Essential source list

| Work | Closely related contribution | Source |
|---|---|---|
| Çelik, Banerjee & Wörndl (2026) | Restaurant locality ranking, different ranking signal | https://ceur-ws.org/Vol-4206/UMAP4GOOD-5.pdf |
| Park et al. (2025) | Busan attraction connectivity vs spending association | https://doi.org/10.17208/jkpa.2025.08.60.4.173 |
| Patro et al. (2020) | Multiobjective local recommendation, provider sustainability | https://doi.org/10.1145/3383313.3412251 |
| Merinov & Ricci (2026) | Urban POI promotion and crowding stakeholder trade-offs (publisher abstract) | https://doi.org/10.1016/j.asoc.2026.114582 |
| Generosi et al. (2025) | Recommender platform for marginal tourist territories | https://doi.org/10.1007/s40558-025-00327-1 |
| Sánchez, Bellogín & Boratto (2023) | Geographic/POI bias analysis and mitigation | https://doi.org/10.1007/s10618-022-00913-5 |
| Hong, Chung & Koo (2023) | Card-transaction tourism recommendation in Jeju | https://doi.org/10.2298/CSIS220620002H |
| Hong, Chung, Koo & Koh (2023) | Deep/temporal card transaction tourism recommendation | https://doi.org/10.1007/s41060-022-00380-7 |
| Salmony, Moreno & Valls (2026) | Sustainability POI framework including economic factors | https://doi.org/10.3233/FAIA250570 |
| Onder et al. (2026) | Conceptual AI tourism visibility-to-economic-demand allocation | https://doi.org/10.1177/13548166261488140 |

## Copy-ready gap paragraph

Prior studies already develop locally oriented and sustainable tourism recommenders, fairness-aware and geographic-diversification policies, and recommendations based on Korean tourism card-transaction records. This study therefore does not claim to invent exposure-aware or economically informed tourism recommendation. Instead, it tests a specific intra-urban priority signal—the mismatch between district estimated foreign visitor-activity shares and recorded foreign-card tourism-consumption shares—within a transparent attraction re-ranking policy in Busan. Its empirical scope is the reproducibility, robustness, and offline exposure/relevance trade-offs of this proxy relative to conventional and geographic-only baselines. Its value for independent tourist relevance, real accessibility, and realized economic outcomes remains to be established.

## Claims explicitly NOT supported

- “First economic tourism recommendation algorithm” or “first algorithm to reduce tourism inequality”
- “Our approach is proven better than geographic re-ranking alternatives”
- “99% retention is 99% user satisfaction”
- “District undercapture measures poverty or SME financial loss”
- “The algorithm increased real visits, tourist spending, or local business profit”
- “Independent V2 human relevance validated” or “professor approved”

## Evaluation/professor gates

1. No completed independent V2 human judgments in the provided all-in-one package (there is an **older two-reviewer exploratory pilot**, not a new V2 validation). Collect real, consented blinded judgments with the policy labels hidden.
2. Old 48 searches and the 36 inspected natural-language searches are development data. Get genuinely unseen tourist searches; freeze model, metrics, inclusion/exclusion, ratings rules, and compare the same candidate pools.
3. Conduct professor/specialist review of economic proxy definitions, Gangseo/airport, spend category/cash limitations, duplicate visitor activity across districts, source data rights, and whether the study can be submitted as an *offline feasibility paper*.
4. For accessibility claims, obtain actual travel times; current tests use only straight-line Haversine radii.
5. Before journal submission, ensure GitHub branch experiments match local reproducible snapshots. In the last audit the optional V2 branch implementation and local snapshot required harmonization.

**Status decision: original offline feasibility claim supported within development data; claims of independent tourist usefulness, universal algorithm superiority, global novelty and economic impact must not be asserted.**

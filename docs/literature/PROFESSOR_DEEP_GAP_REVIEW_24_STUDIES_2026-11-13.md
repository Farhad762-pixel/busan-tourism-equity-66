# Professor research decision brief: Which Busan tourism research gap is worth pursuing?

**Project:** Algorithmic visibility, tourist recommendations, and foreign tourism card spending in Busan, South Korea  
**Date:** 13 November 2026  
**Purpose:** Compare the current manuscript with stronger, data-feasible research gaps in **plain English**, show the related published literature and its actual findings, and recommend **one** research direction.  
**Evidence level:** Targeted English/Korean literature review using publisher or journal sites, scholarly records and KTO/OECD material; **not** an exhaustive systematic review and **not** certification of a world-first idea. Abstract-level details are explicitly distinguished from complete study conclusions. No new human ratings, visitor behavior or economic impacts are claimed.

## A. Decision in 30 seconds

**Keep the project and its data. Do not write a new unrelated paper.** The earlier research is usable, but the headline **“equity re-ranking increases exposure to undercapturing districts”** is a weak contribution by itself: the algorithm directly boosts those districts, so increased exposure is partly **built into the formula**. Fair POI re-ranking and spending relative to visitation are already researched. The next contribution must say *when an apparently good economic target is both reliable AND actually reachable by a relevant recommendation*.

### Recommended main research gap: **The Economic Opportunity–Recommendation Feasibility Gap**

> **Problem:** A district can have a low spending-to-visitation ratio, yet the recommender may have too few suitable attractions for a particular tourist search, be constrained by distance, or be reacting to an imperfect economic measurement. In those cases, an increase in a computed equity score does not establish a genuine actionable opportunity.
>
> **Research opportunity:** Test the **limit of achievable economic targeting** after relevance, attraction supply and geographic eligibility are considered; identify where economic re-ranking improves real *recommendation visibility* beyond geographic diversification, and where it cannot.

**Proposed title:** **From Economic Need to Reachable Recommendations: Auditing Spending-Intensity Targets, Relevance, and Geographic Feasibility in Busan.**

**Important:** “Need” means the paper's *measured proxy*, **not verified business deprivation**. If the supervisor prefers even more careful language, use: **“When Is Economic-Targeted Tourism Re-Ranking Feasible? Evidence from Busan's Visitor–Spending Indicators and Attraction Catalog.”**

This is **not a claim that feasibility-aware re-ranking has never been studied**. A 2026 paper already investigates limitations of relevance-aware fairness measures, and capacity/utility constraints are studied in recommendation. The potentially distinctive empirical question is **the interaction of Busan's visitor–spending signal, tourist intent, catalog supply and geographic constraints** and the demonstration of where a policy fails. This specific end-to-end framing was not located among the **screened** works, but global novelty remains unverified.

---

## B. What the data can and cannot tell us

| We already have | What it enables | What it does **not** measure |
|---|---|---|
| 16 districts × 48 months (2022–2025): 768 district-month records of estimated foreign visitor activity and covered foreign-card tourism spending | District visitor share, spending share, seasonality, measurement sensitivity, historical-versus-later targeting | Unique tourists, firm profitability, payment outside card coverage, tourist preferences, neighborhood welfare |
| 207 official Busan attraction records with names, district, descriptions and GPS coordinates | Query-dependent item eligibility, district catalog supply, text-based relevance and geographic radius experiments | Full POI universe, all local SMEs, opening hours accuracy, certified accessible public transit times |
| 48 development tourist queries, 33 meeting the original positive-match threshold | Baseline-versus-economic re-ranking, category coverage, ranking failures, relevance-aware feasible maximum | Unbiased or representative population of actual visitor searches |
| Existing 33-query re-ranking, multiple district scores, 2,000 shuffled scores and 2022–2023 / 2024–2025 comparison | Historical score stability; comparison with a basic geographic diversification rule | Causal prediction of tourist spending or actual welfare effects |
| Exploratory six-query two-reviewer relevance pilot; separate second-round **blank** rating protocol | Preliminary evidence that TF-IDF scores can be misleading; framework for independent ratings | General tourist satisfaction or new second-round human outcomes |
| Haversine radius calculation from three approximate visitor origins | Preliminary travel-distance eligibility sensitivity | Transit travel time, fare, routing convenience, safe walking routes |

### New verification from the saved checkpoint (read-only)

- **768** distinct district-month records; **16** districts; **48** months; **207** attraction records.
- Only **33 of 48** development search prompts met the model's “at least five positively matched attractions” rule. **15/48 = 31.25%** did not. This is a concrete **retrieval/eligibility bottleneck**, not a new human-impact result.
- In **2024–2025**, the five districts with the highest simple *positive normalized spending-intensity shortfall* were Gangseo-gu, Saha-gu, Seo-gu, Yeongdo-gu, and Yeonje-gu. The same five appeared in **21 of 24 months**, and the average monthly overlap was **4.875 out of five**. This suggests the extreme-high-need set is generally **stable** within this period, rather than supporting a grand claim that priorities switch every season.
- **Selection warning:** The former study's *five policy candidate districts* were a different group screened for attraction supply; do not confuse that candidate selection with the five largest **economic scores**. The top five economic-score districts above are a **new explanatory diagnostic**, not the pre-existing target candidate set.

**Calculation:** For a district d, estimated visitation share is v_d and covered foreign-card spending share is s_d. The existing score `u_d = max(0, 1 - s_d/v_d)` measures a positive shortfall in *normalized covered card-spending intensity per recorded district visit*. Algebraically, `s_d/v_d = (S_d/V_d)/(S_total/V_total)`. It is **not a new general economic concept**: Korea Tourism Organization already publishes consumption intensity including expenditure relative to visits [L01]. Nor is it proof that a district is losing money. Airport/interchange trips, hotel billing, spending categories and payment-provider coverage are plausible alternative explanations that **the existing data cannot identify individually**.

The earlier economic experiment reported **56.41% → 70.14%** of modeled rank-weighted exposure to positive-gap districts, retaining **99.06% of TF-IDF similarity** at lambda 0.8. **Do not translate either into increased revenue or 99.06% human satisfaction.** Its inverse-POI-count comparator was not relevance-matched. The 2022–2023 score and 2024–2025 score correlation **0.971** was a cross-period indicator-alignment check, not a spending forecast.

---

## C. Why the current research claim is less convincing than it sounds

| Existing claim or assumption | Why a professor/reviewer can challenge it | Necessary correction |
|---|---|---|
| “I invented an equity-aware tourism recommender.” | Tourism fairness, provider exposure and re-ranking are well studied [L04, L05, L07, L08, L09]. | Credit original methods; study a *specific empirical failure/success condition*. |
| “The spending-to-visitor gap is a new index.” | Korean official tourism consumption-intensity data already include spending relative to visitation [L01, L02, L03]. | Describe as a **derived proxy**, not a new economic invention. |
| “Higher exposure to undercapturing districts proves the algorithm works.” | Rewarding exactly those districts mechanically tends to raise that group's measured exposure. | Compare credible competitors at **matched human-rated relevance** and report independent metrics or feasibility failures. |
| “The model keeps 99.06% relevance.” | That is **text similarity**, not tourist-judged usefulness. The small pilot found weak market/photography queries [L15, L19]. | Report human ratings, retrieval failures and uncertainty. |
| “Every low-spending district should receive more tourists.” | High visitor estimates can include non-shopping visitors/transit; districts may have different attractions and local capacity [L01, L02, L06, L12, L16]. | Audit measurement reliability and avoid claiming moral entitlement or local financial need. |
| “Distance checks show convenience.” | Straight-line distance ignores bridges, hills, routes, travel hours and actual mode [L10]. | Call it a geographic proxy; measure real transport only with permitted data. |
| “A new 10-query dataset is independent.” | Those 10 eligible prompts have already been viewed in the research process. | Reserve a **truly untouched** final evaluation sample after all design decisions are frozen. |
| “One more algorithm will make the paper publishable.” | New formulas can still be weak if the benchmark, measure and real-world meaning are flawed [L14, L17, L18]. | Make the **research question, falsification and measurement validity** central. |

---

## D. Research gaps ranked for impact, potential distinctiveness and fit

**Ratings below are editorial judgments (not proven bibliometric rankings).** “Novelty potential” means *promising in the screened literature*, **not** first in the world.

### Gap 1 — **Actionable Economic Opportunity / Feasibility Gap** — **RECOMMENDED MAIN CONTRIBUTION**

**Easy explanation:** Your system may correctly identify a district with low recorded spending compared with visits. But if a tourist searches for a **family beach** and that district has no relevant, accessible beach in the official catalogue, increasing its score cannot produce a good recommendation. A policy should tell a tourism manager **when it can help, where it cannot help, and what is missing**.

- **Related prior work:** CAPRI-FAIR shows provider exposure trades off with accuracy and distance [L07]; Merinov & Ricci model tourist utility/crowding trade-offs [L08]; minimum-exposure guarantees formalize fairness constraints [L09]; a 2026 analysis documents limits of relevance-aware fairness scores [L13]; a 2026 POI review highlights poor definitions and real-world evaluation [L14]; Mai et al. show actual Busan tourist spatial choices depend strongly on POI availability and distance [L10].
- **What remains insufficiently resolved in these screened works:** A **Busan-specific test** quantifying whether **economically targeted districts** even have *suitable reachable attraction candidates for each tourist intent*, and the maximum feasible exposure after applying an independent relevance requirement. This is an **inference from the comparison**, not proof the authors never considered something analogous.
- **Existing data:** 207 attraction texts/districts/coordinates, 48 queries, 16-district economic scores, existing benchmark, precomputed geographic-radius results.
- **Proposed tests:** (1) count relevant POIs for each query and district; (2) show retrieval failure/coverage rates; (3) compute per-query **maximum achievable rank-weighted exposure** toward economically targeted districts under a fixed *human-rated relevance* cutoff and realistic candidate eligibility; (4) compare baseline, economic and non-economic diversity policies; (5) report where no reasonable policy can meet the target.
- **Primary outcome:** `achieved fraction of available exposure headroom = (policy exposure − baseline exposure)/(feasible maximum exposure − baseline exposure)` where the denominator is positive. Report **not applicable** for zero/negative headroom; do not artificially set to zero. The feasible maximum must be computed under exactly the same chosen relevance and accessibility constraints and candidate list; pre-specify this rule. Supplement with percentage of searches where **no eligible target POI exists** and the exposure/relevance/coverage frontier.
- **Why it matters:** A destination manager needs to know whether to change a recommendation algorithm, improve attraction data, address transport, or invest in the visitor experience. **A fairer numerical score can hide a lack of actual recommendable opportunities.**
- **Limits:** Our 207 POIs are not a census of all businesses; TF-IDF and Haversine are weak proxies. Human ratings and real travel times would make stronger claims possible.
- **Assessment:** Possible distinctiveness **medium–high in this specific combined setting**; societal policy relevance **high**; existing-data fit **very high**; additional data **modest for a careful offline study**.
- **Candidate title:** **“When Is Economic-Targeted Tourism Re-Ranking Feasible? A Relevance- and Accessibility-Aware Audit in Busan.”**

### Gap 2 — **The False-Opportunity / Measurement-Validity Trap** — **HIGHEST POTENTIAL POLICY IMPACT, BUT NEEDS NEW VALIDATION**

**Easy explanation:** A district may look economically disadvantaged simply because many mobile signals represent transit stops, the business mix is different, or credit cards are captured differently. Giving that area extra tourist exposure could be misguided. **Are we measuring local economic opportunity or a data artifact?**

- **Prior work:** KTO consumption-intensity API [L01]; Data Lab/OECD measurement caveats [L02]; Korean visitor/card studies [L03, L06]; tourism fairness stakeholder critiques [L05]; 2026 economic indicators review [L20]; OECD on local value leakage and resident impact [L16].
- **Under-addressed application:** **Stress-testing a spending-intensity-based tourism ranking intervention for false positives**, not merely observing that the ratio varies. Existing reviewed articles often analyze tourism indicators or recommendation design separately; this combination needs verification.
- **Data tests possible now:** alternative spending/visitation definitions, 2022–2023 vs 2024–2025, Gangseo/no-Gangseo normalization, district catalog availability, change under simple spending-share vs count scores; classification flips under reasonable assumptions. Prior analysis already shows score-normalization changes the Gini result.
- **Extra evidence needed for a substantive 'false' classification:** verified transit/pass-through context, accommodation and merchant categories, business supply, card-provider coverage, or a tourism manager/local-business interview with appropriate approval. **Current panel cannot determine which district is truly disadvantaged or why a ratio is low.**
- **Assessment:** Distinctiveness potential **medium–high as a targeted policy audit**; societal impact **very high**; existing-data fit **medium**; extra data **important**.
- **Candidate title:** **“When Does Spending-Based Tourism Equity Misidentify Need? A Data-Validity Audit of Busan District Recommendations.”**

### Gap 3 — **Economic Signal vs Geographic Diversification, at Equal Tourist Relevance** — **BEST IMMEDIATE COMPLETION PATH**

**Easy explanation:** We already know an economic multiplier boosts selected districts. But **does it work better than simply recommending less-represented places, and is the difference still present when both systems are equally useful to tourists?**

- **Prior work:** exposure fairness [L04, L09], CAPRI-FAIR [L07], geographic bias [L11], Korean transaction-based recommendations [L21], Merinov & Ricci's multistakeholder comparison [L08], offline evaluation validity warnings [L17, L18].
- **Specific gap to test:** Compare district spending-intensity targeting against **inverse attraction count, inverse baseline exposure, inverse spending share and inverse visitor share**, while holding **human-rated relevance** and candidate eligibility constant. The difference between our target and the competitor's outcome is a falsifiable hypothesis, not by itself proof of welfare gains.
- **Existing data:** all computational inputs already present, including the 2,000 shuffled district-score negative control. Original retrospective test reported **69.49%** later-indicator target exposure from the 2022–2023 economic score versus **63.35%** for an inverse-attraction-count control, but the methods were **not relevance-matched**.
- **Needed:** a policy-strength sweep and interpolation on the relevance frontier, a fresh untouched query set, and independent ratings. Treat score similarity across 2022–2023/2024–2025 as *temporal construct stability* rather than spending prediction.
- **Assessment:** Potential originality **moderate** (because the method family is established), academic strength **high if rigorously evaluated**, existing-data fit **very high**, implementation risk **low–moderate**.
- **Candidate title:** **“Does Spending-Intensity-Aware Re-Ranking Add Value Beyond Geographic Diversification? Evidence from Busan.”**

### Gap 4 — **Season-Aware Economic Targets vs Fixed Annual Policies** — **LOWER PRIORITY AFTER DATA CHECK**

**Easy explanation:** Should Busan promote different districts during winter versus summer, using changing visitor/spending gaps?

- **Existing work:** tourism recommender seasonality is already studied [L22]; seasonality and spatial/market composition are studied in tourism economics; Dalir's 2026 simulation [L23] directly tests AI interventions, spending and seasonality.
- **Our evidence:** Top-five districts by monthly shortfall matched the overall 2024–2025 top five in **21/24 months**, and average monthly overlap was **4.875/5**. Strong top-five stability weakens the case that monthly switching is a major unexplored policy need in this particular dataset.
- **Viable alternative:** test whether a few **mid-ranked districts** or specific tourism intents experience useful seasonal shifts, but do not promise a major finding.
- **Assessment:** Potential novelty **low–moderate**, policy impact **medium**, existing-data fit **high**, current empirical motivation **weak**. Do **not** switch the main topic to this without a positive pilot.

### Gap 5 — **Does Extra Visibility Produce Real Local SME Revenue?** — **HIGHEST REAL-WORLD IMPACT, NOT ANSWERABLE WITH THESE DATA ALONE**

**Easy explanation:** If the system recommends more places in Seo-gu, do smaller local businesses actually make more money? Or is the change only on the screen?

- **What exists already:** the Netherlands information experiment measured real changes in visitors' **movement** [L12]; Dalir simulated visitor activity/spending effects [L23]; OECD highlights how spending may not remain within local communities [L16]; 2026 AI demand-allocation theory [L24].
- **What's needed:** platform impressions/clicks/choices, merchant transaction changes or a consented field study with a destination partner, ideally a control group. District-month aggregates alone are not a counterfactual evaluation of recommendations.
- **Assessment:** Highest potential economic significance, but **low immediate feasibility**. Treat as a future follow-up, **not** a claimed result or mandatory part of the present paper.

---

## E. Proposed single stronger paper, not five separate projects

**Working title (recommended):** *When Is Economic-Targeted Tourism Re-Ranking Feasible? A Relevance- and Accessibility-Aware Audit in Busan.*

**Why it is stronger than the old title:** The old hypothesis is close to automatic: “boost districts with high economic scores → they receive more score-weighted exposure.” The new hypothesis can **fail**, as when no suitable attractions exist, when distance removes candidates, when the ratio is unstable, or when a basic geographic policy does as well at the same human relevance.

### The three revised research questions

1. **RQ1: Reliability.** How stable is a district's **observed relative card-spending intensity shortfall** across periods and plausible normalizations? What measurement limitations make it a questionable policy target?
2. **RQ2: Reachability.** For which tourist search intents do districts classified as lower-capture have **relevant, geographically eligible** official attractions? What is the maximum feasible target exposure before harming independently judged relevance?
3. **RQ3: Additional value.** At the same measured tourist-relevance level and eligible-POI set, how much of this **feasible economic-targeting headroom** can spending-aware re-ranking capture compared with simple geographic-diversification baselines?

### Falsifiable hypotheses

- **H1:** Some queries, not necessarily most, will have insufficient relevant/eligible attractions to achieve the intended economic exposure without reducing relevance. **The share of such queries is to be measured**, not assumed.
- **H2:** The historically computed economic score will improve a held-out, **later-score-alignment** outcome more than the strongest non-economic control at matched relevance. This may be **rejected**.
- **H3:** Results will change under at least some defensible data-construction and eligibility assumptions. Existing sensitivity findings motivate this test, but its exact size should not be assumed.

### Deliverables the professor can inspect

- Query-by-query **relevant candidate supply** table, including **all 48** original development searches and their 15 failures; new untouched prompts used for confirmatory evaluation only after freezing the study.
- District × tourist-interest **coverage/eligibility heatmap**, showing where the official catalogue supports each intent (not a measure of all attractions in Busan).
- Exposure frontier chart: **baseline / economic signal / inverse count / inverse spending share / inverse visitor share** at **matched human-rated relevance**; separate distance/radius conditions.
- A **feasibility/headroom table** for each query (including *no feasible target attraction* and *no available headroom* states).
- Economic-score **measurement sensitivity chart**, with the Gangseo stress test clearly labeled **not** a causal airport explanation.
- Reproducible code, versions of the frozen datasets, source provenance, limitations, GitHub documentation and supervisor-ready manuscript.

### What NOT to claim

No observation of commercial Naver/Kakao/Google ranking algorithms; no actual visit or card-spending increase; no local-SME income; no measured subway journey time; no proof that low relative spending is economic deprivation; no world-first fairness method; no human validation from blank forms.

---

## F. Closest literature and actual findings: focused evidence matrix

**How to read this matrix:** 'Published contribution/findings' means only what the linked journal/official source visibly supports. 'Open issue for Busan' is **our interpretation of the remaining empirical question**, not a claim that the authors never considered related ideas elsewhere. Full-text access varies; the paper should be read fully before journal submission. This table covers **24 targeted sources**, not all world literature.

| ID | Literature, year, evidence link | What the source actually reports | Relation to the proposed gap / boundary |
|---|---|---|---|
| **L01** | [Korea Tourism Organization, regional tourism demand intensity API (2025–2026)](https://www.data.go.kr/data/15151868/openapi.do) | Official index includes **tourism spending relative to visits** among consumption-intensity indicators. | The ratio's *general concept is existing*, not newly invented; public index and foreign-only district proxy need definition alignment. |
| **L02** | [OECD, Korea Tourism Data Lab (2025)](https://www.oecd.org/en/publications/2025/06/using-alternative-data-sources-and-tools-to-measure-and-monitor-tourism-case-studies_3508b538/the-korea-tourism-data-lab_01ee60bf.html) | Mobile positioning visitor counts are trend proxies with possible over/underestimation; card measures have separate construction. | A ratio cannot uncritically be interpreted as true spend per person. |
| **L03** | [Oh & Kang, regional tourism activation diagnostic (2023)](https://doi.org/10.31667/jhts.2023.01.96.77) | Uses mobile/credit card big data and regional indicators for diagnosing tourism activation in Korea. | Multi-source indicators in Korean tourism are established; may inform validation. |
| **L04** | [Banerjee, Banik & Wörndl, tourism fairness review (2023)](https://doi.org/10.3389/fdata.2023.1168692) | Reviews multistakeholder fairness and scarce consideration of wider societal effects. | Exposure balance does not automatically mean social equity or economic value. |
| **L05** | [Müllner et al., tourism-management fairness (2025)](https://doi.org/10.3389/fdata.2025.1632766) | Shows mismatch between quantitative fairness metrics and community/stakeholder needs. | Motivates cautious policy meaning and local stakeholder consultation. |
| **L06** | [Kim, relations among Korean tourism-demand indicators (2026)](https://kci.go.kr/kciportal/landing/article.kci?arti_id=ART003396498) | Across 229 Korean areas, mobile visitation, card spending and navigation indicators relate strongly but imperfectly; controlling area scale weakens associations. | Visitor activity and spending capture distinct phenomena; inference from their ratio requires context. |
| **L07** | [dela Cruz et al., CAPRI-FAIR (2024)](https://arxiv.org/abs/2406.03109) | Balances provider/consumer fairness, precision, distance; trade-offs can arise. | Fair POI post-processing is already studied; need query/relevance feasibility, not just an exposure boost. |
| **L08** | [Merinov & Ricci, positive-sum urban tourism (2026)](https://doi.org/10.1016/j.asoc.2026.114582) | Simulates limited tourist awareness and POI re-ranking; positive-sum outcomes and over-promotion risks. | Close related work in tourism utility, popularity and crowding; their simulations are **not** our district card intensity experiment. |
| **L09** | [Lopes et al., minimum exposure guarantees (2024)](https://doi.org/10.1016/j.eswa.2023.121164) | Optimizes ranking utility subject to minimum group exposure constraints; trade-off studied. | Formal exposure targets are established; need context-valid constraints and achievable maxima. |
| **L10** | [Mai et al., Korean urban tourist spatial choice (2025)](https://doi.org/10.1016/j.tourman.2025.105254) | Using visitors to Seoul, Busan and Jeju, travel distance, POI availability and repeat visits shape spatial decisions. | Supports treating actual geography/POI supply as important, while our straight-line proxy remains limited. |
| **L11** | [Sánchez, Bellogín & Boratto, geographic/POI bias (2023)](https://doi.org/10.1007/s10618-022-00913-5) | Characterizes and mitigates location-based venue/category/popularity/distance biases. | Geographic diversity is not new; economic feasibility is the narrower empirical question. |
| **L12** | [Mitas et al., tourist-flow field experiment (2023)](https://doi.org/10.3390/ijerph20085441) | Randomized tourist information affected movement toward lesser-known places with limited experience differences. | Demonstrates possibility of changing **movement**, not card-spending effects in Busan. |
| **L13** | [Relevance-aware item-fairness limits (2026)](https://doi.org/10.1145/3765624) | Some fairness measures have unreachable theoretical extrema depending on dataset/position effects. | Formal feasibility concepts are **already known**; the gap is Busan's economic signal and real query/POI supply. |
| **L14** | [Bellogín et al., POI recommendation pitfalls (2026)](https://doi.org/10.1145/3816430) | Identifies flawed problem assumptions, poor benchmarks and limits to real-world application. | Supports a careful, failure-reporting evaluation rather than another formula. |
| **L15** | [Geninatti Cossatin et al., offline/perceived fairness (2026)](https://doi.org/10.1145/3774935.3806150) | Finds misalignment between offline fairness scores and some user perceptions. | Don't call 99.06% text-relevance retention 99.06% satisfaction. |
| **L16** | [OECD, social benefits of tourism (2026)](https://www.oecd.org/en/publications/oecd-tourism-trends-and-policies-2026_3fd3cd75-en/full-report/enhancing-the-social-benefits-of-tourism_43631a73.html) | Local benefits, SME participation and leakage are separate from visitor volume; resident impacts matter. | **Economic opportunity** is more than card intensity or online exposure. |
| **L17** | [Pereira, Said & Santos, offline evaluation reliability (2025)](https://doi.org/10.1145/3705328.3748086) | Exposure and item sampling choices can distort offline algorithm comparisons. | Use identical candidates, predeclare failures, and preserve query eligibility details. |
| **L18** | [Parajuli, Vaez Barenji & Ekstrand, convergent validity (2026)](https://doi.org/10.1145/3773078.3831818) | Offline evaluation design choices may not agree with dense ground-truth judgments. | Use genuine independent query judgments rather than relying only on cosine scores. |
| **L19** | [Wang, Höpken & Jannach, heterogeneous POI data survey (2025)](https://doi.org/10.1007/s40558-024-00301-3) | Reviews data types and limitations in POI recommender research. | Mixed-language metadata and coverage gaps can constrain recommendation reach. |
| **L20** | [Tourism economic indicators systematic review (2026)](https://doi.org/10.1007/s11301-026-00592-2) | Reviews 149 studies and 2,271 indicators, separating potential, effective and connected economic value. | An easily computed district ratio is an incomplete welfare/prosperity measure. |
| **L21** | [Hong, Chung & Koo, Korean card-transaction recommender (2023)](https://doi.org/10.2298/CSIS220620002H) | Trains a tourism-business recommender with Korean credit-card transaction and location data. | Card-informed recommendation is not new; signal-specific policy evaluation must be demonstrated. |
| **L22** | [Banerjee et al., seasonality and sustainable trips (2025)](https://doi.org/10.1007/s40558-024-00303-1) | Combines emissions, popularity and seasonality in tourism recommendation and a user study. | A basic time-dependent sustainability objective is not new. |
| **L23** | [Dalir, AI tourism eco-economic simulation (2026)](https://doi.org/10.1007/s10796-026-10818-z) | Agent-based simulations can raise modeled spending and visits without necessarily reducing seasonality. | AI/spending/seasonality have been studied, but simulations do not validate Busan business impact. |
| **L24** | [Onder et al., AI discovery and tourism demand allocation (2026)](https://doi.org/10.1177/13548166261488140) | Develops economic arguments about AI travel discovery, market access and demand concentration. | Provides motivation, not a measured link between our district ranking and realized spending. |

### Essential source-search limitations

- Targeted English and Korean searches on publisher sites, KCI, DOI metadata, institutional article records, OECD and official Korean data pages. Some items were assessed from abstracts or available full-text sections only. **This is not PRISMA or an exhaustive review**.
- No comprehensive closed-database Scopus/Web of Science export, forward/backward citation audit of all 24 works, thesis/dissertation repository search, or patent search was performed. The phrase **“nobody has studied this anywhere” cannot be supported**.
- Full bibliographic page details and article text should be cross-checked against originals at final submission; some sources are 2026 online-first releases.
- The proposed gap is a **specific intersection of data, feasible target exposure, and evaluation**, not a claim to invent recommender fairness, feasible rankings or spending intensity.

---

## G. Professor decisions to request now

1. Does the supervisor agree that a **feasibility/failure audit** is a stronger bounded contribution than merely demonstrating a fair ranking gain?
2. Can the manuscript position its score explicitly as a **card-spending-intensity proxy**, not actual local economic deprivation?
3. What is the minimum ethically approved blinded human-rating exercise to establish sensible relevance thresholds and a genuinely untouched benchmark?
4. Can official KTO indicator definitions and permissible data-use/release terms be confirmed? Is partner-level travel-time, business-type or merchant data available?
5. Would the professor prefer the **more immediately complete comparator study** (Gap 3) or the **more distinctive policy-feasibility study** (Gap 1)? The latter uses the former as a component.

## H. Existing research to preserve

- [Current complete manuscript v0.4](../../manuscript/BUSAN_FULL_MANUSCRIPT_DRAFT_v0_4_2026-11-13.md) — **do not discard this**.
- [Earlier spending-intensity novelty audit](DEEP_NOVELTY_AUDIT_SPENDING_INTENSITY_2026-11-13.md) — overlaps with existing indicators and research.
- [Economic-signal specificity diagnostic](../research/ECONOMIC_SIGNAL_SPECIFICITY_DIAGNOSTIC_2026-11-13.md) — previous simple comparator and 2,000 shuffles.
- [Economic-indicator sensitivity report](../research/ECONOMIC_INDICATOR_SENSITIVITY_2026-11-13.md) — year and Gangseo scenarios.
- [Existing human-pilot report](../research/HUMAN_RELEVANCE_PILOT_2026-11-13.md) — 2-reviewer pilot, **not** population evidence.
- [Research reproducibility status](../research/REPRODUCIBILITY_STATUS.md) — code/data and publication limitations.

**Recommended action:** **Freeze the original data and models; seek professor approval for the feasible-exposure audit, then conduct one carefully designed comparative experiment with genuinely independent relevance judgments.** No unrelated new project is needed.
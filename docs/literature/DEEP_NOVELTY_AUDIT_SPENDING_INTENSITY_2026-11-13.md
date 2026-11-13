# Deep novelty audit: spending intensity in Busan tourism recommendation

**Research project:** Economic-Equity-Aware Re-ranking for Intra-Urban Tourism Recommendations: Evidence from Busan, South Korea  
**Review date:** 2026-11-13  
**Status:** Targeted, multi-source literature and prior-art audit. **Not an exhaustive systematic review or a guarantee of a worldwide first.** No existing manuscript or research file was overwritten.

## Executive decision

**Keep the Busan topic. Do not claim a novel spending/visitation indicator or the first fairness-aware tourist recommender.** There is substantial prior work on all of these separately and partially in combination. The more defensible research contribution is a *controlled comparative evaluation* of **district spending-intensity-aware attraction re-ranking** against relevance-only and non-economic geographic-diversity baselines, with temporal, relevance and access constraints.

### Critical new finding: the indicator's mathematics

Let `S_d` = district `d`'s covered foreign-card tourism spending, `V_d` = its mobile-derived estimated foreign visitor-activity indicator, and `S`/`V` the respective sums over the 16 studied districts. Define:

- district spending share `s_d = S_d/S`
- district visitor-activity share `v_d = V_d/V`
- existing study's positive undercapture proxy `u_d = max(0, 1 - s_d/v_d)`

Algebraically, `s_d/v_d = (S_d/V_d)/(S/V)`. Thus `u_d` is the positive shortfall in **relative observed card-spending intensity per estimated district visit**, scaled by the aggregate 16-district ratio. It should not be presented as a novel stand-alone mathematical index, a count of unique tourists, lost revenue or an economic welfare measure.

**Direct official overlap:** Korea Tourism Organization's public API for *regional tourism demand intensity* (registered 2025-11-10, updated 2026-02-25) explicitly lists *tourism consumption intensity*, including **spending relative to visit volume**. Its published index need not be numerically identical to the Busan foreign-only ratio, but **the underlying concept already exists in Korean tourism analytics**:
https://www.data.go.kr/data/15151868/openapi.do

## Screening approach and limits

Targeted English and Korean searches on 2026-11-13 across publisher/conference sites and web-indexed KCI, Korean research-institute, PubMed/PMC and public-data records. Search families included combinations of:
- tourism + fairness/exposure/re-ranking + district/neighborhood
- tourism recommendation + spending/card consumption + local businesses/equity
- tourism economic impact + AI/agent-based visibility + revenue
- visitor activity versus card-spending shares, "tourism demand intensity" / "spending per visit"
- Korean: 관광 추천 경제 형평성 관광소비 방문객; 방문량 대비 소비액 추천; 이동통신 신용카드 관광 활성화 지표

Source types: official KTO metadata (direct), full open-access publisher text where accessible, publisher abstracts, DOI records, and peer-reviewed Korean bibliographic abstracts. Full text was not available for every article. **No documented exhaustive Scopus/Web of Science citation-chain, unindexed thesis search, or patent search was completed.** Findings establish *documented overlaps*, not global absence.

## Directly relevant prior work (priority)

| Study (year) and link | What has already been done | Overlap/limit for our project |
|---|---|---|
| **KTO Public Data API (2025–2026), [Regional tourism demand intensity](https://www.data.go.kr/data/15151868/openapi.do)** | Public tourist consumption-intensity indicator includes expenditure relative to visits | Economic shortfall per visit is not a new standalone index. Official indicator may use a different data population/formula. **Official metadata verified** |
| **Oh & Kang (2023), [regional tourism activation index](https://doi.org/10.31667/jhts.2023.01.96.77)** | Combines telecommunications, visitor activity, card expenditure and stay duration at Korean local-government scale | Using mobile/card indicators together and deriving a tourism index are established. **KCI abstract verified** |
| **Hong, Chung & Koo (2023), [Card transaction tourism recommendation](https://doi.org/10.2298/CSIS220620002H)** | Uses eight years of Korean card transactions and location features in Doc2Vec tourism-business recommendation | Card-informed travel recommendation is established. Unlike ours, mainly predicts recommended business/service preference. **Publisher full abstract + PDF available** |
| **Kim (2026), [Regional Tourism Demand Indicators](https://doi.org/10.17958/ksmt.28.5.202610.1128)** | Directly compares navigational interest, telecom visitors and card-tourism consumption across 229 Korean local areas (2023–2025) | Comparing recorded visitation and consumption across Korean regions is established; does not describe re-ranking. **KCI abstract verified** |
| **Cheng et al. (2025), [Tourist concentration in Korean cities](https://doi.org/10.1016/j.tourman.2024.105064)** | Uses mobile data to examine spatial concentration for international visitors in Busan, Seoul and Jeju | Busan tourism concentration itself is not novel. **Publisher abstract verified** |
| **Sánchez, Bellogín & Boratto (2023), [Location recommender bias mitigation](https://doi.org/10.1007/s10618-022-00913-5)** | Studies venue/category popularity, exposure and geographic-distance polarization; tests hybrid and re-ranking controls | Geographic fairness/re-ranking and distance analysis are established; a meaningful comparator. **Open full text examined** |
| **Banerjee, Banik & Wörndl (2023), [Tourism fairness review](https://doi.org/10.3389/fdata.2023.1168692)** | Synthesizes fairness, popularity, provider and societal interests for tourism recommenders | Fairness in TRS is established. **Open full text examined** |
| **Müllner et al. (2025), [Multistakeholder tourism fairness](https://doi.org/10.3389/fdata.2025.1632766)** | Calls for fairness grounded in tourism management and local stakeholder needs rather than narrow algorithmic indicators | A purely district-card-spending proxy is not automatically normative fairness. **Open full text examined** |
| **Merinov & Ricci (2024), [Urban tourism promotion and user utility](https://doi.org/10.1145/3640457.3688173)** and **(2026), [Positive-sum urban tourism](https://doi.org/10.1016/j.asoc.2026.114582)** | Simulated multistakeholder tourist POI recommendations with limited awareness, crowding and user-utility tradeoffs | Close computational predecessor. Their objective is crowding/popularity rather than *specifically* foreign-card-spending-to-visitation mismatch. **Conference metadata and 2026 journal abstract verified** |
| **Dalir (2026), [AI eco-economic tourism simulation](https://doi.org/10.1007/s10796-026-10818-z)** | Agent-based tourism system simulates fairness-oriented visibility, recommender filtering, visitor activity and **spending**; calibrated from a UK destination | **Very close and important.** We cannot claim nobody has simulated tourism economic effects of visibility. Their spending outputs are model-simulated; our work uses observed district indicators to construct a rank objective, but does NOT simulate or measure downstream spending. **Substantial open publisher text verified** |
| **Tourism Open-ended Experimentation Platform (2026), [local/sustainable recommendation platform](https://doi.org/10.3390/app16083937)** | Builds a platform promoting less-visible local businesses/experiences and economic distribution; early provider-interface evaluation | Local economic inclusion via recommendations is established as a goal. Platform does not report the same district ratio in the material reviewed. **Full accessible text examined** |
| **Onder et al. (2026), [AI discovery and tourism demand allocation](https://doi.org/10.1177/13548166261488140)** | Economic *conceptual* paper on AI visibility, tourism demand and local revenue retention | Distributional economic motivation is not new; it provides theory, not evidence our policy works. **Publisher open text examined** |
| **Madrid visitor-expenditure spatial study (2021 DOI; later journal publication), [bank-card urban tourist expenditure](https://doi.org/10.1080/13683500.2021.1991898)** | Quantifies visitor expenditure concentration within a city using geo-located bank cards and spatial models | Unequal tourist spending and card-based urban geography are established. **Open text examined** |
| **Incheon urban tourism studies (2025, [infrastructure vs visits/spending](https://doi.org/10.34165/urbanr.2025..28.243); 2026, [commercial district structure and tourism](https://doi.org/10.34165/urbanr.2026..29.37))** | Korean fine-grained empirical analysis of visits/card spending, business capacity and infrastructure | Important challenge to interpreting under-spending as algorithm-caused inequity. **KCI / research institute abstracts verified** |
| **Lopes et al. (2024), [Minimum exposure guarantees](https://doi.org/10.1016/j.eswa.2023.121164)** | Fair recommendation post-processing with exposure constraints | Fairness-aware post-processing is existing methodology. **Publisher abstract verified** |

**Additional checked context:** 2026 systematic tourism-recommender literature reviews; OECD 2025 KTO Data Lab report; 2024 sustainable city trip recommendation; 2025/2026 AI travel visibility audits. These strengthen background but do not prove that the exact Busan policy has or has not appeared elsewhere.

## Scientific novelty assessment

### NOT genuinely new (must not claim)
1. Tourism, urban POI, fairness or popularity mitigation.
2. Credit-card data for tourist recommendations.
3. Using mobile visitor estimates and card-tourism expenditure together.
4. The mathematical concept of expenditure relative to visitation (KTO already publishes consumption-intensity measures).
5. Simulating the impact of AI choice/recommendation on economic or distributional outcomes (Dalir 2026).
6. Busan intra-urban tourism concentration (Cheng et al. 2025).

### Remaining *candidate* contribution (conditional, not worldwide first)
> A **controlled Busan policy evaluation** of whether an official-data-informed, district relative foreign-card-spending-intensity signal produces **more economically targeted exposure** than relevance-only, popularity-based and non-economic geographic diversification **at comparable independently judged tourist relevance and geographic feasibility**, using carefully separated historical policy signals and later diagnostic periods.

The search did **not** identify an exact same end-to-end combination in the screened work. It cannot establish that none exists globally. The specific mechanism is still a simple multiplicative re-ranker, not a new algorithm class.

## Why earlier claims need correction

- **Arithmetic observation:** `(spending share)/(visit share)` reduces to normalized **spending per recorded district visit**. Avoid calling it an unprecedented "economic-under-capture index."
- **Outcome circularity:** If the model boosts places with high `u_d` and the outcome measured is exposure to places with high `u_d`, part of the positive exposure gain follows directly from the algorithm. Report independent targets and competitors.
- **Historical alignment:** 2022–2023 and 2024–2025 scores are based on the same measurement system; high correlation means a persistent score, not proof the policy can predict revenues or improve them.
- **Apples-to-apples evaluation:** The existing inverse-attraction-count comparator and spending-aware model used equal λ but *different relevance losses* (99.61% vs 99.20%). Match relevance loss or compare full Pareto frontiers, then obtain real human ratings.
- **Denominator limitations:** Telecom district visits are estimates of activity, not unique city visitors. Different payment, lodging, airport, merchant mix and sector coverage can influence the ratio. A lower ratio does **not** establish that a district needs or wants more tourists.
- **Distance:** Haversine is a straight-line proxy, not subway travel duration.
- **Human relevance:** the two-person pilot and a prepared second-round protocol do not demonstrate general tourist satisfaction; use genuine consented ratings.

## Concrete stronger research design, without changing topic

1. **Pre-register claims and data definitions.** Describe the policy score as "relative card-tourism spending intensity shortfall", not an established measure of economic justice. Compare its ranking and stability with KTO's public consumption-intensity metric if geography, time period, and population definitions can be aligned.
2. **Hold the algorithm input constant.** Use policy information from 2022–2023 and development searches to select rules; use a genuinely **untouched query set** to evaluate. Use later-period economic indicators only as independent-by-time descriptive checks, not outcome causal validation.
3. **Evaluate credible controls at matched relevance:** relevance-only, simple geographic diversity, inverse registered-POI count, inverse spending share, inverse visit share and a location-aware fairness control. Sweep λ or constrain loss to the same *human-rated* nDCG@10 margin rather than compare one λ across differently scaled signals.
4. **Measure all outcomes:** weighted positive-shortfall exposure, continuous intensity-score-weighted exposure, district coverage, Gini/HHI, per-query category failures, catalog eligibility, and access penalties. **Do not optimize and evaluate on the same score without independent controls.**
5. **Independent human relevance study:** use blinded independent reviewers with supervisor ethics/consent guidance and a documented missing-rating rule, on fixed untouched queries. Report variability rather than broad satisfaction from a tiny pilot.
6. **External economics (aspirational separate follow-up):** only if approved access is obtained, use merchant-level transactions, destination management partner or observed visits/purchases to test local business impact. This is **not required for a narrowly framed computational feasibility paper**, but required for revenue-impact claims.

### Suggested updated title (optional; no new topic)
**Does Spending-Intensity-Aware Re-Ranking Add Value Beyond Geographic Diversification? An Offline Tourism Recommendation Study in Busan, South Korea.**

### Suggested main hypothesis
At the same independently judged tourist-relevance level and within matched eligible attraction sets, a ranking policy based on **historical relative card-spending intensity** yields greater *later-period under-intensity-targeted simulated exposure* than alternative non-economic geographic-diversity policies. A failure to outperform them would be a useful falsification, not grounds to hide the result.

## Recommendation for supervisor discussion

The existing Busan paper has sufficient substantial work to complete a rigorous **applied computational study**. Its strongest defensible originality, if any, is **which target signal is operationalized and how carefully it is evaluated**, not invention of tourism fairness or consumption intensity. Before claiming Q1-level or "never done" novelty, read full relevant papers, complete Scopus/Web of Science forward/backward searches (including Korean theses), secure provider-definition alignment and verify independent human relevance. **Do not start over.**

**Sources are attributed with DOI and official links above. Review notes are assessments of the sourced articles, not certification of global non-existence.**

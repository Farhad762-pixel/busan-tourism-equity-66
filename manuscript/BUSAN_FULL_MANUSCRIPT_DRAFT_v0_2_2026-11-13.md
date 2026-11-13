# Economic-Equity-Aware Re-ranking for Intra-Urban Tourism Recommendations: Evidence from Busan, South Korea

**Integrated manuscript working draft v0.2 — 13 November 2026**

**Status:** First integrated academic manuscript for supervisor feedback, NOT ready for a journal submission. Sections 1–2 are drawn from the earlier source-checked writing draft; the following sections integrate the previously saved Methods and Results DOCX, archived analysis tables, the independent RQ3 numerical rerun, archived straight-line distance experiment, and small human-relevance pilot. Claims and caveats are deliberately separated.

## Abstract

**Purpose.** Tourist recommendation rankings allocate visibility among attractions. A destination-management system might seek broader exposure for suitable places in districts where estimated foreign visitor activity is large relative to recorded foreign-card tourism consumption. This study investigates that possibility in a controlled Busan attraction recommender.

**Methods.** The archived analysis combines 16 districts and 48 monthly periods (2022–2025; 768 district-month records) with 207 official tourist attractions. A TF-IDF/cosine-similarity baseline is applied to 48 researcher-defined searches, 33 of which meet the positive-match rule. Candidates are re-ranked using a tunable multiplicative district economic-undercapture signal, and compared through weighted exposure, text relevance and concentration. Supplementary tests use straight-line geographic radius constraints and a two-reviewer relevance pilot.

**Findings.** An independently rerun 33-query experiment at policy strength λ = 0.8 increased simulated weighted exposure to positive-undercapture districts from 56.41% to 70.14% (+13.74 percentage points) while retaining 99.06% of baseline TF-IDF relevance; exposure Gini declined from 0.3263 to 0.2983. A preliminary two-person, six-search relevance pilot rated 61 unique query–attraction pairs and found notable weaknesses for market and photography searches.

**Contribution and limits.** The study offers a transparent empirical application of district-level spending/visitation-share differences in a controlled tourism re-ranking model. It does not audit commercial platforms or establish changes in actual visits, spending or human satisfaction. The benchmark is development data; provider-measurement limits, new blinded relevance testing and real travel-time constraints remain outstanding.

**Keywords:** tourism recommendation; rank exposure; economic-undercapture proxy; Busan; popularity bias; geographic concentration; recommender systems; sustainable tourism.

---

## 1. Introduction

### 1.1 Tourism discovery as an allocation of visibility

Digital information systems have become an important interface between travelers and the attractions, neighborhoods, and businesses they may choose to visit. Tourism recommender systems support destination discovery by organizing large numbers of alternatives and presenting items judged relevant to a visitor's interests. Earlier work established tourism recommendation as a mature field involving domain knowledge, contextual information, and diverse artificial-intelligence techniques (Borràs et al., 2014 [1]). Yet the quality of a recommendation list should not necessarily be evaluated only by the preferences of the person viewing it. Rankings also determine which places receive prominence, creating potential interests for attraction providers, destination managers, and communities that may be affected by the distribution of tourism activity (Abdollahpouri et al., 2020 [2]; Banerjee et al., 2023 [6]).

This distributional perspective is especially relevant for a city containing multiple tourist districts with different attraction types, transport connections, and commercial opportunities. A recommender that repeatedly shows the same familiar locations may provide relevant results while leaving other suitable places less visible. Conversely, deliberately introducing less visible places can be counterproductive if the suggestions do not match visitor interests or are impractical to reach. The design problem is therefore not to distribute recommendations uniformly, but to examine whether a transparent, place-sensitive objective can broaden exposure **subject to** meaningful relevance constraints. Existing ranking-fairness work provides mathematical foundations for measuring and allocating attention, including user-utility trade-offs (Singh & Joachims, 2018 [3]).

### 1.2 Why Busan and why an economic signal?

Busan provides a useful within-city setting for studying that tension. Existing research has already documented substantial spatial concentration and variation in foreign visitor activity within Korean urban destinations, including Busan. Cheng et al. (2025 [7]) analyzed mobile phone traces for international travelers in Seoul, Busan, and Jeju and reported differences in spatial concentration across traveler-origin groups. Accordingly, **this study does not claim to discover tourism concentration in Busan for the first time**. Instead, it asks whether exposure produced by a controlled attraction recommender can be related to a distinct economic indicator and modified through a transparent algorithm.

The research archive combines Korea Tourism Data Lab district-level foreign visitor activity and foreign tourist credit-card consumption with official Busan attraction records. The archived panel covers 16 administrative districts and 48 monthly periods from January 2022 to December 2025 (768 district-month observations), while the points-of-interest corpus contains 207 official attractions. The intended comparison is between two *different kinds of recorded activity*: where an estimated volume of foreign visitors is observed and where foreign-card tourism consumption is recorded. A district may account for a larger proportion of district-level visitor activity than of foreign-card tourism consumption. The study operationalizes that relative difference as an **economic-undercapture score**, not as a direct estimate of business loss or an ethical entitlement to additional visitors.

The interpretation requires particular caution. Korea Tourism Data Lab describes its foreign-visitor data as estimates derived from mobile-network signals and notes that travel purpose cannot be identified precisely. Its documentation also warns that district visitor estimates should not be freely added to represent unique city visitors: one person can appear in multiple visited districts, and the published numbers are better suited to trend analysis than precise absolute population counts (Korea Tourism Organization, data-methodology notes [11]). For this reason, the shares used below are **shares of the sum of estimated district visitation indicators**, rather than shares of unique individuals visiting Busan. The spending data represent *recorded foreign-card tourist consumption*, not total tourist expenditure, cash spending, or the revenue of individual small firms. Differences in card acceptance, visitor mobility, spending categories, and data-provider coverage can influence the indicator. These limitations affect any interpretation of the proposed economic signal.

### 1.3 From popularity-based attention to an operational research question

The research builds on two connected literatures. First, ranking and recommendation studies show that popularity and item exposure can be uneven and that post-processing can alter representation while monitoring relevance. Personalized re-ranking for long-tail items (Abdollahpouri et al., 2019 [4]) and geographic/venue-bias mitigation in location-based recommenders (Sánchez et al., 2023 [5]) demonstrate that the general technique of popularity-aware or geographically aware re-ranking is **already established**. Second, tourism-specific fairness and sustainability studies have considered societal stakeholders, overtourism, environmental cost, seasonality, and the uneven visibility of destinations (Banerjee et al., 2023 [6]; Banerjee et al., 2025 [8]). More recent studies explicitly audit biases in AI-assisted travel recommendation (Andreev et al., 2025 [9]; Najafi & Costa, 2026 [10]). The present work should therefore be understood as an **application-specific operationalization and empirical audit**, rather than the invention of fairness-aware tourist recommendations.

The narrower research opportunity is to investigate a district-level signal that captures the mismatch between estimated foreign visitation activity and recorded foreign-card spending within **one city**, and to examine how that signal interacts with attraction-level relevance. This moves beyond an indicator based solely on the number of attractions, ratings, or visits, while remaining a proxy with several possible alternative explanations. The study does not assume that the resulting re-ranking constitutes a uniquely fair allocation. Instead, it makes the objective explicit, measures its consequences, and retains the option to reject the policy if relevance or accessibility becomes unacceptable.

### 1.4 Study design and research questions

The study uses a **controlled, offline attraction-ranking experiment**; it does not observe what Naver Map, Kakao Map, Google Maps, or commercial travel platforms actually recommend. Textual attraction information is represented using TF-IDF and cosine similarity to construct a baseline for a fixed set of researcher-defined tourist queries. An economic score is constructed from district visitor and spending shares, primarily using 2024–2025 data. Baseline positive-relevance candidates are then re-ranked by a multiplicative rule that raises the score of eligible attractions in districts with positive estimated economic undercapture. The same searches and available attractions are used to compare rank-weighted exposure and textual relevance across policy strengths. Supplementary archived work reports straight-line distance sensitivity checks and a small exploratory human-rating pilot; neither amounts to a field evaluation of travel behavior.

The analysis is organized around three research questions:

**RQ1 — Distribution:** How concentrated are estimated foreign visitor activity and recorded foreign-card tourism consumption across Busan's administrative districts during 2022–2025, and where do their relative district shares differ?

**RQ2 — Visibility:** How does a controlled relevance-based tourism recommender allocate simulated, rank-weighted attraction exposure across districts, and how is that exposure associated with the recorded visitor and spending distributions?

**RQ3 — Trade-off:** To what extent can district economic-undercapture-aware re-ranking increase simulated exposure to places in relatively low-capture districts without substantially reducing measured textual relevance or worsening geographic concentration and practical access constraints?

These questions are **descriptive and computational**. RQ1 identifies patterns rather than their causes; RQ2 audits an investigator-built baseline rather than a commercial provider; and RQ3 evaluates a simulated allocation of attention rather than a change in tourist transactions.

### 1.5 Intended contributions and paper organization

The intended contributions are threefold. First, the study develops a transparent within-city *economic-undercapture* indicator that links two types of official district tourism measurements, while documenting why it cannot be interpreted as a measure of firm-level income or distributive injustice. Second, it incorporates that indicator into an interpretable re-ranking rule and reports exposure, relevance, coverage, and concentration trade-offs under a fixed benchmark. Third, it begins assessing whether the system's computer-based similarity measures are aligned with judgments by human reviewers and whether straight-line geographic constraints change the observed trade-offs. This last contribution remains preliminary because the human pilot is small and travel-time routing has not been measured.

The remaining sections will describe the data and transformations; the baseline, exposure, and re-ranking methods; the offline and pilot results; their implications and alternative interpretations; and the limits of any real-world tourism policy inference. The empirical contribution is conditional on further verification of source provenance, a broader literature review, and new out-of-sample tests.

## 2. Related Work and Theoretical Positioning

### 2.1 Tourism recommenders and the meaning of recommendation quality

Research on tourism recommender systems has long incorporated the distinctive features of travel decision-making, including heterogeneous attractions, location, context, and the need to select among many alternatives. Borràs et al. (2014 [1]) survey intelligent tourism recommender methods and applications, demonstrating that the discipline predates the current generation of AI-based travel assistants. Recommendation *quality* in this tradition generally includes relevance to the traveler, but may also reflect usefulness, constraints, diversity, or context.

A central methodological implication for the present work is that textual similarity is only a **proxy for relevance**. A TF-IDF system can retrieve terms such as “art” or “market” from a record without distinguishing a neighborhood market from an art museum. Its score should not be described as a predicted satisfaction probability. The archived two-reviewer pilot in this study suggests that low-quality descriptions and ambiguous attraction types particularly affect “local market” and “photography walk” queries; however, that pilot cannot support population-level conclusions. Additional human judgments and a held-out benchmark will be needed before a claim of retained *user-perceived* utility is defensible.

### 2.2 Multistakeholder objectives and fairness of ranking exposure

A user-focused recommender may perform well on accuracy metrics while giving limited attention to the consequences for item providers or places. Abdollahpouri et al. (2020 [2]) describe the multistakeholder perspective in which users, providers, and platforms can have distinct interests. Tourism can further involve local residents, environmental impacts, and destination-management goals, as emphasized in the review by Banerjee, Banik, and Wörndl (2023 [6]). That review is important prior art: it already frames tourism recommendation fairness as a domain-specific multi-stakeholder challenge. Consequently, simply adding an “equity” term is not a sufficient novelty claim.

Singh and Joachims (2018 [3]) conceptualize ranking fairness through **exposure**, allowing attention-related constraints to be expressed alongside ranking utility. That perspective motivates using a position-discounted sum of recommendations rather than counting each item in a list equally. The present study uses a weight of \(1/\log_2(r+1)\) at rank \(r\) to summarize which Busan districts appear most visibly across simulated top lists. This weight is a research convention rather than an empirically calibrated click model; different examination or click propensities could change the estimated exposure distribution.

A further conceptual issue is that **districts are not themselves individual providers**. A district may include prosperous attractions, businesses with different levels of need, noncommercial sites, and residents with diverse interests. Allocating more visibility to a district is therefore not equivalent to guaranteeing fair treatment of every local supplier, nor to producing a direct economic transfer. In this study, “equity-aware” refers narrowly to the stated *district-level weighting rule* and should not be interpreted as an independently validated normative fairness standard.

### 2.3 Popularity mitigation and location-based point-of-interest bias

Popularity bias has inspired post-processing methods that increase representation of less frequently recommended items. Abdollahpouri, Burke, and Mobasher (2019 [4]) demonstrate personalized re-ranking for long-tail items while considering recommendation accuracy. The conceptual relationship is close: the present study likewise reorders relevant candidates instead of constructing wholly new attraction records. The difference lies in the **policy signal being tested**—a district-level foreign-card-spending/estimated-visitation mismatch rather than item popularity or long-tail rating frequency.

Location-based recommender research provides even closer methodological context. Sánchez, Bellogín, and Boratto (2023 [5]) examine venue popularity, category popularity, exposure, and geographic-distance-related bias in POI recommendations and evaluate mitigation techniques. Therefore, neither geographic bias measurement nor joint consideration of relevance and location can be claimed as new. The Busan analysis asks a different empirical question: whether a district-level tourism consumption indicator changes the allocation of *simulated* attraction visibility when attached to an explicit, transparent ranking formula.

This also indicates why **distance matters**. A distant attraction may be less suitable even if it has a high equity multiplier. The archived Busan sensitivity test uses Haversine straight-line radii from approximate stations, a useful geometric stress test, but it cannot establish bus/subway travel times, walking convenience, station transfer burdens, opening hours, or feasibility for an individual tourist. In the final manuscript, results obtained from such radii must remain labeled *straight-line-distance-constrained*, not *transit-time-optimized*.

### 2.4 Sustainable tourism, intra-city concentration, and digital recommendations

Tourism scholarship already recognizes the importance of where visitor activity occurs. Cheng et al. (2025 [7]) use mobile-phone-derived activity records to study the spatial concentration of international visitors in Seoul, Busan, and Jeju, including differences across traveler-origin groups. This is particularly important for our geographical framing: **the presence of geographic concentration in Busan is existing knowledge**, not a novel empirical discovery. The distinction proposed here is the additional use of foreign-card consumption shares as a diagnostic input to a controlled recommendation policy.

Sustainable tourism recommendation research has moved beyond individual relevance into broader social and environmental criteria. Banerjee et al. (2025 [8]) combine city-trip carbon-equivalent emissions, destination popularity, and seasonality into a composite sustainability indicator and report a user study of travel trade-offs. Their study shows that sustainable recommendations may explicitly integrate multiple quantitative objectives and human preference data. The Busan framework is narrower geographically and economically: it focuses on attractions *within one city* and tests an index based on estimated visitation versus card-based tourism spending, not intercity carbon emissions or broad destination popularity. This contrast helps define its empirical scope; it **does not** prove methodological novelty.

Recent AI-travel auditing also matters. Andreev et al. (2025 [9]) analyze multiple biases in LLM-based travel suggestions and discuss a public-interest re-ranking layer. Najafi and Costa (2026 [10]) examine digital concentration in recommendations generated by AI systems and characterize the risk of repeatedly emphasizing established destinations. Both precede this manuscript and directly challenge any claim that algorithmic travel visibility or its mitigation is an unexplored topic. Our experiments do **not** reproduce their audits of deployed LLM systems; rather, they use a small, fully specified relevance baseline whose rankings are controlled by the researcher.

### 2.5 Source-data measurement, causal limits, and evaluation design

The choice of a district-level economic signal is also a measurement problem. According to the Korea Tourism Organization's Data Lab metadata [11], foreign visitor estimates are generated from telecom-network observations, may miss users depending on coverage and devices, and cannot accurately identify trip purposes. One visitor can be counted across visited local districts; district sums do not represent a deduplicated count of people entering the city. Data Lab also documents changes to the coverage of some credit-card tourism-consumption records and warns that historical values may be revised [12]. These facts limit the reliability of a simple comparison of numeric totals.

Accordingly, the proposed economic-undercapture score compares **relative distributions of two recorded indicators**, not a spending-per-person estimate. A low recorded card-spending share relative to the sum of estimated district activity could arise from short transit stops, different commercial mixes, seasonal patterns, the prevalence of non-card payments, accommodation payments assigned elsewhere, or other data-generation effects. Without firm-level income data and causal identification, it cannot establish an economic shortfall attributable to recommendations.

Evaluation design creates a second limitation. The archived 48 tourist searches, of which 33 passed a positive-relevance eligibility rule, are now development material. Re-testing a new recommendation strategy on those same searches would risk overestimating its generalization. The two-person human pilot is also development evidence; disagreements and “cannot judge” responses reveal uncertainty. An improved version therefore needs a **new, frozen held-out query set**, better attraction categories and translations, a consistent human-judgment rubric, more reviewers, and predeclared missing-rating handling. Offline relevance/exposure should be clearly separated from field outcomes such as clicks, visits, purchases, and perceptions of fairness.

### 2.6 Synthesis, proposed gap, and theoretical contribution

Table 1 positions the study relative to the most directly related literature. The table summarizes what each cited publication supports and is **not** a claim that its authors never examined other variables.

| Prior research stream | Existing contribution | Focus in the Busan experiment | Implication |
|---|---|---|---|
| Tourism recommender systems (Borràs et al. [1]) | Methods for selecting relevant travel items and handling tourist context | Fixed TF-IDF attraction ranking under a controlled query protocol | Recommendation methodology is established |
| Multistakeholder fairness and ranking exposure (Abdollahpouri et al. [2]; Singh & Joachims [3]; Banerjee et al. [6]) | Formalizes interests beyond the traveler and allocation of ranking visibility | Explicit district-level exposure measures and relevance trade-offs | Fairness and exposure principles are established; district proxy requires justification |
| Popularity and location-aware bias (Abdollahpouri et al. [4]; Sánchez et al. [5]) | Re-ranking and analysis of item/venue/geographic concentration | Multiplier from foreign-card spending share relative to estimated visitation share | Change concerns the signal and setting, not invention of re-ranking |
| Tourism spatial concentration (Cheng et al. [7]) | Within-city visitor concentration in Korean cities, including Busan | Adds spending-share comparison and a simulated re-ranking intervention | Busan concentration itself is not novel |
| Sustainable/AI travel recommendations (Banerjee et al. [8]; Andreev et al. [9]; Najafi & Costa [10]) | Multiple sustainability objectives; geographic visibility audits; policy-oriented re-ranking | Controlled intra-city POIs and transparent economic mismatch signal | Similar high-level goals already studied; detailed difference must be demonstrated |

**Provisional research gap (subject to a fuller literature search).** Within the specific studies reviewed so far, an opportunity remains to test an *intra-urban, district-level economic-capture proxy* constructed from **estimated foreign visitation shares and foreign-card consumption shares** as a transparent, tunable signal in a relevance-preserving point-of-interest ranking experiment, with explicit reporting of geographic exposure and text-relevance trade-offs. This is a **narrow empirical-positioning claim**, not evidence that no other paper has operationalized a comparable index. To establish its novelty, the researcher must search beyond these initial papers, review full texts and forward/backward citations, and contrast exact indicator formulas, location scales, and behavioral measurements.

Three implications follow. First, **measurement transparency** matters: the estimated visitation denominator, spending coverage and location aggregation all influence the economic signal. Second, **algorithmic transparency** matters: a multiplicative re-ranking formula makes the exposure/relevance trade-off auditable but does not prove societal benefit. Third, **evaluation validity** matters: rank-weighted exposure and TF-IDF retention characterize a research system, while claims about visitor satisfaction, travel feasibility, and local business welfare require different data and study designs.

This theoretical framing leads to RQ1–RQ3 as stated in the Introduction. It supports a practical controlled demonstration and a cautious policy discussion, not a claim of proven causal improvement in tourism economic equality.

## 3. Data and Methods

### 3.1 Research design and data sources

This study is a **descriptive, computational and offline** experiment. Its observational component compares the geographic distribution of two Korea Tourism Data Lab indicators. Its computational component examines how a transparent research-built text recommender changes rank exposure when a district-level economic signal is added. The project does not observe Naver Map, Kakao Map or Google Maps rankings, nor does it measure actual clicks, trips or purchases.

The archived monthly panel comprises all 16 Busan administrative districts and January 2022–December 2025 (48 months), resulting in 768 district-month records. One variable estimates foreign tourist activity using mobility-derived information; the other records covered foreign-tourist **credit-card tourism consumption**, expressed in million KRW. The data-provider measurement systems have distinct coverage. In particular, foreign district visit estimates are not counts of deduplicated unique tourists. One traveler may appear in more than one district, so the normalized district shares below represent shares of a **sum of estimated district-visitation indicators**, not shares of unique visitors entering Busan. Card consumption does not capture all cash, card or other tourist spending. These differences are central to the proxy's interpretation, not minor footnotes.

The second dataset contains 207 attractions from the official Busan attraction-information service. Available attributes include identifiers, titles, subtitles or descriptions, district labels, address and place fields, transport text and coordinates. Coverage is uneven and some text is missing or vague. Titles and descriptions contain mixed Korean and English, while the evaluation queries are written in English. Original data exports and a processed JSON database are held in the research archive; redistribution of source-derived data is withheld from public GitHub pending license review. The previously documented archived panel is not a substitute for independently checking the original provider selection filters and any later revisions.

The 2022–2025 panel is used for descriptive RQ1 trends. The **2024–2025** aggregated district indicators define the primary economic signal used in the controlled intervention. This distinction prevents future and earlier periods from being inadvertently mixed in the same model calibration.

### 3.2 Economic concentration and the opportunity proxy

For a district d, let V_d be its summed estimated foreign visitation indicator and C_d the recorded foreign-card tourism consumption over the declared period. Define district-indicator shares:

\[
s^V_d=V_d/\sum_jV_j,\qquad s^C_d=C_d/\sum_jC_j.
\]

The economic capture ratio is s^C_d/s^V_d, and the re-ranking signal is

\[
u_d=\max\{0,\;1-s^C_d/s^V_d\}.
\]

When a district's share of covered card spending meets or exceeds its share of estimated visitation indicators, u_d equals zero. A positive score reflects a **relative mismatch between two observed/estimated indicator distributions**. It is not an estimate of district poverty, business profit, unmet tourist demand or moral entitlement to visibility. The saved 16-district policy input contains finite values for the defined shares; treatment of a zero visitation denominator would require an explicit separate rule in future deployments.

The archived work also screens five illustrative districts having positive undercapture and at least the median supply (13) of official attractions: Dong-gu, Geumjeong-gu, Nam-gu, Seo-gu and Yeongdo-gu. This is an analytic selection rule, not an independently validated classification of districts needing economic intervention. Descriptive RQ1 metrics include share totals, rankings, Gini, HHI and pooled district-month correlations. Associations do not show causal effects.

### 3.3 Text-based baseline and benchmark

Each official attraction is represented by concatenating its available title, subtitle, place, district, address and transport-information fields. A TF-IDF vectorizer with English stop words is fitted over the attraction documents. A query's relevance to an attraction is the cosine similarity between their vectors, denoted r(q,i). The baseline orders attractions by decreasing similarity, retaining source-order tie behavior.

The benchmark contains **48 researcher-authored searches across 12 tourism-intent categories**. The primary experiment requires at least five positive-relevance POIs per query; **33 searches** satisfied this threshold. Up to the 10 highest-ranked POIs are displayed for each eligible query. Because some queries yield fewer than 10 positive-scoring candidates, each policy produces **288 total recommendations**, not 330. The original 48 searches are now *development data*: they may be used to reproduce the initial study but cannot serve as a fresh, independent test for a revised algorithm.

Lexical relevance is an imperfect proxy for tourist suitability. A place can share words with a search without being the intended type of attraction; the official descriptions' language and omissions also influence the cosine score.

### 3.4 Economic-aware re-ranking

The re-ranking procedure takes up to the 50 highest-scoring **positive-similarity** baseline candidates for each eligible search. Attraction i, in district d(i), receives

\[
R(q,i;\lambda)=r(q,i)\,[1+\lambda u_{d(i)}].
\]

The same candidate list is re-sorted by R; up to 10 are returned. The five tested strengths are λ = 0, 0.5, 0.8, 1.0 and 2.0. The baseline is λ = 0. Unlike a simple additive district bonus, the multiplicative rule cannot promote a zero-similarity attraction into the candidate set.

The public FastAPI demonstration is **not** the same system: its current equity endpoint uses an earlier proxy based on district attraction counts and an additive combination controlled by a different parameter. Its output should never be cited as the tested economic policy. The numerical RQ3 findings here come from the independently rerun offline economic experiment using the 2024–2025 signal.

### 3.5 Ranking exposure and evaluation

Ranking position k receives the discount w(k) = 1/log2(k+1), with the first item assigned k = 1. Exposure for district d is the sum of weights for recommendations from d divided by all weights across evaluated queries. Positive-undercapture exposure is the summed exposure of districts with u_d > 0. The five candidate districts and the Seo-gu/Yeongdo-gu pair are analyzed separately.

For each query, mean text relevance is averaged over its returned top list; the 33 per-query means are then averaged so short lists are not automatically down-weighted. **Relevance retention** is mean model similarity divided by mean baseline similarity. Exposure gains are reported in **percentage points**, not as percentage increases in tourist spending. The study also reports Gini and HHI of the full 16-district exposure vector (including zero-exposure districts), top-three exposure share, district coverage and overlap with baseline. Rank position weights are a mathematical modeling choice and not estimated clicks or attention probabilities.

The illustrative λ = 0.8 policy is consistent with the archived study's **99% text-relevance retention constraint**. This parameter was evaluated and selected on development queries rather than on independently held-out tourist searches; the constraint is not a scientifically established threshold for acceptable human satisfaction.

### 3.6 Robustness and straight-line accessibility sensitivity

Archived sensitivity outputs compare alternative economic definitions (ratio, raw spending-share gap, log ratio and rank-based signals), leave-one-intent-category-out tests and query-level resampling. These address how different scoring and benchmark choices affect the simulated outcomes. They should be labeled archived descriptive checks until their exact code, sampling rules and reported uncertainty bounds have been reviewed alongside frozen original inputs.

A separate experiment filters eligible POIs by Haversine **straight-line distance** from approximate Busan Station, Seomyeon Station and Haeundae Station locations. Filters include 5, 10, 15 and 25 km and an unrestricted case. Each origin-and-cap evaluation includes only queries with at least five positive matched attractions under that cap, using **the same included queries for baseline and equity**. This tests geographic eligibility, not subway time, road distance, walking safety or convenience.

### 3.7 Blinded human-relevance pilot

An exploratory pilot drew six queries from the established categories using recorded seed 20261113 and assembled **61 unique** attraction–search pairs from the union of baseline and λ = 0.8 top recommendations. Two volunteers, whose independent judgments were collected by the researcher, rated each attraction from 1 (not relevant) to 5 (highly relevant), with **0 reserved for cannot judge**. They also recorded confidence 1–3 and did not see the policy label or position. Zero scores are missing judgements, not low relevance.

Reviewer A gave 54 valid 1–5 ratings and Reviewer B gave 59; both responded to all 61 items. Only **52 pairs** were jointly judged on the 1–5 scale. For a strict ranking comparison, all items in a query's two-policy union had to have two valid ratings; three of six searches met that rule. Complete-case rank-weighted means and nDCG@10 relative to the **judged union** were calculated. This is a diagnostic pilot, not a powered human utility, equivalence or representative foreign-tourist study. Approval and consent requirements require supervisor review. Individual ratings remain outside public GitHub.

### 3.8 Research versions and reproducibility

The frozen 33-query economic model was **independently rerun on 13 November 2026 from recovered research-archive inputs**: the 207-POI corpus, 16 district economic-signal rows and original researcher-defined queries. All five policy settings matched archived summary metrics within numerical tolerance 1e-7. A public reproduction script, development-query projection, archived policy summary and SHA-256 input inventory are available in the repository. The private economic-score table must be supplied separately by an authorized researcher for end-to-end reproduction; public GitHub does not contain all source records.

The original source exports, full RQ1 data pipeline and accessibility source-script provenance still require an independent audit. Results from these components are labeled **archived** where relevant. The saved research outputs and the validated current GitHub code should not be silently blended across model versions.


## 4. Results

### 4.1 Spatial distribution of foreign visitor activity and spending (RQ1)

Across the saved 2022–2025 panel, **Haeundae-gu accounted for 29.89%** and **Busanjin-gu for 26.89%** of covered foreign-card tourism consumption, or **56.78% together**. The distribution of estimated district visitation indicators differed: Gangseo-gu had the largest recorded indicator share (**17.24%**), followed by a relatively high Haeundae-gu share (**13.21%**). Gangseo-gu may contain airport-related transient movement; the dataset does not identify individual travelers' reasons or journeys.

The archived pooled district-month relationship between estimated visit activity and foreign-card consumption was Pearson r = **0.5726** and Spearman ρ = **0.7242**. These positive correlations are descriptive; they do not establish that commercial recommendation algorithms created the distribution or that undercapturing districts lose business because of low online visibility.

In the saved yearly concentration tables, mean monthly district **spending Gini increased from 0.6183 in 2022 to 0.6609 in 2025**; the corresponding estimated visitation-indicator Gini increased from 0.3340 to 0.4068. These data summarize the dispersion of the included indicators, not changes in household welfare, firm revenue or deduplicated tourist counts.

| Year | Mean monthly visit-indicator Gini | Mean monthly foreign-card-spending Gini |
|---:|---:|---:|
| 2022 | 0.3340 | 0.6183 |
| 2023 | 0.3739 | 0.6281 |
| 2024 | 0.3910 | 0.6389 |
| 2025 | 0.4068 | 0.6609 |

*Source: archived researcher-generated RQ1 monthly concentration tables from Korea Tourism Data Lab indicators; the original raw-to-panel derivation still needs source-receipt reconciliation.*

### 4.2 Baseline ranking visibility (RQ2)

The controlled text baseline represented **15/16 districts** over 33 eligible queries, averaging **6.24 unique districts per search**. Its position-weighted district exposure had Gini **0.3263**, HHI **0.08337**, and top-three share **35.32%**. The archived 16-district correlation between baseline exposure and foreign-card spending share was Pearson **0.4566** (Spearman **0.4353**), while the association with the undercapture signal was Pearson **-0.3975** (Spearman **-0.2956**).

These associations describe **our own retriever**, not any platform's actual search results. They must not be interpreted as evidence that Naver, Kakao or Google cause spending concentration in Busan.

### 4.3 Economic re-ranking exposure–relevance trade-off (RQ3)

The central outcome was independently reproduced from the saved offline inputs. At the illustrative λ = 0.8 setting, weighted exposure to positive-undercapture districts increased from **56.4063% to 70.1443%**, a gain of **13.738 percentage points**. Average TF-IDF cosine similarity changed from **0.1542048 to 0.1527553**, retaining **99.0600%** of the baseline. Exposure Gini declined from **0.326343 to 0.298256**; represented districts remained **15/16**.

| Policy strength (λ) | Positive-undercapture exposure | Exposure gain vs baseline (pp) | TF-IDF relevance retained | Exposure Gini |
|---:|---:|---:|---:|---:|
| 0.0 (baseline) | 56.41% | 0.00 | 100.00% | 0.3263 |
| 0.5 | 65.95% | +9.55 | 99.65% | 0.3070 |
| **0.8** | **70.14%** | **+13.74** | **99.06%** | **0.2983** |
| 1.0 | 71.53% | +15.13 | 98.62% | 0.2975 |
| 2.0 | 77.01% | +20.60 | 95.68% | 0.3279 |

*Source: independently rerun 33-query economic experiment, compared against the saved five-policy summary (13 November 2026). All are simulated ranking indicators, not visitor spending effects.*

The λ = 2.0 model moves more exposure toward the selected group but reduces textual relevance and raises Gini slightly above baseline. Thus, **target-group exposure gain, total district coverage and overall exposure concentration are different objectives**. At λ = 0.8 the five preliminary target districts increased from **30.06% to 39.01%** exposure (+8.95 pp), while the Seo-gu/Yeongdo-gu pair increased from **15.95% to 21.38%** (+5.44 pp).

### 4.4 Archived sensitivity analyses

The archived alternative-signal table reports exposure gains under four economic signals at comparable policy settings: ratio **+13.74 pp**, share gap **+7.54 pp**, log ratio **+13.38 pp**, and rank based **+12.90 pp**, with text relevance retention approximately **99.06%, 99.61%, 99.08% and 99.20%**, respectively. This shows sensitivity in effect magnitude, while the direction of the simulated exposure shift remains positive in these stored comparisons.

The saved leave-one-category-out checks and all 12 reported tourist intent categories also display positive exposure gains. Some categories have only **one eligible query**, so these checks cannot justify a broad claim about real tourist search behavior or demographic groups. The original benchmark is development material, not an independent population sample. Rechecking bootstrap settings and intervals from original input scripts remains necessary before reporting inferential confidence intervals.

### 4.5 Geographic radius sensitivity

For a **15-km Haversine straight-line radius**, the archived accessibility experiment reports:

| Approximate start location | Eligible queries | Undercapture exposure gain (pp) | Relevance retained | Change in mean straight-line distance (km) |
|---|---:|---:|---:|---:|
| Busan Station | 30 | +10.56 | 99.58% | -0.050 |
| Seomyeon Station | 32 | +11.93 | 99.19% | +0.418 |
| Haeundae Station | 27 | +10.64 | 99.12% | +0.071 |

*Source: archived distance experiment report; actual transit, route and accessibility measures were not collected.*

The geographic restriction reduces candidate availability for some query-origin combinations. At Seomyeon and Haeundae the equity policy **increased** average straight-line distance slightly, even as target-group exposure improved. Busan's coastlines, bridges and hills make Euclidean proximity an inadequate substitute for travel time. The evidence therefore supports only a **straight-line geographic feasibility screening**, not tourism convenience.

### 4.6 Human relevance pilot

Both volunteers responded to all **61** query–POI pairs. Among the **52 jointly judgeable items**, exact rating agreement was **18/52 (34.6%)** and ratings were within one point for **41/52 (78.8%)**; quadratic-weighted Cohen's κ was **0.490**. The mean rating among each reviewer's *nonzero* responses was **2.96/5** and **3.00/5**, respectively, using different judged subsets.

| Search intent | Unique pairs | Both judged | Mean paired relevance (/5) |
|---|---:|---:|---:|
| Night view | 5 | 5 | 4.20 |
| Korean history | 10 | 10 | 3.75 |
| Ocean view | 9 | 9 | 3.61 |
| Art village | 12 | 11 | 2.91 |
| Photography walk | 13 | 8 | 2.31 |
| Local market | 12 | 9 | 2.22 |

Only **three searches** had complete two-rater judgments for all items in the two-policy union. Their mean position-weighted human scores were **3.849/5** for baseline and **3.859/5** for λ = 0.8 (difference **+0.010/5**); nDCG@10 measured against the **judged union** was **0.818** and **0.849**, respectively. Such a small, selectively complete pilot cannot establish human relevance equivalence, superiority or tourist satisfaction.

The low-rated market and photography results reveal a meaningful development problem: shared words or incomplete metadata can yield apparently relevant scores for attractions that fail the tourist's intent. The pilot should be used to identify failure modes, not to certify the model.


## 5. Discussion

### 5.1 Main interpretation: an offline ranking mechanism, not an economic impact

The independently reproduced RQ3 result indicates that an explicit district-level economic signal can alter where a **controlled recommender allocates simulated rank exposure** without greatly changing its own average TF-IDF cosine score. The multiplicative formula is transparent and keeps zero-relevance candidates excluded. This is a useful feasibility result for a research prototype; it is not evidence of increased bookings, visits, payments or profitability in any Busan district.

Even the word “economic” must be read cautiously. Spending and estimated visitation shares can diverge because of hotels, merchant mix, trip duration, payment coverage, inter-district movements and data-provider estimation rules. The study therefore evaluates a distributional **proxy**, not an independently demonstrated shortfall. The five selected districts are analytical candidates, not a validated map of local business disadvantage.

### 5.2 Relation to prior recommendation and tourism literature

The ranking-fairness literature already provides exposure-based measures, relevance trade-offs and post-hoc re-ranking [2–5], while tourism work addresses stakeholder fairness, destination sustainability, and concentration [6–8]. Recent travel-AI audits also examine destination visibility and digital overconcentration [9,10]. The contribution proposed here is narrower: an **intra-Busan district-share comparison between estimated foreign visitor activity and recorded foreign-card tourism consumption**, used as an explicit attraction-ranking signal. The work does not establish a new fairness paradigm or prove that this exact objective is absent from all previous studies.

That conditional contribution is potentially valuable because the indicator, baseline, trade-offs and failures are all documented. A deeper full-text and forward-citation literature review is still needed before claiming distinctive scientific novelty.

### 5.3 The tension between fairness objectives and tourist suitability

A policy can improve weighted exposure for positive-undercapture districts yet worsen global inequality metrics at sufficiently large λ. The λ = 2.0 result illustrates why total Gini, target-group gain, district coverage, text relevance and suitable attraction type should be reported separately rather than combined into a single unexplained “fairness score.”

The exploratory human pilot is also a warning. Preserving **99.06% of TF-IDF similarity** does not mean preserving 99.06% of human utility. Reviewers found some market and photography recommendations poorly aligned with actual intent. A future recommender should consider validated venue type, Korean/English descriptions and concrete travel purpose before using an economic multiplier. However, the old 48-query and six-query sets can no longer be considered independent after inspiring these changes.

### 5.4 Accessibility, local context and responsible deployment

Radius filtering may stop the system from suggesting distant POIs, but it omits network topology, transit schedules, walking connections and arrival times. The radius results sometimes increased average distance, and tighter caps excluded many searches. For destination-management use, economic goals should be constrained by **measured route feasibility**, transparent fallback behavior and local stakeholder context. A possible future prototype would compare baseline and policy rankings for realistic origins and show the exposure–relevance–time trade-off to analysts, without claiming real-world impact.

A fair policy would also require agreement on *what* constitutes a desirable distribution. Ranking recommendations equally by district may ignore different numbers and types of businesses or legitimate traveler preferences; allocating them by spending share alone may reinforce existing concentration. The current mismatch proxy is a hypothesis to investigate, not an authoritative ethical entitlement.

## 6. Limitations and Research Ethics

**Data construct:** Mobile-derived district visitor estimates are not unique city visitor counts, and covered foreign-card tourism consumption is not total tourist spending or SME revenue. District aggregates can mask considerable within-district differences.

**Causal inference:** RQ1/RQ2 correlations do not explain the source of observed spending concentration. No real recommendation platform, visitor behavior, clicks, transactions or firm revenue changes were observed.

**Algorithm and generalization:** TF-IDF is sensitive to English/Korean vocabulary, generic attraction descriptions and missing POI type. The 48 searches were authored by the researcher and 15 low-match queries were excluded from the main test. The main 33-query study is reproducible but not an unbiased test on unseen traffic.

**Human relevance:** Two reviewers, six searches, non-random completeness, rating disagreement and three strict complete-case queries cannot establish equivalent human relevance. Ethics review and consent arrangements require professor guidance; the individual ratings are kept private.

**Convenience:** Straight-line distance is not public-transport duration, accessible walking distance, operating hours or actual tourism convenience.

**Provenance and reproducibility:** The 33-query economic experiment was independently rerun from its archived inputs. The RQ1 data pipeline and the distance-script conditions require more complete source and code audit. The public repository omits some economic records pending redistribution-right verification. The current FastAPI demo uses an older attraction-count proxy and must not be confused with the reported economic ranking model.

**Decision thresholds:** The ≥99% TF-IDF retention rule and illustrative λ = 0.8 selection were established within the development benchmark, not estimated from human tolerance or validated against pre-registered held-out data.

## 7. Conclusion and Future Research

This study investigates whether a district-level economic-undercapture proxy can be incorporated transparently into an offline tourism recommender. Using the saved 207-attraction corpus, 2024–2025 district economic indicators, and 33 eligible tourist searches, the independently rerun model found that λ = 0.8 increased simulated undercapture-district weighted exposure by **13.74 percentage points** while retaining **99.06% of baseline TF-IDF similarity**. Its overall exposure Gini decreased, although more aggressive policy settings showed trade-offs that prevent a universal “more equitable” conclusion.

These computational findings do not demonstrate improved tourist experience or redistributed real spending. The pilot human ratings, especially weak results for markets and photography walks, show why relevance to visitor intent must be measured independently. The straight-line distance experiment cannot establish actual travel convenience.

The next research stage is to (1) verify the official data source definitions and original processing pipeline, (2) complete a systematic-enough full-text prior-work review to justify a precise incremental contribution, (3) freeze new, **unseen** multilingual/intent-specific benchmark queries, (4) test an improved venue-type-aware algorithm with larger blinded human evaluation, and (5) add route-based travel duration constraints where authorized data are available. Only an appropriately designed field study could examine actual clicks, visits or transaction outcomes.

The present document is consequently a **supervisor-reviewable first manuscript**, not yet a journal-submission-ready or field-validated paper.


## References — publication identity and URLs checked

1. Borràs, J., Moreno, A., & Valls, A. (2014). Intelligent tourism recommender systems: A survey. *Expert Systems with Applications, 41*(16), 7370–7389. https://doi.org/10.1016/j.eswa.2014.06.007
2. Abdollahpouri, H., Adomavicius, G., Burke, R., Guy, I., Jannach, D., Kamishima, T., Krasnodebski, J., & Pizzato, L. (2020). Multistakeholder recommendation: Survey and research directions. *User Modeling and User-Adapted Interaction, 30*(1), 127–158. https://doi.org/10.1007/s11257-019-09256-1
3. Singh, A., & Joachims, T. (2018). Fairness of exposure in rankings. *Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*. https://doi.org/10.1145/3219819.3220088
4. Abdollahpouri, H., Burke, R., & Mobasher, B. (2019). Managing popularity bias in recommender systems with personalized re-ranking. *Proceedings of the 32nd International FLAIRS Conference*. https://cdn.aaai.org/ocs/18199/18199-78818-1-PB.pdf
5. Sánchez, P., Bellogín, A., & Boratto, L. (2023). Bias characterization, assessment, and mitigation in location-based recommender systems. *Data Mining and Knowledge Discovery, 37*, 1885–1929. https://doi.org/10.1007/s10618-022-00913-5
6. Banerjee, A., Banik, P., & Wörndl, W. (2023). A review on individual and multistakeholder fairness in tourism recommender systems. *Frontiers in Big Data, 6*, 1168692. https://doi.org/10.3389/fdata.2023.1168692
7. Cheng, J., Xu, Y., Jian, Y. I., Ren, M., & Park, S. (2025). Spatial concentration of intra-urban tourist activities and inter-group differences between Asian, European and North American travelers in Korean cities. *Tourism Management, 107*, 105064. https://doi.org/10.1016/j.tourman.2024.105064
8. Banerjee, A., Mahmudov, T., Adler, E., Aisyah, F. N., & Wörndl, W. (2025). Modeling sustainable city trips: integrating CO2e emissions, popularity, and seasonality into tourism recommender systems. *Information Technology & Tourism, 27*, 189–226. https://doi.org/10.1007/s40558-024-00303-1
9. Andreev, H., Kosmas, P., Livieratos, A. D., Theocharous, A., & Zopiatis, A. (2025). Destination (Un)Known: Auditing bias and fairness in LLM-based travel recommendations. *AI, 6*(9), 236. https://doi.org/10.3390/ai6090236
10. Najafi, M., & Costa, C. (2026). Digital overtourism in AI travel recommendations: Evidence from a comparative analysis. *Current Issues in Tourism* (online 1 April 2026). https://doi.org/10.1080/13683500.2026.2654066
11. Korea Tourism Organization. (accessed 13 November 2026). *Korea Tourism Data Lab: data definitions, mobile visitor estimation, and interpretation cautions* [Korean-language official documentation]. https://datalab.visitkorea.or.kr/datalab/portal/getMetaInfoList.do
12. Korea Tourism Organization. (2023). *Notice on changes to tourism credit-card consumption data coverage* [Korean-language official notice]. https://datalab.visitkorea.or.kr/site/portal/ex/bbs/View.do?bcIdx=302575&cbIdx=1135&pageIndex=1

## Appendix A. Evidence and reproduction register

| Component | Supporting GitHub resource | What remains |
|---|---|---|
| 33-query RQ3 numerical rerun | [Experiment reproduction log](../docs/research/RQ3_REPRODUCTION_2026-11-13.md) and [Python script](../experiments/equity/reproduce_rq3.py) | Approved private economic signal input needed for external rerun |
| Fixed query definitions | [48-query development benchmark](../experiments/equity/benchmark/development_queries.csv) | New unseen queries for model v2 |
| Five-policy results | [Archived summary table](../experiments/equity/results/rq3_policy_summary.csv) | Confirm after any model revision |
| Two-reviewer pilot | [Human relevance report](../docs/research/HUMAN_RELEVANCE_PILOT_2026-11-13.md) | Supervisor ethics check and a larger independent sample |
| Distance sensitivity | [15 km archived summary](../experiments/accessibility/results/accessibility_15km_summary.csv) | Real public-transit routing or carefully limited conclusions |
| Data sources | [Official source register](../docs/research/SOURCES_AND_REUSE.md) | Original filters, provider revisions, and reuse rights |
| Literature screening | [Targeted research log](../docs/literature/TARGETED_SEARCH_LOG_2026-11-13.md) | Full-text reading and reference checking |
| API demonstration | [FastAPI source](../src/api/main.py) | Its attraction-distribution proxy is not the economic RQ3 model |

## Appendix B. Professor review checklist

- [ ] Confirm the paper's *exact* economic claim and whether the district mismatch proxy is acceptable for this purpose.
- [ ] Check data collection filters, time periods, visitor-count definition, card coverage, unit conversions and redistribution rights.
- [ ] Confirm that the related literature establishes a defensible narrow gap, not just another popularity-bias reranker.
- [ ] Request a new held-out benchmark and ethical protocol for independent human relevance evaluation.
- [ ] Decide whether real route durations are essential for the target journal or whether straight-line proximity should remain only a sensitivity check.
- [ ] Confirm archived RQ1 and distance figures with clean reproducible scripts.
- [ ] Resolve figure/caption placement, references and target journal's style before submission.

*Archival note:* The original Methods and Preliminary Results Word draft remains a separate source. This integrated document reports the later rerun and human pilot distinctly, without silently asserting that all archived outputs were newly reproduced.

# Economic-signal novelty addendum (13 November 2026)

**Project:** Busan Tourism Equity Research  
**Review type:** targeted literature follow-up, **not a systematic review**.  
**Scientific status:** provisional research-gap argument; no new user ratings or economic impact experiment has been performed for this document.

## Main conclusion

Fairness, popularity mitigation, geographic diversity, and multistakeholder balancing in urban tourism recommendation are **already studied**. The plausible contribution of this Busan prototype is *not a new class of fairness algorithm*. It is the explicit application of a **district-level mismatch between estimated foreign visitor activity and recorded foreign-card tourism spending** as a transparent re-ranking signal, tested for simulated ranking exposure and text-relevance trade-offs within one city. Whether this exact operationalization is globally original remains unverified.

## Closest additional studies

| Study | Verified scope | What it means for the Busan claim |
|---|---|---|
| [Merinov & Ricci (2024), RecSys](https://doi.org/10.1145/3640457.3688173) | Simulates urban-POI promotion, destination overcrowding, tourist preference/choice, and limited catalogue awareness. | Multistakeholder urban tourism recommendation and user-utility trade-offs are **not new**. |
| [Merinov & Ricci (2026), Applied Soft Computing](https://doi.org/10.1016/j.asoc.2026.114582) | Studies positive-sum stakeholder outcomes and shows under- or over-promoting sustainable POIs can hurt outcomes. | Extremely close prior work. Their simulation of user choices differs from our simulated ranking exposure; our study cannot claim it proves improved choices. |
| [Sánchez, Bellogín & Boratto (2023)](https://doi.org/10.1007/s10618-022-00913-5) | Studies venue/category popularity, exposure and distance polarization in location-based recommenders. | Neither exposure fairness nor distance-sensitive POI evaluation is novel. |
| [Banerjee, Banik & Wörndl (2023)](https://doi.org/10.3389/fdata.2023.1168692) | Reviews individual and multistakeholder fairness in tourism recommendations. | Fair tourism recommendations are an established literature. |
| [Najafi & Costa (2026)](https://doi.org/10.1080/13683500.2026.2654066) | Audits concentration in 420 AI travel outputs across ten systems and 14 prompts. | Digital overtourism/algorithmic visibility have already been researched. Our controlled TF-IDF model is not a commercial-LLM audit. |
| [Onder et al. (2026), Tourism Economics](https://doi.org/10.1177/13548166261488140) | Conceptualizes tourism AI discovery as a possible allocation of demand and local economic benefits. | The economics motivation exists; our distinct contribution, if any, is a measurable district-level *proxy* and computation, not proof of demand allocation. |
| [OECD (2026), Korea AI Kokkok policy description](https://www.oecd.org/en/publications/oecd-tourism-trends-and-policies-2026_3fd3cd75-en/full-report/tourism-policies-priorities-and-governance_5254e93a.html) | Reports Korea Tourism Organization adjusts travel recommendation exposure by location and addresses search and selection bias. | Do not claim Korea has no location-sensitive/fairness-aware recommendation service. No evidence here that AI Kokkok uses our particular undercapture ratio. |
| [OECD (2026), social benefits of tourism](https://www.oecd.org/en/publications/oecd-tourism-trends-and-policies-2026_3fd3cd75-en/full-report/enhancing-the-social-benefits-of-tourism_43631a73.html) | Discusses distribution of tourism benefits, SMEs, community impacts and the risk of pushing crowding elsewhere. | Rank-weighted visibility alone is not local economic welfare. |

**Verification limits:** The Sánchez/Frontiers/Najafi/OECD accessible full-text sections and the published journal abstracts/metadata above were consulted. The entire 2026 Merinov & Ricci journal article should be read in full before making a final differentiating claim.

## Revised, bounded research gap for the Introduction

> Prior literature has already examined fairness in tourism recommenders, geographical exposure bias, the redirection of urban tourist attention and trade-offs with traveler utility. This study therefore does not claim to invent equity-aware travel recommendation. It instead investigates whether a within-city economic-under-capture proxy—constructed from district shares of estimated foreign visitor activity versus recorded foreign-card tourism consumption—can be incorporated into a transparent attraction re-ranking method, and what this changes in simulated district exposure and measured textual relevance. The empirical contribution is the Busan-specific operationalization and transparent policy comparison, subject to limitations in data coverage, human relevance, real transit access and the absence of observed spending outcomes.

## Boundaries and next tests

1. The archived RQ3 finding **56.41% to 70.14%** means **+13.74 percentage points of rank-weighted visibility**, not spending. The **99.06%** measure is TF-IDF text-relevance retention, not real tourist satisfaction.
2. Because district visitor activity is mobility-based and not unique individual tourists, the spending-to-activity ratio is a **proxy**, not direct per-tourist expenditure.
3. Test transit-heavy districts (especially airport-related visitor activity), commercial coverage, alternate share-gap/ratio metrics and time periods before claiming a valid economic fairness measure.
4. Finish the **second independent human-rating study** only with actual submitted ratings and appropriate supervisor ethics/consent review; never impute results.
5. Distinguish the 33-query development benchmark and the subsequent 12-query exploratory test from a future **untouched held-out** test set. Never tune on a set and then call it independent evaluation.
6. The accessibility test uses straight-line distances and must not be described as measured bus/subway journey times.
7. Request supervisor feedback on whether the manuscript should be positioned as a **computational feasibility study**, not a causal or economic-impact assessment.

### Next literature-review tasks
Full-text compare Merinov & Ricci 2024 and 2026; use citation chaining and Korean academic databases; verify Data Lab provider definitions and reuse rights; add exact in-text references to the integrated paper. This targeted review does **not** establish exhaustive novelty.

*This addition preserves all previous repository research files and should be read alongside the older preliminary literature matrix and current manuscript drafts.*

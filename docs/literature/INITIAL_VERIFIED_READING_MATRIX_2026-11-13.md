# Initial verified literature matrix — 13 November 2026

**Status: preliminary reading matrix, NOT a completed systematic review.** The titles and links below were checked using publisher, conference, institutional or indexing pages. Abstract-level summaries were used where full text was restricted. Read the complete manuscripts before representing their precise limitations or methods in the final paper.

## Closest papers and why they matter

| Paper and publication link | What the abstract or publication page supports | Relation to the Busan study | Further checks |
|---|---|---|---|
| Borràs, Moreno & Valls (2014), [Intelligent tourism recommender systems: A survey](https://doi.org/10.1016/j.eswa.2014.06.007) | Surveys tourism recommender algorithms, context, functions and techniques | Establishes tourism recommendation as a mature research area | Check newer surveys and changes since 2014 |
| Singh & Joachims (2018), [Fairness of Exposure in Rankings](https://doi.org/10.1145/3219819.3220088) | Formalizes ranking-exposure fairness and utility trade-offs | Direct conceptual basis for rank-position-weighted exposure; **ours is not the first exposure-aware reranking approach** | Compare exposure fairness definitions and assumptions |
| Abdollahpouri, Burke & Mobasher (2019), [Managing Popularity Bias in Recommender Systems with Personalized Re-Ranking](https://cdn.aaai.org/ocs/18199/18199-78818-1-PB.pdf) | Post-processing reduces recommendation popularity bias while maintaining accuracy | Close method family; distinguish economic-capture signal from item-popularity signal | Compare their re-ranking objective and evaluation |
| Abdollahpouri et al. (2020), [Multistakeholder Recommendation: Survey and Research Directions](https://doi.org/10.1007/s11257-019-09256-1) | RecSys outcomes may matter to providers, platforms and society, not just end users | Justifies evaluation of district/provider visibility alongside relevance | Define whether districts are legitimate providers/proxies |
| [A review on individual and multistakeholder fairness in tourism recommender systems](https://pubmed.ncbi.nlm.nih.gov/37234689/) (2023) | Reviews multiple kinds of fairness in tourism and stakeholder consequences | Shows **tourism fairness is not a new field** | Read full review; locate closest actual tourism implementations |
| [Bias characterization, assessment, and mitigation in location-based recommender systems](https://doi.org/10.1007/s10618-022-00913-5) (2023) | Studies venue popularity, category popularity, venue exposure and geographical distance biases | Closest to multi-bias POI reranking; relevant for geographic evaluation | Compare geographic constraint and venue-owner concepts |
| [A survey on popularity bias in recommender systems](https://doi.org/10.1007/s11257-024-09406-0) (2024) | Reviews popularity-bias concepts, mitigations, and external validity problems; notes limited field studies | Reinforces why offline exposure improvements cannot be equated to economic effects | Extract evaluation best practices |
| [Spatial concentration of intra-urban tourist activities and inter-group differences between Asian, European and North American travelers in Korean cities](https://doi.org/10.1016/j.tourman.2024.105064) (2024) | Analyzes tourist spatial concentration in Seoul, Busan and Jeju using mobile data | **Existing Busan-related concentration evidence**: must cite rather than treat concentration itself as novel | Compare spatial units, times, traveler-origin differences |
| Banerjee et al. (2025), [Modeling sustainable city trips: integrating CO2e emissions, popularity, and seasonality into tourism recommender systems](https://doi.org/10.1007/s40558-024-00303-1) | Composite sustainability indicator integrating CO2e, popularity, seasonality and an associated user study | Nearby multi-objective sustainable tourism recommendation work | Our unit is intra-city districts/POIs vs their intercity destinations; verify difference |
| [Destination (Un)Known: Auditing Bias and Fairness in LLM-Based Travel Recommendations](https://www.mdpi.com/2673-2688/6/9/236) (2025) | Audits geographic recommendation bias and proposes public-interest re-ranking governance | Very close in stated goal; our evaluated system is controlled TF-IDF, not a commercial LLM | Compare economic signal and measured outcomes before claiming novelty |
| [Digital overtourism in AI travel recommendations: evidence from a comparative analysis](https://doi.org/10.1080/13683500.2026.2654066) (2026) | Evaluates destination visibility concentration in AI travel outputs across multiple systems | Shows pre-travel digital concentration was already studied; do not claim first | Compare within-city vs region-level analysis |
| [Towards Sustainable Tourism: A Novel Comprehensive Hierarchical Multi-Criteria Evaluation Framework for Points-of-Interest Recommendations](https://doi.org/10.3233/FAIA250570) (2026) | Proposes multi-criteria POI sustainability including economic/social/environmental dimensions | Economic outcomes inside POI recommendations already discussed | Their focus is conceptual criteria vs our empirically operationalized district measure; check full text |

## Working synthesis (hypotheses to verify in a full review)

**What cannot honestly be claimed as new**
- The idea that tourism recommendation systems can reinforce popularity or spatial concentration.
- The concept of supplier/multistakeholder fairness in recommendation ranking.
- The general technique of reranking to trade user relevance for provider or geographic exposure.
- An economic dimension in tourism-sustainability recommendation.

**Narrower candidate contribution for this project, subject to fuller checking**

> An empirically operationalized *within-Busan* opportunity signal based on the **gap between district foreign-visitor share and district foreign-card-tourism-consumption share**, integrated into an interpretable relevance-preserving POI reranker, with a controlled offline exposure/relevance audit and an explicitly limited blinded human relevance pilot.

This is a **candidate** contribution, not yet a confirmed novel algorithm or a measured impact study. District tourism spending is not SME revenue; exposure is not spending.

## Next literature-review work

1. Read the full text of the closest eight papers and extract: population/location, data, fairness objective, algorithm, constraints, relevance measurement, geographic metric, user study, results, and limitations.
2. Search forward and backward citations of the 2023 tourism fairness review and 2025/2026 closest papers, including other Korean destination studies. Track search dates and databases.
3. Create a defensible gap statement **only after** deciding which adjacent works measure actual spending disparities versus visit-count popularity.
4. Seek professor feedback before claiming an original scientific contribution.

**Source integrity:** Linked abstract/publisher pages establish the existence and general scope of these papers. They do not alone establish that no earlier paper has used an equivalent economic-undercapture signal.

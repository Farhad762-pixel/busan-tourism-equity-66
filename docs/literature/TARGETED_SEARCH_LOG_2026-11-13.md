# Targeted literature verification and screening notes — 13 November 2026

This is an **initial targeted review, not a PRISMA/systematic review**. It does not establish an exhaustive search or a proven worldwide novelty claim.

## Research questions for literature screening

1. Does work measure tourism recommendation exposure by provider, district, neighborhood, or destination?
2. Does it incorporate spatial *visitation versus recorded spending* as a ranking objective, or only popularity, visitor counts, CO2, seasonality, or crowding?
3. Does it use attractions/POIs within a single city (rather than intercity itineraries)?
4. Does it measure offline textual similarity, independently human-rated relevance, geographic distance, actual route time, or downstream spending?
5. Does it audit actual deployed algorithms or a controlled researcher-built system?

## Search procedure (targeted)

- Date: 13 November 2026.
- Sources accessed: publisher and conference pages (Elsevier, Springer Nature, ACM/KDD, Frontiers, FLAIRS, MDPI, Taylor & Francis), institutional author publication listing, and Korean Tourism Data Lab documentation.
- Search topics: 'tourism recommender systems survey'; 'fairness exposure rankings'; 'multistakeholder tourism fairness review'; 'popularity mitigation re-ranking'; 'location-based recommender geographic distance bias'; 'spatial concentration tourists Busan Korean cities'; 'sustainable city tourism recommenders'; 'AI travel recommendation geographic bias and overtourism'.
- Selection: Foundational widely cited methodological papers, directly tourism-specific fairness work, geographically relevant Korean-city study, and closest recent travel-AI/sustainable recommender studies. Selection is **purposive** and can miss relevant papers.

## Confirmed bibliographic sources and scope

| Citation | Publisher or other verification URL | Relevant scope | Verification level |
|---|---|---|---|
| [1] Borràs et al. 2014 | https://doi.org/10.1016/j.eswa.2014.06.007 | Tourism-recommender methods overview | Publisher abstract and bibliographic record |
| [2] Abdollahpouri et al. 2020 | https://doi.org/10.1007/s11257-019-09256-1 | Multistakeholder recommendations | Institutional publication metadata and abstract |
| [3] Singh & Joachims 2018 | https://www.kdd.org/kdd2018/accepted-papers/view/fairness-of-exposure-in-rankings | Exposure fairness framework | Conference abstract and author full-text PDF |
| [4] Abdollahpouri et al. 2019 | https://cdn.aaai.org/ocs/18199/18199-78818-1-PB.pdf | Popularity-bias re-ranking | Conference full-text PDF |
| [5] Sánchez et al. 2023 | https://doi.org/10.1007/s10618-022-00913-5 | POI popularity, category, exposure and distance biases | Publisher open-access article |
| [6] Banerjee et al. 2023 | https://doi.org/10.3389/fdata.2023.1168692 | Tourism-specific multistakeholder fairness | Publisher open-access review |
| [7] Cheng et al. **2025** | https://doi.org/10.1016/j.tourman.2024.105064 | Tourist concentration in Busan/Seoul/Jeju | Publisher abstract, institutional bibliographic record (journal year 2025) |
| [8] Banerjee et al. 2025 | https://doi.org/10.1007/s40558-024-00303-1 | Sustainable city trips: emissions/popularity/seasonality | Publisher open-access article |
| [9] Andreev et al. 2025 | https://doi.org/10.3390/ai6090236 | LLM travel bias and re-ranking governance | Publisher open-access article |
| [10] Najafi & Costa 2026 | https://doi.org/10.1080/13683500.2026.2654066 | Digital overtourism / travel AI visibility | Publisher abstract/full-text landing page |

## Official data caveats discovered during verification

Korea Tourism Data Lab's foreign visitor dataset is estimated from mobile signals. It warns against treating the figures as exact unique tourists, indiscriminately summing district values into a city total, or assuming exact purpose-of-visit identification. District-level shares in this study are normalized **estimated district-visit indicators**, not mutually exclusive tourists. Card consumption has distinct provider coverage and can be revised; historical source-definition changes require checking.

- Official methodology: https://datalab.visitkorea.or.kr/datalab/portal/getMetaInfoList.do
- Change notice: https://datalab.visitkorea.or.kr/site/portal/ex/bbs/View.do?bcIdx=302575&cbIdx=1135&pageIndex=1

## Key conclusion of this review stage

The **general idea** of tourism fairness, geographic recommendation concentration, and post-hoc reranking is **not novel**. The manuscript proposes a narrower, testable empirical contribution using a **foreign-card-tourism-consumption versus estimated visitation activity** indicator in a Busan district-level ranking simulation. This remains *provisional*: an exhaustive related-work review is not yet available.

## Tasks before declaring a robust research gap

- Search Scopus, Web of Science, ACM Digital Library, IEEE Xplore, Google Scholar and Korean scholarly databases when available; log actual search dates and filters.
- Review full texts, especially the 2023 location bias paper, 2023 tourism fairness review, 2025 sustainable city trip paper, and 2025/2026 AI-audit studies.
- Perform forward/backward citation tracing. Identify direct comparable work with district-level spending, card transactions, or economic benefit metrics.
- Distinguish algorithm fairness measures from actually observed tourism revenue or distributional outcomes.
- Verify article metadata/author spellings against downloaded originals; obtain supervisor feedback.

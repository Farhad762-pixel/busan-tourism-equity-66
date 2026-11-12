# Methodology and measurement definitions

## RQ1 — Tourism economic distribution

**Data:** Korea Tourism Data Lab, 16 Busan administrative districts, January 2022–December 2025 (48 monthly observations per district; 768 district-month rows). Visitor activity and foreign-tourist credit-card consumption are aligned by district and month; spending is in million KRW.

- `visitor_share(d) = visitors(d) / total_visitors_in_Busan`
- `spending_share(d) = foreign_card_spending(d) / total_foreign_card_spending_in_Busan`
- `benefit_capture_ratio(d) = spending_share(d) / visitor_share(d)`
- `economic_undercapture(d) = max(0, 1 - benefit_capture_ratio(d))`

The primary equity score uses **2024–2025** aggregates; broader 2022–2025 data serve descriptive and robustness analyses. These indicators measure a *relative difference* between spending and visitor shares; they do not measure real SME income, poverty or causal economic loss.

## RQ2 — Controlled baseline algorithm

207 official attractions were indexed by textual metadata (name/title, subtitle, place, district, address and transport information). TF-IDF with English stop-word filtering and cosine similarity scored tourist search queries. From **48 predefined queries / 12 intent categories**, **33** with at least five attractions having positive cosine similarity were evaluated. The baseline returns up to 10 attractions per query; 288 recommendations were produced across the 33 valid queries.

Ranked exposure weights: `w(rank) = 1/log2(rank+1)`, where first rank is 1. District exposure share is the district's sum of weights divided by all ranking weights.

The test measures an **offline research recommender**, not actual platform recommendation frequency or tourist clicks.

## RQ3 — Economic-equity-aware re-ranking

From the baseline's top 50 positive-relevance candidates, re-rank each attraction `i` using:

`final_score(i) = text_relevance(i) * [1 + lambda * economic_undercapture(district(i))]`

Compare `lambda` = 0, 0.5, 0.8, 1.0 and 2.0. A multiplicative formula prevents zero-relevance attractions from receiving a positive final score through the economic term alone.

Evaluation: mean TF-IDF cosine relevance by query; relevance retained vs baseline; rank-weighted exposure of economically undercapturing districts; exposure of five screened candidate districts; exposure Gini and HHI; district coverage; overlap with baseline.

Five preliminary candidate districts: **Dong-gu, Geumjeong-gu, Nam-gu, Seo-gu, Yeongdo-gu**. They met positive undercapture plus an attraction-readiness threshold in the saved study.

## Accessibility sensitivity

Additional offline experiments restrict the **same baseline and re-ranking framework** to attractions within Haversine straight-line distances of approximate Busan Station, Seomyeon Station and Haeundae Station starting points, at several caps including 15 km.

**Do not describe this as transit travel time.** Road/path distance, bus/subway schedules, interchange time, operating hours and tourist preferences have not been independently evaluated.

## Limitations

- No measured tourist spending change or causal effect; exposure is simulated.
- TF-IDF cosine similarity is **not** independent human-rated relevance or satisfaction.
- Benchmark queries are researcher-defined; some queries have too few positive matches.
- Visitor activity is an estimate; spending is foreign credit-card tourism consumption, not all spending.
- Public release of complete source-derived datasets requires a rights review.

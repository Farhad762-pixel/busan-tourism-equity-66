# Independent district economic context from official statistics (28 Nov 2026)

**Status:** New secondary data and exploratory external-signal audit. The public aggregate dataset is in `data/external/official_sbr_busan_tourism_sector_2020_2024_rounded.csv`. No original KTO Data Lab source files, individual firms, cards, credentials, or survey responses are being committed.

## Official independent data added

On **24 November 2026**, Korea's **Southeastern Regional Data Office** published the report *데이터로 살펴본 부울경 관광 업종 변화* using Statistics Business Register (SBR) data.

- Official release: https://mods.go.kr/board.es?act=view&bid=11802&list_no=448027&mainXml=Y&mid=a60301010100
- Official report and 16-district tables: https://www.mods.go.kr/boardDownload.es?bid=11802&list_no=448027&seq=4
- Published figures transcribed: 16 districts × 2020–2024 annual tourism-related establishment counts and total sector sales; 2024 district tourism-sector employment.
- **Units:** firms in THOUSANDS (rounded to 0.1); annual sector sales in TRILLION KRW (rounded to 0.1); employment in THOUSANDS (rounded to 0.1). District rounded totals can disagree with the separately rounded city totals.
- **Not the same population** as foreign-tourist credit-card spending: these SBR tourism-related sectors include transactions from residents/non-tourists. They do not identify tourist flows caused by recommendation systems, or SME-only revenues.

## Descriptive join with the private Busan research panel

The combined research database already has 16 districts × 48 months and 207 attraction records. Calculating **2024-only** undercapture from the private panel and merging district-level SBR 2024 values yields:

| External variable | Pearson r vs 2024 undercapture | Spearman rho | Pearson excluding Gangseo |
|---|---:|---:|---:|
| SBR tourism-sector total sales | **−0.501** | −0.527 | −0.662 |
| SBR tourism-sector establishment count | −0.518 | −0.381 | −0.487 |
| SBR tourism-sector employment | −0.526 | −0.282 | −0.575 |
| SBR sector sales per establishment (approximate ratio of rounded totals) | **−0.049** | −0.388 | −0.660 |

Small n=16, cross-sectional 2024, SBR rounded to one decimal, multiple comparisons and non-identical source populations: this is **descriptive external context, not validated economic deprivation or causal recommender impact**. A descriptive 5,000-sample percentile bootstrap on total sector sales correlation yielded a 95% interval around **[−0.847, +0.105]**; it crosses zero. The indicator's link to sales PER BUSINESS is particularly weak in all 16 districts. **Gangseo**, with high undercapture but 5.0 trillion KRW broad sector sales in 2024, is an important counterexample to simplistic interpretations.

## Programmatic expansion available but not yet executed live

Official data.go.kr KTO endpoints:

1. `https://apis.data.go.kr/B551011/AreaTarResDemService/areaTarSvcDemList` — district/month business-category consumption indicators and navigation searches. Official docs: https://www.data.go.kr/data/15152138/openapi.do
2. `https://apis.data.go.kr/B551011/AreaTarDemDsService/areaTarExpDsList` — consumption/demand intensity. Official docs: https://www.data.go.kr/data/15151868/openapi.do
3. Optional future business-location API: https://www.data.go.kr/data/15012005/openapi.do — shop category/geolocation; would require rigorous geospatial joining and source review.

**Important:** these APIs require data.go.kr-specific service authorization. No authenticated request was performed; dry-run tests are not data collection. The researcher received a ZIP including a tested API collector, private-file join, graphics and detailed instructions. API credentials must be supplied locally as an environment variable, never pasted into public documents or GitHub. 2024 sector sales cannot be treated as foreign tourist spending or as treatment-induced economic effects.

## Publication claim

This new dataset strengthens the paper with an **independent external economic-context sanity check**. It also exposes limits of the district proxy. The original ranking formula is unchanged. Any novelty claim must remain bounded to a particular empirical indicator and reproducible offline exposure experiment. Independent tourist usefulness and causal spending changes require genuine new people/outcomes, which no retrospective public API can fabricate.

## Reproduction and release

The detailed 2024 private-panel join, source SHA-256 and analytic scripts remain in the user's local research validation package. Public GitHub adds the independently published aggregate SBR source only. Have the professor review reuse rights, construct validity and the role of Gangseo before integrating the diagnostic into the final manuscript.

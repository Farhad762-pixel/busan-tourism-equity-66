# Data dictionary and interpretation

Audit date: 2026-11-13 (Asia/Seoul). This dictionary describes available files;
it does not certify the unavailable 768-row panel. Exact headers, row counts,
missing values, date ranges and hashes are in the generated local inventory:
`python scripts/verify_repository.py --output work/audit.json`.

## Processed attractions: 207 rows, 14 columns

Source: Busan Metropolitan City, [Attractions Information Service](https://www.data.go.kr/data/15063481/openapi.do).
`src/clean_attractions.py` maps fields from the existing `getAttractionEn.item`
JSON array, removes exact duplicate full raw records, and preserves order. The
current JSON has 207 distinct records; the CSV is an exact projection, with no
additional imputations or translations. Snapshot download date is not recorded.

| CSV variable | Raw API field | Meaning / unit | Empty rows |
|---|---|---|---:|
| uc_seq | UC_SEQ | Official content identifier; API response calls it `id` | 0 |
| main_title | MAIN_TITLE | Attraction content name; mixed-language source text; response `name` | 0 |
| subtitle | SUBTITLE | Subtitle, text | 66 |
| district | GUGUN_NM | English district label; 16 distinct values | 0 |
| latitude | LAT | Latitude, decimal degrees; coordinate reference not explicitly verified | 0 |
| longitude | LNG | Longitude, decimal degrees; coordinate reference not explicitly verified | 0 |
| address | ADDR1 | Address text | 1 |
| place | PLACE | Place label, text | 6 |
| transport_info | TRFC_INFO | Narrative transport guidance, not travel-time measurements | 11 |
| homepage_url | HOMEPAGE_URL | URL string | 118 |
| opening_info | USAGE_DAY_WEEK_AND_TIME | Operating schedule, unstructured text | 30 |
| usage_amount | USAGE_AMOUNT | Fee description, unstructured text; not a numeric price field | 72 |
| image_url | MAIN_IMG_NORMAL | Image URL only; image rights are not independently established | 0 |
| thumbnail_url | MAIN_IMG_THUMB | Thumbnail URL only | 0 |

Raw-only fields are retained without modification: `CNTCT_TEL` (published venue
contact), `HLDY_INFO` (holiday text), `ITEMCNTNTS` (long description), `TITLE`
(article title), `USAGE_DAY` (operating-day text), `MIDDLE_SIZE_RM1` (facilities
text). These are not currently indexed by the API baseline. Envelope fields
`header`, `numOfRows`, `pageNo`, `totalCount` describe API status/pagination;
`item` contains records. The 10-item raw JSON is a partial response, not a second
complete dataset. The 207-item raw JSON is the current cleaner input.

## Existing Korea Tourism Data Lab CSV families

The original download settings, download dates and foreign-tourist filter
provenance are absent. Filenames alone do not prove the selected population.
No existing raw files are rewritten or newly licensed by this audit.

| Files | Fields / units | Scope and caution |
|---|---|---|
| foreign_visitors_raw.csv | 지역: region; 방문자 수: estimated visitor activity, count; 기준년월일: YYYYMM | 12 Busan city totals, 202510–202609; not 768 district-month rows |
| foreign_spending_raw.csv | Same exact fields and bytes as visitor file | Mislabeled: not usable as spending; preserve as evidence, reacquire correct export |
| haeundae_total_foreign_spending_2022–2025.csv | 기준년월일: YYYYMM; 지역: region; 지역 관광소비액(백만원): regional consumption, **million KRW** | 12 rows per year; Haeundae only; foreign-card filter needs source receipt |
| haeundae_foreign_spending_by_industry_2022–2025.csv | 기준년월일: YYYYMM; 업종별 구분: industry group; 소비액(천원): consumption, **thousand KRW** | 94/95/96/96 rows; do not merge with million-KRW totals without conversion; missing combinations need provider explanation |
| haeundae_foreign_spending_by_country_2022–2025.csv | 국가: country; 소비 비율: consumption ratio | 34/33/33/33 rows; ratio scale must be confirmed against provider documentation |
| haeundae_foreign_spending_types_2022–2025.csv | 카테고리 대분류/중분류: major/minor categories; 카테고리 대분류 소비 비율 / 카테고리 중분류 소비 비율: category ratios | 19 rows/year; denominator and ratio scale not independently confirmed |
| master_literature.csv | paper_id, title, year, authors, journal, research_problem, data, method, main_result, limitation, research_gap, relevance_to_my_topic, url | Header-only template: zero references; no citations verified or invented |

## Derived ranking and archived-table variables

| Variable | Definition / unit / status |
|---|---|
| relevance_score | TF-IDF cosine similarity, dimensionless; six text fields above, English stop words; mixed-language corpus limits English matching |
| equity_score (API) | `(max district attraction count - district count)/(max - min)`, range 0–1; equal counts yield 0; computed on all 207 rows |
| equity_measure | Always `prototype_attraction_distribution_proxy` in current API |
| equity_weight | Current API mixing weight, 0–1, default 0.20 |
| final_score (API) | `(1-equity_weight)*relevance_score + equity_weight*equity_score`; positive-relevance candidates from top 50 only |
| visitor_share / spending_share | District visitor/spending aggregate divided by corresponding Busan total; archived research, panel unavailable |
| benefit_capture_ratio | `spending_share / visitor_share`; zero visitor-share convention needs archived script |
| economic_undercapture | `max(0, 1-benefit_capture_ratio)`; archived economic signal, not API proxy |
| lambda | Archived multiplicative policy strength; **not interchangeable** with API `equity_weight` |
| mean_relevance / mean_query_relevance | Archived text-relevance aggregate; documented as query mean, original weighting must be checked from missing code |
| relevance_retained | Policy mean relevance / baseline mean relevance, ratio; multiply by 100 for percent |
| undercapture_exposure | Archived rank-weighted exposure share for positive-undercapture districts, 0–1 |
| candidate_exposure | Rank-weighted share for the five screened districts listed in methods |
| yeongdo_seogu_exposure | Rank-weighted share for Yeongdo-gu and Seo-gu combined |
| undercapture_gain_pp | `100*(policy exposure - baseline exposure)`, percentage points |
| exposure_gini | Gini over all 16 district exposure shares, including zeros; 0 indicates equal exposure |
| HHI | Sum of squared district shares; 1/16 indicates equal exposure across 16 districts |
| district_coverage | Number of districts with nonzero exposure |
| query_count / eligible_query_count | Number of queries surviving study eligibility rule; original queries missing |
| recommendations | Total returned items across eligible queries, not number of unique attractions |
| origin / distance_cap_km | Archived starting station label and Haversine eligibility cap, kilometers; not route time |
| Baseline / Equity / change | District exposure shares and Equity minus Baseline in archived figure table |
| pooled_pearson / pooled_spearman | Reported correlation over district-month rows; not recomputable without panel |
| share_pearson / share_spearman | Reported share association; exact grouping must be confirmed from script |
| average_monthly_pearson / average_monthly_spearman | Reported monthly-correlation averages; original handling of missing/constant groups unknown |

The complete research JSON schema and manuscript variables cannot be documented
as verified until the referenced archive is supplied. Preserve the original
JSON and create a separate schema mapping rather than overwriting it.


### Additional archived robustness/threshold fields

`economic_signal` names the reported ratio/share-gap/log-ratio/rank-based
specification; exact transformations await original code. `relevance_retention`
and `actual_relevance_retention` are ratios relative to baseline;
`relevance_loss = 1 - relevance_retention`. `minimum_relevance_retention` is the
reported policy-selection threshold. `undercapture_exposure_gain` and
`undercapture_gain` are **share differences**, not percentage points;
`yeongdo_seogu_gain` and `robust_core_gain` are Yeongdo/Seo share differences;
`candidate_gain` is the five-candidate-district share difference. Multiply these
by 100 for percentage points. `gini_change` is policy Gini minus baseline Gini.
`mean_jaccard` reports baseline/policy list-set overlap (intersection / union),
but query aggregation must be checked in the archived code. RQ1 table
`metric,value` rows also include `top_visitor_district`, `top_visitor_share`,
`top_spending_district`, `top_spending_share` and `lower_benefit_candidates`;
these are labels, 0–1 shares and a candidate count, respectively.

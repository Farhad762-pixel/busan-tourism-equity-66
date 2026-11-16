# Busan Research: From Data to Paper — Professor Guide

> This is a faithful **text transcription** of the original PDF dated 15 November 2026, added to GitHub so the research explanation is accessible. Tables are retained as fixed-width text where applicable. The original PDF layout may differ. The document is a supervisor discussion draft, not a final manuscript.

## Original PDF — Page 1

```text
                                                                              BUSAN TOURISM EQUITY / RESEARCH GUIDE



From official data to a tourism recommendation research paper
A simple, evidence-based explanation for the researcher and supervisor
Prepared from the saved Busan project checkpoint and accessibility experiment, with a targeted review
of academic studies. This is a learning and supervisor-review document, not a final manuscript or a
certification of a never-before-studied research gap.

A. The project in one minute
We studied whether the benefits recorded from foreign tourism are concentrated in certain Busan
districts, and whether a relevance-based recommendation system can give economically undercapturing
districts more visibility without hurting recommendation quality. We collected 16-district monthly
foreign-visitor and foreign-card-spending indicators for 2022–2025, assembled 207 official attraction
records, and built an offline text-ranking experiment. A relevance-preserving economic re-ranking
increased simulated weighted exposure to positive-undercapture districts from 56.41% to 70.14%. This is
an algorithmic visibility result, not an observed spending effect.

B. The exact research journey — in order
1. Chose the research question
Why are recorded foreign tourism spending and foreign visitor activity distributed differently in Busan,
and can a recommendation system respond responsibly?
Evidence: Working problem statement and RQ1–RQ3.


2. Downloaded monthly data
Korea Tourism Data Lab exports for 16 districts × 4 years × 2 indicators (128 ZIPs reported in the original
project).
Evidence: Raw downloads were verified in the original workflow; they are not included in the saved checkpoint ZIP.


3. Cleaned and joined files
Python matched foreign visitor activity and foreign-card spending using district and month keys.
Evidence: data/processed/busan_foreign_tourism_master_2022_2025.csv


4. Validated the master panel
All 16 districts × 48 months are present; 768 unique district-month rows; no missing visitor or spending
values.
Evidence: Saved master CSV and docs/data_pipeline_status.md.


5. Added attraction information
Official Busan attractions with titles, descriptions, districts, addresses and coordinates.
Evidence: data/processed/busan_attractions.csv, 207 records.




                                                                   Supervisor discussion draft • 15 November 2026 | Page 1
```

## Original PDF — Page 2

```text
                                                                                 BUSAN TOURISM EQUITY / RESEARCH GUIDE

6. Calculated tourism shares
Computed each district’s share of the sum of estimated visitor activity and recorded foreign-card
spending.
Evidence: results/tables/district_summary_2022_2025.csv.


7. Measured geographic concentration
Calculated Gini, HHI, rankings and visitor–spending associations; compared districts.
Evidence: results/tables/monthly_concentration_2022_2025.csv and RQ1 tables.


8. Built the baseline recommender
TF-IDF cosine text relevance compared queries such as “beautiful beach” to attraction descriptions.
Evidence: src/api/main.py (historical MVP); results/tables/rq2_baseline_*.csv.


9. Derived economic-undercapture scores
Defined u = max(0, 1 − spending share / visitor-activity share). Primary equity score uses 2024–2025
totals.
Evidence: results/tables/teos_primary_2024_2025.csv.


10. Defined a benchmark
48 researcher-written searches in 12 tourism categories; 33 had at least five positive text matches.
Evidence: results/tables/rq2_benchmark_query_quality.csv.


11. Tested the economic re-ranker
Re-ranked at most 50 positive-relevance candidates, returning up to ten results with a district economic
multiplier.
Evidence: results/tables/rq3_extended_policy_frontier.csv and recommendation tables.


12. Checked robustness and distance
Alternative economic definitions and a separate experiment with 5/10/15/25-km straight-line geographic
limits from three approximate station origins.
Evidence: RQ3 robustness tables; Busan_Accessibility_Experiment_Results.zip.


13. Produced research outputs
CSV and JSON datasets, diagrams, GitHub research portal, results report and draft manuscript.
Evidence: Saved project and public repository; check which specific inputs are safe to publish.


C. How to explain the data with real examples
Example row: the cleaned January 2022 Jung-gu record contains 3,371 estimated foreign-visitor activity
units and 303 million KRW in recorded foreign tourism card spending. This is one district–month
observation. It is not a count of unique tourists or all spending.

Example district-level indicator: in 2024–2025, Yeongdo-gu represented approximately 7.48% of the sum
of Busan district foreign-visitor activity but about 1.07% of covered foreign-card tourism spending.
                                                                      Supervisor discussion draft • 15 November 2026 | Page 2
```

## Original PDF — Page 3

```text
                                                                                   BUSAN TOURISM EQUITY / RESEARCH GUIDE

Dividing 1.07% by 7.48% gives approximately 0.143; subtracting from 1 gives an undercapture score of
approximately 0.857.

Mathematically, the ratio of spending share to visitor-activity share is just a normalized form of
recorded spending per estimated district visit. The idea of spending intensity is not itself novel, and its
components are not measured under identical collection systems.
 Recorded/derived data                                          Interpretation / limitation

                                                                Mobile-derived estimate of district activity, not unique city
 District foreign-visitor activity
                                                                visitors.
                                                                Credit-card tourism consumption, not total expenditure or
 Foreign tourism spending
                                                                business profit.
 Attraction description and location                            207 official POIs; not every business or attraction in Busan.
                                                                Relative mismatch between the two recorded district
 Economic undercapture
                                                                indicators; not proof of poverty or lost revenue.
                                                                Similarity of query text and attraction text; not
 TF-IDF relevance
                                                                independent tourist satisfaction.
                                                                Geographic proximity proxy, not transit duration, routes
 Straight-line radius
                                                                or cost.




D. What the results actually show
 Test / question                           Result                                     Meaning

                                                                                      These two districts account for
                                           Haeundae 29.89%; Busanjin 26.89%
 Tourism spending concentration                                                       ~56.78% of recorded foreign-card
                                           (2022–2025).
                                                                                      spending.
                                                                                      A positive relationship, not evidence
                                           Pearson 0.5726 across pooled district-
 Visitor–spending association                                                         about what caused spending
                                           months.
                                                                                      concentration.
                                           Undercapture exposure 56.41% →             The designed re-ranking shifts
 Baseline vs equity, lambda = 0.8
                                           70.14% (+13.74 percentage points).         simulated visibility.
                                                                                      The algorithm retains its own text-
 Text relevance retained                   99.06% of baseline TF-IDF relevance.       matching score, not demonstrated
                                                                                      satisfaction.
                                                                                      A higher exposure score did not
 District coverage                         15 of 16, for both baseline and equity.    increase overall district coverage
                                                                                      here.
                                           At 15 km, +10.56 to +11.93 pp              Still an offline straight-line distance
 Distance constrained
                                           exposure gains from three origins.         check, not route convenience.




E. A new, targeted weakness revealed by the same data
An additional exploratory audit was independently run using the original 48 queries, 207 official POIs
and the saved five policy candidate districts. This is a diagnostic on already-used development queries,
not a new held-out evaluation.
 Specific diagnostic                                            Verified count

 Research queries initially prepared                            48
 Queries with at least five positive text matches               33

                                                                      Supervisor discussion draft • 15 November 2026 | Page 3
```

## Original PDF — Page 4

```text
                                                                                BUSAN TOURISM EQUITY / RESEARCH GUIDE

 Specific diagnostic                                          Verified count

 Queries failing that threshold                               15 of 48 (31.25%)
 Eligible queries with ZERO suitable screened-district POIs
                                                              4 of 33
 among top 50 text matches
                                                              historic place; local art; local food experience; spiritual
 Those four queries
                                                              place
 At 15 km from Busan Station                                  30 eligible queries; 3 lack target candidates
 At 15 km from Seomyeon Station                               32 eligible queries; 3 lack target candidates
 At 15 km from Haeundae Station                               27 eligible queries; 2 lack target candidates



Interpretation: the algorithm cannot promote attractions that are absent from its eligible candidate pool.
This suggests that the actual availability of recommendable POIs, query type and geographic eligibility
must be analyzed before claiming an economic-equity policy is useful. “No matching candidate” means
none in THIS catalog/model, not no real places in Busan.

F. Closest published work — what is already known
Banerjee, Banik & Wörndl (2023)
Reviews consumer, item-provider, platform and societal fairness in tourism recommendation; fairness is
already studied.
https://doi.org/10.3389/fdata.2023.1168692


Sánchez, Bellogín & Boratto (2023)
Evaluates popularity, exposure and geographical-distance bias in location-based recommenders; bias
mitigation is not new.
https://doi.org/10.1007/s10618-022-00913-5


Merinov & Ricci (2024; 2026)
Simulated urban tourism promotions can improve tourist utility and reduce crowding, with important
trade-offs.
https://doi.org/10.1016/j.asoc.2026.114582


Generosi and colleagues (2025)
Built and evaluated a recommender platform to give marginal Italian destinations more attention.
https://doi.org/10.1007/s40558-025-00327-1


CAPRI-FAIR (2024)
Balances provider exposure, user precision and distance in POI recommendations.
https://arxiv.org/abs/2406.03109


Dietz, Sánchez & Bellogín (2025)
Shows POI recommender outputs depend on popularity, check-ins and dataset properties; evaluation
details matter.
https://doi.org/10.1007/s40558-024-00304-0

                                                                      Supervisor discussion draft • 15 November 2026 | Page 4
```

## Original PDF — Page 5

```text
                                                                      BUSAN TOURISM EQUITY / RESEARCH GUIDE

Dalir (2026)
Simulates tourism economic/spending effects of AI recommendation in a different model; economic
simulation is not new.
https://doi.org/10.1007/s10796-026-10818-z


Korea Tourism Organization API (2025–26)
Already describes tourism consumption intensity including spending relative to visit volume.
https://www.data.go.kr/data/15151868/openapi.do


Najafi & Costa (2026)
Finds concentrated destination visibility in AI travel outputs; digital overtourism is already a research
topic.
https://doi.org/10.1080/13683500.2026.2654066


G. Three possible gaps, ranked by fit with your existing data
1. Strongest proposed main gap: the economic-targeting feasibility gap
Question: A district can look economically undercapturing, but does the recommender have enough
relevant and geographically reachable attractions for each tourist search to help? If not, where is the
actual bottleneck? This uses all existing data, has actionable implications for destination management
and is directly motivated by the four no-target search cases above. Similar general constraints have been
studied, so originality of the exact combined Busan audit remains to be verified.

2. Essential comparison: does the economic signal beat ordinary geographic diversification?
Question: If the only purpose is to expose less represented districts, why not just spread
recommendations across districts? Compare relevance-only, inverse-attraction-count / geographic-
spread, and economically targeted re-ranking under identical candidates, distance limits and matched
relevance retention. If economics does not outperform simple geographic diversity, report that negative
result. This is the best experiment to rule out the obvious “you boosted what you measured” objection.

3. Important validity check: false economic opportunity from imperfect data
A relatively low card-spending-to-visitation ratio may reflect airport/transit activity, payment coverage
or district business mix rather than an actionable economic need. Test normalization changes, excluding
Gangseo-gu, alternative 2022–2023 vs 2024–2025 definitions and district inclusion. Making strong
economic policy claims would require additional merchant/transit evidence.

H. Recommended one-paper positioning
Provisional title: “When Does Spending-Intensity-Aware Tourism Re-Ranking Add Value? A Feasibility
and Geographic-Diversification Audit in Busan, South Korea.”

Research question 1: Which Busan districts differ in estimated foreign-visitor activity and covered
foreign tourism card spending?

Research question 2: When do visitor searches have enough suitable, geographically eligible attractions
in economically undercapturing districts?
                                                            Supervisor discussion draft • 15 November 2026 | Page 5
```

## Original PDF — Page 6

```text
                                                                                       BUSAN TOURISM EQUITY / RESEARCH GUIDE

Research question 3: At comparable relevance, does the spending-intensity signal improve targeting
more than simple geographic diversification?

Suggested controls: (a) relevance-only; (b) non-economic geographic diversity; (c) inverse POI catalog
size; (d) economic spending-intensity proxy; (e) distance-constrained variants. Report how many queries
have zero target candidates, feasibility headroom, relevance changes, exposure allocation and failure
cases.

This remains a controlled computational feasibility study. New field surveys, transaction records or
platform agreements would be required to claim actual spending impact. A truly untouched set of
queries and independent human relevance ratings are priorities for publishability.

I. How to search Google Scholar from your Mac
Google Scholar is a web search service. You can use Terminal to open searches in your browser, but that
does not prove a topic is never studied; check the newest papers, “Cited by,” and full texts manually.
Scholar does not provide a generally supported public search API for unrestricted automatic research
extraction.

Paste the following in Mac Terminal (it opens Google Scholar tabs, and does not change your project):
python3 - <<'PY'
import subprocess, urllib.parse
terms = [
    'tourism recommender fairness economic spending exposure',
    'tourism recommender geographic diversification relevance tradeoff',
    'point of interest recommendation feasibility accessible fairness',
    'Busan tourism credit card spending foreign visitor districts',
    '관광 추천 형평성 방문량 대비 관광 소비 지출'
]
for term in terms:
     url = 'https://scholar.google.com/scholar?q=' + urllib.parse.quote_plus(term)
     subprocess.run(['open', url], check=False)
PY

Scholar Search Help: https://scholar.google.com/intl/en-us/scholar/help.html

J. The next five steps — no new research topic required
1. Confirm the professor accepts the narrower aim: actionable economic targeting, not claiming the
       invention of fair tourism recommendation.
2. Freeze the 2022–2023/2024–2025 indicator definitions and develop a new unseen tourist-query
       evaluation set.
3. Run four matching baselines using the same eligible attractions and comparable relevance tolerance.
4. Add blinded, consented human relevance judgments and clearly labeled travel-distance screening;
       actual public transit is optional but preferable.
5. Write the Introduction and Discussion around what works, what fails and why; verify full-text prior
       art and data licensing before public release.




                                                                             Supervisor discussion draft • 15 November 2026 | Page 6
```

## Original PDF — Page 7

```text
                                                                         BUSAN TOURISM EQUITY / RESEARCH GUIDE

K. Honest 90-second presentation script
“Professor, I selected a tourism-spending inequality problem within Busan. I collected monthly district
foreign-visitor and foreign-card tourism spending indicators for 2022–2025 and cleaned them into 768
district-month rows. I added 207 official Busan attraction records. I calculated district visitor and
spending shares, concentration indexes and relative spending-intensity shortfalls. I then built a simple
text-based recommendation system and tested an economic re-ranking across 33 eligible tourist
searches. This increased simulated exposure for undercapturing districts while mostly preserving the
algorithm’s text relevance, but it does not prove higher spending. After examining related studies, I
realized the stronger research question is whether the system has enough suitable and geographically
reachable attractions to make that economic policy actionable—and whether the economic signal adds
value beyond simply diversifying districts. An exploratory audit already found four eligible searches
with no matching attraction from the five selected districts in the model’s candidate pool. I would
appreciate your advice on this narrower contribution and the comparison experiments.”

Research integrity note: The project used AI assistance in coding and drafting. The researcher should
understand and verify all analyses, explain which parts were AI-assisted, and follow the university’s
disclosure requirements. Do not describe simulated visibility or automatic similarity scores as observed
economic effects or measured tourist satisfaction.

L. Quick glossary for professor questions
 Term                                                  Simple meaning

 Observation                                           One row of recorded data; here, one district in one month.
                                                       Making files consistent and checking for missing or
 Data cleaning
                                                       duplicate records.
                                                       A district’s part of the total estimated visitor activity across
 Visitor share
                                                       districts.
                                                       A district’s part of the total recorded foreign-card tourism
 Spending share
                                                       consumption.
                                                       A way to turn words in attraction descriptions and
 TF-IDF
                                                       searches into scores.
                                                       The ordinary relevance-only model against which a
 Baseline
                                                       changed model is tested.
                                                       Reordering already eligible attractions; λ controls strength
 Re-ranking / λ
                                                       of economic weighting.
                                                       How often, and how highly, a district appears in model-
 Exposure
                                                       generated recommendation lists.
                                                       Whether the catalog contains suitable attractions that
 Feasibility
                                                       meet query and geographic constraints.
                                                       A focused question that published work has not
 Literature gap
                                                       adequately resolved; not necessarily a never-seen idea.



If the professor asks how you used AI, explain truthfully which scripts and text were AI-assisted, what
you ran yourself, and which input files and numbers you independently checked.




                                                             Supervisor discussion draft • 15 November 2026 | Page 7
```

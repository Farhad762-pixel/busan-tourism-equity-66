# busan-tourism-equity-66
Business Analytics research on algorithmic tourism visibility and foreign-tourist spending concentration in Busan.
# Algorithmic Visibility and Tourism Spending Inequality in Busan

## Working Title

**Algorithmic Visibility and Tourism Spending Inequality:
An Economic-Equity-Aware Recommendation Framework for Busan**

## Main Research Question

Do tourism recommendation systems disproportionately recommend Busan areas
that already capture high levels of foreign-tourist activity and spending,
and can an economic-equity-aware re-ranking system broaden exposure to
suitable lower-benefit areas without substantially reducing recommendation
relevance or travel convenience?

## Research Problem

International tourism in Busan is increasing rapidly, but tourism activity
and foreign-tourist spending may remain concentrated in a limited number
of major destinations and commercial areas.

Digital tourism recommendation systems may also favor already-popular
destinations because those places have more reviews, searches, visits,
online content, and historical interaction data.

This may create a feedback loop:

Popularity
→ More digital visibility
→ More recommendations
→ More tourists
→ More spending
→ More popularity

At the same time, other high-quality and accessible tourism areas may
receive much less recommendation exposure and lower tourism-related
economic benefits.

This research investigates whether recommendation exposure corresponds
with existing tourism activity and spending concentration in Busan.

It will then test whether an economic-equity-aware re-ranking system can
broaden exposure to suitable lower-benefit areas while preserving
recommendation relevance and travel convenience.

## Research Questions

### RQ1
How geographically concentrated are foreign-tourist visits and spending
across Busan?

### RQ2
To what extent does tourism recommendation exposure correspond to existing
foreign-tourist activity and spending concentration?

### RQ3
Can an economic-equity-aware re-ranking model broaden exposure to suitable
lower-benefit areas without substantially reducing recommendation relevance
or travel convenience?

## Planned Data

1. Foreign-tourist spending by Busan district
2. Foreign visitor activity by Busan district
3. Busan tourism attractions / POIs
4. Restaurants and tourism-related local businesses
5. Tourism recommendation outputs
6. Geographic coordinates and accessibility information
7. Tourist preference / behavior data if publicly available

## Planned Analysis

1. Measure foreign-tourist spending concentration
2. Measure foreign visitor concentration
3. Measure recommendation exposure
4. Compare recommendation exposure with spending and visitor concentration
5. Build a baseline tourism recommendation model
6. Build an economic-equity-aware re-ranking model
7. Compare both models

## Main Evaluation Metrics

- Recommendation relevance
- Geographic coverage
- Recommendation exposure concentration
- Foreign-tourist spending concentration
- Travel distance / convenience
- Exposure of lower-benefit tourism areas

## Important Research Limitation

The study will measure recommendation exposure and potential redistribution
of tourism visibility.

Unless real transaction data from an intervention are available, the study
will not claim that increased recommendation exposure directly causes higher
business revenue.

## Professor-Ready MVP

This FastAPI MVP uses the real **207 Busan attractions** in
`data/processed/busan_attractions.csv`, reading the existing data without modifying it.
Baseline recommendations use TF-IDF and cosine similarity across attraction
titles, subtitles, places, districts, addresses, and transport information.

The equity-aware model is currently a prototype. Its equity score uses attraction
distribution only: districts with fewer attractions in this dataset receive a
higher normalized score, labeled `prototype_attraction_distribution_proxy`.
This proxy measures dataset representation, not real economic inequality.
Future research will replace it with real foreign-tourist spending, visitor
activity, algorithmic visibility, and accessibility data.

The prototype re-ranks only positive-relevance attractions within the baseline's
top 50, using `final_score = (1 - equity_weight) * relevance_score + equity_weight * equity_score`.
It may return fewer results than requested when there are insufficient positive
matches. The default limit is 10 and the default equity weight is 0.20.

From the repository root, install dependencies and start the server:

```bash
python -m pip install -r requirements.txt
python -m uvicorn src.api.main:app --reload
```

Open Swagger UI at <http://127.0.0.1:8000/docs>.

Available endpoints:

- `GET /api/health` — application health.
- `GET /api/attractions` — all 207 attractions; optional `district` filter.
- `GET /api/recommend/baseline` — `query` and optional `limit`.
- `GET /api/recommend/equity` — `query`, optional `limit`, and `equity_weight` (0–1).
- `GET /api/compare` — the same inputs, both recommendation lists, and their unique district counts.

For a demonstration, use **Try it out** with `query=sea cafe photography`,
`limit=10`, and `equity_weight=0.20`. The baseline returns 10 results; the prototype
returns 9 because only nine attractions have positive relevance to this query.

<!-- PROGRESS_START -->

## Current Research Progress

**Status: RQ1 complete; recommendation-exposure experiment in progress.**

Validated research data now include:

- 16 Busan districts
- January 2022 – December 2025
- 768 district-month observations
- Foreign visitor activity
- Foreign tourist credit-card spending
- 207 official Busan attractions
- 0 missing visitor/spending values in the final master panel

Preliminary analysis shows that visitor activity and tourism spending are related but spatially distributed differently. Haeundae-gu and Busanjin-gu, in particular, capture substantially larger shares of foreign-tourist spending.

Initial lower-benefit screening identifies Yeongdo-gu, Seo-gu, Geumjeong-gu, Nam-gu, and Dong-gu as candidates for the equity-aware recommendation experiment.

See [`docs/professor_progress.md`](docs/professor_progress.md) for the current research summary and preliminary results.

**Next:** measure baseline recommendation exposure and compare it with the economic-equity-aware re-ranking model.

<!-- PROGRESS_END -->

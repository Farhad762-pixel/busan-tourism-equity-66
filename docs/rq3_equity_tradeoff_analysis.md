# RQ3 Economic-Equity Re-Ranking Experiment

## Objective

Test whether economically under-capturing Busan districts can receive greater recommendation visibility while preserving tourist relevance.

## Re-ranking rule

`Final Score = Relevance × (1 + λ × Economic Under-Capture)`

This multiplicative design prevents a zero-relevance attraction from being promoted only because its district has high economic need.

## Experimental design

- 48 benchmark queries across 12 tourist-intent categories
- 33 queries passed the primary quality rule (at least 5 positive TF-IDF matches)
- Top-K = 10
- Candidate pool = top 50 positive-relevance attractions
- Extended λ grid: 0 to 4

## Policy frontier

| Scenario | λ | Relevance retained | Under-capture exposure gain | Yeongdo + Seo-gu gain | Gini change |
|---|---:|---:|---:|---:|---:|
| Conservative | 0.80 | 99.06% | +13.74 pp | +5.44 pp | -0.0281 |
| Balanced | 1.00 | 98.62% | +15.13 pp | +5.84 pp | -0.0288 |
| Strong redistribution | 2.00 | 95.68% | +20.60 pp | +8.74 pp | +0.0016 |

The **primary research setting is λ = 0.80** because it satisfies the strict 99% relevance-retention condition while producing a substantial exposure gain.

## Query robustness

- Positive under-capture exposure gain in **12/12** tourist-intent categories.
- All **12/12** categories retained at least 95% relevance.
- Median category relevance retention: **99.62%**.
- Median category under-capture exposure gain: **+11.22 percentage points**.
- Leave-one-category-out exposure gain remained positive in **12/12** tests.
- Lowest leave-one-out relevance retention: **98.83%**.
- Lowest leave-one-out under-capture gain: **+12.07 percentage points**.

## Economic-signal robustness at λ = 0.80

| Signal | Relevance retained | Under-capture exposure gain | Yeongdo + Seo-gu gain |
|---|---:|---:|---:|
| Ratio based | 99.06% | +13.74 pp | +5.44 pp |
| Share gap | 99.61% | +7.54 pp | +3.11 pp |
| Log ratio | 99.08% | +13.38 pp | +6.87 pp |
| Rank based | 99.20% | +12.90 pp | +6.86 pp |

## Interpretation

The controlled experiment supports the feasibility of a relevance-preserving economic-equity re-ranking intervention. It does **not** establish that commercial recommendation systems caused Busan's current tourism-spending inequality or that recommendation exposure directly causes revenue changes.

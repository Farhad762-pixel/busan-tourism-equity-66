# Research Progress Update

## Working Title

**Algorithmic Visibility and Tourism Spending Inequality: An Economic-Equity-Aware Recommendation Framework for Busan**

## Main Research Question

Do tourism recommendation systems disproportionately recommend Busan areas that already capture high levels of foreign-tourist activity and spending, and can an economic-equity-aware re-ranking system broaden exposure to suitable lower-benefit areas without substantially reducing recommendation relevance or travel convenience?

## Current Data Status

The core district-month panel is complete and validated.

- Geography: 16 Busan districts
- Period: January 2022 – December 2025
- Frequency: Monthly
- District-month observations: 768
- Foreign visitor activity source: Korea Tourism Data Lab
- Foreign tourist credit-card spending source: Korea Tourism Data Lab
- Official Busan attractions: 207
- Missing visitor values: 0
- Missing spending values: 0

The raw visitor and spending downloads were validated before analysis: 128 ZIP files checked, 128 valid, 0 empty, 0 broken, and all district-year files contained January–December observations.

## Preliminary RQ1 Findings

### Visitor–Spending Association

- Pooled Pearson correlation: **0.5726**
- Pooled Spearman correlation: **0.7242**
- Visitor-share / spending-share Pearson: **0.4531**
- Visitor-share / spending-share Spearman: **0.6197**
- Average monthly Pearson: **0.4457**
- Average monthly Spearman: **0.5989**

These statistics are interpreted as descriptive associations, not causal effects.

### Highest Foreign-Visitor Shares

1. Gangseo-gu — **17.24%**
2. Haeundae-gu — **13.21%**
3. Jung-gu — **9.54%**
4. Busanjin-gu — **9.07%**
5. Dong-gu — **7.77%**

### Highest Foreign-Tourist Spending Shares

1. Haeundae-gu — **29.89%**
2. Busanjin-gu — **26.89%**
3. Jung-gu — **11.18%**
4. Gijang-gun — **8.76%**
5. Sasang-gu — **5.20%**

The difference between visitor and spending rankings indicates that tourism activity and economic benefit are not distributed identically across Busan.

## Initial Lower-Benefit Screening

The preliminary screening uses three conditions:

1. Spending share is lower than visitor share.
2. Benefit-capture ratio is below 1.
3. The district has at least the median number of official tourism attractions.

Initial candidates:

| District | Official attractions | Benefit-capture ratio |
|---|---:|---:|
| Yeongdo-gu | 13 | 0.122 |
| Seo-gu | 16 | 0.257 |
| Geumjeong-gu | 13 | 0.419 |
| Nam-gu | 15 | 0.451 |
| Dong-gu | 17 | 0.520 |

These are screening candidates, not causal claims about economic disadvantage.

Gangseo-gu requires cautious interpretation because the mobility-based visitor measure may include airport/transit-related activity.

## Recommendation-System MVP

A working FastAPI recommender MVP already exists using the 207 official Busan attractions.

Current endpoints:

- `/api/attractions`
- `/api/recommend/baseline`
- `/api/recommend/equity`
- `/api/compare`

The current equity component is a prototype. The next stage replaces/improves the simple attraction-distribution proxy with the validated visitor/spending evidence.

## Next Stage

### RQ2

Measure whether baseline recommendation exposure is concentrated in districts that already capture high levels of foreign-tourist activity and spending.

Planned measures:

- District recommendation exposure share
- Exposure HHI
- Exposure Gini
- Top-N geographic coverage
- Relationship between recommendation exposure and existing visitor/spending concentration

### RQ3

Compare the baseline recommender with the economic-equity-aware re-ranking model using:

- Recommendation relevance
- Geographic coverage
- Lower-benefit district exposure
- Exposure concentration
- Relevance loss
- Travel convenience/accessibility

## Status

- **Data collection: COMPLETE**
- **Data validation: COMPLETE**
- **RQ1 descriptive statistical analysis: COMPLETE**
- **Baseline recommender MVP: WORKING**
- **RQ2/RQ3 recommendation-exposure experiment: NEXT**

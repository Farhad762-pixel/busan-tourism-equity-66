# RQ1 Statistical Analysis

## Research Question

How geographically concentrated are foreign-tourist visits and spending across Busan?

## Data

- 16 Busan districts
- January 2022 to December 2025
- 48 months
- 768 district-month observations
- Korea Tourism Data Lab foreign visitor activity and foreign credit-card tourism spending indicators
- 207 official Busan attractions

## Visitor–Spending Association

| Measure | Result |
|---|---:|
| Pooled Pearson | 0.5726 |
| Pooled Spearman | 0.7242 |
| Share Pearson | 0.4531 |
| Share Spearman | 0.6197 |
| Average monthly Pearson | 0.4457 |
| Average monthly Spearman | 0.5989 |

These values show association, not causality.

## Top Districts by Foreign-Visitor Share

| Rank | District | Share |
|---:|---|---:|
| 1 | Gangseo-gu | 17.24% |
| 2 | Haeundae-gu | 13.21% |
| 3 | Jung-gu | 9.54% |
| 4 | Busanjin-gu | 9.07% |
| 5 | Dong-gu | 7.77% |

## Top Districts by Foreign-Tourist Spending Share

| Rank | District | Share |
|---:|---|---:|
| 1 | Haeundae-gu | 29.89% |
| 2 | Busanjin-gu | 26.89% |
| 3 | Jung-gu | 11.18% |
| 4 | Gijang-gun | 8.76% |
| 5 | Sasang-gu | 5.20% |

## Initial Lower-Benefit Candidates

| District | Attractions | Benefit-capture ratio |
|---|---:|---:|
| Yeongdo-gu | 13 | 0.122 |
| Seo-gu | 16 | 0.257 |
| Geumjeong-gu | 13 | 0.419 |
| Nam-gu | 15 | 0.451 |
| Dong-gu | 17 | 0.520 |

The screening rule requires a benefit-capture ratio below 1, spending share below visitor share, and at least the median official-attraction supply.

## Interpretation

Foreign-tourist activity and foreign-tourist spending are positively associated, but the spatial distribution of spending is clearly more concentrated in several districts than the visitor distribution alone would imply. Haeundae-gu and Busanjin-gu are especially important examples.

Gangseo-gu should be treated carefully because a mobility-based visitor measure can include airport or transit-related movement.

The next stage tests whether recommendation exposure aligns disproportionately with already high-benefit districts and whether equity-aware re-ranking can broaden exposure while preserving relevance and convenience.

# Professor Results Update

## Research Title

**From Algorithmic Visibility to Local Economic Opportunity:
An Economic-Equity-Aware Tourism Recommendation Framework for Busan**

## 1. Data Completed

The research combines:

- 16 Busan districts
- Monthly data from 2022–2025
- 768 district-month observations
- Foreign visitor activity
- Foreign tourist credit-card spending
- 207 official Busan tourism attractions

The primary policy analysis uses 2024–2025 data, with 2022–2025 retained as a robustness period.

## 2. RQ1 — Tourism Economic Distribution

Foreign visitor activity and tourism spending are positively related, but their geographic distributions are not identical.

The economic under-capture indicator is defined as:

**max(0, 1 − Spending Share / Visitor Share)**

This measures whether a district captures a smaller share of foreign-tourist spending than its share of foreign visitor activity would suggest.

The strongest and most sensitivity-robust economic-opportunity districts were **Yeongdo-gu and Seo-gu**.

## 3. RQ2 — Baseline Algorithmic Visibility

Baseline exposure showed a moderate positive association with existing tourism spending:

- Pearson: **0.4566**
- Spearman: **0.4353**

Exposure was negatively associated with economic under-capture:

- Pearson: **-0.3975**
- Spearman: **-0.2956**

This is an association and does not establish that recommendation systems caused existing tourism inequality.

## 4. RQ3 — Economic-Equity Re-ranking

The proposed re-ranking rule is:

**Final Score = Relevance × (1 + λ × Economic Under-Capture)**

### Conservative Policy — λ = 0.80

- Relevance retained: **99.06%**
- Relevance loss: **0.94%**
- Economic under-capture exposure gain: **+13.74 percentage points**
- Yeongdo + Seo-gu exposure gain: **+5.44 percentage points**
- Exposure Gini change: **-0.0281**

### Balanced Policy — λ = 1.00

- Relevance retained: **98.62%**
- Economic under-capture exposure gain: **+15.13 percentage points**

### Strong Redistribution — λ = 2.00

- Relevance retained: **95.68%**
- Economic under-capture exposure gain: **+20.60 percentage points**

The main recommended research setting is the conservative λ = 0.80 because it retains at least 99% of baseline relevance while producing a substantial improvement in economic-opportunity exposure.

## 5. Robustness

- Positive economic-opportunity exposure gain in **12/12 tourist-intent categories**
- Leave-one-category-out result positive in **12/12 tests**
- Four alternative economic definitions all produce positive gains while retaining approximately 99% relevance

## 6. Main Finding

> A relevance-preserving tourism re-ranking system can substantially increase recommendation visibility for economically under-capturing Busan districts while retaining almost all of the original recommendation relevance.

The framework should be interpreted as a controlled research prototype, not evidence that commercial recommendation platforms caused Busan's current tourism spending distribution.

## 7. Practical Policy Contribution

- **λ = 0:** Pure relevance
- **λ = 0.80:** Conservative economic-equity policy
- **λ = 1.00:** Balanced policy
- **λ = 2.00:** Strong redistribution policy

The next implementation stage is to integrate these policy options into the working FastAPI recommendation system and later add accessibility / travel-time constraints.

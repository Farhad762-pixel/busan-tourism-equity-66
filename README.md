# Busan Tourism Economic-Equity Recommender

## From Algorithmic Visibility to Local Economic Opportunity

**Research project:** An Economic-Equity-Aware Tourism Recommendation Framework for Busan

This repository studies whether digital tourism recommendation exposure aligns with existing foreign-tourist activity and spending concentration across Busan, and whether a relevance-preserving re-ranking system can broaden visibility toward economically under-capturing districts.

## Research questions

1. **RQ1:** How geographically concentrated are foreign-tourist visits and spending across Busan?
2. **RQ2:** To what extent does baseline recommendation exposure correspond to existing visitor and spending concentration?
3. **RQ3:** Can an economic-equity-aware re-ranking model broaden exposure to suitable lower-benefit areas without substantially reducing recommendation relevance?

## Data checkpoint

- 16 Busan districts
- January 2022–December 2025
- 768 district-month observations
- Foreign visitor activity
- Foreign tourist credit-card spending
- 207 official Busan attractions
- Primary policy period: 2024–2025
- Full 2022–2025 period retained for robustness

Raw authenticated Tourism Data Lab downloads are intentionally excluded from the repository. Processed research outputs and reproducible summary tables are included.

## Main findings

### RQ1 — tourism activity and spending are not distributed identically

Visitor activity and spending are positively associated, but several districts capture very different shares of tourism spending relative to visitor activity. The primary economic signal is:

`Economic Under-Capture = max(0, 1 - Spending Share / Visitor Share)`

**Yeongdo-gu and Seo-gu** were the most sensitivity-robust economic-opportunity districts.

### RQ2 — baseline algorithmic visibility is uneven

Using 48 controlled tourist-intent queries across 12 categories (33 passed the primary quality rule):

- Baseline exposure HHI: **0.0834**
- Exposure Gini: **0.3263**
- Top-3 district exposure: **35.3%**
- Exposure vs spending: Pearson **0.4566**, Spearman **0.4353**
- Exposure vs economic under-capture: Pearson **-0.3975**, Spearman **-0.2956**

These are descriptive associations, not causal estimates.

### RQ3 — economic-equity re-ranking works with minimal relevance loss

Final intervention:

`Final Score = Relevance × (1 + λ × Economic Under-Capture)`

| Policy | λ | Relevance retained | Under-capture exposure gain | Yeongdo + Seo-gu gain |
|---|---:|---:|---:|---:|
| Baseline | 0.00 | 100% | 0 pp | 0 pp |
| Conservative | **0.80** | **99.06%** | **+13.74 pp** | **+5.44 pp** |
| Balanced | 1.00 | 98.62% | +15.13 pp | +5.84 pp |
| Strong redistribution | 2.00 | 95.68% | +20.60 pp | +8.74 pp |

The **primary policy setting is λ = 0.80**, selected under a strict 99% relevance-retention rule.

## Robustness

The main result survives:

- 2024–2025 vs 2022–2025 temporal comparison
- alternative opportunity-score specifications
- **12/12** tourist-intent categories
- **12/12** leave-one-category-out tests
- bootstrap uncertainty analysis
- four economic signals: ratio, share gap, log ratio, and rank based

## Professor-ready documents

- [`docs/professor_results_summary.md`](docs/professor_results_summary.md)
- [`docs/rq1_statistical_analysis.md`](docs/rq1_statistical_analysis.md)
- [`docs/rq2_baseline_exposure_audit.md`](docs/rq2_baseline_exposure_audit.md)
- [`docs/rq3_equity_tradeoff_analysis.md`](docs/rq3_equity_tradeoff_analysis.md)
- [`docs/teos_methodology.md`](docs/teos_methodology.md)

## Current FastAPI prototype

The repository already contains a working FastAPI recommender using the 207 official attractions. The **current API equity endpoint still uses the earlier attraction-distribution prototype proxy**. The next implementation step is to replace that API proxy with the validated economic under-capture model and expose policy scenarios (λ = 0, 0.80, 1.00, 2.00).

Start the current API from the repository root:

```bash
python -m pip install fastapi uvicorn scikit-learn
python -m uvicorn src.api.main:app --reload
```

Swagger UI: <http://127.0.0.1:8000/docs>

## Important limitations

- This is a controlled research recommender, not an audit of a commercial platform.
- The study does not claim recommendation systems caused observed tourism-spending inequality.
- Increased recommendation exposure is **potential visibility**, not proven revenue impact.
- Accessibility / travel-time constraints are the next major implementation extension.

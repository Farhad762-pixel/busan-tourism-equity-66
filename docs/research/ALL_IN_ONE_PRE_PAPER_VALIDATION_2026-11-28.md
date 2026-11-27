# Integrated pre-paper validation audit — 28 November 2026

**Scope:** Original Busan tourism dataset and recommendation research. Audit by an assistant from the user's saved combined research JSON, NOT an independent provider source-data audit. This is a supervisor-review note in the draft PR; original research files and main remain unchanged. Separate local comprehensive ZIP and professor PDF were provided to the researcher; raw combined JSON was not committed.

## Completed technical checks

- **Data integrity:** Saved combined JSON contains 768 distinct district-month records (16 districts x 48 months) and 207 unique attractions. No missing or negative values in the activity/card-spending fields in this saved panel. This does NOT verify underlying telecom/card provider provenance or reuse rights.
- **Reproduced original 33-query, five-lambda experiment** using its legacy TF-IDF formula: at lambda=0.8 exposure toward positive-under-capture districts +13.737972 percentage points, with 99.060013% retained TF-IDF relevance. Largest numerical difference vs saved 2026-11-13 archived summary was approximately 1.44e-15.
- **Economic score diagnostic:** 2022–2023 vs 2024–2025 undercapture score Pearson r=0.9710, Spearman rho=0.9667; later undercapture vs official catalog attraction count Pearson r=-0.4566. These correlations do NOT validate independent economic welfare.
- **Search V2 four-policy rerun:** The reproducible local snapshot matched all saved numbers with no numeric drift. Seven synthetic search tests passed. The Search V2 snapshot used to produce these numbers is not guaranteed identical to the optional hybrid implementation currently committed in this PR; harmonize before merge.

## Mixed four-policy V2 outcomes on 36 previously seen, development searches

| Policy | Later undercapture exposure | V2 heuristic score retained | Gini |
|---|---:|---:|---:|
| Relevance-only | 54.65% | 100.00% | 0.4638 |
| Inverse attraction-count | **64.43%** | 99.97% | 0.4481 |
| Inverse baseline exposure | 60.63% | 99.91% | **0.4201** |
| Historical economic signal | 63.74% | 99.98% | 0.4652 |

- Only 17/36 queries had >=1 *source-supported* attraction; 19 had none. Five had >=5.
- Economic and attraction-count policies are **essentially tied** on later economic-score-weighted exposure; paired query-bootstrap interval crosses zero.
- The developer-defined later economic score is not an independent measure of economic benefit. No independent human relevance, observed tourist actions or actual income change is established.

## Complete integrated researcher preparation, not done by third parties

The researcher received an offline all-in-one package with repeatable scripts, aggregate data checks, figures/maps, a 7-page professor report, a source-separated blinded reviewer-only package, a new-tourist-query collection form, and a paper-section outline. **Zero** new independent human ratings or naturally collected untouched queries are yet available; these must not be generated or guessed.

**Next critical evidence:** supervisor/ethics decision and real blinded relevance judgments, genuinely uninspected natural tourist queries, and a fair fixed candidate/quality comparison. Actual transit travel-time measurements are required to claim practical route convenience. Source attribution, reuse licensing and literature novelty also remain under review.

**Verdict:** paper-ready *technical starting evidence*, NOT journal-submission-ready, NOT economic impact evidence, and NOT evidence that the economic algorithm is generally superior to geographic alternatives. Honest mixed results may still support an offline feasibility paper if the evaluation is strengthened.

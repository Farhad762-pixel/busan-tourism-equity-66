# Working full-paper outline — 13 November 2026

**Status:** Research-backed manuscript skeleton, NOT a finished article or submitted paper. Numerical findings are from archived analyses; RQ3 policy summary was independently rerun on 2026-11-13 from recovered private inputs. The literature section is preliminary. Before academic submission, reconcile this outline with the separately saved DOCX/PDF drafts and obtain professor feedback.

## Proposed title

**Economic-Equity-Aware Re-ranking for Intra-Urban Tourism Recommendations: Evidence from Busan, South Korea**

Do not present the system as a commercial Naver/Kakao/Google recommender or claim actual economic spending effects.

## Draft structured abstract (for review, not publication)

**Background:** Tourist activity and recorded foreign-card tourism spending are unevenly distributed among Busan's districts. Recommendations may allocate attention unevenly, but attention does not necessarily translate into visits or revenue.

**Objective:** Test whether an interpretable district economic-undercapture signal can shift the *simulated rank-weighted exposure* of a controlled tourism recommendation system while retaining text-based relevance.

**Methods:** Combine 2022–2025 district tourism indicators (16 districts × 48 months) with 207 official attraction records. Construct a TF-IDF/cosine baseline and evaluate 48 predefined tourist searches; 33 meet the positive-match rule. For the 2024–2025 district policy signal, define undercapture as max(0, 1 - spending_share / visitor_share). Re-rank top-50 positive-relevance candidates by cosine_similarity × (1 + λ × undercapture), then evaluate top-10 exposure, relevance, and concentration.

**Results:** The archived experiment, independently rerun using recovered saved inputs, showed that λ=0.8 shifted undercapture-district rank-weighted exposure from 56.41% to 70.14% (+13.74 percentage points), retaining 99.06% of baseline TF-IDF relevance and changing exposure Gini from 0.3263 to 0.2983. A separate exploratory six-search human pilot involved two reviewers and 61 distinct pairs; the 52 jointly judgeable pairs showed limited exact agreement and weak relevance for local-market and photography-walk searches.

**Conclusion:** District economic signals can modify simulated attraction visibility in this controlled model with a small text-similarity trade-off. These findings do not demonstrate changed real-world spending, tourism flows, user satisfaction, or unfairness of commercial platforms. Further independent human and accessibility evaluation is required.

## 1. Introduction — TO WRITE

- Busan's tourism activity and recorded foreign-card spending have unequal district distributions.
- The economic problem is not merely tourist concentration; the operational hypothesis concerns differences between shares of visitor activity and recorded spending.
- Tourism recommenders influence what potential visitors see; our offline simulation tests *possible* changes in exposure rather than platform causality.
- Define RQ1 (distribution), RQ2 (offline recommendation exposure), RQ3 (multi-objective re-ranking and relevance trade-off).
- Explain scope: Busan districts; 2022–2025 indicators; 2024–2025 policy calibration; official POI corpus.

**Need:** Verified public statistics with correct units and source receipts, motivation from city policy, and verified scholarly citations.

## 2. Related work — PARTIAL READING MATRIX ONLY

The review must compare:
- Tourism recommendation methods and context constraints.
- Item popularity bias, exposure allocation and supplier-side/multistakeholder fairness.
- Sustainable tourism, over-/undertourism and geographical dispersion.
- Existing Korean city spatial-concentration evidence, **including Busan**.
- Recent travel-AI recommendation audits and tourism economic/sustainability objectives.

Start with [verified literature matrix](../docs/literature/INITIAL_VERIFIED_READING_MATRIX_2026-11-13.md).

**Provisional gap hypothesis, not established novelty:** Direct operationalization of *intra-city visitor share versus foreign-card spending share* into an interpretable recommendation re-ranker, with rank-exposure/relevance trade-offs in Busan. A claim of "first ever" is unjustified.

## 3. Data — PARTLY VERIFIED

- **Monthly district panel:** 16 districts, Jan 2022–Dec 2025, 768 unique district-months in recovered private archive (source restrictions not fully checked).
- **Economic variables:** estimated foreign visitor activity and recorded foreign tourist credit-card consumption (in million KRW), not total tourist spending or SME income.
- **Attractions:** 207 official Busan POIs with district, name, subtitle/description, addresses, selected transport information and coordinates; public projection checked.
- **Selection:** primary district economic signal from 2024–2025; descriptive period 2022–2025.
- **Metadata limits:** missing/vague descriptions, English/Korean text mismatch, potential airport-transit artifacts.

**Need:** audit source filters, export dates, units, collection permissions, complete input transformations, plus check possible geographic confounding.

## 4. Methods — REPRODUCED RQ3; OTHER PARTS NEED AUDIT

### RQ1 — Descriptive spatial concentration

Compute district visitor/spending shares, relative capture ratio, district concentration, monthly/annual shifts, and association measures. Report uncertainty and non-causality appropriately.

### RQ2 — Offline ranking audit

TF-IDF cosine similarity over attraction metadata. Forty-eight developer-defined tourist queries across 12 categories; 33 yielded at least five positive-similarity attractions. Top-10 rankings, top-50 candidates and 1/log2(rank+1) attention weights. Report district exposure shares, Gini/HHI, top-N coverage and exposure/spending associations.

### RQ3 — Re-ranking intervention

Economic undercapture(d) = max(0, 1 - district_spending_share / district_visitor_share).

FinalScore(i) = TextSimilarity(i) × (1 + λ × EconomicUndercapture(district(i))).

Compare λ = 0, 0.5, 0.8, 1.0 and 2.0, retaining original baseline as a control. Evaluate weighted exposure, textual relevance, rankings and concentration. Define candidate district eligibility and temporal robustness clearly.

The original 48-query set is a development benchmark; not a held-out test for an improved new algorithm.

### Accessibility sensitivity

Haversine straight-line radius restrictions from approximate Busan Station, Seomyeon Station and Haeundae Station. Do not call these travel times or route convenience; exact route-based validation remains outstanding.

### Human-rating pilot

Two volunteer reviewers (as reported by researcher) independently rated 61 query-attraction pairs across six searches, rating relevance 1–5; zero means cannot judge. 52 pairs had both valid ratings, three full-query cases had no missing judgments. This is exploratory; document ethics/consent approval needs.

## 5. Results — EXISTING FINDINGS, RECONCILE TABLES

**RQ1:** Recorded foreign-tourist card-spending concentration in Haeundae-gu (29.89%) and Busanjin-gu (26.89%) over the saved 2022–2025 panel. Pooled visitor/spending association reported as Pearson 0.5726, Spearman 0.7242; not yet independently rerun from original raw source exports in public GitHub.

**RQ2:** Distribution of controlled baseline rankings; avoid presenting the simulated model as platform audit.

**RQ3:** Reproduced λ=0.8: 56.41% → 70.14% undercapture exposure, +13.74 pp, text-relevance retention 99.06%, exposure Gini 0.3263 → 0.2983, coverage 15/16. Higher λ trades more relevance for exposure and can worsen concentration by some metrics.

**Accessibility:** Earlier 15 km straight-line sensitivity produced +10.56 pp (Busan Station), +11.93 pp (Seomyeon), +10.64 pp (Haeundae) in the saved experimental tables; verify original scripts and access constraints before publication.

**Human pilot:** Reviewer agreement exact 34.6%; quadratic-weighted Cohen's κ ≈ 0.490; three fully judgeable queries yielded 3.849/5 baseline versus 3.859/5 economic policy, a tiny and statistically unestablished difference. Most obvious relevance weaknesses were "local market" and "photography walk". Do not treat this as proof of human non-inferiority.

## 6. Discussion — TO WRITE

- Interpretation: reallocating *visibility* versus redistributing tourist income.
- Compare directly to 2023–2026 tourism fairness and sustainable recommendation studies; distinguish *economic undercapture* from popularity/crowding.
- Equity trade-off and potential harms: biased proxy, accessibility constraints, district-level data masking business differences, overpromotion of unsuitable locations.
- Practical use: optional decision-support tool for destination managers, conditional on relevance and transit quality.
- Why the two-person pilot reveals content quality shortcomings despite strong TF-IDF retention.

## 7. Limitations and ethics — ESSENTIAL

- Offline, researcher-defined ranking model; no real platform, traffic, click, booking or spending changes observed.
- District spending/visitor mismatch is *not* itself proof of distributive injustice or SME income disparity.
- Data source methodology, reuse permissions and raw export checks remain partly outstanding.
- Sparse or mixed-language POI metadata affects relevance; benchmark queries are not held out.
- Small human pilot; missing values; no statistical power for equivalence; seek supervisor ethics guidance.
- Haversine is straight-line geometry, not real route duration.

## 8. Conclusion and future work — TO WRITE

State what the offline results can and cannot establish. Propose a preregistered held-out/multilingual evaluation, more human judges, verified transit routing, source-license compliance, and possibly a real-world pilot if ethical/feasible.

## Required supporting materials

- [Rerun verification and hashes](../docs/research/RQ3_REPRODUCTION_2026-11-13.md)
- [Human pilot methods and results](../docs/research/HUMAN_RELEVANCE_PILOT_2026-11-13.md)
- [Paper roadmap](../docs/research/PAPER_ROADMAP_2026-11-13.md)
- [Literature reading matrix](../docs/literature/INITIAL_VERIFIED_READING_MATRIX_2026-11-13.md)
- [Data sources and redistribution cautions](../docs/research/SOURCES_AND_REUSE.md)

**Prior to sending to the professor:** read the recovered private DOCX/PDF manuscript drafts and integrate their valid material without inventing citations or silently changing tested methods.

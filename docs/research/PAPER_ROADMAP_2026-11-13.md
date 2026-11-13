# Paper completion roadmap — 13 November 2026

Research question: Can an economic-equity-aware attraction recommender redistribute simulated exposure toward economically undercapturing Busan districts without substantially reducing relevance?

| Major work package | Current status |
|---|---|
| Problem, RQ1–RQ3, proposed economic-equity framework | Defined; supervisor review still needed |
| Official 207-attraction dataset | Verified against existing public API projection |
| 2022–2025, 16-district, 768-row tourism panel | Present in recovered private archive; original provider provenance / license and end-to-end RQ1 code still to verify |
| RQ2 + RQ3 offline rankings | **33-query, five-policy RQ3 numerical rerun successful on 2026-11-13**; first 48 queries are development data |
| Accessibility | Archived Haversine-distance sensitivity only; neither routes nor actual travel times verified |
| Human evaluation | **Exploratory two-person, six-query pilot completed**; no population-level conclusions |
| Literature gap and novelty proof | **Not yet supported by a complete verified scholarly review** |
| Manuscript | Archived Methods and Results drafts exist privately; complete Introduction, Literature, Discussion, Conclusion, references and professor revisions still needed |

## Next actions, in order

1. Expand the [preliminary verified literature matrix](../literature/INITIAL_VERIFIED_READING_MATRIX_2026-11-13.md) with full-text notes and citations. Study peer-reviewed tourism recommendation, popularity/exposure bias, supplier fairness, and location-aware multi-objective recommender studies. Write a bounded research gap with real DOI/citations.
2. Reserve NEW evaluation queries and independent relevance judgments *before* changing algorithm rules. The six pilot queries and 48 old searches are no longer held out.
3. Create an **intent-aware experimental v2** to address local market and photography walk mismatches; retain v1 as the frozen control. Do not claim v2 is better until evaluated.
4. Validate original Korea Tourism Data Lab export definitions, period alignment, units, panel processing, source permissions. Rerun RQ1 and full accessibility from original inputs where possible; actual transit time remains an outstanding upgrade.
5. Finish Introduction–Discussion–Conclusion with limitations and bibliography, integrate reproducible figures/tables, send a first full manuscript to professor, revise to their feedback.

## Readiness estimate

The study has enough methods and initial results to **start drafting a full paper now**. It is **not** ready for journal submission because the novelty literature matrix, independent test, stronger human validation, rights/provenance checks and manuscript revision are outstanding. A planning estimate for a professor-reviewable first draft is roughly 3–6 focused weeks, assuming inputs remain accessible; publication-grade revisions may take several additional months.

Remember: 13.74 percentage points is a simulated ranking exposure gain, NOT a revenue gain. The 99.06% metric is TF-IDF similarity retention, NOT 99.06% human satisfaction. The current FastAPI endpoint is still an older attraction-count proxy, not this economic policy.

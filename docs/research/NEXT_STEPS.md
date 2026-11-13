> See the [current audit](AUDIT_2026-11-13.md): the archive and newest Mac code are unavailable in this environment.

# Research roadmap / remaining validation

## Previously reported as completed in the archive (not rerun here)

- 16-district, 48-month tourism visitor and foreign-card-spending data validation.
- 207-attraction official point-of-interest dataset.
- RQ1 district concentration and undercapture analysis.
- RQ2 baseline text-recommender audit.
- RQ3 multi-policy offline re-ranking experiment (33 eligible queries).
- Preliminary Haversine-distance-constrained sensitivity experiment.
- Working drafts of professor summary and manuscript sections available in the local ZIP.

## Outstanding scientific work (priority order)

1. **Human relevance pilot completed; stronger study pending.** Two reviewers independently rated 61 item pairs across six queries. Next: a larger blinded study on NEW queries and ethics review.
2. **Measured accessibility.** Obtain permitted travel-time data or validated route-based alternatives, multiple origin points, and accessibility constraints; don't call Haversine distance travel time.
3. **Benchmark robustness.** Test unseen/multilingual queries, include low-match-query failure cases, and prevent choosing parameters using the same evaluation queries.
4. **Literature review.** Verify related-work novelty with appropriate scholarly citations and citations for all third-party data.
5. **Final manuscript and professor review.** Update the methods/results sections after additional tests, document limitations, citations and precise experiment versions.

## GitHub organization next

An RQ3 rerun from the recovered private archive was verified on 2026-11-13. Its code and frozen development queries are on a new review branch; the district-score inputs remain private. Bulk-sync the remaining approved materials using a careful Mac/Codex merge, but **first confirm rights** for public sharing of Korea Tourism Data Lab and other source data. Do not overwrite your newer Mac-side recommender API with the older checkpoint's API file.

See the [current research readiness and manuscript priorities](PAPER_ROADMAP_2026-11-13.md).

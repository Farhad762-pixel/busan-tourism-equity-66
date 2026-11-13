# Research next actions — planned after 13 November 2026, 16:58 KST

**Planning status:** These are NOT completed experiments or observed findings. They form the beginning of the next chronological research phase while the professor is busy.

## Planned Step 12 — Freeze an independent validation protocol

- Decide the target visitor intents and new English/Korean query categories before the next model improvement.
- Keep new evaluation queries and relevance keys separate from development; choose reviewer recruitment and 'cannot judge' handling before running comparisons.
- Get professor/ethics advice before using independent human participants in publishable research.
- Preserve the exact v1 algorithm, corpus and results as baselines, using their immutable Git commit and data hashes.
- Deliverable: a NEW dated v01 preregistration-style protocol. **Status: planned, not tested.**

## Planned Step 13 — Intent-aware recommender version 2

- Investigate the pilot's 'local market' and 'photography walk' failures; verify POI venue types and bilingual metadata.
- Build a NEW standalone model module rather than editing the frozen original FastAPI or the archived economic rerun script.
- Evaluate in two phases: visible development diagnostics, THEN independent held-out tests. Avoid leaking results from a reserved test set into model design.
- Report suitability, coverage, exposure distribution and failure rates; no unsupported claim of improvement.

## Planned Step 14 — Strengthen data and accessibility validity

- Audit original Data Lab export receipts and provider coverage revisions; reproduce the 16×48 district panel under verified units.
- Check RQ1 transformations and bootstrap assumptions. Separate archived reports from newly rerun results.
- Use actual permitted network-based travel times if possible; otherwise label Haversine as straight-line distance only.

## Planned Step 15 — Expand scientific literature and manuscript

- Complete full-text review of closest prior works, especially economic outcomes in spatially fair tourist/POI ranking.
- Draft a NEW v0.3 manuscript, never overwrite v0.2; explicitly log which claims and tests changed.
- Ask professor for a single review later with this notebook, the new version and a short changes-since-v0.2 comparison.

## Hold points

Do not claim better human relevance until a new blinded evaluation supports it; do not claim spending impact without observed transactions or appropriate causal study; do not release private/restricted raw files until permissions are verified.

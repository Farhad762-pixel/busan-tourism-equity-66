# Step 04 — Working attraction recommender prototype

**GitHub evidence timestamp:** 2026-11-08 21:57:53 KST
**Original commit:** [a6d08a3b56](https://github.com/Farhad762-pixel/busan-tourism-equity-66/commit/a6d08a3b56a30b9a7059ccd4f955dd48bde129c6) · full commit SHA: a6d08a3b56a30b9a7059ccd4f955dd48bde129c6
**Status:** Completed prototype; not the final economic model

## Why this step mattered
Demonstrate baseline attraction search, an early district-representation proxy and comparison endpoints.

## What was done
- Implemented FastAPI health, attractions, baseline, proxy-equity, and comparison endpoints.
- Created reproducibility checks and a demo using the official attractions.

## Where the actual evidence is
- [main.py](../../src/api/main.py)
- [run_mvp_experiment.py](../../scripts/run_mvp_experiment.py)
- [test_repository.py](../../tests/test_repository.py)
- [mvp_demo.json](../../results/reports/mvp_demo.json)

## What this does NOT establish
The public API's equity_score is an attraction-count proxy, NOT the 2024–2025 economic-undercapture multiplier used by RQ3. The user's newer local Mac code may differ.

**Historical-date caution:** 2026-11-08 21:57:53 KST is the publication time of the linked GitHub milestone. Research preparation, experiments, or data collection may have occurred earlier, and private original files may carry different timestamps.

**Snapshot baseline:** [13 November 2026 frozen GitHub state](https://github.com/Farhad762-pixel/busan-tourism-equity-66/tree/d76aa6442d582e490a5342279d8585c8bdf32664); the research journal itself was created later on 13 November at approximately 16:58 KST.

# Reproduction guide

Python 3.12 was used for this audit. Run commands from the repository root.
The pinned direct dependencies are in `requirements*.txt`; transitive packages
are not yet locked, so a future exact-environment archive remains desirable.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-research.txt
python -m unittest discover -s tests -v
python scripts/verify_repository.py --output work/audit.json
python scripts/run_mvp_experiment.py --output work/mvp_demo.json
python scripts/build_figures.py
python -m uvicorn src.api.main:app --reload
```

Swagger: <http://127.0.0.1:8000/docs>. Try `sea cafe photography`, limit `10`,
equity weight `0.20`. The prototype returns 9 items because only 9 have positive
similarity. Baseline returns 10, including a zero-score item. This deliberate
behavior is tested; do not interpret that item as a relevant match.

For API-only work, install `requirements-dev.txt`; for running only the server,
install `requirements.txt`. Tests use Python's built-in unittest and TestClient.
With the current Starlette/httpx pair a deprecation warning may appear; tests
pass, but future dependency upgrades should recheck compatibility.

Scripts resolve inputs from their own repository location. Custom output paths
are relative to your current shell directory. Audit output under `work/` is
ignored; do not publish private inventories or data without review.

## Rebuild the attraction projection without overwriting data

```bash
python src/clean_attractions.py --output work/attractions_rebuilt.csv
```

Use a fresh output filename: the cleaner refuses to overwrite existing files.
Do not run it against original raw inputs as an output destination. The
validator compares the existing CSV to the raw JSON projection without writing.
The 207-record count describes this snapshot, not the live API's current count.

## Private research inputs still needed

The original archive scripts and their inputs are not present. No command in
this repository can currently rerun the reported 33-query economic study.
Do not substitute the attraction-count API formula for the economic formula.

Recover the original files privately, then document their actual schemas:

1. The 768 district-month observations and combined JSON export. Verify exactly
   16 district identifiers × 48 unique months (202201–202512), unique district/month
   keys, numeric nonnegative visitor/spending values, units, source selections,
   missing-value rules and CSV/JSON equality after an explicit schema mapping.
2. Original source receipts and 128 district-year downloads, if available.
   Use only provider-approved downloads. Keep keys outside source code; do not
   automate authenticated scraping or reuse another user's credentials.
3. Original 48 query/category pairs, 33-query eligibility list, candidate lists,
   preprocessing, rank weights and per-query results. Preserve low-match cases.
4. Original scripts for RQ1, `reproduce_rq3.py`, and
   `run_accessibility_experiment.py`; record command lines and versions.
5. For distance tests, origin coordinates, Earth-radius convention, caps,
   order of filtering/truncation, and within-origin query eligibility.

If redistribution is restricted, run the recovered scripts locally against
ignored `data/private/` inputs and publish only permitted aggregate results,
schema/loading instructions and their checksums. Do not invent input mappings
or scrape missing observations to make reported values match.

## Recovered RQ3 experiment (13 November 2026)

The archived 33-query economic model was independently rerun using recovered
private data. Its public script and original authored development-query labels
are available in the repository. Reproduce locally after placing the private
2024-2025 district signal file at data/private/teos_primary_2024_2025.csv:

    python experiments/equity/reproduce_rq3.py

The script checks all five archived policy rows and writes a CSV and input
hashes to ignored work/rq3_reproduced/. Private signals need district,
economic_undercapture, recommendation_candidate for all 16 districts.
Do not upload private inputs or reuse these development queries as an
independent post-improvement benchmark.

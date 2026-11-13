# Synchronization and reproducibility status

## Cloud audit: 2026-11-13

Latest GitHub main inspected: `fd117b8`. The cloud checkout initially lagged at
`2782375`; API and requirements were identical. Work began on a separate review
branch from current main after a local Git bundle and working-tree backup.
Mac project and Downloads are not accessible. No archive was found here.

| Evidence | Current status |
|---|---|
| Existing 207-attraction data | Validated against full raw JSON; data untouched |
| Five API endpoints and Swagger | Covered by automated checks and browser smoke test |
| Existing summary table arithmetic | Checked; saved Gini/HHI and gains agree |
| Full RQ1 / RQ2 / RQ3 reproduction | Blocked: panel, combined JSON, benchmark and scripts absent |
| Accessibility calculation/eligibility | Blocked: original code, origin coordinates and detailed tables absent |
| Mac-only application comparison | Blocked: files unavailable; no older code substituted |
| Source-data release review | New source files excluded; historical permissions remain a follow-up |

See [audit](AUDIT_2026-11-13.md), [reproduction guide](REPRODUCE.md),
[data dictionary](../data_sources/DATA_DICTIONARY.md) and
[manuscript index](../../manuscript/README.md).

## Historical archive report (not independently verified in this checkout)

The following previous checkpoint description is retained for reference. In
particular, its statements about a ZIP and an offline rerun are historical
reports, not results of the current audit. Do not infer that the ZIP or those
scripts are now included in GitHub.

### Earlier synchronization report

This public repository was inspected on 2026-11-12 before the organization update. Existing code, already uploaded raw attraction files, README, and older experiment summaries were **left unchanged**. This update adds a clearly labeled research index and *small, derived* result summaries.

## Research materials available in the local prepared ZIP

`Busan_Research_GitHub_Ready_2026-11-12.zip` contains **87 files**, including:

- `data/json/busan_research_database.json` — full combined JSON research export (kept out of this public update until reuse terms are checked).
- `data/processed/` — tourism panels and official attractions.
- `results/tables/`, `results/figures/` — RQ1, RQ2 and RQ3 archived outputs.
- `experiments/equity/reproduce_rq3.py` — independent reproducibility script.
- `experiments/accessibility/run_accessibility_experiment.py` and resulting CSV/PNG assets.
- `docs/manuscript_and_professor_reports/` — professor-facing PDF and editable paper draft.
- `scripts/verify_repository.py`, `docs/FILE_MANIFEST.csv` — integrity and inventory tools.

**Not included even in the local ZIP:** the original 128 Data Lab source ZIPs and the newest Mac-only API changes.

## Sync checklist

- [x] Inspect existing GitHub repository before modifying files.
- [x] Preserve current `src/api/main.py` and previously published paths.
- [x] Add research index, methods, provenance, status and derived summary tables on a review branch.
- [ ] Verify public redistribution rights for the complete tourism datasets.
- [ ] Compare local Mac code with online `src/api/main.py`; preserve whichever is newest and correct.
- [ ] Upload remaining safe scripts, figures, reports and detailed results (use Codex with the local ZIP for the bulk sync).
- [ ] Upload full JSON/processed datasets **only if** sharing rights permit; otherwise retain privately.
- [ ] Run the offline RQ3 and distance experiment reproduction checks from the merged local repo.
- [ ] Merge the GitHub pull request after review.

## Safe local merge of the ZIP (does not overwrite existing files)

Unzip into a separate folder. Inside your Mac's existing repo:

```bash
cd ~/busan-tourism-equity-66
rsync -av --ignore-existing ~/Downloads/Busan_Research_GitHub_Ready_2026-11-12/ ./
git status
```

**Do not** use `git add .` blindly. Review the complete diff and check credentials and redistribution permissions first. `rsync --ignore-existing` will preserve the existing README and API, but it may also leave older versions of overlapping results files; compare them carefully.

## What reproducibility currently means

- An independent offline RQ3 rerun of the prepared JSON/CSV data reproduced the saved main policy summary to numerical precision.
- Accessibility findings were checked against the supplied experiment tables.
- Full code/data repeatability on the *live GitHub* repository is **not yet established** because the full local files have not been published.

# Versioning and preservation rules — effective 13 November 2026, 16:58 KST

## Researcher's instruction

**Nothing from the existing research should be deleted or overwritten.** Every changed manuscript, algorithm, result table, and progress report becomes a **new dated version**, with an explicit link back to its predecessor. The current notebook and historical state stay unchanged.

## File naming convention

Format: YYYY-MM-DD_HHMM_KST__STEP_XX__short_description__v01.ext. Example:

    2026-11-14_0930_KST__STEP_12__intent_classifier_design__v01.md
    2026-11-16_1400_KST__STEP_13__evaluation_results__v01.csv
    2026-11-19_1100_KST__STEP_14__manuscript_v03.md

Use the **actual** Korea Standard Time (KST, UTC+09) at which each artifact is created or finalized. If created at a different time than the experiment, record the two times separately in the file. Never fabricate original measurement dates.

## Every new step must contain

1. Step number and precise file-creation timestamp/time zone.
2. Goal and why the experiment or writing step is necessary.
3. Inputs, original source files and their versions.
4. Code/methods and reproducible command or manual protocol.
5. Actual results (or clearly state PLANNED / NOT RUN).
6. Limitations, scientific interpretation and unresolved questions.
7. Exact previous-step and next-step links, including Git commit SHA.
8. Whether data are public, private, license-restricted or human-subject-related.

## Rules for updates

- **Append only:** never edit, delete, rename, replace or overwrite any of the 89 tracked files that existed at the frozen revision. That includes the full v0.2 manuscript, archived tables, original README and code.
- To improve an existing method, put the v2 model and its tests in NEW versioned filenames; compare against the original frozen v1 without modifying it.
- For a revised paper, create a NEW manuscript file with a new timestamp and version. Keep the previous full paper at its existing path.
- Create a NEW dated professor index whenever a milestone is added. Older dated notebook folders are never altered; the latest indexed timestamp indicates the newest notebook version.
- Do not publish individual human reviewer ratings, private cards/visitation panels, secret credentials, or unapproved provider data in this public repository.
- The archived 48 development queries and six pilot queries are **not a new held-out benchmark**. Avoid tuning a new model and claiming independent success on these same searches.
- Distinguish economic RQ3 code from the existing FastAPI attraction-count proxy and state precisely which one generated a result.

## Verification

- Frozen commit: d76aa6442d582e490a5342279d8585c8bdf32664
- Baseline file manifest: [BASELINE_TRACKED_FILES_2026-11-13_1658_KST.csv](BASELINE_TRACKED_FILES_2026-11-13_1658_KST.csv).
- A new GitHub Actions guard checks that baseline Git blobs remain identical. For later changes, the guard also checks that each proposed Git change **adds** a file rather than altering or deleting a tracked file.
- Git version history and the notebook are safeguards, **not absolute protection** against repository deletion, force-push by administrators or external source loss. Maintain independent private/local backups.

## Local backup (recommended)

From the researcher's Mac, clone the repository and create an offline bundle:

    git clone https://github.com/Farhad762-pixel/busan-tourism-equity-66.git
    cd busan-tourism-equity-66
    git bundle create BusanResearchHistory_2026-11-13_1658_KST.bundle --all

Store a backup of the **private** district panel, participant records and source receipts securely in a separate location, following consent and data-license rules. Do not place private data in a public Git bundle.

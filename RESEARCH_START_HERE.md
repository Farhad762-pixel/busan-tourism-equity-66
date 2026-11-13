> **Current audit:** [2026-11-13 inventory and evidence limits](docs/research/AUDIT_2026-11-13.md). The referenced Mac archive is not accessible in this cloud checkout. Summary arithmetic checks are not full experiment reproduction.

# Busan Tourism Equity — Research Library

This is the entry point for **research data, methods, reproducibility and professor-facing findings**. The repository's original application and previously committed files remain in their existing locations.

**Project:** Algorithmic Visibility and Tourism Spending Inequality in Busan

**Research question:** Can a relevance-based attraction recommender increase visibility for districts receiving a relatively small share of recorded foreign tourism spending, without substantially reducing relevance or practicality?

## Start here

| Resource | Location |
| --- | --- |
| Current research status | [Research roadmap](docs/research/NEXT_STEPS.md) |
| Research methods and definitions | [Methods](docs/research/METHODS_AND_METRICS.md) |
| Previously reported numerical findings | [Results](docs/research/VERIFIED_RESULTS.md) |
| Data sources and reuse checks | [Sources & reuse](docs/research/SOURCES_AND_REUSE.md) |
| What is synced, and what is not | [Reproducibility and sync status](docs/research/REPRODUCIBILITY_STATUS.md) |
| RQ3 results summary | [Equity policy results](experiments/equity/results/rq3_policy_summary.csv) |
| Distance test summary | [Accessibility results](experiments/accessibility/results/accessibility_15km_summary.csv) |
| Human relevance pilot | [Two-reviewer pilot, results and limits](docs/research/HUMAN_RELEVANCE_PILOT_2026-11-13.md) |
| Verified RQ3 rerun | [Reproduction evidence and private-input procedure](docs/research/RQ3_REPRODUCTION_2026-11-13.md) |
| Paper completion roadmap | [Status and next priorities](docs/research/PAPER_ROADMAP_2026-11-13.md) |

## Current data and results

- 16 districts × 48 months (2022–2025) = **768** district-month visitor/spending observations in the **local research archive**.
- **207** official Busan tourist attractions with coordinates.
- Offline recommender evaluated with 48 predefined tourist searches; **33** queries across 12 categories met the main positive-match threshold.
- At equity strength `lambda=0.8`, exposure to districts with measured economic undercapture rose **56.41% → 70.14%**, with **99.06%** of baseline TF-IDF text relevance retained.
- Preliminary distance tests use **straight-line kilometers only**, not routes or transit time.

**Interpretation:** These are simulated ranking results. They do **not** demonstrate changes in tourist travel, real spending, satisfaction, or commercial platform behavior.

## Publication caution

This is a **public GitHub repository**. The complete JSON database, original Korea Tourism Data Lab ZIP files, and any potentially restricted source downloads are **not part of this organization-only update**; confirm reuse and redistribution terms before publishing them. No keys, tokens, cookies or personal access credentials should be committed.

## Source-code caution

The previously committed `src/api/main.py` may not match newer uncommitted changes on the researcher's Mac. **Do not overwrite the Mac's latest API with an archived checkpoint.**

**Status:** Existing summary documents are on main. The reproducibility audit is on a separate review branch; full archive synchronization remains a follow-up task.

## Manuscript writing update (13 November 2026)

[Introduction and Related Work working draft](manuscript/INTRODUCTION_AND_RELATED_WORK_2026-11-13.md) · [Verified literature screening notes](docs/literature/TARGETED_SEARCH_LOG_2026-11-13.md).

The draft explains the narrow economic-proxy contribution and the visitor-estimation limits. It is not a final journal submission.

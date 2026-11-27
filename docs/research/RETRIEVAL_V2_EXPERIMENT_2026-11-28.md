# Source-evidence-aware attraction retrieval — experimental candidate

**Status:** Standalone, opt-in search experiment. **NOT** a validated replacement for the original economic-equity experiment.

## Problem

The original Busan catalog contains 207 official attractions but many English descriptions are short, translated, boilerplate, or have Korean-only labels. The original word-only TF-IDF index also mixes walking/transport directions into attraction content. This can lead to zero overlap for natural tourist searches or spurious matches from directions that mention unrelated places.

## Intervention

Add an optional \`/api/recommend/hybrid\` endpoint using word and character TF-IDF on the attraction's place/title/subtitle. A small inspectable concept dictionary handles some common alternate terms. When a search explicitly specifies features such as beach, temple, garden, museum, market, oceanfront, swimming or illuminated bridge, an evidence check looks for those features in the source text.

Results are separated into:

- \`supported\`: all explicitly checked features are present in the short official record under the declared heuristic rules.
- \`related_unverified\`: a possibly useful alternative, with exact missing source evidence displayed.

**Source-supported does not equal independently confirmed suitability.** Missing descriptions do not prove an activity is impossible.

## Reproduce and inspect

\`\`\`bash
pip install -r requirements.txt
python -m unittest tests.test_hybrid_search -v
python experiments/retrieval/audit_retrieval_v2.py
uvicorn src.api.app_v2:app --reload
\`\`\`

Open \`http://127.0.0.1:8000/docs\` and test \`/api/recommend/hybrid\`.

This app entry point composes with \`src.api.main\` and does **not** modify the original five routes or the original archived TF-IDF methods.

## Interpretation and no-leakage rules

The historical 48 queries are development data. The 36 natural-language searches used in the November 27 exploratory comparison have ALSO been inspected and cannot honestly be called fresh held-out data again. Do not tune and test on the same queries and report independent results.

The old 2024–2025 undercapture boost and its archived +13.74 percentage-point exposure result belong to the **old retrieval experiment only**. The new retrieval method is not yet plugged into the economic-under-capture model and does not prove economic benefit.

The current public \`/api/recommend/equity\` endpoint remains an **attraction-count proxy**, not the full private-data economic score. Do not confuse either API with the historical RQ3 economic experiment.

## What is required next

1. Independently review search relevance with blind raters. Explicitly count queries with no usable answer; do not reward forcing an incorrect suggestion.
2. Freeze genuinely untouched tourist queries after changes are complete.
3. Measure intent satisfaction, precision/nDCG, coverage, and human uncertainty.
4. If adopted, rerun both relevance-only and economic ranking algorithms with the SAME new candidate sets; do not mix old and new results.
5. Keep original raw tourism files and source-derived sensitive outputs private pending source-permission review.

**Decision standard:** adopt this retrieval method only if it demonstrably improves independently judged recommendation usefulness, not merely the number of returned items.

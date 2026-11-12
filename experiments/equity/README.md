# Equity-aware ranking (RQ3)

**Status:** The standalone reproducibility script and full outputs are present in the prepared **local** project ZIP, not yet all copied into this public repository.

The experiment uses:
- 207 Busan attraction records.
- 16-district foreign visitor and spending data, using **2024–2025** totals for the equity signal.
- 48 predefined tourist searches, 33 with at least five positive textual matches.
- TF-IDF cosine similarity baseline and `final_score = relevance * (1 + lambda * undercapture)` re-ranking from top 50 candidates.
- Up to 10 recommendations, rank-weighted exposure (`1/log2(rank+1)`).

**Results:** [Policy summary](results/rq3_policy_summary.csv), [Methods](../../docs/research/METHODS_AND_METRICS.md), [Interpretation](../../docs/research/VERIFIED_RESULTS.md).

**Next:** Merge `experiments/equity/reproduce_rq3.py` from the local archive, run it against the local dataset, and verify summary figures before public release. Never commit API keys. Confirm dataset sharing rights.

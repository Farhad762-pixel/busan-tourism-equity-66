# Verified RQ3 reproduction — 13 November 2026

The saved economic-equity offline experiment was **rerun from the recovered archive inputs**, not only checked for summary-table arithmetic. The new public reproduction script and the 48 researcher-written development searches accompany this record.

**Inputs (local archive):** 207 official attractions; 16 district economic-signal rows for 2024–2025; 48 saved tourist search queries (33 eligible). The district economic-signal CSV is kept **private** until third-party source redistribution terms are clarified.

**Reproduction:** five policies (lambda 0, 0.5, 0.8, 1.0, 2.0), 33 eligible queries, 288 recommendations per setting, and all seven policy summary measures matched original reports within 1e-7. Original legacy reproduction script and the new private-input script both passed against the archive.

| Lambda | Exposure to undercapturing districts | Relevance retained | Gain in exposure (percentage points) | Gini |
|---:|---:|---:|---:|---:|
| 0.0 | 56.4063% | 100.0000% | 0 | 0.326343 |
| 0.5 | 65.9523% | 99.6498% | +9.5459 | 0.307021 |
| **0.8** | **70.1443%** | **99.0600%** | **+13.7380** | **0.298256** |
| 1.0 | 71.5346% | 98.6233% | +15.1283 | 0.297528 |
| 2.0 | 77.0073% | 95.6840% | +20.6010 | 0.327899 |

## Saved archive input hashes (SHA-256)

- Attraction CSV: 79f8cc89aaac21c3fb86729c3e388c5f7b1cbc148c08f437684a734db0b969f3
- Private 2024–2025 economic signal table: 7317e2003112a22b25a66db726c0e36686a6337142dadadc3884b7bf5731aeef
- Original 48-query full quality table: fb1f5b9cb931ae87088a26cd01fe35d867dafb69841bb0614aa26b537351c27d

The smaller public development benchmark is a projection of the original 48-query file and therefore has a different checksum.

## How to rerun locally

1. Install the repository's research requirements.
2. Place an approved local copy of the economic-score table in data/private/teos_primary_2024_2025.csv (ignored by Git).
3. Run the program: python experiments/equity/reproduce_rq3.py
4. Examine work/rq3_reproduced/rq3_policy_summary.csv and input_hashes.json. Both stay out of public Git.

The private file must contain the 16 district names with economic_undercapture and recommendation_candidate columns. It is **not** part of public GitHub.

## Limits

The rerun validates a historical offline simulation using **previously seen development queries**. It is not a new held-out test; it does not prove real tourist spending impact or human satisfaction. We still need independently verified original download provenance, publication rights, new unseen evaluation, larger blinded human relevance evaluation, and route-based convenience data or carefully limited distance claims.

Local environment for this verification: Python 3.13, scikit-learn 1.8.0, NumPy 2.3.5.

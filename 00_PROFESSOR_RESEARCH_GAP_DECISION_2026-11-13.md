# OPEN FIRST — Which Busan tourism research gap should we pursue?

**13 November 2026 | Supervisor decision note | Same research project, not a new paper**

## In one minute

The existing Busan paper has real data and a working recommender, but merely showing that the *economic equity boost raises exposure to the districts it boosts* is not enough to establish original value. Prior research already studies tourism recommendation fairness, geographic bias, card-transaction recommendation, and spending per visit. A meaningful paper needs to identify **when the policy is useful, when it cannot work, and why**.

**Recommended next research gap: the Economic Opportunity–Recommendation Feasibility Gap.**

> **Key question:** When a Busan district appears to have relatively low recorded card spending compared with estimated visitor activity, does the attraction catalogue contain **relevant, geographically eligible places** that the recommender can actually recommend—and does an economic policy capture more of that *achievable* exposure than standard diversification rules?

This avoids claiming actual business revenue changes, new economic indicators, or a world-first fairness method.

## Why this is worth studying

**The data already exist:** 16 districts, 48 months of visitor/spending indicators (2022–2025), 207 official attractions with district/coordinates, 48 development search queries, the existing 33-query ranking experiment and radius-based sensitivity checks.

**Verified exploratory diagnosis:** **15 of 48 (31.25%)** development queries had fewer than five positively matched attractions under the original text-retrieval rule. Even a sophisticated district equity score cannot repair the lack of relevant eligible suggestions without changing the retrieval/catalogue stage.

**Economic caution:** KTO already publishes tourism consumption intensity, including spending relative to visitation. Our foreign-visitor/card-spending mismatch is a **relative measurement proxy**, *not* verified community deprivation or unique-tourist spending.

## Gap choices

| Potential gap | Likely academic contribution | Data feasibility | Recommendation |
|---|---|---|---|
| **1. Economic opportunity vs reachable relevant recommendations** | Diagnose when a fairness objective is operationally **feasible** and its achievable upper bound | **Very high** | **Best combined contribution** |
| **2. False opportunity from spending/visitation data artifacts** | Challenge the validity of the economic need proxy | Medium; requires independent provider/business/transport context for definitive claims | Highest policy impact, later extension |
| **3. Economic signal vs ordinary geographic diversity** | Stronger matched-relevance policy comparison | **Very high** | Essential experiment inside #1 |
| **4. Monthly/seasonal dynamic opportunity scores** | Test changing regional policy priorities | High, but top-five scores were usually stable in existing panel | Lower priority |
| **5. Actual local SME revenue effects** | Connect recommendation exposure to real spending | **Not possible** using current aggregate data alone | Future field study |

## What is already known (do not claim it is new)

- [KTO tourism demand intensity](https://www.data.go.kr/data/15151868/openapi.do) — expenditure relative to visit volume exists as an official indicator.
- [Hong, Chung & Koo (2023)](https://doi.org/10.2298/CSIS220620002H) — credit-card-informed Korean tourism recommendations.
- [Merinov & Ricci (2026)](https://doi.org/10.1016/j.asoc.2026.114582) — balancing tourist utility with low-popularity POI exposure in urban simulations.
- [CAPRI-FAIR (2024)](https://arxiv.org/abs/2406.03109) — provider fairness, utility and distance tradeoffs.
- [Mai et al. (2025)](https://doi.org/10.1016/j.tourman.2025.105254) — Busan/Seoul/Jeju tourist spatial choice depends on POI availability and distance.
- [Müllner et al. (2025)](https://doi.org/10.3389/fdata.2025.1632766) — simplified fairness metrics can miss community stakeholders.
- [Bellogín et al. (2026)](https://doi.org/10.1145/3816430) — real-world POI recommendation evaluation and problem-definition pitfalls.
- [OECD (2026)](https://www.oecd.org/en/publications/oecd-tourism-trends-and-policies-2026_3fd3cd75-en/full-report/enhancing-the-social-benefits-of-tourism_43631a73.html) — local economic value and SME benefit are not equivalent to tourist volumes or screen exposure.

## What the suggested study would do

1. **Audit the economic proxy** across years, source definitions and normalization choices; avoid using “unfair deprivation” as an observed fact.
2. **Measure query-by-query eligibility:** which lower-capture districts have at least one independently relevant candidate in the fixed attraction corpus?
3. **Define an achievable exposure limit** under a predeclared relevance and accessibility constraint; identify cases where the target is **not reachable**.
4. Compare economic-targeted re-ranking, relevance-only ranking and geographic-diversity competitors at **matched independent relevance**, reporting failures as well as gains.
5. Use frozen, untouched searches and genuine consented reviewer judgments. Existing 33 searches and 10 later explored prompts are **development evidence**, not independently held out.

**No second-round human ratings have been collected**, and the geographic radius experiment is straight-line distance, not real transit duration.

## Full professor report (24 focused studies)

**[Read the full deep literature/gap review, with findings and linked sources](docs/literature/PROFESSOR_DEEP_GAP_REVIEW_24_STUDIES_2026-11-13.md)**

The full report explains each study's contribution, what remains uncertain, the five research gaps, exact methods and required data, a detailed experiment plan, and questions for supervisor approval. Its 24 sources are a **targeted evidence matrix**, not a complete systematic literature review. The report **does not claim anything is proven to have never been studied**.

## Preserve the completed work

- [Full manuscript v0.4](manuscript/BUSAN_FULL_MANUSCRIPT_DRAFT_v0_4_2026-11-13.md) — no need to start over.
- [Existing economic specificity experiment](docs/research/ECONOMIC_SIGNAL_SPECIFICITY_DIAGNOSTIC_2026-11-13.md) — the prior 33-query comparator; not relevance-matched.
- [Economic score sensitivity](docs/research/ECONOMIC_INDICATOR_SENSITIVITY_2026-11-13.md).
- [Existing human pilot](docs/research/HUMAN_RELEVANCE_PILOT_2026-11-13.md).

**Supervisor decision requested:** Is *reachability and feasibility of economic-targeted recommendation* a worthwhile incremental contribution? If yes, we will freeze the research design and complete **one** rigorous comparison, rather than continually rewriting paper titles.

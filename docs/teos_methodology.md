> **Evidence update (2026-11-13):** This document preserves previously reported research. The cloud audit checked available attraction data, API behavior and summary arithmetic; it did not rerun the economic or accessibility studies because their inputs/scripts are missing. See [audit](research/AUDIT_2026-11-13.md).

# Economic Under-Capture and Opportunity Methodology

## Primary policy period

The primary economic signal uses **2024–2025** foreign visitor activity and foreign-tourist credit-card spending across all 16 Busan districts. The full **2022–2025** period is used as a temporal robustness check.

## Economic under-capture

For district *d*:

`Benefit Capture Ratio = Spending Share / Visitor Share`

`Economic Under-Capture = max(0, 1 - Benefit Capture Ratio)`

A larger value means the district captures a smaller share of foreign-tourist spending than its share of foreign visitor activity would suggest. It is a descriptive opportunity signal, not a causal measure of disadvantage.

## Tourism-supply screening

Official Busan attraction counts are used as a screening / readiness indicator. The final policy intervention does **not** treat attraction quantity as economic need. Instead, economic need and attraction relevance are kept conceptually separate.

## Re-ranking intervention

`Final Score = Relevance × (1 + λ × Economic Under-Capture)`

The multiplicative form means a zero-relevance attraction cannot become relevant solely because its district has high economic under-capture.

## Policy scenarios

- `λ = 0`: baseline relevance only
- `λ = 0.80`: conservative policy; at least 99% relevance retention
- `λ = 1.00`: balanced policy
- `λ = 2.00`: strong redistribution scenario

## Robustness

The study checks temporal stability, multiple opportunity-score specifications, 12 tourist-intent categories, leave-one-category-out tests, bootstrap uncertainty, and four alternative economic-need definitions (ratio, share gap, log ratio, rank based).

## Causal limitation

The study does not claim that recommendation systems caused Busan's observed spending distribution, nor that increased exposure automatically causes higher local revenue. It tests whether a controlled recommender can redistribute potential digital visibility while preserving relevance.

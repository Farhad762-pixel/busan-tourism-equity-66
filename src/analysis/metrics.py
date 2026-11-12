"""Metrics use all supplied districts, including districts with zero exposure."""

import math


def _nonnegative(values):
    numbers = [float(value) for value in values]
    if not numbers or any(not math.isfinite(x) or x < 0 for x in numbers):
        raise ValueError("Expected a nonempty sequence of finite nonnegative values")
    return numbers


def gini(values):
    numbers = sorted(_nonnegative(values))
    total = sum(numbers)
    if total == 0:
        return 0.0
    n = len(numbers)
    return sum((2 * i - n - 1) * x for i, x in enumerate(numbers, 1)) / (n * total)


def hhi(values):
    numbers = _nonnegative(values)
    total = sum(numbers)
    return sum((x / total) ** 2 for x in numbers) if total else 0.0


def ranked_exposure(rankings, districts):
    """Each ranking is a sequence of district names; ranks restart per query."""
    weights = dict.fromkeys(districts, 0.0)
    for ranking in rankings:
        for rank, district in enumerate(ranking, 1):
            if district not in weights:
                raise ValueError(f"Unknown district: {district}")
            weights[district] += 1 / math.log2(rank + 1)
    total = sum(weights.values())
    return {district: value / total if total else 0.0 for district, value in weights.items()}

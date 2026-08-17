"""Permutation-test discreteness floors (EXPERIMENT_PLAN_R3.md §2.3, §5.2).

A permutation test cannot report a p-value smaller than its own permutation
distribution admits. When that floor is at or above alpha, the test cannot reject
on any data, and reporting it as non-significant is a category error: the result
is undecidable, not null.

Revision 1 of the plan registered four confirmatory tests at B=5, whose floor is
0.0625 against alpha 0.003125. This module makes that arithmetic explicit so a
gate can act on it.
"""

from __future__ import annotations

from math import comb
from typing import Literal

Mode = Literal["paired_exact", "unpaired_exact", "monte_carlo", "not_applicable"]

_MODES = ("paired_exact", "unpaired_exact", "monte_carlo", "not_applicable")


def paired_exact_floor(n_pairs: int) -> float:
    """Smallest attainable two-sided p for a sign-flip test over n_pairs.

    There are 2**n_pairs sign assignments. By mirror symmetry the as-or-more-
    extreme count is always even, so the smallest attainable p is 2/2**n_pairs.
    """
    if n_pairs < 1:
        raise ValueError(f"n_pairs must be >= 1, got {n_pairs}")
    return 2.0 / (2 ** n_pairs)


def unpaired_exact_floor(n1: int, n2: int) -> float:
    """Smallest attainable two-sided p for an exact two-sample permutation test."""
    if n1 < 1 or n2 < 1:
        raise ValueError(f"group sizes must be >= 1, got {n1}, {n2}")
    return 2.0 / comb(n1 + n2, n1)


def monte_carlo_floor(n_permutations: int) -> float:
    """Smallest attainable p under the (1 + #extreme) / (1 + N) estimator."""
    if n_permutations < 1:
        raise ValueError(f"n_permutations must be >= 1, got {n_permutations}")
    return 1.0 / (1 + n_permutations)


def min_attainable_p(
    mode: Mode,
    *,
    n_pairs: int | None = None,
    n1: int | None = None,
    n2: int | None = None,
    n_permutations: int | None = None,
) -> float | None:
    """Dispatch to the floor appropriate to the test's mode.

    Returns None for `not_applicable` slots, which are exempt from the gate but
    still occupy their place in the family (§5.2).
    """
    if mode not in _MODES:
        raise ValueError(f"unknown permutation mode {mode!r}; expected one of {_MODES}")
    if mode == "not_applicable":
        return None
    if mode == "paired_exact":
        if n_pairs is None:
            raise ValueError("paired_exact requires n_pairs")
        return paired_exact_floor(n_pairs)
    if mode == "unpaired_exact":
        if n1 is None or n2 is None:
            raise ValueError("unpaired_exact requires n1 and n2")
        return unpaired_exact_floor(n1, n2)
    if n_permutations is None:
        raise ValueError("monte_carlo requires n_permutations")
    return monte_carlo_floor(n_permutations)


def ceiling_pairs(n_pairs: int, alpha: float) -> int:
    """How many as-or-more-extreme assignment *pairs* still permit rejection.

    This is the quantity tabulated in plan §2.3. Rejection needs
    count/2**B < alpha with count even, so the largest admissible even count is
    the largest even integer strictly below alpha * 2**B, and the pair count is
    half of it.
    """
    total = 2 ** n_pairs
    threshold = alpha * total
    m = int(threshold)
    if m == threshold:  # strict inequality: an exact hit is not admissible
        m -= 1
    if m % 2:
        m -= 1
    return max(m // 2, 0)


def discordance_tolerance(n_pairs: int, alpha: float) -> int:
    """Largest k tolerated in the equal-magnitude worst case (§2.3 table).

    With all |d_i| equal and k differences opposing the majority, the
    as-or-more-extreme count is 2 * sum_{s=0}^{k} C(B, s). Equal magnitudes
    maximise ties, so this is the pessimistic bound; unequal magnitudes with a
    small discordant difference do better.
    """
    total = 2 ** n_pairs
    threshold = alpha * total
    best = -1
    running = 0
    for k in range(n_pairs + 1):
        running += comb(n_pairs, k)
        if 2 * running < threshold:
            best = k
        else:
            break
    return best

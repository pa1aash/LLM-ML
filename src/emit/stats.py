"""Inference primitives (plan §2.3, §3.4). Deterministic and exhaustive where the
permutation distribution is small enough to enumerate, so a replay reproduces a
p-value bit for bit rather than approximately.
"""

from __future__ import annotations

import statistics
from itertools import combinations, product
from typing import Sequence


def paired_signflip_p(diffs: Sequence[float]) -> tuple[float, float, int, int]:
    """Exact two-sided sign-flip permutation p over paired differences.

    Under the null each difference's sign is exchangeable, so the reference set
    is all 2**B sign vectors. Returns (p, T_observed, n_as_extreme, n_assignments).
    """
    b = len(diffs)
    if b < 1:
        raise ValueError("need at least one paired difference")
    t_obs = statistics.fmean(diffs)
    target = abs(t_obs)
    n_extreme = 0
    for signs in product((1.0, -1.0), repeat=b):
        t = statistics.fmean([s * d for s, d in zip(signs, diffs)])
        if abs(t) >= target:
            n_extreme += 1
    total = 2 ** b
    return n_extreme / total, t_obs, n_extreme, total


def unpaired_perm_p(a: Sequence[float], b: Sequence[float]) -> tuple[float, float, int, int]:
    """Exact two-sided two-sample permutation p on the difference of means."""
    n1, n2 = len(a), len(b)
    pooled = list(a) + list(b)
    t_obs = statistics.fmean(a) - statistics.fmean(b)
    target = abs(t_obs)
    n_extreme = 0
    total = 0
    idx = range(n1 + n2)
    for pick in combinations(idx, n1):
        s = set(pick)
        ga = [pooled[i] for i in pick]
        gb = [pooled[i] for i in idx if i not in s]
        if abs(statistics.fmean(ga) - statistics.fmean(gb)) >= target:
            n_extreme += 1
        total += 1
    return n_extreme / total, t_obs, n_extreme, total


def cliffs_delta(a: Sequence[float], b: Sequence[float]) -> tuple[float, int]:
    """Cliff's delta and the Mann-Whitney U it derives from.

    delta = (#{a>b} - #{a<b}) / (n1*n2). Ties contribute 0 to the numerator and
    0.5 each to U, which is the convention that makes delta = 2*U/(n1*n2) - 1
    hold exactly. The plan does not state a tie convention; see the defect report.
    """
    n1, n2 = len(a), len(b)
    if n1 == 0 or n2 == 0:
        raise ValueError("both samples must be non-empty")
    gt = lt = ties = 0
    for x in a:
        for y in b:
            if x > y:
                gt += 1
            elif x < y:
                lt += 1
            else:
                ties += 1
    delta = (gt - lt) / (n1 * n2)
    u = gt + 0.5 * ties          # U for sample `a`
    return delta, u


def mean_std(xs: Sequence[float]) -> tuple[float, float]:
    return statistics.fmean(xs), (statistics.stdev(xs) if len(xs) > 1 else 0.0)

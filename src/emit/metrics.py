"""D (structural diversity) and S (surface diversity), per plan §2.4.

Both are mean pairwise distances over a batch. D operates on parsed design-choice
vectors; S operates on raw generated text and includes generations that failed to
parse, which is the whole point of it (§2.4.6).
"""

from __future__ import annotations

import math
import re
from itertools import combinations
from typing import Any, Iterable, Sequence

from . import constants as K

_WS = re.compile(r"\s+")


# ------------------------------------------------------------------ D (§2.4.2)

def pairwise_d(x: dict[str, Any], y: dict[str, Any]) -> float:
    """Field-level Hamming distance between two configurations.

                 sum_{b<=min} sum_{f in F} [x_bf != y_bf] + 6*|Bx-By| + sum_{g in G} [x_g != y_g]
        d(x,y) = -----------------------------------------------------------------------------
                                        6*max(Bx,By) + |G|

    d in [0,1], and d == 0 iff the two design-choice vectors are identical.
    """
    bx = x.get("blocks", [])
    by = y.get("blocks", [])
    nbx, nby = len(bx), len(by)

    mismatches = 0
    for i in range(min(nbx, nby)):
        for f in K.PER_BLOCK_FIELDS:
            if bx[i].get(f) != by[i].get(f):
                mismatches += 1
    mismatches += K.N_PER_BLOCK_FIELDS * abs(nbx - nby)
    for g in K.ARCH_LEVEL_FIELDS:
        if x.get(g) != y.get(g):
            mismatches += 1

    denom = K.N_PER_BLOCK_FIELDS * max(nbx, nby) + len(K.ARCH_LEVEL_FIELDS)
    if denom == 0:
        raise ValueError("both configurations have zero blocks and no arch fields")
    return mismatches / denom


def batch_diversity(configs: Sequence[dict[str, Any]]) -> float | None:
    """Mean of d over all C(n,2) unordered pairs of *parseable* generations.

    Returns None when fewer than 2 parseable generations are present (§2.7).
    Null is recorded, never imputed. An all-identical batch returns 0.0 exactly,
    which is a legal measurement rather than a missing value.
    """
    n = len(configs)
    if n < 2:
        return None
    total = 0.0
    count = 0
    for a, b in combinations(range(n), 2):
        total += pairwise_d(configs[a], configs[b])
        count += 1
    return total / count


def pooled_diversity(configs: Sequence[dict[str, Any]]) -> float | None:
    """D_cell_pooled: mean of d over all pairs of a cell, across batches (§2.4.5).

    A different estimand from the mean of within-batch D values: it additionally
    includes cross-batch pairs. Both are reported; thresholds apply to the batch
    mean, the bootstrap targets this.
    """
    return batch_diversity(configs)


# ------------------------------------------------------------------ S (§2.4.6)

def normalise_text(text: str) -> str:
    """Lowercase; collapse whitespace runs to one space; strip. Nothing else.

    No punctuation stripping, no code-fence removal, no JSON-aware handling: the
    measure must treat both prompt formats identically, and any format-aware
    normalisation would build the answer into the instrument.
    """
    return _WS.sub(" ", text.lower()).strip()


def trigram_set(text: str, n: int = K.SURFACE_NGRAM_N) -> frozenset[tuple[str, ...]]:
    toks = normalise_text(text).split(" ")
    toks = [t for t in toks if t]
    if len(toks) < n:
        return frozenset()
    return frozenset(tuple(toks[i : i + n]) for i in range(len(toks) - n + 1))


def pairwise_s(gx: frozenset, gy: frozenset) -> float:
    """Jaccard distance between two n-gram sets, with the §2.7 degenerate rules.

    Two empty sets -> 0.0 (identical and empty). One empty, one not -> 1.0.
    """
    if not gx and not gy:
        return 0.0
    if not gx or not gy:
        return 1.0
    return 1.0 - len(gx & gy) / len(gx | gy)


def batch_surface_diversity(texts: Sequence[str]) -> tuple[float | None, int]:
    """S(batch), and the count of generations with an empty n-gram set.

    Every generation in the batch is included, without exception, including those
    that failed to parse. A batch in which more than half the generations have
    empty n-gram sets yields None (§2.7).
    """
    n = len(texts)
    grams = [trigram_set(t) for t in texts]
    empty = sum(1 for g in grams if not g)
    if n < 2:
        return None, empty
    if empty * 2 > n:  # strictly more than half
        return None, empty
    total = 0.0
    count = 0
    for a, b in combinations(range(n), 2):
        total += pairwise_s(grams[a], grams[b])
        count += 1
    return total / count, empty


# ------------------------------------------------- per-field entropy (§2.4.4)

def normalised_field_entropy(configs: Iterable[dict[str, Any]], field: str) -> float | None:
    """Shannon entropy of a field's realised values, pooled across all block
    positions and generations, divided by log2(|vocab|). Constant field -> 0.0."""
    vocab = K.FIELD_VOCAB[field]
    counts: dict[Any, int] = {}
    total = 0
    for cfg in configs:
        for blk in cfg.get("blocks", []):
            v = blk.get(field)
            counts[v] = counts.get(v, 0) + 1
            total += 1
    if total == 0:
        return None
    h = 0.0
    for c in counts.values():
        p = c / total
        if p > 0:
            h -= p * math.log2(p)
    return h / math.log2(len(vocab))


# ------------------------------------------------------- classification (§2.6)

def classify_level(d: float, d_rand: float) -> str:
    if d < K.THRESHOLD_COLLAPSED * d_rand:
        return "collapsed"
    if d < K.THRESHOLD_DIVERSE * d_rand:
        return "reduced"  # same numeric band as `partial`
    return "diverse"


def classify_change(delta: float, d_rand: float, destination_label: str) -> str:
    if abs(delta) < K.THRESHOLD_NO_CHANGE * d_rand:
        return "no chg"
    if delta >= K.THRESHOLD_RECOVERS * d_rand and destination_label != "collapsed":
        return "recovers"
    return "other"

"""Anchor-tracking scorer — EXPERIMENT_PLAN_R4.md §2.4.7, §2.8.

This is the outcome the sixth prediction column is built on, and therefore the
one that decides C2 when the free-prose column is unreliable.

Everything below is REGISTERED at plan revision 5. Three things S3b had to decide
for itself are now in the plan:

  field collapse   normalised per-field entropy < 0.15 (plan 2.4.4, R5-4)
  denominators     tracks_first over all collapsed fields; tracks_exemplar over
                   the three the exemplar names (plan 2.4.7, R5-4)
  labelling        ONE-SIDED at the per-field chance rate (plan 2.6, R5-1)

The flat 0.50 bar and the symmetric per-field rule are both REJECTED. They are
still computed and emitted so a reader can see what the rejected rules would have
said, but `label_registered` is the one that scores.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field as dc_field
from typing import Any, Iterable, Sequence

from . import constants as K
from .metrics import normalised_field_entropy

try:
    from scipy.stats import norm as _norm

    def _phi(x: float) -> float:
        return float(_norm.cdf(x))

    def _phi_inv(p: float) -> float:
        return float(_norm.ppf(p))
except Exception:  # pragma: no cover - scipy is present in this environment
    def _phi(x: float) -> float:
        return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

    def _phi_inv(p: float) -> float:
        raise RuntimeError("scipy required for BCa")


# ---------------------------------------------------------------- field collapse

#: Plan 2.4.4 (R5-4). Mirrors D < 0.15*D_rand: normalised entropy is already
#: scaled so 1.0 is the uniform reference.
FIELD_COLLAPSE_ENTROPY_THRESHOLD = K.FIELD_COLLAPSE_ENTROPY_THRESHOLD

#: Plan 2.4.7 (R5-4). The three fields 2.8's exemplar actually specifies.
EXEMPLAR_FIELDS = ("conv_type", "activation", "normalization")

EXEMPLARS = {
    "modal": {"conv_type": "standard_3x3", "activation": "relu",
              "normalization": "batchnorm"},
    "non_modal": {"conv_type": "depthwise_separable", "activation": "gelu",
                  "normalization": "groupnorm"},
}


def enumeration_order(field: str, order: str) -> list:
    """The value list as the harness presents it, per §2.8."""
    vocab = list(K.FIELD_VOCAB[field])
    if order == "canonical":
        return vocab
    if order == "reversed":
        return list(reversed(vocab))
    raise ValueError(f"unknown enumeration order {order!r}")


def collapsed_fields(configs: Sequence[dict], threshold: float | None = None) -> list[str]:
    """Fields whose normalised entropy falls below the collapse threshold."""
    if threshold is None:
        threshold = FIELD_COLLAPSE_ENTROPY_THRESHOLD
    out = []
    for f in K.PER_BLOCK_FIELDS:
        h = normalised_field_entropy(configs, f)
        if h is not None and h < threshold:
            out.append(f)
    return out


def modal_value(configs: Sequence[dict], field: str, order: str) -> tuple[Any, bool]:
    """Most frequent realised value, ties broken toward the earlier-enumerated.

    Returns (value, tied). The tie-break deliberately biases toward finding
    tracking, so a null result is conservative and a positive one must be read
    with the tie count (§2.4.7).
    """
    counts: dict[Any, int] = {}
    for cfg in configs:
        for blk in cfg.get("blocks", []):
            v = blk.get(field)
            counts[v] = counts.get(v, 0) + 1
    if not counts:
        return None, False
    top = max(counts.values())
    tied_values = [v for v, c in counts.items() if c == top]
    order_list = enumeration_order(field, order)
    tied_values.sort(key=lambda v: order_list.index(v) if v in order_list else len(order_list))
    return tied_values[0], len(tied_values) > 1


# ------------------------------------------------------------------ per batch

@dataclass
class BatchTracking:
    collapsed: list[str]
    tracks_first: float | None          # proportion over collapsed fields
    tracks_exemplar: float | None       # proportion over collapsed EXEMPLAR_FIELDS
    n_first: int
    n_exemplar: int
    modal_tie_count: int
    no_collapse: bool = False           # plan 2.4.7: zero collapsed fields
    per_field_first: dict[str, int] = dc_field(default_factory=dict)
    per_field_exemplar: dict[str, int] = dc_field(default_factory=dict)

    def to_json(self) -> dict:
        return {
            "collapsed_fields": self.collapsed,
            "tracks_first": self.tracks_first,
            "tracks_exemplar": self.tracks_exemplar,
            "n_first": self.n_first,
            "n_exemplar": self.n_exemplar,
            "modal_tie_count": self.modal_tie_count,
            "no_collapse": self.no_collapse,
            "per_field_first": self.per_field_first,
            "per_field_exemplar": self.per_field_exemplar,
        }


def batch_tracking(configs: Sequence[dict], order: str, exemplar: str,
                   threshold: float | None = None) -> BatchTracking:
    """§2.4.7 for one batch at one stage. Zero collapsed fields -> null, never 0."""
    coll = collapsed_fields(configs, threshold)
    if not coll:
        # Plan 2.4.7: no collapse IS the evidence of no tracking, not a null.
        return BatchTracking([], None, None, 0, 0, 0, no_collapse=True)

    ties = 0
    first_hits: dict[str, int] = {}
    exemplar_hits: dict[str, int] = {}
    ex_values = EXEMPLARS[exemplar]

    for f in coll:
        modal, tied = modal_value(configs, f, order)
        ties += int(tied)
        first_hits[f] = int(modal == enumeration_order(f, order)[0])
        if f in EXEMPLAR_FIELDS:
            exemplar_hits[f] = int(modal == ex_values[f])

    tf = sum(first_hits.values()) / len(first_hits)
    te = (sum(exemplar_hits.values()) / len(exemplar_hits)) if exemplar_hits else None
    return BatchTracking(coll, tf, te, len(first_hits), len(exemplar_hits), ties,
                         False, first_hits, exemplar_hits)


# ------------------------------------------------------------------- BCa

def _bca(values: Sequence[float], n_boot: int, seed: int) -> tuple[float, float, float]:
    """BCa 95% interval on the mean. Returns (point, lo, hi).

    Falls back to the percentile interval when the bootstrap distribution is
    degenerate (every resample identical), which happens whenever every batch
    reports the same proportion — common with small collapsed-field counts.
    """
    n = len(values)
    point = sum(values) / n
    if n < 2:
        return point, point, point

    rng = random.Random(seed)
    boots = []
    for _ in range(n_boot):
        s = [values[rng.randrange(n)] for _ in range(n)]
        boots.append(sum(s) / n)
    boots.sort()

    n_less = sum(1 for b in boots if b < point)
    if n_less == 0 or n_less == n_boot:
        lo = boots[int(0.025 * (n_boot - 1))]
        hi = boots[int(0.975 * (n_boot - 1))]
        return point, lo, hi

    z0 = _phi_inv(n_less / n_boot)

    jack = []
    for i in range(n):
        rest = values[:i] + values[i + 1:]
        jack.append(sum(rest) / len(rest))
    jbar = sum(jack) / n
    num = sum((jbar - x) ** 3 for x in jack)
    den = 6.0 * (sum((jbar - x) ** 2 for x in jack) ** 1.5)
    a = num / den if den != 0 else 0.0

    out = []
    for q in (0.025, 0.975):
        z = _phi_inv(q)
        adj = z0 + (z0 + z) / (1 - a * (z0 + z))
        p = _phi(adj)
        p = min(max(p, 0.0), 1.0)
        out.append(boots[min(int(p * (n_boot - 1)), n_boot - 1)])
    return point, out[0], out[1]


# ------------------------------------------------------------------ labelling

def label_against(point: float, lo: float, hi: float, bar: float) -> str:
    """§2.6's three-way label, generalised over the reference bar.

    The plan registers bar = 0.50 flat. The per-field form passes the chance rate.
    `indeterminate` also covers the boundary case lo == bar or hi == bar, which
    §2.6 leaves open (S3B-04): an interval whose endpoint sits exactly on the bar
    does not exclude it.
    """
    if lo > bar:
        return "tracks"
    if hi < bar:
        return "no tracking"
    return "indeterminate"


def is_dissociable(order: str, exemplar: str) -> bool:
    """Plan 2.5 (R5-5): can tracks_first and tracks_exemplar be told apart here?

    Under `canonical` order the first-enumerated values of the three exemplar
    fields ARE the `modal` exemplar's values, so in the (canonical, modal) cell
    the two sub-quantities are numerically identical and tracks_exemplar is
    excluded from the grid.
    """
    ex = EXEMPLARS[exemplar]
    return any(enumeration_order(f, order)[0] != ex[f] for f in EXEMPLAR_FIELDS)


def label_null_at_chance(point: float, lo: float, hi: float, bar: float) -> str:
    """THE REGISTERED RULE (plan 2.6, R5-1). One-sided, against chance.

    The substantive null IS chance: a genuine prior produces a tracking rate AT
    chance, not below it. So:

        tracks        -> the interval excludes the bar from ABOVE (lo > bar)
        no tracking   -> the interval CONTAINS the bar, or lies below it
        indeterminate -> reserved for insufficient data, decided upstream

    Under the two rejected symmetric rules `genuine prior` can essentially never
    MATCH the tracking column, because "no tracking" would require the observed
    rate to sit measurably BELOW chance — which nothing predicts.

    `indeterminate` is NOT produced here: plan 2.6 reserves it for insufficient
    data, decided upstream from the usable-batch count.
    """
    if lo > bar:
        return "tracks"
    return "no tracking"


def chance_rate(fields: Iterable[str]) -> float:
    """Vocabulary-weighted expected tracking rate under a genuine prior.

    Each collapsed field contributes 1/|V_f|; the aggregate is their mean over
    every (batch, field) collapsed instance.
    """
    fs = list(fields)
    if not fs:
        return float("nan")
    return sum(1.0 / len(K.FIELD_VOCAB[f]) for f in fs) / len(fs)


# ------------------------------------------------------------------- per cell

@dataclass
class CellTracking:
    quantity: str                       # "tracks_first" | "tracks_exemplar"
    point: float | None
    ci95: tuple[float, float] | None
    n_batches_used: int
    n_null_batches: int
    n_no_collapse_batches: int
    modal_tie_count: int
    chance_rate: float
    label_registered: str               # plan 2.6 R5-1: one-sided at chance
    label_flat: str                     # REJECTED rev-4 rule, reported only
    label_chance: str                   # REJECTED symmetric rule, reported only
    per_field: dict[str, dict]
    reason: str = "measured"            # measured | no_collapse | insufficient_data

    def to_json(self) -> dict:
        return {
            "quantity": self.quantity,
            "point": self.point,
            "ci95": list(self.ci95) if self.ci95 else None,
            "n_batches_used": self.n_batches_used,
            "n_null_batches": self.n_null_batches,
            "n_no_collapse_batches": self.n_no_collapse_batches,
            "modal_tie_count": self.modal_tie_count,
            "chance_rate": self.chance_rate,
            "label_registered": self.label_registered,
            "tracking_label_rule": K.TRACKING_LABEL_RULE,
            "rejected_label_flat_0p50": self.label_flat,
            "rejected_label_per_field_symmetric": self.label_chance,
            "rejected_rules_agree_with_registered":
                self.label_flat == self.label_chance == self.label_registered,
            "reason": self.reason,
            "per_field": self.per_field,
        }


def cell_tracking(batches: Sequence[BatchTracking], quantity: str,
                  n_boot: int = K.BOOTSTRAP_RESAMPLES,
                  seed: int = K.BOOTSTRAP_SEED) -> CellTracking:
    """Aggregate batch proportions to a cell, with both labelling rules.

    The bootstrap unit is the BATCH (S3B-03): §2.4.5's registered unit is the
    generation, but the statistic here is a per-batch proportion over fields, and
    generations are not its sampling unit.
    """
    vals = [getattr(b, quantity) for b in batches]
    used = [v for v in vals if v is not None]
    n_nc = sum(1 for b in batches if b.no_collapse)
    n_null = len(vals) - len(used) - n_nc
    ties = sum(b.modal_tie_count for b in batches)

    if quantity == "tracks_first":
        instances = [f for b in batches for f in b.per_field_first]
    else:
        instances = [f for b in batches for f in b.per_field_exemplar]
    cr = chance_rate(instances)

    per_field: dict[str, dict] = {}
    key = "per_field_first" if quantity == "tracks_first" else "per_field_exemplar"
    fields_seen: set[str] = set()
    for b in batches:
        fields_seen |= set(getattr(b, key))
    for f in sorted(fields_seen):
        hits = [getattr(b, key)[f] for b in batches if f in getattr(b, key)]
        if not hits:
            continue
        p, lo, hi = _bca(hits, n_boot, seed)
        f_chance = 1.0 / len(K.FIELD_VOCAB[f])
        per_field[f] = {
            "n": len(hits), "point": p, "ci95": [lo, hi],
            "chance_rate": f_chance,
            "label_flat_0p50": label_against(p, lo, hi, K.ANCHOR_TRACKING_THRESHOLD),
            "label_per_field_chance": label_against(p, lo, hi, f_chance),
        }

    # Plan 2.4.7: a majority of no-collapse batches IS `no tracking`, not null.
    if n_nc * 2 > len(batches):
        return CellTracking(quantity, None, None, len(used), n_null, n_nc, ties, cr,
                            "no tracking", "no tracking", "no tracking", per_field,
                            reason="no_collapse")

    # Plan 2.7: `indeterminate` comes from insufficient data only. no_collapse
    # batches count as usable.
    min_usable = max(2, int(0.4 * len(batches)))
    if not used or (len(used) + n_nc) < min_usable:
        return CellTracking(quantity, None, None, len(used), n_null, n_nc, ties, cr,
                            "indeterminate", "indeterminate", "indeterminate",
                            per_field, reason="insufficient_data")

    point, lo, hi = _bca(used, n_boot, seed)
    return CellTracking(
        quantity, point, (lo, hi), len(used), n_null, n_nc, ties, cr,
        label_null_at_chance(point, lo, hi, cr),                       # registered
        label_against(point, lo, hi, K.ANCHOR_TRACKING_THRESHOLD),     # rejected
        label_against(point, lo, hi, cr),                              # rejected
        per_field, reason="measured",
    )


def score_cell(batch_configs: Sequence[Sequence[dict]], order: str, exemplar: str,
               n_boot: int = K.BOOTSTRAP_RESAMPLES,
               seed: int = K.BOOTSTRAP_SEED,
               threshold: float | None = None) -> dict:
    """End-to-end: batches of configs -> both tracking quantities for one cell."""
    bts = [batch_tracking(cfgs, order, exemplar, threshold) for cfgs in batch_configs]
    return {
        "enumeration_order": order,
        "exemplar": exemplar,
        "exemplar_dissociable": is_dissociable(order, exemplar),
        "batches": [b.to_json() for b in bts],
        "tracks_first": cell_tracking(bts, "tracks_first", n_boot, seed).to_json(),
        "tracks_exemplar": cell_tracking(bts, "tracks_exemplar", n_boot, seed).to_json(),
    }


# ------------------------------------------- cross-level exemplar response
# Plan revision 6 §2.5a. The single-cell `tracks_exemplar` reading cannot
# separate `format tax` from `genuine prior`: a format tax tracks WHICHEVER
# exemplar is shown, so it is high in both exemplar cells, and a genuine prior's
# fixed modal value coincides with the shown exemplar at chance in each. The
# discriminating question is not "does the modal match the exemplar" but "does
# the modal MOVE when the exemplar changes".

def cross_level_delta_batch(
    modal_by_field_modal_cell: dict[str, Any],
    modal_by_field_non_modal_cell: dict[str, Any],
) -> tuple[float | None, int]:
    """Delta_exemplar for one batch index, pooled over both exemplar cells.

        own   = modal equals the exemplar shown in ITS OWN cell
        other = modal equals the exemplar shown in the OTHER cell
        delta = mean(own) - mean(other), over both cells' collapsed exemplar fields

    The pairing makes the null EXACT rather than merely expected: if the modal
    value v is the same in both cells -- which is what a genuine prior, a repair
    artifact, quantisation and decoding all imply -- then
    sum(own) = [v = e_modal] + [v = e_non_modal] = sum(other), so delta is
    identically 0. Only a modal that MOVES with the exemplar makes it positive.

    Returns (delta, n_fields_used); (None, 0) if no exemplar field is collapsed
    in either cell.
    """
    e_m = EXEMPLARS["modal"]
    e_n = EXEMPLARS["non_modal"]
    own, other = [], []
    for f in EXEMPLAR_FIELDS:
        v = modal_by_field_modal_cell.get(f)
        if v is not None:
            own.append(int(v == e_m[f]))
            other.append(int(v == e_n[f]))
        v = modal_by_field_non_modal_cell.get(f)
        if v is not None:
            own.append(int(v == e_n[f]))
            other.append(int(v == e_m[f]))
    if not own:
        return None, 0
    return (sum(own) - sum(other)) / len(own), len(own)


def label_cross_level(point: float, lo: float, hi: float) -> str:
    """Plan §2.6, one-sided against a chance rate of EXACTLY ZERO.

    Delta is identically 0 under every rival whose modal value does not move
    with the exemplar, so the null needs no chance-rate estimate at all.
    """
    return "responds" if lo > 0.0 else "no response"


def cross_level_cell(
    deltas: Sequence[float | None],
    n_boot: int = K.BOOTSTRAP_RESAMPLES,
    seed: int = K.BOOTSTRAP_SEED,
    min_usable_fraction: float = 0.4,
) -> dict:
    """Aggregate per-batch deltas to a cell-pair verdict."""
    used = [d for d in deltas if d is not None]
    n_null = len(deltas) - len(used)
    min_usable = max(2, int(min_usable_fraction * len(deltas)))
    if len(used) < min_usable:
        return {"quantity": "cross_level_exemplar", "point": None, "ci95": None,
                "n_batches_used": len(used), "n_null_batches": n_null,
                "label_registered": "indeterminate", "reason": "insufficient_data",
                "chance_rate": 0.0}
    point, lo, hi = _bca(used, n_boot, seed)
    return {"quantity": "cross_level_exemplar", "point": point, "ci95": [lo, hi],
            "n_batches_used": len(used), "n_null_batches": n_null,
            "label_registered": label_cross_level(point, lo, hi),
            "reason": "measured", "chance_rate": 0.0}

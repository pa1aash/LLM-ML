"""Generalised signature scorer — EXPERIMENT_PLAN_R4.md §2.5, §2.6.

Five rivals, six columns. Columns 1-3 are levels on D, 4-5 are changes in D, 6
is the anchor-tracking pattern.

Decisions taken to proceed, recorded in audit/S3B_SCORER_DEFECTS.md:

  S3B-05  The anchor-tracking column's rival predictions are PROSE PATTERNS over
          four quantities (pre/post x first/exemplar), while §2.6's label
          vocabulary defines a label for ONE proportion. Encoded here as an
          explicit predicate per rival over the 2x2 label grid.

  S3B-06  `recovers` is defined as dD >= 0.25*D_rand, and a change meeting that
          bound whose destination is still `collapsed` is "demoted to partial" —
          but `partial` is defined as dD < 0.25*D_rand. The demotion therefore
          assigns a label outside its own numeric band. Implemented as the plan
          directs (demotion wins) with the contradiction recorded.

  S3B-07  An indeterminate column lowers n_s, which lowers ceil(0.75*n_s). So
          while indeterminacy can never add a MATCHED CELL, it CAN create a
          winner that did not exist before. Verified in fixture C14.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

from . import constants as K

COLUMNS = ("free_prose", "schema_pre_repair", "post_repair", "bf16",
           "high_temp", "anchor_tracking")
COLUMN_KIND = {"free_prose": "level", "schema_pre_repair": "level",
               "post_repair": "level", "bf16": "change", "high_temp": "change",
               "anchor_tracking": "tracking"}

#: §2.5, transcribed. Level/change cells are labels; the tracking cell is the
#: name of a predicate defined below (S3B-05).
RIVALS: dict[str, dict[str, str]] = {
    "repair artifact": {
        "free_prose": "diverse", "schema_pre_repair": "diverse",
        "post_repair": "collapsed", "bf16": "no chg", "high_temp": "no chg",
        "anchor_tracking": "post_only",
    },
    "format tax": {
        "free_prose": "diverse", "schema_pre_repair": "collapsed",
        "post_repair": "collapsed", "bf16": "no chg", "high_temp": "no chg",
        "anchor_tracking": "pre_present",
    },
    "quantisation": {
        "free_prose": "partial", "schema_pre_repair": "partial",
        "post_repair": "partial", "bf16": "recovers", "high_temp": "partial",
        "anchor_tracking": "none",
    },
    "decoding": {
        "free_prose": "reduced", "schema_pre_repair": "reduced",
        "post_repair": "reduced", "bf16": "no chg", "high_temp": "recovers",
        "anchor_tracking": "none",
    },
    "genuine prior": {
        "free_prose": "collapsed", "schema_pre_repair": "collapsed",
        "post_repair": "collapsed", "bf16": "no chg", "high_temp": "no chg",
        "anchor_tracking": "none",
    },
}

#: §2.6: `reduced` and `partial` name the same numeric band at level.
_LEVEL_CANON = {"partial": "reduced", "reduced": "reduced",
                "collapsed": "collapsed", "diverse": "diverse"}

INDETERMINATE = "indeterminate"


# ------------------------------------------------------------------ labelling

def classify_level(d: float, d_rand: float) -> str:
    """§2.6 levels. Boundaries are strict `<`, so a value exactly on a boundary
    falls in the UPPER band, deterministically (S3B-08 / fixture C13)."""
    if d < K.THRESHOLD_COLLAPSED * d_rand:
        return "collapsed"
    if d < K.THRESHOLD_DIVERSE * d_rand:
        return "reduced"
    return "diverse"


def classify_change(delta: float, d_rand: float, destination_label: str) -> str:
    """§2.6 changes: no chg / partial / recovers / worsens."""
    if delta <= K.THRESHOLD_WORSENS * d_rand:
        return "worsens"
    if abs(delta) < K.THRESHOLD_NO_CHANGE * d_rand:
        return "no chg"
    if delta >= K.THRESHOLD_RECOVERS * d_rand:
        # S3B-06: the demotion assigns `partial` outside its own numeric band.
        return "partial" if destination_label == "collapsed" else "recovers"
    if delta >= K.THRESHOLD_PARTIAL_CHANGE_LOWER * d_rand:
        return "partial"
    return "worsens"   # negative, past the no-change band


# ------------------------------------------- the anchor-tracking predicates

def _grid(obs: dict[str, str]) -> dict[str, str]:
    """Normalise the 2x2 label grid: pre_first, pre_exemplar, post_first,
    post_exemplar."""
    return {k: obs.get(k, INDETERMINATE) for k in
            ("pre_first", "pre_exemplar", "post_first", "post_exemplar")}


def _tracking_match(prediction: str, obs: dict[str, str]) -> str:
    """Return 'match', 'mismatch', or 'indeterminate' for the tracking column.

    S3B-05: each rival's prose row is encoded as a predicate over the grid. A
    predicate whose READ quantities include an `indeterminate` yields
    `indeterminate` for that rival's column; quantities the predicate does not
    read cannot make it indeterminate.
    """
    g = _grid(obs)

    if prediction == "post_only":
        # "post-repair modal tracks first-enumerated; pre-repair does not"
        reads = ("post_first", "pre_first")
        if any(g[r] == INDETERMINATE for r in reads):
            return INDETERMINATE
        return "match" if (g["post_first"] == "tracks"
                           and g["pre_first"] == "no tracking") else "mismatch"

    if prediction == "pre_present":
        # "pre-repair modal tracks first-enumerated and/or exemplar"
        reads = ("pre_first", "pre_exemplar")
        if g["pre_first"] == "tracks" or g["pre_exemplar"] == "tracks":
            return "match"
        if any(g[r] == INDETERMINATE for r in reads):
            return INDETERMINATE
        return "mismatch"

    if prediction == "none":
        # "no tracking" / "no tracking under any permutation"
        reads = ("pre_first", "pre_exemplar", "post_first", "post_exemplar")
        if any(g[r] == "tracks" for r in reads):
            return "mismatch"
        if any(g[r] == INDETERMINATE for r in reads):
            return INDETERMINATE
        return "match"

    raise ValueError(f"unknown tracking prediction {prediction!r}")


# --------------------------------------------------------------------- scoring

@dataclass
class Verdict:
    winner: str | None
    verdict: str
    scores: dict[str, int]
    n_scoreable: int
    threshold: int
    scoreable: list[str]
    indeterminate: list[str]
    observations: dict[str, Any]

    def to_json(self) -> dict:
        return {
            "winner": self.winner, "verdict": self.verdict,
            "scores": self.scores, "n_scoreable": self.n_scoreable,
            "winning_threshold": self.threshold,
            "scoreable_columns": self.scoreable,
            "indeterminate_columns": self.indeterminate,
            "observations": self.observations,
        }


def _cell_match(column: str, observed: Any, predicted: str) -> str:
    if observed == INDETERMINATE:
        return INDETERMINATE
    if COLUMN_KIND[column] == "tracking":
        return _tracking_match(predicted, observed)
    if COLUMN_KIND[column] == "level":
        return "match" if _LEVEL_CANON[observed] == _LEVEL_CANON[predicted] else "mismatch"
    # change column: `worsens` matches nothing, by §2.6
    return "match" if observed == predicted else "mismatch"


def score(observations: dict[str, Any]) -> Verdict:
    """§2.6 signature scoring over six columns.

    `observations` maps each column to its observed label — or to
    `"indeterminate"`, or, for `anchor_tracking`, to the 2x2 label grid.
    """
    per_rival_cell: dict[str, dict[str, str]] = {}
    for rival, row in RIVALS.items():
        per_rival_cell[rival] = {
            c: _cell_match(c, observations.get(c, INDETERMINATE), row[c])
            for c in COLUMNS
        }

    # A column is unscoreable if it is indeterminate for ANY rival that reads it.
    indeterminate = [
        c for c in COLUMNS
        if any(per_rival_cell[r][c] == INDETERMINATE for r in RIVALS)
    ]
    scoreable = [c for c in COLUMNS if c not in indeterminate]
    n_s = len(scoreable)

    scores = {r: sum(1 for c in scoreable if per_rival_cell[r][c] == "match")
              for r in RIVALS}

    if n_s < K.SIGNATURE_MIN_SCOREABLE:
        return Verdict(None, "no verdict — too few scoreable columns", scores,
                       n_s, 0, scoreable, indeterminate, observations)

    threshold = math.ceil(K.SIGNATURE_WIN_FRACTION * n_s)
    best = max(scores.values())
    leaders = [r for r, v in scores.items() if v == best]

    if best == 0:
        return Verdict(None, "no rival matched — the five-rival set is incomplete",
                       scores, n_s, threshold, scoreable, indeterminate, observations)
    if len(leaders) > 1:
        return Verdict(None,
                       "no clean winner — mixed attribution (tie: "
                       + ", ".join(sorted(leaders)) + ")",
                       scores, n_s, threshold, scoreable, indeterminate, observations)
    if best < threshold:
        return Verdict(None,
                       f"no clean winner — mixed attribution (leader {leaders[0]!r} "
                       f"scored {best} < threshold {threshold})",
                       scores, n_s, threshold, scoreable, indeterminate, observations)
    return Verdict(leaders[0], f"{leaders[0]} wins {best}/{n_s} (threshold {threshold})",
                   scores, n_s, threshold, scoreable, indeterminate, observations)

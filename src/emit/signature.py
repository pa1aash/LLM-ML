"""Generalised signature scorer — EXPERIMENT_PLAN_R5.md §2.5, §2.6.

Five rivals, six columns. Columns 1-3 are levels on D, 4-5 are changes in D, 6
is the anchor-tracking pattern.

All of this is REGISTERED at plan revision 5:

  2.5  the five tracking predicates, each reading all four grid entries; every
       rival predicts on BOTH sub-quantities at BOTH stages (R5-5)
  2.6  `partial` (change) widened so the recovers-into-collapse demotion no
       longer lands outside its own band (R5-10)
  2.6  indeterminacy may create winners; the verdict carries
       `contingent_on_indeterminacy` rather than the behaviour being prevented
       (R5-6)
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

#: Plan 2.5, transcribed. Level/change cells are labels; the tracking cell names
#: a predicate defined below.
RIVALS: dict[str, dict[str, str]] = {
    "repair artifact": {
        "free_prose": "diverse", "schema_pre_repair": "diverse",
        "post_repair": "collapsed", "bf16": "no chg", "high_temp": "no chg",
        "anchor_tracking": "R-A",
    },
    "format tax": {
        "free_prose": "diverse", "schema_pre_repair": "collapsed",
        "post_repair": "collapsed", "bf16": "no chg", "high_temp": "no chg",
        "anchor_tracking": "F-T",
    },
    "quantisation": {
        "free_prose": "partial", "schema_pre_repair": "partial",
        "post_repair": "partial", "bf16": "recovers", "high_temp": "partial",
        "anchor_tracking": "NONE",
    },
    "decoding": {
        "free_prose": "reduced", "schema_pre_repair": "reduced",
        "post_repair": "reduced", "bf16": "no chg", "high_temp": "recovers",
        "anchor_tracking": "NONE",
    },
    "genuine prior": {
        "free_prose": "collapsed", "schema_pre_repair": "collapsed",
        "post_repair": "collapsed", "bf16": "no chg", "high_temp": "no chg",
        "anchor_tracking": "NONE",
    },
}

#: Plan 2.6: `reduced` and `partial` name the same numeric band at level.
_LEVEL_CANON = {"partial": "reduced", "reduced": "reduced",
                "collapsed": "collapsed", "diverse": "diverse"}

INDETERMINATE = "indeterminate"


# ------------------------------------------------------------------ labelling

def classify_level(d: float, d_rand: float) -> str:
    """Plan 2.6 levels. Boundaries are strict `<`, so a value exactly on a
    boundary falls in the UPPER band, deterministically."""
    if d < K.THRESHOLD_COLLAPSED * d_rand:
        return "collapsed"
    if d < K.THRESHOLD_DIVERSE * d_rand:
        return "reduced"
    return "diverse"


def classify_change(delta: float, d_rand: float, destination_label: str) -> str:
    """Plan 2.6 changes: no chg / partial / recovers / worsens.

    `partial` is the band [0.10, 0.25)*D_rand OR a recovers-magnitude change into
    a collapsed destination (R5-10). The four labels partition the line.
    """
    if delta <= K.THRESHOLD_WORSENS * d_rand:
        return "worsens"
    if abs(delta) < K.THRESHOLD_NO_CHANGE * d_rand:
        return "no chg"
    if delta >= K.THRESHOLD_RECOVERS * d_rand:
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


#: Plan 2.5 (R5-5). Every rival predicts on both sub-quantities at both stages.
GRID_KEYS = ("pre_first", "pre_exemplar", "post_first", "post_exemplar")

#: Which grid entries each predicate READS. A predicate is indeterminate only if
#: an entry it reads is (plan 2.5).
PREDICATE_READS = {
    "R-A":  ("pre_first", "pre_exemplar", "post_first"),
    "F-T":  GRID_KEYS,
    "NONE": GRID_KEYS,
}


def _tracking_match(prediction: str, obs: dict[str, str]) -> str:
    """'match' / 'mismatch' / 'indeterminate' for the tracking column (plan 2.5).

    An entry excluded as non-dissociable (the (canonical, modal) cell) must have
    been filled from a dissociable cell of the same model before reaching here.
    """
    if prediction not in PREDICATE_READS:
        raise ValueError(f"unknown tracking prediction {prediction!r}")
    g = _grid(obs)
    if any(g[k] == INDETERMINATE for k in PREDICATE_READS[prediction]):
        return INDETERMINATE

    if prediction == "R-A":
        # sanitize_config coerces to valid_vals[0] -- the first-enumerated value
        # -- and never sees the exemplar, which is a prompt object.
        hit = (g["pre_first"] == "no tracking"
               and g["pre_exemplar"] == "no tracking"
               and g["post_first"] == "tracks")
    elif prediction == "F-T":
        # The prompt drives the choice before repair, on whichever of the two it
        # makes salient; repair only coerces illegal values, so post mirrors pre.
        # The disjunction is NECESSARY: in a dissociable cell one modal value
        # cannot equal both the first-enumerated and the exemplar value.
        hit = ((g["pre_first"] == "tracks" or g["pre_exemplar"] == "tracks")
               and g["post_first"] == g["pre_first"]
               and g["post_exemplar"] == g["pre_exemplar"])
    else:
        hit = all(g[k] == "no tracking" for k in GRID_KEYS)
    return "match" if hit else "mismatch"


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
    contingent_on_indeterminacy: bool = False
    would_win_at_n_s_6: bool | None = None

    def to_json(self) -> dict:
        return {
            "winner": self.winner, "verdict": self.verdict,
            "scores": self.scores, "n_scoreable": self.n_scoreable,
            "winning_threshold": self.threshold,
            "scoreable_columns": self.scoreable,
            "indeterminate_columns": self.indeterminate,
            "n_indeterminate": len(self.indeterminate),
            "contingent_on_indeterminacy": self.contingent_on_indeterminacy,
            "would_win_at_n_s_6": self.would_win_at_n_s_6,
            "observations": self.observations,
        }


def _cell_match(column: str, observed: Any, predicted: str) -> str:
    if observed == INDETERMINATE:
        return INDETERMINATE
    if COLUMN_KIND[column] == "tracking":
        return _tracking_match(predicted, observed)
    if COLUMN_KIND[column] == "level":
        return "match" if _LEVEL_CANON[observed] == _LEVEL_CANON[predicted] else "mismatch"
    # change column: `worsens` matches nothing, by plan 2.6
    return "match" if observed == predicted else "mismatch"


def score(observations: dict[str, Any]) -> Verdict:
    """Plan 2.6 signature scoring over six columns.

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
    # Plan 2.6 (R5-6). Indeterminacy CAN create a winner, because the threshold
    # scales with n_s. Not prevented -- flagged.
    full_threshold = math.ceil(K.SIGNATURE_WIN_FRACTION * len(COLUMNS))  # 5
    contingent = best < full_threshold
    verdict = f"{leaders[0]} wins {best}/{n_s} (threshold {threshold})"
    if contingent:
        verdict += (f" — CONTINGENT ON INDETERMINACY: {len(indeterminate)} column(s) "
                    f"unscoreable; at n_s=6 the threshold would be {full_threshold} "
                    f"and this rival scored {best}")
    return Verdict(leaders[0], verdict, scores, n_s, threshold, scoreable,
                   indeterminate, observations,
                   contingent_on_indeterminacy=contingent,
                   would_win_at_n_s_6=(not contingent))

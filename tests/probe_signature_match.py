"""Block E probe — can §2.5/§2.6 signature matching be implemented as written?

Not a test of the code. A test of the PLAN: this attempts to build the scorer the
plan describes and records every point at which the text does not determine the
behaviour. Each blocker below is a place where two implementers would produce
different verdicts from the same data.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from emit import constants as K  # noqa: E402
from emit.metrics import classify_change, classify_level  # noqa: E402

# The falsifier set, transcribed verbatim from plan §2.5.
RIVALS = {
    "repair artifact": ["diverse", "diverse", "collapsed", "no chg", "no chg"],
    "format tax":      ["diverse", "collapsed", "collapsed", "no chg", "no chg"],
    "quantisation":    ["partial", "partial", "partial", "recovers", "partial"],
    "decoding":        ["reduced", "reduced", "reduced", "no chg", "recovers"],
    "genuine prior":   ["collapsed", "collapsed", "collapsed", "no chg", "no chg"],
}
COLUMNS = ["free-prose", "schema pre-repair", "post-repair", "bf16", "high temp"]
KIND = ["level", "level", "level", "change", "change"]

LEVEL_LABELS = {"collapsed", "reduced", "partial", "diverse"}
CHANGE_LABELS = {"no chg", "recovers"}          # the only two §2.6 defines

BLOCKERS: list[dict] = []


def blocker(ref: str, problem: str, decided: str) -> None:
    BLOCKERS.append({"ref": ref, "problem": problem, "decided": decided})


def audit_label_vocabulary() -> None:
    for rival, row in RIVALS.items():
        for col, kind, label in zip(COLUMNS, KIND, row):
            if kind == "change" and label not in CHANGE_LABELS:
                blocker(
                    "§2.5 / §2.6",
                    f"rival {rival!r} predicts {label!r} in the CHANGE column "
                    f"{col!r}, but §2.6 defines only {sorted(CHANGE_LABELS)} for a "
                    f"change. {label!r} is a LEVEL label with no delta-D rule.",
                    "scored as UNSCOREABLE; that cell can never match, which "
                    "silently caps this rival at 4 of 5",
                )
            if kind == "level" and label not in LEVEL_LABELS:
                blocker("§2.5", f"{rival}/{col}: unknown level label {label!r}", "n/a")


def audit_pairwise_distinctness() -> None:
    """§2.5 asserts all five signatures are pairwise distinct. Check it, treating
    `reduced` and `partial` as the same band, which §2.6 says they are."""
    def canon(row):
        return tuple("reduced" if v == "partial" else v for v in row)

    names = list(RIVALS)
    collisions = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = canon(RIVALS[names[i]]), canon(RIVALS[names[j]])
            diff = [c for c, x, y in zip(COLUMNS, a, b) if x != y]
            if not diff:
                collisions.append((names[i], names[j]))
            elif len(diff) == 1:
                blocker(
                    "§2.5",
                    f"{names[i]!r} and {names[j]!r} differ in exactly ONE column "
                    f"({diff[0]!r}) once `partial` is folded into `reduced` as "
                    f"§2.6 requires. If that column is indeterminate the two are "
                    f"indistinguishable.",
                    "recorded; no code change",
                )
    for a, b in collisions:
        blocker("§2.5", f"{a!r} and {b!r} are NOT distinct after folding "
                        f"`partial` into `reduced`", "recorded")


def audit_change_classifier() -> None:
    d_rand = 0.771931  # measured, see tests/compute_d_rand.py
    out = classify_change(0.15 * d_rand, d_rand, "reduced")
    if out not in CHANGE_LABELS:
        blocker(
            "§2.6",
            f"a delta-D of 0.15*D_rand is neither `no chg` (<0.10) nor `recovers` "
            f"(>=0.25); the classifier returns {out!r}, a value no rival predicts. "
            f"§2.6 gives no name for the 0.10-0.25 band, and no rule for how an "
            f"unnamed observation scores.",
            "returns 'other'; scores 0 against every rival for that column",
        )
    neg = classify_change(-0.30 * d_rand, d_rand, "collapsed")
    blocker(
        "§2.6",
        f"a large NEGATIVE delta-D (further collapse) classifies as {neg!r}. "
        f"`recovers` is defined only for positive change; no rival predicts a "
        f"named label for a strong negative change.",
        "returns 'other'",
    )


def audit_operand_resolution() -> None:
    blocker(
        "§2.5 column definitions vs §2.2",
        "every column is defined at a specific precision (NF4). The frontier "
        "model has NO precision factor; its cells record "
        "precision='provider_default (unknown)'. The plan says the frontier "
        "'contributes to the format, repair and temperature columns' but never "
        "states the substitution rule for the NF4 coordinate.",
        "would have to assume provider_default substitutes for NF4; not stated",
    )
    blocker(
        "§2.5 vs §2.6",
        "the free-prose COLUMN is defined on post-repair D, but §2.6's "
        "reliability caveat and the format-tax/genuine-prior discrimination are "
        "both argued about free-prose PRE-repair diversity. The scored quantity "
        "and the caveated quantity are different stages.",
        "scored the column as defined (post-repair); caveat applies to pre-repair",
    )
    blocker(
        "§2.6 indeterminate rescaling",
        "the rescaling rule is given for exactly ONE indeterminate column "
        "('max score drops to 4, the >=4-of-5 rule reads >=3-of-4'). Two "
        "independent mechanisms can produce indeterminate cells — the free-prose "
        "parse-rate rule and the bootstrap boundary-straddle rule — so two or "
        "more indeterminate columns are reachable, and the plan gives no rule "
        "for that case.",
        "would need a general rule such as ceil(0.8*n_scoreable); not stated",
    )


def audit_threshold_operands() -> None:
    blocker(
        "§2.6 vs §2.4.5",
        "levels are classified from D_mean (batch-mean form), but the bootstrap "
        "interval that can force a cell to `indeterminate` is computed on "
        "D_cell_pooled — a different estimand (it includes cross-batch pairs). "
        "A boundary-straddle test therefore compares an interval on one quantity "
        "against a threshold applied to another. Measured gap on random draws: "
        "0.0026 absolute, against a no-change band of 0.077.",
        "recorded; used D_mean for classification as §2.6 directs",
    )
    blocker(
        "§2.6 vs §5.5",
        "labels depend on D_rand, but the E1 results-file schema has no field for "
        "D_rand. It lives in a separate results/E1_reference.json. A results file "
        "therefore carries `label_pre`/`label_post` without the reference value "
        "that produced them.",
        "emitted the reference to its own file; provenance gap remains",
    )
    blocker(
        "§2.5 change columns",
        "delta-D is never defined as a difference of D_mean or of D_pooled. §2.6 "
        "applies thresholds to D_mean; §2.4.5 bootstraps delta on pooled. Both "
        "readings are supported by the text.",
        "used difference of D_mean for classification",
    )


def main() -> int:
    audit_label_vocabulary()
    audit_pairwise_distinctness()
    audit_change_classifier()
    audit_operand_resolution()
    audit_threshold_operands()

    print(f"SIGNATURE-MATCHING PROBE: {len(BLOCKERS)} points where the plan does "
          f"not determine the behaviour\n")
    for i, b in enumerate(BLOCKERS, 1):
        print(f"{i:>2}. [{b['ref']}]")
        for line in _wrap(b["problem"], 92):
            print(f"    {line}")
        print(f"    -> decided: {b['decided']}")
        print()
    return 0


def _wrap(text: str, width: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


if __name__ == "__main__":
    raise SystemExit(main())

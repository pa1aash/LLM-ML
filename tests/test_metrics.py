"""Block C1-C5 — known-answer tests on D and S.

Every expected value here is derived by hand from the plan's definitions and
stated in the assertion, so a disagreement between the code and the plan shows up
as a failed test rather than as a plausible-looking number.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from emit.metrics import (  # noqa: E402
    batch_diversity,
    batch_surface_diversity,
    normalise_text,
    pairwise_d,
    pairwise_s,
    trigram_set,
)

RESULTS: list[dict] = []


def block(**over):
    base = {
        "conv_type": "standard_3x3",
        "channels": 64,
        "activation": "relu",
        "normalization": "batchnorm",
        "skip_connection": "identity",
        "pooling": "none",
    }
    base.update(over)
    return base


def arch(n_blocks=4, blocks=None, global_pool="avg", fc_layers=1):
    return {
        "blocks": blocks if blocks is not None else [block() for _ in range(n_blocks)],
        "global_pool": global_pool,
        "fc_layers": fc_layers,
    }


def record(name, expected, actual, ok, note=""):
    RESULTS.append(
        {"case": name, "expected": expected, "actual": actual, "ok": ok, "note": note}
    )


# ------------------------------------------------------------------------ C1

def c1_identical():
    xs = [arch() for _ in range(20)]
    d = batch_diversity(xs)
    ok = d == 0.0
    record("C1 D over identical set", "0.0 exactly", repr(d), ok,
           "d == 0 iff design-choice vectors identical; 0.0 is a legal measurement")
    # also the pairwise primitive
    assert pairwise_d(arch(), arch()) == 0.0


# ------------------------------------------------------------------------ C2

def c2_one_field():
    """Two 4-block architectures differing in exactly one per-block field.

    numerator   = 1 mismatch
    denominator = 6 * max(4,4) + |G| = 24 + 2 = 26
    d           = 1/26 = 0.038461538461538464
    """
    a = arch(4)
    b = arch(4)
    b["blocks"][2]["activation"] = "gelu"
    expected = float(Fraction(1, 26))
    got = pairwise_d(a, b)
    ok = got == expected
    record("C2 D, exactly one field differs", f"1/26 = {expected!r}", repr(got), ok,
           "numerator 1; denominator 6*max(4,4)+2 = 26")
    d_set = batch_diversity([a, b])
    assert d_set == expected


# ------------------------------------------------------------------------ C3

def c3_monotonic():
    """Six fields differing must exceed one field differing.

    all six fields of one block  -> 6/26 = 3/13
    """
    a = arch(4)
    one = arch(4)
    one["blocks"][2]["activation"] = "gelu"
    six = arch(4)
    six["blocks"][2] = block(
        conv_type="bottleneck", channels=256, activation="mish",
        normalization="none", skip_connection="none", pooling="maxpool",
    )
    d1 = pairwise_d(a, one)
    d6 = pairwise_d(a, six)
    expected6 = float(Fraction(6, 26))
    ok = d6 == expected6 and d6 > d1
    record("C3 D monotone in mismatch count", f"6/26 = {expected6!r} > 1/26",
           f"{d6!r} > {d1!r}", ok, "strictly increasing in field mismatches")

    # Block-count mismatch uses the 6*|Bx-By| term with a max() denominator.
    a3, a6 = arch(3), arch(6)
    expected_bc = float(Fraction(6 * 3, 6 * 6 + 2))
    got_bc = pairwise_d(a3, a6)
    ok2 = got_bc == expected_bc
    record("C3b D across block counts 3 vs 6", f"18/38 = {expected_bc!r}",
           repr(got_bc), ok2, "6*|3-6| = 18 over 6*max(3,6)+2 = 38")


# ------------------------------------------------------------------------ C4

def c4_surface_bounds():
    same = ["alpha beta gamma delta epsilon"] * 8
    s_same, empt = batch_surface_diversity(same)
    ok1 = s_same == 0.0
    record("C4a S over identical strings", "0.0 exactly", repr(s_same), ok1,
           f"empty-trigram count {empt}")

    # Two texts whose 3-gram sets are disjoint.
    a = "one two three four five"
    b = "six seven eight nine ten"
    ga, gb = trigram_set(a), trigram_set(b)
    assert ga and gb and not (ga & gb)
    s_disj, _ = batch_surface_diversity([a, b])
    ok2 = s_disj == 1.0
    record("C4b S over disjoint 3-gram sets", "1.0 exactly", repr(s_disj), ok2,
           f"|A|={len(ga)}, |B|={len(gb)}, |A&B|=0")

    # Normalisation is minimal and format-blind.
    ok3 = normalise_text("  A\n\tB   c  ") == "a b c"
    record("C4c normalisation", "'a b c'", repr(normalise_text("  A\n\tB   c  ")), ok3,
           "lowercase, collapse whitespace, strip; nothing else")


# ------------------------------------------------------------------------ C5

def c5_degenerate():
    empty = trigram_set("hi there")          # 2 tokens < n=3 -> empty set
    nonempty = trigram_set("a b c d")
    assert not empty and nonempty

    ok1 = pairwise_s(empty, frozenset()) == 0.0
    record("C5a two empty 3-gram sets", "0.0", repr(pairwise_s(empty, frozenset())),
           ok1, "both identical and empty")

    ok2 = pairwise_s(empty, nonempty) == 1.0
    record("C5b one empty, one not", "1.0", repr(pairwise_s(empty, nonempty)), ok2)

    # More than half the batch empty -> S = null. 6 of 10 is strictly more.
    texts = ["hi"] * 6 + ["a b c d e"] * 4
    s_null, n_empty = batch_surface_diversity(texts)
    ok3 = s_null is None and n_empty == 6
    record("C5c >half batch empty", "None (6/10 empty)", f"{s_null!r} ({n_empty}/10)", ok3,
           "recorded as null, never imputed")

    # Exactly half is NOT more than half -> S defined.
    texts2 = ["hi"] * 5 + ["a b c d e"] * 5
    s_half, n_half = batch_surface_diversity(texts2)
    ok4 = s_half is not None and n_half == 5
    record("C5d exactly half empty", "not None (5/10)", f"{s_half!r} ({n_half}/10)", ok4,
           "'more than half' is strict")


def main() -> int:
    for fn in (c1_identical, c2_one_field, c3_monotonic, c4_surface_bounds, c5_degenerate):
        fn()
    w = max(len(r["case"]) for r in RESULTS)
    print(f"{'CASE'.ljust(w)}  {'EXPECTED':<28} {'ACTUAL':<28} OK")
    print("-" * (w + 64))
    for r in RESULTS:
        print(f"{r['case'].ljust(w)}  {r['expected']:<28} {r['actual']:<28} "
              f"{'yes' if r['ok'] else 'NO  <-- FINDING'}")
    print()
    for r in RESULTS:
        if r["note"]:
            print(f"  {r['case']}: {r['note']}")
    bad = [r for r in RESULTS if not r["ok"]]
    print()
    print(f"{len(RESULTS) - len(bad)}/{len(RESULTS)} known-answer cases matched.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())

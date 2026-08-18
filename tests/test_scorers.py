"""Block C — adversarial fixtures for the two scorers that decide C2.

All data here is synthetic and constructed by hand. No model is involved.

Each fixture states what the plan requires and what the code produced. A scorer
that returns a plausible answer for a case it should refuse is the finding.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emit import constants as K  # noqa: E402
from emit.anchor import (  # noqa: E402
    EXEMPLARS, batch_tracking, cell_tracking, chance_rate, collapsed_fields,
    enumeration_order, is_dissociable, modal_value,
)
from emit.signature import (  # noqa: E402
    INDETERMINATE, RIVALS, classify_change, classify_level, score,
)

DR = K.D_RAND  # 0.719205
RESULTS: list[dict] = []
DISAGREEMENTS: list[dict] = []


def record(case: str, expected: str, actual: str, note: str = "") -> None:
    RESULTS.append({"case": case, "expected": expected, "actual": actual,
                    "ok": expected == actual, "note": note})


# --------------------------------------------------------------- level helpers

LVL = {"collapsed": 0.05 * DR, "reduced": 0.35 * DR, "diverse": 0.80 * DR}


def obs(free, pre, post, bf16, temp, tracking):
    return {"free_prose": free, "schema_pre_repair": pre, "post_repair": post,
            "bf16": bf16, "high_temp": temp, "anchor_tracking": tracking}


TRACK_NONE = {"pre_first": "no tracking", "pre_exemplar": "no tracking",
              "post_first": "no tracking", "post_exemplar": "no tracking"}
TRACK_POST_ONLY = {"pre_first": "no tracking", "pre_exemplar": "no tracking",
                   "post_first": "tracks", "post_exemplar": "no tracking"}
# A satisfiable format-tax grid: the prompt drove the model to the
# first-enumerated value, and repair left it there.
TRACK_PRE = {"pre_first": "tracks", "pre_exemplar": "no tracking",
             "post_first": "tracks", "post_exemplar": "no tracking"}


# ---------------------------------------------------------------- C1 .. C5

RIVAL_FIXTURES = {
    "repair artifact": obs("diverse", "diverse", "collapsed", "no chg", "no chg",
                           TRACK_POST_ONLY),
    "format tax": obs("diverse", "collapsed", "collapsed", "no chg", "no chg",
                      TRACK_PRE),
    "quantisation": obs("reduced", "reduced", "reduced", "recovers", "partial",
                        TRACK_NONE),
    "decoding": obs("reduced", "reduced", "reduced", "no chg", "recovers",
                    TRACK_NONE),
    "genuine prior": obs("collapsed", "collapsed", "collapsed", "no chg", "no chg",
                         TRACK_NONE),
}


def c1_to_c5():
    for i, (rival, o) in enumerate(RIVAL_FIXTURES.items(), start=1):
        v = score(o)
        record(f"C{i}  {rival} signature", f"winner={rival}",
               f"winner={v.winner}",
               f"scores={v.scores}, n_s={v.n_scoreable}, thr={v.threshold}")


# ------------------------------------------------------------------- C6, C7

def c6_no_rival():
    """A true zero-match observation, and whether one is even reachable.

    Finding S3B-09: across the three LEVEL columns the three labels
    {collapsed, reduced, diverse} partition the space, and in free-prose every
    one of them is predicted by some rival. So free-prose can never mismatch all
    five, and `best == 0` is unreachable while free-prose is scoreable.
    """
    never_matched: dict[str, list[str]] = {}
    for col in ("free_prose", "schema_pre_repair", "post_repair"):
        vals = ["collapsed", "reduced", "diverse"]
        never_matched[col] = [v for v in vals
                              if not any(_LEVEL_CANON_EQ(RIVALS[r][col], v)
                                         for r in RIVALS)]
    for col in ("bf16", "high_temp"):
        vals = ["no chg", "partial", "recovers", "worsens"]
        never_matched[col] = [v for v in vals
                              if not any(RIVALS[r][col] == v for r in RIVALS)]

    # The most hostile observation available: pick a never-matched value wherever
    # one exists, otherwise the value matching the fewest rivals.
    o = obs("diverse", "diverse", "diverse", "worsens", "worsens", TRACK_POST_ONLY)
    v = score(o)
    reachable = (v.winner is None and "no rival matched" in v.verdict)
    record("C6  most hostile observation available",
           "zero-match unreachable",
           "zero-match unreachable" if not reachable else "zero-match reached",
           f"scores={v.scores}; values matching NO rival, per column: "
           + "; ".join(f"{c}:{never_matched[c] or 'none'}" for c in never_matched))

    # The only corner where zero-match IS reachable: free_prose and
    # schema_pre_repair indeterminate (they can never mismatch all five), the
    # remaining level column on `diverse`, both change columns on `worsens`, and
    # a tracking grid that fails every rival.
    track_nobody = {"pre_first": "no tracking", "pre_exemplar": "no tracking",
                    "post_first": "no tracking", "post_exemplar": "tracks"}
    forced = obs(INDETERMINATE, INDETERMINATE, "diverse", "worsens", "worsens",
                 track_nobody)
    v2 = score(forced)
    record("C6b zero-match branch when the level columns are removed",
           "no rival matched",
           "no rival matched" if (v2.winner is None and "no rival matched" in v2.verdict)
           else f"{v2.verdict}",
           f"n_s={v2.n_scoreable}, scores={v2.scores}")


def _LEVEL_CANON_EQ(a, b):
    canon = {"partial": "reduced", "reduced": "reduced",
             "collapsed": "collapsed", "diverse": "diverse"}
    return canon[a] == canon[b]


def c7_tie():
    """Force a genuine top tie.

    schema_pre_repair indeterminate removes the cell separating repair-artifact
    from format-tax; a TRACK_NONE grid makes both of them fail the tracking cell
    that genuine-prior passes. All three land on the same score.
    """
    o = obs("diverse", INDETERMINATE, "collapsed", "no chg", "no chg", TRACK_NONE)
    v = score(o)
    leaders = sorted(r for r, sc in v.scores.items() if sc == max(v.scores.values()))
    record("C7  rivals tie at the top", "mixed attribution",
           "mixed attribution" if (v.winner is None and "mixed attribution" in v.verdict)
           else f"winner={v.winner}",
           f"leaders={leaders}, scores={v.scores}, n_s={v.n_scoreable}, "
           f"verdict={v.verdict!r}")


# ------------------------------------------------------------ C8, C9, C10

def _indet(o, cols):
    o = dict(o)
    for c in cols:
        o[c] = INDETERMINATE
    return o


def c8_one_indeterminate():
    o = _indet(RIVAL_FIXTURES["format tax"], ["free_prose"])
    v = score(o)
    record("C8  one column indeterminate", "n_s=5, threshold=4",
           f"n_s={v.n_scoreable}, threshold={v.threshold}",
           f"winner={v.winner}, scores={v.scores}")


def c9_two_indeterminate():
    o = _indet(RIVAL_FIXTURES["format tax"], ["free_prose", "bf16"])
    v = score(o)
    record("C9  two indeterminate", "n_s=4, threshold=3",
           f"n_s={v.n_scoreable}, threshold={v.threshold}",
           f"winner={v.winner}, scores={v.scores}")


def c10_three_indeterminate():
    o = _indet(RIVAL_FIXTURES["format tax"], ["free_prose", "bf16", "high_temp"])
    v = score(o)
    record("C10 three indeterminate", "no verdict",
           "no verdict" if (v.winner is None and "no verdict" in v.verdict)
           else f"winner={v.winner} / {v.verdict}",
           f"n_s={v.n_scoreable}")


# ------------------------------------------------------------ C11, C12, C13

def c11_partial_band():
    delta = 0.15 * DR                       # inside [0.10, 0.25)
    lab = classify_change(delta, DR, destination_label="reduced")
    record("C11 change in the partial band", "partial", lab,
           f"dD={delta:.6f}, band [{0.10*DR:.6f}, {0.25*DR:.6f})")

    # the demotion rule: >= 0.25 but destination still collapsed -> partial
    lab2 = classify_change(0.30 * DR, DR, destination_label="collapsed")
    record("C11b recovers demoted by collapsed destination", "partial", lab2,
           f"dD={0.30*DR:.6f} >= {0.25*DR:.6f} but destination collapsed "
           f"(S3B-06: label sits outside its own numeric band)")


def c12_worsens():
    delta = -0.30 * DR
    lab = classify_change(delta, DR, destination_label="collapsed")
    o = obs("diverse", "collapsed", "collapsed", lab, "no chg", TRACK_PRE)
    v = score(o)
    bf16_matches = [r for r in RIVALS if RIVALS[r]["bf16"] == lab]
    record("C12 worsens scores mismatch for all", "worsens / 0 rivals match",
           f"{lab} / {len(bf16_matches)} rivals match",
           f"format tax still leads on the other columns: scores={v.scores}, "
           f"verdict={v.verdict!r}")


def c13_exact_boundary():
    d = K.THRESHOLD_COLLAPSED * DR          # exactly 0.15 * D_rand
    lab = classify_level(d, DR)
    below = classify_level(math.nextafter(d, 0.0), DR)
    record("C13 D exactly on the collapsed boundary", "reduced", lab,
           f"D={d!r}; rule is strict `<`, so the boundary belongs to the UPPER "
           f"band. One ULP below gives {below!r}. Deterministic, no tie-break needed.")


# ------------------------------------------------------------------- C14

def c14_straddle():
    """A straddling interval makes a column indeterminate.

    Two claims are checked separately, because only the first is true:
      (i)  it can never ADD a matched cell   -> verified
      (ii) it can never create a WINNER      -> FALSE, and demonstrated
    """
    base = RIVAL_FIXTURES["format tax"]
    v0 = score(base)
    v1 = score(_indet(base, ["free_prose"]))
    added = {r: v1.scores[r] - v0.scores[r] for r in RIVALS}
    never_added = all(v <= 0 for v in added.values())
    record("C14a straddle never adds a matched cell", "True", str(never_added),
           f"score deltas={added}")

    # Winner-creating case: format-tax fails BOTH change columns, so it sits at
    # 4/6 against threshold 5 and no one wins. Make one of the columns it already
    # failed indeterminate: 4/5 against threshold 4, and it wins.
    o = obs("diverse", "collapsed", "collapsed", "recovers", "recovers", TRACK_PRE)
    before = score(o)
    after = score(_indet(o, ["bf16"]))
    record("C14b straddle CAN create a winner", "before=None, after=format tax",
           f"before={before.winner}, after={after.winner}",
           f"before: {before.scores['format tax']}/{before.n_scoreable} vs thr "
           f"{before.threshold}; after: {after.scores['format tax']}/"
           f"{after.n_scoreable} vs thr {after.threshold}. Lowering n_s lowers "
           f"ceil(0.75*n_s) — S3B-07.")


# --------------------------------------------------------- C15 (the point)

def _block(**over):
    base = {"conv_type": "standard_3x3", "channels": 64, "activation": "relu",
            "normalization": "batchnorm", "skip_connection": "identity",
            "pooling": "maxpool"}
    base.update(over)
    return base


def _cfg(blocks):
    return {"blocks": blocks, "global_pool": "avg", "fc_layers": 1}


def _constant_batch(n=20, k=4, **over):
    """A batch whose every block is the same, so every field is collapsed."""
    return [_cfg([_block(**over) for _ in range(k)]) for _ in range(n)]


def _diverse_batch(n=20, k=4, order="canonical"):
    """A batch that cycles every field through its vocabulary -> no collapse."""
    out = []
    for i in range(n):
        blocks = []
        for b in range(k):
            over = {}
            for j, f in enumerate(K.PER_BLOCK_FIELDS):
                vocab = enumeration_order(f, order)
                over[f] = vocab[(i + b + j) % len(vocab)]
            blocks.append(_block(**over))
        out.append(_cfg(blocks))
    return out


def c15_repair_vs_format():
    """The case the sixth column exists for.

    Free-prose is FORCED indeterminate, which under revision 3 would have left
    repair-artifact and format-tax separated by nothing they could both be scored
    on. Here they must still separate.
    """
    nb = K.N_BATCHES_PER_CELL

    # repair-artifact truth: pre-repair diverse (no collapse), post-repair
    # collapsed onto the FIRST-enumerated value of every field.
    first_vals = {f: enumeration_order(f, "canonical")[0] for f in K.PER_BLOCK_FIELDS}
    ra_pre = [_diverse_batch() for _ in range(nb)]
    ra_post = [_constant_batch(**first_vals) for _ in range(nb)]

    # format-tax truth: collapsed onto the first-enumerated value ALREADY at
    # pre-repair, and still there after.
    ft_pre = [_constant_batch(**first_vals) for _ in range(nb)]
    ft_post = [_constant_batch(**first_vals) for _ in range(nb)]

    # Plan 2.5: (canonical, modal) is the DEGENERATE cell -- the first-enumerated
    # values of the three exemplar fields ARE the modal exemplar's values, so
    # tracks_first and tracks_exemplar cannot be dissociated there. The fixture
    # therefore runs in a dissociable cell.
    def grid(pre_batches, post_batches, order="canonical", exemplar="non_modal"):
        assert is_dissociable(order, exemplar), (order, exemplar)
        g = {}
        for stage, batches in (("pre", pre_batches), ("post", post_batches)):
            bts = [batch_tracking(b, order, exemplar) for b in batches]
            for q, short in (("tracks_first", "first"), ("tracks_exemplar", "exemplar")):
                ct = cell_tracking(bts, q, n_boot=2000)
                g[f"{stage}_{short}"] = ct.label_registered
                g[f"{stage}_{short}_chance"] = ct.label_chance
                if ct.label_registered != ct.label_flat:
                    DISAGREEMENTS.append({
                        "fixture": "C15", "stage": stage, "quantity": q,
                        "point": ct.point, "ci95": ct.ci95,
                        "chance_rate": ct.chance_rate,
                        "registered": ct.label_registered,
                        "rejected_flat_0p50": ct.label_flat,
                    })
        return g

    ra_grid = grid(ra_pre, ra_post)
    ft_grid = grid(ft_pre, ft_post)

    ra_obs = obs(INDETERMINATE, "diverse", "collapsed", "no chg", "no chg",
                 {k: v for k, v in ra_grid.items() if not k.endswith("_chance")})
    ft_obs = obs(INDETERMINATE, "collapsed", "collapsed", "no chg", "no chg",
                 {k: v for k, v in ft_grid.items() if not k.endswith("_chance")})

    ra_v, ft_v = score(ra_obs), score(ft_obs)
    record("C15a repair-artifact, free-prose indeterminate",
           "winner=repair artifact", f"winner={ra_v.winner}",
           f"grid={ {k: v for k, v in ra_grid.items() if not k.endswith('_chance')} }, "
           f"n_s={ra_v.n_scoreable}, scores={ra_v.scores}")
    record("C15b format-tax, free-prose indeterminate",
           "winner=format tax", f"winner={ft_v.winner}",
           f"grid={ {k: v for k, v in ft_grid.items() if not k.endswith('_chance')} }, "
           f"n_s={ft_v.n_scoreable}, scores={ft_v.scores}")

    separated = (ra_v.winner == "repair artifact" and ft_v.winner == "format tax"
                 and ra_v.winner != ft_v.winner)
    record("C15c the two rivals separate on the tracking column alone",
           "True", str(separated),
           "free-prose indeterminate for both; the only column distinguishing "
           "them is anchor_tracking (schema_pre_repair also differs, which is "
           "the second discriminator revision 4 added)")


# ------------------------------------------------------------------- C16

def c16_genuine_prior_invariance():
    """A genuine prior: the modal value is a property of the model, so it is the
    SAME under both enumeration orders. The scorer must not read invariance as
    an instrument effect."""
    nb = K.N_BATCHES_PER_CELL
    # Collapsed onto a value that is NOT first under either order.
    # Must avoid BOTH enumeration heads AND BOTH exemplars on the three exemplar
    # fields, or a coincidence reads as tracking (see the S3b/S2d defect report).
    fixed = {"conv_type": "dilated_3x3", "channels": 128, "activation": "silu",
             "normalization": "layernorm", "skip_connection": "projection",
             "pooling": "strided_conv"}
    batches = [_constant_batch(**fixed) for _ in range(nb)]

    grids = {}
    for order in ("canonical", "reversed"):
        bts = [batch_tracking(b, order, "non_modal") for b in batches]
        cf = cell_tracking(bts, "tracks_first", n_boot=2000)
        ce = cell_tracking(bts, "tracks_exemplar", n_boot=2000)
        grids[order] = {"first": cf, "exemplar": ce}
        if cf.label_registered != cf.label_flat:
            DISAGREEMENTS.append({
                "fixture": f"C16 ({order})", "stage": "post", "quantity": "tracks_first",
                "point": cf.point, "ci95": cf.ci95, "chance_rate": cf.chance_rate,
                "registered": cf.label_registered,
                "rejected_flat_0p50": cf.label_flat})

    both_none = all(grids[o]["first"].label_registered == "no tracking"
                    and grids[o]["exemplar"].label_registered == "no tracking"
                    for o in grids)
    record("C16a no tracking under either enumeration order", "True", str(both_none),
           "canonical: first=" + grids["canonical"]["first"].label_registered
           + ", exemplar=" + grids["canonical"]["exemplar"].label_registered
           + " | reversed: first=" + grids["reversed"]["first"].label_registered
           + ", exemplar=" + grids["reversed"]["exemplar"].label_registered)

    g = {"pre_first": "no tracking", "pre_exemplar": "no tracking",
         "post_first": grids["canonical"]["first"].label_registered,
         "post_exemplar": grids["canonical"]["exemplar"].label_registered}
    v = score(obs("collapsed", "collapsed", "collapsed", "no chg", "no chg", g))
    record("C16b invariance is not read as an instrument effect",
           "winner=genuine prior", f"winner={v.winner}",
           f"scores={v.scores}; the tracking column matches `none` for the three "
           f"rivals that predict it and mismatches the two that predict tracking")


# --------------------------------------------------- the two-bar comparison

def bar_comparison():
    """Where the flat 0.50 bar and the per-field chance rates disagree.

    Sweeps a synthetic proportion across the range, at a realistic collapsed-field
    mix, and reports the bands in which the two rules give different labels.
    """
    print("\nFLAT 0.50 BAR vs PER-FIELD CHANCE RATES")
    print("  vocabulary sizes: " + ", ".join(
        f"{f}={len(K.FIELD_VOCAB[f])}" for f in K.PER_BLOCK_FIELDS))
    all_six = list(K.PER_BLOCK_FIELDS)
    cr_all = chance_rate(all_six)
    print(f"  chance rate over all six fields          = {cr_all:.6f}")
    cr_ex = chance_rate(["conv_type", "activation", "normalization"])
    print(f"  chance rate over the 3 exemplar fields   = {cr_ex:.6f}")
    print(f"  REJECTED flat bar (rev 4)                = {K.ANCHOR_TRACKING_THRESHOLD:.6f}")
    print(f"  REGISTERED rule (rev 5)                  = {K.TRACKING_LABEL_RULE}")
    print()
    print(f"  {'true rate':>10} {'point':>8} {'ci95':>20} {'flat 0.50':>14} "
          f"{'per-field sym':>14} {'REGISTERED':>14}  disagree")
    rows = []
    for true_rate in (0.10, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.60, 0.75, 0.90):
        n = K.N_BATCHES_PER_CELL
        vals = [1.0 if i < round(true_rate * n) else 0.0 for i in range(n)]
        from emit.anchor import _bca, label_against, label_null_at_chance  # noqa
        p, lo, hi = _bca(vals, 4000, K.BOOTSTRAP_SEED)
        lf = label_against(p, lo, hi, K.ANCHOR_TRACKING_THRESHOLD)
        lc = label_against(p, lo, hi, cr_all)
        ln = label_null_at_chance(p, lo, hi, cr_all)
        dis = "YES" if len({lf, lc, ln}) > 1 else ""
        rows.append((true_rate, p, lo, hi, lf, lc, ln, dis))
        print(f"  {true_rate:>10.2f} {p:>8.4f} [{lo:>7.4f},{hi:>7.4f}] {lf:>14} "
              f"{lc:>14} {ln:>14}  {dis}")
    n_dis = sum(1 for r in rows if r[7])
    print(f"\n  {n_dis}/{len(rows)} sampled rates give different verdicts.")
    return rows


def main() -> int:
    c1_to_c5(); c6_no_rival(); c7_tie()
    c8_one_indeterminate(); c9_two_indeterminate(); c10_three_indeterminate()
    c11_partial_band(); c12_worsens(); c13_exact_boundary(); c14_straddle()
    c15_repair_vs_format(); c16_genuine_prior_invariance()

    w = max(len(r["case"]) for r in RESULTS)
    print(f"{'CASE'.ljust(w)}  {'EXPECTED':<34} {'ACTUAL':<34} OK")
    print("-" * (w + 76))
    for r in RESULTS:
        print(f"{r['case'].ljust(w)}  {r['expected']:<34} {r['actual']:<34} "
              f"{'yes' if r['ok'] else 'NO  <-- FINDING'}")
    print()
    for r in RESULTS:
        if r["note"]:
            print(f"  {r['case']}:\n    {r['note']}")

    bar_comparison()

    if DISAGREEMENTS:
        print("\nLABELLING DISAGREEMENTS OBSERVED IN THE FIXTURES")
        for d in DISAGREEMENTS:
            print(f"  {d['fixture']} {d['stage']}/{d['quantity']}: point={d['point']}, "
                  f"ci={d['ci95']}, chance={d['chance_rate']:.4f} -> "
                  f"flat={d['flat_0p50']}, per-field={d['per_field']}")
    else:
        print("\nNo flat-vs-per-field disagreement arose inside the C15/C16 "
              "fixtures themselves (they are constructed at the extremes, where "
              "both rules agree). The disagreement band is in the sweep above.")

    bad = [r for r in RESULTS if not r["ok"]]
    print(f"\n{len(RESULTS) - len(bad)}/{len(RESULTS)} fixture assertions matched.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())

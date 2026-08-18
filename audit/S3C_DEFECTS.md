# S3C — DEFECTS FOUND AND DELIBERATELY NOT FIXED IN REVISION 6

**Session:** S3c, 2026-08-18. **Governing plan:** `EXPERIMENT_PLAN_R6.md`,
SHA-256 `d63a7625f06dcbaa08ad35182490036de12c3d0354febee9e141656ec79d340b`.

**Revision 6's scope was closed by construction** and carries exactly three
things: the two pilot-confirmed design parameters, the cross-level exemplar
predicate, and the corrected pilot criterion. Everything below was found this
session and **deliberately not folded in.**

**The reason is the pattern, not indifference.** Five revisions in two days each
added machinery to close the previous round's gaps, and each addition generated
more: 25 defects at S3a, 18 at S3b, three inside revision 5's own drafting. A plan
that keeps acquiring apparatus is converging on complexity, not on rigour, and
complexity is where the next defect lives. **After G2 each item below is handled
as a `DEVIATIONS.md` implementation decision — logged before the affected analysis
runs, never as a silent choice.**

---

## S3C-01 — MATERIAL — the E2 power pilot's substrate is simulated, not the benchmark

**Plan §3.5** says the pilot variance is drawn "from the benchmark's own
best-of-20 distribution by pure table sampling". **The NAS-Bench-201 tables are
not in this repository**, and fetching them is outside a no-compute session.

`scripts/power_e2.py` therefore simulates the pool — Beta(8,2) scaled to
[0.10, 0.74], bounded and left-skewed like a tabular NAS accuracy table — with the
run outcome the max of k = 20 draws, exactly as a run is defined.

**Why this is weaker than it looks, and where it still bites.** The registered
effect size is Cliff's δ, a **rank** statistic, and power at a fixed δ is driven
by distributional overlap, which the simulation controls by construction. But the
registered *test statistic* is a **difference of means**, which is scale- and
shape-sensitive, so the mapping from δ = 0.62 to a mean shift is synthetic.

**Post-G2 handling:** re-run the pilot against the real table once it is present,
before the first E2 run. If it returns R > 24, raising R is compliance (§3.4); if
it returns R ≤ 24, R stays at 24 because R_final is fixed once. **Log as a
`DEVIATIONS.md` entry either way**, since the substrate differs from what §3.5
registers.

---

## S3C-02 — MATERIAL — the tracking pilot's collapse model is assumed, not measured

`scripts/pilot_tracking.py` assumes each field collapses independently with
probability **0.80**, which is a guess about post-repair schema cells, not a
measurement. `B_tracking = 28` is conditional on it.

**Direction of the error is known:** a *lower* true collapse rate means fewer
fields per batch, coarser proportions, wider intervals — so 28 would be too small.
A higher rate makes 28 conservative.

**Post-G2 handling:** the first completed anchor cell yields the real collapse
rate. If it is materially below 0.80, re-run the pilot and raise `B_tracking`
before the remaining cells — compliance under §8.2, logged as a deviation.

---

## S3C-03 — MATERIAL — single-cell `tracks_exemplar` is emitted but read by nothing

Revision 6 removed it from the predicates (§2.5) because it cannot separate
`format tax` from `genuine prior`, and replaced it with the cross-level delta. It
is still computed, still emitted (A21), and now **scored by no rival**.

That is deliberate — it remains a useful descriptive quantity and the reader can
see the coincidence rate directly — but a quantity in the results file that no
predicate reads is an invitation to over-read it in the manuscript.

**Post-G2 handling:** the manuscript must label it descriptive-only wherever it
appears. Not a plan change.

---

## S3C-04 — MINOR — the cross-level delta assumes both exemplar cells share a batch index

§2.5a pools "at the same batch index" across the modal and non-modal cells. The
shared seed vector makes that well-defined, **but if one cell has a null batch and
the other does not, the pair is broken** and the plan does not say whether to drop
the pair or fall back to an unpaired difference.

**Decided for the implementation:** drop the pair — the exactness of the null
depends on comparing the *same* batch index across cells, and an unpaired
difference would forfeit it.

**Post-G2 handling:** `DEVIATIONS.md` entry recording the drop rule before the
first cross-level computation.

---

## S3C-05 — MINOR — `B_tracking` and `B_batch` now differ, and X5 pairs on the larger

The main grid runs at `B_batch = 16`; the twelve anchor cells run at
`B_tracking = 28`. X5 pairs on (batch, exemplar) **within the anchor cells**, so it
has 56 pairs. Nothing breaks — X5 runs by Monte Carlo and its floor depends on N —
but the plan now carries two batch counts and a reader could conflate them.

**Post-G2 handling:** naming discipline in the emitter and the manuscript. Already
distinguished in `src/emit/constants.py`.

---

## S3C-06 — MINOR — the pilots are quarantined by convention, not by mechanism

Both pilot files carry `pilot: true`, `confirmatory: false`,
`quarantined_from_analysis: true`, and live under `results/pilots/`. **Nothing in
the emitter enforces the quarantine** — the gates count confirmatory statistics in
the results file, and a pilot record placed in the wrong file would not be caught.

**Post-G2 handling:** an emitter assertion that `results/pilots/` is never read by
the analysis path. A three-line check, logged as a deviation when added.

---

## Summary

| ID | Severity | Post-G2 route |
|---|---|---|
| S3C-01 | MATERIAL | re-run the pilot against the real table; `DEVIATIONS.md` either way |
| S3C-02 | MATERIAL | measure the collapse rate from the first anchor cell; raise `B_tracking` if needed |
| S3C-03 | MATERIAL | manuscript labelling discipline |
| S3C-04 | MINOR | log the pair-drop rule before first use |
| S3C-05 | MINOR | naming discipline |
| S3C-06 | MINOR | add the emitter assertion |

**None is blocking.** Two are material and both have a defined trigger and a
defined response. The plan is not amended for any of them.

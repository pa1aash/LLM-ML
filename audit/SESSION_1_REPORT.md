# SESSION 1 REPORT — S0 ground truth

---

## 1. Repository shape

The repository holds 48 tracked-or-present files: twelve Python modules, three
shell orchestrators, a ten-page LaTeX manuscript with 47 references and eleven
figures, four planning documents, and two zip snapshots. All six experimental
conditions (A, A2, B, C, D, E) are implemented in a single runner,
[src/run_v2.py](../src/run_v2.py), which calls
[src/search_space.py](../src/search_space.py) to build architectures and
[src/train_arch.py](../src/train_arch.py) to train them, and reaches the language
model over HTTP against a local server that no script ever starts. Every figure
and every table in the paper is produced by
[src/deep_analysis_v2.py](../src/deep_analysis_v2.py), which reads a results
directory. **That results directory does not exist.** Nothing in the repository
pins a dependency, records a model identity, or stores a single experimental
observation.

## 2. Data census verdict

**RAW, SPEC and TRANSCRIPT data are present in 0 of the 24
condition × dataset × seed cells.**

There is no `results/`, no `results_v2/`, no `results.json`, no `metadata.json`,
no architecture specification and no LLM transcript — not in the working tree,
and not inside either archive zip (both contain only `.tex`, `.bib`, `.sty`,
`.bst` and figure PDFs).

What survives is SUMMARY and DERIVED only:

| Cell group | Surviving evidence |
|---|---|
| 6 conditions × CIFAR-10 × seed 42 | full — accuracy, architecture, pairwise stats, rank, transcript tables |
| 6 conditions × CIFAR-100 × seed 42 | partial — accuracy and pairwise stats only |
| all 12 cells × seed 137 | **nothing** |

Five generated `paper/figures/tab_*.tex` files plus the annotated cells of
`fig4_design_heatmap.pdf` are the entire numeric evidence base.

## 3. Claim trace verdict

47 numeric claims traced: **3 REPRODUCIBLE (6%), 30 PRESENT (64%),
14 ORPHAN (30%)**.

Restricting to the headline surface — the abstract plus Tables 1, 2 and 3 —
**34 claims, of which 9 are ORPHAN: 26%.**

The three REPRODUCIBLE items are arithmetic ratios between two artifact values
(32-fold, 39×, 8.5×). **No inferential statistic in the paper is reproducible.**
The orphans include the generating model, the hardware, all six seed-137
replication figures, and — most seriously — **`parameter std = 0K`**, which is
quoted in the abstract, Results, Discussion and Conclusion, and **the Bonferroni
threshold α = 0.0071** against which every significance decision is declared.

## 4. Forensic answers

**F1 — Generation config.** Thinking was suppressed by configuration
(`enable_thinking=False`, [llm_server_small.py:43](../src/llm_server_small.py#L43)),
transcripts were truncated to 2000 characters, and `finish_reason` is hardcoded
to `"stop"` — so the "zero causal attributions" result is a property of the
harness, not a measured property of the model.

**F2 — Identical designs.** Undeterminable directly (specs absent), but Jaccard
0.022 ≠ 0 mathematically refutes strict identity; recovered Figure 4 values
(skip 50/50) plus `param std = 0K` imply the 20 designs share one template and
one parameter count while differing in the *ordering* of block choices.

**F3 — Independence.** Condition B uses genuinely fresh contexts but has no RNG
control at all; conditions C and D condition proposal *i+1* on outcomes 1…*i*,
yet Welch's *t*, Mann–Whitney *U* and the bootstrap all treat n=20 as
independent — and those are exactly the comparisons carrying the thesis.

**F4 — Selection hygiene.** The feedback loop is clean (validation-only, as
claimed), but top-5 retraining selects on **test** accuracy
([run_v2.py:340](../src/run_v2.py#L340)) and the convergence figure plots
best-so-far **test** accuracy; the train/val split also moves per architecture
rather than being fixed.

**F5 — Effect sizes.** Cohen's *d* uses a pooled (equal-variance) SD on a
comparison with a 1000:1 variance ratio while the *t*-test assumes unequal
variances; Mann–Whitney is already computed and reported, but Cliff's δ / A₁₂ —
though exact functions of *U* — are **not recoverable**, because `u_stat` was
never persisted.

## 5. Bibliography verdict

**Of 47 entries: 2 FABRICATED, 3 WRONG-METADATA, 0 STALE, 1 UNRESOLVED,
41 clean.** Resolution rate 46/47 (97.9%) against fetched OpenAlex / Semantic
Scholar / arXiv records.

**5 of 47 entries (10.6%) misattribute authorship.** `li2025gptnas` has **zero**
overlap with the real author list — all six named authors are wrong.
`kamoi2024llmselfcorrect` has one real author of five. Both entries flagged in
the session brief (`white2023nas`, `li2025gptnas`) were caught independently by
the pipeline, confirming it works. This is a **submission blocker**.

## 6. Internal inconsistencies

1. Prose claims 20 "identical" designs / "zero structural variance" while citing Jaccard 0.022 in the same sentence — identical vectors give exactly 0.000.
2. Same paragraph self-contradicts: "the same skip-connection configuration" vs "skip connections split evenly between projection (50%) and identity (50%)" twenty lines later.
3. Bonferroni threshold: paper declares α = 0.05/7 = 0.0071; the code applies α = 0.05/15 = 0.00333. Every star in Table 3 was computed at the code's threshold and reported against the paper's.
4. B vs C at p_t = .007 is called "marginal"; under the paper's own stated α = .0071 it would be significant. The exact p is **unrecoverable** (artifact rounds to 3 dp; source data gone).
5. **Condition D holds the best single architecture on both datasets** (91.4 CIFAR-10, 66.9 CIFAR-100) while the headline is that structured feedback hurts. Best-of-*k* is never discussed.
6. "Evaluates it on the test set only once" contradicts Algorithm 1 line 7 and the code, which evaluate test for all 20.
7. Algorithm 1 shows one split before the loop; the code re-splits per architecture via `seed+i`.
8. Table 5 caption says "epoch 20 vs final **test** accuracy (epoch 50)"; the code correlates epoch-20 validation against *best* validation.
9. Table 5 is self-correlated — `best_val_acc` is a max over all 50 epochs and includes epoch 20, inflating ρ.
10. Bootstrap resamples: paper says 10 000, code uses 5 000.
11. Condition D conv-type share: text says 99%/1%, Figure 4 shows 100%/0%.
12. Welch (unequal variance) paired with pooled-SD Cohen's *d* (equal variance) on the same comparison.
13. Seven comparisons called "pre-specified"; the script computes all 15 exhaustively and no pre-registration artifact exists.
14. Model identity three ways: paper Qwen3-1.7B-4bit, code `Qwen/Qwen3-8B`, `docs/methodology.md:77` a hosted third-party API.
15. Hardware: abstract A100-40GB vs `docs/` GH200 480GB.
16. Page budget: `main.tex:12` targets 8 pages, README targeted 4, the PDF is 10.
17. **`sanitize_config` collapses malformed LLM output to `standard_3x3 / relu / batchnorm`** — precisely the reported "narrow prior" — and runs on the LLM arms only, never the random arms.
18. Reasoning suppression and 2000-character transcript truncation are undisclosed; Limitation (iv) attributes the null to model size instead.
19. All six seed-137 replication numbers are ORPHAN.

## 7. Open actions requiring operator input

Full list of 35 in [audit/OPEN_ACTIONS.md](OPEN_ACTIONS.md). Those needing a
decision only the operator can make:

1. **OA-1 — Does the raw experimental data still exist anywhere?** On the GPU host, in a backup, on the Windows machine that produced `logs/main.log`? **This is the highest-value question in the project**: its answer decides whether S2 is claim surgery or a rebuild.
2. **OA-2** — Authorise replacing `paper/references.bib` with the verified file.
3. **OA-3** — Which model actually generated the proposals? No artifact can settle it.
4. **OA-4** — `parameter std = 0K` has no evidentiary basis: recover it or remove it.
5. **OA-28** — `logs/main.log` is a failed build from an unrelated host; delete?
6. **OA-32** — Disable "Block command line pushes that expose my email" so the two commits can reach GitHub.
7. **OA-33** — hyperresearch v0.8.5 has no `premier` gear; upgrade, or accept default breadth.
8. **OA-35** — Confirm the disposition of the agent-tooling files `hyperresearch install` created, whose filenames the authorship contract forbids (excluded via `.git/info/exclude`).

## 8. G0 recommendation — **PASS** (unsigned)

The G0 criterion is a **characterisation** criterion: *"The paper's evidence base
is characterised — every headline number classified REPRODUCIBLE / PRESENT /
ORPHAN, the five forensic questions answered or explicitly marked
undeterminable, and the reference list verified against fetched records."*

All three requirements are met. Every headline number is classified with an
evidence path. All five forensic questions are answered from code, and the one
that could not be answered directly (F2) is explicitly marked undeterminable with
its reason stated and a bounded reconstruction supplied. The reference list was
resolved 46/47 against fetched records, with the two known-bad entries caught
independently as a self-test.

**Recommend PASS.** The gate asks whether we now know what the evidence base is —
and we do, in detail.

That said, the operator should sign with full sight of what the characterisation
found: **the evidence base is largely absent.** A quarter of the headline claims
have no basis in the repository, no inferential statistic can be recomputed, the
central "narrow prior" finding has an unexcluded instrumental explanation in
`sanitize_config`, the condition the paper says is harmed by feedback produces
the best architecture on both datasets, and one in ten references misattributes
authorship. Passing G0 records that we have mapped the ground truth; it does not
imply the ground is solid. S1 and S2 inherit five blocking actions, of which
OA-1 governs everything downstream.

**Operator signature:** ______________________  **Date:** ____________

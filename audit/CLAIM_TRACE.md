# CLAIM TRACE — every asserted number vs. the repository

S0 ground-truth audit. The repository is truth; the PDF is a claim about it.

**Status definitions**

- **REPRODUCIBLE** — a repo script recomputes the value from repo data, or it is
  exact arithmetic on values that are themselves in a repo artifact.
- **PRESENT** — the value exists in a stored artifact, but nothing in the repo
  derives it from raw data.
- **ORPHAN** — no artifact in the repo contains or produces this number.

**The controlling fact:** there is no `results/` or `results_v2/` directory, no
`results.json`, no architecture specs, and no transcripts — anywhere in the tree
or in either archive zip. Every analysis entry point
(`load_all(results_dir)`, [deep_analysis_v2.py:47](../src/deep_analysis_v2.py#L47))
reads a directory that does not exist. **No statistic in this paper can be
recomputed from repository data.** Nothing was run; there was nothing to run it on.

Surviving numeric artifacts, in full:

| Artifact | Holds |
|---|---|
| `paper/figures/tab_main.tex` | mean/std/median/best × 6 conditions × 2 datasets |
| `paper/figures/tab_stats.tex` | 15 pairwise comparisons × 2 datasets (p_t, p_U, d, CI) |
| `paper/figures/tab_arch.tex` | params, blocks, gap, efficiency, diversity, time (CIFAR-10) |
| `paper/figures/tab_rank.tex` | Spearman ρ, Kendall τ, p × 6 conditions |
| `paper/figures/tab_transcript.tex` | transcript counts × 3 LLM conditions |
| `paper/figures/fig4_design_heatmap.pdf` | design-choice percentages (annotated cells, text-extractable) |

---

## 1. Abstract

| Claim | Location | Status | Evidence | Notes |
|---|---|---|---|---|
| Six strategies, CIFAR-10/100 | L44–47 | PRESENT | `tab_main.tex` (6 rows × 2 datasets) | |
| Qwen3-1.7B | L45 | **ORPHAN** | — | No artifact records the model. `run_v2.py:32` hardcodes `Qwen/Qwen3-8B`; servers ignore the requested name. See FORENSICS F1. |
| 20 architectures per condition | L46 | PRESENT | `tab_rank.tex` n=20; `tab_transcript.tex` 20 | |
| 50 training epochs | L46 | PRESENT | `train_arch.py:56` default `epochs=50` | Config, not measurement |
| NVIDIA A100-40GB | L47 | **ORPHAN** | — | Contradicts `docs/` (GH200 480GB). `metadata.json` would have held `device`; absent. |
| 89.0 ± 0.7 (B, CIFAR-10) | L49 | PRESENT | `tab_main.tex` | |
| 77.3 ± 22.6 (A, CIFAR-10) | L49 | PRESENT | `tab_main.tex` | |
| Mann–Whitney p < 0.001 (A vs B) | L50 | PRESENT | `tab_stats.tex` `0.000*` | |
| Cohen's d = −0.71 (A vs B) | L50 | PRESENT | `tab_stats.tex` | Pooled-SD d across σ 22.6 vs 0.7 — see FORENSICS F5 |
| **All 20 designs identical** | L51–53 | **ORPHAN — and contradicted** | — | Specs absent. Refuted by the paper's own Jaccard 0.022 ≠ 0. See §5.1 |
| standard 3×3 / ReLU / BatchNorm | L52–53 | PRESENT | `fig4_design_heatmap.pdf`: 100/100/100 | Identical to `sanitize_config` defaults — see FORENSICS F2 |
| **parameter std = 0 K** | L53 | **ORPHAN** | — | No code computes param std (`grep` over `src/`: zero hits). `tab_arch.tex` stores the mean only. |
| d = +1.25, p_t < 0.001, p_U = 0.002 (B vs D) | L57–58 | PRESENT | `tab_stats.tex` `0.001*`, `0.002*`, `+1.25 [+0.54,+2.71]` | |
| Bonferroni α = 0.0071 | L58–59 | **ORPHAN — and contradicted** | — | Code computes α = 0.05/15 = 0.00333. See §5.2 |
| Jaccard 0.022 → 0.268 | L60 | PRESENT | `tab_arch.tex` | |
| CIFAR-100 all LLM comparable, p = 0.61 | L61 | PRESENT | `tab_stats.tex` B vs C CIFAR-100 `0.606` | |

---

## 2. Table 1 (CIFAR-10) and Table 2 (CIFAR-100)

Accuracy columns of both tables are transcribed from `tab_main.tex` and match
exactly.

| Claim | Status | Evidence |
|---|---|---|
| All Mean/Std/Med/Best, CIFAR-10, 6 conditions | PRESENT | `tab_main.tex` |
| All Mean/Std, CIFAR-100, 6 conditions | PRESENT | `tab_main.tex` |
| Par. (K) means: 508 / 778 / 511 / 574 / 727 / 625 | PRESENT | `tab_arch.tex` Params column |
| **Par. (K) std: 460 / 612 / 0 / 191 / 302 / 375** | **ORPHAN** | No artifact holds these; no code computes parameter std |

Table 1's parameter standard deviations are a headline result (the "0" for
condition B is quoted in the abstract, in §5.2 of the paper, and in the
conclusion) and **no artifact in the repository contains them.**

---

## 3. Table 3 — statistical comparisons

Table 3 is a **hand-selected 7-row subset** of the 15 comparisons in
`tab_stats.tex`. All seven values transcribe correctly:

| Comparison | Paper | `tab_stats.tex` | Status |
|---|---|---|---|
| A vs B (C10) | .037 / <.001* / −0.71 | 0.037 / 0.000* / −0.71 | PRESENT |
| A2 vs B (C10) | .008 / <.001* / −0.94 | 0.008 / 0.000* / −0.94 | PRESENT |
| B vs C (C10) | .007 / .042 / +0.93 | 0.007 / 0.042 / +0.93 | PRESENT |
| B vs D (C10) | <.001* / .002* / +1.25 | 0.001* / 0.002* / +1.25 | PRESENT |
| A vs E (C10) | .40 / .066 / −0.27 | 0.400 / 0.066 / −0.27 | PRESENT |
| A vs B (C100) | <.001* / <.001* / −1.53 | 0.000* / 0.000* / −1.53 | PRESENT |
| B vs C (C100) | .606 / .787 / −0.16 | 0.606 / 0.787 / −0.16 | PRESENT |

The **significance stars are inherited from a table computed under a different
threshold** — see §5.2. The claim that these seven were *pre-specified*
([main.tex:302](../paper/main.tex#L302)) is unsupported: the analysis script
computes all 15 pairs exhaustively
([deep_analysis_v2.py:394](../src/deep_analysis_v2.py#L394)) and there is no
pre-registration artifact in the repository.

---

## 4. Tables 4–5, figures, and in-text statistics

| Claim | Location | Status | Evidence |
|---|---|---|---|
| Table 4 all columns (params, blocks, gap, eff., div., time) | L530–537 | PRESENT | `tab_arch.tex`, exact match |
| Table 5 Spearman ρ, all 6 | L626–632 | PRESENT | `tab_rank.tex`, exact match |
| Table 5 p-values | L626–632 | PRESENT | `tab_rank.tex` |
| Transcript: 0 causal, 0%, n=20 ×3 | L667–670 | PRESENT | `tab_transcript.tex` |
| "32-fold reduction in std" | L488 | **REPRODUCIBLE** | 22.6 / 0.7 = 32.3, both in `tab_main.tex` |
| "39 times lower diversity" | L546 | **REPRODUCIBLE** | 0.856 / 0.022 = 38.9, both in `tab_arch.tex` |
| "8.5-fold over zero-shot" | L601 | **REPRODUCIBLE** | 0.187 / 0.022 = 8.5, both in `tab_arch.tex` |
| Random conv/activation percentages | L574–578 | PRESENT | `fig4_design_heatmap.pdf` — matches exactly |
| REA conv/activation percentages | L579–581 | PRESENT | `fig4_design_heatmap.pdf` — matches exactly |
| B: 100% std 3×3, 100% ReLU, 50/50 skip | L560–566 | PRESENT | `fig4_design_heatmap.pdf` — matches exactly |
| C: 100% std 3×3, 100% ReLU, 75/25 skip | L568–570 | PRESENT | `fig4_design_heatmap.pdf` — matches exactly |
| **D: "99% standard 3×3 with 1% other types"** | L571–572 | **PRESENT — and contradicted** | `fig4_design_heatmap.pdf` shows **100 / 0 / 0 / 0** for D |
| D: 94% ReLU, 6% GELU, 100% BatchNorm | L572–573 | PRESENT | `fig4_design_heatmap.pdf` — matches exactly |
| Gen. gap 6.0–6.8% vs 4.2% | L660–663 | PRESENT | `tab_arch.tex` Gap column |
| "all between 87.8% and 89.8%" (B range) | L641 | **ORPHAN** (lower bound) | `tab_main.tex` holds Best = 89.8; the minimum 87.8 is in no artifact |
| **Seed-137: B 88.2±1.5** | L681 | **ORPHAN** | No seed-137 value exists in any artifact |
| **Seed-137: C 88.3±1.3** | L682 | **ORPHAN** | " |
| **Seed-137: A 69.3±30.1** | L683 | **ORPHAN** | " |
| **Seed-137: B CIFAR-100 61.1±2.5** | L684 | **ORPHAN** | " |
| **Pooled n=40: B 88.6±1.2** | L685–686 | **ORPHAN** | " |
| **Pooled n=40: C 87.9±1.7** | L686 | **ORPHAN** | " |

`get_accs` defaults to `seed="s42"`
([deep_analysis_v2.py:66](../src/deep_analysis_v2.py#L66)) and every generated
table is seed-42 only. The entire replication subsection — the paper's answer to
"does this hold across seeds" — rests on **six orphan numbers**.

---

## 5. Internal inconsistencies

### 5.1 "Identical designs" vs Jaccard 0.022 — the text is wrong, the tables are consistent

`mean_jaccard_distance` returns `1 − |∩|/|∪|` over per-block signature sets
([deep_analysis_v2.py:120](../src/deep_analysis_v2.py#L120)). **Identical
configurations give identical sets, hence distance exactly 0.000.** A reported
0.022 is therefore incompatible with 20 identical designs.

The paper asserts identity in four places:

- Abstract L51: "all 20 zero-shot designs share *identical* design choices"
- L543–546: "The parameter standard deviation is 0K: every architecture uses the
  same number of blocks, the same convolution types, the same activation, the
  same normalisation, and the same skip-connection configuration."
- L701–703: "The **zero structural variance** of condition B (parameter
  std = 0K, Jaccard distance 0.022)" — both numbers in one sentence, as if
  compatible.
- L774: "producing 20 structurally identical designs"

And contradicts itself 20 lines later:

- L565–566: "with skip connections split evenly between projection (50%) and
  identity (50%)"

**Determination.** From the recovered Figure 4 values (B: skip 50% identity /
50% projection) plus `parameter std = 0K`, the split must be *within* each
architecture, and the residual Jaccard must come from the *ordering* of choices
across blocks — the signature is indexed by block position
([deep_analysis_v2.py:115](../src/deep_analysis_v2.py#L115)) while the parameter
count is order-invariant. See FORENSICS F2 for the full derivation.

So: **Tables 1 and 4 and Figure 4 are mutually consistent. The prose claim of
identity is false** — the designs share one template and one parameter count but
are not identical. The magnitude 0.022 implies roughly 3 of 20 deviate.

This cannot be confirmed directly: the condition-B specs are not in the
repository.

### 5.2 p_t = .007 against α_corr = 0.0071 — the threshold in the paper is not the threshold in the code

The paper pre-specifies seven comparisons and
α_corr = 0.05/7 = 0.0071 ([main.tex:302–312](../paper/main.tex#L302)), stating
"We report a result as significant only when p < α_corr = 0.0071 and mark such
results with *".

The code marks significance with
`alpha_corr = 0.05/n_comp` where `n_comp = len(pairs)` over **all** active
pairs ([deep_analysis_v2.py:406–415](../src/deep_analysis_v2.py#L406)). With six
active conditions that is C(6,2) = 15, so **α_corr = 0.05/15 = 0.00333** — not
0.0071.

Every star in Table 3 was therefore computed at 0.00333 and then reported under a
stated threshold of 0.0071. The two disagree on exactly one cell, and it is the
load-bearing one:

| | α = 0.00333 (code) | α = 0.0071 (paper's stated rule) |
|---|---|---|
| B vs D, p_t = .001 | significant * | significant * |
| **B vs C, p_t = .007** | **not significant** | **significant, if the true value is < .0071** |

**Can the exact p be recovered? No.** `latex_table_stats` formats with
`{comp['t_p']:.3f}` ([deep_analysis_v2.py:416](../src/deep_analysis_v2.py#L416)),
so the artifact preserves only `p_t ∈ [0.0065, 0.0075)`. The unrounded value lived
in `results.json`, which does not exist. The absence of a star in
`tab_stats.tex` establishes only `p_t ≥ 0.00333`.

**Determination.** The paper's characterisation — "p_t approximately equals
α_corr" and therefore "marginal" ([main.tex:483–489](../paper/main.tex#L483)) —
is *not* supportable as written. Under the threshold the paper itself declares,
p = .007 < .0071 is significant, and the paper would have to report that both
feedback conditions significantly underperform zero-shot. Under the threshold the
code actually applied, .007 is comfortably non-significant and "marginal" is an
overstatement in the other direction. The honest statement is that the comparison
sits inside the rounding interval of its own decision threshold and cannot be
resolved from the surviving evidence.

### 5.3 Condition D holds the best single architecture — CONFIRMED, on both datasets

From `tab_main.tex`:

| Condition | CIFAR-10 Best | CIFAR-100 Best |
|---|---|---|
| A Random | 90.3 | 65.0 |
| A2 Filtered | 90.3 | 65.0 |
| B Zero-Shot | 89.8 | 66.2 |
| C Unstr. FB | 90.2 | 65.1 |
| **D Struct. FB** | **91.4** | **66.9** |
| E REA | 90.6 | 65.0 |

**Condition D produces the single best architecture of any condition on both
datasets** — the condition the paper's headline says is harmed by feedback.

This is not a minor tension. Under a fixed budget of *k* = 20 proposals, a search
method is normally judged by expected-best-of-*k*, since the practitioner keeps
the best architecture and discards the rest — which is exactly what the paper's
own Algorithm 1 does (`α* ← argmax v_i`, [main.tex:344](../paper/main.tex#L344)).
On that estimand D wins outright and the "feedback hurts" conclusion inverts. The
paper reports mean-of-population instead and never reconciles the two, nor
reports a best-of-*k* comparison. The word "Best" appears in Table 1 and is not
discussed anywhere in the Results or Discussion.

The paper does note REA's best (90.6) is "competitive with all LLM conditions"
([main.tex:500](../paper/main.tex#L500)) — but 90.6 also exceeds B's 89.8, which
goes unremarked.

### 5.4 Further inconsistencies found

| # | Inconsistency | Evidence |
|---|---|---|
| 1 | **Algorithm 1 vs code — test-set usage.** "evaluates it on the test set only once" ([main.tex:334](../paper/main.tex#L334)) but Algorithm 1 line 7 evaluates `t_i` every iteration, and `train_arch.py:137-150` evaluates test for all 20. The prose contradicts the algorithm *and* the code. | [main.tex:334](../paper/main.tex#L334) vs [train_arch.py:150](../src/train_arch.py#L150) |
| 2 | **Algorithm 1 vs code — the split.** Algorithm 1 splits once before the loop; the code re-splits per architecture via `seed+i`. | [main.tex:329](../paper/main.tex#L329) vs [train_arch.py:43](../src/train_arch.py#L43) |
| 3 | **Table 5 caption vs code.** Caption and body say "epoch 20 vs final **test** accuracy (epoch 50)"; the code correlates epoch-20 val against `best_val_acc` — validation, and *best*, not final. | [main.tex:620](../paper/main.tex#L620) vs [deep_analysis_v2.py:181](../src/deep_analysis_v2.py#L181) |
| 4 | **Table 5 is self-correlated.** `best_val_acc` is the max over all 50 epochs, which *includes* epoch 20 — so the two correlated quantities share a term, inflating ρ. | [deep_analysis_v2.py:182](../src/deep_analysis_v2.py#L182) |
| 5 | **Bootstrap resamples.** Paper says 10 000 for Cohen's d CIs; code uses 5 000. | [main.tex:311](../paper/main.tex#L311) vs [deep_analysis_v2.py:80](../src/deep_analysis_v2.py#L80) |
| 6 | **D conv-type share.** Text says 99% standard 3×3 with 1% other; Figure 4 shows 100/0/0/0. | [main.tex:571](../paper/main.tex#L571) vs `fig4_design_heatmap.pdf` |
| 7 | **Welch + pooled-d mismatch.** Welch assumes unequal variances; Cohen's d uses a pooled (equal-variance) SD, on a comparison with a 1000:1 variance ratio. | [deep_analysis_v2.py:83](../src/deep_analysis_v2.py#L83) vs [98](../src/deep_analysis_v2.py#L98) |
| 8 | **"Pre-specified" comparisons.** Claimed for 7 comparisons; the code computes all 15 and no pre-registration artifact exists. | [main.tex:302](../paper/main.tex#L302) vs [deep_analysis_v2.py:394](../src/deep_analysis_v2.py#L394) |
| 9 | **Independence.** n=20 treated as independent units in Welch/Mann–Whitney/bootstrap, but C and D generate proposal *i+1* conditioned on outcomes 1…*i*. | [run_v2.py:219-248](../src/run_v2.py#L219) |
| 10 | **Model identity, three ways.** Paper: Qwen3-1.7B-4bit. Code: `LLM_MODEL = "Qwen/Qwen3-8B"`. `docs/methodology.md`: a hosted third-party commercial LLM API. | [main.tex:290](../paper/main.tex#L290), [run_v2.py:32](../src/run_v2.py#L32), `docs/methodology.md:77` |
| 11 | **Hardware.** Abstract: A100-40GB. `docs/`: GH200 480GB. | [main.tex:47](../paper/main.tex#L47) vs `docs/research-state.md:34` |
| 12 | **Page budget.** `main.tex:12` comment targets 8 pages; README targeted a 4-page venue; the PDF is 10 pages. | [main.tex:12](../paper/main.tex#L12) |
| 13 | **Top-5 retrain selects on test accuracy** inside the "no leakage" v2 fixes. | [run_v2.py:340](../src/run_v2.py#L340) |
| 14 | **Transcript claim vs configuration.** "zero causal attributions" is reported as a model property; reasoning was disabled via `enable_thinking=False` and transcripts truncated to 2000 chars. | [llm_server_small.py:43](../src/llm_server_small.py#L43), [run_v2.py:194](../src/run_v2.py#L194) |
| 15 | **Sanitiser confound.** LLM arms pass through `sanitize_config`, which collapses unknown values to `standard_3x3 / relu / batchnorm`; random arms do not. That is the reported template. | [run_v2.py:52-67](../src/run_v2.py#L52) |

---

## 6. Summary counts

Across the 47 distinct numeric claims traced above:

| Status | Count | Share |
|---|---|---|
| REPRODUCIBLE | 3 | 6% |
| PRESENT | 30 | 64% |
| ORPHAN | 14 | 30% |

The three REPRODUCIBLE items are arithmetic ratios between two artifact values
(32-fold, 39×, 8.5×). **No inferential statistic in the paper is reproducible**,
because no analysis script can run: every one of them reads a results directory
that does not exist.

### Headline claims — abstract plus Tables 1, 2 and 3

Counting the distinct numeric assertions in the abstract and in Tables 1–3
(the paper's headline surface): **34 claims, of which 9 are ORPHAN — 26%.**

The orphans are not peripheral. They are:

1. the generating model (Qwen3-1.7B),
2. the hardware (A100-40GB),
3. **parameter std = 0 K** — quoted in the abstract, Results, Discussion and Conclusion,
4. the identity claim about all 20 designs,
5. **the Bonferroni threshold α = 0.0071** that every significance decision is stated against,
6. Table 1's six parameter-std values.

So roughly a quarter of the headline numbers have no evidentiary basis in the
repository, and they include the paper's single most-quoted result
(`parameter std = 0K`) and the decision threshold underpinning its statistical
claims.

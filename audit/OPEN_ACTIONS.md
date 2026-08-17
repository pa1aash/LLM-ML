# OPEN ACTIONS

Every unresolved item from Blocks 2–5, numbered. Items marked **[OPERATOR]**
require a decision or an action only the operator can take.

---

## Blocking — must resolve before any submission

**OA-1. The experimental data does not exist in this repository.** [OPERATOR]
No `results/`, `results_v2/`, `results.json`, `metadata.json`, architecture specs
or transcripts, in the tree or in either archive zip. Every analysis entry point
reads a directory that is absent, so no statistic in the paper can be recomputed.
*Question: does the raw data still exist on the GPU host, in a backup, or on the
Windows machine that produced `logs/main.log`? If it is recoverable, most of this
audit's ORPHAN findings collapse to PRESENT or REPRODUCIBLE. If it is not, the
paper cannot be defended against a reviewer request for artifacts.*
This is the single highest-value question in the audit.

**OA-2. Bibliography misattributes authorship in 5 of 47 entries.** [OPERATOR]
2 FABRICATED, 3 WRONG-METADATA. `li2025gptnas` has zero correct authors. See
`BIB_AUDIT.md`. Replace `paper/references.bib` with
`audit/references_verified.bib` after review.

**OA-3. Which model actually generated the proposals?** [OPERATOR]
Three-way conflict: the paper says Qwen3-1.7B-4bit
([main.tex:290](../paper/main.tex#L290)); `run_v2.py:32` hardcodes
`Qwen/Qwen3-8B`; and `docs/methodology.md:77` names a hosted third-party
commercial LLM API instead (read that line directly — the file is on disk but
gitignored). The servers ignore the requested model name and `metadata.json`
never recorded it, so no artifact can settle this. Only the operator knows which
server was running.

**OA-4. `parameter std = 0K` has no evidentiary basis.** [OPERATOR]
It is quoted in the abstract, Results, Discussion and Conclusion. No artifact
contains it and no code in `src/` computes a parameter standard deviation.
Either recover the specs (OA-1) or remove the claim.

**OA-5. The Bonferroni threshold in the paper is not the one applied.**
Paper states α = 0.05/7 = 0.0071; `deep_analysis_v2.py:413` applies α = 0.05/15
= 0.00333. Every significance star in Table 3 was computed at 0.00333 and
reported against 0.0071. Decide which correction is intended and regenerate.

*Disposition, S2 2026-08-17:* not recoverable for the original run — its numbers
are abandoned wholesale (`EXPERIMENT_PLAN_R2.md` §1.3) — and **fixed prospectively**:
FAMILY_SIZE = 16, ALPHA = 0.05/16 = **0.003125**, read from one module-level
constant, with the emitter asserting that the confirmatory-test count is exactly
16 and that every `alpha_applied` equals the top-level `alpha`, aborting
otherwise (§5.2). The defect cannot recur silently.

---

## Determinations that require data to close

**OA-6. Exact p-value for B vs C (CIFAR-10) is unrecoverable.**
`tab_stats.tex` rounds to 3 dp, bounding it to `p_t ∈ [0.0065, 0.0075)`. Whether
it falls below the paper's stated α = 0.0071 decides between "feedback
significantly hurts" and "marginal". Needs `results.json`.

**OA-7. Whether the 20 condition-B designs are identical cannot be verified.**
Jaccard 0.022 ≠ 0 refutes strict identity; the recovered Figure 4 values plus
`param std = 0K` imply the designs differ in the *ordering* of block choices
(see `FORENSICS.md` F2). Needs the specs to confirm.

**OA-8. The sanitiser confound cannot be ruled out.**
`sanitize_config` ([run_v2.py:52-67](../src/run_v2.py#L52)) collapses any
out-of-vocabulary field to `standard_3x3 / relu / batchnorm` — precisely the
"narrow prior" template the paper reports — and runs on the LLM arms only, never
the random arms. Distinguishing a genuine model prior from sanitiser output
requires re-running condition B with raw pre-sanitisation generations logged.

**OA-9. Cliff's δ / A₁₂ are not computable from what survives.**
Both are exact functions of the Mann–Whitney `U` statistic, which
`full_comparison` computes ([deep_analysis_v2.py:99](../src/deep_analysis_v2.py#L99))
but which is **never persisted** — `tab_stats.tex` stores only `u_p`. Given the
1000:1 variance ratio, a rank-based effect size should be the headline rather
than pooled Cohen's *d*. Needs re-running the analysis on recovered data.

---

## Methodological defects to fix in code before any re-run

**OA-10. Rank-stability correlation is self-correlated and mislabelled.**
`rank_correlation_from_histories` correlates `val_acc[19]` against
`best_val_acc`, which is the max over all 50 epochs and therefore *includes*
epoch 20 ([deep_analysis_v2.py:181-182](../src/deep_analysis_v2.py#L181)). Table 5's
caption also says "final **test** accuracy (epoch 50)", which is neither
validation nor final. Both the statistic and its label need correcting.

**OA-11. Top-5 retraining selects on test accuracy.**
`valid.sort(key=lambda x: x["test_acc"])` ([run_v2.py:340](../src/run_v2.py#L340))
inside the v2 "no leakage" fixes. Should select on `best_val_acc`.

**OA-12. Sequential dependence vs independence-assuming tests.**
Conditions C and D generate proposal *i+1* conditioned on outcomes 1…*i*, yet
Welch, Mann–Whitney and the bootstrap all treat n=20 as independent. This affects
exactly the B-vs-C and B-vs-D comparisons carrying the thesis. Either change the
estimand (expected-best-of-*k*) or the inference (block bootstrap / permutation
over runs, with runs as the unit).

**OA-13. Welch's *t* is paired with a pooled-SD Cohen's *d*.**
Contradictory variance assumptions on the same comparison
([deep_analysis_v2.py:83](../src/deep_analysis_v2.py#L83) vs
[98](../src/deep_analysis_v2.py#L98)). Use Glass's Δ or a rank-based measure.

**OA-14. `bonferroni1936teoria` unresolved.**
Not indexed by OpenAlex, Semantic Scholar or arXiv — expected for a 1936 Italian
monograph. Verify against a library catalogue.

**OA-15. Reasoning suppression is undisclosed.**
`enable_thinking=False` ([llm_server_small.py:43](../src/llm_server_small.py#L43))
and transcripts truncated to 2000 characters
([run_v2.py:194](../src/run_v2.py#L194)). The paper attributes the zero-causal-
attribution result to the model's size (Limitation iv). Either disclose the
configuration or re-run with reasoning enabled and full transcripts stored.

**OA-16. `finish_reason` is hardcoded to `"stop"`.**
[llm_server_small.py:54](../src/llm_server_small.py#L54) — truncated generations
are indistinguishable from complete ones. Fix before re-running.

**OA-17. Train/validation split is not fixed.**
`seed + i` per architecture re-splits train/val for every architecture
([run_v2.py:166](../src/run_v2.py#L166), [train_arch.py:43](../src/train_arch.py#L43)),
contradicting Algorithm 1. It is balanced across conditions, so it is a
precision issue rather than a bias, but the paper describes a single split.

---

## Reporting inconsistencies to correct in the manuscript

**OA-18.** Prose claims 20 "identical" designs / "zero structural variance" while
citing Jaccard 0.022 in the same sentence ([main.tex:701](../paper/main.tex#L701)).
Self-contradicts L565's "skip connections split evenly 50/50".

**OA-19.** Condition D holds the **best single architecture on both datasets**
(91.4 CIFAR-10, 66.9 CIFAR-100) while the headline says structured feedback
hurts. Best-of-*k* is the standard estimand for a fixed search budget and is
never discussed. Must be addressed head-on, not omitted.

**OA-20.** "Evaluates it on the test set only once"
([main.tex:334](../paper/main.tex#L334)) contradicts Algorithm 1 line 7 and the
code, which evaluate test for all 20 architectures.

**OA-21.** Bootstrap resamples: paper says 10 000, code uses 5 000.

**OA-22.** Condition D conv-type share: text says 99%/1%, Figure 4 shows 100%/0%.

**OA-23.** Seven comparisons described as "pre-specified"; the script computes
all 15 exhaustively and no pre-registration artifact exists.

**OA-24.** All six seed-137 replication numbers are ORPHAN. The replication
subsection has no evidentiary basis in the repository.

**OA-25.** Hardware conflict: abstract says A100-40GB, `docs/` say GH200 480GB.

**OA-26. CLOSED, S2 2026-08-17.** Page budget: `main.tex:12` targets 8 pages,
README targeted a 4-page venue, the PDF is 10 pages. **Reconciled: 8 pages
excluding references**, per the selected venue (AI for Meta-Science, position
track). See `VENUE.md`. The built PDF is 2 pages over and must be cut, not
respaced.

---

## Repository hygiene

**OA-27. `.gitignore` excludes `paper/main.bbl`.** arXiv and most camera-ready
pipelines require the `.bbl`. Not changed during this audit (append-only scope).

**OA-28. `.gitignore` excludes `*.log`**, so `logs/main.log` is untracked. That
file is a *failed* MiKTeX build from an unrelated Windows host
(`C:/Users/nitua/...`) and is arguably deletable; it is not this paper's build
log. [OPERATOR]

**OA-29. `archive/resv2.zip` is redundant** — its `main.tex` and
`references.bib` are byte-identical (SHA-256) to the live `paper/` copies.

**OA-30. Unreferenced figures.** `figure1_accuracy_boxplots.pdf`,
`figure2_convergence.pdf`, `figure3_invalid_rates.pdf`,
`fig5_training_dynamics.pdf` are present but not included by `main.tex`.

**OA-31. No dependency pinning of any kind.** No `requirements.txt`, lockfile,
`environment.yml`, or `pyproject.toml`. Python, torch, transformers and CUDA
versions are unrecorded. A reproducibility-conscious reviewer will ask.

**OA-32. CLOSED.** GitHub push was blocked by `GH007: your push would publish a
private email address`. The operator disabled the protection at
github.com/settings/emails; `origin/main` is current and tracks local `main`
with correct authorship. Verified S2, 2026-08-17.

**OA-33. hyperresearch v0.8.5 has no `premier` gear and no `profile` command.**
The S0 session contract specifies `hyperresearch profile use premier` (100–130
sources, doubled depth budget). v0.8.5 exposes no `profile` or `gear` subcommand
at all — `hyperresearch profile list` errors with `No such command 'profile'`.
**UNRESOLVED — the requested gear could not be selected or confirmed.** The
positioning run therefore executes at the CLI's default breadth. Either upgrade
hyperresearch to a version exposing gears, or accept default breadth and record
that the source count is not the contracted 100–130.

**OA-34. `[scholar] contact_email` cannot be set through the CLI in v0.8.5.**
Configuration is stored in `.hyperresearch/hyperresearch.db` (sqlite), and the
valid config keys are only `vault.*`, `web.*`, `search.*`, `sync.*`, `index.*` —
`config set scholar.contact_email` is rejected as an unknown key.
`.hyperresearch/config.toml` was written by hand carrying the address, but
**it is not known to be read by v0.8.5**, so Unpaywall may still be skipped
rather than enabled. Verify against the installed version's source before relying
on open-access resolution.

**OA-35. `hyperresearch install` writes filenames the authorship contract
forbids.** [OPERATOR] It creates an agent-instruction file at the repository root
and an agent-configuration directory beside it, both named after an AI assistant,
plus `.hyperresearch/hook.js`. The contract bars naming an assistant in
filenames.

Disposition taken: all three are excluded through `.git/info/exclude` rather than
`.gitignore`, so the forbidden names never enter committed content at all — a
`.gitignore` entry would itself have to spell them. They remain on disk, and are
regenerable at any time by re-running `hyperresearch install`, so nothing is
lost. Confirm this disposition, and note that re-running `install` recreates
them and that a fresh clone will not exclude them until
`.git/info/exclude` is repopulated.

**OA-37. The C6 thread is unresolved: CoLLM-NAS's noise-accumulation ablation
has five unverified candidate citing papers, and its replication status is
unsettled. Must be resolved before S6 writing.**
*Opened S2, 2026-08-17.* CoLLM-NAS is the source of the "partially scooped"
verdict that governs this paper's novelty position, and its venue status is now
settled — **Oral, CVPR 2026 Workshop on Neural Architecture Search**, verbatim
from the vault's own copy of the paper's Comments field
(`250926037v2-collm-nas-collaborative-large-language-models-for-efficient-knowledg`).
What is **not** settled is whether its Generator-memory / noise-accumulation
ablation (its §4.4 / Figure 6) has been independently cited, replicated, or
challenged. No other note in the vault engages with it; a vault-wide search for
"CoLLM-NAS" returns only the paper's own note and this project's interim reports.

*The exact query that settles it*, run once in S1 before the fetch budget was
exhausted and not followed through:
`GET https://api.semanticscholar.org/graph/v1/paper/arXiv:2509.26037/citations?fields=title,year,venue`
then fetch each citing paper's full text and check for engagement with the
Generator-memory finding specifically, not a related-work mention.

*Five candidate citing papers — UNVERIFIED LEADS, NOT EVIDENCE.* None has been
fetched or read. **None may be cited as corroboration, replication, or challenge
until fetched and read in full.**
- arXiv 2605.04057, "Structured Progressive Knowledge Activation for LLM-Driven
  Neural Architecture Search" (2026) — closest by topic; its abstract describes a
  different LLM-NAS failure mode ("functional entanglement"), so on the abstract
  alone it does not appear to replicate or challenge the noise-accumulation
  finding. Full text not checked.
- arXiv 2605.19247, "Structuring Open-Ended NAS: Semi-Automated Design Knowledge
  Structuring with LLMs for Efficient Neural Architecture Search" (2026) —
  adjacent territory ("inefficient exploration due to biased or low-quality
  design ideas"). Full text not checked.
- arXiv 2606.29582, "Bilevel Optimization for Neural Architecture Search" (2026)
  — appears to cite CoLLM-NAS only as an example method. Not checked.
- "Scaling Closed-Loop Feature Channel Configuration with LLMs" (2026, no arXiv
  ID captured). Not checked.
- "LLM-Driven Transient Stability Assessment: From Automated Simulation to Neural
  Architecture Design" (2025, no arXiv ID captured) — power-systems domain,
  unlikely relevant. Not checked.

*Why it blocks S6 rather than S2.* The pre-registration does not depend on the
answer — `EXPERIMENT_PLAN_R2.md` §7 records the thread as explicitly out of scope,
and E2 is framed as a replication-in-a-new-regime claim (C4) precisely because
CoLLM-NAS's priority is assumed to hold. But the manuscript's novelty paragraph
does depend on it: if an independent paper has already replicated the ablation,
the "scooped" framing hardens; if one has challenged it, the framing must be
reopened. Neither can be asserted from search hits.

**OA-38. Eight of the fifteen obliged citations are absent from
`audit/references_verified.bib`.** *Opened S2, 2026-08-17.* The S0 bibliography
audit verified the manuscript's existing 47 entries; it did not add new ones, and
the S1 corpus post-dates it. Missing: CoLLM-NAS, RZ-NAS, The Format Tax, Let Me
Speak Freely?, Grammar-Aligned Decoding, The Parser Already Knows,
NAS-Bench-Suite-Zero, ZiCo, ZiCo-BC, Lindauer & Hutter. Each has a vault note
with a verified fetch record and an arXiv or PMLR identifier, listed in
`EXPERIMENT_PLAN_R2.md` §6. **They must be added to `references_verified.bib` and
verified against an academic API before S6 writing** — sourced from the fetched
records, never from memory. Rows 8–11 are load-bearing for the novelty
constraint, rows 12–14 are E3's entire evidence base, and row 15 is the only
citable source in the corpus for E2's estimand.

**OA-36. arXiv PDF extraction is broken environment-wide — root-caused.**
`hyperresearch fetch` on any arXiv PDF returns
`JUNK_CONTENT: Binary PDF garbage in content`. **The cause is not pymupdf, not a
redirect, and not a bot wall**: curl returns a valid 625 KB `%PDF-1.5` for the
same URL and pymupdf parses all 17 pages cleanly. The CLI applies a
text-heuristic to the downloaded bytes and discards the payload *before*
invoking the parser.

*Consequence:* every arXiv PDF fetched during the S0 width sweep was silently
reduced to its abstract landing page — 37 of 66 active notes (56%) were
abstract-only, including sources carrying the novelty verdict.

*Disposition:* **routed around in S1, not fixed.** A direct curl + pymupdf
extraction repaired 27 notes (0 failures); ABSTRACT-ONLY fell 37 → 10, and all
10 remaining are genuinely short web pages, not paper abstracts. See
`research/temp/fulltext-repair-log.md` and `audit/HR_STEP_LOG.md`. **The defect
will recur on every future run** until the package is patched or upgraded —
patching an installed third-party package was out of scope. [OPERATOR] Decide
whether to pin a fix, upgrade, or keep the workaround script.

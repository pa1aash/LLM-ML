# CONTEXT PACK — LLM-ML repository

For a collaborator who has read the PDF but never opened the repository.
Written during the S0 ground-truth audit. Machine-readable companion:
`audit/REPO_INVENTORY.json`.

---

## 1. The one thing to know first

**The repository contains no experimental data.**

There is no `results/` directory, no `results_v2/` directory, no `results.json`,
no `metadata.json`, no architecture specifications, and no LLM transcripts —
not in the working tree, and not inside either archive zip. 48 files total:
12 source files, 3 shell scripts, 10 paper files, 11 rendered figures, 5
generated LaTeX tables, 4 planning docs, 2 zip snapshots, 1 stray build log.

Every number in the paper therefore traces back to at most one of five
generated `.tex` table files, or to nothing at all. See `audit/CLAIM_TRACE.md`.

---

## 2. Repository layout

```
src/        12 Python modules — search space, trainer, 2 runners, 2 LLM servers,
            3 analysis scripts
scripts/    3 shell orchestrators (assume src/*.py are co-located; they call
            `python3 -u run_v2.py`, not `python3 -u src/run_v2.py`)
paper/      main.tex (45.8 KB), references.bib (47 entries), icml2025.sty/.bst,
            main.pdf (10 pages), build artifacts, figures/
docs/       4 planning notes. GITIGNORED during this audit — see §7.
archive/    resv1.zip, resv2.zip — paper snapshots only, NO data
logs/       main.log — a FAILED Windows MiKTeX build from an unrelated host
audit/      this audit (new)
```

---

## 3. Code map

### Call graph

```
scripts/run_all_v2.sh ─┬─> run_v2.py --condition {A,A2,B,C,D,E} --seed {42,137}
                       ├─> run_v2.py --temp-ablation
                       ├─> run_v2.py --rank-correlation
                       ├─> run_v2.py --retrain-top5
                       └─> deep_analysis_v2.py --results_dir results_v2
                                                --output_dir figures_v2

run_v2.py ─> search_space.py  (random_architecture_config, build_and_validate,
          │                    config_to_string, SEARCH_SPACE_DESCRIPTION)
          ├─> train_arch.py   (train_architecture)
          └─> HTTP POST http://localhost:8000/v1/chat/completions
                    ^
                    └── served by llm_server.py OR llm_server_small.py
                        (neither is started by any script — see §5)

deep_analysis_v2.py ─> reads results_v2/*/results.json
                    └─> writes figures_v2/{fig1..fig7}.pdf, tab_*.tex
```

### Which file does what

| Role | File | Notes |
|---|---|---|
| Defines the search space | [src/search_space.py](../src/search_space.py) | `SEARCH_SPACE` dict at line 13; ~10^8 configs claimed |
| Trains one architecture | [src/train_arch.py](../src/train_arch.py) | 50 epochs, SGD, cosine LR, bf16 |
| Runs the statistics | [src/deep_analysis_v2.py](../src/deep_analysis_v2.py) | Welch t, Mann–Whitney U, Cohen's d, bootstrap, Jaccard |
| Makes each figure | [src/deep_analysis_v2.py](../src/deep_analysis_v2.py) | `fig1_violin` … `fig7_channels`, lines 194–359 |
| Makes each table | [src/deep_analysis_v2.py](../src/deep_analysis_v2.py) | `latex_table_*`, lines 362–481 |

All six conditions are implemented in a single file,
[src/run_v2.py](../src/run_v2.py):

| Cond | Function | Line |
|---|---|---|
| A (random) | `run_random(filtered=False)` | [158](../src/run_v2.py#L158) |
| A2 (filtered random) | `run_random(filtered=True)` | [158](../src/run_v2.py#L158) |
| B (LLM zero-shot) | `run_llm_zeroshot` | [176](../src/run_v2.py#L176) |
| C (unstructured feedback) | `run_llm_feedback(structured=False)` | [202](../src/run_v2.py#L202) |
| D (structured feedback) | `run_llm_feedback(structured=True)` | [202](../src/run_v2.py#L202) |
| E (regularised evolution) | `run_rea` | [275](../src/run_v2.py#L275) |

`src/run_experiment.py` is the v1 runner (A/B/C/D only) and is superseded.
`src/deep_analysis.py` and `src/analyze_results.py` are the v1 analysis pair.

---

## 4. Data census

Granularity classes, as requested, across the whole tree and both zips:

| Class | Definition | Count found |
|---|---|---|
| RAW | per-architecture, per-epoch loss/accuracy curves | **0** |
| SPEC | generated architecture JSON specifications | **0** |
| TRANSCRIPT | raw LLM generations | **0** |
| SUMMARY | per-condition aggregates | **5** (`paper/figures/tab_*.tex`) |
| DERIVED | figures, rendered tables | **11** (figure PDFs) |

### Cell coverage: 6 conditions × 2 datasets × 2 seeds = 24 cells

**RAW / SPEC / TRANSCRIPT present in 0 of 24 cells.**

SUMMARY coverage is partial and asymmetric:

| Cell group | What survives |
|---|---|
| 6 conditions × CIFAR-10 × seed 42 | mean, std, median, best (`tab_main.tex`); params, blocks, gap, efficiency, diversity, time (`tab_arch.tex`); 15 pairwise tests (`tab_stats.tex`); rank correlations (`tab_rank.tex`); transcript counts for B/C/D (`tab_transcript.tex`) |
| 6 conditions × CIFAR-100 × seed 42 | mean, std, median, best; 15 pairwise tests only |
| all 12 cells × seed 137 | **nothing** — no artifact contains any seed-137 value |

The paper asserts a seed-137 partial replication ([main.tex:350](../paper/main.tex#L350)).
`scripts/run_all_v2.sh` was written to run seed 137 for all six conditions on both
datasets. No seed-137 number appears in any surviving artifact, so the replication
claim is unverifiable from this repository.

---

## 5. Environment

**Nothing is pinned.** There is no `requirements.txt`, no lockfile, no
`environment.yml`, no `pyproject.toml`, no `setup.py`.

| Item | Recorded? |
|---|---|
| Python version | no |
| torch / torchvision version | no |
| transformers / bitsandbytes version | no |
| CUDA version | no |
| Hardware | conflicting: abstract says A100-40GB; `docs/` say GH200 480GB |
| Which LLM served the requests | **not recorded anywhere** — see below |

**RNG seeding.** `run_v2.py` passes `seed + i` to architecture *i*
([run_v2.py:166](../src/run_v2.py#L166), [189](../src/run_v2.py#L189),
[256](../src/run_v2.py#L256)). `train_architecture` then calls
`torch.manual_seed(seed)` and uses the same seed for the train/val split
([train_arch.py:43](../src/train_arch.py#L43), [59](../src/train_arch.py#L59)).
Consequence: **the train/validation split changes for every architecture.** It is
balanced across conditions — architecture *i* always gets split *seed+i* in every
condition — but it is not a fixed split, contradicting Algorithm 1
([main.tex:329](../paper/main.tex#L329)), which shows a single split before the loop.

The LLM server is a separate process with no seeding hook at all, so LLM sampling
is not reproducible.

**Model provenance gap.** `run_v2.py` hardcodes `LLM_MODEL = "Qwen/Qwen3-8B"`
([line 32](../src/run_v2.py#L32)) and sends it in every request. Both servers
**ignore** the requested model and answer with whatever they loaded
([llm_server_small.py:54](../src/llm_server_small.py#L54)). No script starts a
server. `metadata.json` records condition, dataset, seed, n, temperature and
device — but **not the model** ([run_v2.py:441](../src/run_v2.py#L441)). So
nothing in the repo, and nothing that the repo would have written, records which
model produced the results. The paper's `Qwen3-1.7B-4bit` claim is consistent with
`llm_server_small.py` but cannot be confirmed from any artifact.

---

## 6. Paper source

| Property | Value |
|---|---|
| documentclass | `article`, 10pt, `\usepackage{icml2025}` ([main.tex:2](../paper/main.tex#L2)) |
| Citation style | `icml2025.bst`, author–year via `\citep` / `\citet` |
| Page count | **10** (`Output written on main.pdf (10 pages, 555094 bytes)`) |
| PDF vs .tex | `main.tex` 2026-05-14 01:35:40; `main.pdf` 2026-05-14 01:38:01 → **PDF is current** |
| Build | last build succeeded; no TeX toolchain is installed locally, so no rebuild was attempted |
| PDF metadata | `/Title` and `/Author` are empty — good, but re-verify at submission |

The `main.tex` comment at line 12 reads `Compact spacing for 8-page fit`, the
README targeted a 4-page venue, and the artifact is 10 pages. All three disagree.

`logs/main.log` is **not** this build. It is a failed MiKTeX run from
`C:/Users/nitua/AppData/Local/Temp/paper/` that aborted on a missing
`icml2025.sty` and produced no PDF. The real build log is `paper/main.log`.

---

## 7. Dead weight and conflicts

- **`archive/resv2.zip` is redundant.** Its `main.tex` and `references.bib` are
  byte-identical (SHA-256 match) to the live `paper/` copies. `resv1.zip` is a
  genuinely earlier version.
- **`docs/methodology.md` is superseded and contradicts the paper.** It describes
  4 conditions, 3 replications, and **a hosted third-party commercial LLM API**
  as the generating model — against the paper's 6 conditions, 1 primary seed, and
  locally-served Qwen3-1.7B. It is best read as the pre-registration-era v1 plan,
  not a description of what ran. The specific vendor and model string are at
  `docs/methodology.md:77`, which stays on disk (gitignored, not committed).
- `docs/` was added to `.gitignore` during this audit (operator decision) so the
  public repo does not carry a superseded plan contradicting the manuscript. The
  files remain on disk and are cited throughout this audit.
- A cloud host IP present in `docs/methodology.md` and `docs/research-state.md`
  was replaced with `<REDACTED-HOST>` (operator-authorised).
- `credentials/` is empty; the `.pem` the old README described is gone. No secret
  of any kind was found in the tree.
- **Orphan v1 code**: `run_experiment.py`, `deep_analysis.py`,
  `analyze_results.py` are referenced only by `scripts/run_all.sh` and produce the
  three `figure*_*.pdf` files, which the current `main.tex` does not include.
- **Unreferenced figures**: `figure1_accuracy_boxplots.pdf`,
  `figure2_convergence.pdf`, `figure3_invalid_rates.pdf`,
  `fig5_training_dynamics.pdf` are present but not `\includegraphics`'d by
  `main.tex`.
- **`.gitignore` excludes `*.log`**, so `logs/main.log` and `paper/main.log` are
  untracked. It also excludes `paper/main.bbl`, which arXiv and most camera-ready
  pipelines require. Flagged as an open action, not changed.

# Step 2 findings — preliminary answers to the six questions

**Status.** Width sweep complete: 8/8 fetchers returned, ~90 notes, ~150
structured claims. This is a **step-2-level synthesis**, not the final report.
Steps 3–16 (contradiction graph, loci, depth investigation, cross-locus
reconciliation, triple draft, synthesis, four critics, patch, polish) have **not**
run. Positions below are supported by fetched primary sources but have not been
adversarially stress-tested by the critic layer.

---

## Q1 — Novelty: **partially scooped, and the scooper invited the follow-up**

**GENIUS (Zheng et al., arXiv:2304.10970, April 2023) already observed the
effect.** Section 6, verbatim:

> "we find that later iterations under-perform earlier iterations in some cases,
> and it is unclear why this should be the case… We believe future work on this
> problem is particularly valuable."

Appendix tables show real non-monotonic and declining trajectories on
NAS-Bench-201.

This is the most important finding for framing, and it cuts both ways:

- **Against**: the observation is published, and predates this work by ~3 years.
  "Contrary to prevailing assumptions" is not defensible.
- **For**: it is a single unexplained sentence — no systematic ablation isolating
  feedback as causal, no link to scale, quantisation or diversity, mixed in with
  improving trials. **And GENIUS explicitly asks for the follow-up.** The
  strongest available framing is *"GENIUS flagged this anomaly and called it
  valuable future work; we are that systematic study."* That is an honest,
  citable, defensible position — and it is considerably stronger than a novelty
  claim that a reviewer can puncture with one sentence from a 2023 paper.

Priority against the rest: **none runs the subject paper's mechanism.**
EvoPrompting, GPT-NAS, LLMatic, RZ-NAS and CoLLM-NAS all embed the LLM in an
evolutionary or quality-diversity scaffold rather than sequential self-refinement
on a scalar metric. LLMatic states outright that *"LLMs struggle to conduct NAS
directly through prompts."*

## Q2 — Mechanism: **the result is confirmatory, and predicted by a scaling law**

Settled enough that a small-model demonstration reads as confirmatory:

- **Huang et al. (ICLR 2024)**: intrinsic self-correction *degrades* reasoning
  across all models; degradation largest for the weakest (Llama-2-70b-chat GSM8K
  62.0→36.5) and smallest for the strongest (GPT-4-Turbo 91.5→90.0).
- **Song et al., "Mind the Gap" (ICLR 2025)**: formalises the
  **generation–verification gap** and shows it **scales monotonically with
  pretraining FLOPs**. A 1.7B model failing is the *predicted value* of a
  published relationship.
- **Stechly et al.**: "significant performance collapse with self-critique and
  significant performance gains with sound external verification." Credits
  **CRITIC (Gou et al. 2023)** as first to notice self-critique degradation.

**Four rival explanations for twenty identical designs, none excluded by the
paper:**

1. **`sanitize_config`** coerces malformed output to `standard_3x3 / relu /
   batchnorm` — the exact reported template — and runs on LLM arms only
   (`audit/FORENSICS.md` F2). Internal, and the strongest.
2. **Decoding procedure.** Diverse Beam Search (2018): standard beam search
   yields "sequences that differ only slightly from each other." Predates
   everything.
3. **RLHF/alignment.** Hamilton (EACL 2024): mode collapse rises monotonically
   with alignment intensity. The RLHF-diversity paper claims the first rigorous
   demonstration of across-input mode collapse from RLHF, across 5 OPT scales.
4. **Quantisation.** **Still under-sourced** — no source found that isolates
   quantisation's effect on generation diversity. Genuine gap.

Note the opposite failure mode exists too: GENIUS reports GPT-4 shows response
randomness even at temperature 0.

## Q3 — Methodology: **the paper fails a published checklist, by name**

**Lindauer & Hutter, *Best Practices for Scientific Research on NAS* (JMLR)** —
14 numbered practices. Failures:

- **BP8** — random *sampling* and random *search* are distinct required
  baselines. The paper has one random arm.
- **BP9** — seeded multi-run reporting with mean and stdev. The paper has
  **1 primary seed**; the partial second seed's numbers are **ORPHAN**.
- **Li & Talwalkar (UAI 2019)** uses **6 seeds per benchmark** as its own remedy.
- **Agarwal et al. (NeurIPS 2021 Outstanding Paper)** argues against
  point-estimate comparison on small N, for interval estimates and IQM.
- **The 1000-papers survey states the correct estimand explicitly**:
  expected-best-of-*k* = top 100/*k*% in expectation. The paper reports
  mean-of-population — and **condition D wins on best-of-*k* on both datasets**
  (`audit/CLAIM_TRACE.md` §5.3). The estimand choice inverts the headline.
- No tabular benchmark. The paper concedes NAS-Bench-201 as the natural next
  step.

## Q4 — Counter-evidence: **it bounds the claim; it does not defeat it**

Every counter-case examined uses **external, executable, or proxy-scored
verification** — none is intrinsic self-refinement on a scalar metric:

| Work | Feedback mechanism | Verdict |
|---|---|---|
| **EvoPrompting** (62B PaLM) | evolutionary selection; **random-parents ablation is the worst plateau** — feedback demonstrably helps | strongest direct counter; different scale + scaffold |
| **CoLLM-NAS** (CVPR 2026 NAS WS, Oral) | stateful Navigator LLM, iterative feedback + trajectory; beats conventional search on NAS-Bench-201/ImageNet, 4–10× cheaper | strongest same-domain counter |
| **RZ-NAS** (ICML 2025) | reflection inside evolutionary mutation–selection, zero-cost proxies | bounds |
| **FunSearch** (Nature) | hard external evaluator + island diversity | bounds |
| **AlphaEvolve** | population-based, multi-evaluator | bounds |
| **Reflexion** | test-execution-grounded, 91% pass@1 | bounds |
| **OPRO** (ICLR 2024) | past solutions + scores in prompt; +8% GSM8K, +50% BBH | bounds; prompt-opt, frontier scale |
| **Olausson self-repair** (ICLR 2024) | self-repair gains "often modest… sometimes not present at all" | **supports** the thesis |

**Conclusion: "feedback degrades LLM-guided NAS" is false unqualified.** The
defensible version is *feedback helps iff it carries credit assignment* — which
Tyen et al. (ACL 2024) supplies the mechanism for: models fail to **find** errors,
not to fix them; correction is robust once error location is given externally.
Scalar validation accuracy signals *that* something is wrong, never *where*.

## Q5 — Venue: see `research/temp/venue-findings-interim.md`

Primary: **"Who Verifies the Agents?"** (Sydney) — its topic list names
*"Self-evolving agents: stable improvement without collapse."* 4–9 pp,
double-blind, non-archival.
Secondary: **SLM-Agents** (Paris) — quantisation explicitly in scope; **Aug 29**.
EvoRobust deadline **Aug 30**, no CFP published yet.
AutoML 2026 closed (May 14) and artifact-gated. ICBINB moved to ICLR.

## Q6 — Framing: preliminary

**Strongest defensible thesis:** *Under a fixed budget, sequential self-refinement
on a scalar reward degrades small-model architecture proposals relative to
parallel zero-shot sampling — because scalar feedback carries no credit
assignment. Feedback helps only when it is externally verified and
localising.*

**What must be abandoned:**
1. "Contrary to prevailing assumptions" — GENIUS said it in 2023.
2. "All 20 designs identical" — refuted by the paper's own Jaccard 0.022.
3. `parameter std = 0K` — ORPHAN, no artifact.
4. Any unqualified "feedback degrades LLM-NAS" — RZ-NAS and CoLLM-NAS refute it.
5. The narrow-prior interpretation as *the* explanation — three rivals stand.

**Single highest-value experiment:** re-run condition B with
`sanitize_config` **disabled and raw generations logged**, plus a decoding
ablation (temperature × top-p). This costs no GPU training if only parse/validity
and diversity are measured, and it is the only experiment that discriminates
between the paper's thesis and the two strongest rival explanations. Without it,
the central claim is unfalsifiable from the stored evidence.

*(Runner-up, if compute exists: NAS-Bench-201 replication, which answers Q3's
benchmark objection and gives zero-noise best-of-k comparison.)*

---

# Q3 hardened — full texts recovered (batch 7)

Full-text fetches of the three canonical critiques supply exact numbers. The
Q3 verdict is no longer a characterisation; it is an enumeration.

**Yang, Esperança & Carlucci — "NAS evaluation is frustratingly hard" (ICLR 2020)**

- A **random-sampling average-architecture baseline beats most of 8 NAS methods
  across 5 datasets.**
- **Training-protocol tricks contribute >3pp accuracy; architecture choice
  contributes <1pp.**
- Impoverishing the searched operations shifts accuracy by only **0.18pp** —
  macro-structure (cell wiring) dominates searched micro-operations.
- **Seed alone drops ranking Kendall-τ to 0.48.**

The third bullet is the most dangerous for the subject paper. Its entire
between-condition spread on CIFAR-10 is **89.0 vs 87.2 = 1.8pp**, and Yang et al.
report that architecture choice buys **<1pp** while protocol buys **>3pp**. A
reviewer can argue the paper's headline effect is smaller than the protocol noise
floor its own fixed protocol cannot rule out. The fourth bullet independently
undermines a one-seed design: if seed alone degrades ranking correlation to 0.48,
a single seed cannot support a ranking claim between conditions.

**Li & Talwalkar (UAI 2019)**

- **0 of 12** audited 2018–19 NAS papers were exactly reproducible.
- Published random-search baselines used **1–24 architectures**, versus the
  **300–700** needed for a fair budget-matched comparison.

The subject paper's random baseline is **20 architectures** — inside the range
Li & Talwalkar identify as the failure mode. Its central claim ("LLM zero-shot
beats random search") rests on a baseline the canonical critique says is roughly
an order of magnitude too small to be fair.

**Sciuto et al. (ICLR 2020)** supplies the statistical template the subject paper
should have used: Welch's *t*-test reporting **NAO significantly *worse* than
random sampling (p = 0.02)** — a published precedent for a negative NAS result
reported rigorously, and a direct model for how to present this paper's finding.

**Huang et al. — exact scale gradient**: GPT-4 GSM8K 95.5→89.0 (**−6.5pp**) vs
Llama-2-70B 62.0→36.5 (**−25.5pp**). A clean monotone relationship between model
capability and self-correction damage.

## Which critiques the paper fails — enumerated

| Source | Requirement | Subject paper | Verdict |
|---|---|---|---|
| Lindauer & Hutter BP8 | random *sampling* and random *search* as distinct baselines | one random arm (+A2 filter) | **FAIL** |
| Lindauer & Hutter BP9 | seeded multi-run, mean ± stdev | 1 seed; seed-137 numbers ORPHAN | **FAIL** |
| Li & Talwalkar | budget-matched random baseline, 300–700 archs | 20 | **FAIL** |
| Li & Talwalkar | exact reproducibility | no data, no pins, no model record | **FAIL** |
| Yang et al. | control training protocol before attributing to architecture | fixed protocol, effect 1.8pp < 3pp protocol sensitivity | **FAIL** |
| Yang et al. | seed-robust rankings | 1 seed, τ=0.48 at 1 seed | **FAIL** |
| Agarwal et al. | interval estimates / IQM, not point estimates | mean-of-population point estimates | **FAIL** |
| 1000-papers survey | expected-best-of-*k* estimand | mean-of-population; best-of-*k* inverts the result | **FAIL** |
| Sciuto et al. | significance testing vs random sampling | done, but on dependent samples with pooled *d* | **PARTIAL** |
| Lindauer & Hutter | tabular benchmark where available | custom CNN space only | **FAIL** |

**RZ-NAS final citation**: ICML 2025, PMLR vol. 267, pp. 27237–27254; Zipeng Ji,
Guanghui Zhu, Chunfeng Yuan, Yihua Huang. No arXiv preprint exists.

## What this does to Q6

The reframe is now forced rather than optional. The paper cannot lead with
"LLM beats random search" — that comparison fails Li & Talwalkar on baseline
size. It cannot lead with "feedback degrades NAS" — RZ-NAS and CoLLM-NAS refute
it unqualified, and GENIUS published the observation in 2023.

What survives is narrower and sturdier: **a mechanism claim** — sequential
self-refinement on a *scalar, non-localising* reward degrades small-model
proposals, while every published success (EvoPrompting, RZ-NAS, CoLLM-NAS,
FunSearch, AlphaEvolve, Reflexion, OPRO) supplies external, executable, or
localising verification. Tyen et al. gives the mechanism; Song et al. gives the
scaling law; the six-arm matched-budget design gives the controlled evidence.

That thesis does not depend on beating random search, and it survives every
critique enumerated above except the seed and estimand objections — both of which
are fixable in the analysis, not the experiment, **if the raw data exists**
(OA-1).

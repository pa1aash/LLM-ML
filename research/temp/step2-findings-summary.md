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

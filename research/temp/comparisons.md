# Cross-locus reconciliation — step 6

Two loci carry committed positions (L2/L3/L4 were deferred to step 8), so this
is a two-body reconciliation.

- **L1** — `interim-report-l1-feedback-degradation-priority`
- **L5** — `interim-report-l5-rz-nas-zero-cost-proxy-validation`

---

## 1. What L5 does, and does not do, to L1's conclusion

L1 concludes the unqualified thesis is refuted, resting partly on **RZ-NAS's
reflection ablation**. L5 concludes RZ-NAS's reflection *signal* is an
unvalidated, plausibly size-confounded proxy. The temptation is to read L5 as
demolishing L1's refutation. **It does not, and the distinction must be held
precisely.**

### What L5 does NOT do

**L5 does not show RZ-NAS's ablation is wrong.** That ablation compares
*reflection* against *no reflection*, holding the proxy fixed. Whatever the
proxy measures, both arms measure it. A confound in the shared signal does not
manufacture a difference between arms — it is common to both. The internal
validity of "reflection beats no reflection" **stands regardless of proxy
validity**, and L1's use of it to refute the unqualified thesis therefore
survives intact.

Nor does L5 rehabilitate the unqualified thesis by any other route. EvoPrompting's
ablation — the second pillar of L1's refutation — uses external fitness-based
selection, not a zero-cost proxy, and is untouched by L5 entirely. And GENIUS's
per-trial numbers, L1's third strand, are independent of both.

### What L5 DOES do

L5 attacks the **construct validity** of RZ-NAS's improvement, not its
existence. It questions *what the improvement is an improvement in*.

If the reflected-on signal substantially tracks parameter count rather than
architecture quality — Synflow 0.57–0.62 with parameter count, Zen-Score
0.68–0.99, ZiCo's margin over a naive `#Params` baseline nearly vanishing on the
size-isolated NATS-Bench-SSS — then "reflection improves the proxy score" may be
closer to "reflection reliably grows the model" than to "reflection finds better
architectures."

That has one specific consequence for priority: **RZ-NAS and the subject paper
may not be measuring the same phenomenon.** RZ-NAS refines against a cheap
possibly-size-tracking scalar; the subject paper refines against measured
validation accuracy. A result about the first does not automatically transfer to
the second. So RZ-NAS's status as a counter-example is **narrowed in scope, not
cancelled**.

Two further points sharpen this and are worth carrying:

- RZ-NAS **quotes NAS-Bench-Suite-Zero's ensemble-motivated warning verbatim and
  does not act on it**, using a single experimenter-chosen proxy per run.
- Its rank-correlation validation is **confined to NAS-Bench-201 — the benchmark
  NAS-Bench-Suite-Zero itself identifies as the easy case** where nearly all
  proxies look adequate.

Neither is an error in the ablation. Both are gaps in the paper's warrant for
generalising it.

---

## 2. Joint surviving position

The unqualified claim that iterative feedback degrades LLM-guided neural
architecture search is refuted and cannot be restated: two controlled ablations
(RZ-NAS, EvoPrompting) show feedback helping under curated signals, and the
observation most often cited in its support — GENIUS's Section 6 remark — is
contradicted by GENIUS's own per-trial tables, which show feedback beating
zero-shot in every reported trajectory. What survives is narrower and
mechanism-specific: **when an LLM's uncurated iteration history accumulates
inside a single growing context, rather than being filtered into a synthesised
strategy or an external archive, iterative feedback degrades proposal quality,
particularly as task difficulty rises** — and that formulation is already
ablation-verified in CoLLM-NAS (Sept 2025), so it is *partially scooped* rather
than open. Two things remain genuinely untouched by any source across both loci:
the **small/quantised single-model regime** (every prior ablation uses
frontier-scale or fine-tuned research-scale models — GPT-4o, 62B PaLM,
purpose-fine-tuned GPT), and the **collapse-to-a-single-template** observation.
Layered on top, L5 establishes that the strongest counter-case refines against a
signal it never validated cross-benchmark and which is size-confounded for at
least three of its five proxies — which does not restore the general claim, but
does mean the counter-evidence and the subject paper may be measuring different
things, and that any comparison between them must say which.

---

## 3. Seams and disagreements — not smoothed

**S1. The two loci disagree on how much weight RZ-NAS can bear, and neither
resolves it.** L1 treats RZ-NAS's ablation as load-bearing refutation evidence.
L5 treats the same paper as methodologically compromised in its signal. Both are
correct about different properties of the same artifact. **Unreconciled:** no
source establishes whether a size-confounded proxy is *sufficient* for the
ablation's conclusion to transfer to accuracy-based feedback. That is an
empirical question nobody in the corpus has asked.

**S2. CORRECTED BY STEP 8 (C6) — the asymmetry was overstated.** This seam
originally read that L1's "partially scooped" verdict rested on *one
un-peer-reviewed arXiv v2 preprint*. **That is wrong. CoLLM-NAS was accepted as
an Oral at the CVPR 2026 NAS Workshop, and the evidence for that was already in
the vault** — missed by L1 and by this file's first draft. The verdict carrying
the most consequence for the subject paper's novelty is therefore **peer-reviewed
and orally accepted**, which strengthens rather than weakens the "partially
scooped" finding.

What remains genuinely open is narrower: whether CoLLM-NAS's noise-accumulation
ablation has been **independently cited, replicated or challenged**. Step 8
returned that as **NOT SETTLED — fetch budget exhausted**, with five candidate
citing papers listed as unverified leads.

**S3. L1's GENIUS finding is based on partial sampling.** The investigator read
one appendix table (NAS-Bench-Macro, Temperature=1) of several in Appendix A.3.
A full pass could still surface a trial where the *final* iteration nets worse
than zero-shot, which would restore GENIUS as an independent second scoop and
change L1's verdict. **This is an open falsifier of L1's own position**, and L1
records it as such.

**S4. Scope boundary neither locus crosses.** L1 explicitly excludes the
template-collapse claim from its remit ("a distinct empirical claim requiring
L2's diversity-collapse literature"). L5 does not touch it either. So the
surviving novelty claim the joint position leans on — template collapse — **has
been assessed by neither investigator.** It rests on the deferred L2 evidence
and on the repo audit's sanitiser finding, not on step-5 work.

**S5. RESOLVED BY STEP 8 (C5) — the quantity is UNUSABLE. Do not cite it.**
The Zen-Score tau comparison is **not apples-to-apples**: Zen-NAS's 0.91/0.88 is
over **n=16 ResNet-50 variants**, while the 0.28–0.29 figures are over
**n=15,625 NAS-Bench-201 architectures**. Different pools, different scales;
the comparison is meaningless. **Marked UNUSABLE — it must not enter the
decision brief or any downstream artifact.**

Step 8 also found that the two low figures are **not independent
reproductions**: RZ-NAS reused ZiCo's published table verbatim. So even the
"two independent sources agree" reading was wrong. This kills the
self-report-inflation line entirely — correctly, and before it reached a
reviewer.

**S6. Untested corner.** MAE-DET, RZ-NAS's COCO proxy, is addressed by no source
in hand. Its size-confound status is **UNKNOWN**, not "clean".

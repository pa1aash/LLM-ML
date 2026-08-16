# Corpus critic findings — S1e, step 8

Governing question for every item: **what source, if it existed, would overturn
the current direction?** Every claim below is answered from note IDs and
verbatim quoted support. NOT IN CORPUS / NOT SETTLED are recorded wherever the
vault (or, for C1/C6, the one permitted search wave) does not support a claim
— that is a reportable finding, not a gap in this document.

---

## C1 — Novelty of the instrumentation thesis itself

**Verdict: ADJACENT AND ACTIVE, BUT NOT STATED FOR NAS. The general mechanism
is already a live 2024–2026 literature; its specific application to LLM-guided
architecture/program search — parser, sanitiser, schema-repair, or
constrained-decoding artifacts being mistaken for a model's own "collapse to a
template" or "feedback degrades proposals" — is not published anywhere this
search wave or the vault could find.**

### What the vault already contains

Vault searches (`constrained decoding output distribution`, `JSON schema
enforcement LLM generation`, `harness benchmark artifact agent evaluation`,
`repair retry loop code generation pass rate`, `grammar-constrained generation
diversity`, `sanitiser coercion architecture generation`, `structured output
constrained decoding grammar`) returned **no source that states the
instrumentation-artifact thesis** for NAS or for LLM-driven search generally.
The closest vault-resident material is on a different question — whether
self-correction/self-repair helps or hurts, not whether the *measurement
apparatus* (parser/sanitiser/decoder constraint) is responsible for an
observed effect:

- `230609896-is-self-repair-a-silver-bullet-for-code-generation` (Olausson et
  al.) — already in corpus. Finding: "when the cost of carrying out repair is
  taken into account, performance gains are often modest, vary a lot between
  subsets of the data, and are sometimes not present at all... self-repair is
  bottlenecked by the model's ability to provide feedback on its own code."
  This is mechanism-of-self-correction evidence, not an instrumentation-artifact
  claim — it never asks whether the *harness* (rather than the model) produced
  the measured pass-rate change.
- `when-can-llms-actually-correct-their-own-mistakesa-critical-survey-of-self-corre`
  and `large-language-models-cannot-self-correct-reasoning-yet` — same
  category, mechanism-of-self-correction, not instrumentation.

No vault source discusses JSON-schema enforcement, grammar-constrained
decoding, or output-repair/retry loops as a **confound** that could be
mistaken for a property of the model being searched over.

### What the search wave found (arXiv, academic APIs)

One targeted arXiv sweep (`abs:"grammar-constrained" AND abs:"quality"`,
`abs:"structured output" AND abs:"degrad"`, `abs:"format constraint" AND
abs:"reasoning"`) surfaced four papers that state the **general** version of
the instrumentation thesis directly. All four have now been fetched into the
vault at the corpus critic's discretion (fetch discipline for C1 explicitly
permitted this):

1. **`240802442-let-me-speak-freely-a-study-on-the-impact-of-format-restrictions-on-pe`**
   (Tam et al., "Let Me Speak Freely?", Aug 2024, cs.CL). Verbatim abstract:
   > "Structured generation, the process of producing content in standardized
   > formats like JSON and XML, is widely utilized in real-world applications
   > to extract key output information from large language models (LLMs)...
   > Surprisingly, we observe a significant decline in LLMs reasoning
   > abilities under format restrictions. Furthermore, we find that stricter
   > format constraints generally lead to greater performance degradation in
   > reasoning tasks."
   This is the closest thing in the literature to "the harness is the
   result": the measured capability (reasoning) drops as a direct function of
   output-format constraint tightness, independent of the underlying model.

2. **`240521047-grammar-aligned-decoding`** (May 2024, foundational). Verbatim:
   > "we demonstrate that GCD techniques (and in general constrained decoding
   > techniques) can distort the LLM's distribution, leading to outputs that
   > are grammatical but appear with likelihoods that are not proportional to
   > the ones given by the LLM, and so ultimately are low-quality."
   This is a formal statement that a grammar/schema enforcer changes what is
   sampled, independent of the underlying model's own distribution — the
   mechanism the subject paper's sanitiser/parser critique would need to cite
   as precedent.

3. **`260403616-the-format-tax`** (Apr 2026, most directly on point).
   Verbatim: "Asking a large language model to respond in JSON should be a
   formatting choice, not a capability tax. Yet we find that structured
   output requirements — JSON, XML, LaTeX, Markdown — substantially degrade
   reasoning and writing performance across open-weight models. The research
   response has focused on constrained decoding, but sampling bias accounts
   for only a fraction of the degradation. The dominant cost enters at the
   prompt: format-requesting instructions alone cause most of the accuracy
   loss, before any decoder constraint is applied." **This is a load-bearing
   nuance for the subject paper's mechanism story**: if the subject paper's
   own instrumentation critique attributes degradation/collapse to a
   parser/sanitiser stage specifically, "The Format Tax" would predict that a
   meaningful share of the effect instead traces to the *prompt* asking for a
   fixed schema in the first place, not the decoder-side repair step. The
   subject paper's mechanism claim should be checked against this
   prompt-vs-decoder split before being stated unqualified.

4. **`260810137-the-parser-already-knows-lightweight-bias-correction-in-constrained-de`**
   (Aug 2026, most recent). Verbatim: "Grammar Constrained Decoding (GCD)
   forces Language Models (LMs) to produce syntactically valid outputs by
   masking out non-conforming tokens at each step. However, rigid masking
   distorts the model's underlying probability distribution, often biasing
   generation toward valid but suboptimal outputs."

### Adjacent literatures explicitly checked and found empty for the NAS-specific claim

- `abs:"neural architecture search" AND abs:"parser"` (arXiv) — 1 irrelevant
  hit (AutoKE, scientific-ML knowledge embedding, unrelated).
- `abs:"neural architecture search" AND abs:"constrained decoding"` (arXiv) —
  0 hits.
- `abs:"retry loop" AND abs:"code generation"` (arXiv) — 0 hits.
- `abs:"evaluation harness" AND abs:"confound"` (arXiv) — 0 hits.

No paper in arXiv's indexed literature, as of this search, combines the
constrained-decoding/structured-output-distortion mechanism with neural
architecture search specifically.

### Committed reading

Two claims must be kept separate, and the subject paper's positioning depends
on which one it is making:

- **"Constrained/structured output requirements can distort what is measured
  about an LLM's capability, independent of the model's true underlying
  distribution"** — this is **already published and active** (4 sources
  above, 2024–2026, one as recent as this month). A paper asserting only this
  general point, without the NAS application, would read as confirmatory, not
  novel, and should cite this literature rather than present the mechanism as
  original.
- **"Parser/sanitiser/schema-repair artifacts in an LLM-guided NAS pipeline
  are responsible for the observed 'collapse to a single template' and/or
  the observed feedback-degradation effect"** — this specific, NAS-scoped
  instantiation of the mechanism is **NOT IN CORPUS and not found in this
  search wave**. It is the genuine, checked-for gap the subject paper can
  claim, provided it is framed as an application of an established mechanism
  to a new setting (architecture search) rather than as a new mechanism.

### Sources fetched for C1

- `240802442-let-me-speak-freely-a-study-on-the-impact-of-format-restrictions-on-pe`
- `240521047-grammar-aligned-decoding`
- `260403616-the-format-tax`
- `260810137-the-parser-already-knows-lightweight-bias-correction-in-constrained-de`

All four are abstract-page-depth notes (fetched via `hyperresearch fetch` on
the arXiv abstract URL); full-text PDF extraction was not run for these —
if the draft needs mechanism-level detail beyond the abstract (e.g., ASAp's
algorithm in Grammar-Aligned Decoding, or the exact prompt-vs-decoder
attribution split in The Format Tax), a follow-up PDF fetch is recommended
before citing beyond the abstract-level claims quoted above.

---

## C4 — L2 quote verification

**(i) 4-bit quantisation reduces lexical/syntactic (not semantic) diversity,
lexical drop worse in smaller models.**

Source: `241210271-benchmarking-linguistic-diversity-of-large-language-models`,
Section 6.4 ("Impact of Model Scale and Quantization"), verbatim:

> "We further investigate the impact of post-training quantization on
> linguistic diversity. We quantize the Qwen2.5 models of various scales to
> 4-bit precision with the bitsandbytes library, whereas the original models
> were run with bf16. As shown in Figure 8, quantization does not affect
> semantic diversity but reduces both syntactic and lexical diversity. The
> reduction in lexical diversity is more pronounced in smaller models, while
> the effect on syntactic diversity becomes more evident in larger models.
> This finding suggests that quantization has greater impact on the diversity
> of form rather than content."

**Verdict: CONFIRMED**, accurate paraphrase (not a literal verbatim string,
but the substance matches exactly: semantic diversity unaffected, both
lexical and syntactic diversity reduced, lexical drop worse in smaller
models). **One nuance the L2 claim as stated omits**: the syntactic-diversity
effect runs in the *opposite* size direction from the lexical effect —
"more evident in larger models" — a directionally important detail if the
draft ever generalizes this to "smaller models are worse across the board."
The claim as given only asserts the lexical-size relationship, so it is not
technically wrong, just incomplete if extended further.

**(ii) 4-bit causes mild "Signal Degradation" while 2-bit causes catastrophic
"Computation Collapse."**

Source:
`260419884-from-signal-degradation-to-computation-collapse-uncovering-the-two-fai`.
Abstract, verbatim:

> "While 4-bit quantization is widely regarded as an optimal trade-off,
> reducing the precision to 2-bit usually triggers a catastrophic
> 'performance cliff.'... we conduct a systematic mechanistic analysis,
> revealing two qualitatively distinct failure modes: Signal Degradation,
> where the computational patterns remain intact but information precision is
> impaired by cumulative error; and Computation Collapse, where key
> components fail to function, preventing correct information processing and
> destroying the signal in the early layers."

And later, the explicit bit-width pairing, verbatim:

> "the Signal Degradation mode (typical in 4-bit) is localizable and
> repairable, whereas the Computation Collapse mode (observed in 2-bit)
> proves systemic and irreversible without retraining."

And the phenomenology section: "The degradation from FP16 to 4-bit is
gradual, maintaining usability. Conversely, the transition to 2-bit triggers
a catastrophic collapse where accuracy plummets to zero."

**Verdict: CONFIRMED.** The word "mild" is not used verbatim, but "gradual...
maintaining usability" directly supports it, and the 4-bit→Signal-Degradation
/ 2-bit→Computation-Collapse pairing is explicit ("typical in 4-bit" /
"observed in 2-bit"). One minor imprecision worth flagging for the draft: the
paper's own appendix notes "the 4-bit and 3-bit AWQ models exhibit Signal
Degradation," so the pairing is "typical," not an absolute 1:1 rule confined
only to 4-bit.

**(iii) QeRL's contrary finding that quantisation noise INCREASES sampling
entropy.**

Source:
`251011696-qerl-beyond-efficiency-quantization-enhanced-reinforcement-learning-fo`.
Abstract, verbatim:

> "Beyond efficiency, our findings show that quantization noise increases
> policy entropy, enhancing exploration, and enabling the discovery of better
> strategies during RL."

And body text, verbatim: "our analysis surprisingly reveals that quantization
noise, with precise control, can benefit RL by increasing policy entropy...
This finding contrasts with results from SFT of LLMs (Dettmers et al., 2023a;
Guo et al., 2023), demonstrating that controllable quantization noise in RL
enhances exploration."

**Verdict: CONFIRMED verbatim for the words used ("quantization noise
increases policy entropy") — but the L2 claim as phrased ("increases sampling
entropy," unqualified) overstates the scope of what QeRL actually shows, and
this needs correcting before it enters the draft as a rival explanation.**
QeRL's finding is specific to **policy entropy during RL training**, produced
by a deliberately engineered Adaptive Quantization Noise (AQN) mechanism that
dynamically schedules injected noise via LoRA adapters — not a general claim
about the output-distribution entropy of a static, already-quantized model
doing ordinary inference-time generation. QeRL's own text explicitly
contrasts its RL-training result against SFT results, i.e., the authors
themselves flag this as context-dependent, not a general property of
quantization noise on any sampling process. If the subject paper cites QeRL
as a rival explanation for why a quantized model might show *higher* output
diversity (contra the paper's own observed collapse), the citation should
specify "RL-training-time entropy under an engineered noise schedule," not
"sampling entropy" generically — the subject paper's own regime (zero-shot /
few-shot generation from a static quantized model, no RL, no AQN) does not
match the setting QeRL's finding was established in.

---

## C5 — Zen-Score Kendall-tau discrepancy

**Verdict: NOT apples-to-apples. UNUSABLE as stated — must not enter any
downstream artifact as evidence of a self-report-vs-independent-reproduction
gap.**

**Zen-NAS's self-report** (`zen-nas-a-zero-shot-nas-for-high-performance-deep-image-recognition-full-text`),
Figure 15 caption, verbatim:

> "Zen-Score v.s. top-1 accuracy, 16 randomly sampled structures generated
> from ResNet-50, with Kendall's τ-score between accuracy and Zen-Score."
> — τ = 0.91 (CIFAR-10), τ = 0.88 (CIFAR-100)

**RZ-NAS's report**
(`icml-poster-rz-nas-enhancing-llm-guided-neural-architecture-search-via-reflectiv`),
Table 3, verbatim caption: "The correlation coefficients between various
Zero-Cost proxies and test accuracy on **NAS-Bench-201** (KT and SPR
represent Kendall's τ and Spearman's φ, respectively)." Zen-Score row: KT =
0.29 (CIFAR-10), 0.28 (CIFAR-100), 0.29 (ImageNet16-120).

**ZiCo's report** (`zico-zero-shot-nas-via-inverse-coefficient-of-variation-on-gradients-full-text`),
Table (NATSBench-TSS = NAS-Bench-201), Zen-score row: KT = 0.29/0.28/0.29,
SPR = 0.38/0.36/0.40 — matching RZ-NAS's Table 3 to two decimal places across
every cell.

**Three separate problems, checked directly:**

1. **Architecture pool.** Zen-NAS's self-report is computed on "16 randomly
   sampled structures generated from ResNet-50" — 16 hand-generated variants
   of a single architecture family. RZ-NAS's and ZiCo's number is computed on
   the full NAS-Bench-201 space (15,625 architectures spanning a diverse cell
   topology search space). These are not the same population, and Kendall's
   τ computed over a narrow, near-homogeneous 16-sample pool derived from one
   parent architecture is expected to be inflated relative to τ computed over
   a large, structurally diverse benchmark — this is exactly the
   narrow-diversity effect that NAS-Bench-Suite-Zero's own finding (used
   elsewhere in this corpus, L5) predicts.
2. **Sample size.** n=16 vs. n=15,625. A Kendall's τ estimated from 16 points
   carries far higher variance than one estimated from a benchmark of that
   size; the two numbers are not comparable point estimates of the same
   quantity.
3. **Validation protocol / benchmark identity.** Zen-NAS trained its own 16
   structures itself, off-benchmark. RZ-NAS and ZiCo both validate against
   NAS-Bench-201's standardized, pre-computed accuracy tables. Same
   correlation statistic (Kendall's τ) is used in both cases, so the *formula*
   is comparable — but the *population it is computed over* is not.

**Additional finding not anticipated by the locus question**: RZ-NAS's and
ZiCo's numbers are **not independent** of each other. RZ-NAS's Table 3 values
for GraSP, Synflow, Zen-Score, and ZiCo all match ZiCo's own published Table
exactly (same KT and SPR to two decimals across every cell and every
dataset), which is the same conclusion L5's interim report already reached
("confirming RZ-NAS reused this paper's published correlation figures rather
than recomputing them"). So "RZ-NAS and ZiCo independently report 0.28–0.29"
as framed in the task brief is imprecise: it is **one measurement (ZiCo's),
reported twice**, not two independent replications.

**Disposition**: this finding — Zen-NAS's self-report vastly exceeding the
independently-validated NAS-Bench-201 number — cannot be used as evidence
that "proxy authors systematically overstate their own proxy's quality"
(the framing L5's interim report flagged as a risk) because the two numbers
are not measuring the same thing. It should not appear in the draft except,
at most, as a methodological aside noting that self-reported correlation
figures in the zero-cost-proxy literature are sometimes computed on
small, non-standardized samples rather than shared benchmarks — a general
observation about the field's evaluation hygiene, not a specific indictment
of Zen-Score's validity relative to RZ-NAS's or ZiCo's numbers.

---

## C2 — L3 citation check: expected-best-of-k vs. population mean

**Verdict: the specific quoted claim from the prior session does not exist
verbatim. A closely related but functionally different statement does exist
in `neural-architecture-search-insights-from-1000-papers`, and it is not a
normative "correct estimand" recommendation — it is a justification for why
random search is a strong baseline. The corpus's actual normative guidance on
what to report (Lindauer & Hutter; Yang et al.) points toward
mean-and-standard-deviation over repeated runs, not a general
"expected-best-of-k is the estimand" doctrine. Report as NOT IN CORPUS for
the literal claim as previously recorded.**

**What `neural-architecture-search-insights-from-1000-papers` actually says**
(Section 3.1, "Baselines"), verbatim (LaTeX math markup expanded):

> "This is especially true for highly engineered search spaces with a high
> fraction of strong architectures, since random search with a budget of k
> evaluations will, in expectation, find architectures in the top 100/k% of
> the search space."

This sentence exists and is close in substance to the prior session's
paraphrase ("expected-best-of-k = top 100/k% in expectation"), but its
**function in the source is different from what the paraphrase implies**: it
is offered as an explanation for *why random search is a surprisingly strong
baseline* ("Despite its naïveté, multiple papers have shown that random
search performs surprisingly well... This is especially true..."), not as a
general methodological claim that expected-best-of-k is *the correct
estimand a NAS paper should report* under a fixed budget, in contrast to
population mean. The survey never frames this as an estimand choice at all —
searches for "estimand," "population mean," "best-of-k" (hyphenated or not),
and "top k%" return zero hits anywhere else in the 201,140-character full
text.

**What the corpus's actual best-practices/reviewer-facing sources say instead**
— and this cuts the other way from "expected-best-of-k is the recommended
estimand":

`190902453v3-best-practices-for-scientific-research-on-neural-architecture-search`
/ `best-practices-for-scientific-researchon-neural-architecture-search`
(Lindauer & Hutter), section "Perform Multiple Runs with Different Seeds,"
verbatim:

> "we recommend that, if possible in terms of compute budgets, all methods
> should be repeated several times with different seeds and the authors
> should report mean and standard deviation (or median and quartiles if the
> noise is not symmetric) across the repetitions."

`nas-evaluation-is-frustratingly-hard` (Yang et al.), its own recommended
evaluation protocol, verbatim:

> "Report mean and standard deviation of the top-1 test accuracy, obtained at
> the end of the augmentation, for both the randomly sampled and the searched
> architectures... We emphasize that the comparison is not against random
> search, but rather against random sampling, i.e., the average architecture
> of the search space."

`190207638-random-search-and-reproducibility-for-neural-architecture-search`
(Li & Talwalkar) is critical of reporting a single best-found architecture at
all, verbatim: "the high variance of extremal statistics makes it difficult
to isolate the impact of the novel contributions introduced in each work,"
and recommends "the use [of] multiple runs to select the best architecture,"
going further to also evaluate "broad reproducibility... with multiple sets
of random seeds."

**Reading these together**: the corpus's actual, reviewer-facing
recommendation is to run a method **repeatedly** (multiple seeds), each run
producing one best-found result, and to report the **mean and standard
deviation across those repeated runs** — which is an empirical estimate of
E[best-of-k] obtained by averaging many independent best-of-k realizations —
compared against a **random-sampling population-mean baseline** (the average
architecture) as the floor, not as the target estimand for the method itself.
This is compatible with, but meaningfully more specific than, "expected-best-
of-k is the correct estimand" — and it explicitly recommends reporting
variance (std/quartiles) alongside the point estimate, which the flat
"expected-best-of-k = top 100/k%" paraphrase omits entirely. **If the draft
needs a citable normative statement about what NAS reviewers expect on this
axis, Lindauer & Hutter's "report mean and standard deviation across
repetitions" is the defensible citation — not the 1000-papers survey's
random-search justification, which was never making a reporting-standard
claim.**

---

## C7 — MAE-DET (RZ-NAS's COCO proxy)

**Verdict: UNKNOWN, confirmed. No corpus source addresses it directly.**

A vault-wide search for "MAE-DET" returns exactly three notes:
`interim-report-l5-rz-nas-zero-cost-proxy-validation` (which itself only
records that RZ-NAS *uses* MAE-DET for COCO and flags it as untested),
`icml-poster-rz-nas-enhancing-llm-guided-neural-architecture-search-via-reflectiv`
(RZ-NAS's own paper, which introduces MAE-DET as its Section 4.3 detection
proxy but runs no correlation/bias check on it), and
`zico-bc-a-bias-corrected-zero-shot-nas-for-vision-tasks-full-text`, where the
only occurrence is a **bibliography entry** — "Zhenhong Sun, Ming Lin, Xiuyu
Sun, Zhiyu Tan, Hao Li, and Rong Jin. Mae-det: Revisiting maximum entropy
principle in zero-shot nas for efficient object detection. arXiv preprint
arXiv:2111.13336, 2021" — cited in ZiCo-BC's reference list, not discussed in
its body text. Neither NAS-Bench-Suite-Zero, ZiCo, nor ZiCo-BC evaluates
MAE-DET's size/quality confound status. Its size-confound status remains
**UNKNOWN**, exactly as L5 recorded, and must not be upgraded to "clean" or
"confounded" without a source added to the corpus.

---

## C3 — L4 citation check: serial dependence within one context

**Verdict: NOT IN CORPUS, as anticipated. All three sources address a
different, standard notion of independence — independent training runs/seeds
— not intra-run serial dependence between proposals generated one after
another inside the same context.**

- `180608295-how-many-random-seeds-statistical-power-analysis-in-deep-reinforcement`:
  its independence assumption for its t-test framework is verbatim
  "Measurements are independent from one another. This seems reasonable in
  RL" — about measurements *across* seeded runs, not within one run's
  sequence of outputs.
- `230401910-on-the-variance-of-neural-network-training-with-respect-to-test-sets-a`:
  "these trainings make approximately independent errors on their test-sets"
  and "each independent run of training produces a different network" — again,
  run-to-run independence (different seeds), not within-run serial dependence.
- `210813264-deep-reinforcement-learning-at-the-edge-of-the-statistical-precipice`
  (Agarwal et al.): supplies the interval-estimate/stratified-bootstrap
  methodology explicitly built on "N independent runs" per task, footnoted as
  "A run can be different from using a fixed random seed... such as
  non-determinism of ML frameworks with GPUs" — still a between-run
  independence concept.
- `evaluating-the-search-phase-of-neural-architecture-search` was also
  checked (not on the original list but adjacent): its "independent" mentions
  concern architectures trained independently vs. under weight-sharing — a
  different independence question again (rank-correlation validity under
  weight sharing), not serial in-context dependence.

None of the four sources discusses correlation between successive outputs
generated by one model conditioning on its own prior outputs within a single
growing context — the specific structural property the subject repo's own
code was found to have (per the loci brief's deferral rationale, sourced from
audit/FORENSICS.md F3, not from literature). This is the expected outcome:
the literature supplies the standard for valid inference under the *standard*
independence assumption (independent seeded runs), and offers no ready-made
standard for the *serial-dependence-within-one-context* case the subject
paper's own design instantiates. Any claim in the draft about "valid
inference under serial dependence" must be sourced elsewhere or stated as an
open methodological question, not attributed to any of these four papers.

---

## C6 — CoLLM-NAS corroboration

**Sub-question 1: "Has it been accepted at a venue since?" — SETTLED, YES,
from the vault.**

The note already in the vault,
`250926037v2-collm-nas-collaborative-large-language-models-for-efficient-knowledg`
(fetched earlier in this session, well before this locus was assigned),
contains this in its "Comments" field, verbatim:

> "Accepted as Oral at CVPR 2026 Workshop on Neural Architecture Search
> (NAS)"

**This is a load-bearing correction to `research/temp/comparisons.md`.** Seam
S2 currently states: "L1's 'partially scooped' verdict rests on **one
un-peer-reviewed arXiv v2 preprint** (CoLLM-NAS) with no corroborating source
in the corpus... The verdict carrying the most consequence for the subject
paper's novelty is the one resting on the weakest evidence." That
characterization is **factually inconsistent with the vault's own copy of the
source it is describing**. CoLLM-NAS is no longer accurately described as
"un-peer-reviewed" — it has passed peer review and was accepted as an Oral
presentation at a dedicated NAS workshop co-located with CVPR 2026. This does
not make it equivalent to a full ICML/NeurIPS/ICLR main-track paper (it is
still a workshop-tier venue, and oral-vs-poster at a workshop is a lighter
bar than main-track acceptance), but "un-peer-reviewed preprint" overstates
the weakness of the evidence base underneath L1's strongest scoop claim. The
draft and any revision of comparisons.md's S2 seam should update this
characterization before proceeding.

**Sub-question 2: "Has its Generator-memory / noise-accumulation ablation
been cited, challenged, or replicated anywhere?" — NOT SETTLED, fetch budget
exhausted.**

No other note in the vault discusses or cites CoLLM-NAS. A vault-wide search
for "CoLLM-NAS" returns only the paper's own note and this investigation's
interim reports that discuss it (`interim-report-l1-feedback-degradation-priority`,
`research/temp/comparisons.md`) — no independent corpus source engages with
its Generator-memory ablation specifically. Settling this sub-question
requires fetching external sources, which the fetch budget for this session
does not permit.

**The exact search that would settle it** (queued for the orchestrator's
next targeted fetch wave, not run to completion here): query the Semantic
Scholar citations endpoint for `arXiv:2509.26037` (`GET
/graph/v1/paper/arXiv:2509.26037/citations?fields=title,year,venue`), then
fetch each citing paper's full text and check specifically for engagement
with the Generator-memory / noise-accumulation finding (Section 4.4 / Figure
6 of CoLLM-NAS), not just a related-work citation. Before this session's
fetch budget was exhausted, that citations query was run once and returned
five candidate citing papers, none yet fetched into the vault, listed here
for the orchestrator to prioritize (**not vault-verified — treat as
unconfirmed leads, not evidence**, until fetched and read):

- arXiv 2605.04057, "Structured Progressive Knowledge Activation for
  LLM-Driven Neural Architecture Search" (2026) — closest candidate by topic;
  its own abstract describes a related but distinct LLM-NAS failure mode
  ("functional entanglement": local LLM edits propagating into non-local
  performance shifts) and proposes factor-conditioned editing as a fix. Based
  on the abstract alone, it does not appear to replicate or challenge
  CoLLM-NAS's noise-accumulation finding specifically, but the full text was
  not checked.
- arXiv 2605.19247, "Structuring Open-Ended NAS: Semi-Automated Design
  Knowledge Structuring with LLMs for Efficient Neural Architecture Search"
  (2026) — abstract discusses "inefficient exploration due to biased or
  low-quality design ideas" in LLM-assisted open-ended NAS, adjacent territory,
  full text not checked.
- arXiv 2606.29582, "Bilevel Optimization for Neural Architecture Search"
  (2026) — general bilevel-optimization framing, appears to cite CoLLM-NAS
  only as an example LLM-NAS method; unlikely to engage the ablation, not
  checked.
- "Scaling Closed-Loop Feature Channel Configuration with LLMs" (2026, no
  arXiv ID captured) — not checked.
- "LLM-Driven Transient Stability Assessment: From Automated Simulation to
  Neural Architecture Design" (2025, no arXiv ID captured) — different
  application domain (power-systems stability), unlikely to be substantively
  relevant; not checked.

**Do not cite any of the five above in the draft as corroboration,
replication, or challenge until fetched and read in full** — at present they
are search hits, not verified evidence, and including them without
verification would repeat exactly the kind of interpretive drift this corpus
critic pass exists to catch.

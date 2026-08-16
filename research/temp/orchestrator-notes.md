# Orchestrator notes — llm-nas-feedback-positioning-7125b1

## Chain-position tracking

`TodoWrite` is **not available** in this session's toolset. Per the entry
skill's recovery procedure, chain position is tracked by **disk artifacts**
instead — find the highest-numbered step whose canonical artifact exists and
resume from the next step.

| Step | Canonical artifact | Done |
|---|---|---|
| bootstrap | `research/query-<tag>.md`, `research/scaffold.md` | ✅ |
| 1 decompose | `research/prompt-decomposition.json`, `research/temp/coverage-matrix.md` | ✅ |
| 2 width-sweep | vault notes tagged `<tag>` | |
| 3 contradiction-graph | `research/temp/contradiction-graph.json` | |
| 4 loci-analysis | `research/loci.json` | |
| 5 depth-investigation | vault notes `type: interim` | |
| 6 cross-locus-reconcile | `research/comparisons.md` | |
| 7 source-tensions | `research/temp/source-tensions.json` | |
| 8 corpus-critic | `research/corpus-critic-gaps.json` | |
| 9 evidence-digest | `research/temp/evidence-digest.md` | |
| 10 triple-draft | `research/temp/draft-{a,b,c}.md` | |
| 11 synthesize | `research/notes/final_report_<tag>.md` | |
| 12 critics | `research/critic-findings-*.json` | |
| 13 gap-fetch | `research/temp/post-critic-fetch-log.md` | |
| 14 patcher | `research/patch-log.json` | |
| 15 polish | `research/polish-log.json` | |
| 16 readability | `research/readability-recommendations.json` | |

## Bootstrap record

- Vault already initialised (`.hyperresearch/hyperresearch.db`); `init` no-op.
- All 16 step skills present in the project skills directory; no
  `--steps-only` install needed.
- `archive-run`: `archived: false`, 0 files moved — fresh vault, nothing to
  archive.
- `vault-tag` minted: `llm-nas-feedback-positioning-7125b1`.
- Modality: **synthesize**. Register: analyze. inference_depth: deep.

## Known environment constraints (carry into every step)

1. **No `premier` gear.** hyperresearch v0.8.5 exposes no `profile`/`gear`
   subcommand at all. The S0 contract asked for `profile use premier`
   (100–130 sources, doubled depth budget); it cannot be selected. This run
   executes at default breadth. Logged as audit action OA-33. Step 2 should
   compensate by explicitly targeting the upper end of its source range rather
   than assuming the gear widened it.
2. **`[scholar] contact_email` not settable via CLI.** v0.8.5 stores config in
   sqlite and rejects the key. `.hyperresearch/config.toml` was written by hand
   carrying the address, but it is not known to be read. **Unpaywall may be
   skipped rather than enabled** — expect reduced open-access resolution on
   paywalled venue pages. Logged as OA-34.
3. **Python's SSL trust store is broken in this environment** — `urllib` raises
   `CERTIFICATE_VERIFY_FAILED` against every host. `curl` works fine. Any
   fetching that shells out is fine; anything using Python `urllib` directly
   will fail and must be routed through `curl`.
4. **`TodoWrite` unavailable** — see tracking table above.

## Running log

### Step 1 — decompose (done)
- Tier: **full**. Format: **argumentative**. Citations: **wikilink**.
- 32 sub-questions, 18 entities, 6 required H2 headings (one per numbered question, prompt order).
- Coverage matrix: 58 phrases mapped, **zero gaps**.
- Two phrases deliberately split (RLHF vs quantisation diversity loss; NAS-Bench-101 vs 201).
- Two phrases deliberately kept broad against narrowing: "architecture **or program** search" (FunSearch-class counter-evidence qualifies) and "automated design" (venue fit is likely AutoML/agentic/AI-for-science, not a NAS-specific workshop).

### Step 2 — width sweep (in progress)

Search plan written: **68 planned searches**, 17 adversarial (min 5). Academic
API sweep launched across 36 queries × (arXiv + OpenAlex).

**Thesis forming, before sources land.** The positioning risk for this paper is
not that its finding is wrong — it is that the finding is *over-determined*. Four
distinct literatures each independently predict "small quantised instruction-tuned
model emits the same design twenty times":

1. intrinsic self-correction fails without external verification (Huang et al.,
   Kamoi et al., Stechly et al.),
2. RLHF/alignment compresses output diversity,
3. quantisation degrades the tail of the sampling distribution,
4. low-temperature / structured-JSON decoding collapses diversity by itself.

If all four predict the observation, then observing it is confirmatory, not
novel — and the paper's framing ("the LLM encodes a strong narrow prior") is one
of five explanations, not the explanation. **And the audit found a fifth, purely
instrumental one the paper never considers: `sanitize_config` rewrites malformed
output into exactly the reported template.** That is the sharpest thing this
positioning analysis can tell the author, and no external source will surface it —
it comes from the repo audit. The report must connect them.

**Where the novelty probably survives.** The *controlled six-arm comparison* with
a matched budget is likely rarer than the individual claims. EvoPrompting/GENIUS/
LLMatic/GPT-NAS all argue feedback *works*; a registered negative is scarcer.
Expect priority to be partially contested by any 2025-26 ablation that removed
feedback and saw no gain — that is the specific thing to hunt.

**Expected sharpest tension (feeds step 3/4 loci).** Q4's counter-evidence
(FunSearch, AlphaEvolve, Reflexion) all use *executable, external, verifiable*
feedback. This paper uses *scalar validation accuracy* — external and real, but
uninformative about which component to change. The reconciliation is probably
"feedback helps iff it carries credit assignment", which would *bound* the
counter-evidence rather than be defeated by it. That is a defensible thesis and
is stronger than "feedback hurts".

**Estimand tension (Q3).** The audit already shows condition D wins on
best-of-k on both datasets. If reviewers hold that best-of-k is the right
estimand for a fixed-budget search method, the paper's headline inverts. Need
published support for that estimand claim — hunting it under Q3-bestofk.

**Venue-search note (Q5).** The NeurIPS 2026 workshop list is the one part of
this query that cannot be answered from any model's recall — it must be fetched
live, and if the list is not yet published at the time of this run, that is
itself the finding and must be reported as such rather than papered over with
plausible-sounding workshop names. Fabricating a workshop, a page limit, or a
CFP URL would be the single worst failure mode available to this report. If the
2026 list is unavailable, fall back to: (a) the NeurIPS 2025 workshop list as
the structural precedent, clearly labelled as precedent not fact, and (b) the
standing policies (double-blind, non-archival) that hold across editions.

**Redundancy watch for step 2.6.** The self-correction literature is heavily
derivative — dozens of surveys restate Huang et al. 2024 and Kamoi et al. 2024.
Expect a large cluster there and discount it: three surveys citing the same two
primaries is one independent source, not four. The same applies to NAS-evaluation
critique, where most 2023+ papers restate Li & Talwalkar and Yang et al. Coverage
counting must use *independent* sources or Q2 and Q3 will look far better covered
than they are.

### Step 2 — wave 1 dispatched

44 curated sources partitioned into 8 non-overlapping batches; 8
`hyperresearch-fetcher` subagents dispatched in parallel.

Selection was **curated, not bulk**. The raw academic sweep returned 261
candidates across 36 queries, but arXiv's `all:` search degraded badly on long
natural-language phrases — `Q3-bestofk` and `Q4-selfrepair` returned particle-
physics papers, `Q1-agentic` returned thyroid-management guidelines. Rather than
feed that noise to fetchers, candidates were filtered by title-match against the
named canonical works, and the ones the sweep missed (GENIUS, Yang et al., Huang
et al., Stechly, Olausson, Tyen) were resolved directly by arXiv ID and verified
by title before inclusion. Every one of those six came back with the expected
title.

**Three integrity instructions were given to fetchers explicitly**, because they
are the failure modes that would most damage this specific report:

1. **Venue fabrication.** Four batches carry a NeurIPS/OpenReview/AutoML/ICBINB
   URL. Each was told: record exactly what the page says; if the NeurIPS 2026
   workshop list is not yet published, say so — do not substitute plausible
   workshop names, page limits, or CFP URLs.
2. **RZ-NAS may not exist as described.** Two batches were told to *confirm or
   refute* that a paper called RZ-NAS appeared at ICML 2025 with a reflective
   zero-cost strategy, and to report its true authors and venue — not to assume
   the query's characterisation is correct. The query asserts it; that assertion
   is unverified.
3. **GPT-NAS author list.** Batch 4 was told to record arXiv 2305.05351's real
   authors, because the S0 bibliography audit found this exact paper cited in the
   subject manuscript with a **fully fabricated** author list (zero of six
   correct). Confirming the true authors here closes that loop from the other
   direction.

**Source count risk.** 44 selected is below the `full` tier's 45 minimum and well
below the 55–80 target. Wave 2 is therefore expected, not optional. Gaps to fill
after the coverage check: Q3 estimand (best-of-k vs mean), Q3 seeds/statistical
practice, Q2 quantisation-specific diversity loss, and Q1 agentic/multi-agent NAS
2025–26 — all four returned noise in the sweep and none has adequate coverage
yet. The `premier` gear that would have widened this automatically does not exist
in v0.8.5 (OA-33), so the compensation has to be manual.

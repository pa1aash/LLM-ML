# Scaffold — llm-nas-feedback-positioning-7125b1

> PRIVATE PLANNING DOCUMENT. Must not appear anywhere in the final report.

## Run config

| Field | Value |
|---|---|
| `vault_tag` | `llm-nas-feedback-positioning-7125b1` |
| `query_file_path` | `research/query-llm-nas-feedback-positioning-7125b1.md` |
| `modality` | **synthesize** |
| `register` | analyze (explicit in query) |
| `inference_depth` | deep (explicit in query) |
| Source of query | user prompt (no `research/prompt.txt` present) |

## User Prompt (VERBATIM — gospel)

See `research/query-llm-nas-feedback-positioning-7125b1.md`. That file is the
canonical reference for every step and every subagent. Do not paraphrase it.

## Modality classification rationale

**synthesize.** The query does not ask for an enumeration of entities
(`collect`) and is not primarily a forecast. It asks six questions and demands
*"commit to a position on each"* — a defended thesis backed by evidence chains.
Question FIVE (venue mapping with per-workshop fields and a defended ranking)
carries a `compare` sub-structure and needs proportionate per-entity depth plus
an explicit recommendation; that is a section-level obligation inside an
otherwise `synthesize` report, not a reclassification of the whole run.

## Tier rationale

**`pipeline_tier: full`. `response_format: argumentative`.
`citation_style: wikilink`.**

Classified `full` because the query is a contested-evidence positioning problem,
not a lookup: it poses six numbered questions, demands an explicit committed
position on each, requires priority to be established against seven named bodies
of prior work, and instructs that adversarial searches be run for criticism and
failed replications of *every position adopted*. Novelty and counter-evidence
(Q1, Q4) are directly adversarial — the answer depends on finding the strongest
case against the subject paper, which is exactly what the depth-investigation and
critic layers exist to force.

`argumentative` because the deliverable is a defended thesis with evidence
chains, culminating in Q6's demand for a single strongest defensible thesis, an
explicit claim to abandon, and one prioritised experiment. `wikilink` because no
`research/wrapper_contract.json` exists and this is vault-internal work feeding
the G1 gate.

Question FIVE is the one part that behaves like `structured` — a per-workshop
field set plus a ranking. It is handled as a comparison section inside the
argumentative report, not as a tier change.

## Wrapper requirements

None. This is an unwrapped run:

- No `research/prompt.txt`.
- No `research/wrapper_contract.json`.
- Save path: pipeline default — `research/notes/final_report_llm-nas-feedback-positioning-7125b1.md`.
- Citation format: pipeline default.
- Terminal sections: pipeline default.

## Named prior work the query requires priority to be established against

Question ONE names these explicitly; step 2's search plan must cover each:

- EvoPrompting
- GENIUS / "Can GPT-4 Perform Neural Architecture Search?"
- LLMatic
- GPT-NAS
- RZ-NAS (ICML 2025, reflective zero-cost strategy)
- Agentic and multi-agent NAS, 2025–2026
- Any LLM-NAS ablation reporting a null or negative effect of feedback

Question TWO additionally requires rival-explanation coverage: mode collapse,
output-diversity loss under RLHF, quantisation effects on diversity, and
decoding-temperature effects.

Question THREE requires the NAS-evaluation critique literature: Li & Talwalkar,
Yang et al., and the tabular-benchmark family (NAS-Bench-101/201, NATS-Bench,
NAS-Bench-Suite-Zero).

## Repository context feeding this run

This positioning analysis serves a specific manuscript, audited in the same
session. Findings from `audit/` that bear directly on the six questions:

- The paper's evidence base has **no stored experimental artifacts**; 26% of
  headline claims are ORPHAN (`audit/CLAIM_TRACE.md`).
- The reported "single template" (standard 3×3 / ReLU / BatchNorm) is **exactly
  the fallback of a sanitiser applied to the LLM arms only** — an unexcluded
  instrumental rival to the mode-collapse explanation the query asks about
  (`audit/FORENSICS.md` F2).
- **Condition D — the structured-feedback arm the paper says is harmed —
  produces the best single architecture on both datasets.** Under
  expected-best-of-*k*, the estimand question THREE raises, the headline
  inverts (`audit/CLAIM_TRACE.md` §5.3).
- Proposals in the feedback arms are **sequentially dependent**, while the tests
  applied assume independence — precisely the issue question THREE names
  (`audit/FORENSICS.md` F3).

These are context, not conclusions. The pipeline must reach its own positions
from fetched sources.

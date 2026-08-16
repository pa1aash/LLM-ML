# HR_PARTIAL — manifest

Read-only extraction of the hyperresearch positioning run for
`llm-nas-feedback-positioning-7125b1`. **No completed final report exists.** This
directory holds every artifact the run actually produced.

## Why there is no report

The V8 16-step pipeline is **not implemented in the CLI**. `hyperresearch v0.8.5`
exposes no `run`, `runs`, `report`, or `resume` command, and its database schema
has no `runs`, `reports`, `steps`, or `queries` table — only
`notes / note_content / sources / tags / links / assets / embeddings / aliases`.
The pipeline lives entirely in the agent skill files
(`hyperresearch-1-decompose` … `-16-readability-audit`) and is driven by the
orchestrating agent, so "run state" is a property of the conversation, not of
any CLI store.

The run reached **step 2 of 16** and stopped there. Steps 3–16 never executed, so
their artifacts were never written.

## Step-by-step: what produced output

| Step | Canonical artifact | Status |
|---|---|---|
| bootstrap | `research/query-<tag>.md`, `research/scaffold.md` | ✅ produced |
| 1 decompose | `research/prompt-decomposition.json`, `research/temp/coverage-matrix.md` | ✅ produced |
| 2 width-sweep | 78 vault notes + 65 `claims-*.json` | ✅ produced |
| 3 contradiction-graph | `research/temp/contradiction-graph.json` | ❌ absent |
| 4 loci-analysis | `research/loci.json` | ❌ absent |
| 5 depth-investigation | notes with `type: interim` | ❌ absent (DB confirms **0** interim notes) |
| 6 cross-locus-reconcile | `research/comparisons.md` | ❌ absent |
| 7 source-tensions | `research/temp/source-tensions.json` | ❌ absent |
| 8 corpus-critic | `research/corpus-critic-gaps.json` | ❌ absent |
| 9 evidence-digest | `research/temp/evidence-digest.md` | ❌ absent |
| 10 triple-draft | `research/temp/draft-{a,b,c}.md` | ❌ absent |
| 11 synthesize | `research/notes/final_report_<tag>.md` | ❌ absent |
| 12 critics | `research/critic-findings-*.json` | ❌ absent |
| 13 gap-fetch | `research/temp/post-critic-fetch-log.md` | ❌ absent |
| 14 patcher | `research/patch-log.json` | ❌ absent |
| 15 polish | `research/polish-log.json` | ❌ absent |
| 16 readability | `research/readability-recommendations.json` | ❌ absent |

## Contents

The 78 fetched source notes are **not duplicated** into this directory; they are
already version-controlled at `research/notes/`. Copying them would add 2.4 MB of
redundancy. This directory holds the run-state artifacts only.

```
research/query-llm-nas-feedback-positioning-7125b1.md   canonical query (verbatim)
research/scaffold.md                                    run config, modality, tier rationale
research/prompt-decomposition.json                      32 sub-questions, 18 entities, 6 headings
research/temp/coverage-matrix.md                        58 query phrases mapped, 0 gaps
research/temp/search-plan.md                            68 planned searches, 3 lenses
research/temp/orchestrator-notes.md                     running log of all 8 fetcher returns
research/temp/venue-findings-interim.md                 NeurIPS 2026 workshop analysis + ranking
research/temp/step2-findings-summary.md                 preliminary answers to all six questions
research/temp/claims-*.json                             65 files, structured claims w/ quotes
(notes NOT duplicated here — see ../../research/notes/, 78 fetched sources)
config.toml                                             hand-written; see caveat below
```

## Substantive output that does exist

Although no pipeline-synthesised report exists, two hand-written analyst
artifacts in `research/temp/` do answer the brief's six questions at step-2
evidence level, grounded in fetched primary sources:

- **`step2-findings-summary.md`** — preliminary positions on all six questions,
  including the enumerated NAS-methodology failure table.
- **`venue-findings-interim.md`** — the NeurIPS 2026 workshop landscape with a
  defended ranking and per-workshop fields where CFPs were fetched.

These are **not** critic-reviewed pipeline output. They carry no adversarial
stress-testing from steps 12–14.

## Caveats recorded during the run

- `.hyperresearch/config.toml` was written **by hand**. v0.8.5 stores live config
  in sqlite and rejects `config set scholar.contact_email` as an unknown key, so
  the Unpaywall contact address may not be read at all.
- v0.8.5 has **no `profile`/`gear` subcommand**, so the contracted `premier` gear
  (100–130 sources) could not be selected. The run executed at manually curated
  breadth: 44 seed URLs → 78 notes after citation chasing.
- `arxiv.org/pdf/...` extraction fails environment-wide with
  `JUNK_CONTENT: Binary PDF garbage`. Fetchers that recovered full text did so
  via `curl` + Read, or via `arxiv.org/html/...`.

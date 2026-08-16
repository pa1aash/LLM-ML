# STATE

**Project:** *When Does Feedback Help? A Controlled Study of LLM-Guided Neural
Architecture Design*
**Target:** a NeurIPS 2026 workshop (venue undecided — see `VENUE.md`)
**Ladder:** S0 ground truth → S1 position → S2 claim surgery → S3 preflight →
S4 build → S5 results-file layer → S6 write → S7 referee

---

## Current stage: **S1b — positioning, in progress**

S0 audit complete (G0 unsigned). S1 Block A complete (corpus repaired).
S1a Block B complete (coverage audit + Q2/Q3 gap-fill). S1b: venue sweep in
flight; pipeline steps 3-9 not started.

---

## Done

- **Git bootstrap.** Repository initialised at `/Users/palaash/Desktop/LLM-ML`
  with local identity `Palaash Gang <palaashgang@gmail.com>`. `main` branch.
  Note: `$HOME` is itself a git repo with no commits — every git write in this
  session asserted `rev-parse --show-toplevel` first.
- **Pre-commit hook installed** (`.git/hooks/pre-commit`): rejects any commit
  made outside this repository, and any staged addition that names an AI
  assistant or adds a co-author trailer. Self-tested against both rules.
- **`.gitignore` extended** (append-only) and `docs/` excluded by operator
  decision.
- **Secret scan clean.** No keys, tokens, or private keys anywhere.
  `credentials/` is empty. `.remember/` is self-ignored.
- **Cloud host IP redacted** from `docs/methodology.md` and
  `docs/research-state.md` (operator-authorised).
- **README rewritten** to a generic public surface — no title, abstract, or
  results.
- **First commit created** (37 files).
- **Full audit written**: `audit/REPO_INVENTORY.json`, `audit/CONTEXT_PACK.md`,
  `audit/CLAIM_TRACE.md`, `audit/FORENSICS.md`, `audit/BIB_AUDIT.md`,
  `audit/references_verified.bib`, `audit/OPEN_ACTIONS.md`.
- **Scaffolding created**: `STATE.md`, `GATES.md`, `VENUE.md`.

## The three findings that shape everything downstream

1. **The repository contains no experimental data.** 0 RAW, 0 SPEC, 0 TRANSCRIPT
   across all 24 condition × dataset × seed cells. 26% of headline claims are
   ORPHAN, including `parameter std = 0K` and the Bonferroni threshold.
2. **`sanitize_config` silently collapses malformed LLM output to
   `standard_3x3 / relu / batchnorm`** — exactly the "narrow prior" template the
   paper reports — and runs on the LLM arms only. The central finding has an
   unexcluded instrumental explanation.
3. **Condition D holds the best single architecture on both datasets** (91.4 /
   66.9) while the paper's headline is that structured feedback hurts. Under
   expected-best-of-*k*, the standard estimand for a fixed search budget, the
   conclusion inverts.

## ⏰ Time-critical finding (S1, from the live NeurIPS page)

**The NeurIPS 2026 workshop list is published and the suggested submission date
is 2026-08-29 — 13 days from today.** 102 workshops accepted (48 Sydney /
28 Paris / 26 Atlanta); workshops run Dec 11–13, 2026. Source:
`research/temp/venue-findings-interim.md`, fetched from the official
announcement of 2026-08-10.

Three workshops are a direct topical fit — **Self-Evolving Diversity-Driven
Search for Robust AI Systems** (Sydney) is the closest match found, with
**Workshop for Autonomous Machine Learning Research** (Sydney) and **SLM-Agents**
(Paris, explicitly small language models) behind it. Note that **ICBINB, the
canonical negative-results venue, is scoped to "Failure Modes of AI in Biology"
this year and is NOT a fit** — an assumption that would have been wrong if
answered from memory.

A 13-day runway cannot rebuild the experiment. It may suffice for claim surgery
**iff** OA-1 resolves favourably.

## Open

- **G0 awaiting operator signature.** Recommendation in
  `audit/SESSION_1_REPORT.md` §8.
- **32 open actions**, `audit/OPEN_ACTIONS.md`. Five are blocking; **OA-1 (does
  the raw data still exist anywhere?) is the highest-value question in the
  project** — its answer determines whether S2 is claim surgery or a rebuild.
- Block 8 positioning analysis (novelty, mechanism literature, methodology
  standards, counter-evidence, venue map, framing) — feeds G1.

## Blocked

- **Push to `origin`.** GitHub rejects with `GH007: your push would publish a
  private email address`. The authorship contract mandates
  `palaashgang@gmail.com`, so the resolution is the operator disabling "Block
  command line pushes that expose my email" at github.com/settings/emails.
  Elected but not yet done. Commits exist locally with correct authorship;
  nothing is lost, the push simply has not landed.

## Not done, deliberately

- No experiment was re-run, no model retrained, no ML dependency installed.
- Nothing under `paper/`, `src/`, `scripts/`, `logs/` or `archive/` was modified.
  The only edits outside `audit/` and the scaffolding were the operator-approved
  IP redaction in `docs/` and the README rewrite.

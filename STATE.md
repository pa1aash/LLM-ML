# STATE

**Project:** *When Does Feedback Help? A Controlled Study of LLM-Guided Neural
Architecture Design*
**Target:** a NeurIPS 2026 workshop (venue undecided — see `VENUE.md`)
**Ladder:** S0 ground truth → S1 position → S2 claim surgery → S3 preflight →
S4 build → S5 results-file layer → S6 write → S7 referee

---

## Current stage: **S0 — ground truth**

Audit complete. **G0 is unsigned.**

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

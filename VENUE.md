# VENUE

## Target — SELECTED 2026-08-17

### **AI for Meta-Science (NeurIPS 2026) — position track, 8 pages**

Selected at S2 on operator authorisation, recorded against G1. Source of every
field below: `research/notes/ai-for-meta-science-neurips-2026-workshop.md`,
extracted to `research/temp/venue-candidates.md`. `NOT STATED` means the fetched
CFP page is silent — no value is inferred or carried across from general NeurIPS
policy.

| Field | Value |
|---|---|
| **Track** | Position paper |
| **Page limit** | **8 pages** (position). Technical track is 4. Excludes references; appendix unlimited. |
| **Template** | **NeurIPS 2026 LaTeX template**, footnote changed to `Submitted to AI for Meta-Science workshop (NeurIPS 2026).` |
| **Checklist** | Not required |
| **Portal** | OpenReview |
| **Deadline** | **2026-08-29 AoE** |
| **Notification** | 2026-09-29 |
| **Anonymity** | **NOT STATED** — see the open item below |
| **Archival** | **NOT STATED** |
| **Dual submission** | Previously published relevant work welcome for presentation |
| **Reviewing obligation** | Recruiting reviewers for both tracks; ≤3 papers per reviewer |
| **Negative results** | No explicit statement. Scope names reproducibility checking and research evaluation. |

**Why it fits.** The workshop's scope is that research production has outpaced
quality control — reproducibility norms, evaluation, publication criteria. The
paper's thesis (`EXPERIMENT_PLAN_R6.md` §1.1) is that a reported effect in a
subfield is an artifact of its measurement apparatus. That is a meta-science
claim with an ML instantiation, which is the workshop's premise rather than an
awkward fit to it. The position track's 8 pages also accommodates the three
experiments plus the mandatory-caveat blocks (§4.4), which 4 pages would not.

**Open, and must be resolved before submission:**
- **Anonymity is NOT STATED on the fetched CFP.** Treat as **double-blind** —
  the conservative default, and the standing G-anon rule below assumes it. Verify
  against the OpenReview venue page at S6 and record the answer here.
- **Archival status is NOT STATED.** Verify at S6. If archival, re-check the
  dual-submission position before any later extended version is planned.

### Fallback — **AI for Science: Verification in the Age of AI Scientists (NeurIPS 2026)**

| Field | Value |
|---|---|
| **Track** | **B — Position** ("clear, contestable" claims) |
| **Page limit** | 4–8 pages; unlimited references and appendices |
| **Template** | NeurIPS 2026 LaTeX template, footnote `Submitted to the AI for Science workshop (NeurIPS 2026).` |
| **Checklist** | Explicitly not required |
| **Anonymity** | **Explicitly double-blind** |
| **Archival** | **Explicitly non-archival** |
| **Portal / deadline** | OpenReview, 2026-08-29 AoE |
| **Dual submission** | No ban; welcomes original unpublished and recently published work |

The fallback states anonymity and archival status explicitly, where the primary
does not. It is a cleaner formal fit for a verification-flavoured framing, and a
weaker fit for the meta-science framing the paper actually takes. **Track C
(Verifier Systems) requires released code and artifacts** and is not a candidate.

### Style file — hard requirement at S6

**`neurips_2026.sty` must be fetched and byte-verified from two independent
mirrors at S6.** `media.neurips.cc` has previously returned 404/403. Record both
source URLs and the SHA-256 of each download in this file; they must match. Do
not build against a style file obtained from a single source, and do not
substitute a prior year's file.

The manuscript currently uses `icml2025.sty`. That is now definitively wrong and
is replaced at S6.

### Page-budget reconciliation — closes OA-26

Three conflicting budgets existed in the repository: the former README targeted a
4-page ICML workshop, `paper/main.tex:12` targets 8 pages, and `paper/main.pdf`
builds to 10. **The binding number is 8 pages excluding references**, per the
selected venue's position track. `main.tex` happens to already target 8; the
built PDF is 2 pages over and must be cut, not respaced.

### Superseded targets found in the repository

Recorded so the conflict is not silently reconciled:

| Source | Target claimed |
|---|---|
| Former `README.md` (rewritten in S0) | AI-Assisted Research Workflows @ ICML 2026 — 4 pages, ICML format |
| `paper/main.tex:12` comment | "Compact spacing for 8-page fit" |
| `paper/main.pdf` as built | **10 pages** |

Three different page budgets. **Reconciled above: 8 pages excluding references.
OA-26 is closed.** The `icml2025.sty` the manuscript currently uses is replaced
by `neurips_2026.sty` at S6.

---

## Properties of NeurIPS workshops

- **Double-blind.** Submissions are anonymous. The manuscript already uses
  "Anonymous Authors / Anonymous Institution"
  ([main.tex:35-36](paper/main.tex#L35)).
- **Non-archival.** NeurIPS workshops do not publish formal proceedings, so a
  workshop paper does not preclude later submission of an extended version to an
  archival venue. Verify per workshop — a minority run archival tracks or opt-in
  proceedings.
- Page limits, deadlines and anonymity policies vary **per workshop** and are set
  in each workshop's own call for papers. Nothing here substitutes for reading
  the specific CFP.

---

## Standing rule: G-anon

**Before any submission, all four must hold and be verified:**

1. **The repository goes private.** It is public during development. `credentials/`
   is empty and `docs/` is gitignored, but the repo still exposes the full source,
   the manuscript, and this audit.
2. **The paper carries no repository URL.** No GitHub link, no anonymised-repo
   link that resolves to an identifiable account, no author-identifying path in a
   figure or listing.
3. **PDF metadata is scrubbed.** `/Title` and `/Author` are currently empty in
   `main.pdf` — good, but re-verify after every rebuild, and check
   `/Producer`, `/Creator` and XMP for host or username leakage. Note that
   `logs/main.log` contains the path `C:/Users/nitua/...`; confirm no such path
   reaches the compiled PDF.
4. **Self-citations are audited.** No citation phrased so as to identify the
   authors ("in our previous work", "our earlier study"). `references.bib` shows
   no self-citation at present — re-check after the bibliography is replaced with
   `audit/references_verified.bib`.

G-anon is verified at **G7** and re-verified immediately before upload.

---

## Positioning constraints already known from the audit

These bear directly on which workshop is a fit, and are inputs to Block 8:

- The result is a **controlled negative/null finding** about LLM self-refinement
  in automated design. Venues differ sharply in appetite for negative results.
- The evidence base has **no stored artifacts** (see `audit/CLAIM_TRACE.md`), so
  any workshop with an artifact or reproducibility requirement is out of reach
  until OA-1 is resolved.
- The search space is a **custom CNN space, not a tabular benchmark**. The paper
  itself concedes NAS-Bench-201 as the natural next step
  ([main.tex:757](paper/main.tex#L757)). Reviewers drawing on the NAS-evaluation
  critique literature (Li & Talwalkar; Yang et al.) will press on this.
- **Condition D holds the best architecture on both datasets**
  (`audit/CLAIM_TRACE.md` §5.3). Any venue whose reviewers think in terms of
  expected-best-of-*k* under a fixed budget will read the headline as inverted.

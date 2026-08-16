# VENUE

## Target

**A NeurIPS 2026 workshop. Specific workshop undecided.**

Workshop selection is the deliverable of Block 8's positioning analysis and is
gated at **G1**. Until G1 is signed, no venue-specific formatting decision is
final.

### Superseded targets found in the repository

Recorded so the conflict is not silently reconciled:

| Source | Target claimed |
|---|---|
| Former `README.md` (rewritten in S0) | AI-Assisted Research Workflows @ ICML 2026 — 4 pages, ICML format |
| `paper/main.tex:12` comment | "Compact spacing for 8-page fit" |
| `paper/main.pdf` as built | **10 pages** |

Three different page budgets. This must be reconciled against the chosen
workshop's actual limit (open action **OA-26**).

The manuscript currently uses `icml2025.sty`. A NeurIPS workshop will almost
certainly require the NeurIPS style; treat the current formatting as
provisional.

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

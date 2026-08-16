---
title: TAE | NeurIPS 2026 Workshop - AI Evaluation
id: tae-neurips-2026-workshop-ai-evaluation-2
tags:
- llm-nas-feedback-positioning-7125b1
- venue-candidate
- neurips-2026-workshop
- cfp-details
- evaluation-methodology
created: '2026-08-16T16:52:23.151573Z'
updated: '2026-08-16T16:53:43.676919Z'
source: https://tai-eval.github.io/cfp
source_domain: tai-eval.github.io
fetched_at: '2026-08-16T16:52:23.151273Z'
fetch_provider: builtin
status: draft
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'TAE dedicated /cfp subpage (supplements the thin main-page note [[tae-neurips-2026-workshop-ai-evaluation]])
  -- resolves all previously-missing fields. Format: full papers up to 8 pages excluding
  references/appendices, appendices allowed with no page limit (reviewers not required
  to read them), NeurIPS 2026 LaTeX template using \usepackage[dblblindworkshop]{neurips_2026}
  for submission and \usepackage[dblblindworkshop, final]{neurips_2026} for camera-ready,
  plus a required \workshoptitle{} field. Anonymity: explicitly double-blind (''please
  ensure that all papers are appropriately anonymized''). Archival status: explicitly
  non-archival, in-person poster session for all accepted papers. Submission via single
  PDF through OpenReview; each submission gets up to three reviews from the program
  committee; organizers recuse from conflicted submissions. Same key dates as the
  main page (submission Aug 29, 2026 AoE; review deadline Sep 14; notification Sep
  22; program posted Sep 27; workshop Dec 11 or 12). Restates full topic list verbatim
  including the ''uncertainty and robustness'' bullet on seeds/sampling variation/random
  seeds that closely matches the target paper''s Q3 methodology concerns. No explicit
  statement on negative results specifically, but the workshop''s entire premise (''evaluation
  protocols themselves, not only the models being evaluated'') is methodologically
  hospitable to a null-result submission framed as an evaluation-methodology critique.'
---

*Suggested by [[tae-neurips-2026-workshop-ai-evaluation]] — TAE main page lacked page limit/format/anonymity/archival fields; fetching dedicated CFP subpage*

TAE | NeurIPS 2026 Workshop - AI Evaluation
NeurIPS 2026, Sydney, Australia, December 11 or 12, 2026
Call for Papers
Modern AI systems are judged through benchmarks, aggregate scores, and public leaderboards, but these signals are fragile: performance can drop on newly collected test sets, repeated benchmark use can lead to overfitting, rankings can shift under small perturbations, variance is often underreported, and leakage or contamination can distort comparisons. Audits also find weak documentation, reproducibility, statistical reporting, and lifecycle practice, while leaderboards can reward selective disclosure and benchmark-specific optimization.
The core gap is methodological. Many evaluation claims do not state what is measured, how it becomes a protocol, or what inference the protocol supports. We invite submissions that study evaluation protocols themselves, not only the models being evaluated.
We invite submissions on topics including, but not limited to:
Uncertainty and robustness:
How stable are evaluation conclusions under sampling variation, calibration error, random seeds, data splits, prompts, metrics, evaluator choices, noisy or delayed feedback, tail risk, and worst-case behavior?
Benchmark and leaderboard auditing:
How do benchmark reuse, contamination, leakage, documentation gaps, lifecycle practice, public incentives, and benchmark-specific optimization affect the trustworthiness of evaluation claims?
Black-box auditing:
How can AI systems be audited when model internals, training data, or evaluation pipelines are inaccessible, and what behavioral tests, probes, or external evidence can reveal hidden failure modes, contamination, or systematic risk?
Measurement and causal validity:
What construct is an evaluation protocol intended to measure, what ground truth does it rely on, and what causal, structural, or statistical assumptions connect the protocol to the claim?
Stress tests and judge reliability:
How should evaluations assess protocol robustness, ambiguous labels, human-, crowd-, and model-judge reliability, and failure modes in evaluation pipelines?
Domain coverage and representation:
How do imbalances in benchmark suites, such as extensive coverage of coding, mathematics, ethics, and logical reasoning but limited or absent coverage of banking and other regulatory-compliance settings, non-Western cultural contexts, and other underserved domains, affect the validity and generalizability of evaluation claims? How should evaluation portfolios be designed, weighted, and updated to provide representative cross-domain coverage and expose systematic blind spots?
Application-domain evaluation:
How should evaluation protocols be designed and audited for domain-specific settings such as medicine and healthcare, finance, science, robotics, AI agents, cybersecurity, education, public-sector decision-making, and other high-stakes applications?
Deployment risk and governance:
When do offline metrics support real-world model selection, safety claims, monitoring, and deployment decisions, and what decision-aware metrics, fairness–accuracy–risk trade-offs, reporting checklists, auditing guidelines, and deployment criteria are needed?
Important Dates (Indicative)
Paper submission opens:
July 30, 2026
Paper submission deadline:
August 29, 2026 (AoE)
Review deadline:
September 14, 2026 (AoE)
Author notification:
September 22, 2026 (AoE)
Final program posted:
September 27, 2026
Workshop:
December 11 or 12, 2026
Submission Requirements
Submissions should be anonymized and prepared using the
official NeurIPS 2026 LaTeX template
.
Please use
\usepackage[dblblindworkshop]{neurips_2026}
for submission. For accepted camera-ready versions, please use
\usepackage[dblblindworkshop, final]{neurips_2026}
. The NeurIPS 2026 workshop template requires both
\title{}
and
\workshoptitle{}
; please set
\workshoptitle{TAE (Trust-AI-Eval): Can We Trust AI Evaluation?}
.
Full papers:
up to 8 pages, excluding references and appendices.
Appendices:
allowed, with no page limit, but reviewers are not required to read appendices.
All submissions must be submitted as a single PDF through OpenReview. The review process is double-blind, so please ensure that all papers are appropriately anonymized.
All accepted papers will be presented in an in-person poster session. Accepted papers are to be considered
non-archival
.
Submission site:
OpenReview
. If you have not already done so, we recommend creating an OpenReview profile as soon as possible, as new profile creation can take up to two weeks in some cases.
Reviewing Process
We are committed to a rigorous and fair evaluation of all submissions. Reviewers must declare conflicts before review assignments are made. Each submission will receive up to three reviews from the program committee. Final decisions will be made by the organizing team, based on the reviews. Organizers will recuse themselves from any submission with which they have a conflict, as identified by OpenReview.
Please email any inquiries to
aiteval2026@gmail.com
.
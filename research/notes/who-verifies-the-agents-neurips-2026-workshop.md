---
title: Who Verifies the Agents? · NeurIPS 2026 Workshop
id: who-verifies-the-agents-neurips-2026-workshop
tags:
- llm-nas-feedback-positioning-7125b1
- neurips-2026-workshop
- venue-candidate
- cfp-details
- agent-verification
created: '2026-08-16T15:51:41.045798Z'
updated: '2026-08-16T15:54:04.987999Z'
source: https://verify-agents-workshop.github.io/
source_domain: verify-agents-workshop.github.io
fetched_at: '2026-08-16T15:51:41.043198Z'
fetch_provider: builtin
status: draft
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Who Verifies the Agents? Toward Reliable Agent Development (NeurIPS 2026,
  Sydney, Dec 11 or 12) frames verification as ''the bottleneck between fragile prototypes
  and scalable, reliable agent systems'' and asks, of any agent change, ''did it actually
  get better?'' Three topic pillars: (1) Safety/Robustness of Verification, (2) Environment-Grounded
  Verification and Simulators -- explicitly listing ''Evolutionary and search-based
  methods for environment-driven agent optimization'' and ''Automated agent design,
  prompt optimization, and scaffold search with verifiable feedback'' -- and (3) Diverse/Heterogeneous
  Verifiable Signals, listing ''Beyond scalar rewards: holistic evaluation of agentic
  behavior'' and ''Reflective and self-improving verification (agents that verify
  other agents).'' A cross-cutting topic is explicitly ''Self-evolving agents: stable
  improvement without collapse or reward hacking'' and ''Evaluation of agent-generated
  designs vs. human-engineered systems'' -- both near-exact matches to the target
  paper''s thesis (an agent''s self-refinement loop failing to improve, collapsing
  to one design). Format: papers 4-9 pages excluding references/appendices, NeurIPS
  2026 template; demo papers <=4 pages. Double-blind review; non-archival (OpenReview
  posting, no formal proceedings); dual-submission-friendly (accepts work under review
  or recently published elsewhere). Submission deadline Aug 29, 2026; review period
  Aug 30-Sep 12; AC discussion Sep 13-23; notification Sep 29. No explicit position
  statement on negative results, but the framing implicitly wants exactly this kind
  of result (a case where an update did NOT make an agent better).'
---

*Suggested by [[announcing-the-neurips-2026-workshops-neurips-blog]] — NeurIPS 2026 Who Verifies the Agents workshop - maps to intrinsic self-correction fails without external verification thesis*

Who Verifies the Agents? · NeurIPS 2026 Workshop
NeurIPS 2026 Workshop
Who Verifies
the Agents?
Toward Reliable Agent Development
Verification is the bottleneck between fragile prototypes and scalable, reliable agent systems. This workshop convenes researchers and practitioners to make verification a first-class discipline.
Dec 11 or 12, 2026
Sydney, Australia
Call for Papers
Submit on OpenReview
Submissions due Aug 29, 2026 (AoE)
Overview
Agents that reason, plan, and act in open-ended environments are advancing at a remarkable pace. Yet a basic question has become surprisingly hard to answer: when we update an agent's prompt, add a new tool, or change its reasoning strategy,
did it actually get better?
Answering that question is
verification
. Today it works well only where ground truth is clear, such as formal mathematics, competitive programming, and software tests. For general agentic tasks, verification signals remain shallow and noisy: improvements plateau, regressions slip through silently, and development turns into guesswork.
This workshop treats verification as a
first-class research problem
. We bring together researchers and practitioners working on robust verifiers, environment-grounded evaluation, and richer verification signals to lay the foundations of reliable agent development.
Confirmed Speakers & Panelists
Pin-Yu Chen
IBM
Trusted AI at IBM Research; PI at the MIT–IBM Watson AI Lab.
Azalia Mirhoseini
Stanford · Ricursive Intelligence
Scalable, self-improving AI; AlphaChip and Mixture-of-Experts.
Seshendra Nalla
Datadog
VP of Observability Data Platform; contributor to BitsEvolve.
Dhaval Patel
IBM Research
Time-series foundation models and LLM agents at IBM T.J. Watson.
Ion Stoica
UC Berkeley · Anyscale · Databricks
Systems for AI at Berkeley: Ray, Spark, vLLM, Chatbot Arena.
Yu Su
Ohio State · NeoCognition
Agent reliability and evaluation: Mind2Web, MMMU, SeeAct.
Call for Papers
Topics of Interest
We invite submissions across three core pillars, as well as topics at their intersection:
Pillar 1: Safety and Robustness of Verification
Robust verifiers that prevent reward hacking and specification gaming
Adversarial robustness of verifiers and red-teaming of evaluation harnesses
Alignment-aware verification: ensuring verifiers remain faithful as agents evolve
Pillar 2: Environment-Grounded Verification and Simulators
Faithful simulators as verification infrastructure for open-ended tasks
Multi-agent and self-optimizing systems for environment-grounded evaluation
Measuring agents in production: observability, monitoring, and runtime verification
Evolutionary and search-based methods for environment-driven agent optimization
Benchmarks and environment design that stress-test verification methods
Pillar 3: Diverse and Heterogeneous Verifiable Signals
Composing heterogeneous signals (user experience, cost/latency, calibration, multimodality) into reliable verification metrics
Beyond scalar rewards: holistic evaluation of agentic behavior
Human-in-the-loop verification and human–AI collaborative evaluation
Reflective and self-improving verification (agents that verify other agents)
Automated agent design, prompt optimization, and scaffold search with verifiable feedback
Formal verification of agent-generated artifacts, including the use of proof assistants and verification languages (e.g., Dafny, Rocq, and Lean)
Cross-Cutting Topics
Verification for meta-agents and Agent4Agent systems (agents that design, optimize, or evaluate other agents)
Self-evolving agents: stable improvement without collapse or reward hacking
Evaluation of agent-generated designs vs. human-engineered systems
Scalable oversight and verification for long-horizon, multi-step agent behavior
Cognitive and neuroscience-inspired verification frameworks
Submission Guidelines
Format:
Papers should be between 4 to 9 pages (excluding references and appendices), using the
NeurIPS 2026 template
. We also welcome demo papers, which should be no more than 4 pages.
Dual submission policy:
We welcome work that is under review or has been recently published at other venues.
Review:
Reviews will be double blind. Authors of submitted papers may be asked to contribute reviews.
Presentation:
Accepted papers will be presented as posters; select papers will be chosen for oral presentations or lightning talks.
Non-archival:
The workshop is non-archival; accepted papers will be made available on OpenReview but do not constitute formal proceedings.
Submissions and reviewing are handled through
OpenReview
.
Call for Reviewers
We are assembling the program committee and welcome researchers and practitioners working on agents, evaluation, and verification.
Guidelines
Scope:
Evaluate submissions based on their contributions to the verification, evaluation, reliability, robustness, and safety of AI agents. We welcome work on topics including safety, simulators, heterogeneous signals, meta-agents, benchmarks, and evaluation methodologies.
Reviewer Responsibilities:
Provide constructive feedback on assigned submissions. Maintain confidentiality throughout the review process and declare any conflicts of interest.
Area Chair (AC) Responsibilities:
ACs are expected to oversee assigned reviews, ensure reviews are fair and constructive, and submit final recommendations of assigned submissions.
Sign up as a reviewer →
Important Dates
Submission deadline
August 29, 2026
Review period
Aug 30 – Sep 12, 2026
AC discussion period
Sep 13 – Sep 23, 2026
Author notification
September 29, 2026
Workshop day
Dec 11 or 12, 2026
The exact workshop day (Friday, Dec 11 or Saturday, Dec 12) will be confirmed once assigned by NeurIPS. All deadlines are 23:59 Anywhere on Earth (AoE) unless otherwise noted.
Organizing Committee
Ahmad Beirami
Fidian
Mert Cemri
UC Berkeley
Zhang-Wei Hong
MIT–IBM Watson AI Lab
Hung Le
Fidian
Ninareh Mehrabi
Meta Superintelligence Labs
Melissa Pan
UC Berkeley
Dilara Soylu
Stanford University
No mystery is solved until it's verified. 🐾
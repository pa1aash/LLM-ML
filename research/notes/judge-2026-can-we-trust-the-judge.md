---
title: JUDGe 2026 — Can We Trust the Judge?
id: judge-2026-can-we-trust-the-judge
tags:
- llm-nas-feedback-positioning-7125b1
created: '2026-08-16T15:51:46.588897Z'
source: https://judge2026.github.io
source_domain: judge2026.github.io
fetched_at: '2026-08-16T15:51:46.586973Z'
fetch_provider: builtin
status: draft
type: note
tier: unknown
content_type: unknown
deprecated: false
---

*Suggested by [[announcing-the-neurips-2026-workshops-neurips-blog]] — NeurIPS 2026 JUDGe workshop on Reliable Evaluation for LMs - evaluation methodology angle*

JUDGe 2026 — Can We Trust the Judge?
NeurIPS 2026 · Atlanta · Dec 12–13
JUDGe
Can We Trust
the
Judge?
"Rigorous evaluation is the backbone of trustworthy AI — let's scrutinize the scrutinizers."
A full-day workshop on building reliable, valid, and robust LLM-based evaluators. We bring together NLP researchers, ML systems builders, safety scientists, and industry practitioners around a single foundational question: how do we know whether an LLM evaluator is actually measuring what we intend it to measure?
Conference
NeurIPS 2026
Workshop Date
Dec 12–13, 2026
Venue
Atlanta, Georgia
Submission Deadline
Aug 29, 2026 AoE
LLM
OUTPUT
v_n+1
⚖
LLM JUDGE
validity in context?
TRAINING
SIGNAL / GATE
downstream
feedback loop — bias compounds
FAILURE FACETS
⟶ Surface vs. semantic sensitivity
⟶ Criteria drift
⟶ Positional & ordering bias
⟶ Sycophancy & self-preference
⟶ Reasoning chain validity
⟶ Safety-relevant meaning
⟶ Inter-judge consistency
CAN WE TRUST THE JUDGE? · NEURIPS 2026 · ATLANTA
About the Workshop
Why JUDGe?
Evaluation validity is not a property of a judge in isolation — it is a property of a judge
in a system
. A well-calibrated evaluator can fail systematically when deployed in a pipeline where its outputs gate safety decisions, feed back into training, or depend on context it was never designed to handle. The field has treated evaluation as a measurement problem — how accurate is the judge? — when the harder question is infrastructural: how does a judge's error profile interact with what is upstream and downstream of it, and what happens downstream when it fails?
JUDGe is the first NeurIPS workshop to take evaluator reliability and validity seriously as a
systems
problem. Judges embedded in RLHF, DPO, and Constitutional AI pipelines don't just mismeasure — their failure modes compound into model weights and downstream decisions. This workshop is where NLP evaluation researchers, alignment scientists, and production ML practitioners come together around that shared problem.
🎯
Core Evaluation Validity
Construct validity, calibration, human–model alignment, criteria pre-registration, and inter-judge consistency.
🔀
Surface vs. Semantic Sensitivity
Robustness of LLM judges to meaning-preserving paraphrase, length and formatting bias, and semantic content scoring.
🪞
Bias & Sycophancy
Positional and ordering bias in pairwise evaluation, self-preference, and feedback loop risks in judge-guided alignment.
🛡️
Safety-Relevant Evaluation
Semantic drift under iterative transformation, adversarial robustness of safety evaluators, and meaning preservation.
🏗️
Benchmark Construction
Adversarial benchmark design, criteria drift in datasets, domain-specific frameworks, and negative-result datasets.
⚙️
Judge Design & Architecture
Prompt engineering, fine-tuning vs. prompting, multi-judge ensembles, tool-augmented judges, and capability gaps.
🏭
Practitioner Perspectives
Production evaluation pipelines, practitioner–researcher gaps, deployment failure case studies, and cost–quality trade-offs.
🤖
Agentic & Emerging Topics
Reasoning chain validity, multi-turn agentic evaluation, cross-lingual reliability, and ethical dimensions of automated evaluation.
Research Agenda
Failure Taxonomy
LLM judge failures don't arrive in isolation — in production pipelines they cascade. Sycophancy biases preference data, which shifts model style, which drifts the judge's implicit criteria across training iterations. Surface sensitivity enables adversarial safety bypasses. Correlated errors across judge families mean ensembles suppress disagreement precisely on the cases most likely to be collectively wrong. The taxonomy below organizes these into seven empirically grounded failure facets, each with an open question at the frontier of current research.
Facet
Core failure mode
Open question
01
Surface vs. semantic sensitivity
Formatting and length drive scores over meaning; paraphrases receive inconsistent judgments.
Can judges be calibrated to score meaning-equivalent responses identically?
02
Criteria drift
Criteria shift after seeing real outputs; "evaluate helpfulness" is operationalized inconsistently.
Can criteria be pre-registered and verified for post-hoc consistency?
03
Positional & ordering bias
Primacy/recency effects skew pairwise rankings.
Does position-swap averaging fully debias long-context evaluation?
04
Sycophancy & self-preference
Judges favour stylistically familiar outputs regardless of quality.
How do we detect and break the sycophancy–training feedback loop?
05
Reasoning chain validity
Judge capability bounds evaluation capability; gap worsens as models outpace judges.
What is the minimum judge–model capability gap for valid evaluation?
06
Safety-relevant meaning preservation
Judges are fooled by adversarial paraphrase preserving harmful content.
What protocols reliably detect safety-relevant semantic drift?
07
Inter-judge consistency
Cross-judge agreement is low on semantically complex cases.
What inter-judge agreement threshold is acceptable in high-stakes settings?
Community Deliverable
Judge Deployment Disclosure Template
One concrete output of JUDGe is a structured disclosure template for judge deployment decisions — analogous to a model card, but for the evaluation pipeline. No such standard currently exists. The organizing team is drafting a seed version from collective production experience at Meta, Amazon, and Google, releasing it on
GitHub ↗
before the workshop, and refining it collaboratively with attendees during the poster session and panel. The post-workshop version will be published as an open-access community standard.
The template covers four dimensions:
📋
Training Data Provenance
The judge's training data sources, known capability bounds, and distribution assumptions.
🔗
Deployment Context
What decisions or training signals the judge's scores produce, and what is upstream and downstream.
⚠️
Known Failure Modes
Which of the seven failure facets apply, with empirical evidence where available.
✅
Human Validation
What validation was performed before deployment, including human agreement rate and methodology.
Timeline
Important Dates
All deadlines are 11:59 PM AoE. All notifications precede the mandatory NeurIPS deadline of September 29, 2026.
CFP Opens
August 1, 2026
Call for papers issued
Submission Deadline
August 29th, 2026
Papers due via OpenReview
Notifications
September 29, 2026
Accept / reject decisions sent
Camera-Ready
October 15, 2026
Final versions due
Workshop Day
Dec 12–13, 2026
NeurIPS 2026 · Atlanta, Georgia
Submissions
Call for Papers
JUDGe welcomes original research on all dimensions of LLM evaluator reliability and validity. Works in progress, negative results, practitioner case studies, and cross-disciplinary contributions are particularly encouraged — the workshop is designed for work that wouldn't fit neatly into a standard NLP or ML venue track.
Submission Tracks
Full Papers
6 pages + references · Oral presentation
Short Papers
4 pages + references · Poster presentation
Junior Spotlight
2 pages + references · Oral · Students & early-career only
Topics of Interest
Construct validity in LLM-based evaluators
Calibration methods for LLM judges
Human–model alignment in evaluation
Robustness to meaning-preserving paraphrase
Positional and ordering bias in pairwise evaluation
Sycophancy and self-preference detection
Semantic drift detection under iterative transformation
Adversarial robustness of safety evaluators
Adversarial benchmark design for stress-testing
Multi-judge ensembles and disagreement resolution
Tool-augmented and environment-grounded judges
Production evaluation pipeline case studies
Reasoning chain validity in complex task evaluation
Agentic and multi-turn LLM evaluation
Cross-lingual and multilingual evaluation reliability
Societal and ethical dimensions of automated evaluation
All submissions via
OpenReview
, double-blind, ≥3 reviews per paper. All accepted work is
non-archival
and posted on the workshop website (authors may opt out). Previously published work at a major ML venue is not eligible.
Submit on OpenReview ↗
NeurIPS LaTeX Template ↗
Program
Workshop Schedule
09:00 – 09:10
Opening remarks
Workshop goals and evaluation framing from the organizing committee
09:10 – 10:00
Keynote
Keynote Address
Speaker TBD
10:00 – 10:20
Break
Coffee Break
10:20 – 12:00
Oral Papers
Paper Session — 4 Full Papers
15 min presentation + 5 min Q&A each
12:00 – 13:00
Break
Lunch Break
13:00 – 14:00
Junior Spotlight
Junior Spotlight Talks
3 presentations (15 min + 5 min Q&A) — student and early-career authors
14:00 – 14:40
Discussion
Birds-of-a-Feather Groups
5 themed tables — (1) calibration & reliability methods; (2) adversarial robustness & safety evaluation; (3) practitioner eval pipelines & production failures; (4) agentic & multi-turn evaluation; (5) evaluation governance & disclosure standards — facilitators report brief summaries
14:40 – 15:00
Break
Coffee Break
15:00 – 15:45
Panel
Panel Discussion
"When a judge fails inside a production pipeline, who is responsible for detecting it — and what would that even look like?"
15:45 – 17:00
Poster
Poster Session & Networking
75-minute poster session for accepted papers
Invited Speakers
Keynote & Panelists
Eugene Yan
Anthropic
Keynote
Jennifer Wortman Vaughan
Microsoft Research NYC
Panelist
Wei Xu
Georgia Tech
Panelist
Vijai Mohan
Google DeepMind
Panelist
Organizing Committee
Workshop Organizers
Dr. Shanu Sushmita
Northeastern University (Seattle) & University of Washington
Dr. Jayash Koshal
Meta & Northeastern University
Meghana Makhija
Amazon
Dr. Hui Wan
Google DeepMind
Dr. Amjad Abu-Jbara
Amazon Ads
Diversity & Inclusion
Our Commitments
Speaker Diversity
≥50% of confirmed invited speakers identify as women and/or from underrepresented groups. Outreach runs through WAI, Black in AI, LatinX in AI, and Queer in AI networks.
Junior Spotlight Track
Dedicated oral slots for student and early-career authors (≤3 years post-PhD), each paired with a senior researcher for pre-workshop written feedback.
Registration Support
Complimentary registrations available for junior attendees from underrepresented groups, funded through external sponsorship. Contact the lead organizer for inquiries.
Inclusive CFP
Cross-disciplinary perspectives, practitioner case studies, negative results, and works in progress are all welcome — not just finished research.
Get in Touch
Contact & Links
Questions about the workshop, submissions, sponsorship, or travel support? Reach out to the lead organizer.
General Inquiries
judge-neurips-2026@googlegroups.com
Workshop logistics, accessibility, sponsorship
OpenReview
Submission Portal ↗
Active from August 1, 2026
NeurIPS 2026
neurips.cc ↗
Conference registration and travel information
---
title: Verification in the Age of AI Scientists | AI for Science
id: verification-in-the-age-of-ai-scientists-ai-for-science
tags:
- llm-nas-feedback-positioning-7125b1
- neurips-2026-workshop
- venue-candidate
- cfp-details
- ai-for-science
created: '2026-08-16T15:53:10.999117Z'
updated: '2026-08-16T15:54:10.168561Z'
source: https://ai4sciencecommunity.github.io/neurips26.html
source_domain: ai4sciencecommunity.github.io
fetched_at: '2026-08-16T15:53:10.998336Z'
fetch_provider: builtin
status: draft
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'AI for Science: Verification in the Age of AI Scientists (NeurIPS 2026 AI4Science
  workshop) frames the central problem as: ''The bottleneck for AI for Science is
  no longer hypothesis generation, it is verification'' -- asking how to trust AI-generated
  science ''when verifiers are imperfect, scarce, or absent,'' organized around three
  challenges: verification under open-ended hypothesis generation (subtle failure
  modes like data leakage/benchmark gaming making an output ''look verified without
  being so''), verification under imperfect simulators, and verification under real-world
  resource/safety constraints. Format: 4-8 pages, unlimited references/appendices,
  NeurIPS 2026 LaTeX template (checklist not required), nonarchival, OpenReview submission,
  footnote must read ''Submitted to/Accepted at/Published in the AI for Science workshop
  (NeurIPS 2026).'' Tentative dates: submission deadline Aug 29, 2026 AoE; reviews
  due Sep 17; AC recommendations Sep 24; notifications Sep 29; workshop Dec 11 or
  12. GAP: page does not state a double-blind/anonymity policy explicitly, nor any
  stated position on negative results specifically. Scope is broad AI-for-science
  (biology, chemistry, mathematics, climate, healthcare) with only a loose conceptual
  match to LLM-guided architecture search -- ''automated design'' fit is thematic
  (verification of AI-generated outputs) rather than domain-specific, making this
  a weaker topical match than Verify-Agents or TAE despite superficial appeal of the
  ''verification'' framing.'
---

*Suggested by [[announcing-the-neurips-2026-workshops-neurips-blog]] — NeurIPS 2026 AI for Science workshop, subtitled Verification in the Age of AI Scientists - Tier 3 candidate touching the self-verification theme and automated design broadly*

Verification in the Age of AI Scientists | AI for Science
About
AI Scientists now operate at a scale that outpaces human capacity for manual review. Systems such as Sakana’s AI Scientist write entire workshop papers end-to-end. Lila Sciences runs autonomous ``AI Science Factories’’ that hypothesize, experiment, and iterate without human guidance. FutureHouse’s Kosmos and Robin generate thousands of candidate hypotheses in a single run, and Google’s Co-Scientist proposes testable experiments at a rate no laboratory can fully evaluate. 
Each of these systems emphasizes
verified
results, yet that standard ranges from near-perfect formal proof in mathematics to decade-long clinical trials in medicine, with no shared framework for judging sufficiency across domains. As outputs scale beyond what humans can manually inspect, the question of which results to trust becomes as hard as generating them.
The bottleneck for AI for Science is no longer hypothesis generation, it is verification
.
Our NeurIPS 2026 workshop,
Verification in the Age of AI Scientists
, asks how we should trust, judge, and act on AI-generated science when verifiers are imperfect, scarce, or absent. In most sciences the verifier itself is imperfect or prohibitively expensive, and as AI Scientists scale beyond what humans can manually inspect, the central problem becomes
which AI outputs deserve our scarce verification budget, and on what evidence we should be willing to act
. We organize our discussion around three challenges.
Verification in open-ended hypothesis generation
When AI Scientists propose thousands of candidate hypotheses, only a small fraction can ever be tested, and not all plausible outputs are scientifically meaningful, novel, or worth pursuing. Subtle failure modes such as data leakage, benchmark gaming, and hallucinated citations can make an output look verified without being so, and human taste, intuition, and domain expertise remain essential filters that are not yet well understood as learnable verifiers. This workshop asks how to build verifiers that can separate genuinely novel scientific contributions from convincing artifacts.
Verification under imperfect simulators
Scientific domains differ dramatically in the reliability of their verifiers. In mathematics, formal systems such as Lean provide near-perfect verification, but in biology, force fields fail outside their training distribution and structure prediction has well-documented blind spots , while climate models depend on partial observations and expert judgment. This workshop asks when surrogate verifiers can substitute for ground truth, and on what evidence AI Scientists should be willing to act when the two disagree.
Verification under real-world constraints (uncertainty & safety)
In practice, verification is bounded by time, cost, experimental throughput, and safety. A single Phase III clinical trial costs hundreds of millions of dollars and takes a decade, and in extreme weather prediction, rare out-of-distribution events drive evacuation and infrastructure decisions before sufficient evidence can be gathered. This workshop asks how scarce verification resources should be allocated across competing AI-generated hypotheses when downstream decisions affect human lives.
Follow Us
Please follow us on
X
and
LinkedIn
for the latest news, or join us on the
Slack
for active discussions.
AI for Science Party
Detailed information to be posted.
Invited Talks
Mario Krenn
University of Tübingen
AI, Physics
Teresa Head-Gordon
UC Berkeley
AI, Chemistry
Anna Scaglione
Cornell
AI, Power System
Adam Zsolt Wagner
Google DeepMind
AI, Mathematics
Charlotte Deane
Oxford
AI, Biology
Amanda Barnard
Australian National University
AI, Healthcare
Panel: The Verification Gap: Abundant Hypotheses, Scarce Verifiers
Marinka Zitnik (Moderator)
Harvard
David Rolnick
McGill and Mila
AI, Climate Science
Rianne van den Berg
Microsoft Research
AI, Chemistry
Cheng Soon Ong
CSIRO and Australian National University
AI, Science
Lina Yao
UNSW
AI, Healthcare
Tentative Dates (Anywhere on Earth)
Submission deadline: August 29, 2026 AoE
Reviewer period: August 31 – September 1, 2026 AoE
Reviewer reviews due: September 17, 2026 AoE
Area Chair recommendations due: September 24, 2026 AoE
Accept/reject notifications: September 29, 2026 AoE
Workshop date: December 11 or 12, 2026
Submissions
Please submit your paper through
OpenReview
. Our workshop is
nonarchival
, and accepted papers will be posted on the workshop website. Please use the
NeurIPS 2026 LaTeX template
; the NeurIPS checklist is not required. Change the template footnote to “Submitted to/Accepted at/Published in the AI for Science workshop (NeurIPS 2026).” Submissions should be 4-8 pages, with unlimited references and appendices. See the
Call for Papers page
for full details.
Call for Reviewers/Area Chairs
We are calling for active researchers in the field to help with our review process. Here are the
reviewer
and
area chair
sign up forms.
Frequent Q&A
What is the abstract deadline and why do we have it?
You only need to create a submission tab on OpenReview by the abstract deadline. (
This is not a separate submission track for short papers
). As we receive a large volume of diverse submissions, to entire good review quality and coverage of reviewer areas, we keep an abstract deadline for us to have a chance to invite new reviewers if needed.
Can I attend the workshop even if I don’t have any submissions?
Yes, you are welcome to attend the workshop. Registration is through NeurIPS 2026 registration system with workshop selected.
Can I join the organizing team?
We always welcome new members to join our organizing team, feel free to reach out to us if you are interested. Several questions are recommended to be answered to help us make decision: what do you like about the workshop? what do you think we should improve? what can you contribute to the organizing team?
Organizers and Contact
For any question, please contact
ai4scienceneurips2026@googlegroups.com
.
Organizers
Marinka Zitnik
Harvard
Priya Donti
MIT
Yuanqi Du
Microsoft Research
Ada Fang
Harvard
Anvita Bhagavathula
MIT
Ana Rivera
MIT
Emilien Dupont
Google DeepMind
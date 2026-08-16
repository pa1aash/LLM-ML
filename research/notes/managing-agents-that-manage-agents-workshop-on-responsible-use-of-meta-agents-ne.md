---
title: 'Managing Agents that Manage Agents: Workshop on Responsible Use of Meta-Agents
  (NeurIPS 2026)'
id: managing-agents-that-manage-agents-workshop-on-responsible-use-of-meta-agents-ne
tags:
- llm-nas-feedback-positioning-7125b1
- venue-candidate
- neurips-2026-workshop
- cfp-details
- agent-verification
- priority-source
created: '2026-08-16T16:51:36.043518Z'
updated: '2026-08-16T16:53:43.078895Z'
source: https://meta-agents-workshop.github.io/
source_domain: meta-agents-workshop.github.io
fetched_at: '2026-08-16T16:51:36.043241Z'
fetch_provider: builtin
status: draft
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Managing Agents that Manage Agents (Workshop on Responsible Use of Meta-Agents,
  NeurIPS 2026, Sydney, Dec 11-12) is the STRONGEST new candidate found in this pass.
  It defines ''meta-agents'' as higher-order agents that build, optimize, and supervise
  other agents (citing AlphaEvolve, GEPA, Meta-Harness as examples) and explicitly
  names topic (1) ''Automated Design and Discovery of Agent Harnesses'' -- ''searching
  the space of agent architectures, tools, and harnesses (Meta Agent Search, automated
  harness design), and telling when a discovered design generalizes past the tasks
  it was tuned on'' -- and topic (3) ''Self-Improvement and Open-Ended Evolution''
  -- ''agents that rewrite their own code..., self-play and co-evolution, open-endedness,
  and HONEST ANALYSES OF HOW SELF-IMPROVING AGENTS DRIFT OR GAME THEIR OWN REWARD.''
  This is a near-exact scope match for a controlled negative result about an LLM agent''s
  self-refinement loop in architecture design failing to improve. Format: Full papers
  <=9 pages, Short papers <=4 pages (main text; references/appendices excluded but
  main text must be self-contained), plus a Demo track and a Position-paper track
  (governance/oversight/societal impact). Double-blind (author names, affiliations,
  acknowledgments removed; prior work cited in third person). Non-archival; work under
  review elsewhere is welcome, work already published at NeurIPS/other archival ML
  venues is excluded. UNIQUE MANDATORY REQUIREMENT: every submission must include
  a short ''responsible-use statement'' covering societal impacts and mitigations
  -- a missing statement is explicit grounds for desk rejection. Submission via OpenReview;
  deadline Aug 29, 2026 AoE; notification by Sep 29, 2026; workshop Dec 11-12, 2026.
  No explicit blanket statement welcoming negative results, but ''honest analyses
  of...drift'' is functionally an invitation for exactly this paper''s finding. Organized
  by a Stanford/CMU/Northeastern team (Simon Yu, Dilara Soylu, Derek Chong, Christopher
  D. Manning among organizers); confirmed speakers include Graham Neubig (CMU, agent
  harness automation) and Jenny Zhang (Recursive Superintelligence/UBC, ''Self-Improving
  Agents and Their Failure Modes'' -- Darwin Gödel Machine).'
---

*Suggested by [[announcing-the-neurips-2026-workshops-neurips-blog]] — First Workshop on Meta Agents, checking scope for agents-designing-agents fit*

Managing Agents that Manage Agents: Workshop on Responsible Use of Meta-Agents (NeurIPS 2026)
Managing Agents that Manage Agents
Workshop on Responsible Use of Meta-Agents
NeurIPS 2026 · December 11-12, 2026 · Sydney, Australia
Meta-agents are increasingly used to train, manage, and supervise other agents, and even people. How do we ensure this capability develops responsibly?
Follow @MetaAgentWkshop
About The Workshop
Most agentic systems today rely on manual design for their training, harnesses, and goals. As models grow more capable, new systems are emerging to automate this. AlphaEvolve writes and tests its own programs; GEPA and Meta-Harness use agents to optimize the trajectories of other agents, beating reinforcement learning at a fraction of the cost. We call these higher-order agents that
build
,
optimize
, and
supervise
other agents
meta-agents
.
Meta-agents will likely play an increasingly central role in how agentic systems are used and developed. Yet discourse on them stays dispersed across separate communities, from meta-learning to reinforcement learning to systems research. A systematic, interdisciplinary view is needed to address their potential for both use and misuse, convening core figures from these subfields alongside researchers in AI and organizational science.
The shift from manual to automated agent design raises open
technical problems
. A meta-agent can design the harness, train the agent system, and enable continual learning and self-improvement. When does a discovered or self-improved design actually generalize, and which optimization methods and learning signals improve a meta-agent's capabilities?
As capabilities scale,
societal impact
needs careful oversight. A meta-agent acts like a manager, decomposing objectives and assigning tasks to worker agents, so a misaligned one can spawn and coordinate swarms of subordinate agents toward the wrong goal. Meta-agents can also manage humans, with risks of economic disruption and eroded autonomy. So every result raises the same question:
who evaluates and oversees an agent that builds or improves another agent, or itself?
The workshop covers the full lifecycle, design, training, evaluation, deployment, and oversight, and every submission carries a responsible-use statement.
Topics
We invite work across the topics below, capability first, then evaluation, oversight, and governance. Topics include but are not limited to:
(1) Automated Design and Discovery of Agent Harnesses:
Most agent harnesses are still built by hand. We invite work on searching the space of agent architectures, tools, and harnesses (Meta Agent Search, automated harness design), and on telling when a discovered design generalizes past the tasks it was tuned on.
(2) Optimization and Post-Training of Compound Agentic Systems:
Once an agent is more than one model call, the problem is optimizing the whole program. We seek work on optimizers for multi-module systems (DSPy, GEPA, Trace), credit assignment across modules, post-training of compound systems, inference-time search, and context optimization.
(3) Self-Improvement and Open-Ended Evolution:
A meta-agent can point at itself. We welcome work on agents that rewrite their own code (the Darwin Gödel Machine, self-taught optimizers), self-play and co-evolution, open-endedness, and honest analyses of how self-improving agents drift or game their own reward.
(4) Evaluation and Benchmarks for Meta-Agents:
Does a discovered or self-improved agent actually generalize? We want benchmarks and tests for meta-level methods, the ones that answer this question rather than leaderboards that hide the failure cases.
(5) Misalignment and Safety for Meta-Agents:
Making agent execution observable and auditable, red-teaming systems that act on other agents, and detecting reward gaming, over-optimization, and drift before a system acts on other agents at scale.
(6) Governance and Human Oversight of Meta-Agents:
Rollback and halt controls a deployer can actually trigger, who signs off before a discovered agent ships, and how to govern agents that manage other agents, including perspectives from management science and other fields outside AI.
Call For Papers
Managing Agents that Manage Agents
(NeurIPS 2026) invites submissions on architectures, algorithms, theory, empirical studies, benchmarks, and position papers about agents that design, optimize, supervise, train, or improve other agents. Submissions must present original, unpublished work that has not appeared at NeurIPS or other archival machine-learning venues.
Key Dates
Submission Deadline
:
August 29, 2026, AoE
Notification
:
on or before September 29, 2026, AoE
Workshop Date
: December 11-12, 2026 (Sydney)
All deadlines follow the
Anywhere on Earth (AoE)
timezone.
Submission Site
Submissions are managed via OpenReview and remain private during review. All authors should maintain up-to-date OpenReview profiles for conflict-of-interest management and paper matching. Submit your paper at the
OpenReview submission portal
.
Interested in serving as a reviewer or Area Chair (AC)?
Self-nominate using this form
.
Scope
We welcome contributions across the topics above. Accepted papers are presented as posters, with a subset selected for oral or spotlight talks, and we give a
Best Paper
award and a
Best Social Impact Paper
award for the work that most thoughtfully addresses the societal implications of meta-agents. The workshop is in person at NeurIPS 2026 in Sydney.
Submission Guidelines
Formatting
Submissions must be in English and use the NeurIPS 2026 workshop LaTeX template. Papers are submitted as a
single PDF
:
Full Papers
: at most 9 pages (main text)
Short Papers
: at most 4 pages (main text)
Demo Track
: live demonstrations of meta-agent systems and tools, presented alongside the poster sessions.
Position Papers
: on the governance, oversight, and societal impact of meta-agents.
References and appendices do not count toward the page limit, but the main text must be self-contained.
Responsible-Use Statement
Every submission also includes a short
responsible-use statement
covering the potential societal impacts of the proposed work and suggested mitigations. It is reviewed with the paper, and a missing one is grounds for desk rejection.
Anonymity
The workshop uses
double-blind review
. Submissions must be anonymized, with author names, affiliations, and acknowledgments removed and prior work cited in the third person.
Non-Archival Policy
The workshop is non-archival.
Papers under review elsewhere are welcome, and accepted papers may be published at other venues afterward. Work already published at NeurIPS or other archival ML venues should not be submitted.
Contact
Email
meta-agents-workshop@googlegroups.com
.
Speakers & Panelists
Eight invited speakers and panelists planning to attend in person, all confirmed except where marked tentative. Talk topics are illustrative and finalized with each speaker.
Graham Neubig
Carnegie Mellon University
Speaker
Talk:
Automating and Evaluating the Agent Harness
Automating the SWE-agent harness (OpenHands) and recursive agent optimization, with the evaluation needed to trust the result.
Chelsea Finn
Stanford University
Speaker & Panelist
(Tentative)
Talk:
From Meta-Learning to Agents that Learn to Learn
How learning-to-learn, from MAML to the Meta-Harness, carries into agents that tune their own scaffolding.
Jenny Zhang
Recursive Superintelligence & UBC
Speaker
Talk:
Self-Improving Agents and Their Failure Modes
The Darwin Gödel Machine and HyperAgents as open-ended self-improvement, and the failure modes when an agent rewrites its own code.
Robert Lange
Sakana AI
Speaker
Talk:
Evolutionary Methods for Self-Improving Agents
Evolutionary, nature-inspired methods (The AI Scientist, ShinkaEvolve) for agents that improve other agents.
Bo Li
University of Illinois Urbana-Champaign
Speaker & Panelist
Talk:
How Meta-Agents Could Help on Safety Evaluation
Trustworthy-ML for agents that act on other agents: red-teaming, robustness, and safety benchmarks (DecodingTrust).
Hancheng Cao
Emory University
Speaker & Panelist
Talk:
AI Agents that Manage People: Work, Labor, and Oversight
How AI agents reshape work, organizational design, and management (When Your Boss Is an AI Bot).
Yuandong Tian
Recursive
Panelist
Panelist.
Reinforcement learning, planning, and efficient reasoning for self-improving AI; co-founder of Recursive.
Chen Sun
Google DeepMind
Panelist
Panelist.
World models and open-endedness: the learned environments a meta-agent uses to train, simulate, and evaluate other agents.
Tentative Schedule
All invited talks include a Q&A session. Titles are illustrative; the final schedule is confirmed closer to the workshop.
Time (AEDT)
Session
Speaker
Talk Title
08:20 – 08:30
Opening Remarks & Framing
Organizers
08:30 – 09:00
Invited Talk 1
Graham Neubig (CMU)
Automating and Evaluating the Agent Harness
09:00 – 09:30
Invited Talk 2
Chelsea Finn (Stanford)
(tentative)
From Meta-Learning to Agents that Learn to Learn
09:30 – 10:00
Invited Talk 3
Robert Lange (Sakana AI)
Evolutionary Methods for Self-Improving Agents
10:00 – 10:30
Technical Problems: Oral + Spotlight Talks
Selected authors
10:30 – 11:30
Poster Session 1 + Demo Track
11:30 – 13:00
Lunch Break
13:00 – 14:00
Poster Session 2 + Demo Track
14:00 – 14:30
Invited Talk 4
Jenny Zhang (Recursive Superintelligence & UBC)
Self-Improving Agents and Their Failure Modes
14:30 – 15:00
Invited Talk 5
Bo Li (UIUC)
How Meta-Agents Could Help on Safety Evaluation
15:00 – 15:30
Invited Talk 6
Hancheng Cao (Emory)
AI Agents that Manage People: Work, Labor, and Oversight
15:30 – 16:00
Societal Impacts: Oral + Position Talks
Selected authors
16:00 – 16:45
Societal Impact Panel & Debate
Oversight of Meta-Agents
(Cao, Chen Sun, Yuandong Tian, Finn
(tentative)
, Bo Li)
As meta-agents build and manage other agents, what role remains for humans, and who stays accountable when something goes wrong?
16:45 – 17:00
Awards & Closing Remarks
Organizers
Organizers
This workshop is organized and advised by
Simon Yu
Northeastern University
Dilara Soylu
Stanford University
Derek Chong
Stanford University
Ananjan Nandi
Stanford University
Apurva Gandhi
Carnegie Mellon University
Jiuding Sun
Stanford University
Zichen Liu
Google DeepMind
Christopher D. Manning
Stanford University
Weiyan Shi
Northeastern University
Sponsors
We gratefully acknowledge the support of our sponsor.
Meta AI
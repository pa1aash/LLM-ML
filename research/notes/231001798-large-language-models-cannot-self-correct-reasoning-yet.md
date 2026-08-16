---
title: '[2310.01798] Large Language Models Cannot Self-Correct Reasoning Yet'
id: 231001798-large-language-models-cannot-self-correct-reasoning-yet
tags:
- llm-nas-feedback-positioning-7125b1
created: '2026-08-16T15:45:59.373659Z'
source: https://arxiv.org/abs/2310.01798
source_domain: arxiv.org
fetched_at: '2026-08-16T15:45:59.373278Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
---

*Suggested by [[231108516-llms-cannot-find-reasoning-errors-but-can-correct-them-given-the-error]] — Huang et al. 2023 is the paper Tyen et al. cite as showing self-correction causes correct answers to become incorrect -- the foundational negative result on intrinsic LLM self-correction*

[2310.01798] Large Language Models Cannot Self-Correct Reasoning Yet
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computation and Language
arXiv:2310.01798
(cs)
[Submitted on 3 Oct 2023 (
v1
), last revised 14 Mar 2024 (this version, v2)]
Title:
Large Language Models Cannot Self-Correct Reasoning Yet
Authors:
Jie Huang
,
Xinyun Chen
,
Swaroop Mishra
,
Huaixiu Steven Zheng
,
Adams Wei Yu
,
Xinying Song
,
Denny Zhou
View a PDF of the paper titled Large Language Models Cannot Self-Correct Reasoning Yet, by Jie Huang and 6 other authors
View PDF
HTML (experimental)
Abstract:
Large Language Models (LLMs) have emerged as a groundbreaking technology with their unparalleled text generation capabilities across various applications. Nevertheless, concerns persist regarding the accuracy and appropriateness of their generated content. A contemporary methodology, self-correction, has been proposed as a remedy to these issues. Building upon this premise, this paper critically examines the role and efficacy of self-correction within LLMs, shedding light on its true potential and limitations. Central to our investigation is the notion of intrinsic self-correction, whereby an LLM attempts to correct its initial responses based solely on its inherent capabilities, without the crutch of external feedback. In the context of reasoning, our research indicates that LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction. Drawing from these insights, we offer suggestions for future research and practical applications in this field.
Comments:
ICLR 2024
Subjects:
Computation and Language (cs.CL)
; Artificial Intelligence (cs.AI)
Cite as:
arXiv:2310.01798
[cs.CL]
(or
arXiv:2310.01798v2
[cs.CL]
for this version)
https://doi.org/10.48550/arXiv.2310.01798
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Jie Huang [
view email
]
[v1]
Tue, 3 Oct 2023 04:56:12 UTC (129 KB)
[v2]
Thu, 14 Mar 2024 04:27:52 UTC (137 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Large Language Models Cannot Self-Correct Reasoning Yet, by Jie Huang and 6 other authors
View PDF
HTML (experimental)
TeX Source
view license
Current browse context:
cs.CL
< prev
|
next >
new
|
recent
|
2023-10
Change to browse by:
cs
cs.AI
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
export BibTeX citation
Loading...
BibTeX formatted citation
×
loading...
Data provided by:
Bookmark
Bibliographic Tools
Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer
(
What is the Explorer?
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?
)
Litmaps Toggle
Litmaps
(
What is Litmaps?
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?
)
DagsHub Toggle
DagsHub
(
What is DagsHub?
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?
)
Core recommender toggle
CORE Recommender
(
What is CORE?
)
Author
Venue
Institution
Topic
About arXivLabs
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community?
Learn more about arXivLabs
.
Which authors of this paper are endorsers?
|
Disable MathJax
(
What is MathJax?
)
---

## Full-text extraction (from PDF, arxiv.org/pdf/2310.01798, ICLR 2024 camera-ready, v2)

Authors: Jie Huang (Google DeepMind / UIUC), Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou (Google DeepMind). Published as a conference paper at ICLR 2024.

**Definition of intrinsic self-correction (Section 2):** "we first define the concept of intrinsic self-correction, a scenario wherein the model endeavors to rectify its initial responses based solely on its inherent capabilities, without the crutch of external feedback." Distinguished from self-correction with oracle labels / external feedback (human, other models, external tools/knowledge sources). "For brevity, unless explicitly stated otherwise (e.g., self-correction with oracle feedback), all references to 'self-correction' in the remainder of this paper pertain to intrinsic self-correction."

**Central finding:** "LLMs struggle to self-correct their reasoning without external feedback, and at times, their performance even degrades after self-correction... In most instances, the performance after self-correction even deteriorates." This is explicitly stated to contrast with prior optimistic results (Kim et al. 2023 "RCI"; Shinn et al. 2023 "Reflexion") — those improvements were shown to stem from using oracle (ground-truth) labels to decide when to stop self-correcting; "the improvements vanish when oracle labels are not available."

**Models tested (multiple scales) — this directly addresses model-scale dependence:**
- GPT-3.5-Turbo (gpt-3.5-turbo-0613)
- GPT-4 (accessed 2023/08/29)
- GPT-4-Turbo (gpt-4-1106-preview)
- Llama-2-70b-chat

Temperature = 1 for GPT-3.5-Turbo and GPT-4; temperature = 0 for GPT-4-Turbo and Llama-2 ("to provide a comparison across different decoding algorithms"). Max two rounds of self-correction. Three-step prompting: (1) initial generation, (2) model reviews its own generation and produces feedback, (3) model answers again incorporating its own feedback.

**Table 2 (oracle-label self-correction, for reference/contrast):**
- GPT-3.5: Standard Prompting GSM8K 75.9, CommonSenseQA 75.8, HotpotQA 26.0 → Self-Correct(Oracle) 84.3 / 89.7 / 29.0 (improves)
- GPT-4: Standard 95.5 / 82.0 / 49.0 → Self-Correct(Oracle) 97.5 / 85.5 / 59.0 (improves)

**Table 3 (intrinsic self-correction, GPT-3.5 and GPT-4) — VERBATIM NUMBERS:**
- GPT-3.5: Standard Prompting (1 call) GSM8K 75.9, CommonSenseQA 75.8, HotpotQA 26.0. Self-Correct round 1 (3 calls): 75.1 / 38.1 / 25.0. Self-Correct round 2 (5 calls): 74.7 / 41.8 / 25.0.
- GPT-4: Standard Prompting (1 call) GSM8K 95.5, CommonSenseQA 82.0, HotpotQA 49.0. Self-Correct round 1 (3 calls): 91.5 / 79.5 / 49.0. Self-Correct round 2 (5 calls): 89.0 / 80.0 / 43.0.

**Table 4 (intrinsic self-correction, GPT-4-Turbo and Llama-2) — VERBATIM NUMBERS — KEY MODEL-SCALE EVIDENCE:**
- GPT-4-Turbo: Standard Prompting (1 call) GSM8K 91.5, CommonSenseQA 84.0. Self-Correct round 1 (3 calls): 88.0 / 81.5. Self-Correct round 2 (5 calls): 90.0 / 83.0.
- Llama-2 (70b-chat, the smallest/weakest model tested): Standard Prompting (1 call) GSM8K 62.0, CommonSenseQA 64.0. Self-Correct round 1 (3 calls): 43.5 / 37.5. Self-Correct round 2 (5 calls): 36.5 / 36.5.

This is the paper's clearest scale signal: Llama-2-70b-chat (weakest model) shows the LARGEST relative degradation (GSM8K 62.0→36.5, a 25.5-point / 41% relative drop; CommonSenseQA 64.0→36.5, a 27.5-point / 43% relative drop) versus GPT-4-Turbo (strongest model tested) showing the SMALLEST degradation (GSM8K 91.5→90.0, only 1.5 points; CommonSenseQA 84.0→83.0, only 1.0 point). GPT-3.5 (mid-tier) shows severe degradation on CommonSenseQA (75.8→41.8, a 33.7% point / 44% relative drop) but only mild on GSM8K (75.9→74.7). The paper does NOT explicitly theorize a monotonic scale law in prose, but the tabulated results show weaker/smaller models degrading more severely under intrinsic self-correction than the strongest model (GPT-4-Turbo), which is the closest this paper comes to a scale-dependence claim.

**Mechanism analysis (Section 3.3, "Why does performance not increase, but instead decrease?"):**
"For GSM8K, 74.7% of the time, GPT-3.5 retains its initial answer. Among the remaining instances, the model is more likely to modify a correct answer to an incorrect one than to revise an incorrect one to a correct one. The fundamental issue is that LLMs cannot properly judge the correctness of their reasoning." Change-type breakdown per Figure 1 (pie charts) includes Correct→Incorrect, Incorrect→Correct, Incorrect→Incorrect, No Change categories, e.g. GSM8K/GPT-3.5: No Change 74.7%, Correct→Incorrect 8.8%, Incorrect→Correct 7.0%, Incorrect→Incorrect 8.9%(approx, read from pie). Llama-2 shows much larger swings (~40% No Change, large Correct→Incorrect and Incorrect→Incorrect slices), consistent with weaker models being less stable under self-correction.

**Multi-agent debate vs self-consistency (Section 4):** Multi-agent debate (Du et al. 2023) reimplemented with gpt-3.5-turbo-0301, 3 agents, 2 rounds. Table 7: Standard Prompting (1 response) GSM8K 76.7; Self-Consistency (3 responses) 82.5; Multi-Agent Debate round1 (6 responses) 83.2; Self-Consistency (6 responses) 85.3; Multi-Agent Debate round2 (9 responses) 83.0; Self-Consistency (9 responses) 88.2 (best). Conclusion: "multi-agent debate significantly underperforms simple self-consistency using majority voting" at equal inference cost — reframed as "not attributed to 'self-correction', but rather to 'self-consistency'" (i.e., gains from selection among multiple independent generations + voting, not from genuine critique/correction).

**Prompt-design confound (Section 5):** Shows self-correction "improvements" reported in prior work (e.g., Madaan et al. 2023 Self-Refine on CommonGen-Hard) stem from sub-optimally worded initial prompts; when the initial prompt is fixed to be equally informative as the feedback prompt, standalone performance rises and self-correction again decreases performance (Table 8: their improved "Standard Prompting (ours)" = 81.8 already beats Self-Correct* = 75.1, whereas original weak prompt was 44.0→67.0* after self-correction).

**Conclusion / Section 6 statement on external feedback:** "current LLMs struggle to self-correct their reasoning without external feedback... it is imperative for the community to approach the concept of self-correction with a discerning perspective." Cites Gou et al. 2023 and Zhou et al. 2023a as prior work also showing self-correction performance weakens without external feedback and can be biased by misleading feedback (Wang et al. 2023a) — "consistent with our findings in this work."

**Limitations (Section 7):** Explicitly scoped to reasoning tasks; acknowledges self-correction has shown success in OTHER domains such as altering response style or enhancing safety (Bai et al. 2022; Ganguli et al. 2023; Madaan et al. 2023), distinguishing capability-to-fix from capability-to-judge-appropriateness. This is a scope-limiting caveat relevant to any downstream paper trying to generalize the "self-correction degrades" finding beyond reasoning tasks into a different domain like NAS/architecture search.

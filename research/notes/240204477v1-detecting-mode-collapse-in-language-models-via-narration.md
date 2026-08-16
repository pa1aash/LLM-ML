---
title: '[2402.04477v1] Detecting Mode Collapse in Language Models via Narration'
id: 240204477v1-detecting-mode-collapse-in-language-models-via-narration
tags:
- llm-nas-feedback-positioning-7125b1
- mode-collapse
- output-diversity
- rlhf
created: '2026-08-16T15:45:56.861822Z'
updated: '2026-08-16T15:49:51.502047Z'
source: https://arxiv.org/abs/2402.04477v1
source_domain: arxiv.org
fetched_at: '2026-08-16T15:45:56.861031Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Hamilton (McGill), EACL 2024 ScaleLLM workshop (non-archival, single-author).
  Samples 4,374 stories (temp=1.0) from three OpenAI models of increasing alignment
  intensity (davinci-instruct-beta: instruction-tuning only; text-davinci-003: +RLHF;
  gpt-3.5-turbo: +conversational fine-tuning) across 8 crossed demographic ''virtual
  author'' prompt variables, clusters via BERTopic. Finds gpt-3.5-turbo (most-aligned)
  produces the most topically repetitive, template-like stories -- reusing specific
  named entities (Amara, Rachel, Mary) regardless of requested demographic -- while
  earlier/less-aligned models produce more topically diffuse (if less coherent) output.
  Frames this as LLM ''mode collapse'' by direct analogy to GAN mode collapse, attributed
  to ''overalignment,'' and claims to be an early empirical report of this phenomenon
  in LLMs (as of Feb 2024). Does NOT test quantisation as a variable -- isolates RLHF/alignment
  intensity only, so it partially but not fully covers a ''quantisation causes diversity
  loss'' rival explanation. Useful precedent that alignment/RLHF intensity alone can
  drive output-diversity collapse independent of any architecture-search-specific
  claim.'
---

[2402.04477v1] Detecting Mode Collapse in Language Models via Narration
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computation and Language
arXiv:2402.04477v1
(cs)
[Submitted on 6 Feb 2024]
Title:
Detecting Mode Collapse in Language Models via Narration
Authors:
Sil Hamilton
View a PDF of the paper titled Detecting Mode Collapse in Language Models via Narration, by Sil Hamilton
View PDF
HTML (experimental)
Abstract:
No two authors write alike. Personal flourishes invoked in written narratives, from lexicon to rhetorical devices, imply a particular author--what literary theorists label the implied or virtual author; distinct from the real author or narrator of a text. Early large language models trained on unfiltered training sets drawn from a variety of discordant sources yielded incoherent personalities, problematic for conversational tasks but proving useful for sampling literature from multiple perspectives. Successes in alignment research in recent years have allowed researchers to impose subjectively consistent personae on language models via instruction tuning and reinforcement learning from human feedback (RLHF), but whether aligned models retain the ability to model an arbitrary virtual author has received little scrutiny. By studying 4,374 stories sampled from three OpenAI language models, we show successive versions of GPT-3 suffer from increasing degrees of "mode collapse" whereby overfitting the model during alignment constrains it from generalizing over authorship: models suffering from mode collapse become unable to assume a multiplicity of perspectives. Our method and results are significant for researchers seeking to employ language models in sociological simulations.
Comments:
To appear in the proceedings of the first Workshop on the Scaling Behavior of Large Language Models (EACL 2024)
Subjects:
Computation and Language (cs.CL)
; Artificial Intelligence (cs.AI)
Cite as:
arXiv:2402.04477
[cs.CL]
(or
arXiv:2402.04477v1
[cs.CL]
for this version)
https://doi.org/10.48550/arXiv.2402.04477
Focus to learn more
arXiv-issued DOI via DataCite
Journal reference:
https://aclanthology.org/2024.scalellm-1.5/
Submission history
From: Sil Hamilton [
view email
]
[v1]
Tue, 6 Feb 2024 23:52:58 UTC (69 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Detecting Mode Collapse in Language Models via Narration, by Sil Hamilton
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
2024-02
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

## Full-text extraction (from PDF, arxiv.org/pdf/2402.04477v1, Sil Hamilton, McGill University, EACL 2024 ScaleLLM workshop)

**Core empirical setup:** 4,374 stories sampled (temperature=1.0, max 400 tokens ≈307 words) from three OpenAI models of increasing alignment: davinci-instruct-beta (instruction-tuning only, no RLHF), text-davinci-003 (instruction tuning + RLHF), gpt-3.5-turbo (further conversational fine-tuning). All are 175B-parameter decoder-only models sharing lineage from InstructGPT. Prompts varied 8 demographic descriptors (education, orientation, ethnicity, implied reader, gender, story type) crossed to create 4,374 unique "virtual author" prompts, topic-clustered via BERTopic.

**Central finding — mode collapse increases monotonically with alignment intensity:** "successive versions of GPT-3 suffer from increasing degrees of 'mode collapse' whereby overfitting the model during alignment constrains it from generalizing over authorship: models suffering from mode collapse become unable to assume a multiplicity of perspectives." gpt-3.5-turbo (most-aligned, RLHF+conversational-FT) produces the MOST topically repetitive stories despite varying demographic prompts, repeatedly reusing specific named entities ("Amara, Rachel, and Mary... appearing more frequently (or exclusively) in stories written by gpt-3.5-turbo... despite adjusting the demographic descriptors"). The two less-aligned/earlier models (davinci-instruct-beta, text-davinci-003) instead produced topically diffuse, lexically ambiguous stories that BERTopic mostly failed to cluster into coherent topics at all.

**Mechanism claim:** "We suspect the model suffers from mode collapse due to overalignment." Explicit analogy to GAN mode collapse ("wherein overfitting a GAN results in the model failing to generalize over their target distribution... GANs suffering from mode collapse consequently becoming more repetitive the more training they receive"). Author states: "To our best knowledge, that large language models can suffer from mode collapse has not been previously reported in the literature" (as of Feb 2024) — i.e., this paper claims to be an early/first empirical demonstration of LLM-side mode collapse attributable to RLHF/alignment, distinct from the classical GAN usage of the term.

**Relation to "alignment tax":** Cites Ouyang et al. 2022 (InstructGPT paper) acknowledging an "alignment tax" — degraded performance on "several public NLP datasets" post-RLHF — but notes it was previously unclear whether this tax extended to out-of-distribution creative/generative tasks; this paper argues it does, manifesting as loss of narrative/authorial diversity.

**Limitations (author-stated):** Only tested OpenAI proprietary, now-deprecated models (2024 deprecations limit reproducibility); recommends future work use open-weight models (Llama 2, Mistral) for reproducibility. Confined to fictional narrative genre; does not test whether mode collapse appears in conversational or non-fictional generation.

**Relevance to the query's mechanism question (rival explanations for "twenty identical designs"):** This is a directly on-point, small/informal (EACL workshop, single-author, non-archival ScaleLLM workshop) precedent for the mechanism "RLHF/alignment intensity → reduced generation diversity → repetitive/templated outputs," independent of and prior to any NAS-specific claim. It supports treating "RLHF-induced mode collapse" as a plausible rival explanation for a quantised chat/instruct model collapsing to one architecture template, separate from any decoding-temperature or quantisation-specific explanation. Note: this paper does NOT test quantisation as a variable — alignment/RLHF intensity is the only mechanism it isolates, so it only partially covers the query's "quantisation" rival-explanation angle and cannot be used alone to establish a quantisation-specific diversity-loss mechanism.

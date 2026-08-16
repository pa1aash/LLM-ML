---
title: 'RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost
  Strategy'
id: rz-nas-enhancing-llm-guided-neural-architecture-search-via-reflective-zero-cost
tags:
- llm-nas-feedback-positioning-7125b1
- rz-nas
- llm-guided-nas
- counter-evidence
created: '2026-08-16T15:47:44.757716Z'
updated: '2026-08-16T15:50:44.684655Z'
source: https://proceedings.mlr.press/v267/ji25a.html
source_domain: proceedings.mlr.press
fetched_at: '2026-08-16T15:47:44.756990Z'
fetch_provider: builtin
status: draft
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'CONFIRMED VENUE: RZ-NAS by Zipeng Ji, Guanghui Zhu, Chunfeng Yuan, Yihua
  Huang (Nanjing University / PasaLab) is a real, peer-reviewed paper published at
  ICML 2025 (Proceedings of the 42nd International Conference on Machine Learning,
  PMLR vol. 267, pp. 27237-27254), OpenReview forum id 9UExQpH078. This directly resolves
  the environment note''s locating query -- the claim that RZ-NAS is ICML 2025 with
  a ''reflective zero-cost'' strategy is accurate, not fabricated. Method: Reflective
  Zero-cost NAS integrates LLM ''reflection modules'' -- LLM-generated natural-language
  feedback used iteratively within an evolutionary search loop (see companion GitHub
  repo, evolution_search.py) -- together with training-free (zero-cost) proxy metrics,
  to guide architecture optimization across both micro and macro search spaces. The
  abstract explicitly frames prior LLM-to-NAS work as limited by ''limited search
  spaces, time-cost search efficiency, and uncompetitive performance,'' and claims
  RZ-NAS ''achieves SOTA performance across multiple downstream tasks'' via this LLM-reflection-in-the-loop
  design. Critically, this is a claim that LLM feedback/reflection IMPROVES NAS outcomes
  -- the opposite finding from the target paper''s degradation thesis -- making RZ-NAS
  a first-order counter-evidence candidate for question FOUR and a first-order novelty
  comparator for question ONE. No arXiv preprint exists for this paper (confirmed
  via arXiv API title search returning zero results); PMLR/ICML proceedings and GitHub
  are the only primary sources. Note: the OpenReview forum page (openreview.net/forum?id=9UExQpH078)
  could not be fetched due to a bot-verification wall (AUTH_REQUIRED); the openreview.net/attachment
  PDF route returned 403 Forbidden; the PDF hosted on raw.githubusercontent.com failed
  PDF-text extraction in this pipeline. Full mechanism/experimental detail (e.g.,
  exact ablation of reflection vs. no-reflection, iteration counts, whether reflection
  ever degrades results in some settings) is NOT yet captured from this batch and
  would require a follow-up fetch of the PDF via a different extraction route.'
---

RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy
[
edit
]
RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy
Zipeng Ji, Guanghui Zhu, Chunfeng Yuan, Yihua Huang
Proceedings of the 42nd International Conference on Machine Learning
, PMLR 267:27237-27254, 2025.
Abstract
LLM-to-NAS is a promising field at the intersection of Large Language Models (LLMs) and Neural Architecture Search (NAS), as recent research has explored the potential of architecture generation leveraging LLMs on multiple search spaces. However, the existing LLM-to-NAS methods face the challenges of limited search spaces, time-cost search efficiency, and uncompetitive performance across standard NAS benchmarks and multiple downstream tasks. In this work, we propose the Reflective Zero-cost NAS (RZ-NAS) method that can search NAS architectures with humanoid reflections and training-free metrics to elicit the power of LLMs. We rethink LLMs’ roles in NAS in current work and design a structured, prompt-based to comprehensively understand the search tasks and architectures from both text and code levels. By integrating LLM reflection modules, we use LLM-generated feedback to provide linguistic guidance within architecture optimization. RZ-NAS enables effective search within both micro and macro search spaces without extensive time cost, achieving SOTA performance across multiple downstream tasks.
Cite this Paper
BibTeX
@InProceedings{pmlr-v267-ji25a,
  title = 	 {{RZ}-{NAS}: Enhancing {LLM}-guided Neural Architecture Search via Reflective Zero-Cost Strategy},
  author =       {Ji, Zipeng and Zhu, Guanghui and Yuan, Chunfeng and Huang, Yihua},
  booktitle = 	 {Proceedings of the 42nd International Conference on Machine Learning},
  pages = 	 {27237--27254},
  year = 	 {2025},
  editor = 	 {Singh, Aarti and Fazel, Maryam and Hsu, Daniel and Lacoste-Julien, Simon and Berkenkamp, Felix and Maharaj, Tegan and Wagstaff, Kiri and Zhu, Jerry},
  volume = 	 {267},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {13--19 Jul},
  publisher =    {PMLR},
  pdf = 	 {https://raw.githubusercontent.com/mlresearch/v267/main/assets/ji25a/ji25a.pdf},
  url = 	 {https://proceedings.mlr.press/v267/ji25a.html},
  abstract = 	 {LLM-to-NAS is a promising field at the intersection of Large Language Models (LLMs) and Neural Architecture Search (NAS), as recent research has explored the potential of architecture generation leveraging LLMs on multiple search spaces. However, the existing LLM-to-NAS methods face the challenges of limited search spaces, time-cost search efficiency, and uncompetitive performance across standard NAS benchmarks and multiple downstream tasks. In this work, we propose the Reflective Zero-cost NAS (RZ-NAS) method that can search NAS architectures with humanoid reflections and training-free metrics to elicit the power of LLMs. We rethink LLMs’ roles in NAS in current work and design a structured, prompt-based to comprehensively understand the search tasks and architectures from both text and code levels. By integrating LLM reflection modules, we use LLM-generated feedback to provide linguistic guidance within architecture optimization. RZ-NAS enables effective search within both micro and macro search spaces without extensive time cost, achieving SOTA performance across multiple downstream tasks.}
}
Copy to Clipboard
Download
Endnote
%0 Conference Paper
%T RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy
%A Zipeng Ji
%A Guanghui Zhu
%A Chunfeng Yuan
%A Yihua Huang
%B Proceedings of the 42nd International Conference on Machine Learning
%C Proceedings of Machine Learning Research
%D 2025
%E Aarti Singh
%E Maryam Fazel
%E Daniel Hsu
%E Simon Lacoste-Julien
%E Felix Berkenkamp
%E Tegan Maharaj
%E Kiri Wagstaff
%E Jerry Zhu	
%F pmlr-v267-ji25a
%I PMLR
%P 27237--27254
%U https://proceedings.mlr.press/v267/ji25a.html
%V 267
%X LLM-to-NAS is a promising field at the intersection of Large Language Models (LLMs) and Neural Architecture Search (NAS), as recent research has explored the potential of architecture generation leveraging LLMs on multiple search spaces. However, the existing LLM-to-NAS methods face the challenges of limited search spaces, time-cost search efficiency, and uncompetitive performance across standard NAS benchmarks and multiple downstream tasks. In this work, we propose the Reflective Zero-cost NAS (RZ-NAS) method that can search NAS architectures with humanoid reflections and training-free metrics to elicit the power of LLMs. We rethink LLMs’ roles in NAS in current work and design a structured, prompt-based to comprehensively understand the search tasks and architectures from both text and code levels. By integrating LLM reflection modules, we use LLM-generated feedback to provide linguistic guidance within architecture optimization. RZ-NAS enables effective search within both micro and macro search spaces without extensive time cost, achieving SOTA performance across multiple downstream tasks.
Copy to Clipboard
Download
APA
Ji, Z., Zhu, G., Yuan, C. & Huang, Y.. (2025). RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy.
Proceedings of the 42nd International Conference on Machine Learning
, in
Proceedings of Machine Learning Research
267:27237-27254 Available from https://proceedings.mlr.press/v267/ji25a.html.
Copy to Clipboard
Download
Related Material
Download PDF
OpenReview
Software
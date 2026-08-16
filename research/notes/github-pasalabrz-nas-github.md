---
title: GitHub - PasaLab/RZ-NAS · GitHub
id: github-pasalabrz-nas-github
tags:
- llm-nas-feedback-positioning-7125b1
- rz-nas
- llm-guided-nas
created: '2026-08-16T15:49:09.809983Z'
updated: '2026-08-16T15:51:14.811410Z'
source: https://github.com/PasaLab/RZ-NAS
source_domain: github.com
fetched_at: '2026-08-16T15:49:09.808895Z'
fetch_provider: builtin
status: draft
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: Official RZ-NAS code repository (PasaLab, 5 stars). Confirms implementation
  is evolutionary search (evolution_search.py) over micro and macro CNN search spaces,
  using zero-cost proxies (ZeroShotProxy/ folder, configurable via --zero_shot_score
  flag) plus structured LLM prompts (prompt/ and descriptions/ folders, with a template.txt
  showing full prompt structure). Search spaces include PlainNet-style and SuperRes-block
  architectures (SuperResIDWEXKX.py, SuperResK1KXK1.py, SuperResKXKX.py), i.e. CNN-style
  search spaces analogous in spirit to the target paper's CNN search space. This is
  a small, low-visibility repo (5 stars, 0 forks, 19 commits) -- useful for confirming
  the method is real and reproducible in principle, but does not itself provide ablation
  numbers isolating the reflection module's contribution; would need the paper PDF
  (extraction failed in this pipeline) for the actual iteration-by-iteration or with/without-reflection
  results tables.
---

*Suggested by [[rz-nas-enhancing-llm-guided-neural-architecture-search-via-reflective-zero-cost]] — official code repo, README may describe method and results tables*

GitHub - PasaLab/RZ-NAS · GitHub
Skip to content
You signed in with another tab or window.
Reload
to refresh your session.
You signed out in another tab or window.
Reload
to refresh your session.
You switched accounts on another tab or window.
Reload
to refresh your session.
Dismiss alert
Uh oh!
There was an error while loading.
Please reload this page
.
PasaLab
/
RZ-NAS
Public
Notifications
You must be signed in to change notification settings
Fork
0
Star
5
main
Branches
Tags
Go to file
Code
Open more actions menu
Folders and files
Name
Name
Last commit message
Last commit date
Latest commit
History
19 Commits
19 Commits
Dataloader
Dataloader
PlainNet
PlainNet
SearchSpace
SearchSpace
ZeroShotProxy
ZeroShotProxy
descriptions
descriptions
prompt
prompt
Masternet.py
Masternet.py
README.md
README.md
SuperResIDWEXKX.py
SuperResIDWEXKX.py
SuperResK1KXK1.py
SuperResK1KXK1.py
SuperResKXKX.py
SuperResKXKX.py
analyze_model.py
analyze_model.py
basic_blocks.py
basic_blocks.py
benchmark_network_latency.py
benchmark_network_latency.py
evolution_search.py
evolution_search.py
global_utils.py
global_utils.py
super_blocks.py
super_blocks.py
val.py
val.py
val_cifar.py
val_cifar.py
View all files
Repository files navigation
RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy
About
This is the repository for the paper RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy.
LLM-to-NAS is a promising field at the intersection of Large Language Models (LLMs) and Neural Architecture Search (NAS), as recent research has explored the potential of architecture generation leveraging LLMs on multiple search spaces. However, the existing LLM-to-NAS methods face the challenges of limited search spaces, time-cost search efficiency, and uncompetitive performance across standard NAS benchmarks and multiple downstream tasks. In this work, we propose Reflective Zero-cost NAS (RZ-NAS) that can search NAS architectures with humanoid reflections and training-free metrics to elicit the power of LLMs. We rethink LLMs' roles in NAS in current work and design a structured, prompt-based to comprehensively understand the search task and architectures from both text and code levels. By integrating LLM reflection modules, we use LLM-generated feedback to provide linguistic guidance within architecture optimization. RZ-NAS enables effective search within both micro and macro search spaces without extensive time cost, achieving SOTA performance across multiple downstream tasks.
Search
One example of the whole prompt is saved in
template.txt
. More zero-cost proxies and search spaces are saved under the folder
descriptions
.
For different zero-cost proxies, you can change the parameter
zero_shot_score
.
python evolution_search.py --gpu 0 --zero_shot_score <zero-cost proxy> --search_space <micro/macro search space>
more customized parameters setting can be found in ./scripts.
About
No description, website, or topics provided.
Resources
Readme
Activity
Custom properties
Stars
5
stars
Watchers
0
watching
Forks
0
forks
Report repository
Releases
Packages
Contributors
Languages
You can’t perform that action at this time.
# BIBLIOGRAPHY AUDIT

> ## ⛔ SUBMISSION BLOCKER
>
> **2 of 47 entries (4.3%) carry FABRICATED author lists** — author names that do
> not appear on the cited work at all. **3 further entries (6.4%) carry
> WRONG-METADATA** — real papers with corrupted or invented co-authors.
>
> **5 of 47 entries (10.6%) misattribute authorship.** One entry
> (`li2025gptnas`) has **zero** overlap with the real author list: all six named
> authors are wrong. A reviewer who checks a single reference has a better than
> one-in-ten chance of landing on a bad one. **This must be fixed before any
> submission.**

Method: every entry was resolved against a **fetched** record — OpenAlex
(`filter=title.search:`), falling back to Semantic Scholar, then the arXiv API.
Nothing below is written from memory. The resolving URL for each entry is
recorded in `audit/references_verified.bib` in the `note` field.

Resolution rate: **46 of 47 (97.9%)**. One unresolved.

---

## Diff table — entries requiring action

| key | claimed authors | verified authors | claimed venue/year | verified venue/year | verdict |
|---|---|---|---|---|---|
| `li2025gptnas` | Li, Haixin; Jin, Rongyu; He, Jianan; Zheng, Wentao; Wei, Zhuoran; Chi, Siyuan | **Yu, Caiyang; Liu, Xianggen; Wang, Yifan; Liu, Yun; Feng, Wentao; Xiong, Deng; Tang, Chenwei; Lv, Jiancheng** | arXiv 2305.05351 / 2023 | arXiv:2305.05351 / 2023 | **FABRICATED** |
| `kamoi2024llmselfcorrect` | Kamoi, Ryo; Raman, Yusen; Peng, Guanghui; Strobelt, Hendrik; Malin, Bradley | **Kamoi, Ryo; Zhang, Yusen; Zhang, Nan; Han, Jiawei; Zhang, Rui** | TMLR / 2024 | TMLR / 2024 | **FABRICATED** |
| `white2023nas` | White, Colin; Safari, Mahmoud; **Suber, Rhea**; Ru, Binxin; **Thomas, Shan**; Hutter, Frank | White, Colin; Safari, Mahmoud; **Sukthanker, Rhea Sanjay**; Ru, Binxin; **Elsken, Thomas**; **Zela, Arber**; **Dey, Debadeepta**; Hutter, Frank | arXiv 2301.08727 / 2023 | arXiv:2301.08727 / 2023 | **WRONG-METADATA** |
| `tyen2024llms` | Tyen, Gladys; Mansoor, Hassan; **Muresanu, Tony**; Chen, Peter; **Phang, Jason** | Tyen, Gladys; Mansoor, Hassan; **Cărbune, Victor**; Chen, Peter; **Mak, Tony** | ACL Findings / 2024 | ACL Findings / 2024 | **WRONG-METADATA** |
| `wang2024scienceagentbench` | **Wang, Ziru**; **Chen, Fangqi**; **Arber, Yubo**; others | **Chen, Ziru**; Chen, Shijie; Ning, Yuting; Zhang, Qianheng; Wang, Boshi; Yu, Botao; … | arXiv 2410.05080 / 2024 | arXiv:2410.05080 / 2024 | **WRONG-METADATA** |
| `bonferroni1936teoria` | Bonferroni, Carlo E. | — | Pubbl. R. Ist. Sup. Sci. Econ. Comm. Firenze, vol 8 / 1936 | — | **UNRESOLVED** |

### How the two known-bad entries were caught

Both entries flagged in the session brief were detected independently by the
resolution pipeline, which confirms it works:

- **`white2023nas`** — "Suber, Rhea" is a corruption of **Sukthanker, Rhea
  Sanjay**; "Thomas, Shan" is a corruption of **Thomas Elsken** with the given
  name replaced; and two real authors (**Arber Zela**, **Debadeepta Dey**) are
  dropped. Title and arXiv ID are correct. 4/6 surname overlap.
- **`li2025gptnas`** — title and arXiv ID (2305.05351) are correct; the author
  list is entirely invented. **0/6 surname overlap** — not one claimed author
  appears on the paper. The bib key also says `2025` while its own `year` field
  says `2023`.

`kamoi2024llmselfcorrect` was not flagged in the brief but is equally bad: only
"Kamoi" is real, "Raman, Yusen" is a corruption of **Yusen Zhang**, and Peng,
Strobelt and Malin are not authors of the work.

---

## Entries verified clean

The remaining **41 entries resolved with author lists matching the verified
record.** Differences observed in these were confined to:

- diacritics (`Esperanca` / `Esperança`),
- given/family name-order flips introduced by the *resolver*, not the bib
  (`zheng2023genius` "Qian, Chen"; `so2019evolved` "Liang, Chen"),
- initials vs full names (`lu2024aiscientist` "Lange, Robert Tjarko" /
  "R. T. Lange"),
- author-list truncation by OpenAlex at 9 names (`madaan2023selfrefine`,
  `romeraparedes2024funsearch`),
- corporate authorship (`qwen2025qwen3` `{Qwen Team}` — a legitimate BibTeX
  convention; the underlying record lists individuals).

None of these is an error in `paper/references.bib`.

---

## Non-authorship defects

These do not misattribute credit but will produce wrong output or reviewer
friction.

| key | defect | effect |
|---|---|---|
| `so2019evolved` | declared `@article` but supplies `booktitle` | `icml2025.bst` will drop the venue — The Evolved Transformer (ICML 2019) renders without a venue |
| `huang2024selfcorrection` | declared `@article` but supplies `booktitle` | same; ICLR 2024 venue lost |
| `howard2017mobilenets` | declared `@inproceedings` but supplies `journal` | MobileNets is arXiv-only and was never a conference paper; type and field both wrong |
| `li2025gptnas` | key year (2025) ≠ field year (2023) | citation renders as "2023" while the key implies 2025; also invites a stale-citation query |
| `romeraparedes2024funsearch` | year 2024 vs record 2023 | FunSearch appeared online in Nature in Dec 2023, in the 2024 issue. Defensible; note only |

**No entry was found STALE** in the sense of a preprint that has since been
published under a different venue. Several entries resolved to their arXiv
mirrors because OpenAlex's `primary_location` prefers the open-access copy; in
each case the venue claimed by the bib (ICLR, ICML, NeurIPS, UAI) is the correct
published venue, and the bib was left as-is in the verified file.

---

## The unresolved entry

`bonferroni1936teoria` — *Teoria Statistica delle Classi e Calcolo delle
Probabilità*, Pubblicazioni del R. Istituto Superiore di Scienze Economiche e
Commerciali di Firenze, vol. 8, 1936.

**UNRESOLVED — not indexed by OpenAlex, Semantic Scholar, or arXiv.** This is
expected for a pre-digital Italian monograph and is not evidence of a defect. It
is *not* reproduced as a record in `references_verified.bib`; it appears there
only as a comment. Verify against a library catalogue before submission.
Logged as open action **OA-14**.

---

## Output

`audit/references_verified.bib` — 46 fetched records in the repository's existing
BibTeX style, each carrying `note = {verified: <url>}`. The five defective
entries carry an inline `% VERDICT:` comment naming the specific corruption.

**`paper/references.bib` was not modified.**

---

## Verdict

| | count | share |
|---|---|---|
| FABRICATED | 2 | 4.3% |
| WRONG-METADATA | 3 | 6.4% |
| **Total misattributed** | **5** | **10.6%** |
| Non-authorship defects (type/year) | 5 | 10.6% |
| UNRESOLVED | 1 | 2.1% |
| Clean | 41 | 87.2% |

**Submission blocker.** A fabricated author list is not a typographical error —
it is the signature of a reference generated rather than retrieved, and reviewers
increasingly check for exactly this. With 5 of 47 entries misattributing
authorship, and one with zero correct authors, the bibliography cannot go to a
venue in its current state. Replace `paper/references.bib` with
`audit/references_verified.bib` after operator review, then re-verify the
`\citep` keys still resolve and rebuild.

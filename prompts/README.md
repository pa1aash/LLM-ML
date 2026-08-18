# prompts/ — frozen at session S3-1

Every file in this directory is an input to a measurement. A change to any of
them invalidates the `prompts` hashes in every results-file header emitted
against them (`EXPERIMENT_PLAN_R6.md` §5.5) and is itself a `DEVIATIONS.md`
entry. `prompts/MANIFEST.json` carries the SHA-256 of each file and is written
by `scripts/freeze_prompts.py`; `--check` verifies without rewriting.

## Layout

| Path | Variant |
|---|---|
| `E1/schema_canonical.txt` | schema-constrained JSON request, canonical enumeration order |
| `E1/schema_reversed.txt` | schema-constrained JSON request, reversed enumeration order |
| `E1/freeprose.txt` | free-prose description request |
| `E1/anchor/exemplar_modal.txt` | worked example: `standard_3x3` / `relu` / `batchnorm` |
| `E1/anchor/exemplar_nonmodal.txt` | worked example: `depthwise_separable` / `gelu` / `groupnorm` |
| `E1/anchor/exemplar_absent.txt` | no exemplar block — **zero bytes** |
| `E2/e2_zeroshot.txt` | zero-shot arm |
| `E2/e2_uncurated.txt` | uncurated in-context accumulation arm |
| `E2/e2_curated.txt` | curated summary arm, and the curation prompt below `=== CURATION PROMPT ===` |
| `E2/e2_archive.txt` | external archive arm, top-*m* |

## Composition (DEVIATIONS.md D-002)

An E1 prompt is a template plus an exemplar block. The line holding
`{{EXEMPLAR_BLOCK}}` is replaced by the exemplar file's contents; runs of three
or more consecutive newlines in the result collapse to two. `exemplar_absent.txt`
is zero bytes, so the absent level is the literal absence of the block rather
than a rewording of it.

- The **30 main-grid cells** compose `canonical` (or `freeprose`) with `absent`:
  they carry no worked example.
- The **12 anchor cells** (§2.8) cross `{canonical, reversed}` with
  `{modal, non-modal}`.
- `freeprose` exists at canonical order only. The enumeration-order factor
  belongs to the §2.8 sub-design, which runs schema-constrained.

Each field's allowed values are enumerated in exactly **one** place, the
`### Allowed values` block, so that "reverse every field's allowed values" has a
single unambiguous site per field. `scripts/freeze_prompts.py` checks that the
canonical and reversed files differ on those lines and nowhere else, that every
list is an exact reversal, and that the two files have identical token bags and
character counts.

Free-prose carries the same search-space description and the same value
enumerations as the schema variant, in canonical order, and differs by removing
the JSON structure template and the return-only-JSON instruction — so X1
contrasts format, not the information the two arms receive.

## E2 slots

`{{TASK}}`, `{{HISTORY}}`, `{{STRATEGY}}`, `{{ARCHIVE}}` are filled by the
runner. *m* = 5 and the 120-word strategy bound are D-003.

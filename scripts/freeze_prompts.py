"""Freeze `prompts/` and write `prompts/MANIFEST.json` (plan §2.1, §2.8, §3.2, §5.5).

The manifest is the record the emitter header quotes: §5.5's `prompts` field is
one SHA-256 per frozen file. Running this script after a prompt file changes
produces a different manifest, which is the intended alarm -- a prompt changing
after S3-1 invalidates every header hash emitted against it and is itself a
DEVIATIONS.md entry.

  python3 scripts/freeze_prompts.py           # write (or refresh) the manifest
  python3 scripts/freeze_prompts.py --check   # verify only; non-zero on drift
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emit import constants as K  # noqa: E402
from harness import prompts as P  # noqa: E402

ROLES = {
    "E1/schema_canonical.txt": "E1 schema-constrained request, canonical enumeration order",
    "E1/schema_reversed.txt": "E1 schema-constrained request, reversed enumeration order",
    "E1/freeprose.txt": "E1 free-prose description request",
    "E1/anchor/exemplar_modal.txt": "worked example: standard_3x3 / relu / batchnorm",
    "E1/anchor/exemplar_nonmodal.txt": "worked example: depthwise_separable / gelu / groupnorm",
    "E1/anchor/exemplar_absent.txt": "no exemplar block (zero bytes, D-002)",
    "E2/e2_zeroshot.txt": "E2 arm: zero-shot",
    "E2/e2_uncurated.txt": "E2 arm: uncurated in-context accumulation",
    "E2/e2_curated.txt": "E2 arm: curated summary, plus the curation prompt",
    "E2/e2_archive.txt": "E2 arm: external archive, top-m",
    "README.md": "documentation of the composition rule; never sent to a model",
}

SENT_TO_MODEL = {name: not name.endswith("README.md") for name in ROLES}


def verifications() -> dict:
    order = P.verify_order_reversal(P.read("E1/schema_canonical.txt"),
                                    P.read("E1/schema_reversed.txt"))
    levels = P.verify_exemplar_levels(P.read("E1/anchor/exemplar_modal.txt"),
                                      P.read("E1/anchor/exemplar_nonmodal.txt"))
    absent_sha = P.sha256_file("E1/anchor/exemplar_absent.txt")
    absent = {
        "pass": absent_sha == P.EMPTY_SHA256,
        "sha256": absent_sha,
        "expected_sha256_of_empty_file": P.EMPTY_SHA256,
        "bytes": (P.PROMPT_ROOT / "E1/anchor/exemplar_absent.txt").stat().st_size,
    }
    return {"canonical_vs_reversed": order,
            "modal_vs_nonmodal": levels,
            "absent_is_empty": absent}


def build() -> dict:
    files = {}
    for name in P.prompt_files():
        path = P.PROMPT_ROOT / name
        files[name] = {
            "sha256": P.sha256_file(name),
            "bytes": path.stat().st_size,
            "role": ROLES.get(name, "UNDECLARED"),
            "sent_to_model": SENT_TO_MODEL.get(name, True),
        }
    return {
        "frozen_at": _frozen_at(),
        "frozen_by": "scripts/freeze_prompts.py",
        "plan_revision": K.PLAN_REVISION,
        "plan_sha256": K.PLAN_SHA256,
        "schema_version": K.SCHEMA_VERSION,
        "session": "S3-1",
        "note": "Any change to a file below invalidates every emitted "
                "`prompts` header hash and is a DEVIATIONS.md entry (S3-1).",
        "files": files,
        "compositions": {
            "e1_main_grid_schema": {
                "template": "E1/schema_canonical.txt",
                "exemplar": "E1/anchor/exemplar_absent.txt",
                "note": "the 30 main-grid cells carry no worked example (D-002)",
            },
            "e1_main_grid_freeprose": {
                "template": "E1/freeprose.txt",
                "exemplar": "E1/anchor/exemplar_absent.txt",
            },
            "e1_anchor_2x2": {
                "templates": ["E1/schema_canonical.txt", "E1/schema_reversed.txt"],
                "exemplars": ["E1/anchor/exemplar_modal.txt",
                              "E1/anchor/exemplar_nonmodal.txt"],
                "note": "12 cells: 3 models x 2 orders x 2 exemplars (§2.8)",
            },
            "rule": "the line holding {{EXEMPLAR_BLOCK}} is replaced by the "
                    "exemplar file's contents; runs of 3+ newlines collapse to 2",
        },
        "exemplar_values": K.EXEMPLAR_VALUES,
        "e2_parameters": {"archive_m": P.E2_ARCHIVE_M,
                          "strategy_word_bound": P.E2_STRATEGY_WORD_BOUND,
                          "source": "DEVIATIONS.md D-003"},
        "verification": verifications(),
    }


def _frozen_at() -> str:
    if P.MANIFEST_PATH.exists():
        try:
            return json.loads(P.MANIFEST_PATH.read_text())["frozen_at"]
        except Exception:
            pass
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    doc = build()

    v = doc["verification"]
    ok = all(v[k]["pass"] for k in v)
    print("PROMPT FREEZE  (plan §2.1 / §2.8 / §3.2 / §5.5)\n")
    o = v["canonical_vs_reversed"]
    print(f"  canonical vs reversed : {'PASS' if o['pass'] else 'FAIL'}")
    print(f"    lines               : {o['n_lines']}, differing {o['n_differing_lines']} "
          f"-> {o['differing_line_numbers']}")
    print(f"    fields reversed     : {o['n_fields_reversed']} "
          f"({', '.join(o['fields_reversed'])})")
    print(f"    token bag identical : {o['token_multiset_identical']} "
          f"({o['n_tokens']} tokens)")
    print(f"    char count identical: {o['character_count_identical']} "
          f"({o['n_characters']} chars)")
    for f in o["findings"]:
        print(f"    FINDING: {f}")
    print(f"  modal vs non-modal    : {'PASS' if v['modal_vs_nonmodal']['pass'] else 'FAIL'}"
          f"  fields differing {v['modal_vs_nonmodal']['fields_differing']}")
    print(f"  absent is empty       : {'PASS' if v['absent_is_empty']['pass'] else 'FAIL'}"
          f"  ({v['absent_is_empty']['bytes']} bytes)\n")

    for name, rec in doc["files"].items():
        print(f"  {rec['sha256']}  {rec['bytes']:>5}  {name}")

    if check_only:
        if not P.MANIFEST_PATH.exists():
            print("\n  FAIL: no manifest on disk")
            return 1
        drift = P.verify_manifest()
        print(f"\n  manifest matches disk : {'PASS' if drift['pass'] else 'FAIL'}")
        if not drift["pass"]:
            print(f"    {drift}")
        return 0 if (ok and drift["pass"]) else 1

    if not ok:
        print("\n  ABORT: verification failed; manifest not written")
        return 1
    P.MANIFEST_PATH.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"\n  written: {P.MANIFEST_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

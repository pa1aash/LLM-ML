"""Frozen prompt access, composition and verification.

Plan §2.1 (both E1 prompts frozen in `prompts/E1/`), §2.8 (the anchor prompts
frozen in `prompts/E1/anchor/`, with a diff proving the two enumeration orders
differ only in the order of the value lists), §3.2 (`prompts/E2/`), §5.5 (the
`prompts` header carries one SHA-256 per file).

The composition rule, the zero-byte absent exemplar and the single-site value
enumerations are registered in DEVIATIONS.md D-002; the six-field exemplar value
map is D-001; E2's m and word bound are D-003.

Nothing in this module rewrites a prompt. A prompt file is read, hashed and
composed, never edited: any change to a file under `prompts/` invalidates the
manifest and the emitter header that quotes it.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PROMPT_ROOT = ROOT / "prompts"
MANIFEST_PATH = PROMPT_ROOT / "MANIFEST.json"

#: Sits alone on one line in each E1 template; composition replaces that line.
EXEMPLAR_TOKEN = "{{EXEMPLAR_BLOCK}}"

#: SHA-256 of the empty file. `exemplar_absent.txt` is zero bytes by design
#: (D-002 point 2): the absent level is the literal absence of the block.
EMPTY_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

E1_TEMPLATES = {
    ("schema", "canonical"): "E1/schema_canonical.txt",
    ("schema", "reversed"): "E1/schema_reversed.txt",
    ("freeprose", "canonical"): "E1/freeprose.txt",
}

EXEMPLAR_FILES = {
    "modal": "E1/anchor/exemplar_modal.txt",
    "non_modal": "E1/anchor/exemplar_nonmodal.txt",
    "absent": "E1/anchor/exemplar_absent.txt",
}

E2_ARMS = {
    "zero_shot": "E2/e2_zeroshot.txt",
    "uncurated": "E2/e2_uncurated.txt",
    "curated": "E2/e2_curated.txt",
    "archive": "E2/e2_archive.txt",
}

CURATION_DELIMITER = "=== CURATION PROMPT ==="

#: D-003. Both are prompt content §3.2 delegates to this artifact.
E2_ARCHIVE_M = 5
E2_STRATEGY_WORD_BOUND = 120


# ------------------------------------------------------------------ raw access

def read(rel_path: str) -> str:
    return (PROMPT_ROOT / rel_path).read_text()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def sha256_file(rel_path: str) -> str:
    return hashlib.sha256((PROMPT_ROOT / rel_path).read_bytes()).hexdigest()


def prompt_files() -> list[str]:
    """Every frozen prompt file, relative to `prompts/`, in sorted order."""
    out = []
    for p in sorted(PROMPT_ROOT.rglob("*")):
        if p.is_file() and p.name != "MANIFEST.json":
            out.append(str(p.relative_to(PROMPT_ROOT)))
    return out


# ------------------------------------------------------------------ composition

def _collapse_blank_runs(text: str) -> str:
    """D-002 point 1: three or more consecutive newlines collapse to two."""
    return re.sub(r"\n{3,}", "\n\n", text)


def compose_e1(prompt_format: str, enumeration_order: str, exemplar: str) -> str:
    """The prompt one E1 cell sends, assembled from frozen files only.

    `freeprose` exists at `canonical` order only: the enumeration-order factor is
    the §2.8 sub-design's, and that sub-design runs at the schema-constrained
    configuration. Asking for a reversed free-prose prompt is a bug, not a cell.
    """
    key = (prompt_format, enumeration_order)
    if key not in E1_TEMPLATES:
        raise ValueError(
            f"no frozen template for format={prompt_format!r} "
            f"order={enumeration_order!r}; have {sorted(E1_TEMPLATES)}"
        )
    if exemplar not in EXEMPLAR_FILES:
        raise ValueError(f"unknown exemplar level {exemplar!r}")
    body = read(E1_TEMPLATES[key])
    block = read(EXEMPLAR_FILES[exemplar]).rstrip("\n")
    if EXEMPLAR_TOKEN not in body:
        raise RuntimeError(f"{E1_TEMPLATES[key]} no longer carries {EXEMPLAR_TOKEN}")
    return _collapse_blank_runs(body.replace(EXEMPLAR_TOKEN, block))


def compose_e2(arm: str, task: str, history: str = "", strategy: str = "",
               archive: str = "") -> str:
    """The proposal prompt for one E2 arm. Only the arm's own slots are filled."""
    if arm not in E2_ARMS:
        raise ValueError(f"unknown E2 arm {arm!r}; have {sorted(E2_ARMS)}")
    text = read(E2_ARMS[arm])
    if CURATION_DELIMITER in text:
        text = text.split(CURATION_DELIMITER, 1)[0].rstrip("\n") + "\n"
    return (text.replace("{{TASK}}", task)
                .replace("{{HISTORY}}", history)
                .replace("{{STRATEGY}}", strategy)
                .replace("{{ARCHIVE}}", archive))


def e2_curation_prompt(history: str, strategy: str) -> str:
    """The distillation prompt of the curated arm (§3.2, D-003)."""
    text = read(E2_ARMS["curated"])
    if CURATION_DELIMITER not in text:
        raise RuntimeError("e2_curated.txt no longer carries the curation section")
    section = text.split(CURATION_DELIMITER, 1)[1].lstrip("\n")
    return section.replace("{{HISTORY}}", history).replace("{{STRATEGY}}", strategy)


# ----------------------------------------------------------------- verification

_ENUM_LINE = re.compile(r"^- (\w+): (.+)$")


def enumeration_lines(text: str) -> dict[int, tuple[str, list[str]]]:
    """Every `- field: v1, v2, …` line, by line number.

    D-002 point 4: each field's values appear in exactly one place, so this is
    the complete set of sites the order manipulation touches.
    """
    out: dict[int, tuple[str, list[str]]] = {}
    for i, line in enumerate(text.split("\n")):
        m = _ENUM_LINE.match(line)
        if m:
            out[i] = (m.group(1), [v.strip() for v in m.group(2).split(",")])
    return out


def verify_order_reversal(canonical: str, reversed_: str) -> dict[str, Any]:
    """§2.8's invariant, checked rather than asserted.

    "The only difference between the two order levels is the order of the value
    lists; wording, schema structure, exemplar and instruction token count are
    otherwise identical."

    Four independent checks, all of which must pass:
      1. the two files have the same number of lines;
      2. every differing line is an enumeration line in BOTH files;
      3. every field's value list in the reversed file is the exact reverse of
         the canonical file's;
      4. the whitespace-separated token multisets of the two files are identical
         — the token-count clause, checked as an equality of bags rather than of
         counts, which is strictly stronger.
    """
    c_lines = canonical.split("\n")
    r_lines = reversed_.split("\n")
    c_enum = enumeration_lines(canonical)
    r_enum = enumeration_lines(reversed_)

    findings: list[str] = []
    if len(c_lines) != len(r_lines):
        findings.append(f"line counts differ: {len(c_lines)} vs {len(r_lines)}")

    differing = [i for i in range(min(len(c_lines), len(r_lines)))
                 if c_lines[i] != r_lines[i]]
    non_enum = [i for i in differing if i not in c_enum or i not in r_enum]
    if non_enum:
        findings.append(
            "lines differ that are not value enumerations: "
            + ", ".join(f"{i + 1}:{c_lines[i]!r}" for i in non_enum)
        )

    fields_reversed = []
    for i, (field, c_vals) in sorted(c_enum.items()):
        if i not in r_enum:
            findings.append(f"line {i + 1} is an enumeration in canonical only")
            continue
        r_field, r_vals = r_enum[i]
        if r_field != field:
            findings.append(f"line {i + 1}: field {field} vs {r_field}")
        elif r_vals != list(reversed(c_vals)):
            findings.append(
                f"line {i + 1}: {field} is not the exact reverse "
                f"({c_vals} -> {r_vals})"
            )
        else:
            fields_reversed.append(field)

    # Reversing a comma-separated list moves which value carries the trailing
    # comma, so the bag is taken over tokens stripped of one trailing comma.
    # Character length is compared separately and is exactly preserved by a
    # reversal, which catches any wording change the bag would absorb.
    c_tokens = sorted(t.rstrip(",") for t in canonical.split())
    r_tokens = sorted(t.rstrip(",") for t in reversed_.split())
    if c_tokens != r_tokens:
        findings.append("token multisets differ: wording is not identical "
                        "up to value ordering")
    if len(canonical) != len(reversed_):
        findings.append(f"character counts differ: {len(canonical)} vs "
                        f"{len(reversed_)}; a pure reversal preserves length")

    return {
        "pass": not findings,
        "n_lines": len(c_lines),
        "n_differing_lines": len(differing),
        "differing_line_numbers": [i + 1 for i in differing],
        "fields_reversed": fields_reversed,
        "n_fields_reversed": len(fields_reversed),
        "token_multiset_identical": c_tokens == r_tokens,
        "n_tokens": len(c_tokens),
        "character_count_identical": len(canonical) == len(reversed_),
        "n_characters": len(canonical),
        "findings": findings,
    }


def verify_exemplar_levels(modal: str, non_modal: str) -> dict[str, Any]:
    """The two exemplar levels differ only in the three fields §2.8 names.

    Not required by the plan, checked anyway: an exemplar pair that differed
    anywhere else would put an unregistered manipulation inside the sub-design.
    """
    m_lines, n_lines = modal.split("\n"), non_modal.split("\n")
    findings = []
    if len(m_lines) != len(n_lines):
        findings.append(f"line counts differ: {len(m_lines)} vs {len(n_lines)}")
    differing = [i for i in range(min(len(m_lines), len(n_lines)))
                 if m_lines[i] != n_lines[i]]
    fields = []
    for i in differing:
        m = re.match(r'^\s*"(\w+)":', m_lines[i])
        n = re.match(r'^\s*"(\w+)":', n_lines[i])
        if not m or not n or m.group(1) != n.group(1):
            findings.append(f"line {i + 1} differs outside a field value")
        else:
            fields.append(m.group(1))
    expected = ["conv_type", "activation", "normalization"]
    if sorted(fields) != sorted(expected):
        findings.append(f"fields differing are {fields}, expected {expected}")
    return {"pass": not findings, "fields_differing": fields, "findings": findings}


# --------------------------------------------------------------------- manifest

def load_manifest() -> dict[str, Any]:
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(
            f"{MANIFEST_PATH} is missing; run scripts/freeze_prompts.py"
        )
    return json.loads(MANIFEST_PATH.read_text())


def prompt_hashes() -> dict[str, str]:
    """The `prompts` header of §5.5: one SHA-256 per frozen file.

    Read from the manifest rather than recomputed, so that a file edited after
    the freeze produces a verification failure instead of a quietly updated
    header.
    """
    man = load_manifest()
    return {name: rec["sha256"] for name, rec in man["files"].items()}


def verify_manifest() -> dict[str, Any]:
    """Recompute every hash and compare against the frozen manifest."""
    man = load_manifest()
    on_disk = {name: sha256_file(name) for name in prompt_files()}
    recorded = {name: rec["sha256"] for name, rec in man["files"].items()}
    changed = {n: (recorded[n], on_disk[n]) for n in recorded
               if n in on_disk and recorded[n] != on_disk[n]}
    return {
        "pass": not changed and set(recorded) == set(on_disk),
        "missing_from_disk": sorted(set(recorded) - set(on_disk)),
        "missing_from_manifest": sorted(set(on_disk) - set(recorded)),
        "changed": changed,
    }

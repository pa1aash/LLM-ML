"""raw -> parse -> sanitise, as three separable, independently loggable stages.

Plan §2.1's three logged stages, §2.4.4's repair channels, §2.8's repair
mechanism. The stages are separate objects with separate outputs because the
contrast the experiment turns on -- pre-repair versus post-repair -- is only
measurable if the middle stage's output survives.

  stage 1  extract   locate a candidate JSON object in the raw text
  stage 2  parse     strict json.loads; MAY FAIL, and failure is a RECORDED
                     OUTCOME, not an exception someone handled away
  stage 3  sanitise  OPTIONAL, runnable OFF, applied SYMMETRICALLY across arms
                     when applied at all (OA-8)

Two rules that are easy to state and easy to violate:

  * `coerced` and `filled` are NEVER merged. `coerced` means the model emitted
    an illegal value and the harness overwrote it; `filled` means the model
    emitted nothing and the harness invented one. They are different findings
    about different mechanisms and the manuscript must be able to say which
    (§2.4.4).
  * THE FREE-PROSE PATH USES NO PERMISSIVE EXTRACTOR. Stages 1 and 2 are the
    same code, with the same rules, for both prompt formats. A prose generation
    that does not parse under those rules is a parse failure. A prose-specific
    field-scraper would be a second instrument with its own artifact, and the
    plan rejects it (§2.6).
"""

from __future__ import annotations

import copy
import json
import re
from dataclasses import dataclass, field
from typing import Any

from emit import constants as K

#: Plan §2.4.4. Kept as a tuple so a caller cannot accidentally add a fourth.
REPAIR_CHANNELS = ("passthrough", "coerced", "filled")

_FENCED = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.DOTALL)

#: The architecture-level fields the repository's sanitiser also rewrites.
ARCH_DEFAULTS = {"global_pool": "avg", "fc_layers": 1, "dropout": 0.0}
GLOBAL_POOL_VALUES = ("avg", "max")
GLOBAL_POOL_ALIASES = {"avgpool": "avg", "average": "avg", "avg_pool": "avg",
                       "maxpool": "max", "maximum": "max", "max_pool": "max"}


# ------------------------------------------------------------ stage 1: extract

@dataclass
class ExtractResult:
    candidate: str | None
    method: str          # "fenced" | "balanced_brace" | "none"
    n_candidates_tried: int


def extract(raw_text: str) -> ExtractResult:
    """Locate a candidate JSON object. IDENTICAL for both prompt formats.

    The rules are the repository's own
    (`parse_architecture_from_llm`, run_v2.py:68-88): fenced blocks first, then
    a balanced-brace scan for the first top-level object carrying `blocks`.
    Nothing here is format-aware, and nothing is added for prose.
    """
    tried = 0
    for block in _FENCED.findall(raw_text):
        tried += 1
        try:
            obj = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and "blocks" in obj:
            return ExtractResult(block, "fenced", tried)

    depth = 0
    start = None
    for i, ch in enumerate(raw_text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            if depth == 0:
                continue
            depth -= 1
            if depth == 0 and start is not None:
                tried += 1
                chunk = raw_text[start:i + 1]
                try:
                    obj = json.loads(chunk)
                except json.JSONDecodeError:
                    start = None
                    continue
                if isinstance(obj, dict) and "blocks" in obj:
                    return ExtractResult(chunk, "balanced_brace", tried)
                start = None
    return ExtractResult(None, "none", tried)


# -------------------------------------------------------------- stage 2: parse

@dataclass
class ParseResult:
    outcome: str                      # "parsed" | "parse_failed"
    spec_pre_repair: dict[str, Any] | None
    error: str | None
    extraction_method: str
    n_candidates_tried: int

    @property
    def parsed(self) -> bool:
        return self.outcome == "parsed"


def parse(raw_text: str) -> ParseResult:
    """Strict parse. Returns an outcome; raises nothing for bad model output.

    A parse failure is a measurement (§2.4.3's parse-failure rate is a reported
    outcome), so it is returned, not raised, and never repaired-and-resubmitted.
    """
    if not isinstance(raw_text, str):
        return ParseResult("parse_failed", None, "raw text is not a string", "none", 0)
    ex = extract(raw_text)
    if ex.candidate is None:
        return ParseResult("parse_failed", None,
                           "no JSON object with a `blocks` key",
                           ex.method, ex.n_candidates_tried)
    try:
        obj = json.loads(ex.candidate)
    except json.JSONDecodeError as exc:          # extract already parsed it
        return ParseResult("parse_failed", None, f"json: {exc}",
                           ex.method, ex.n_candidates_tried)
    if not isinstance(obj.get("blocks"), list):
        return ParseResult("parse_failed", None, "`blocks` is not a list",
                           ex.method, ex.n_candidates_tried)
    return ParseResult("parsed", obj, None, ex.method, ex.n_candidates_tried)


# ----------------------------------------------------------- stage 3: sanitise

@dataclass
class SanitiseResult:
    applied: bool
    spec_post_repair: dict[str, Any] | None
    #: per field, one channel per block position (arch fields carry one entry)
    repair_channels: dict[str, list[str]] = field(default_factory=dict)
    #: what a coerced/filled field was rewritten TO, per field per block
    repair_destinations: dict[str, list[Any]] = field(default_factory=dict)
    enumeration_order: str = "canonical"

    def channel_counts(self) -> dict[str, dict[str, int]]:
        """§5.5 `batches[].repair_channels`: counts per field."""
        out: dict[str, dict[str, int]] = {}
        for f, chans in self.repair_channels.items():
            out[f] = {c: chans.count(c) for c in REPAIR_CHANNELS}
        return out


def ordered_vocab(field_name: str, enumeration_order: str) -> list:
    """The value list AS THE HARNESS PRESENTS IT (§2.8, D-006).

    The repository hard-codes its `valid` dict in canonical order. §2.8's
    mechanism requires the sanitiser's list and the prompt's list to be the SAME
    list -- "reversing the enumeration reverses the repair target" -- so the
    order is a parameter here, and `valid_vals[0]` moves with it.
    """
    vocab = list(K.FIELD_VOCAB[field_name])
    if enumeration_order == "canonical":
        return vocab
    if enumeration_order == "reversed":
        return list(reversed(vocab))
    raise ValueError(f"unknown enumeration order {enumeration_order!r}")


def _global_pool_values(enumeration_order: str) -> list[str]:
    vals = list(GLOBAL_POOL_VALUES)
    return vals if enumeration_order == "canonical" else list(reversed(vals))


def sanitise(spec: dict[str, Any], enumeration_order: str = "canonical",
             enabled: bool = True) -> SanitiseResult:
    """The repository's `sanitize_config`, instrumented and order-parameterised.

    OA-8: this stage is OPTIONAL. With `enabled=False` the pre-repair spec is
    returned untouched, every channel is `passthrough`, and nothing is coerced
    or filled -- which is what makes the pre/post contrast a contrast rather
    than a re-description.

    D-005: `channels` snaps to the NEAREST legal value, as the repository does
    and as §2.4.1 states, not to `valid_vals[0]`. It is still `coerced`; the
    destination is recorded so the difference is visible in the results file.
    """
    if not enabled:
        return SanitiseResult(False, copy.deepcopy(spec), {}, {}, enumeration_order)

    out = copy.deepcopy(spec)
    channels: dict[str, list[str]] = {f: [] for f in K.PER_BLOCK_FIELDS}
    dests: dict[str, list[Any]] = {f: [] for f in K.PER_BLOCK_FIELDS}

    for block in out.get("blocks", []):
        if not isinstance(block, dict):
            continue
        for f in K.PER_BLOCK_FIELDS:
            vocab = ordered_vocab(f, enumeration_order)
            present = f in block and block[f] is not None
            if f == "channels":
                if not present:
                    block[f] = vocab[0]              # filled -> first-enumerated
                    channels[f].append("filled")
                    dests[f].append(vocab[0])
                    continue
                try:
                    val = int(block[f])
                except (TypeError, ValueError):
                    block[f] = vocab[0]              # unreadable -> first-enumerated
                    channels[f].append("coerced")
                    dests[f].append(vocab[0])
                    continue
                if val in vocab:
                    block[f] = val
                    channels[f].append("passthrough")
                    dests[f].append(val)
                else:
                    snapped = min(vocab, key=lambda x: abs(x - val))   # D-005
                    block[f] = snapped
                    channels[f].append("coerced")
                    dests[f].append(snapped)
                continue

            if not present:
                block[f] = vocab[0]
                channels[f].append("filled")
                dests[f].append(vocab[0])
                continue
            val = str(block[f]).lower().strip()
            if val in vocab:
                block[f] = val
                channels[f].append("passthrough")
                dests[f].append(val)
            else:
                block[f] = vocab[0]
                channels[f].append("coerced")
                dests[f].append(vocab[0])

    # Architecture-level fields. The repository rewrites these too, so they carry
    # channels on the same three-way vocabulary.
    gp_vals = _global_pool_values(enumeration_order)
    if "global_pool" not in out or out["global_pool"] is None:
        out["global_pool"] = gp_vals[0]
        channels["global_pool"] = ["filled"]
        dests["global_pool"] = [gp_vals[0]]
    else:
        gp = str(out["global_pool"]).lower().strip()
        gp = GLOBAL_POOL_ALIASES.get(gp, gp)
        if gp in gp_vals:
            out["global_pool"] = gp
            channels["global_pool"] = ["passthrough"]
        else:
            out["global_pool"] = gp_vals[0]
            channels["global_pool"] = ["coerced"]
        dests["global_pool"] = [out["global_pool"]]

    for name, default in (("fc_layers", 1), ("dropout", 0.0)):
        caster = int if name == "fc_layers" else float
        if name not in out or out[name] is None:
            out[name] = caster(default)
            channels[name] = ["filled"]
        else:
            try:
                cast = caster(out[name])
                channels[name] = ["passthrough" if cast == out[name] else "coerced"]
                out[name] = cast
            except (TypeError, ValueError):
                out[name] = caster(default)
                channels[name] = ["coerced"]
        dests[name] = [out[name]]

    return SanitiseResult(True, out, channels, dests, enumeration_order)


# --------------------------------------------------------------- whole pipeline

@dataclass
class PipelineResult:
    parse: ParseResult
    sanitise: SanitiseResult | None

    def to_record_fields(self) -> dict[str, Any]:
        """The subset of a §5.5 `generations[]` record these stages own."""
        return {
            "parse_outcome": self.parse.outcome,
            "parse_error": self.parse.error,
            "extraction_method": self.parse.extraction_method,
            "spec_pre_repair": self.parse.spec_pre_repair,
            "spec_post_repair": (self.sanitise.spec_post_repair
                                 if self.sanitise else None),
            "repair_channels": (self.sanitise.repair_channels
                                if self.sanitise else {}),
            "repair_destinations": (self.sanitise.repair_destinations
                                    if self.sanitise else {}),
            "sanitiser_applied": bool(self.sanitise and self.sanitise.applied),
        }


def run_pipeline(raw_text: str, enumeration_order: str = "canonical",
                 sanitiser_enabled: bool = True) -> PipelineResult:
    """All three stages. A parse failure stops before stage 3, by definition:
    there is nothing to sanitise, and the generation is excluded from BOTH
    stages' diversity (§2.1, D-05) rather than counted as a sanitised one."""
    p = parse(raw_text)
    if not p.parsed:
        return PipelineResult(p, None)
    return PipelineResult(p, sanitise(p.spec_pre_repair, enumeration_order,
                                      enabled=sanitiser_enabled))

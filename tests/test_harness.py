"""Block D — known-answer tests for the generation harness, against a stub backend.

Every path the harness has is exercised here without a model: a scripted backend
returns exactly what each test needs, so the answer is known in advance and the
comparison is expected-versus-actual rather than "it ran".

  D1   well-formed schema generation -> all fields passthrough
  D2   one illegal value            -> that field coerced, others passthrough
  D3   one absent field             -> that field filled, others passthrough
  D4   unparseable output           -> parse failure recorded, no spec, not sanitised
  D5   truncated output             -> finish_reason reflects truncation, NOT "stop"
  D6   backend error                -> recorded as failure, no retry, run continues
  D7   sanitiser OFF                -> pre-repair spec preserved, nothing coerced or filled
  D8   identical seed twice         -> byte-identical raw text
  D9   REVERSED enumeration order   -> the FILLED value is the REVERSED order's first
  D10  full generation record round-trips through the results file

D9 is the load-bearing one: the entire anchor-tracking column, and therefore
contrast X5 and the `repair artifact` row of §2.5, rests on the repair target
moving when the enumeration order is reversed. If D9 fails, that column measures
nothing and X5 is vacuous — which is reported as a blocking finding, not
adjusted around.
"""

from __future__ import annotations

import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emit import anchor as A                                     # noqa: E402
from emit import constants as K                                  # noqa: E402
from emit.emitter import ResultsEmitter, not_applicable_slot     # noqa: E402
from emit.metrics import (batch_diversity, batch_surface_diversity,  # noqa: E402
                          normalised_field_entropy)
from harness import prompts as P                                 # noqa: E402
from harness.aggregate import cell_record                        # noqa: E402
from harness.backends import BackendError, compute_finish_reason  # noqa: E402
from harness.config import (BackendConfig, CellSpec, GenerationParams,  # noqa: E402
                            SanitisePolicy, build_backend)
from harness.generate import Harness, assert_symmetric           # noqa: E402
from harness.parse import ordered_vocab, run_pipeline            # noqa: E402

RESULTS: list[dict] = []


def check(test: str, what: str, expected, actual) -> bool:
    ok = expected == actual
    RESULTS.append({"test": test, "what": what, "expected": expected,
                    "actual": actual, "pass": ok})
    return ok


def note(test: str, what: str, value) -> None:
    RESULTS.append({"test": test, "what": what, "expected": "(recorded)",
                    "actual": value, "pass": True})


# ------------------------------------------------------------------- fixtures

LEGAL_BLOCK = {"conv_type": "dilated_3x3", "channels": 128, "activation": "silu",
               "normalization": "layernorm", "skip_connection": "projection",
               "pooling": "maxpool"}


def config(n_blocks: int = 3, **overrides) -> dict:
    blocks = []
    for _ in range(n_blocks):
        blk = dict(LEGAL_BLOCK)
        for k, v in overrides.items():
            if v is None:
                blk.pop(k, None)
            else:
                blk[k] = v
        blocks.append(blk)
    return {"blocks": blocks, "global_pool": "avg", "fc_layers": 1, "dropout": 0.1}


def as_response(cfg: dict) -> str:
    return ("Here is the architecture.\n\n```json\n"
            + json.dumps(cfg, indent=2) + "\n```\n")


def harness(script, *, sanitise: bool = True, temperature: float = 0.7) -> Harness:
    backend = build_backend(BackendConfig("stub", "Qwen/Qwen3-1.7B"), script=script)
    return Harness(backend=backend, params=GenerationParams(temperature),
                   sanitise_policy=SanitisePolicy(enabled=sanitise))


def cell(order: str = "canonical", exemplar: str = "absent", *, cell_id: str = "KAT",
         n_batches: int = 1, n_per_batch: int = 1) -> CellSpec:
    return CellSpec(cell_id=cell_id, model="Qwen/Qwen3-1.7B", prompt_format="schema",
                    precision="nf4", temperature=0.7, enumeration_order=order,
                    exemplar=exemplar, n_batches=n_batches, n_per_batch=n_per_batch)


def one(script, *, order: str = "canonical", sanitise: bool = True) -> dict:
    h = harness(script, sanitise=sanitise)
    return h.generate_one(cell=cell(order), batch=0, index_in_batch=0,
                          prompt=P.compose_e1("schema", order, "absent"))


def channels_of(rec: dict) -> dict:
    return {f: list(v) for f, v in (rec.get("repair_channels") or {}).items()}


# ------------------------------------------------------------------------ D1

def d1() -> None:
    rec = one(as_response(config()))
    check("D1", "parse_outcome", "parsed", rec["parse_outcome"])
    chans = channels_of(rec)
    per_block = {f: set(chans[f]) for f in K.PER_BLOCK_FIELDS}
    check("D1", "every per-block channel is passthrough",
          {f: {"passthrough"} for f in K.PER_BLOCK_FIELDS}, per_block)
    check("D1", "arch-level channels",
          {"global_pool": ["passthrough"], "fc_layers": ["passthrough"],
           "dropout": ["passthrough"]},
          {k: chans[k] for k in ("global_pool", "fc_layers", "dropout")})
    check("D1", "post-repair spec equals pre-repair spec",
          rec["spec_pre_repair"]["blocks"], rec["spec_post_repair"]["blocks"])


# ------------------------------------------------------------------------ D2

def d2() -> None:
    rec = one(as_response(config(activation="ELU")))
    chans = channels_of(rec)
    check("D2", "activation channel per block",
          ["coerced", "coerced", "coerced"], chans["activation"])
    check("D2", "coerced destination is valid_vals[0] under canonical",
          ["relu", "relu", "relu"], rec["repair_destinations"]["activation"])
    others = {f: set(chans[f]) for f in K.PER_BLOCK_FIELDS if f != "activation"}
    check("D2", "every other field passthrough",
          {f: {"passthrough"} for f in K.PER_BLOCK_FIELDS if f != "activation"},
          others)
    check("D2", "no field is filled", 0,
          sum(c.count("filled") for c in chans.values()))


# ------------------------------------------------------------------------ D3

def d3() -> None:
    rec = one(as_response(config(normalization=None)))
    chans = channels_of(rec)
    check("D3", "normalization channel per block",
          ["filled", "filled", "filled"], chans["normalization"])
    check("D3", "filled destination is valid_vals[0] under canonical",
          ["batchnorm"] * 3, rec["repair_destinations"]["normalization"])
    others = {f: set(chans[f]) for f in K.PER_BLOCK_FIELDS if f != "normalization"}
    check("D3", "every other field passthrough",
          {f: {"passthrough"} for f in K.PER_BLOCK_FIELDS if f != "normalization"},
          others)
    # §2.4.4: the two channels are different findings and are never merged.
    check("D3", "nothing is coerced (filled != coerced)", 0,
          sum(c.count("coerced") for c in chans.values()))


# ------------------------------------------------------------------------ D4

def d4() -> None:
    prose = ("The architecture uses three blocks. The first applies a dilated "
             "convolution with 128 channels, silu activation and layer "
             "normalisation, followed by max pooling.")
    h = harness(prose)
    recs = h.generate_batch(cell=cell(n_per_batch=4), batch=0,
                            prompt=P.compose_e1("freeprose", "canonical", "absent"))
    rec = recs[0]
    check("D4", "parse_outcome", "parse_failed", rec["parse_outcome"])
    check("D4", "spec_pre_repair", None, rec["spec_pre_repair"])
    check("D4", "spec_post_repair", None, rec["spec_post_repair"])
    check("D4", "sanitiser_applied", False, rec["sanitiser_applied"])
    check("D4", "repair_channels empty", {}, rec["repair_channels"])
    check("D4", "backend status is ok — the failure is the model's, not the call's",
          "ok", rec["status"])
    from harness.aggregate import batch_record
    b = batch_record(recs, batch=0, order="canonical", exemplar="absent")
    check("D4", "batch parse_failures", 4, b["parse_failures"])
    check("D4", "D_pre excluded (no parseable specs)", None, b["D_pre"])
    check("D4", "D_post excluded (no parseable specs)", None, b["D_post"])
    check("D4", "S is still computed over raw text (§2.4.6)", True, b["S"] is not None)


# ------------------------------------------------------------------------ D5

def d5() -> None:
    truncated = '{"blocks": [{"conv_type": "dilated_3x3", "chann'
    rec = one({"text": truncated, "finish_reason": "length"})
    check("D5", "finish_reason", "length", rec["finish_reason"])
    check("D5", 'finish_reason is NOT "stop"', True, rec["finish_reason"] != "stop")
    check("D5", "finish_reason_source recorded", "stub", rec["finish_reason_source"])
    check("D5", "truncated generation does not parse", "parse_failed",
          rec["parse_outcome"])
    # The rule the local backend applies, as a pure function (OA-16). The
    # budget test comes first: an EOS token emitted exactly at the budget is
    # still a truncation, and calling it "stop" is the defect.
    check("D5", "rule: at budget with EOS last -> length", "length",
          compute_finish_reason(4096, 4096, 7, {7}))
    check("D5", "rule: under budget with EOS last -> stop", "stop",
          compute_finish_reason(100, 4096, 7, {7}))
    check("D5", "rule: under budget, no EOS -> unknown", "unknown",
          compute_finish_reason(100, 4096, 9, {7}))


# ------------------------------------------------------------------------ D6

def d6() -> None:
    good = as_response(config())
    script = [good, good, good, BackendError("simulated 503 from the server"), good]
    h = harness(script)
    recs = h.generate_batch(cell=cell(n_per_batch=5), batch=0,
                            prompt=P.compose_e1("schema", "canonical", "absent"))
    check("D6", "run continues: records emitted", 5, len(recs))
    check("D6", "one recorded failure", 1,
          sum(1 for r in recs if r["status"] == "backend_error"))
    failed = [r for r in recs if r["status"] == "backend_error"][0]
    check("D6", "failed generation index", 3, failed["index_in_batch"])
    check("D6", "finish_reason on a failure", "error", failed["finish_reason"])
    check("D6", "no raw text", None, failed["raw_text"])
    check("D6", "parse not attempted", "not_attempted", failed["parse_outcome"])
    check("D6", "error is recorded verbatim", True,
          "simulated 503" in failed["error"])
    # NO SILENT RETRY: one backend call per generation, no more.
    check("D6", "backend calls made (5 generations, no retry)", 5,
          len(h.backend.calls))
    check("D6", "surviving generations parsed", 4,
          sum(1 for r in recs if r["parse_outcome"] == "parsed"))


# ------------------------------------------------------------------------ D7

def d7() -> None:
    cfg = config(activation="ELU", normalization=None)
    rec = one(as_response(cfg), sanitise=False)
    check("D7", "sanitiser_applied", False, rec["sanitiser_applied"])
    check("D7", "pre-repair spec preserved verbatim", cfg["blocks"],
          rec["spec_pre_repair"]["blocks"])
    check("D7", "post-repair spec is the pre-repair spec", cfg["blocks"],
          rec["spec_post_repair"]["blocks"])
    check("D7", "illegal value NOT coerced", "ELU",
          rec["spec_post_repair"]["blocks"][0]["activation"])
    check("D7", "absent field NOT filled", False,
          "normalization" in rec["spec_post_repair"]["blocks"][0])
    check("D7", "no repair channels recorded", {}, rec["repair_channels"])
    # OA-8: one policy per run, checked from the records themselves.
    on = one(as_response(cfg), sanitise=True)
    check("D7", "symmetric run passes", True,
          assert_symmetric([rec, one(as_response(cfg), sanitise=False)])["symmetric"])
    try:
        assert_symmetric([rec, on])
        asymmetric_detected = False
    except AssertionError:
        asymmetric_detected = True
    check("D7", "asymmetric application across a run is refused (OA-8)", True,
          asymmetric_detected)


# ------------------------------------------------------------------------ D8

def _seeded_text(prompt, params, seed):
    rng = random.Random(seed)
    cfg = config(n_blocks=rng.choice([3, 4, 5]),
                 conv_type=rng.choice(K.FIELD_VOCAB["conv_type"]),
                 channels=rng.choice(K.FIELD_VOCAB["channels"]))
    return as_response(cfg) + f"\n(seed trace {rng.random():.12f})"


def d8() -> None:
    a = harness(_seeded_text).generate_one(cell=cell(), batch=0, index_in_batch=0,
                                           prompt="P")
    b = harness(_seeded_text).generate_one(cell=cell(), batch=0, index_in_batch=0,
                                           prompt="P")
    check("D8", "same (batch, index) -> same generation seed",
          a["generation_seed"], b["generation_seed"])
    check("D8", "raw text is byte-identical", a["raw_text"], b["raw_text"])
    check("D8", "raw_text_sha256 identical", a["raw_text_sha256"],
          b["raw_text_sha256"])
    c = harness(_seeded_text).generate_one(cell=cell(), batch=0, index_in_batch=1,
                                           prompt="P")
    check("D8", "a different index draws a different seed", True,
          a["generation_seed"] != c["generation_seed"])
    check("D8", "…and therefore different text (the check is not vacuous)", True,
          a["raw_text"] != c["raw_text"])
    check("D8", "registered batch seed is still S[0] (§2.3)", K.SEEDS[0], a["seed"])


# ------------------------------------------------------------------------ D9

def d9() -> dict:
    """The mechanism the anchor-tracking column rests on."""
    findings: dict = {}
    absent_activation = as_response(config(activation=None))
    illegal_activation = as_response(config(activation="ELU"))

    can_first = ordered_vocab("activation", "canonical")[0]      # relu
    rev_first = ordered_vocab("activation", "reversed")[0]       # mish
    note("D9", "canonical first-enumerated activation", can_first)
    note("D9", "reversed  first-enumerated activation", rev_first)

    can = one(absent_activation, order="canonical")
    rev = one(absent_activation, order="reversed")
    ok_fill_can = check("D9", "FILLED under canonical -> canonical first",
                        [can_first] * 3, can["repair_destinations"]["activation"])
    ok_fill_rev = check("D9", "FILLED under reversed -> REVERSED first",
                        [rev_first] * 3, rev["repair_destinations"]["activation"])
    check("D9", "filled value under reversed is not the canonical first", True,
          rev["spec_post_repair"]["blocks"][0]["activation"] != can_first)

    can_c = one(illegal_activation, order="canonical")
    rev_c = one(illegal_activation, order="reversed")
    ok_coerce = (check("D9", "COERCED under canonical -> canonical first",
                       [can_first] * 3, can_c["repair_destinations"]["activation"])
                 and check("D9", "COERCED under reversed -> REVERSED first",
                           [rev_first] * 3, rev_c["repair_destinations"]["activation"]))

    # …and the same fact as the tracking scorer sees it, which is what X5 reads.
    h = harness(absent_activation)
    recs = h.generate_batch(cell=cell("reversed", "modal", n_per_batch=20), batch=0,
                            prompt=P.compose_e1("schema", "reversed", "modal"))
    specs = [r["spec_post_repair"] for r in recs]
    modal, tied = A.modal_value(specs, "activation", "reversed")
    tr = A.batch_tracking(specs, "reversed", "modal")
    ok_scorer = (check("D9", "scorer: modal activation under reversed", rev_first, modal)
                 and check("D9", "scorer: tracks_first indicator on that field", 1,
                           tr.per_field_first["activation"]))
    check("D9", "scorer: modal ties on that field", False, tied)
    note("D9", "batch tracks_first (all six collapsed fields)", tr.tracks_first)

    findings["holds"] = bool(ok_fill_can and ok_fill_rev and ok_coerce and ok_scorer)
    if not findings["holds"]:
        findings["blocking"] = (
            "BLOCKING: the repair target does not move with the enumeration "
            "order. The anchor-tracking column measures nothing and X5 is "
            "vacuous. Report; do not adjust."
        )
    return findings


# ----------------------------------------------------------------------- D10

def _cell_script(prompt, params, seed):
    """Deterministic, seed-keyed, and deliberately mixed: legal generations,
    coercions, fills, and unparseable prose, so a round-trip exercises every
    quantity the scorers consume."""
    rng = random.Random(seed)
    roll = rng.random()
    if roll < 0.10:
        return "No JSON here: the model described the network in prose instead."
    cfg = config(n_blocks=rng.choice([3, 4]),
                 conv_type=rng.choice(K.FIELD_VOCAB["conv_type"]),
                 channels=rng.choice(K.FIELD_VOCAB["channels"]),
                 pooling=rng.choice(K.FIELD_VOCAB["pooling"]))
    if roll < 0.25:
        for blk in cfg["blocks"]:
            blk["activation"] = "ELU"          # coerced
    elif roll < 0.40:
        for blk in cfg["blocks"]:
            blk.pop("normalization", None)     # filled
    return as_response(cfg) + f"\n(trace {rng.random():.9f})"


REQUIRED_HEADER = {
    "schema_version", "experiment", "plan_revision", "plan_sha256",
    "plan_supersedes_sha256", "plan_chain_sha256", "code_commit", "generated_at",
    "environment", "model", "prompts", "seeds", "n_batches_per_cell",
    "b_tracking", "r_final", "field_collapse_entropy_threshold",
    "exemplar_values", "chance_rates", "tracking_label_rule", "d_rand",
    "bootstrap", "confirmatory_family_size", "alpha", "discreteness_gate",
    "generations", "cells", "statistics", "na_counts", "failures",
}
REQUIRED_GENERATION = {
    "generation_id", "cell_id", "batch", "index_in_batch", "seed",
    "enumeration_order", "exemplar", "raw_text", "raw_text_sha256",
    "finish_reason", "parse_outcome", "parse_error", "spec_pre_repair",
    "spec_post_repair", "repair_channels", "metrics_computed_at",
}
REQUIRED_BATCH = {
    "batch", "seed", "n", "parse_failures", "generation_ids", "D_pre", "D_post",
    "S", "empty_trigram_count", "field_entropy_pre", "field_entropy_post",
    "repair_channels", "collapsed_fields_pre", "collapsed_fields_post",
    "modal_value_pre", "modal_value_post", "tracks_first_pre", "tracks_first_post",
    "tracks_exemplar_pre", "tracks_exemplar_post", "n_first_pre", "n_first_post",
    "n_exemplar_pre", "n_exemplar_post", "modal_tie_count",
}
REQUIRED_CELL = {
    "cell_id", "factors", "seed_honoured", "batches", "D_pre_mean", "D_pre_std",
    "D_post_mean", "D_post_std", "D_pre_pooled", "D_pre_pooled_ci95",
    "D_post_pooled", "D_post_pooled_ci95", "S_mean", "S_std", "S_pooled",
    "S_pooled_ci95", "tracks_first_pre_mean", "tracks_first_pre_ci95",
    "tracks_first_post_mean", "tracks_first_post_ci95",
    "tracks_exemplar_pre_mean", "tracks_exemplar_pre_ci95",
    "tracks_exemplar_post_mean", "tracks_exemplar_post_ci95",
    "chance_rate_applied_first", "chance_rate_applied_exemplar",
    "cross_level_exemplar", "null_batches", "null_S_batches",
    "null_tracking_batches_first", "null_tracking_batches_exemplar",
    "label_pre", "label_post", "label_tracking_grid", "label_tracking_unread",
    "tracking_predicate_outcome", "boundary_straddle", "status",
}


def d10() -> None:
    spec = cell("canonical", "modal", cell_id="KAT_ANCHOR",
                n_batches=K.N_BATCHES_PER_CELL, n_per_batch=K.N_GENERATIONS_PER_BATCH)
    h = harness(_cell_script)
    prompt = P.compose_e1("schema", "canonical", "modal")
    records = h.generate_cell(cell=spec, prompt=prompt)
    check("D10", "generations produced", 16 * 20, len(records))

    cellrec = cell_record(spec, records)

    em = ResultsEmitter(experiment="E1")
    em.model = h.run_manifest()
    em.prompts = P.prompt_hashes()
    specs = [{"id": "X5.anchor", "permutation_mode": "monte_carlo",
              "n_permutations": 100_000}]
    specs += [{"id": f"PAD{i}", "permutation_mode": "paired_exact",
               "n_pairs_planned": K.N_BATCHES_PER_CELL}
              for i in range(K.FAMILY_SIZE - 2)]
    specs += [{"id": "X3.frontier", "permutation_mode": "not_applicable"}]
    em.declare_confirmatory_design(specs)

    em.add_generations(records)
    em.add_cell(cellrec)
    em.add_statistic({
        "id": "X5.anchor", "kind": "paired_permutation",
        "contrast_operands": {
            "left": {"cell_id": spec.cell_id, "stage": "post_repair",
                     "quantity": "tracks_first"},
            "right": {"cell_id": spec.cell_id, "stage": "post_repair",
                      "quantity": "tracks_first"}},
        "contrast": "canonical vs reversed enumeration order",
        "paired": True, "pairing_key": ["batch", "exemplar"],
        "permutation_mode": "monte_carlo", "test_statistic": "difference_of_means",
        "n_permutations": 100_000, "permutation_seed": K.BOOTSTRAP_SEED,
        "estimate": None, "p": None, "confirmatory": True, "significant": None,
        "status": "fixture_no_contrast_run",
    })
    for i in range(K.FAMILY_SIZE - 2):
        em.add_statistic({"id": f"PAD{i}", "kind": "paired_permutation",
                          "permutation_mode": "paired_exact", "n_pairs_planned": 16,
                          "n_pairs_realised": 16, "p": 0.5, "confirmatory": True,
                          "significant": False})
    em.add_statistic(not_applicable_slot("X3.frontier", "no precision factor"))
    em.add_delta({"id": "bf16.fixture", "column": "bf16", "from_cell": spec.cell_id,
                  "to_cell": spec.cell_id, "stage": "post_repair",
                  "delta_d_mean": 0.0, "ci95": [None, None],
                  "destination_label": "", "label": ""})

    path = ROOT / "results" / "_fixture_S3_1_harness.json"
    em.write(str(path))
    doc = json.loads(path.read_text())

    # ---- every registered field present -----------------------------------
    check("D10", "header fields missing", set(), REQUIRED_HEADER - set(doc))
    check("D10", "generation fields missing", set(),
          REQUIRED_GENERATION - set(doc["generations"][0]))
    check("D10", "cell fields missing", set(), REQUIRED_CELL - set(doc["cells"][0]))
    check("D10", "batch fields missing", set(),
          REQUIRED_BATCH - set(doc["cells"][0]["batches"][0]))
    check("D10", "prompt hashes carried into the header", 11,
          len(doc["prompts"]))
    check("D10", "model served recorded (OA-3)", "stub::Qwen/Qwen3-1.7B",
          doc["model"]["served"])
    check("D10", "enable_thinking recorded True (OA-15)", True,
          doc["model"]["enable_thinking"])
    check("D10", "truncation_chars is null (OA-15)", None,
          doc["model"]["truncation_chars"])

    # ---- replay: recompute every batch quantity from generations[] alone ---
    gens: dict[tuple[int, int], dict] = {}
    for g in doc["generations"]:
        gens[(g["batch"], g["index_in_batch"])] = g

    mismatches = []
    for b in doc["cells"][0]["batches"]:
        idx = sorted(i for (bb, i) in gens if bb == b["batch"])
        recs = [gens[(b["batch"], i)] for i in idx]
        pre = [r["spec_pre_repair"] for r in recs
               if r["parse_outcome"] == "parsed" and r["spec_pre_repair"]]
        post = [r["spec_post_repair"] for r in recs
                if r["parse_outcome"] == "parsed" and r["spec_post_repair"]]
        texts = [r["raw_text"] for r in recs if r["raw_text"] is not None]
        s_val, n_empty = batch_surface_diversity(texts)
        replayed = {
            "n": len(recs),
            "parse_failures": sum(1 for r in recs
                                  if r["parse_outcome"] == "parse_failed"),
            "D_pre": batch_diversity(pre), "D_post": batch_diversity(post),
            "S": s_val, "empty_trigram_count": n_empty,
            "field_entropy_post": {f: normalised_field_entropy(post, f)
                                   for f in K.PER_BLOCK_FIELDS},
            "collapsed_fields_post": A.collapsed_fields(post),
            "tracks_first_post": A.batch_tracking(post, "canonical",
                                                  "modal").tracks_first,
            "generation_ids": [r["generation_id"] for r in recs],
        }
        for key, val in replayed.items():
            if b[key] != val:
                mismatches.append({"batch": b["batch"], "field": key,
                                   "stored": b[key], "replayed": val})
    check("D10", "batch quantities that do not replay", [], mismatches)

    # ---- replay: cell aggregates ------------------------------------------
    import statistics as st
    d_post = [b["D_post"] for b in doc["cells"][0]["batches"] if b["D_post"] is not None]
    check("D10", "D_post_mean replays", round(st.fmean(d_post), 12),
          round(doc["cells"][0]["D_post_mean"], 12))
    check("D10", "D_post_std replays", round(st.stdev(d_post), 12),
          round(doc["cells"][0]["D_post_std"], 12))

    # ---- every quantity the scorers consume is present ---------------------
    c = doc["cells"][0]
    consumed = {
        "level columns (D_pre_mean / D_post_mean)":
            c["D_pre_mean"] is not None and c["D_post_mean"] is not None,
        "change columns (deltas[])": bool(doc.get("deltas")),
        "tracking grid (label_tracking_grid)": set(c["label_tracking_grid"]) ==
            {"pre_first", "post_first", "cross_level"},
        "unread tracks_exemplar labels (A21, S3C-03)":
            set(c["label_tracking_unread"]) == {"pre_exemplar", "post_exemplar"},
        "chance rate actually applied (A22)":
            c["chance_rate_applied_first"] is not None,
        "per-field modal values (A23)":
            all("modal_value_post" in b for b in c["batches"]),
        "cross-level slot (A27)": "cross_level_exemplar" in c,
        "repair channels (A5)": bool(c["batches"][0]["repair_channels"]),
    }
    check("D10", "scorer inputs absent from the record", [],
          [k for k, v in consumed.items() if not v])
    note("D10", "results file bytes", path.stat().st_size)
    note("D10", "cell D_post_mean", doc["cells"][0]["D_post_mean"])
    note("D10", "cell tracks_first_post_mean",
         doc["cells"][0]["tracks_first_post_mean"])


# ------------------------------------------------------- structural invariant

def structural() -> None:
    """The calling layer must not branch on backend (S3-1 Block B)."""
    src = (ROOT / "src" / "harness" / "generate.py").read_text()
    leaked = [k for k in ("local_bf16", "local_nf4", "hosted_api", '"stub"')
              if k in src]
    check("STRUCT", "backend kinds named in the calling layer", [], leaked)
    cfg = (ROOT / "src" / "harness" / "config.py").read_text()
    check("STRUCT", "the one branch on backend kind lives in build_backend",
          True, "def build_backend" in cfg)
    # "no silent retries" as a structural fact rather than a word search:
    # generate_one calls the backend exactly once and contains no loop at all,
    # so there is nowhere for a resubmission to hide.
    import ast
    tree = ast.parse(src)
    fn = next(n for n in ast.walk(tree)
              if isinstance(n, ast.FunctionDef) and n.name == "generate_one")
    calls = [n for n in ast.walk(fn) if isinstance(n, ast.Call)
             and isinstance(n.func, ast.Attribute) and n.func.attr == "generate"]
    loops = [n for n in ast.walk(fn) if isinstance(n, (ast.For, ast.While))]
    check("STRUCT", "backend calls inside generate_one", 1, len(calls))
    check("STRUCT", "loops inside generate_one (a retry would need one)", 0,
          len(loops))
    check("STRUCT", "no sleep in the calling layer", True, "sleep(" not in src)


def main() -> int:
    d1(); d2(); d3(); d4(); d5(); d6(); d7(); d8()
    d9_findings = d9()
    d10()
    structural()

    width = max(len(r["what"]) for r in RESULTS)
    current = None
    for r in RESULTS:
        if r["test"] != current:
            current = r["test"]
            print(f"\n--- {current} " + "-" * (width - len(current) + 20))
        mark = "ok  " if r["pass"] else "FAIL"
        exp, act = repr(r["expected"]), repr(r["actual"])
        if r["expected"] == "(recorded)":
            print(f"  {mark} {r['what']:<{width}}  {act}")
        else:
            print(f"  {mark} {r['what']:<{width}}  expected {exp}")
            if not r["pass"]:
                print(f"       {'':<{width}}  ACTUAL   {act}")

    failed = [r for r in RESULTS if not r["pass"]]

    def jsonable(v):
        if isinstance(v, (str, int, float, bool)) or v is None:
            return v
        if isinstance(v, dict):
            return {str(k): jsonable(x) for k, x in v.items()}
        if isinstance(v, (list, tuple)):
            return [jsonable(x) for x in v]
        if isinstance(v, (set, frozenset)):
            return sorted(str(x) for x in v)
        return repr(v)

    out = {"tests": [{**r, "expected": jsonable(r["expected"]),
                      "actual": jsonable(r["actual"])} for r in RESULTS],
           "n_checks": len(RESULTS), "n_failed": len(failed),
           "d9": d9_findings}
    (ROOT / "audit" / "S3_1_KAT.json").write_text(json.dumps(out, indent=2) + "\n")
    print(f"\n{len(RESULTS) - len(failed)}/{len(RESULTS)} checks passed")
    if not d9_findings["holds"]:
        print("\n" + d9_findings["blocking"])
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

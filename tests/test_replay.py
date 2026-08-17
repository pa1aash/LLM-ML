"""Block D — replay test.

A results file that cannot regenerate its own numbers is not a provenance record,
it is an assertion. This builds a fixture results file using the schema EXACTLY as
plan §5.5 specifies — no added fields — and then tries to recompute every
statistic in it from the record's own stored inputs, comparing bit for bit.

What cannot be replayed is the finding. Nothing here amends the schema.
"""

from __future__ import annotations

import json
import random
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emit import constants as K  # noqa: E402
from emit.emitter import ResultsEmitter, not_applicable_slot  # noqa: E402
from emit.metrics import batch_diversity, batch_surface_diversity, pooled_diversity  # noqa: E402
from emit.sampler import sample_batches  # noqa: E402
from emit.stats import cliffs_delta, mean_std, paired_signflip_p  # noqa: E402

FINDINGS: list[dict] = []


def note(field: str, replayable: bool, reason: str) -> None:
    FINDINGS.append({"field": field, "replayable": replayable, "reason": reason})


def build_fixture(path: Path) -> dict:
    """Two cells, 16 batches each, one real paired contrast, family padded to 16."""
    rng = random.Random(31337)

    cells = []
    truth = {}
    for cell_id, shift in (("CELL_A", 0.0), ("CELL_B", -0.25)):
        batches_cfgs = sample_batches(K.N_BATCHES_PER_CELL, K.N_GENERATIONS_PER_BATCH,
                                      seed=900 + int(shift * 100))
        batch_records = []
        d_values = []
        for i, cfgs in enumerate(batches_cfgs):
            # Degrade diversity deterministically for CELL_B by collapsing a
            # fraction of each batch onto the batch's first configuration.
            if shift:
                k = int(len(cfgs) * 0.6)
                cfgs = [cfgs[0]] * k + cfgs[k:]
            d_post = batch_diversity(cfgs)
            texts = [json.dumps(c, sort_keys=True) for c in cfgs]
            s_val, n_empty = batch_surface_diversity(texts)
            d_values.append(d_post)
            batch_records.append({
                "batch": i,
                "seed": K.SEEDS[i],
                "n": len(cfgs),
                "parse_failures": 0,
                "D_pre": d_post,
                "D_post": d_post,
                "S": s_val,
                "empty_trigram_count": n_empty,
                "field_entropy_pre": {},
                "field_entropy_post": {},
                "repair_channels": {},
            })
            truth.setdefault(cell_id, {}).setdefault("configs", []).extend(cfgs)
        mean, std = mean_std(d_values)
        flat = truth[cell_id]["configs"]
        cells.append({
            "cell_id": cell_id,
            "factors": {"model": "fixture", "format": "schema",
                        "precision": "NF4", "temperature": 0.7},
            "seed_honoured": True,
            "batches": batch_records,
            "D_pre_mean": mean, "D_pre_std": std,
            "D_post_mean": mean, "D_post_std": std,
            "D_pre_pooled": pooled_diversity(flat),
            "D_pre_pooled_ci95": [None, None],
            "D_post_pooled": pooled_diversity(flat),
            "D_post_pooled_ci95": [None, None],
            "S_mean": statistics.fmean([b["S"] for b in batch_records]),
            "S_std": statistics.stdev([b["S"] for b in batch_records]),
            "S_pooled": None, "S_pooled_ci95": [None, None],
            "null_batches": 0, "null_S_batches": 0,
            "label_pre": "", "label_post": "",
            "boundary_straddle": False,
            "status": "ok",
        })

    a = [b["D_post"] for b in cells[0]["batches"]]
    b = [b["D_post"] for b in cells[1]["batches"]]
    diffs = [x - y for x, y in zip(a, b)]
    p, t_obs, n_ext, total = paired_signflip_p(diffs)
    delta, u = cliffs_delta(a, b)

    specs = [{"id": "X1.fixture", "permutation_mode": "paired_exact",
              "n_pairs_planned": K.N_BATCHES_PER_CELL}]
    n_pad = K.FAMILY_SIZE - 2  # one real contrast + one not_applicable slot
    specs += [{"id": f"PAD{i}", "permutation_mode": "paired_exact",
               "n_pairs_planned": K.N_BATCHES_PER_CELL} for i in range(n_pad)]
    specs += [{"id": "X3.frontier", "permutation_mode": "not_applicable"}]

    em = ResultsEmitter(experiment="E1")
    em.declare_confirmatory_design(specs)
    for c in cells:
        em.add_cell(c)

    em.add_statistic({
        "id": "X1.fixture",
        "kind": "paired_permutation",
        "contrast": "CELL_A vs CELL_B",       # free text, exactly as §5.5 shows
        "paired": True,
        # NOTE: plan §5.5's own worked example writes "exact" here, which is not
        # one of the modes §5.2's floor computation recognises. Using the enum
        # §5.2 requires. See the implementation defect report.
        "permutation_mode": "paired_exact",
        "n_pairs_planned": K.N_BATCHES_PER_CELL,
        "n_pairs_realised": K.N_BATCHES_PER_CELL,
        "n_permutations": total,
        "min_attainable_p_planned": 2 / 2 ** K.N_BATCHES_PER_CELL,
        "min_attainable_p_realised": 2 / 2 ** K.N_BATCHES_PER_CELL,
        "estimate": t_obs,
        "ci95": [None, None],
        "delta_ci95_boot": [None, None],
        "p": p,
        "confirmatory": True,
        "significant": p < K.ALPHA,
        "effect": {"metric": "cliffs_delta", "value": delta,
                   "ci95": [None, None], "u_stat": u},
        "status": "ok",
    })
    for i in range(n_pad):
        em.add_statistic({
            "id": f"PAD{i}", "kind": "paired_permutation", "contrast": "pad",
            "paired": True, "permutation_mode": "paired_exact",
            "n_pairs_planned": 16, "n_pairs_realised": 16, "n_permutations": 65536,
            "estimate": 0.0, "p": 0.5, "confirmatory": True, "significant": False,
        })
    em.add_statistic(not_applicable_slot("X3.frontier", "no precision factor on a hosted API"))

    doc = em.write(str(path))
    return doc


def replay(doc: dict) -> None:
    cells = {c["cell_id"]: c for c in doc["cells"]}

    # ---- 1. batch means and stds: stored per batch, so replayable ------------
    ok_all = True
    for c in doc["cells"]:
        d = [b["D_post"] for b in c["batches"]]
        mean, std = mean_std(d)
        ok = (mean == c["D_post_mean"]) and (std == c["D_post_std"])
        ok_all &= ok
    note("cells[].D_post_mean / D_post_std", ok_all,
         "recomputed bit-exactly from cells[].batches[].D_post" if ok_all
         else "MISMATCH on recomputation")

    # ---- 2. the paired contrast --------------------------------------------
    stat = next(s for s in doc["statistics"] if s["id"] == "X1.fixture")
    # The schema gives the operand cells ONLY as a free-text `contrast` string.
    # Replay therefore requires parsing prose. Done here to prove the point.
    left, right = [t.strip() for t in stat["contrast"].split(" vs ")]
    if left not in cells or right not in cells:
        note("statistics[].contrast -> operand cells", False,
             "free-text contrast does not resolve to cell_ids; replay impossible "
             "without out-of-band knowledge")
    else:
        a = [b["D_post"] for b in cells[left]["batches"]]
        b_ = [b["D_post"] for b in cells[right]["batches"]]
        diffs = [x - y for x, y in zip(a, b_)]
        p, t_obs, _, total = paired_signflip_p(diffs)
        ok = (p == stat["p"]) and (t_obs == stat["estimate"]) and (total == stat["n_permutations"])
        note("statistics[].p / estimate (paired permutation)", ok,
             "recomputed bit-exactly, but ONLY because the free-text contrast "
             "string happened to be parseable as two cell_ids; the schema does "
             "not require that" if ok else "MISMATCH")

        delta, u = cliffs_delta(a, b_)
        ok2 = (delta == stat["effect"]["value"]) and (u == stat["effect"]["u_stat"])
        note("statistics[].effect.cliffs_delta / u_stat", ok2,
             "recomputed bit-exactly from the same batch-level operands" if ok2
             else "MISMATCH")

        # Which stage? The statistic does not say whether it compares D_pre or
        # D_post. Here both are equal by construction, hiding the ambiguity.
        note("statistics[] -> which stage (D_pre vs D_post)", False,
             "no field identifies the operand stage; only the prose `contrast` "
             "hints at it, and it is not machine-readable")

    # ---- 3. generation-level quantities -------------------------------------
    note("cells[].D_post_pooled", False,
         "pooled D is a mean over all C(320,2) GENERATION pairs; the schema "
         "stores no per-generation design vectors, only per-batch aggregates")
    note("cells[].D_post_pooled_ci95 (bootstrap)", False,
         "BCa bootstrap resamples GENERATIONS (§2.4.5); with no per-generation "
         "record the resample cannot be reconstructed even given bootstrap_seed")
    note("cells[].S_pooled / S_pooled_ci95", False,
         "S is computed on RAW GENERATED TEXT; no text is stored anywhere in the "
         "schema, so S can never be replayed from a results file")
    note("cells[].batches[].S", False,
         "same: the per-batch S value is stored but its input text is not")
    note("cells[].batches[].field_entropy_*", False,
         "entropy pools field values across every block position of every "
         "generation; not derivable from stored aggregates")
    note("cells[].batches[].repair_channels", True,
         "counts ARE the primitive record; nothing upstream is needed")
    note("E2 runs[] -> Y1..Y4", False,
         "§5.5 names runs[] but never specifies its fields, so no E2 statistic "
         "has a defined replay path")

    ok3 = doc["discreteness_gate"]["verdict"] == "pass"
    note("discreteness_gate", ok3,
         "floors recomputable from per_test[].n_planned alone" if ok3 else "gate failed")


def main() -> int:
    path = ROOT / "results" / "_fixture_E1.json"
    doc = build_fixture(path)
    reloaded = json.loads(path.read_text())
    assert reloaded == json.loads(json.dumps(doc)), "round-trip through JSON changed the document"
    replay(reloaded)

    w = max(len(f["field"]) for f in FINDINGS)
    print(f"{'FIELD'.ljust(w)}  REPLAYABLE  REASON")
    print("-" * (w + 76))
    for f in FINDINGS:
        mark = "yes       " if f["replayable"] else "NO        "
        print(f"{f['field'].ljust(w)}  {mark}  {f['reason']}")
    n_ok = sum(1 for f in FINDINGS if f["replayable"])
    print()
    print(f"{n_ok}/{len(FINDINGS)} inspected quantities are replayable from the "
          f"schema as plan §5.5 specifies it.")
    print(f"fixture written: {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

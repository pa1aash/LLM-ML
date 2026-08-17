"""Block D — plan-to-code coverage check.

Forward:  every cell in R4's §2.5 prediction table must map to a quantity the
          emitter emits, at the stage the table assumes.
Reverse:  every quantity the scorers consume must be produced by a registered
          emitter field, not computed ad hoc.

A gap in either direction is a finding.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emit import constants as K  # noqa: E402
from emit.signature import COLUMNS, COLUMN_KIND, RIVALS  # noqa: E402

# Registered schema fields, transcribed from R4 §5.5 (schema_version 1.3.0).
CELL_FIELDS = {
    "cell_id", "factors", "seed_honoured", "batches",
    "D_pre_mean", "D_pre_std", "D_post_mean", "D_post_std",
    "D_pre_pooled", "D_pre_pooled_ci95", "D_post_pooled", "D_post_pooled_ci95",
    "S_mean", "S_std", "S_pooled", "S_pooled_ci95",
    "tracks_first_post_mean", "tracks_first_post_ci95",
    "tracks_exemplar_post_mean", "tracks_exemplar_post_ci95",
    "null_batches", "null_S_batches", "null_tracking_batches",
    "label_pre", "label_post", "label_tracking",
    "boundary_straddle", "status",
}
BATCH_FIELDS = {
    "batch", "seed", "n", "parse_failures", "generation_ids",
    "D_pre", "D_post", "S", "empty_trigram_count",
    "field_entropy_pre", "field_entropy_post", "repair_channels",
    "collapsed_fields_pre", "collapsed_fields_post",
    "tracks_first_pre", "tracks_first_post",
    "tracks_exemplar_pre", "tracks_exemplar_post", "modal_tie_count",
}
HEADER_FIELDS = {"d_rand", "alpha", "confirmatory_family_size", "seeds",
                 "n_batches_per_cell", "bootstrap", "discreteness_gate"}

FORWARD: list[dict] = []
REVERSE: list[dict] = []


def fwd(column: str, quantity: str, stage: str, field: str, ok: bool, note: str = ""):
    FORWARD.append({"column": column, "quantity": quantity, "stage": stage,
                    "field": field, "ok": ok, "note": note})


def rev(consumed: str, produced_by: str, ok: bool, note: str = ""):
    REVERSE.append({"consumed": consumed, "produced_by": produced_by,
                    "ok": ok, "note": note})


def forward_check():
    # --- level columns -----------------------------------------------------
    fwd("free_prose", "D_mean", "post_repair", "cells[].D_post_mean",
        "D_post_mean" in CELL_FIELDS)
    fwd("schema_pre_repair", "D_mean", "pre_repair", "cells[].D_pre_mean",
        "D_pre_mean" in CELL_FIELDS)
    fwd("post_repair", "D_mean", "post_repair", "cells[].D_post_mean",
        "D_post_mean" in CELL_FIELDS)

    # --- change columns ----------------------------------------------------
    fwd("bf16", "delta of D_mean", "post_repair",
        "cells[].D_post_mean (two cells)", "D_post_mean" in CELL_FIELDS,
        "the DIFFERENCE itself has no registered field; it is derived at "
        "analysis time from two cells")
    fwd("high_temp", "delta of D_mean", "post_repair",
        "cells[].D_post_mean (two cells)", "D_post_mean" in CELL_FIELDS,
        "same: no registered field holds the delta")

    # --- the tracking column: four quantities, two stages ------------------
    fwd("anchor_tracking", "tracks_first", "post_repair",
        "cells[].tracks_first_post_mean / _ci95",
        "tracks_first_post_mean" in CELL_FIELDS)
    fwd("anchor_tracking", "tracks_exemplar", "post_repair",
        "cells[].tracks_exemplar_post_mean / _ci95",
        "tracks_exemplar_post_mean" in CELL_FIELDS)
    fwd("anchor_tracking", "tracks_first", "PRE_repair",
        "cells[].tracks_first_pre_mean / _ci95",
        "tracks_first_pre_mean" in CELL_FIELDS,
        "MISSING. The repair-artifact and format-tax rows both hinge on the "
        "PRE-repair value, but the cell schema registers only the POST-repair "
        "aggregates. Only the per-BATCH pre value exists.")
    fwd("anchor_tracking", "tracks_exemplar", "PRE_repair",
        "cells[].tracks_exemplar_pre_mean / _ci95",
        "tracks_exemplar_pre_mean" in CELL_FIELDS,
        "MISSING, same reason.")
    fwd("anchor_tracking", "label", "both stages", "cells[].label_tracking",
        "label_tracking" in CELL_FIELDS,
        "ONE label field for a column whose predictions are a 2x2 grid over "
        "(stage x quantity); it cannot carry the pattern the rivals predict")

    # --- collapse classification the tracking column depends on ------------
    fwd("anchor_tracking", "which fields are collapsed", "both",
        "cells[].batches[].collapsed_fields_pre/post",
        "collapsed_fields_pre" in BATCH_FIELDS and "collapsed_fields_post" in BATCH_FIELDS,
        "field present, but NO THRESHOLD is registered that defines it (S3B-01)")

    # --- indeterminacy inputs ----------------------------------------------
    fwd("free_prose", "parse rate (for the <50% rule)", "n/a",
        "cells[].batches[].parse_failures", "parse_failures" in BATCH_FIELDS)
    fwd("all level/change", "boundary straddle", "n/a",
        "cells[].boundary_straddle", "boundary_straddle" in CELL_FIELDS)
    fwd("all", "D_rand (threshold denominator)", "n/a", "header d_rand",
        "d_rand" in HEADER_FIELDS)


def reverse_check():
    rev("D_rand", "header d_rand + constants.D_RAND", True)
    rev("D_mean per cell per stage", "cells[].D_{pre,post}_mean", True)
    rev("batch D values (for the paired contrast)",
        "cells[].batches[].D_{pre,post}", True)
    rev("per-field normalised entropy", "cells[].batches[].field_entropy_{pre,post}",
        True, "emitted; the collapse THRESHOLD applied to it is not registered")
    rev("collapsed-field list", "cells[].batches[].collapsed_fields_{pre,post}", True)
    rev("modal value per field", "NOT EMITTED", False,
        "the scorer derives modal(f) from the generation-level specs. "
        "generations[].spec_{pre,post}_repair carries them, so it is derivable — "
        "but no field records the modal value itself, so a reader cannot check "
        "the tracking indicator without recomputing from raw specs")
    rev("enumeration order per cell", "cells[].factors.enumeration_order", True)
    rev("exemplar per cell", "cells[].factors.exemplar", True)
    rev("the exemplar's VALUE per field", "NOT EMITTED", False,
        "R4 §2.8 names the exemplar only in prose (3x3/ReLU/BatchNorm vs "
        "depthwise-separable/GELU/GroupNorm); no schema field carries the "
        "value map, and it is undefined for channels/skip_connection/pooling")
    rev("modal_tie_count", "cells[].batches[].modal_tie_count", True)
    rev("tracks_* per batch", "cells[].batches[].tracks_*_{pre,post}", True)
    rev("tracks_* cell aggregate + CI", "cells[].tracks_*_post_mean/_ci95", False,
        "POST only; the PRE aggregate has no registered field (see forward check)")
    rev("chance rate per field", "NOT EMITTED", False,
        "derivable from constants.FIELD_VOCAB, but the per-field rule proposed "
        "for revision 5 needs it recorded per cell to be auditable")
    rev("n_scoreable / winning threshold", "signature_match.n_scoreable / "
        "winning_threshold", True)
    rev("indeterminate columns", "signature_match.indeterminate_columns", True)


def main() -> int:
    forward_check()
    reverse_check()

    print("FORWARD — every §2.5 prediction cell maps to an emitted quantity\n")
    w = max(len(f"{r['column']}/{r['quantity']}") for r in FORWARD)
    for r in FORWARD:
        key = f"{r['column']}/{r['quantity']}"
        print(f"  {key.ljust(w)}  stage={r['stage']:<12} "
              f"{'OK ' if r['ok'] else 'GAP'}  {r['field']}")
        if r["note"]:
            print(f"  {' ' * w}    -> {r['note']}")
    gaps_f = [r for r in FORWARD if not r["ok"]]
    print(f"\n  {len(FORWARD) - len(gaps_f)}/{len(FORWARD)} forward mappings resolve.")

    print("\n\nREVERSE — every quantity the scorers consume is a registered field\n")
    w2 = max(len(r["consumed"]) for r in REVERSE)
    for r in REVERSE:
        print(f"  {r['consumed'].ljust(w2)}  {'OK ' if r['ok'] else 'GAP'}  "
              f"{r['produced_by']}")
        if r["note"]:
            print(f"  {' ' * w2}    -> {r['note']}")
    gaps_r = [r for r in REVERSE if not r["ok"]]
    print(f"\n  {len(REVERSE) - len(gaps_r)}/{len(REVERSE)} consumed quantities are "
          f"registered fields.")

    print(f"\n\nTOTAL GAPS: {len(gaps_f)} forward, {len(gaps_r)} reverse")
    for r in gaps_f + gaps_r:
        label = r.get("column", r.get("consumed"))
        print(f"  - {label}: {r['note'][:100]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

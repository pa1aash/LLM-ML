"""generations[] -> batches[] -> cells[]  (plan §5.5, §2.4).

The generation records are the ground layer: §5.5's D-21 requires that every
pooled, bootstrapped or entropy quantity be recomputable from them alone. This
module is the forward direction — records in, the batch and cell dictionaries
§5.5 registers out. `tests/test_harness.py` D10 goes the other way, recomputing
each aggregate straight from a reloaded results file, so agreement between the
two is a check rather than a tautology.

Every quantity here is computed by the S3a/S3b primitives (`emit.metrics`,
`emit.anchor`), not reimplemented, so the fixtures that pin those pin these.
"""

from __future__ import annotations

import statistics as _stats
from typing import Any, Sequence

from emit import anchor as A
from emit import constants as K
from emit.metrics import (batch_diversity, batch_surface_diversity,
                          normalised_field_entropy)

from .parse import REPAIR_CHANNELS


def _specs(records: Sequence[dict], stage: str) -> list[dict]:
    key = "spec_pre_repair" if stage == "pre" else "spec_post_repair"
    return [r[key] for r in records
            if r.get("parse_outcome") == "parsed" and r.get(key) is not None]


def batch_record(records: Sequence[dict], *, batch: int, order: str,
                 exemplar: str) -> dict[str, Any]:
    """One §5.5 `cells[].batches[]` entry, from that batch's generations."""
    pre = _specs(records, "pre")
    post = _specs(records, "post")
    texts = [r["raw_text"] for r in records if r.get("raw_text") is not None]

    s_val, n_empty = batch_surface_diversity(texts) if texts else (None, 0)

    ex_level = exemplar if exemplar in A.EXEMPLARS else "modal"
    tr_pre = A.batch_tracking(pre, order, ex_level) if pre else None
    tr_post = A.batch_tracking(post, order, ex_level) if post else None

    channels: dict[str, dict[str, int]] = {}
    for r in records:
        for f, chans in (r.get("repair_channels") or {}).items():
            slot = channels.setdefault(f, {c: 0 for c in REPAIR_CHANNELS})
            for c in chans:
                slot[c] = slot.get(c, 0) + 1

    def modal_map(specs: list[dict]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for f in K.PER_BLOCK_FIELDS:
            out[f] = A.modal_value(specs, f, order)[0] if specs else None
        return out

    return {
        "batch": batch,
        "seed": records[0]["seed"] if records else None,
        "n": len(records),
        "parse_failures": sum(1 for r in records
                              if r.get("parse_outcome") == "parse_failed"),
        "backend_errors": sum(1 for r in records
                              if r.get("status") == "backend_error"),
        "generation_ids": [r["generation_id"] for r in records],
        "D_pre": batch_diversity(pre),
        "D_post": batch_diversity(post),
        "S": s_val,
        "empty_trigram_count": n_empty,
        "field_entropy_pre": {f: normalised_field_entropy(pre, f)
                              for f in K.PER_BLOCK_FIELDS},
        "field_entropy_post": {f: normalised_field_entropy(post, f)
                               for f in K.PER_BLOCK_FIELDS},
        "repair_channels": channels,
        "collapsed_fields_pre": A.collapsed_fields(pre) if pre else [],
        "collapsed_fields_post": A.collapsed_fields(post) if post else [],
        "modal_value_pre": modal_map(pre),
        "modal_value_post": modal_map(post),
        "tracks_first_pre": tr_pre.tracks_first if tr_pre else None,
        "tracks_first_post": tr_post.tracks_first if tr_post else None,
        "tracks_exemplar_pre": tr_pre.tracks_exemplar if tr_pre else None,
        "tracks_exemplar_post": tr_post.tracks_exemplar if tr_post else None,
        "n_first_pre": tr_pre.n_first if tr_pre else 0,
        "n_first_post": tr_post.n_first if tr_post else 0,
        "n_exemplar_pre": tr_pre.n_exemplar if tr_pre else 0,
        "n_exemplar_post": tr_post.n_exemplar if tr_post else 0,
        "modal_tie_count": ((tr_pre.modal_tie_count if tr_pre else 0)
                            + (tr_post.modal_tie_count if tr_post else 0)),
    }


def _mean_std(xs: list[float]) -> tuple[float | None, float | None]:
    vals = [x for x in xs if x is not None]
    if not vals:
        return None, None
    return _stats.fmean(vals), (_stats.stdev(vals) if len(vals) > 1 else 0.0)


def cell_record(cell: Any, records: Sequence[dict],
                n_boot: int = K.BOOTSTRAP_RESAMPLES,
                boot_seed: int = K.BOOTSTRAP_SEED) -> dict[str, Any]:
    """One §5.5 `cells[]` entry.

    `D_*_pooled_ci95` is left null here: §2.4.5's pooled interval resamples
    GENERATIONS and recomputes a C(N,2) pairwise mean per resample, which is an
    analysis-layer computation, not a harness one. The point estimates are
    emitted; the interval is filled by the analysis layer.
    """
    by_batch: dict[int, list[dict]] = {}
    for r in records:
        by_batch.setdefault(r["batch"], []).append(r)

    batches = [batch_record(sorted(rs, key=lambda r: r["index_in_batch"]),
                            batch=b, order=cell.enumeration_order,
                            exemplar=cell.exemplar)
               for b, rs in sorted(by_batch.items())]

    d_pre_mean, d_pre_std = _mean_std([b["D_pre"] for b in batches])
    d_post_mean, d_post_std = _mean_std([b["D_post"] for b in batches])
    s_mean, s_std = _mean_std([b["S"] for b in batches])

    ex_level = cell.exemplar if cell.exemplar in A.EXEMPLARS else "modal"
    tracking: dict[str, Any] = {}
    for stage in ("pre", "post"):
        bts = [A.batch_tracking(_specs(sorted(rs, key=lambda r: r["index_in_batch"]),
                                       stage),
                                cell.enumeration_order, ex_level)
               for _, rs in sorted(by_batch.items())]
        for quantity in ("tracks_first", "tracks_exemplar"):
            tracking[f"{quantity}_{stage}"] = A.cell_tracking(
                bts, quantity, n_boot, boot_seed).to_json()

    all_pre = _specs(records, "pre")
    all_post = _specs(records, "post")

    def ci(key: str) -> list:
        c = tracking[key]["ci95"]
        return list(c) if c else [None, None]

    return {
        "cell_id": cell.cell_id,
        "factors": cell.to_factors(),
        "seed_honoured": True,
        "batches": batches,
        "D_pre_mean": d_pre_mean, "D_pre_std": d_pre_std,
        "D_post_mean": d_post_mean, "D_post_std": d_post_std,
        "D_pre_pooled": batch_diversity(all_pre),
        "D_pre_pooled_ci95": [None, None],
        "D_post_pooled": batch_diversity(all_post),
        "D_post_pooled_ci95": [None, None],
        "S_mean": s_mean, "S_std": s_std,
        "S_pooled": None, "S_pooled_ci95": [None, None],
        "tracks_first_pre_mean": tracking["tracks_first_pre"]["point"],
        "tracks_first_pre_ci95": ci("tracks_first_pre"),
        "tracks_first_post_mean": tracking["tracks_first_post"]["point"],
        "tracks_first_post_ci95": ci("tracks_first_post"),
        "tracks_exemplar_pre_mean": tracking["tracks_exemplar_pre"]["point"],
        "tracks_exemplar_pre_ci95": ci("tracks_exemplar_pre"),
        "tracks_exemplar_post_mean": tracking["tracks_exemplar_post"]["point"],
        "tracks_exemplar_post_ci95": ci("tracks_exemplar_post"),
        "chance_rate_applied_first": tracking["tracks_first_post"]["chance_rate"],
        "chance_rate_applied_exemplar": tracking["tracks_exemplar_post"]["chance_rate"],
        "cross_level_exemplar": {"point": None, "ci95": [None, None],
                                 "n_batches_used": 0, "n_null_batches": 0,
                                 "chance_rate": 0.0, "label_registered": "",
                                 "reason": "requires both exemplar cells"},
        "null_batches": sum(1 for b in batches if b["D_post"] is None),
        "null_S_batches": sum(1 for b in batches if b["S"] is None),
        "null_tracking_batches_first":
            tracking["tracks_first_post"]["n_null_batches"],
        "null_tracking_batches_exemplar":
            tracking["tracks_exemplar_post"]["n_null_batches"],
        "label_pre": "", "label_post": "",
        "label_tracking_grid": {"pre_first": tracking["tracks_first_pre"]["label_registered"],
                                "post_first": tracking["tracks_first_post"]["label_registered"],
                                "cross_level": ""},
        "label_tracking_unread": {
            "pre_exemplar": tracking["tracks_exemplar_pre"]["label_registered"],
            "post_exemplar": tracking["tracks_exemplar_post"]["label_registered"]},
        "tracking_detail": tracking,
        "tracking_predicate_outcome": {"repair_artifact": "", "format_tax": "",
                                       "quantisation": "", "decoding": "",
                                       "genuine_prior": ""},
        "boundary_straddle": False,
        "status": "ok",
    }

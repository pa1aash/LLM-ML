"""Verify the NAS-Bench-201 / NATS-Bench downloads and extract the accuracy table.

Plan §3.1: E2's substrate is the NATS-Bench topology search space (TSS), 15,625
architectures, validation and test accuracy by table lookup.

Two jobs, deliberately in one script so the table can never exist without its
provenance record:

  1. hash every downloaded artifact and compare against the PUBLISHED value,
     which for these files is a truncated MD5 fragment embedded in the filename
     and nothing more (DEVIATIONS.md D-013);
  2. extract validation and test accuracy for all 15,625 architectures on all
     three tasks into one compact table, and hash that too.

The binaries stay gitignored; `results/checksums/nasbench201.json` is tracked.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets" / "nasbench201"
SIMPLE_DIR = DATA / "NATS-tss-v1_0-3ffb9-simple"
TABLE_PATH = DATA / "nb201_tss_accuracy_table.json"
RECORD_PATH = ROOT / "results" / "checksums" / "nasbench201.json"

TASKS = {
    # task -> (dataset key for validation, dataset key for test)
    # NATS-Bench reports CIFAR-10's validation split under `cifar10-valid` and
    # its test accuracy under `cifar10` (trained on train+val), which is the
    # benchmark's own convention, not a choice made here.
    "cifar10": ("cifar10-valid", "cifar10"),
    "cifar100": ("cifar100", "cifar100"),
    "ImageNet16-120": ("ImageNet16-120", "ImageNet16-120"),
}

SOURCES = {
    "NATS-tss-v1_0-3ffb9-simple.tar": {
        "url": "https://drive.google.com/file/d/17_saCsj_krKjlCBLOJEpNtzPXArMCqxU",
        "published": "3ffb9",
        "published_form": "MD5 fragment embedded in the filename, per the "
                          "NATS-Bench README naming pattern "
                          "NATS-[tss/sss]-[version]-[md5sum]-simple.tar",
    },
    "NATS-tss-v1_0-3ffb9.pickle.pbz2": {
        "url": "https://drive.google.com/file/d/1vzyK0UVH2D3fTpa1_dSWnp1gvGpAxRul",
        "published": "3ffb9",
        "published_form": "MD5 fragment embedded in the filename; this is the "
                          "benchmark data file the fragment is generated from",
    },
}


def digests(path: Path) -> dict:
    md5, sha = hashlib.md5(), hashlib.sha256()
    n = 0
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            md5.update(chunk)
            sha.update(chunk)
            n += len(chunk)
    return {"bytes": n, "md5": md5.hexdigest(), "sha256": sha.hexdigest()}


def verify() -> dict:
    out = {}
    for name, meta in SOURCES.items():
        path = DATA / name
        if not path.exists():
            out[name] = {**meta, "present": False,
                         "verdict": "ABSENT — not downloaded"}
            continue
        d = digests(path)
        frag = meta["published"].lower()
        found = frag in d["md5"]
        where = d["md5"].find(frag)
        out[name] = {
            **meta, "present": True, **d,
            "fragment_found_in_md5": found,
            "fragment_offset_in_md5": where if found else None,
            "verdict": ("MATCH — the published fragment appears in the computed "
                        f"MD5 at offset {where}" if found else
                        "NO MATCH — the published fragment does not appear in "
                        "the computed MD5 of this file"),
        }
    return out


def _final_epoch_mean(results: dict, dataset: str, key: str) -> float:
    """Mean over the benchmark's available seeds of one final-epoch metric.

    This is exactly what `nats_bench.get_more_info(..., hp="200",
    is_random=False)` returns, computed directly so the table can be built by a
    single sequential pass over the archive instead of 15,625 random reads.
    `verify_against_api` checks the two agree.
    """
    vals = []
    for (ds, _seed), inner in results.items():
        if ds != dataset:
            continue
        acc = inner["eval_acc1es"].get(f"{key}@{inner['epochs'] - 1}")
        if acc is not None:
            vals.append(acc)
    if not vals:
        raise KeyError(f"{dataset}/{key} absent")
    return sum(vals) / len(vals)


#: task -> (dataset, validation key, dataset, test key), in the benchmark's own
#: vocabulary. CIFAR-10's validation split lives under `cifar10-valid` and its
#: test accuracy under `cifar10`, which is the benchmark's convention.
METRIC_KEYS = {
    "cifar10": ("cifar10-valid", "x-valid", "cifar10", "ori-test"),
    "cifar100": ("cifar100", "x-valid", "cifar100", "x-test"),
    "ImageNet16-120": ("ImageNet16-120", "x-valid", "ImageNet16-120", "x-test"),
}


def extract_table(n: int = 15625) -> dict:
    """One sequential pass over the tar archive; six numbers per architecture.

    The random-access route (the `nats_bench` API over the unpacked directory)
    reads 15,625 small files and, on a memory-constrained machine, spends its
    time in page-cache thrash rather than in decompression. Streaming the tar in
    archive order is the same data read once, in order.
    """
    import bz2      # noqa: PLC0415
    import pickle   # noqa: PLC0415
    import tarfile  # noqa: PLC0415

    table: dict[str, dict[str, list]] = {
        t: {"valid": [None] * n, "test": [None] * n} for t in METRIC_KEYS
    }
    seen = 0
    t0 = time.time()
    with tarfile.open(DATA / "NATS-tss-v1_0-3ffb9-simple.tar") as tf:
        for member in tf:
            m = re.fullmatch(r".*/(\d{6})\.pickle\.pbz2", member.name)
            if not m:
                continue
            index = int(m.group(1))
            fh = tf.extractfile(member)
            if fh is None:
                continue
            data = pickle.loads(bz2.decompress(fh.read()))
            results = data["200"]["all_results"]
            for task, (vds, vkey, tds, tkey) in METRIC_KEYS.items():
                table[task]["valid"][index] = _final_epoch_mean(results, vds, vkey)
                table[task]["test"][index] = _final_epoch_mean(results, tds, tkey)
            seen += 1
            if seen % 2500 == 0:
                print(f"    {seen}/{n}  {time.time() - t0:.0f}s", flush=True)
    print(f"  extracted {seen} architectures in {time.time() - t0:.0f}s")
    missing = [t for t in table if any(v is None for v in table[t]["valid"])]
    if seen != n or missing:
        raise RuntimeError(f"incomplete extraction: {seen}/{n}, gaps in {missing}")
    return {"n_architectures": n, "hp": "200", "is_random": False,
            "source": "NATS-tss-v1_0-3ffb9-simple",
            "extraction": "sequential tar pass; final-epoch accuracy averaged "
                          "over the benchmark's available seeds",
            "tasks": table}


def verify_against_api(table: dict, sample: int = 25) -> dict:
    """Cross-check the fast path against `nats_bench` itself, on a sample.

    A hand-rolled reader that silently disagreed with the published API would
    put a wrong table under every E2 number, so the agreement is measured rather
    than assumed.
    """
    import random  # noqa: PLC0415

    from nats_bench import create  # noqa: PLC0415

    api = create(str(SIMPLE_DIR), "tss", fast_mode=True, verbose=False)
    rng = random.Random(20260819)
    idxs = rng.sample(range(table["n_architectures"]), sample)
    worst = 0.0
    checked = 0
    for i in idxs:
        for task, (vkey, tkey) in TASKS.items():
            vinfo = api.get_more_info(i, vkey, hp="200", is_random=False)
            tinfo = (vinfo if tkey == vkey else
                     api.get_more_info(i, tkey, hp="200", is_random=False))
            worst = max(worst,
                        abs(table["tasks"][task]["valid"][i] - vinfo["valid-accuracy"]),
                        abs(table["tasks"][task]["test"][i] - tinfo["test-accuracy"]))
            checked += 2
        api.clear_params(i)
    return {"architectures_sampled": sample, "values_compared": checked,
            "max_absolute_disagreement": worst,
            "pass": worst < 1e-9,
            "sampled_indices": sorted(idxs)}


def main() -> int:
    print("NAS-BENCH-201 / NATS-BENCH  (plan §3.1)\n")
    checks = verify()
    for name, rec in checks.items():
        print(f"  {name}")
        print(f"    published (expected) : {rec['published']}  "
              f"[{rec['published_form'].split(',')[0]}]")
        if rec.get("present"):
            print(f"    computed md5         : {rec['md5']}")
            print(f"    computed sha256      : {rec['sha256']}")
            print(f"    bytes                : {rec['bytes']:,}")
        print(f"    verdict              : {rec['verdict']}\n")

    if not SIMPLE_DIR.exists():
        print("  ABORT: the uncompressed benchmark directory is missing")
        return 1

    table = extract_table()
    api_check = verify_against_api(table)
    print(f"  API cross-check: {api_check['values_compared']} values on "
          f"{api_check['architectures_sampled']} architectures, "
          f"max disagreement {api_check['max_absolute_disagreement']:.2e} -> "
          f"{'PASS' if api_check['pass'] else 'FAIL'}")
    if not api_check["pass"]:
        print("  ABORT: the fast reader disagrees with nats_bench")
        return 1
    TABLE_PATH.write_text(json.dumps(table))
    tdig = digests(TABLE_PATH)
    print(f"  table written: {TABLE_PATH.relative_to(ROOT)}  "
          f"({tdig['bytes']:,} bytes)")
    print(f"  table sha256 : {tdig['sha256']}")

    record = {
        "generated_by": "scripts/build_nasbench_table.py",
        "plan_section": "3.1",
        "deviation": "DEVIATIONS.md D-013",
        "note": "The maintainers publish no full checksum for these files. The "
                "expected value is a truncated MD5 fragment embedded in the "
                "filename; the computed values are full digests. Recorded so a "
                "reader can see exactly how much assurance the published value "
                "carries.",
        "downloads": checks,
        "derived_table": {
            "path": str(TABLE_PATH.relative_to(ROOT)),
            "gitignored": True,
            "tasks": sorted(TASKS),
            "n_architectures": table["n_architectures"],
            "hp": "200", "is_random": False,
            "api_cross_check": api_check,
            **tdig,
        },
    }
    RECORD_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECORD_PATH.write_text(json.dumps(record, indent=2) + "\n")
    print(f"  record written: {RECORD_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Torch-free access to the repository's OWN uniform random sampler.

Plan §2.6 requires D_rand to be computed from "the repository's own uniform
random sampler". `src/search_space.py` imports torch at module level, and this
session may not install ML dependencies, so the module cannot be imported.

Rather than reimplement the sampler — which would silently substitute a different
distribution for the one the plan names — this module extracts the *verbatim
source text* of `SEARCH_SPACE` and `random_architecture_config` with `ast` and
executes those two nodes in a namespace containing only `random`. The extracted
source is hashed so a results file can prove which bytes were run.
"""

from __future__ import annotations

import ast
import hashlib
import os
import random
from typing import Any, Callable

_SEARCH_SPACE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "search_space.py"
)

_WANTED_FUNCS = ("random_architecture_config",)
_WANTED_ASSIGNS = ("SEARCH_SPACE",)


def extract_sampler(path: str = _SEARCH_SPACE_PATH) -> tuple[Callable, dict, str, str]:
    """Return (sampler_fn, SEARCH_SPACE, extracted_source, sha256_of_extract)."""
    with open(path, "r") as fh:
        source = fh.read()
    tree = ast.parse(source)

    chunks: list[str] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if any(n in _WANTED_ASSIGNS for n in names):
                chunks.append(ast.get_source_segment(source, node))
        elif isinstance(node, ast.FunctionDef) and node.name in _WANTED_FUNCS:
            chunks.append(ast.get_source_segment(source, node))

    missing = [n for n in _WANTED_ASSIGNS + _WANTED_FUNCS if not any(n in c for c in chunks)]
    if missing:
        raise RuntimeError(f"could not extract {missing} from {path}")

    extracted = "\n\n".join(chunks) + "\n"
    digest = hashlib.sha256(extracted.encode()).hexdigest()

    ns: dict[str, Any] = {"random": random}
    exec(compile(extracted, f"<extracted:{os.path.basename(path)}>", "exec"), ns)
    return ns["random_architecture_config"], ns["SEARCH_SPACE"], extracted, digest


def source_sha256(path: str = _SEARCH_SPACE_PATH) -> str:
    """SHA-256 of the whole search_space.py, for provenance alongside the extract."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sample_batches(n_batches: int, n_per_batch: int, seed: int) -> list[list[dict]]:
    """Draw n_batches x n_per_batch configurations from the repository's sampler.

    One `random.Random` per batch, seeded `seed + batch_index`, so batches are
    independent and the draw is reproducible from (seed, n_batches, n_per_batch).
    """
    sampler, _, _, _ = extract_sampler()
    out = []
    for b in range(n_batches):
        rng = random.Random(seed + b)
        out.append([sampler(rng) for _ in range(n_per_batch)])
    return out


def sample_flat(n: int, seed: int) -> list[dict]:
    """Draw n configurations from a single seeded stream (plan §2.6's literal form)."""
    sampler, _, _, _ = extract_sampler()
    rng = random.Random(seed)
    return [sampler(rng) for _ in range(n)]

"""The generation harness for EXPERIMENT_PLAN_R6.md.

One interface, three backends (local bf16, local NF4, hosted API) plus a stub,
selected by configuration in `config.build_backend`. The calling layer in
`generate.py` does not branch on backend.
"""

from .config import (BackendConfig, CellSpec, GenerationParams, SanitisePolicy,
                     build_backend)
from .backends import BackendError, BackendResponse
from .generate import Harness, assert_symmetric, generation_id, generation_seed
from .parse import ParseResult, SanitiseResult, parse, run_pipeline, sanitise

__all__ = [
    "BackendConfig", "BackendError", "BackendResponse", "CellSpec",
    "GenerationParams", "Harness", "SanitisePolicy", "assert_symmetric",
    "build_backend", "generation_id", "generation_seed", "parse",
    "run_pipeline", "sanitise", "ParseResult", "SanitiseResult",
]

"""Results-schema emitter for EXPERIMENT_PLAN_R3.md.

The only path by which a number reaches a results file. Every write runs the
three fatal gates first.
"""

from .constants import ALPHA, FAMILY_SIZE, SCHEMA_VERSION
from .emitter import ResultsEmitter, not_applicable_slot
from .gates import GateViolation

__all__ = [
    "ALPHA",
    "FAMILY_SIZE",
    "SCHEMA_VERSION",
    "ResultsEmitter",
    "not_applicable_slot",
    "GateViolation",
]

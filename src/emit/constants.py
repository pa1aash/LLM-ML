"""Registered constants from EXPERIMENT_PLAN_R3.md.

Every value here is stated in the governing plan. Nothing in this module is a
tuning parameter. The plan hash is recorded so a results file can be traced back
to the exact document that authorised its numbers.

Sections cited refer to EXPERIMENT_PLAN_R3.md.
"""

from __future__ import annotations

# ---------------------------------------------------------------- plan identity

PLAN_REVISION = 3
PLAN_FILENAME = "EXPERIMENT_PLAN_R3.md"
PLAN_SHA256 = "be61bda9f7b9a33dd9240ea56e010bc87bf0013495e7b0bbafeab0cbeccbdf03"
PLAN_SUPERSEDES_SHA256 = (
    "a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1"
)
PLAN_CHAIN_SHA256 = [
    "aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d",  # rev 1
    "a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1",  # rev 2
]

# §5.5. The plan specifies 1.2.0 for revision 3.
SCHEMA_VERSION = "1.2.0"

# ------------------------------------------------------- family and alpha (§5.2)

# Single source of truth. Gate 1 asserts the emitted confirmatory count equals
# FAMILY_SIZE and that every alpha_applied equals ALPHA.
FAMILY_SIZE = 16
ALPHA = 0.05 / FAMILY_SIZE  # 0.003125 exactly

# ------------------------------------------------------------------- E1 (§2.3)

N_BATCHES_PER_CELL = 16
N_GENERATIONS_PER_BATCH = 20
N_CELLS = 30

SEEDS = [
    7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008,
    7009, 7010, 7011, 7012, 7013, 7014, 7015, 7016,
]
assert len(SEEDS) == N_BATCHES_PER_CELL

# §2.7. A cell with this many null batches or more is `insufficient`.
# The 0.6 proportion is unchanged across all three revisions.
NULL_BATCH_INSUFFICIENT_THRESHOLD = 10

# ------------------------------------------------------------ bootstrap (§2.4.5)

BOOTSTRAP_RESAMPLES = 10_000
BOOTSTRAP_METHOD = "BCa"
BOOTSTRAP_SEED = 90210
BOOTSTRAP_RESAMPLING_UNIT = "generation"

# -------------------------------------------------------- design space (§2.4.1)

# The six per-block categorical fields, in the order the repository's own search
# space declares them (src/search_space.py:52-58 as cited by the plan).
PER_BLOCK_FIELDS = (
    "conv_type",
    "channels",
    "activation",
    "normalization",
    "skip_connection",
    "pooling",
)
N_PER_BLOCK_FIELDS = len(PER_BLOCK_FIELDS)  # 6, the coefficient in d's numerator

# G in the d formula (§2.4.2). NOTE: `n_blocks` is named as an architecture-level
# member of the design-choice vector in §2.4.1 but is NOT a member of G — the
# formula handles block-count mismatch through its own 6*|Bx-By| term instead.
# See the implementation defect report.
ARCH_LEVEL_FIELDS = ("global_pool", "fc_layers")

FIELD_VOCAB = {
    "conv_type": ["standard_3x3", "depthwise_separable", "dilated_3x3", "bottleneck"],
    "channels": [32, 64, 128, 256],
    "activation": ["relu", "gelu", "silu", "mish"],
    "normalization": ["batchnorm", "layernorm", "groupnorm", "none"],
    "skip_connection": ["identity", "projection", "none"],
    "pooling": ["maxpool", "avgpool", "strided_conv", "none"],
}

# ------------------------------------------------------- surface diversity (§2.4.6)

SURFACE_NGRAM_N = 3

# ------------------------------------------------------------- thresholds (§2.6)

# Fractions of D_rand. D_rand itself is measured, not assumed.
THRESHOLD_COLLAPSED = 0.15
THRESHOLD_DIVERSE = 0.60
THRESHOLD_NO_CHANGE = 0.10
THRESHOLD_RECOVERS = 0.25

# §2.6 halt condition on the measured reference.
D_RAND_SANITY_RANGE = (0.65, 0.80)

# The plan does not register a seed for the D_rand draw (§2.6 specifies the
# count and the sampler but not the seed). Registered here; see the defect report.
D_RAND_SEED = 20260817
D_RAND_N_PLAN = 200  # §2.6 literal


# -------------------------------------------------------------------- E2 (§3.4)

R_FLOOR = 20  # binding; may never be reduced (§8.2)
E2_PROPOSALS_PER_RUN = 20
E2_MONTE_CARLO_PERMUTATIONS = 100_000

E1_GENERATIONS = N_CELLS * N_BATCHES_PER_CELL * N_GENERATIONS_PER_BATCH  # 9600


def total_generations(r_final: int) -> int:
    """§3.5: 9,600 + 320*R."""
    return E1_GENERATIONS + 320 * r_final

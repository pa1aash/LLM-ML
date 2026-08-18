"""Registered constants from EXPERIMENT_PLAN_R5.md.

Every value here is stated in the governing plan. Nothing in this module is a
tuning parameter. The plan hash is recorded so a results file can be traced back
to the exact document that authorised its numbers.

Sections cited refer to EXPERIMENT_PLAN_R5.md.
"""

from __future__ import annotations

# ---------------------------------------------------------------- plan identity

PLAN_REVISION = 5
PLAN_FILENAME = "EXPERIMENT_PLAN_R5.md"
PLAN_SHA256 = "e3206e718161cc139830ff79741c6fe8f78e1d34f1147d3f644b36be2107b201"
PLAN_SUPERSEDES_SHA256 = (
    "738601db1d55e81010a62ec1e1259f82e6466f7e8db02f0ec3de4ed15d80cc9d"
)
PLAN_CHAIN_SHA256 = [
    "aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d",  # rev 1
    "a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1",  # rev 2
    "be61bda9f7b9a33dd9240ea56e010bc87bf0013495e7b0bbafeab0cbeccbdf03",  # rev 3
    "738601db1d55e81010a62ec1e1259f82e6466f7e8db02f0ec3de4ed15d80cc9d",  # rev 4
]

# §5.5. The plan specifies 1.4.0 for revision 5.
SCHEMA_VERSION = "1.4.0"

# ------------------------------------------------------- family and alpha (§5.2)

# Single source of truth. Gate 1 asserts the emitted confirmatory count equals
# FAMILY_SIZE and that every alpha_applied equals ALPHA.
#
# Revision 4 added contrast X5 (enumeration order at the anchor model), the
# seventeenth confirmatory test. X1-X4 across 3 models = 12, X5 = 1, Y1-Y4 = 4.
# Revisions 1-3 registered 16 / 0.003125.
#
# Revision 5 extends the tracking sub-design to all three models but adds NO
# test: column classification is descriptive by CI position, not a hypothesis
# test, so per-model scoring needs no per-model contrast (R5-2, plan section 2.8).
FAMILY_SIZE = 17
ALPHA = 0.05 / FAMILY_SIZE  # 0.0029411764705882353

# ------------------------------------------------------------------- E1 (§2.3)

N_BATCHES_PER_CELL = 16          # B_batch; K is reserved for block count (D-22)
N_GENERATIONS_PER_BATCH = 20
N_CELLS_MAIN_GRID = 30
# §2.8: 3 models x 2 enumeration orders x 2 exemplars (R5-2).
N_CELLS_ANCHOR = 12
N_CELLS = N_CELLS_MAIN_GRID + N_CELLS_ANCHOR  # 42

# §2.8 (R5-8). Floor plus a procedure, like R: the S3 tracking-CI-width pilot may
# raise it, and raising it is compliance rather than a deviation.
B_TRACKING_FLOOR = 16
B_TRACKING = B_TRACKING_FLOOR

# §2.4.4 (R5-4). A field is collapsed when its NORMALISED entropy falls below
# this. Mirrors D < 0.15*D_rand: both scales put the uniform reference at 1.0.
FIELD_COLLAPSE_ENTROPY_THRESHOLD = 0.15

# §2.6 (R5-1). The registered labelling rule for anchor tracking. The flat 0.50
# bar and the symmetric per-field rule are both REJECTED; see the plan for the
# measured disagreement table.
TRACKING_LABEL_RULE = "one_sided_at_chance"

SEEDS = [
    7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008,
    7009, 7010, 7011, 7012, 7013, 7014, 7015, 7016,
]
assert len(SEEDS) == N_BATCHES_PER_CELL

# §2.7. A cell with this many null batches or more is `insufficient`.
# The 0.6 proportion is unchanged across all four revisions.
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
# formula handles block-count mismatch through its own 6*|Kx-Ky| term instead,
# so including n_blocks in G as well would double-count it (D-24).
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

# §2.6 halt condition, tightened at revision 4 (defect D-10). The old
# [0.65, 0.80] admitted the repository sampler (0.7719), the block-free corrected
# sampler (0.7765) AND revision 3's own stated anchor (0.74).
D_RAND_SANITY_RANGE = (0.705, 0.735)

D_RAND_SEED = 20260817           # registered at revision 4 (D-12)
D_RAND_BLOCK_COUNTS = (3, 4, 5, 6)

# Measured from the CORRECTED uniform sampler at fixed block count, in the E1
# batch structure, averaged over K. See tests/compute_d_rand_r4.py.
D_RAND = 0.719205                # analytic 0.718872; agreement 0.000333
D_REPO_SAMPLER = 0.771931        # reported for comparability, NEVER the anchor

# §2.6 change-label bands (D-01, D-03). `partial` on a change is the band the
# plan previously left unnamed; `worsens` is the negative direction.
THRESHOLD_PARTIAL_CHANGE_LOWER = 0.10   # same edge as no-change
THRESHOLD_WORSENS = -0.10

# §2.6 signature scoring, generalised to k indeterminate columns (D-06).
N_SIGNATURE_COLUMNS = 6
SIGNATURE_WIN_FRACTION = 0.75    # winner needs >= ceil(0.75 * n_scoreable)
SIGNATURE_MIN_SCOREABLE = 4      # below this: "no verdict"

# §2.6 anchor-tracking: the REJECTED flat bar, retained only so the emitter can
# report what the rejected rule would have said (R5-1).
ANCHOR_TRACKING_THRESHOLD_REJECTED_FLAT = 0.50
ANCHOR_TRACKING_THRESHOLD = ANCHOR_TRACKING_THRESHOLD_REJECTED_FLAT

# §3.4 tractability cut for exact vs Monte-Carlo permutation (D-16).
EXACT_PERMUTATION_MAX = 10_000_000


# -------------------------------------------------------------------- E2 (§3.4)

R_FLOOR = 20  # binding; may never be reduced (§8.2)
E2_PROPOSALS_PER_RUN = 20
E2_MONTE_CARLO_PERMUTATIONS = 100_000

def e1_generations(b_tracking: int = B_TRACKING) -> int:
    """§3.5: 9,600 main grid + 240 * B_tracking anchor cells."""
    main = N_CELLS_MAIN_GRID * N_BATCHES_PER_CELL * N_GENERATIONS_PER_BATCH  # 9600
    return main + N_CELLS_ANCHOR * b_tracking * N_GENERATIONS_PER_BATCH


E1_GENERATIONS = e1_generations()  # 13,440 at the B_tracking floor


def total_generations(r_final: int, b_tracking: int = B_TRACKING) -> int:
    """§3.5: 9,600 + 240*B_tracking + 320*R."""
    return e1_generations(b_tracking) + 320 * r_final

"""Run every S3a/S3b/S3-1 check and report a single pass/fail."""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUITES = [
    ("Block B  adversarial gate tests", "tests/test_gates.py"),
    ("Block C1-C5  known-answer metrics", "tests/test_metrics.py"),
    ("R4-3  D_rand (corrected uniform) + D_repo_sampler", "tests/compute_d_rand_r4.py"),
    ("Block D  replay test", "tests/test_replay.py"),
    ("Block E  signature-match probe", "tests/probe_signature_match.py"),
    ("S3b C1-C16  scorer fixtures", "tests/test_scorers.py"),
    ("S3b Block D  plan-to-code coverage", "tests/check_coverage.py"),
    ("S3-1 Block A  prompt freeze verification", "scripts/freeze_prompts.py"),
    ("S3-1 Block D  harness D1-D10 known-answer tests", "tests/test_harness.py"),
]
fail = 0
for name, path in SUITES:
    args = ["--check"] if path.endswith("freeze_prompts.py") else []
    r = subprocess.run([sys.executable, path, *args], cwd=ROOT,
                       capture_output=True, text=True)
    status = "PASS" if r.returncode == 0 else "FAIL"
    if r.returncode:
        fail += 1
        print(r.stdout[-2000:]); print(r.stderr[-2000:])
    print(f"[{status}] {name}")
print()
print(f"{len(SUITES)-fail}/{len(SUITES)} suites passed")
sys.exit(1 if fail else 0)

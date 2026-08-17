"""Run every S3a check and report a single pass/fail."""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUITES = [
    ("Block B  adversarial gate tests", "tests/test_gates.py"),
    ("Block C1-C5  known-answer metrics", "tests/test_metrics.py"),
    ("Block C6-C7  D_rand + batch-variance probe", "tests/compute_d_rand.py"),
    ("Block D  replay test", "tests/test_replay.py"),
    ("Block E  signature-match probe", "tests/probe_signature_match.py"),
]
fail = 0
for name, path in SUITES:
    r = subprocess.run([sys.executable, path], cwd=ROOT, capture_output=True, text=True)
    status = "PASS" if r.returncode == 0 else "FAIL"
    if r.returncode:
        fail += 1
        print(r.stdout[-2000:]); print(r.stderr[-2000:])
    print(f"[{status}] {name}")
print()
print(f"{len(SUITES)-fail}/{len(SUITES)} suites passed")
sys.exit(1 if fail else 0)

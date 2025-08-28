"""Run Codex baseline checks in dry-run mode.

This script validates README metadata and verifies that cross references are
up to date without altering the repository. It exits with a non-zero status if
any problems are detected.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def run_validate_metadata() -> bool:
    """Return ``True`` if all README metadata validations succeed."""

    ls = subprocess.run(
        ["git", "ls-files", "*README*.md"], capture_output=True, text=True, cwd=ROOT
    )
    readmes = [line.strip() for line in ls.stdout.splitlines() if line.strip()]
    if not readmes:
        print("No README.md files found")
        return True

    cmd = [sys.executable, str(ROOT / "ops" / "validate_metadata.py"), *readmes]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    lines = [ln.strip() for ln in result.stdout.splitlines() if ln.strip()]
    return result.returncode == 0 and all(ln.endswith(": OK") for ln in lines)


def run_update_crossrefs() -> bool:
    """Return ``True`` if cross references are up to date."""

    cmd = [sys.executable, str(ROOT / "ops" / "update_crossrefs.py")]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    status = subprocess.run(
        ["git", "status", "--porcelain"], capture_output=True, text=True, cwd=ROOT
    )
    changed = [line for line in status.stdout.splitlines() if line and not line.startswith("??")]
    has_changes = bool(changed)
    if has_changes:
        print("Crossref updates needed:")
        print("\n".join(changed))
        subprocess.run(["git", "checkout", "--", "."], cwd=ROOT, check=False)

    return result.returncode == 0 and not has_changes


def main() -> int:
    meta_ok = run_validate_metadata()
    cross_ok = run_update_crossrefs()
    return 0 if meta_ok and cross_ok else 1


if __name__ == "__main__":  # pragma: no cover - CLI entry
    raise SystemExit(main())

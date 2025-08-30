#!/usr/bin/env python3
"""Generate a plan to remove directories not present in ``desired_dirs.txt``.

The script walks the filesystem from a base path (current directory by
default) and compares the discovered directories with the desired list.
Directories absent from the desired list are written under the ``remove`` key
of a simple YAML file.
"""
import argparse
import os
from pathlib import Path
from typing import List


def existing_dirs(base: Path) -> List[str]:
    result: List[str] = []
    for root, dirs, _ in os.walk(base):
        # Ignore hidden directories such as .git
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        rel_root = Path(root).relative_to(base)
        for d in dirs:
            path = (rel_root / d).as_posix().lstrip('./')
            result.append(path)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate SWEEP_PLAN.yaml")
    parser.add_argument("desired_dirs", help="Path to desired_dirs.txt")
    parser.add_argument(
        "output", nargs="?", default="SWEEP_PLAN.yaml", help="Output YAML file"
    )
    parser.add_argument(
        "base", nargs="?", default=".", help="Base path to inspect for existing directories"
    )
    args = parser.parse_args()

    with open(args.desired_dirs, "r", encoding="utf8") as f:
        desired = {line.strip() for line in f if line.strip()}

    base = Path(args.base)
    current = set(existing_dirs(base))
    to_remove = sorted(current - desired)

    with open(args.output, "w", encoding="utf8") as f:
        f.write("remove:\n")
        for d in to_remove:
            f.write(f"  - {d}\n")
    print(f"Wrote {len(to_remove)} remove actions to {args.output}")


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/env python3
"""Parse an ASCII tree representation and emit desired directory list.

The script expects a text file containing an ASCII tree, similar to the
output of the ``tree`` command.  Each line is inspected and directories are
extracted heuristically by stripping the tree drawing characters and using
indentation to build the path hierarchy.

Usage::

    python scripts/gen_desired_state.py ascii_view.txt desired_dirs.txt

The resulting ``desired_dirs.txt`` will contain one directory path per line.
"""
from __future__ import annotations

import argparse
import re
from typing import Iterable, List

TREE_CHARS = "│└├─"  # characters used by ``tree`` style drawings


def parse_ascii_tree(lines: Iterable[str]) -> List[str]:
    """Return a list of directory paths parsed from an ASCII tree."""
    dirs: List[str] = []
    stack: List[str] = []
    for raw in lines:
        if not raw.strip():
            continue
        # Remove tree drawing characters
        cleaned = re.sub(f"^[{TREE_CHARS} ]+", "", raw.rstrip())
        if not cleaned:
            continue
        indent = len(raw) - len(raw.lstrip())
        level = indent // 4  # assume four spaces per level
        stack = stack[:level]
        name = cleaned.strip()
        # Heuristic: ignore entries that look like files
        if "." in name:
            continue
        path = "/".join(stack + [name])
        dirs.append(path)
        stack.append(name)
    return dirs


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse ASCII tree into directory list")
    parser.add_argument("ascii_view", help="File containing ASCII tree")
    parser.add_argument("output", help="Output file for desired directories")
    args = parser.parse_args()

    with open(args.ascii_view, "r", encoding="utf8") as f:
        dirs = parse_ascii_tree(f)

    with open(args.output, "w", encoding="utf8") as f:
        f.write("\n".join(dirs) + "\n")
    print(f"Wrote {len(dirs)} directories to {args.output}")


if __name__ == "__main__":  # pragma: no cover
    main()

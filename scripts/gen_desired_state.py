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


def parse_ascii_tree(lines: Iterable[str]) -> List[str]:
    """Return a list of directory paths parsed from an ASCII tree.

    The function supports ``tree``-style drawings that may include branch
    characters (``├``, ``└``) and inline annotations like ``[CODE]`` or
    descriptions after the directory name.
    """

    dirs: List[str] = []
    stack: List[str] = []
    for raw in lines:
        line = raw.rstrip()
        if not line:
            continue

        if "├" in line or "└" in line:
            # Determine level from the prefix before the branch character.
            idx = line.find("├") if "├" in line else line.find("└")
            prefix = line[:idx]
            level = len(prefix) // 4 + 1
            cleaned = line[idx + 3 :].strip()
        else:
            # Root line (no branch characters)
            level = 0
            cleaned = line.strip()

        name = cleaned.split()[0]
        if "." in name:
            # Skip entries that look like files
            continue

        stack = stack[:level]
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

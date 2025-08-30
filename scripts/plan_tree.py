#!/usr/bin/env python3
"""Generate a plan to create directories from ``desired_dirs.txt``.

The output is a simple YAML file with a single top-level key ``create``
containing the list of directories.  The format is intentionally minimal to
avoid requiring third-party dependencies.
"""
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate TREE_PLAN.yaml")
    parser.add_argument("desired_dirs", help="Path to desired_dirs.txt")
    parser.add_argument(
        "output", nargs="?", default="TREE_PLAN.yaml", help="Output YAML file"
    )
    args = parser.parse_args()

    with open(args.desired_dirs, "r", encoding="utf8") as f:
        dirs = [line.strip() for line in f if line.strip()]

    with open(args.output, "w", encoding="utf8") as f:
        f.write("create:\n")
        for d in dirs:
            f.write(f"  - {d}\n")
    print(f"Wrote {len(dirs)} create actions to {args.output}")


if __name__ == "__main__":  # pragma: no cover
    main()

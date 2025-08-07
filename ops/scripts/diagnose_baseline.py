from __future__ import annotations

"""Generate a baseline diagnosis report.

This script reads ``baseline.csv`` in the repository root and writes a
Markdown file with tables grouped by simple file categories.
"""

from collections import defaultdict
import csv
from pathlib import Path
from typing import Dict, Iterable, List

CODE_EXTS = {"py"}
DOC_EXTS = {"md"}
CONFIG_EXTS = {"txt", "ini", "yml", "yaml"}


def _categorise(ext: str) -> str:
    ext = ext.lower()
    if ext in CODE_EXTS:
        return "code"
    if ext in DOC_EXTS:
        return "documentation"
    if ext in CONFIG_EXTS:
        return "configuration"
    return "other"


def _read_baseline(baseline_path: Path) -> Iterable[Dict[str, str]]:
    with baseline_path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def _group_by_category(rows: Iterable[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    groups: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        cat = _categorise(row["ext"])
        groups[cat].append(row)
    return groups


def _write_markdown(groups: Dict[str, List[Dict[str, str]]], output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8") as f:
        for category in sorted(groups):
            items = sorted(groups[category], key=lambda r: r["path"])
            f.write(f"## {category.capitalize()}\n\n")
            f.write("| path | ext | version | size | date | sha1 |\n")
            f.write("| --- | --- | --- | --- | --- | --- |\n")
            for row in items:
                f.write(
                    f"| {row['path']} | {row['ext']} | {row['version']} | {row['size']} | {row['date']} | {row['sha1']} |\n"
                )
            f.write("\n")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    baseline_path = repo_root / "baseline.csv"
    rows = _read_baseline(baseline_path)
    groups = _group_by_category(rows)
    output_path = Path(__file__).with_name("diagnosis.md")
    _write_markdown(groups, output_path)


if __name__ == "__main__":
    main()

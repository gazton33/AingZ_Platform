"""Sweep repository to compute file metadata and compare with blueprint."""
from __future__ import annotations

import csv
import hashlib
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Dict, Set
import re
import difflib

REPO_ROOT = Path(__file__).resolve().parent.parent
BLUEPRINT_FILE = REPO_ROOT / "rw_b_blueprint_v_4_extendido_2025_08_06.md"
BASELINE_CSV = REPO_ROOT / "baseline.csv"


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts:
            if path == BASELINE_CSV:
                continue
            yield path


def iter_all_paths(root: Path) -> Set[str]:
    paths: Set[str] = set()
    for p in root.rglob("*"):
        if ".git" in p.parts or "__pycache__" in p.parts or p == BASELINE_CSV:
            continue
        rel = p.relative_to(root).as_posix()
        if p.is_dir():
            paths.add(rel + "/")
        else:
            paths.add(rel)
    return paths


def file_sha1(path: Path) -> str:
    h = hashlib.sha1()
    with path.open("rb") as fh:
        while chunk := fh.read(8192):
            h.update(chunk)
    return h.hexdigest()


def file_version(path: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=%h", "--", str(path)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout.strip() or "-"
    except Exception:
        return "-"


def build_baseline() -> List[Dict[str, str]]:
    rows = []
    for f in iter_files(REPO_ROOT):
        rel = f.relative_to(REPO_ROOT).as_posix()
        rows.append(
            {
                "path": rel,
                "ext": f.suffix.lstrip("."),
                "version": file_version(f),
                "size": str(f.stat().st_size),
                "date": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
                "sha1": file_sha1(f),
            }
        )
    return rows


def save_baseline(rows: List[Dict[str, str]]) -> None:
    with BASELINE_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["path", "ext", "version", "size", "date", "sha1"]
        )
        writer.writeheader()
        writer.writerows(rows)


# Blueprint parsing ---------------------------------------------------------

TREE_BLOCK_RE = re.compile(r"```text(.*?)```", re.DOTALL)
LINE_RE = re.compile(r"([\s│]*)(├──|└──) (.*)")


def parse_blueprint() -> Set[str]:
    text = BLUEPRINT_FILE.read_text(encoding="utf-8")
    match = TREE_BLOCK_RE.search(text)
    if not match:
        return set()
    block = match.group(1).splitlines()
    paths: Set[str] = set()
    stack: List[str] = []
    for line in block:
        m = LINE_RE.match(line)
        if not m:
            continue
        indent, _branch, rest = m.groups()
        level = indent.count("│")
        names = extract_names(rest)
        for name in names:
            name = name.strip()
            if not name:
                continue
            is_dir = name.endswith("/")
            clean = name.rstrip("/")
            stack = stack[:level]
            current = "/".join(stack + [clean]) if clean else clean
            paths.add(current + ("/" if is_dir else ""))
            if is_dir:
                if len(stack) == level:
                    stack.append(clean)
                else:
                    stack[level] = clean
    return paths


def extract_names(rest: str) -> List[str]:
    # Remove description after ':'
    rest = rest.split(":", 1)[0]
    parts = [p.strip() for p in rest.split(",")]
    names: List[str] = []
    for part in parts:
        if "(" in part and ")" in part:
            before, after = part.split("(", 1)
            inside = after.split(")", 1)[0]
            before = before.strip()
            if "/" in before or before.endswith("."):
                name = before
            else:
                name = inside
        else:
            name = part
        names.append(name.strip())
    return names


# Comparison ---------------------------------------------------------------

def compare_tree(actual_paths: Set[str], expected_paths: Set[str]) -> Dict[str, List[str]]:
    missing = sorted(p for p in expected_paths if p not in actual_paths)
    orphan = sorted(p for p in actual_paths if p not in expected_paths)
    # Detect incorrect names by fuzzy matching
    incorrect: Dict[str, str] = {}
    for exp in missing:
        candidates = difflib.get_close_matches(exp, actual_paths, n=1, cutoff=0.8)
        if candidates:
            incorrect[exp] = candidates[0]
    legacy_files = [p for p in orphan if not p.endswith("/")]
    orphan_paths = [p for p in orphan if p.endswith("/")]
    return {
        "missing": missing,
        "incorrect": [f"{k} -> {v}" for k, v in incorrect.items()],
        "orphan_paths": orphan_paths,
        "legacy_files": legacy_files,
    }


def main() -> None:
    rows = build_baseline()
    save_baseline(rows)
    actual_paths = iter_all_paths(REPO_ROOT)
    expected_paths = parse_blueprint()
    report = compare_tree(actual_paths, expected_paths)
    for key, items in report.items():
        print(f"{key} ({len(items)}):")
        for item in items:
            print(f"  - {item}")


if __name__ == "__main__":
    main()

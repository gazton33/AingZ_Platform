import os
import re
from pathlib import Path

OK_STATUSES = {"OK", "ACTUALIZADO"}


def readme_kpi(root: Path) -> tuple[float, int, int]:
    readmes = list(root.rglob("README.md"))
    total = len(readmes)
    ok = 0
    status_pattern = re.compile(r"\*\*STATUS:\*\*\s*`([^`]+)`", re.IGNORECASE)
    for path in readmes:
        try:
            with path.open(encoding="utf-8") as fh:
                for line in fh:
                    m = status_pattern.search(line)
                    if m:
                        if m.group(1).strip().upper() in OK_STATUSES:
                            ok += 1
                        break
        except Exception:
            pass
    percent = (ok / total * 100) if total else 0.0
    return percent, ok, total


def directory_naming_kpi(root: Path) -> tuple[int, int]:
    valid_pattern = re.compile(r"^[a-z0-9_]+$")
    total = 0
    valid = 0
    for dirpath, dirnames, _ in os.walk(root):
        dirnames[:] = [
            d for d in dirnames if not (d.startswith('.') or d.startswith('__'))
        ]
        for d in dirnames:
            total += 1
            if valid_pattern.match(d):
                valid += 1
    return valid, total


def glossary_refs_kpi(root: Path) -> tuple[int, int]:
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+glossary[^)]*)\)")
    total = 0
    valid = 0
    for path in root.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        for match in link_pattern.finditer(text):
            total += 1
            target = match.group(1).split('#')[0]
            if target.startswith("http://") or target.startswith("https://"):
                continue
            if (path.parent / target).resolve().exists():
                valid += 1
    return valid, total


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    percent_ok, ok_readmes, total_readmes = readme_kpi(root)
    valid_dirs, total_dirs = directory_naming_kpi(root)
    valid_refs, total_refs = glossary_refs_kpi(root)

    print(f"README OK: {ok_readmes}/{total_readmes} ({percent_ok:.2f}%)")
    print(f"Valid directory names: {valid_dirs}/{total_dirs}")
    print(f"Glossary references updated: {valid_refs}/{total_refs}")


if __name__ == "__main__":
    main()

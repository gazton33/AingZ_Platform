"""Validate that technical terms listed in README files exist in the glossary."""
import re
import sys
from pathlib import Path

def load_glossary_terms(glossary_path: Path) -> set[str]:
    terms: set[str] = set()
    pattern = re.compile(r"^\|\s*[A-Z0-9_]+\s*\|\s*[A-Z0-9_]+\s*\|\s*(.+?)\s*\|", re.UNICODE)
    with glossary_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("|"):
                match = pattern.match(line)
                if match:
                    name_cell = re.sub(r"<[^>]+>", "", match.group(1)).strip()
                    if name_cell:
                        terms.add(name_cell.lower())
    return terms

def readme_terms(readme_path: Path) -> list[str]:
    content = readme_path.read_text(encoding="utf-8")
    m = re.search(r"##+\s*Terminology\n(.+?)(\n##|\Z)", content, re.DOTALL | re.IGNORECASE)
    if not m:
        return []
    section = m.group(1)
    terms: list[str] = []
    for line in section.splitlines():
        line = line.strip()
        if line.startswith("-"):
            term_match = re.match(r"-\s*(?:\[([^\]]+)\]|([^\[]+))", line)
            if term_match:
                term = term_match.group(1) or term_match.group(2)
                term = term.strip().lower()
                term = re.sub(r"[^a-z0-9]+", " ", term).strip()
                if term:
                    terms.append(term)
    return terms

def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    glossary = repo_root / "core/kns/glossary/rw_b_glosario_code_v_2_20250729.md"
    known_terms = load_glossary_terms(glossary)
    failures: list[str] = []
    for readme in repo_root.rglob("README.md"):
        terms = readme_terms(readme)
        if not terms:
            continue
        missing = [t for t in terms if t not in known_terms]
        if missing:
            failures.append(f"{readme}: missing terms: {', '.join(missing)}")
    if failures:
        for msg in failures:
            print(msg)
        return 1
    print("All glossary references are valid.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

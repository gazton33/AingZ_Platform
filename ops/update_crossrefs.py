import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple


def load_paths_cache(cache_path: Path) -> Dict[str, str]:
    with cache_path.open('r', encoding='utf-8') as f:
        return json.load(f)


def find_readme_files(root: Path) -> List[Path]:
    files: List[Path] = []
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        name = path.name.lower()
        if 'readme' in name and not name.startswith('informe_'):
            files.append(path)
    return files


def update_file(path: Path, mappings: Dict[str, str]) -> List[Tuple[str, str, str]]:
    content = path.read_text(encoding='utf-8')
    original = content
    updates: List[Tuple[str, str, str]] = []

    for old, new in mappings.items():
        if not new:
            continue
        if old in content and new not in content:
            content = content.replace(old, new)
            updates.append((str(path.relative_to(ROOT)), old, new))

    if content != original:
        path.write_text(content, encoding='utf-8')
    return updates


def append_log_entry(log_path: Path, file: str, action: str) -> None:
    date = datetime.now().strftime("%Y-%m-%d")
    entry = f"- {date} | {file} | {action}"
    existing = ''
    if log_path.exists():
        existing = log_path.read_text(encoding='utf-8').rstrip('\n') + '\n'
    log_path.write_text(existing + entry + '\n', encoding='utf-8')


def log_updates(root: Path, updates: List[Tuple[str, str, str]]) -> None:
    if not updates:
        return
    for file, old, new in updates:
        action = f"Updated crossref: {old} -> {new}"
        for log_name in ['changelog.md', 'lessons_learned.md']:
            append_log_entry(root / log_name, file, action)


ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    cache_path = ROOT / 'ops/paths_cache.json'
    mappings = load_paths_cache(cache_path)

    readmes = find_readme_files(ROOT)
    all_updates: List[Tuple[str, str, str]] = []
    for readme in readmes:
        all_updates.extend(update_file(readme, mappings))

    log_updates(ROOT, all_updates)


if __name__ == '__main__':
    main()

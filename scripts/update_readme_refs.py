#!/usr/bin/env python3
import os
from pathlib import Path
import re

root_dir = Path(__file__).resolve().parents[1]  # AingZ_Platform_main

# Ensure root_dir points to AingZ_Platform_main
if root_dir.name != 'AingZ_Platform_main':
    raise SystemExit('Script must reside under AingZ_Platform_main/scripts/')


def generate_precedencia(dir_path: Path) -> str:
    rel_parts = dir_path.relative_to(root_dir).parts
    lines = ["AingZ_Platform_main/"]
    for i, part in enumerate(rel_parts):
        prefix = "    " * i + "└── "
        lines.append(f"{prefix}{part}/")
    return "\n".join(lines)


def generate_procedencia(dir_path: Path) -> str:
    # List immediate subdirectories
    children = sorted([p.name for p in dir_path.iterdir() if p.is_dir()])
    base_name = dir_path.name if dir_path != root_dir else 'AingZ_Platform_main'
    lines = [f"{base_name}/"]
    if children:
        for i, name in enumerate(children):
            prefix = "├── " if i < len(children) - 1 else "└── "
            lines.append(f"{prefix}{name}/")
    else:
        lines.append("└── (sin subdirectorios)")
    return "\n".join(lines)


def lateral_refs(dir_path: Path) -> str:
    if dir_path == root_dir:
        # references to child directories
        targets = sorted([p.name for p in dir_path.iterdir() if p.is_dir()])
        refs = [f"[./{name}/]" for name in targets]
    else:
        parent = dir_path.parent
        targets = sorted([p.name for p in parent.iterdir() if p.is_dir() and p.name != dir_path.name])
        refs = [f"[../{name}/]" for name in targets]
    return ", ".join(refs) if refs else "N/A"


def update_readme(readme: Path) -> None:
    dir_path = readme.parent
    text = readme.read_text(encoding='utf-8')

    # Update lateral references
    lateral = lateral_refs(dir_path)
    text = re.sub(r"- \*\*Referencias laterales:\*\*.*", f"- **Referencias laterales:** {lateral}", text)

    # Update precedencia tree
    prec_tree = generate_precedencia(dir_path)
    text = re.sub(
        r"## 4\. Precedencia en el Árbol de Directorios\n```text\n.*?```",
        f"## 4. Precedencia en el Árbol de Directorios\n```text\n{prec_tree}\n```",
        text,
        flags=re.S,
    )

    # Update or insert procedencia tree
    proc_tree = generate_procedencia(dir_path)
    if "## 4.1 Procedencia en el Árbol de Directorios" in text:
        text = re.sub(
            r"## 4\.1 Procedencia en el Árbol de Directorios\n```text\n.*?```",
            f"## 4.1 Procedencia en el Árbol de Directorios\n```text\n{proc_tree}\n```",
            text,
            flags=re.S,
        )
    else:
        text = re.sub(
            r"(## 4\. Precedencia en el Árbol de Directorios\n```text\n.*?```)",
            r"\1\n\n## 4.1 Procedencia en el Árbol de Directorios\n```text\n" + proc_tree + "\n```",
            text,
            flags=re.S,
        )

    readme.write_text(text, encoding='utf-8')


def main():
    for readme in root_dir.rglob('README.md'):
        update_readme(readme)


if __name__ == '__main__':
    main()

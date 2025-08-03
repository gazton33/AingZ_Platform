#!/usr/bin/env python3
"""Normalize README files across the repository.

This script replaces any "README_bucket_template - copia.md" files with a
standardized "README.md" describing the purpose of the directory within
AingZ_Platform.
"""
import pathlib

def main():
    root = pathlib.Path('.').resolve()
    for path in root.rglob('README_bucket_template - copia.md'):
        directory = path.parent
        rel_dir = directory.relative_to(root).as_posix()
        new_path = directory / 'README.md'
        content = (
            f"# {rel_dir} — README\n\n"
            "Este directorio forma parte de AingZ_Platform. "
            "Documenta su objetivo dentro del RuleSet, arquitectura y "
            "ciclo de vida. Completar detalles específicos según corresponda.\n"
        )
        new_path.write_text(content, encoding='utf-8')
        path.unlink()

if __name__ == '__main__':
    main()

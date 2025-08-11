#!/usr/bin/env python3
"""Tallar READMEs al formato V4.

Busca archivos README en el repositorio (excluyendo el README raíz, plantillas e informes)
y garantiza que posean front-matter con los campos requeridos y una sección
`## OutputTemplate`. Si ya cumplen con estos requisitos, se dejan intactos.
El listado de referencias cruzadas se obtiene de `ops/paths_cache.json` si está disponible.
"""
from __future__ import annotations

from pathlib import Path
import datetime
import json
import re

ROOT = Path('.')
REQUIRED = ["CODE", "ID", "VERSION", "ROUTE", "CROSSREF", "AUTHOR", "DATE"]


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")


def write(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")


def parse_fm(txt: str):
    if not txt.startswith("---\n"):
        return None, txt
    end = txt.find("\n---", 4)
    if end == -1:
        return None, txt
    fm = txt[4:end]
    body = txt[end + 4 :].lstrip("\n")
    data = {}
    for line in fm.splitlines():
        if ":" in line and not line.strip().startswith("#"):
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data, body


def has_output_tpl(txt: str) -> bool:
    return re.search(r"^##\s*OutputTemplate\s*$", txt, flags=re.M) is not None


def mk_code(path: Path) -> str:
    base = path.parts[0] if len(path.parts) > 1 else path.stem
    base = re.sub(r"[^A-Za-z0-9]", "", base).upper()[:5] or "DOC"
    return base


def main() -> None:
    # Cargar crossrefs desde cache
    crossrefs: list[str] = []
    try:
        cache = json.loads(read(ROOT / "ops/paths_cache.json"))
        crossrefs = [cache.get(k, k) for k in list(cache.keys())]
    except Exception:
        pass

    today = datetime.date.today().isoformat()

    changed = 0
    for p in ROOT.rglob("*readme*.md"):
        if not p.is_file():
            continue
        if p.name == "README.md" and p.parent == ROOT:
            continue  # Excluir README raíz
        low = p.name.lower()
        if "template" in low or low.startswith("informe_"):
            continue  # Excluir plantillas e informes

        txt = read(p)
        fm, body = parse_fm(txt)
        if fm and all(k in fm for k in REQUIRED) and has_output_tpl(txt):
            continue  # ya V4

        CODE = mk_code(p)
        ID = p.stem + "_v4"
        VERSION = f"v4.0-{today}"
        ROUTE = str(p.as_posix())
        AUTHOR = "AingZ_Platform"
        DATE = today

        if not body or not body.strip():
            body = f"# {p.stem} (v4)\n\n"

        fm_lines = [
            "---",
            f"CODE: {CODE}",
            f"ID: {ID}",
            f"VERSION: {VERSION}",
            f"ROUTE: {ROUTE}",
            "CROSSREF:",
        ] + [f"  - {cr}" for cr in crossrefs] + [
            f"AUTHOR: {AUTHOR}",
            f"DATE: {DATE}",
            "---",
            "",
        ]

        if not has_output_tpl(body):
            body = (
                body.rstrip()
                + (
                    "\n\n## OutputTemplate\n```yaml\n"
                    "CODE:\nID:\nVERSION:\nROUTE:\nCROSSREF:\nAUTHOR:\nDATE:\n"
                    "```\n"
                )
            )

        new_txt = "\n".join(fm_lines) + body
        write(p, new_txt)
        changed += 1

    print(f"Tallado V4 aplicado a {changed} archivo(s)")


if __name__ == "__main__":
    main()

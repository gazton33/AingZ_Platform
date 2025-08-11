#!/usr/bin/env python3
"""Genera reporte de incoherencias para archivos Markdown.

Produce `ops/reports/incoherencias.md` e `ops/reports/incoherencias.json`
con detalles y severidad de inconsistencias detectadas en front-matter,
referencias cruzadas y estructura general de los archivos.
"""
from __future__ import annotations

from pathlib import Path
import datetime
import hashlib
import json
import re
from typing import Tuple

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - yaml optional
    yaml = None

ROOT = Path('.').resolve()
REPORT_DIR = ROOT / 'ops' / 'reports'
REPORT_MD = REPORT_DIR / 'incoherencias.md'
REPORT_JSON = REPORT_DIR / 'incoherencias.json'
REQUIRED = ["CODE", "ID", "VERSION", "ROUTE", "CROSSREF", "AUTHOR", "DATE"]


def read(p: Path) -> str:
    return p.read_text(encoding='utf-8', errors='ignore')


def write(p: Path, s: str) -> None:
    p.write_text(s, encoding='utf-8')


def parse_fm(txt: str) -> Tuple[dict | None, str]:
    if not txt.startswith('---'):
        return None, txt
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", txt, re.S)
    if not m:
        return None, txt
    fm_text, body = m.group(1), m.group(2)
    data = {}
    if yaml:
        try:
            data = yaml.safe_load(fm_text) or {}
        except Exception:
            data = {}
    else:
        for line in fm_text.splitlines():
            if ':' in line and not line.strip().startswith('#'):
                k, v = line.split(':', 1)
                data[k.strip()] = v.strip()
    return data, body


def has_output_template(txt: str) -> bool:
    return re.search(r"^##\s*OutputTemplate\s*$", txt, flags=re.M) is not None


def sha1_text(s: str) -> str:
    return hashlib.sha1(s.encode('utf-8')).hexdigest()


def code_ok(c: str) -> bool:
    return isinstance(c, str) and re.fullmatch(r"[A-Z0-9_]{1,5}", c or '') is not None


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    paths_cache = {}
    cache_path = ROOT / 'ops' / 'paths_cache.json'
    if cache_path.exists():
        try:
            paths_cache = json.loads(read(cache_path))
        except Exception:
            paths_cache = {}
    required_crossrefs = sorted(set(paths_cache.values())) if isinstance(paths_cache, dict) else []

    md_files = sorted([p for p in ROOT.rglob('*.md')], key=lambda q: q.as_posix())
    issues = []
    index = []
    seen_code = {}
    seen_id = {}
    seen_h1 = {}

    for p in md_files:
        rel = p.as_posix()
        txt = read(p)
        fm, body = parse_fm(txt)
        h1 = None
        m = re.search(r"^\s*#\s+(.*)$", txt, flags=re.M)
        if m:
            h1 = m.group(1).strip()

        index.append({'path': rel, 'sha1': sha1_text(txt), 'bytes': len(txt.encode('utf-8')), 'h1': h1 or ''})

        if not fm:
            issues.append({'path': rel, 'type': 'front_matter_missing', 'msg': 'Sin front-matter'})
        else:
            missing = [k for k in REQUIRED if k not in fm]
            if missing:
                issues.append({'path': rel, 'type': 'front_matter_incomplete', 'msg': f'Faltan campos {missing}'})

            c = fm.get('CODE')
            if not code_ok(c):
                issues.append({'path': rel, 'type': 'code_rule', 'msg': f"CODE inválido '{c}' (<=5, SCREAMING_SNAKE)"})

            r = fm.get('ROUTE')
            if r and r != rel:
                issues.append({'path': rel, 'type': 'route_mismatch', 'msg': f"ROUTE='{r}' no coincide con path real"})

            cr = fm.get('CROSSREF')
            if cr is None:
                issues.append({'path': rel, 'type': 'crossref_missing', 'msg': 'CROSSREF ausente'})
            else:
                if isinstance(cr, str):
                    cr_list = [cr]
                elif isinstance(cr, list):
                    cr_list = [str(x) for x in cr]
                else:
                    cr_list = []
                for ref in cr_list:
                    if ref and not (ROOT / ref).exists():
                        issues.append({'path': rel, 'type': 'crossref_broken', 'msg': f'Referencia no existe: {ref}'})
                if required_crossrefs:
                    missing_req = [req for req in required_crossrefs if req not in cr_list]
                    if missing_req:
                        issues.append({'path': rel, 'type': 'crossref_required_missing', 'msg': f'Faltan refs canónicas: {missing_req}'})

        if not has_output_template(txt):
            issues.append({'path': rel, 'type': 'outputtemplate_missing', 'msg': "Falta sección '## OutputTemplate'"})

        if fm:
            cid = fm.get('ID')
            if cid:
                seen_id.setdefault(cid, []).append(rel)
            ccode = fm.get('CODE')
            if ccode:
                seen_code.setdefault(ccode, []).append(rel)
        if h1:
            seen_h1.setdefault(h1, []).append(rel)

    for d, label in [(seen_id, 'id_duplicate'), (seen_code, 'code_duplicate'), (seen_h1, 'h1_duplicate')]:
        for k, paths in d.items():
            if len(paths) > 1:
                issues.append({'path': ', '.join(paths), 'type': label, 'msg': f"Duplicado '{k}' en {len(paths)} archivos"})

    severity_map = {
        'front_matter_missing': 'CRITICO',
        'crossref_broken': 'CRITICO',
        'outputtemplate_missing': 'CRITICO',
        'code_rule': 'CRITICO',
        'route_mismatch': 'CRITICO',
        'front_matter_incomplete': 'ALTO',
        'crossref_required_missing': 'ALTO',
        'crossref_missing': 'ALTO',
        'id_duplicate': 'MEDIO',
        'code_duplicate': 'MEDIO',
        'h1_duplicate': 'BAJO',
    }

    for it in issues:
        it['severity'] = severity_map.get(it['type'], 'MEDIO')

    by_type = {}
    by_sev = {}
    for it in issues:
        by_type[it['type']] = by_type.get(it['type'], 0) + 1
        by_sev[it['severity']] = by_sev.get(it['severity'], 0) + 1

    today = datetime.date.today().isoformat()
    fm_hdr = [
        '---',
        'CODE: RPRT',
        'ID: incoherencias_reporte_v4',
        f'VERSION: v4.0-{today}',
        'ROUTE: ops/reports/incoherencias.md',
        'CROSSREF:',
    ] + [f'  - {p}' for p in required_crossrefs] + [
        'AUTHOR: AingZ_Platform',
        f'DATE: {today}',
        '---',
        '',
    ]

    lines = ['# Reporte de Incoherencias — V4 (no-loss)', '']
    lines += ['## Resumen', '']
    lines += [f"- Archivos MD analizados: **{len(md_files)}**"]
    lines += [f"- Incoherencias totales: **{len(issues)}**", '']
    if by_sev:
        lines += ['### Por severidad', '']
        for k in ['CRITICO', 'ALTO', 'MEDIO', 'BAJO']:
            if k in by_sev:
                lines += [f"- {k}: **{by_sev[k]}**"]
        lines += ['']
    if by_type:
        lines += ['### Por tipo', '']
        for k, v in sorted(by_type.items(), key=lambda kv: kv[0]):
            lines += [f"- {k}: **{v}**"]
        lines += ['']

    if issues:
        lines += ['## Detalle', '']
        for it in issues:
            lines += [f"- `{it['path']}` — **{it['type']}** ({it['severity']}): {it['msg']}"]
        lines += ['']

    write(REPORT_JSON, json.dumps({
        'issues': issues,
        'summary_by_type': by_type,
        'summary_by_severity': by_sev,
        'scanned': len(md_files)
    }, indent=2, ensure_ascii=False))
    write(REPORT_MD, "\n".join(fm_hdr + lines))
    print(f"Reporte generado: {REPORT_MD}")


if __name__ == '__main__':
    main()

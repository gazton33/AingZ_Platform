# RULE_CODING_COMPLIANCE_V4

## 1. Mandatos (obligatorios)
- Todo README/asset debe incluir **front-matter YAML** con: `CODE, ID, VERSION, ROUTE, CROSSREF, AUTHOR, DATE`.
- Cada README debe cerrar con **OutputTemplate**.
- Crossrefs obligatorios a: **Blueprint V4**, **Master Plan V4**, **Prompt Codex v4**, **Glosario v2** y **Diccionario CODE_TRIGGERS v2**.
- Ningún PR puede mergearse si `TRG_AUDIT_TL` reporta fallos o si `ci_audit.yml` falla.

## 2. Triggers requeridos
- `TRG_CONSOLIDATE_TL`, `TRG_AUDIT_TL`, `TRG_LSWP`.

## 3. Hooks locales (sugeridos)
- `ops/hooks/pre-commit`: ejecuta `python ops/run_codex_baseline_v4_check.py` y `pytest`.
- `ops/hooks/pre-push`: re-ejecuta validaciones para garantizar consistencia.

## 4. Criterio de aceptación
- `ops/validate_metadata.py` retorna **OK** para todos los READMEs.
- `ops/update_crossrefs.py` no deja cambios pendientes.
- CI (`ci_audit.yml`) en **verde**.
- Lessons/changelog/checklist actualizados por lote (PDCA).


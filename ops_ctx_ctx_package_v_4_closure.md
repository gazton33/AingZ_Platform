---

## file: ops/ctx/CTX\_Package\_V4\_Closure.md code: CTXPK name: CtxPackageV4Closure version: v4.0 date: 2025-08-10 owner: AingZ\_Platform · RwB status: active xrf: blueprint: RwB\_Blueprint\_V4 mplan: RwB\_MasterPlan\_V4 glossary: CODE\_Glossary\_v2 dictionary: CODE\_Triggers\_v2 triggers: [TRG\_CONSOLIDATE\_TL, TRG\_AUDIT\_TL, TRG\_PURGE\_AI] chg: CHG\_main.md#ctx\_package\_v4\_closure chk: CHK\_root.md#ctx\_package\_v4\_closure

# CTX Package — Cierre de hilo (V4, no‑loss)

## Propósito

Dejar un **paquete de contexto autosuficiente** para continuar el proyecto sin depender del historial de chat. Contiene: artefactos creados, rutas exactas, orden de ejecución, validaciones, pendientes y patrones de PR.

## Artefactos creados/actualizados (rutas exactas)

- **Workflows** (`.github/workflows/`):

  - `aingz_tallado_readmes.yml` — Tallado V4 de READMEs (front‑matter + OutputTemplate).
  - `aingz_crossref_fix.yml` — Rewire de referencias según `ops/paths_cache.json`.
  - `aingz_harvest_knowledge.yml` — Índice + Corpus (no‑loss) → `ops/data/index/knowledge_index.json`, `ops/log/harvest_readmes.md`, `library/intg/Corpus_Platform_V4.md`.
  - `aingz_diff_guard.yml` — Guard no‑loss en PR de Markdown.
  - `aingz_incoherence_report.yml` — Reporte de incoherencias con **severidad** → `ops/reports/incoherencias.{md,json}`.
  - `aingz_purge_fixes_v2.yml` — **Auto‑fix** no destructivo (CRÍTICO/ALTO) + **sync** del índice.
  - `aingz_orchestrator.yml` — Orquestación en cadena (Tallado → Crossref → Harvest → Incoherences → Purge) + **validación de ****\`\`**** raíz**.

- **Plantillas / Ruleset / WF**:

  - `ops/templates/template_readme_rw_b_v_4.md` — Plantilla **no‑loss** GPT‑5/Codex‑ready (pegado de legacy íntegro + `legacy_control`).
  - `core/rulset/RULE_CODING_COMPLIANCE_V4.md` — Reglas de naming/metadatos V4.
  - `core/wf/INTG_ReadAll_Consolidate_V4.md` — WF maestro de integración y consolidación.

- **Datos/Registros** (se generan con los workflows):

  - `ops/data/index/knowledge_index.json` — Índice canónico con metadatos normalizados.
  - `ops/log/harvest_readmes.md` — Inventario literal de MD.
  - `library/intg/Corpus_Platform_V4.md` — Corpus consolidado (incluye texto completo, no‑loss).
  - `ops/reports/incoherencias.{md,json}` — Incoherencias por tipo y severidad.

## Permisos y secrets (GitHub App)

- **Secrets requeridos** (Repository secrets):
  - `APP_ID`, `INSTALLATION_ID`, `APP_PRIVATE_KEY` (PK PEM completa, multilinea).
- **Permiso de la App**: `Actions: Read & write`, `Contents: Read & write`, `Pull requests: Read & write`.
- **Opcional**: `REPO_PAT` (PAT personal) **no usado** si la App está correcta.

## Orden operativo (Runbook)

1. **Orchestrator** → Actions: *AingZ Orchestrator* (`reason: orchestrate-v4`).
2. Revisar PRs que se abran en orden: *tallado-readmes* → *crossref-fix* → *harvest* → *incoherences* → *purge-fixes*.
3. Validar checks: **CI Audit V4** (si aplica) y **AingZ Diff Guard** (debe estar ✅).
4. Mergear PRs en el mismo orden (no‑loss garantizado por Diff Guard).

> Nota: el orquestador incluye un **validador del ****\`\`**** raíz**; si falla, revisar `CROSSREF`, `CODE` (≤5 SCREAMING\_SNAKE) y `ROUTE='README.md'`.

## Criterios de validación (V4 no‑loss)

- **Front‑matter V4** presente en todos los MD críticos (`CODE, ID, VERSION, ROUTE, CROSSREF, AUTHOR, DATE`).
- **CROSSREF**: rutas existentes; incluir canónicos de `ops/paths_cache.json`.
- **Diff Guard**: `removed ≤ added + 10` (margen) en PRs de `.md`.
- **Índice** normalizado: `has_front_matter` correcto; `meta.CROSSREF` siempre **lista de strings**; sin tipos `date/datetime`.
- **Plantilla** no‑loss aplicada para nuevos assets.

## Pendientes conocidos / Próxima iteración

- **Duplicados** a resolver manualmente (reportados por `incoherencias.json`):
  - `id_duplicate`, `code_duplicate`, `h1_duplicate` (propuesta: PRs atómicos con rename/split/merge, manteniendo no‑loss en cuerpo).
- **Protección de rama** `main`: marcar como *required* → **Diff Guard** (y **CI Audit V4** si lo usás).
- **Extender paths\_cache** si incorporamos nuevos canónicos (Blueprint/MPLAN/prompt/ruleset).

## Cómo usar la plantilla de README (no‑loss)

- Crear/actualizar el README del asset usando `ops/templates/template_readme_rw_b_v_4.md`.
- **Pegar** el contenido legacy íntegro en el bloque `legacy`.
- Completar `legacy_control` con `sha1` y conteo de líneas del legacy.

## Protocolo de PR (sugerido)

- Título: `Agent: <motivo>`
- Cuerpo: breve del cambio + artefactos generados (paths) + nota “no‑loss garantizado por Diff Guard”.
- Merge: squash o merge normal; evitar rebase si el orquestador está activo.

## Anexo — rutas clave

- `ops/paths_cache.json` — fuente de canónicos para CROSSREF.
- `.github/workflows/` — todos los WFs de esta cadena.
- `library/intg/` — corpus consolidado.

---

## OutputTemplate (obligatorio)

```yaml
output_example:
  status: OK
  id_asset: ctx_package_v4_closure
  generated_by: ai
  created_at: 2025-08-10T00:00:00-03:00
  params:
    - orchestrator: enabled
    - purge_mode: CRITICO_ALTO
  result:
    - workflows:
      - .github/workflows/aingz_tallado_readmes.yml
      - .github/workflows/aingz_crossref_fix.yml
      - .github/workflows/aingz_harvest_knowledge.yml
      - .github/workflows/aingz_diff_guard.yml
      - .github/workflows/aingz_incoherence_report.yml
      - .github/workflows/aingz_purge_fixes_v2.yml
      - .github/workflows/aingz_orchestrator.yml
    - data:
      - ops/data/index/knowledge_index.json
      - ops/log/harvest_readmes.md
      - ops/reports/incoherencias.json
      - library/intg/Corpus_Platform_V4.md
  log:
    - step1: orchestrator dispatch
    - step2: pr reviews
    - step3: merge chain
```


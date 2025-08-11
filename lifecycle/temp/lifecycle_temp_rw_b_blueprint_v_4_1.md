---

## file: lifecycle/temp/rw\_b\_blueprint\_v\_4\_1.md code: BLPR name: RwB\_Blueprint\_V\_4\_1 version: v4.1 date: 2025-08-11 owner: AingZ\_Platform · RwB status: active xrf: blueprint: RwB\_Blueprint\_V4 mplan: RwB\_MasterPlan\_V4 glossary: CODE\_Glossary\_v2 dictionary: CODE\_Triggers\_v2 triggers: [TRG\_CONSOLIDATE\_TL, TRG\_AUDIT\_TL] chg: CHG\_main.md#2025-08-11-blueprint-4\_1 chk: CHK\_root.md#2025-08-11-blueprint-4\_1

# Blueprint V4.1 — Ajustes de Precedencia y Enforcement

> **Propósito**: fijar en el **árbol V4** la **precedencia normativa** (Glosario/Diccionario > Blueprint > Master Plan > RuleSets > Workflows > README > Actions/Bot > Notion > Scripts) y extender el **enforcement** (Pre/PostCheck) como contrato único entre **Chat · Actions · Bot/API · Notion**.

## 1) Contexto y objetivos V4.1

- Elimina ambigüedades entre plataformas con un **contrato I/O** estable (front‑matter + OutputTemplate + XRF + TRIGGERS).
- Define **gates** uniformes y **matrices VERSUS** para visibilidad operativa.
- Mantiene el **árbol V4** y precisa **migraciones menores** (nombres/rutas).

## 2) Precedencia normativa (obligatoria)

1. **CODE\_Glossary\_v2** — naming `CODE` ≤5, `SCREAMING_SNAKE`.
2. **CODE\_Triggers\_v2** — semántica y obligación por ciclo.
3. **Blueprint V4** — estructura/semántica de buckets.
4. **Master Plan V4** — objetivos/PDCA.
5. RuleSets operativos → Workflows → README(s) → Actions/Bot → Notion → Scripts.

## 3) Árbol V4 (válido)

```text
/
  core/
    data/  doc/  kns/  wf/
  ops/
    pipelines/  scripts/  test/  log/  templates/
  packages/
  lifecycle/
  snapshots_ctx/
  library/
```

## 4) Reglas universales (resumen)

- Ningún asset es válido sin: **(a) CODE**, **(b) ruta exacta**, **(c) WF específico**, **(d) OutputTemplate**.
- Todo asset debe incluir front‑matter con **XRF vivos** (Blueprint/MPlan/Glosario/Diccionario) y **TRIGGERS** por ciclo.
- **PDCA vivo**: registrar `CHG/CHK/CHKP/LESSONS` en cada iteración.

## 5) Enforcement (Pre/PostCheck)

**PreCheck (mínimo)**

- CODE `^[A-Z]{1,5}$` y presente en Glosario.
- `file:` = **ruta real** (árbol V4). Ruta válida.
- XRF completo y **TRIGGERS** (≥ `TRG_CONSOLIDATE_TL`).
- **OutputTemplate** presente.

**PostCheck (mínimo)**

- `status: OK` y `created_at` ISO en OutputTemplate.
- Evidencias: artefacto CI / commit / snapshot Notion.
- `CHG/CHK/CHKP/LESSONS` actualizados.

## 6) Matriz VERSUS — Plataforma × I/O × Evidencias

| Plataforma | I/O                          | Evidencias                         | Gate                  |
| ---------- | ---------------------------- | ---------------------------------- | --------------------- |
| Chat       | Markdown/MD, tablas, Mermaid | OutputTemplate en canvas + CHG/CHK | Checklist V4          |
| Actions    | Archivos/Artefactos          | Artefacto OutputTemplate + commit  | Job `PreCheck V4`     |
| Bot/API    | Comments/labels, archivos    | Comment con OutputTemplate + log   | `PreCheck V4: passed` |
| Notion     | Propiedades/DB               | Página con snapshot OutputTemplate | Props obligatorias    |

## 7) Integración Notion (DBs y campos mínimos)

- **DBs**: `Assets`, `Workflows`, `Triggers`, `CHG`, `CHK`, `LESSONS`.
- **Props**: `CODE`, `Ruta`, `Versión`, `Plataforma`, `Estado`, `XRF`, `Triggers`, `Resultado`.
- **Vistas**: Kanban por Plataforma; Timeline PDCA; Compliance V4.

## 8) Migraciones menores V4.1

- Ajustar nombres/rutas para cumplir CODE ≤5 y nuevas rutas explícitas de **WF** y **templates**.
- Consolidar READMEs con **plantilla v4.1**.

## 9) Gates de error

- `BAD_CODE_FORMAT`, `UNKNOWN_CODE`, `ROUTE_OUT_OF_BLUEPRINT`, `MISMATCH_FILE_ROUTE`, `MISSING_XRF`, `MISSING_TRIGGERS`, `NO_OUTPUTTEMPLATE`.

## 10) Checklist rápido

-

---

# OutputTemplate (obligatorio)

blueprint\_4\_1: status: OK id\_asset: BLPR\_4\_1\_2025-08-11T00:00:00Z generated\_by: ai created\_at: 2025-08-11T00:00:00Z notes: - precedence\_locked: true - enforcement\_extended: true


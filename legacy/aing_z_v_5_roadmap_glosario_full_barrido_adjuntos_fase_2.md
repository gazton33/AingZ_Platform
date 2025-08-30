---

## file: core/doc/workbench/ROADMAP\_GLOS\_FULL\_V5\_FASE2.md code: RMAP name: RoadmapGlosarioFullV5 version: v0.1 date: 2025-08-15 owner: AingZ\_Platform · RwB status: draft refs: baseline\_id: BL-2025-08-15-ARB+AST-v1.3 ctx\_package: true sources: - glos\_code\_semantics\_v\_5\_main.md (V5 MAIN en uso) - rw\_b\_glosario\_code\_v\_2\_20250729.md (histórico v2) - rw\_b\_diccionario\_code\_triggers\_v\_2\_20250729.md (histórico v2) - readme\_core\_kns\_glossary\_rw\_b\_v\_3\_2.md (README KNS) - readme\_core\_data\_dicts\_rw\_b\_v\_3\_2.md (README DICTS) - aingz\_v\_5\_baselines\_unificados\_dir\_tree\_assets\_v\_1.md (ARB+AST v1.3 LOCKED) triggers: [TRG\_CONSOLIDATE\_TL, TRG\_AUDIT\_TL] chg: CHG#fase2\_glosario\_full\_v5 chk: CHK#fase2\_glosario\_full\_v5

# Roadmap — Glosario Full V5 + Actualización Dir Tree/Assets (Fase 2)

> Objetivo: **consolidar y validar un Glosario Full V5** (sin omitir conceptos) **alineado 1:1** con el **Árbol/Assets** del baseline **v1.3 (LOCKED)**; publicar **MAPX** Glosario↔Árbol y **congelar baseline** actualizado.

---

## 1) Alcance y criterios de éxito

**Incluye:**

- Integración de **todas** las entidades/items/data de glosarios y diccionarios adjuntos.
- Normalización de **CODE ≤5**, `Name` PascalCase, `AliasFinal` (EN) y `Contract` ≤120.
- **MAPX** bidireccional Glosario↔Árbol/Assets.
- Checklist de modificaciones para **actualizar** `aingz_v_5_baselines_unificados_dir_tree_assets`.

**Éxito (DoD):**

- `GLOS_V5_FULL v1.0` (FINAL) + `MAPX v1.0` publicados.
- `CHKP` emitido; `BL-2025-08-15-ARB+AST-v1.3` → `v1.4` (**WIP**) actualizado y luego `v1.4` (**LOCKED**).

---

## 2) Roadmap por fases (WBS + entregables + criterios)

### F0 • Preparación (Día 0)

- **Tareas**: levantar baseline y fuentes; fijar reglas de naming; armar tablero de seguimiento y matrices.
- **Entregables**: este **Roadmap** + plantilla **VALM** de QA + **LSWP** para barrido.
- **Criterios**: fuentes inventariadas; owners asignados.

### F1 • Barrido LSWP 100% y Consolidación (Día 0–1)

- **Tareas**:
  1. **LSWP** (Literal Sweep) 100% de archivos adjuntos (glosarios+diccionarios+baseline).
  2. Tabla **DELTA**: V2↔V5 MAIN (códigos, secciones, conflictos, deprecaciones).
  3. Resolver **nomenclatura** y **alias** según baseline; marcar **gaps**.
- **Entregables**: **LSWP.md**, **DELTA\_V2\_V5.mtr**, **GAPS.mtr**.
- **Criterios**: cobertura 100%; conflictos clasificados (blocker/major/minor).

### F2 • Draft integrado (Día 1–2)

- **Tareas**:
  1. Generar **GLOS\_V5\_FULL\_draft.md** (secciones A–J + buckets/paths del árbol).
  2. Completar **AliasFinal** y **Contracts** homogéneos.
  3. Diseñar **MAPX v0.9** (Glosario↔Árbol/Assets).
- **Entregables**: **Glosario Full v0.9**, **MAPX v0.9**.
- **Criterios**: 0 códigos duplicados; `Contract` ≤120; validación sintáctica.

### F3 • QA + Validación cruzada (Día 2)

- **Tareas**: ejecutar **VALD/VALOG**; probar integridad de `MAPX`; check semántico con `TRIGGERS v2`.
- **Entregables**: **VALM**, **VALOG**, **RPT QA**.
- **Criterios**: 100% pass en reglas; sin conflictos con `CODE_TRIGGERS`.

### F4 • Freeze y publicación (Día 2–3)

- **Tareas**: promover **Glosario v1.0 (FINAL)**; publicar **MAPX v1.0**; emitir **CHKP** y actualizar **Dir Tree/Assets** a `v1.4`.
- **Entregables**: **GLOS\_V5\_FINAL v1.0**, **MAPX v1.0**, **CHKP-2025-08-XX**, **ARB+AST v1.4 LOCKED**.
- **Criterios**: checklist completo; ADR/CHG actualizados.

---

## 3) Plan de QA (VALD/VALM) y reglas (SOLID‑Gate)

- **DIP/Hexagonal**: glosario desacoplado de rutas; `AliasFinal` sólo para activos de árbol.
- **ISP**: tablas con ≤8 columnas; `Contract` preciso.
- **SRP**: una responsabilidad/concepto por fila; deprecaciones explícitas.
- **OCP**: extensiones por `SPEC`/`RULE` sin tocar core.
- **LSP**: tests de sustitución para adaptadores de `TRIGGERS`/`CODES` (misma semántica).

**VALM (mínima)**

- Unicidad (`CODE`, `ID`), longitud y formato.
- Cobertura de buckets del árbol; `MAPX` 1:1 sin órfanos.
- Compatibilidad con **CODE\_TRIGGERS v2** (lookups vigentes) y **V5 MAIN**.

---

## 4) Checklist de modificaciones (para Generar/Validar Glosario Full + Actualizar Árbol)

1. **Normalizar AliasFinal** según baseline en: `docs/*`, `data/semantics/*`, `ai_learn/*`, `develop/*`, `guides/*`, `log/*`.
2. **Completar modelos** faltantes en `out_template/{docs,workspaces,platform_arch,ai_tools}` (propuestos: `DOCS`, `WSPC`, `PARCH`, `ATOOL`).
3. Definir `RCNT/RunControl` y sub‑entradas (`START`, `STOP`, `RESUME`, `ROLLBACK`).
4. Consolidar `NCHK` y `NCHG` (scope, campos obligatorios) en brainstorming.
5. Publicar **MAPX** y **XRF** mínimos en `main/log/qms/`.
6. Emitir **CHKP** y bump a `ARB+AST v1.4`.

---

## 5) Barrido LSWP 100% — Resumen y acciones

> Resultado del análisis literal de todos los adjuntos (tipo, foco, highlights, acciones):

| File                                                  | Tipo             | Foco                          | Highlights                                                                                                    | Acciones                                                                                  |
| ----------------------------------------------------- | ---------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| glos\_code\_semantics\_v\_5\_main.md                  | Glosario V5 MAIN | Semántica V5 (A–J)            | `SPEC` como reemplazo de `RWB/RWS`; secciones **F**, **H**, **I** completas; feedback abierto en **E**, **F** | Adoptar `SPEC` (deprecación RWB/RWS); alinear con AliasFinal del árbol; incorporar `MAPX` |
| rw\_b\_glosario\_code\_v\_2\_20250729.md              | Glosario v2      | Vocabulario RwB histórico     | Contiene `RWB/RWS`, `WF_M`, `WK_P`, etc.                                                                      | Mapear V2→V5 (RWB/RWS→SPEC; WF\_M→WFM; WK\_P→WKP); mantener lookup en `TRIGGERS`          |
| rw\_b\_diccionario\_code\_triggers\_v\_2\_20250729.md | Diccionario      | Lookups por CODE/Prompt       | Tabla grande A–I con prompts/refs                                                                             | Validar que todos los CODE del Glosario V5 estén en este lookup o documentar sustitutos   |
| readme\_core\_kns\_glossary\_rw\_b\_v\_3\_2.md        | README           | Proceso y sincronización      | KNS/glossary se sincroniza desde `data/dicts/`                                                                | Mantener pipeline v3.2; actualizar crossrefs a V5                                         |
| readme\_core\_data\_dicts\_rw\_b\_v\_3\_2.md          | README           | Data/Dicts                    | Diccionarios vivos; sincronización con KNS                                                                    | Asegurar propagación V5→dicts                                                             |
| AINGZ\_V5\_Baselines\_Unificados\_v1\_3\_locked.md    | Baseline         | Árbol + Assets + Correcciones | AliasFinal EN; `out_template/*` y `run_control` pendientes                                                    | Usar como fuente para AliasFinal; completar pendientes y subir a v1.4                     |

**Conflictos/Decisiones**

- `RWB/RWS` (v2) **→** `SPEC` (V5). Mantener alias históricos en `Aliases` (no en `CODE`).
- `PIPE` (script) vs `Pipeline (estructura)` — usar `PIPE` para script y `PLINE`/`PIPEL` para estructura si aplica.
- Reutilización `VALD`: mismo concepto en QA/log — separar `VALD` (matrix) vs `VALOG` (log).

---

## 6) Matrices auxiliares (plantillas)

**6.1 DELTA\_V2\_V5.mtr (campos)**: `ID_v2, CODE_v2, Name_v2, CODE_v5, Name_v5, Estado{igual|rename|deprecate|nuevo}, Rationale`.

**6.2 MAPX\_GLOS\_TREE.csv (campos)**: `Path, Assets_fuente, AliasFinal, CODE, Name, Notas`.

**6.3 VALM\_GLOS.csv (campos)**: `Regla, Chequeo, Resultado, Evidencia`.

---

## 7) Riesgos y mitigaciones

- **Divergencia V2↔V5** → DELTA obligatorio + alias históricos.
- **Áreas pendientes del árbol** (`out_template/*`, `run_control`) → definir mínimos y validar en QA.
- **Lock‑in semántico** → reglas `RULE/SPEC` y `ADR` inicial documentan extensiones.

---

## 8) Milestones y fechas

- **M1 (Día 1)**: LSWP 100% + DELTA + GAPS.
- **M2 (Día 2)**: Glosario Full v0.9 + MAPX v0.9 + VALM pass.
- **M3 (Día 3)**: Glosario v1.0 (FINAL) + MAPX v1.0 + CHKP + Árbol v1.4 LOCKED.

---

## 9) OutputTemplate

```yaml
output_example:
  status: DRAFT
  id_asset: roadmap_glos_full_v5_fase2
  generated_by: ai
  created_at: 2025-08-15T00:00:00-03:00
  params:
    - phases: [F0,F1,F2,F3,F4]
    - qa: [VALM,VALD,VALOG]
  result:
    - deliverables: [GLOS_V5_FULL, MAPX, DELTA, LSWP, VALM, RPT_QA, CHKP]
  log:
    - step1: plan
    - step2: sweep
    - step3: integrate
    - step4: validate
    - step5: freeze
```


---

## file: main/data\_base/core\_actv/data/semantics/ruleset/SEM\_RULESET\_AINGZ\_V5\_v0\_1.md code: SEMR name: SemanticRulesetAingZV5 version: v0.1 date: 2025-08-15 owner: AingZ\_Platform · RwB status: draft xrf: baseline\_id: BL-2025-08-15-ARB+AST-v1.3 depends\_on: - glos\_code\_semantics\_v\_5\_main.md - rw\_b\_glosario\_code\_v\_2\_20250729.md - rw\_b\_diccionario\_code\_triggers\_v\_2\_20250729.md - readme\_core\_kns\_glossary\_rw\_b\_v\_3\_2.md - readme\_core\_data\_dicts\_rw\_b\_v\_3\_2.md triggers: [TRG\_CONSOLIDATE\_TL, TRG\_AUDIT\_TL] chg: CHG#sem\_ruleset\_v5 chk: CHK#sem\_ruleset\_v5 notes: "Reglas de semántica unificadas. Integra el espíritu **RwB (Raw\_Base)**: literalidad, no-omisión, enfoque genérico/universal."

# **Semantic Ruleset — AingZ V5 (RwB Mode)**

> **Propósito**: establecer normas de semántica y operación que aseguren **literalidad** (LSWP), **no omisión de información** por criterios subjetivos, y un **enfoque genérico/universal** del trabajo. Las reglas son **agnósticas de rutas** y se alinean al **Baseline Árbol/Assets v1.3** para los *alias\_final*.

---

## 0) Alcance y definiciones

- **RwB (Raw\_Base)**: modo operativo que **prioriza evidencia literal** y **neutralidad**; ninguna curaduría subjetiva puede eliminar datos.
- **Semántica**: conjunto de **códigos, nombres, contratos y alias** con unicidad y trazabilidad.
- **AliasFinal (EN)**: taxonomía normalizada para assets del árbol baseline.
- **MAPX**: matriz de mapeo Glosario↔Árbol/Assets.

---

## 1) Principios (obligatorios)

1. **Literalidad primero (LSWP)**: todo barrido y consolidación se hace por **evidencia textual 100%** antes de sintetizar.
2. **No‑omisión**: se preservan **todos** los ítems encontrados; las deprecaciones requieren **rationale** y **ReplacedBy**.
3. **Contrato sobre implementación**: cada término define **qué garantiza** y sus **límites observables** (≤120 chars).
4. **Unicidad**: `CODE` (≤5, SCREAMING\_SNAKE) y `ID` son únicos; `Name` en PascalCase.
5. **Agnosticismo**: sin rutas ni nombres de archivos en definiciones semánticas.
6. **Compatibilidad**: mapeos **V2→V5** conservan **alias históricos** como metadatos, no como `CODE` vigente.
7. **Interoperabilidad**: misma semántica para GPT‑5, Codex, API, GH Bot, VSC y Python.
8. **Auditabilidad**: cada cambio queda en `CHG`, validado por `VALD` y registrado en `VALOG`.
9. **AliasFinal/Idioma nativo**: usar el idioma **nativo** de la plataforma/SDK/API (usualmente inglés). En activos del árbol, respetar el *alias\_final* del baseline; `Name/Contract` en español.
10. **Separación de templates**: `out_template/*` aloja **templates de salida estructurados** para trabajos puntuales. El bucket `wf_template/` se **renombra** a `wf_playbooks/` (propuesto) y contendrá **workflows detallados paso a paso para la AI**, incluyendo en cada archivo su **OutputTemplate** específico. (Si se aprueba otro nombre, se actualiza por CHG.)
11. **Tono/Estilo GLOS V5**: el tono, taxonomía y forma de las definiciones siguen **GLOS\_Code\_Semantics\_V5\_MAIN** (neutral, técnico, imperativo; sin marketing).
12. **Prioridad de naming por plataforma**: ante ambigüedad, prevalece el naming nativo del lenguaje/plataforma/SDK objetivo (p.ej., Python/JS/CLI/YAML, GitHub Actions, VS Code, OpenAI API).

---

## 2) Reglas operativas (SEMR)

| Nº  | Regla            | Descripción                                                                                                                                                                                 | Evidencia/Artefactos         |
| --- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| R1  | **LSWP.100**     | Antes de decidir, ejecutar **Literal Sweep 100%** sobre todas las fuentes del scope.                                                                                                        | LSWP.md, RPT                 |
| R2  | **CODE.≤5**      | `CODE` máximo 5 chars, SCREAMING\_SNAKE; `Name` en PascalCase.                                                                                                                              | VALM (nomenclatura)          |
| R3  | **CONTR.120**    | `Contract` ≤120 chars, describe finalidad/garantías, no implementación.                                                                                                                     | VALM (contratos)             |
| R4  | **ALIAS.EN**     | En assets del árbol usar **AliasFinal EN** definidos en baseline; no inventar alias.                                                                                                        | MAPX, Baseline               |
| R5  | **MAPX.1:1**     | Mantener mapeo **1:1** Glosario↔Árbol; sin órfanos.                                                                                                                                         | MAPX.csv                     |
| R6  | **DEPREC.RB**    | Deprecaciones requieren `Deprecated:true` + `ReplacedBy` + **rationale**.                                                                                                                   | CHG, DELTA V2→V5             |
| R7  | **HIST.ALIAS**   | Alias históricos (`RWB`, `RWS`, etc.) se conservan como **Aliases** no vigentes.                                                                                                            | GLOS/Main                    |
| R8  | **VALD.QA**      | Ejecutar matrices de validación (`VALD`) y registrar resultados en `VALOG`.                                                                                                                 | VALD.mtx, VALOG              |
| R9  | **TRG.SYNC**     | Cambios en glosario **sincronizan** con `CODE_TRIGGERS` y `dicts` de datos.                                                                                                                 | Dicts/Triggers               |
| R10 | **XRF.MIN**      | Publicar **XRF mínima** (ID/CODE ↔ Path) para QMS.                                                                                                                                          | main/log/qms/XRF.mtx         |
| R11 | **RUNCTRL.DEF**  | Definir `RCNT` (RunControl) y sub‑entradas (`START/STOP/RESUME/ROLLBACK`) como prereq de pipeline.                                                                                          | guides/run\_control          |
| R12 | **TEMPL.MIN**    | Completar modelos mínimos `out_template/{docs,workspaces,platform_arch,ai_tools}`.                                                                                                          | out\_template/\*             |
| R13 | **LANG.NATIVE**  | Para `CODE`, `AliasFinal` y campos técnicos, usar términos nativos del lenguaje/plataforma objetivo; evitar traducciones que rompan convenciones.                                           | GLOS\_V5\_MAIN, SDK/API docs |
| R14 | **TONE.GLOSV5**  | Redactar definiciones según el tono/estructura de **GLOS\_Code\_Semantics\_V5\_MAIN**.                                                                                                      | GLOS\_V5\_MAIN               |
| R15 | **WF.PLAYBOOKS** | Renombrar `wf_template/` → `wf_playbooks/` (propuesto). Cada **playbook** define pasos, entradas/salidas, herramientas y **OutputTemplate** embebido para generar el asset bajo el ruleset. | wf\_playbooks/\*             |

---

## 3) Flujo RwB (resumen operativo)

1. **LSWP** de fuentes → 2. **DELTA V2→V5** (rename/deprec/new) → 3. **Draft integrado** (GLOS v0.9) → 4. **MAPX v0.9** → 5. **VALD/VALOG** → 6. **Freeze** (GLOS v1.0 + MAPX v1.0) → 7. **Actualizar Árbol/Assets** (v1.4 LOCKED).

---

## 4) Roles y ownership (mínimo)

- **Semantic Owner**: custodia del glosario (`GLOS`, `DCD`, `VCB`).
- **Triggers Owner**: custodia de `DTRG` (sincronización automática y revisiones).
- **Baseline Owner**: aplica alias y publica **CHKP**.

---

## 5) QA (VALM/VALD) — Checklist

-

---

## 6) Plantillas mínimas (apéndice)

### 6.1 Entrada de Glosario

```yaml
- CODE: VALD
  Name: Validation
  Contract: Verificar conformidad técnica; produce pass/fail + métricas.
  Aliases: [Validacion]
  Deprecated: false
  ReplacedBy: null
  PlatformNotes: {GPT5: "QA gates", PY: "unit/integration hooks"}
```

### 6.2 Fila MAPX

```yaml
- Path: main/data_base/core_actv/data/out_template/mtx/
  Assets: [matrix, table, record_sheet, mapping, relation, validation, comparison]
  AliasFinal: [matrix, table, record_sheet, mapping, relation, validation, comparison]
  MapTo: [MTR, TBL, RSHT, MAPX, RELN, VALD, VRS]
```

### 6.3 WF Playbook (propuesto)

```yaml
- CODE: WFPB
  Name: WorkflowPlaybook
  Contract: Instrucciones paso a paso para generar un asset bajo el ruleset; incluye OutputTemplate embebido.
  Inputs:
    - name: source_files
      type: list[path]
      required: true
    - name: params
      type: dict
      required: false
  Tools: [web.run, file_search, python, etc.]
  Preconditions: [baseline_locked, sem_ruleset_v5_applied]
  Steps:
    - id: s1
      do: LSWP.100 (leer fuentes)
      out: lswp_report
    - id: s2
      do: Normalizar (CODE≤5, Contract≤120, Lang.Native)
      out: draft_glossary
    - id: s3
      do: MAPX (1:1 Glosario↔Árbol)
      out: mapx_v0_9
  OutputTemplate:
    type: yaml
    schema:
      asset_id: str
      version: semver
      files: [paths]
      qa: {valm: pass|fail, vald: pass|fail}
```

---

## 7) OutputTemplate (del Ruleset)

```yaml
output_example:
  status: DRAFT
  id_asset: sem_ruleset_aingz_v5_v0_1
  generated_by: ai
  created_at: 2025-08-15T00:00:00-03:00
  params:
    - mode: RwB (Raw_Base)
    - alignment: baseline_alias_final
    - qa: [VALM, VALD, VALOG]
  result:
    - rules: 12
    - checklists: 8
    - templates: [glosario_item, mapx_row]
  log:
    - step1: lswp_sources
    - step2: unify_rules
    - step3: publish_semr
```


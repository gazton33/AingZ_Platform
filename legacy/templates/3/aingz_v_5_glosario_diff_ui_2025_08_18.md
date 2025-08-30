---

## file: glossary.diff.ui code: GBLDUI name: GlosarioDiffUI version: 1.0.1 date: 2025-08-18 owner: Arch status: Draft refs: [GLOS::, RULESET::, WF::, DIR::, QMS::, CHG::, TPL::] triggers: [qa\_glosario, router\_chain] changes: [CHG-2025-08-18-009] checks: [no\_file\_refs, wikilinks\_only, router\_chain\_enforced]

# UI de validación dinámica para *diffs* de glosarios

> Interacción vía casillas, listas editables y bloques YAML. Sin rutas ni URLs. Solo namespaces aprobados.

## 0) Controles rápidos

-

---

## 1) Resumen del origen a integrar

```yaml
source_summary:
  name: CodeSemanticsV5 (MAIN)
  version: v5.0.0-rc2
  date: 2025-08-12
  status: working
  scope: generico, sin rutas
  notes: "Listo para normalización a V5 canon"
```

---

## 2) Editor de mapeo Legacy→V5

> Marque la **Acción** y ajuste **Target V5**. Añada filas si faltan códigos.

| Legacy.CODE | Legacy.Name       | Mantener | Agregar | Renombrar | Deprec. | Target V5 (canon)          | Notas                           |
| ----------- | ----------------- | -------- | ------- | --------- | ------- | -------------------------- | ------------------------------- |
| RULE        | Ruleset           | [ ]      | [ ]     | [ ]       | [ ]     | [[RULESET::INDEX]]         | Autoridad normativa             |
| LITW        | LiteralWork       | [ ]      | [ ]     | [ ]       | [ ]     | [[QMS::Checklists]] · LSWP | Unificar con LSWP               |
| CFG         | Configuration     | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Config               | Por entorno                     |
| SPEC        | SpecificExtension | [ ]      | [ ]     | [ ]       | [ ]     | RULESET::SPEC              | Neutral                         |
| BLN         | Baseline          | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Baseline             | Snapshot QA                     |
| PKG         | Package           | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Package              | Release                         |
| CTX         | Context           | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Context              | Ámbito                          |
| MOD         | Module            | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Module               | Interfaz                        |
| TRG         | Trigger           | [ ]      | [ ]     | [ ]       | [ ]     | [[WF::]]                   | Solo WF::\*                     |
| PIPE        | PipelineScript    | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Script.Pipeline      | Evitar choque con [[DIR::PIPE]] |
| SCR         | Script            | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Script               | Ejecutable                      |
| TST         | Test              | [ ]      | [ ]     | [ ]       | [ ]     | QMS::Test                  | Exit codes                      |
| AUDT        | Audit             | [ ]      | [ ]     | [ ]       | [ ]     | QMS::Audit                 | Evidencia                       |
| LOG         | Log               | [ ]      | [ ]     | [ ]       | [ ]     | [[DIR::LOG]]               | Append-only                     |
| RDM         | Readme            | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Readme               | Onboarding                      |
| MTR         | Matrix            | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Matrix               | CSV/JSON                        |
| VRS         | VersusMatrix      | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Versus               | Comparativas                    |
| KNS         | Knowledge         | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Knowledge            | Núcleo                          |
| INSI        | Insight           | [ ]      | [ ]     | [ ]       | [ ]     | GLOS::Insight              | Accionable                      |

---

## 3) Deltas propuestos

> Marque **OK** en cada bloque.

### 3.1 Altas

-

### 3.2 Renombres / Reubicaciones

-

### 3.3 Deprecaciones

-

---

## 4) Patch plan — a [[GLOS::GlosarioReal]]

> Este bloque se usará para aplicar cambios.

```yaml
patch_plan:
  add:
    - LITW: {name: LiteralWork, contract: "Barrido literal 100% sin inferencia", refs: [QMS::Checklists]}
    - CFG:  {name: Configuration, contract: "Parámetros operativos declarativos", refs: []}
    - BLN:  {name: Baseline, contract: "Snapshot QA de referencia", refs: []}
    - PKG:  {name: Package, contract: "Unidad empaquetada firmada", refs: []}
    - CTX:  {name: Context, contract: "Ámbito lógico de trabajo", refs: []}
    - MOD:  {name: Module, contract: "Interfaz estable y versionada", refs: []}
    - SCR:  {name: Script, contract: "Ejecutable puntual con side‑effects controlados", refs: []}
    - MTR:  {name: Matrix, contract: "Tabla/DF. Export CSV/JSON", refs: []}
    - VRS:  {name: VersusMatrix, contract: "Comparativas con criterios trazables", refs: []}
    - KNS:  {name: Knowledge, contract: "Núcleo de saberes", refs: []}
    - INSI: {name: Insight, contract: "Hallazgo estratégico accionable", refs: []}
  rename:
    - TRG→WF: {rule: "Triggers sólo bajo WF::*", action: "mover alias TRG_* a WF::*"}
    - PIPE.script: {rule: "Evitar colisión con DIR::PIPE", target: "Script.Pipeline"}
  deprecate:
    - RWB: {replaced_by: SPEC, note: "Neutralización de marca"}
    - RWS: {replaced_by: SPEC, note: "Neutralización de marca"}
validation:
  assertions: [no_file_refs, wikilinks_only, router_chain_enforced]
```

---

## 5) Checklist de aceptación

```yaml
checklist_glossary:
  schema:
    - [ ] Cada entrada tiene {CODE, Name, Contract}
    - [ ] Sin duplicados de CODE
    - [ ] Sin rutas ni URLs
  semantics:
    - [ ] Crossrefs sólo en namespaces aprobados
    - [ ] TRG bajo WF::*
    - [ ] Publicación de E/S de PIPE sólo como [[DIR::*]]
  coverage:
    - [ ] Legacy→V5 coverage_pct == 100
    - [ ] broken_links == 0
```

---

## 6) Firma y registro

```yaml
signoff:
  reviewer: <tu_nombre>
  date: 2025-08-18
  decision: approve|changes_requested
chg_log:
  - id: CHG-2025-08-18-009
    title: UI de diff aprobada para integración
    outcome: pending
```

---

## 7) Previsualización de entradas

> Se agregarán en [[GLOS::GlosarioReal]] cuando §4 esté aprobado.

```yaml
preview_entries:
  - code: LITW
    name: LiteralWork
    definition: Barrido literal 100% sin inferencia
    scope: QA y auditoría
    refs: [QMS::Checklists]
  - code: CFG
    name: Configuration
    definition: Parámetros operativos declarativos por entorno
    scope: Global
    refs: []
  - code: BLN
    name: Baseline
    definition: Snapshot de referencia de QA
    scope: Control de calidad
    refs: []
```

---

OutputTemplate: example: diff\_review: status: READY actions\_required: [validate\_mapping, approve\_patch] coverage\_target\_pct: 100 router\_chain: [README, RULESET, PIPE] log: - step1: authoring - step2: validation


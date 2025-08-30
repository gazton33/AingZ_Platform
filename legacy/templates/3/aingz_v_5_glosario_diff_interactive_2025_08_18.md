---

## file: glossary.diff.interactive code: GBLD name: GlosarioDiffInteractive version: 1.0.0 date: 2025-08-18 owner: Arch status: Draft refs: [GLOS::, RULESET::, WF::, DIR::, QMS::, CHG::, TPL::] triggers: [qa\_glosario, router\_chain] changes: [] checks: [no\_file\_refs, wikilinks\_only, router\_chain\_enforced]

# Canvas interactivo — Revisión y validación de *diffs* de glosarios

> Política: sin rutas ni enlaces a archivos. Solo namespaces aprobados (DIR::, GLOS::, RULESET::, WF::, QMS::, CHG::, TPL::).

## 0) Instrucciones de revisión

1. Validar mapeo *Legacy→V5* en §2.
2. Confirmar altas/renombres/deprecaciones en §3.
3. Aprobar *patch plan* de integración a [[GLOS::GlosarioReal]] en §4.
4. Ejecutar checklist §5 y firmar §6.

---

## 1) Resumen del origen (versión adjunta)

```yaml
source_summary:
  name: CodeSemanticsV5 (MAIN)
  version: v5.0.0-rc2
  date: 2025-08-12
  status: working
  scope: genérico, sin rutas
  notes: "Sub-secciones listas para feedback iterativo"
```

---

## 2) Mapeo Legacy→V5 (propuesta inicial)

> Edite la columna *Acción* y el *Target V5* cuando aplique. Sin rutas.

| Legacy.CODE | Legacy.Name       | Acción                 | Target V5 (canon)          | Notas                           |
| ----------- | ----------------- | ---------------------- | -------------------------- | ------------------------------- |
| RULE        | Ruleset           | mantener               | [[RULESET::INDEX]]         | Autoridad normativa             |
| LITW        | LiteralWork       | **agregar**            | [[QMS::Checklists]] · LSWP | Unificar con LSWP en control    |
| CFG         | Configuration     | **agregar**            | GLOS::Config               | Declarar límites por entorno    |
| SPEC        | SpecificExtension | **renombrar**          | RULESET::SPEC              | Extensión neutral               |
| BLN         | Baseline          | **agregar**            | GLOS::Baseline             | Snapshot QA                     |
| PKG         | Package           | **agregar**            | GLOS::Package              | Release firmado                 |
| CTX         | Context           | **agregar**            | GLOS::Context              | Ámbito lógico                   |
| MOD         | Module            | **agregar**            | GLOS::Module               | Interfaz estable                |
| TRG         | Trigger           | **alinear**            | [[WF::]]                   | Triggers sólo bajo WF::\*       |
| PIPE        | PipelineScript    | **verificar colisión** | GLOS::Script.Pipeline      | Evitar choque con [[DIR::PIPE]] |
| SCR         | Script            | **agregar**            | GLOS::Script               | Ejecutable puntual              |
| TST         | Test              | **agregar**            | QMS::Test                  | Exit codes claros               |
| AUDT        | Audit             | **agregar**            | QMS::Audit                 | Evidencia formal                |
| LOG         | Log               | **agregar**            | [[DIR::LOG]]               | Append‑only                     |
| RDM         | Readme            | **alinear**            | GLOS::Readme               | Onboarding + contrato           |
| MTR         | Matrix            | **agregar**            | GLOS::Matrix               | CSV/JSON                        |
| VRS         | VersusMatrix      | **agregar**            | GLOS::Versus               | Comparativas                    |
| KNS         | Knowledge         | **agregar**            | GLOS::Knowledge            | Núcleo de saberes               |
| INSI        | Insight           | **agregar**            | GLOS::Insight              | Accionable                      |

> Si detecta más códigos, añádalos aquí. Este cuadro es el *backlog* vivo de normalización.

---

## 3) Deltas propuestos (auto‑clasificados)

> Revise y marque *OK*.

### 3.1 Altas (no existen en [[GLOS::GlosarioReal]])

-

### 3.2 Renombres / Reubicaciones

-

### 3.3 Deprecaciones

-

---

## 4) Patch plan — Integración a [[GLOS::GlosarioReal]]

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

## 5) Checklist de aceptación (glosario)

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
  - id: CHG-2025-08-18-008
    title: Diff validado CodeSemanticsV5 → GlosarioReal
    outcome: pending
```

---

## 7) Previsualización de entradas (si se aprueba §4)

> Estas entradas se agregarían a [[GLOS::GlosarioReal]].

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


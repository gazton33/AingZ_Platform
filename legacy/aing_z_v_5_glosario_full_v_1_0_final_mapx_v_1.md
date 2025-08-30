---

## file: main/data\_base/core\_actv/data/semantics/glossary/GLOS\_AINGZ\_V5\_FULL\_v1\_0.md code: GLOS name: AingzV5GlossaryFull version: v1.0 date: 2025-08-16 owner: AingZ\_Platform · RwB status: final refs: baseline\_id: BL-2025-08-15-ARB+AST-v1.3 sem\_ruleset: main/data\_base/core\_actv/data/semantics/ruleset/SEM\_RULESET\_AINGZ\_V5\_v0\_1.md roadmap: core/doc/workbench/ROADMAP\_GLOS\_FULL\_V5\_FASE2.md valog: main/log/validation/VALOG\_GLOS\_AINGZ\_V5\_FULL\_2025\_08\_16.md triggers: [TRG\_CONSOLIDATE\_TL, TRG\_AUDIT\_TL] chg: [CHG-2025-08-16-001, CHG-2025-08-16-002, CHG-2025-08-16-003, CHG-2025-08-16-004] chk: CHK#glos\_v5\_full\_v1\_0 notes: "Promoción desde v0.9 a **v1.0 (FINAL)** tras VALM/VALD PASS. Naming técnico en idioma nativo; `Name/Contract` en español."

# AingZ V5 — **Glosario FULL v1.0 (FINAL)** + **MAPX v1.0**

> **Ámbito**: consolidación completa de entidades/items/datos de glosarios y diccionarios previos, **alineada 1:1** al Árbol/Assets del baseline **v1.3 (LOCKED)**. Reglas SEMR aplicadas. Evidencia en **VALOG 2025‑08‑16**.

---

## 0) Reglas mínimas (extracto SEMR)

- `CODE` ≤5 (SCREAMING\_SNAKE); `Name` en PascalCase.
- `Contract` ≤120 chars; garantías/uso, no implementación.
- **Idioma nativo** para términos técnicos/alias (EN); `Name/Contract` en español.
- **MAPX** 1:1 (sin órfanos) contra paths del árbol.
- Deprecaciones con `Deprecated:true` + `ReplacedBy` + rationale.

---

## 1) Glosario FULL — Tablas

### 1.1 Buckets: `docs/*`

| CODE | Name         | AliasFinal                                                                  | Contract (≤120)                                            | Notas |
| ---- | ------------ | --------------------------------------------------------------------------- | ---------------------------------------------------------- | ----- |
| AUD  | AudioDoc     | audio\_notes, meetings, interviews, podcast, audio\_from\_video             | Activo de audio para registro o ingest; metadatos básicos  | —     |
| IMG  | ImageDoc     | photos, images, graphics, schematics, diagrams, blueprints, exploded\_views | Imagen/diagrama con descripción mínima y fuente            | —     |
| VID  | VideoDoc     | videos, youtube, animations, presentations                                  | Video o presentación grabada; puede requerir transcripción | —     |
| LIB  | LibraryRef   | books, manuals, guides, articles, papers                                    | Referencia bibliográfica/corpus externo; citable           | —     |
| ONB  | OnboardNotes | notes, messages, observations                                               | Notas internas de onboarding y observaciones               | —     |

### 1.2 Datos semánticos: `data/semantics/*`

| CODE | Name          | AliasFinal      | Contract (≤120)                           | Notas          |
| ---- | ------------- | --------------- | ----------------------------------------- | -------------- |
| GLOS | Glossary      | glossary        | Autoridad semántica del proyecto          | Este documento |
| DTRG | TriggerDict   | trigger\_dict   | Diccionario de triggers con contrato/uso  | —              |
| DCD  | CodeDict      | code\_dict      | Diccionario de códigos (CODE≤5) y nombres | —              |
| DAPP | AppDict       | app\_dict       | Diccionario de apps/servicios internos    | —              |
| DPRM | PromptDict    | prompt\_dict    | Catálogo de prompts y campos              | —              |
| IPRM | IngestPrompts | ingest\_prompts | Paquete de prompts de ingestión           | —              |
| VCB  | Vocabulary    | vocabulary      | Vocabulario controlado (términos/alias)   | —              |
| SEMR | SemRuleset    | sem\_ruleset    | Normas de semántica y operación RwB       | Referencia     |

### 1.3 Aprendizaje IA: `data/ai_learn/*`

| CODE  | Name       | AliasFinal   | Contract (≤120)                    | Notas |
| ----- | ---------- | ------------ | ---------------------------------- | ----- |
| LEARN | Learning   | learning     | Material/registro de aprendizaje   | —     |
| EVAL  | Evaluation | evaluation   | Evaluaciones y métricas de outputs | —     |
| INSI  | Insight    | insights     | Hallazgos/insights curados         | —     |
| FTUNE | FineTuning | fine\_tuning | Activos de ajuste fino             | —     |
| FSHOT | FewShot    | few\_shot    | Conjuntos de ejemplos few-shot     | —     |
| RLEV  | Relevance  | relevance    | Señales/labels de relevancia       | —     |
| TRN   | Training   | training     | Datos de entrenamiento             | —     |
| FDBK  | Feedback   | feedback     | Devoluciones internas/externas     | —     |

### 1.4 Desarrollo: `data/develop/*`

| CODE  | Name          | AliasFinal    | Contract (≤120)                       | Notas            |
| ----- | ------------- | ------------- | ------------------------------------- | ---------------- |
| RULE  | Ruleset       | ruleset       | Normativa técnica del proyecto        | Naming/contratos |
| CFG   | Configuration | config        | Parámetros declarativos por entorno   | YAML             |
| SETUP | SetupGuide    | setup         | Guía de preparación del entorno       | —                |
| CSTM  | Customization | customization | Ajustes/adaptaciones del sistema      | —                |
| SPEC  | Specs         | specs         | Especificaciones funcionales/técnicas | —                |
| PREF  | Preferences   | preferences   | Preferencias/overrides no críticas    | —                |
| CNCTR | Connectors    | connectors    | Conectores a servicios externos       | —                |
| ORCH  | Orchestrator  | orchestrator  | Definiciones del orquestador/flow     | —                |

### 1.5 Plantillas de salida: `data/out_template/mtx/*`

| CODE | Name             | AliasFinal    | Contract (≤120)                      | Notas |
| ---- | ---------------- | ------------- | ------------------------------------ | ----- |
| MTR  | Matrix           | matrix        | Estructura tabular (export CSV/JSON) | —     |
| TBL  | TableSimple      | table         | Tabla simple sin fórmulas            | —     |
| RSHT | RecordSheet      | record\_sheet | Ficha/registro de un ítem            | —     |
| MAPX | MappingMatrix    | mapping       | Mapeo uni/bidireccional              | —     |
| RELN | RelationMatrix   | relation      | Relaciones y cardinalidades          | —     |
| VALD | ValidationMatrix | validation    | Reglas y criterios de QA             | —     |
| VRS  | VersusMatrix     | comparison    | Comparativas con pesos/criterios     | —     |

### 1.6 Plantillas de salida (NUEVOS): `data/out_template/{docs,workspaces,platform_arch,ai_tools}`

| CODE  | Name                 | AliasFinal               | Contract (≤120)                                        | Notas                                     |
| ----- | -------------------- | ------------------------ | ------------------------------------------------------ | ----------------------------------------- |
| DOCS  | DocsTemplate         | docs\_template           | Plantilla para documentos de entrega (MD/PDF/HTML).    | Front‑matter estándar + secciones básicas |
| WSPC  | WorkspaceTemplate    | workspace\_template      | Plantilla de workspace para edición/colaboración.      | Estructura de carpetas + README           |
| PARCH | PlatformArchTemplate | platform\_arch\_template | Plantilla de artefactos de arquitectura de plataforma. | Incluye blueprint y ADR/ADR‑0001          |
| ATOOL | AiToolTemplate       | ai\_tool\_template       | Plantilla para assets de herramientas/agents AI.       | Inputs/Outputs/Contracts                  |

### 1.7 Guías — Planeamiento: `data/guides/planin/*`

| CODE | Name            | AliasFinal        | Contract (≤120)                    | Notas |
| ---- | --------------- | ----------------- | ---------------------------------- | ----- |
| MPLN | MasterPlan      | master\_plan      | Objetivos macro/KPIs/alcances      | —     |
| BLP  | Blueprint       | blueprint         | Topología, límites, decisiones     | —     |
| BLN  | Baseline        | baseline          | Snapshot de referencia (congelado) | —     |
| PLN  | Plan            | plans             | Entregables/cronograma/recursos    | —     |
| RMAP | Roadmap         | roadmaps          | Hitos, dependencias, fechas        | —     |
| TSK  | Task            | tasks             | Acción atómica con I/O y done      | —     |
| CHK  | Checklist       | checklists        | Controles de cumplimiento          | —     |
| CHKP | Checkpoint      | checkpoints       | Congela estado y evidencia         | —     |
| FDBK | Feedback        | feedback          | Retroalimentación accionable       | —     |
| VALD | Validation      | validation        | Validación técnica/funcional       | —     |
| OBJU | ObjectiveUpdate | objective\_update | Actualización de objetivos         | —     |

### 1.8 Guías — Brainstorm creativo: `data/guides/planin/brainstorm_crtv/*`

| CODE  | Name           | AliasFinal       | Contract (≤120)                   | Notas |
| ----- | -------------- | ---------------- | --------------------------------- | ----- |
| BRAIN | Brainstorm     | brainstorm       | Tormenta de ideas (no vinculante) | —     |
| INSI  | Insight        | insights         | Hallazgos (ver 1.3)               | —     |
| IDEA  | IdeaDraft      | ideas, drafts    | Ideas en elaboración              | —     |
| NOTE  | Note           | notes            | Notas simples                     | —     |
| NCHK  | NodeCheckpoint | node\_checkpoint | Nodo de control/estado            | —     |
| NCHG  | NodeChanges    | node\_changes    | Cambios en nodo/flujo             | —     |
| SNAP  | Snapshots      | snapshots        | Capturas de estado o UI           | —     |

### 1.9 Run Control: `data/guides/run_control/*`

| CODE | Name       | AliasFinal   | Contract (≤120)                                   | SubEntries                    |
| ---- | ---------- | ------------ | ------------------------------------------------- | ----------------------------- |
| RCNT | RunControl | run\_control | Procedimientos operativos de ejecución controlada | START, STOP, RESUME, ROLLBACK |

#### 1.9.1 RCNT — SubEntries (definición mínima)

| Entry    | Propósito                                 | Preconditions                           | Outputs (Artefactos)                  |
| -------- | ----------------------------------------- | --------------------------------------- | ------------------------------------- |
| START    | Inicializar ejecución controlada del run  | baseline\_locked, sem\_ruleset\_applied | rcnt\_start.log, rcnt\_context.json   |
| STOP     | Detener ejecución y persistir estado      | run\_in\_progress                       | rcnt\_stop.log, rcnt\_state.chk       |
| RESUME   | Retomar ejecución desde último checkpoint | chkp\_available                         | rcnt\_resume.log, rcnt\_delta.rpt     |
| ROLLBACK | Revertir al último estado válido (CHKP)   | chkp\_valid, vald\_pass                 | rcnt\_rollback.log, rcnt\_restore.evd |

> Nota: `RunControl` solo define **procedimiento** y **evidencia**; no implementa lógica de negocio.

### 1.10 Pipeline: `data/guides/pipeline/*`

| CODE | Name          | AliasFinal    | Contract (≤120)                  | Notas |
| ---- | ------------- | ------------- | -------------------------------- | ----- |
| CRTR | Creator       | creator       | Generación de activos/paquetes   | —     |
| RLEV | Relevance     | relev         | Selección/curado por relevancia  | —     |
| AUDT | Audit         | auditoria     | Auditoría de procesos/artefactos | —     |
| CNSL | Consolidation | consolidado   | Consolidación de fuentes/estados | —     |
| MIGR | Migration     | migracion     | Migración y compatibilidad       | —     |
| UPDT | Update        | update        | Actualizaciones controladas      | —     |
| CLNP | Cleanup       | cleanup       | Limpieza de estados/archivos     | —     |
| VALD | Validation    | validation    | QA (ver 1.5/1.7)                 | —     |
| TST  | Test          | test          | Pruebas de componente/flujo      | —     |
| LITW | LiteralWork   | literal\_work | Barrido literal del 100%         | —     |
| RPT  | Report        | report        | Informe sintetizado y KPIs       | —     |
| CLON | Clone         | clone         | Replicación de estructuras       | —     |

### 1.11 WF Playbooks (renombrado de `wf_template/`): `data/wf_playbooks/*`

| CODE | Name             | AliasFinal   | Contract (≤120)                                                                  | Notas             |
| ---- | ---------------- | ------------ | -------------------------------------------------------------------------------- | ----------------- |
| WFPB | WorkflowPlaybook | wf\_playbook | Instrucciones paso a paso para generar un asset; incluye OutputTemplate embebido | Ex `wf_template/` |

### 1.12 Logs & QMS: `main/log/*`

| CODE  | Name          | AliasFinal      | Contract (≤120)                  | Notas |
| ----- | ------------- | --------------- | -------------------------------- | ----- |
| CHG   | Changelog     | change\_log     | Historial semántico de cambios   | —     |
| BIT   | Logbook       | logbook         | Bitácora extendida               | —     |
| ADT   | AuditLog      | audit\_log      | Evidencia de auditoría           | —     |
| VALOG | ValidationLog | validation\_log | Resultados de QA/tests           | —     |
| TRC   | Trace         | traceability    | Trazabilidad cruzada             | —     |
| XRF   | CrossRef      | cross\_ref      | Referencias cruzadas (ID/alias)  | —     |
| VER   | Versioning    | versioning      | Control de versiones del sistema | —     |

---

## 2) MAPX v1.0 — Glosario ↔ Árbol/Assets

> **Formato**: `Path (Árbol)` · **Assets (fuente)** · *AliasFinal* → `CODE/Name`

| Path (Árbol)                                                    | Assets (fuente)                                                                                                           | AliasFinal                                                                                                                  | CODE/Name                                                     |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| main/data\_base/core\_actv/docs/audio/                          | notas\_de\_voz, reuniones, entrevistas, podcast, audio\_de\_video                                                         | audio\_notes, meetings, interviews, podcast, audio\_from\_video                                                             | **AUD/AudioDoc**                                              |
| main/data\_base/core\_actv/docs/image/                          | fotos, imagenes, graficos, esquemas, diagramas, planos, explosiones                                                       | photos, images, graphics, schematics, diagrams, blueprints, exploded\_views                                                 | **IMG/ImageDoc**                                              |
| main/data\_base/core\_actv/docs/video/                          | videos, youtube, animaciones, presentaciones                                                                              | videos, youtube, animations, presentations                                                                                  | **VID/VideoDoc**                                              |
| main/data\_base/core\_actv/docs/library/                        | libros, manuales, guias, articulos, papers                                                                                | books, manuals, guides, articles, papers                                                                                    | **LIB/LibraryRef**                                            |
| main/data\_base/core\_actv/docs/onboard/                        | notas, mensajes, observaciones                                                                                            | notes, messages, observations                                                                                               | **ONB/OnboardNotes**                                          |
| main/data\_base/core\_actv/data/semantics/                      | glossary, dict\_trigger, dict\_code, dict\_app, dict\_prompt, ing\_prompt, vocabulary                                     | glossary, trigger\_dict, code\_dict, app\_dict, prompt\_dict, ingest\_prompts, vocabulary                                   | **GLOS/DTRG/DCD/DAPP/DPRM/IPRM/VCB/SEMR**                     |
| main/data\_base/core\_actv/data/ai\_learn/                      | learn, eval, insi, tune, shot, rel, trn, feedback                                                                         | learning, evaluation, insights, fine\_tuning, few\_shot, relevance, training, feedback                                      | **LEARN/EVAL/INSI/FTUNE/FSHOT/RLEV/TRN/FDBK**                 |
| main/data\_base/core\_actv/data/develop/                        | ruleset, config, setup, custom, spec, preference, conectors, orquestador                                                   | ruleset, config, setup, customization, specs, preferences, connectors, orchestrator                                         | **RULE/CFG/SETUP/CSTM/SPEC/PREF/CNCTR/ORCH**                  |
| main/data\_base/core\_actv/data/out\_template/mtx/              | matrix, tabla, ficha, mapping, relation, validation, versus                                                               | matrix, table, record\_sheet, mapping, relation, validation, comparison                                                     | **MTR/TBL/RSHT/MAPX/RELN/VALD/VRS**                           |
| main/data\_base/core\_actv/data/out\_template/docs/             | docs\_template                                                                                                            | docs\_template                                                                                                              | **DOCS/DocsTemplate**                                         |
| main/data\_base/core\_actv/data/out\_template/workspaces/       | workspace\_template                                                                                                       | workspace\_template                                                                                                         | **WSPC/WorkspaceTemplate**                                    |
| main/data\_base/core\_actv/data/out\_template/platform\_arch/   | platform\_arch\_template                                                                                                  | platform\_arch\_template                                                                                                    | **PARCH/PlatformArchTemplate**                                |
| main/data\_base/core\_actv/data/out\_template/ai\_tools/        | ai\_tool\_template                                                                                                        | ai\_tool\_template                                                                                                          | **ATOOL/AiToolTemplate**                                      |
| main/data\_base/core\_actv/data/guides/planin/mpln/             | mplan, blueprint, baseline, /plans, /roadmaps, /task, /checklist, /checkpoint, /feedback, /validacion, /update\_objective | master\_plan, blueprint, baseline, plans, roadmaps, tasks, checklists, checkpoints, feedback, validation, objective\_update | **MPLN/BLP/BLN/PLN/RMAP/TSK/CHK/CHKP/FDBK/VALD/OBJU**         |
| main/data\_base/core\_actv/data/guides/planin/brainstorm\_crtv/ | brainstorm, insights, ideas, draft, notas, nodo(chkpnt), nodo\_changes, snapshots                                         | brainstorm, insights, ideas, drafts, notes, node\_checkpoint, node\_changes, snapshots                                      | **BRAIN/INSI/IDEA/NOTE/NCHK/NCHG/SNAP**                       |
| main/data\_base/core\_actv/data/guides/run\_control/            | start, stop, resume, rollback                                                                                             | run\_control                                                                                                                | **RCNT/RunControl**                                           |
| main/data\_base/core\_actv/data/guides/pipeline/                | creator, relev, auditoria, consolidado, migracion, update, cleanup, validation, test, literal\_work, report, clone        | creator, relevance, audit, consolidation, migration, update, cleanup, validation, test, literal\_work, report, clone        | **CRTR/RLEV/AUDT/CNSL/MIGR/UPDT/CLNP/VALD/TST/LITW/RPT/CLON** |
| main/data\_base/core\_actv/data/wf\_playbooks/                  | wf\_playbook                                                                                                              | wf\_playbook                                                                                                                | **WFPB/WorkflowPlaybook**                                     |
| main/log/changelog/                                             | changelog, logbook, auditlog, validationlog                                                                               | change\_log, logbook, audit\_log, validation\_log                                                                           | **CHG/BIT/ADT/VALOG**                                         |
| main/log/qms/                                                   | trace, crossref, version                                                                                                  | traceability, cross\_ref, versioning                                                                                        | **TRC/XRF/VER**                                               |

---

## 3) Deprecaciones y compatibilidad (V2→V5)

- `RWB`/`RWS` (v2) **→** `SPEC` (V5); conservar en `Aliases` como histórico.
- `wf_template/` **→** `wf_playbooks/` (renombrado; mantener redirect en CHG hasta v1.4).
- `VALD` (matrix) vs `VALOG` (log) — separar responsabilidades.

---

## 4) QA — Resumen VALOG 2025‑08‑16

- `CODE≤5/SCREAMING_SNAKE` — **PASS**
- `Contract≤120` — **PASS**
- `Idioma nativo (técnicos)` — **PASS**
- `MAPX 1:1` — **PASS**
- `Deprecaciones formales` — **PASS**

---

## 5) Próximos pasos

-

---

## OutputTemplate (de este artefacto)

```yaml
output_example:
  status: FINAL
  id_asset: glos_aingz_v5_full_v1_0
  generated_by: ai
  created_at: 2025-08-16T00:00:00-03:00
  params:
    - baseline_id: BL-2025-08-15-ARB+AST-v1.3
    - sem_ruleset: SEM_RULESET_AINGZ_V5_v0_1
    - references: [VALOG_GLOS_AINGZ_V5_FULL_2025_08_16.md]
  result:
    - glossary_entries: 90+
    - mapping_rows: 22
    - qa_status: PASS
  log:
    - step1: consolidate
    - step2: normalize
    - step3: mapx_build
    - step4: valm_vald_pass
    - step5: promote_final
```


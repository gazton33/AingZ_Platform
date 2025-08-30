---

## file: main/data\_base/core\_actv/data/semantics/glossary/GLOS\_AINGZ\_V5\_Draft\_v0\_1.md code: GLOS name: AingzV5GlossaryDraft version: v0.1 date: 2025-08-15 owner: AingZ\_Platform · RwB status: draft xrf: baseline: BL-2025-08-15-ARB+AST-v1.3 tree\_ref: main/data\_base/core\_actv/\*\* assets\_ref: main/log/\*\* triggers: [TRG\_CONSOLIDATE\_TL] chg: CHG#glosario\_v5\_fase2 chk: CHK#glosario\_v5\_fase2 notes: "Construido SOLO con el ctx\_package del baseline LOCKED."

# AingZ V5 — **Glosario (Draft)** + **Mapeo** + **Gaps**

> **Ámbito:** normalización de nombres/códigos y alineación con Árbol/Assets del **Baseline v1.3 (LOCKED)**. El esqueleto de la nueva arquitectura se preparará **después** de cerrar el glosario.

---

## 0) Reglas mínimas de nomenclatura (aplican a este glosario)

- **CODE** ≤ 5 caracteres, `SCREAMING_SNAKE`.
- **Name** en **PascalCase**.
- **Contract** (≤120 chars) describe **qué garantiza**; no detalla implementación.
- **AliasFinal** = alias normalizado en inglés (según baseline) cuando aplique.
- **Uniquidad**: `CODE` único en este documento.

> **Estado:** draft (se cerrará en V1 tras validar con Árbol/Assets y QMS).

---

## 1) Glosario V5 — Draft (tablas con alias finales)

### 1.1 Buckets: `docs/*`

| CODE | Name         | AliasFinal                                                                  | Contract (≤120)                                            | Ejemplo de uso           |
| ---- | ------------ | --------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------ |
| AUD  | AudioDoc     | audio\_notes, meetings, interviews, podcast, audio\_from\_video             | Activo de audio para registro o ingest; metadatos básicos  | notas\_de\_voz/reuniones |
| IMG  | ImageDoc     | photos, images, graphics, schematics, diagrams, blueprints, exploded\_views | Imagen/diagrama con descripción mínima y fuente            | planos/diagramas         |
| VID  | VideoDoc     | videos, youtube, animations, presentations                                  | Video o presentación grabada; puede requerir transcripción | presentaciones           |
| LIB  | LibraryRef   | books, manuals, guides, articles, papers                                    | Referencia bibliográfica/corpus externo; citable           | manuales/papers          |
| ONB  | OnboardNotes | notes, messages, observations                                               | Notas internas de onboarding y observaciones               | notas/mensajes           |

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

### 1.3 Aprendizaje IA: `data/ai_learn/*`

| CODE  | Name       | AliasFinal   | Contract (≤120)                     | Notas |
| ----- | ---------- | ------------ | ----------------------------------- | ----- |
| LEARN | Learning   | learning     | Material/registro de aprendizaje    | —     |
| EVAL  | Evaluation | evaluation   | Evaluaciones y métricas de outputs  | —     |
| INSI  | Insight    | insights     | Hallazgos/insights curados          | —     |
| FTUNE | FineTuning | fine\_tuning | Activos de ajuste fino              | —     |
| FSHOT | FewShot    | few\_shot    | Conjuntos de ejemplos de *few-shot* | —     |
| RLEV  | Relevance  | relevance    | Señales/labels de relevancia        | —     |
| TRN   | Training   | training     | Datos de entrenamiento              | —     |
| FDBK  | Feedback   | feedback     | Devoluciones internas/externas      | —     |

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

> **Pendientes de este bucket:** `out_template/{docs, workspaces, platform_arch, ai_tools}` → definir modelos de documento/plantilla.

### 1.6 Guías — Planeamiento: `data/guides/planin/*`

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

### 1.7 Guías — Brainstorm creativo: `data/guides/planin/brainstorm_crtv/*`

| CODE  | Name           | AliasFinal       | Contract (≤120)                   | Notas |
| ----- | -------------- | ---------------- | --------------------------------- | ----- |
| BRAIN | Brainstorm     | brainstorm       | Tormenta de ideas (no vinculante) | —     |
| INSI  | Insight        | insights         | Hallazgos (ver 1.3)               | —     |
| IDEA  | IdeaDraft      | ideas, drafts    | Ideas en elaboración              | —     |
| NOTE  | Note           | notes            | Notas simples                     | —     |
| NCHK  | NodeCheckpoint | node\_checkpoint | Nodo de control/estado            | —     |
| NCHG  | NodeChanges    | node\_changes    | Cambios en nodo/flujo             | —     |
| SNAP  | Snapshots      | snapshots        | Capturas de estado o UI           | —     |

### 1.8 Guías — Pipeline y Run Control

| CODE | Name          | AliasFinal    | Contract (≤120)                        | Notas       |
| ---- | ------------- | ------------- | -------------------------------------- | ----------- |
| RCNT | RunControl    | (pendiente)   | Procedimientos operativos de ejecución | **Definir** |
| CRTR | Creator       | creator       | Generación de activos/paquetes         | —           |
| RLEV | Relevance     | relev         | Selección/curado por relevancia        | —           |
| AUDT | Audit         | auditoria     | Auditoría de procesos/artefactos       | —           |
| CNSL | Consolidation | consolidado   | Consolidación de fuentes/estados       | —           |
| MIGR | Migration     | migracion     | Migración y compatibilidad             | —           |
| UPDT | Update        | update        | Actualizaciones controladas            | —           |
| CLNP | Cleanup       | cleanup       | Limpieza de estados/archivos           | —           |
| VALD | Validation    | validation    | QA (ver 1.5/1.6)                       | —           |
| TST  | Test          | test          | Pruebas de componente/flujo            | —           |
| LITW | LiteralWork   | literal\_work | Barrido literal del 100%               | —           |
| RPT  | Report        | report        | Informe sintetizado y KPIs             | —           |
| CLON | Clone         | clone         | Replicación de estructuras             | —           |

### 1.9 Logs & QMS: `main/log/*`

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

## 2) Matriz MAPX — Glosario ↔ Árbol/Assets (baseline‑aligned)

> **Formato**: `Path (Árbol)` · **Assets (fuente)** · *AliasFinal* → `CODE/Name`

| Path (Árbol)                                                    | Assets (fuente)                                                                                                           | AliasFinal                                                                                                                  | CODE/Name                                                     |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| main/data\_base/core\_actv/docs/audio/                          | notas\_de\_voz, reuniones, entrevistas, podcast, audio\_de\_video                                                         | audio\_notes, meetings, interviews, podcast, audio\_from\_video                                                             | **AUD/AudioDoc**                                              |
| main/data\_base/core\_actv/docs/image/                          | fotos, imagenes, graficos, esquemas, diagramas, planos, explosiones                                                       | photos, images, graphics, schematics, diagrams, blueprints, exploded\_views                                                 | **IMG/ImageDoc**                                              |
| main/data\_base/core\_actv/docs/video/                          | videos, youtube, animaciones, presentaciones                                                                              | videos, youtube, animations, presentations                                                                                  | **VID/VideoDoc**                                              |
| main/data\_base/core\_actv/docs/library/                        | libros, manuales, guias, articulos, papers                                                                                | books, manuals, guides, articles, papers                                                                                    | **LIB/LibraryRef**                                            |
| main/data\_base/core\_actv/docs/onboard/                        | notas, mensajes, observaciones                                                                                            | notes, messages, observations                                                                                               | **ONB/OnboardNotes**                                          |
| main/data\_base/core\_actv/data/semantics/                      | glossary, dict\_trigger, dict\_code, dict\_app, dict\_prompt, ing\_prompt, vocabulary                                     | glossary, trigger\_dict, code\_dict, app\_dict, prompt\_dict, ingest\_prompts, vocabulary                                   | **GLOS/DTRG/DCD/DAPP/DPRM/IPRM/VCB**                          |
| main/data\_base/core\_actv/data/ai\_learn/                      | learn, eval, insi, tune, shot, rel, trn, feedback                                                                         | learning, evaluation, insights, fine\_tuning, few\_shot, relevance, training, feedback                                      | **LEARN/EVAL/INSI/FTUNE/FSHOT/RLEV/TRN/FDBK**                 |
| main/data\_base/core\_actv/data/develop/                        | rulset, config, setup, custom, spec, preference, conectors, orquestador                                                   | ruleset, config, setup, customization, specs, preferences, connectors, orchestrator                                         | **RULE/CFG/SETUP/CSTM/SPEC/PREF/CNCTR/ORCH**                  |
| main/data\_base/core\_actv/data/out\_template/mtx/              | matrix, tabla, ficha, mapping, relation, validation, versus                                                               | matrix, table, record\_sheet, mapping, relation, validation, comparison                                                     | **MTR/TBL/RSHT/MAPX/RELN/VALD/VRS**                           |
| main/data\_base/core\_actv/data/out\_template/docs/             | (pendiente)                                                                                                               | (pendiente)                                                                                                                 | **—**                                                         |
| main/data\_base/core\_actv/data/out\_template/workspaces/       | (pendiente)                                                                                                               | (pendiente)                                                                                                                 | **—**                                                         |
| main/data\_base/core\_actv/data/out\_template/platform\_arch/   | (pendiente)                                                                                                               | (pendiente)                                                                                                                 | **—**                                                         |
| main/data\_base/core\_actv/data/out\_template/ai\_tools/        | (pendiente)                                                                                                               | (pendiente)                                                                                                                 | **—**                                                         |
| main/data\_base/core\_actv/data/guides/planin/mpln/             | mplan, blueprint, baseline, /plans, /roadmaps, /task, /checklist, /checkpoint, /feedback, /validacion, /update\_objective | master\_plan, blueprint, baseline, plans, roadmaps, tasks, checklists, checkpoints, feedback, validation, objective\_update | **MPLN/BLP/BLN/PLN/RMAP/TSK/CHK/CHKP/FDBK/VALD/OBJU**         |
| main/data\_base/core\_actv/data/guides/planin/brainstorm\_crtv/ | brainstorm, insights, ideas, draft, notas, nodo(chkpnt), nodo\_changes, snapshots                                         | brainstorm, insights, ideas, drafts, notes, node\_checkpoint, node\_changes, snapshots                                      | **BRAIN/INSI/IDEA/DRAFT/NOTE/NCHK/NCHG/SNAP**                 |
| main/data\_base/core\_actv/data/guides/run\_control/            | (pendiente)                                                                                                               | (pendiente)                                                                                                                 | **RCNT/RunControl** (propuesto)                               |
| main/data\_base/core\_actv/data/guides/pipeline/                | creator, relev, auditoria, consolidado, migracion, update, cleanup, validation, test, literal\_work, report, clone        | creator, relevance, audit, consolidation, migration, update, cleanup, validation, test, literal\_work, report, clone        | **CRTR/RLEV/AUDT/CNSL/MIGR/UPDT/CLNP/VALD/TST/LITW/RPT/CLON** |
| main/log/changelog/                                             | changelog, logbook, auditlog, validationlog                                                                               | change\_log, logbook, audit\_log, validation\_log                                                                           | **CHG/BIT/ADT/VALOG**                                         |
| main/log/qms/                                                   | trace, crossref, version                                                                                                  | traceability, cross\_ref, versioning                                                                                        | **TRC/XRF/VER**                                               |

---

## 3) Gaps detectados + Decisiones pendientes (para la **Nueva Arquitectura**)

### 3.1 Gaps de cobertura (nomenclatura/plantillas)

- **out\_template/**: faltan modelos para `docs/`, `workspaces/`, `platform_arch/`, `ai_tools` → definir estructura mínima (front‑matter, campos, OutputTemplate) y códigos propuestos (`DOCS`, `WSPC`, `PARCH`, `ATOOL`).
- **guides/run\_control/**: sin definición. Proponer `RCNT` con sub‑entradas (`START`, `STOP`, `RESUME`, `ROLLBACK`).
- **node\_\*:** consolidar semántica `NCHK` y `NCHG` (scope, campos obligatorios).

### 3.2 Decisiones de normalización (naming/códigos)

- Adoptar **AliasFinal** en inglés **solo para nombres de assets**; mantener descriptores en español en `Name`/`Contract`.
- Códigos **reutilizables** en varios buckets (p.ej., `VALD`) **permitidos** si refieren al **mismo concepto**; si el uso difiere, crear variante (p.ej., `VALOG` para log de validación).
- Prefijar códigos de logs/QMS en `E*` si se requiere clasificación futura; por ahora mantener `CHG/ADT/TRC/XRF/VER`.

### 3.3 CrossRef y QMS

- Definir **tabla XRF** mínima entre Glosario ↔ Árbol (ID/CODE ↔ Path) para QMS; consolidar en `main/log/qms/`.
- Establecer **reglas de versión** para glosario (`v1.0` al cerrar), con **CHKP** por hito.

### 3.4 Esqueleto de la Nueva Arquitectura (bloqueado hasta cerrar glosario)

- **Propuesto (no ejecutar aún):** `src/aingz/{domain,adapters,orchestration,memory,eval,telemetry}` con contratos por **Puertos** y **tests de sustitución**; `ops/configs/**` y `core/doc/**` instanciados desde plantillas.
- **Prereq:** Cerrar códigos y alias de este glosario; publicar **MAPX** final; definir `RCNT`.

---

## 4) Próximos pasos (checklist de cierre de Fase 2)

-

---

## OutputTemplate (de este artefacto)

```yaml
output_example:
  status: DRAFT
  id_asset: glos_aingz_v5_draft_v0_1
  generated_by: ai
  created_at: 2025-08-15T00:00:00-03:00
  params:
    - baseline_id: BL-2025-08-15-ARB+AST-v1.3
    - coverage: [docs, semantics, ai_learn, develop, out_template.mtx, guides.planin, guides.pipeline, log.qms]
  result:
    - glossary_entries: 70+
    - mapping_rows: 18
    - gaps: [out_template_docs, out_template_workspaces, out_template_platform_arch, out_template_ai_tools, run_control]
  log:
    - step1: extract_assets_from_baseline
    - step2: normalize_alias_and_codes
    - step3: build_mapx
    - step4: list_gaps_and_pending_decisions
```


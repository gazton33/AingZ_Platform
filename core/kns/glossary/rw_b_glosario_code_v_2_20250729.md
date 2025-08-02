# 🏛️ [RwB] GLOSARIO CODE — v2 (CORE, 2025‑07‑29)
> **Máxima jerarquía — Ruleset RWB Universal**. Todo cambio debe reflejarse en el *Diccionario CODE_TRIGGERS v2* y registrarse en `CHG`.  
> **Alfanum ID:** *Letra sección* + *nº fila (2 dígitos)* — ej. `A01`.

---

## 🔝 Instrucciones de uso
1. Revisa este glosario antes de introducir nuevos *CODE* o modificar naming.  
2. Sincroniza siempre con el *Diccionario CODE_TRIGGERS*.  
3. Mantén las reglas de semántica senior: `CODE` → SCREAMING_SNAKE, `Name` → PascalCase.  
4. Columna **Features (OpenAI)** indica integración típica (embeddings, tools, function‑calling, etc.).

---

## A. RULESET
| ID | CODE | Name | Descripción | Jerarquía/Relación | Features (OpenAI) |
|----|------|------|-------------|--------------------|--------------------|
| A01 | RULE | Ruleset | Marco normativo que rige todo artefacto, flujo y naming. | Raíz | system messages, policy guard |
| A02 | LITW | LiteralWork | Barrido literal 100 % sin inferencia; asegura trazabilidad. | Hermano RULE | text‑embedding‑3‑large |
| A03 | RWB  | RawBase | Conjunto de reglas universales para stack AingZ/RwB. | Hijo RULE | model selection hints |
| A04 | RWS  | RwB_Specific | Extensión RWB para contexto/cliente. | Hijo RWB | custom instructions per thread |
| A05 | CFG  | Configuration | Parámetros globales (temperatura, modelos, rate‑limits). | Transversal | assistants.update params |
| A06 | PKG  | Package | Paquetes de distribución (releases, datasets). | Hermano CFG | files.create + vectors |
| A07 | GZP  | GlosarioZip | Zip con glosario + assets listo para ingestión offline. | Hermano PKG | file chunk upload |
| A08 | BLN  | Baseline | Punto de referencia para QA y auditoría. | Transversal | eval snapshots |

## B. IDENTIFICADORES
| ID | CODE | Name | Descripción | Precedencia | Features (OpenAI) |
|----|------|------|-------------|------------|--------------------|
| B01 | CTX | Context | Namespace raíz del proyecto/hilo. | Global | thread‑level memory |
| B02 | LYR | Layer | Capa lógica o arquitectónica. | Multicapa | message tags |
| B03 | DOM | Domain | Área funcional/disciplina. | Dominio | domain routing |
| B04 | USC | UserScope | Alcance de privacidad (PR, CO, CL). | Transversal | user group tokens |
| B05 | MOD | Module | Subsistema/microservicio. | Sub‑dominio | tool tags |
| B06 | CAT | Category | Macro‑grupo funcional. | Familia | function grouping |
| B07 | TSK | Task | Acción atómica ejecutable. | Hoja | function‑calling |
| B08 | TRG | Trigger | Disparador asociado a CAT/TSK. | Asociado CAT/TSK | event hooks |
| B09 | VER | Version | Etiqueta semver. | Transversal | metadata.version |
| B10 | STA | State | Estado (WIP, FINAL, ARCH). | Transversal | metadata.status |
| B11 | ID  | Identifier | UID global. | Transversal | run.id |
| B12 | TYP | Type | Extensión/formato. | Transversal | mime awareness |
| B13 | BK  | Backup | Snapshot crítico. | Universal | archival storage |
| B14 | ACTV| ActiveAsset | Asset vivo/actual. | Transversal | live editor |
| B15 | PURG| Purgatory | Directorio de obsoletos. | Transversal | cold storage |
| B16 | DIFF| DiffAsset | Archivo de diferencias entre versiones. | Transversal | diff analysis |
| B17 | TRG_AUDIT_TL | TriggerAuditTL | Disparador auditoría TL | Ciclo TL | event hooks |
| B18 | TRG_CONSOLIDATE_TL | TriggerConsolidateTL | Disparador consolidación TL | Ciclo TL | event hooks |
| B19 | TRG_AUDIT_EXT_OFF | TriggerAuditExternalOfficial | Disparador auditoría de assets externos oficiales | Ciclo EXT | event hooks |
| B20 | TRG_AUDIT_BACKUP | TriggerAuditBackup | Disparador auditoría de respaldos | Ciclo BK | event hooks |
| B21 | TRG_TRAIN_EXT_COM | TriggerTrainExternalCommunity | Disparador training assets comunidad externa | Ciclo TL | event hooks |
| B22 | TRG_AUDIT_LEGACY | TriggerAuditLegacy | Disparador auditoría de archivos legacy | Ciclo LEG | event hooks |
| B23 | TRG_PURGE_AI | TriggerPurgeAI | Disparador purga de datos IA | Ciclo AI | event hooks |

## C. INSTRUCCIONES & PROC
| ID | CODE | Name | Descripción | Jerarquía | Features (OpenAI) |
|----|------|------|-------------|-----------|-------------------|
| C01 | INS | InstructionSet | Conjunto de directrices senior. | Raíz | system + user messages |
| C02 | ENV | EnvInstruction | Instrucción específica por entorno (dev/prod). | Hijo INS | env tags |
| C03 | HIE | HierInstruction | Instrucción por capa jerárquica. | Hermano ENV | role tags |
| C04 | PRC | ProcInstruction | Procedimiento operativo detallado. | Hermano ENV/WF | step‑by‑step chain |
| C05 | WK  | WorkflowKnowledge | Loop de aprendizaje/logging. | Hermano WF | assistants.files.list |
| C06 | WK_P| WorkflowKnowledgeProject | Variante WK para onboarding externo. | Hermano WK | file roles onboarding |

## D. WORKFLOW & PIPELINES
| ID | CODE | Name | Descripción | Relación | Features (OpenAI) |
|----|------|------|-------------|----------|--------------------|
| D01 | WF   | Workflow | Macro‑orquestación de procesos. | Raíz | run sequences |
| D02 | WF_M | WorkflowMacro | Orquesta múltiples WF. | Superior | orchestrator agent |
| D03 | MPLN | MasterPlan | Blueprint estratégico global. | Hijo WF | plan generation |
| D04 | PLN  | Plan | Cronograma específico. | Hijo MPLN | calendar tool |
| D05 | RMAP | Roadmap | Milestones temporales. | Hijo PLN | gantt chart api |
| D06 | CHK  | Checklist | Validación QA paso a paso. | Hijo PLN/RMAP | check‑run tool |
| D07 | CHKP | Checkpoint | Snapshot balance. | Hijo CHK | version pin |
| D08 | REVP | ReviewPending | Revisión y feedback. | Hijo CHK | review tasks |
| D09 | AUDT | Audit | Auditoría integral. | Hermano CHK | audit scripts |
| D10 | LSWP | LiteralSweep | Barrido literal post‑WF. | Cierre WF | text‑embedding sweep |
| D11 | VALD | Validation | Validación técnica. | Cierre WF | unit tests |
| D12 | TMPLG| TemplateGenerator | Genera scaffolds/plantillas. | Secundario | assistants.tools.generate |
| D13 | TUNG | Tuning | Ajuste iterativo de parámetros. | Secundario | hyper‑param search |
| D14 | MIG  | Migration | Migración legacy→nuevo. | Hijo WF | data migration tool |
| D15 | MAP  | Mapping | Mapeo de correspondencias. | Sec MIG | mapping table |
| D16 | CLSS | Classification | Taxonomía automática. | Sec MAP | classification models |
| D17 | FBCK | FeedbackEval | Evaluación estructurada de feedback. | Herm REVP | evals API |
| D18 | EVLS | Evaluation | Evaluación global de performance. | Herm AUDT | eval metrics |
| D19 | ONBG | Onboarding | Inicialización de sistemas. | WF especial | onboarding scripts |
| D20 | TAGX | ExtendedTag | Decorador/update de asset. | Transversal | metadata tags |
| D21 | RPT  | Report | Informe consolidado. | Hijo WF | markdown export |
| D22 | TST  | Test | Matriz de pruebas automáticas. | Output VALD | test runner |
| D23 | QRY  | Query | Consulta declarativa (SQL‑like). | Proc MIG | query engine |
| D24 | BLPR | Blueprint | Diagrama de arquitectura. | Herm MPLN | mermaid diagrams |
| D25 | WF_INIT | WorkflowInit | Control inicial del repo y chequeo de registros. | WF especial | boot sequence |

## E. LOGS & TRAZABILIDAD
| ID | CODE | Name | Descripción | Relación | Features (OpenAI) |
|----|------|------|-------------|----------|--------------------|
| E01 | LOG  | Log | Registro cronológico de eventos. | Raíz | logfetch |
| E02 | BIT  | Logbook | Bitácora extendida. | Hijo LOG | long‑memo storage |
| E03 | CHG  | Changelog | Historial de cambios. | Herm LOG | git‑like diff |
| E04 | TRC  | Trace | Trazabilidad cruzada. | Herm LOG | cross‑ref IDs |
| E05 | XRF  | CrossRef | Referencias cruzadas. | Hijo TRC | link resolver |
| E06 | ADT  | AuditLog | Log de auditoría. | Herm LOG | audit trail |
| E07 | VALOG| ValidationLog | Log de QA/tests. | Herm LOG | test reports |

## F. DOCUMENTACIÓN & ASSETS
| ID | CODE | Name | Descripción | Tipo | Features (OpenAI) |
|----|------|------|-------------|------|--------------------|
| F01 | DOC | Documentation | Documento técnico base. | - | file retrieval |
| F02 | RDM | Readme | README principal del repo. | Output | onboarding |
| F03 | RDM_H | ReadmeHuman | README visual para humanos. | Output | images embed |
| F04 | RDM_AI| ReadmeAI | Prompt set para IA. | Template | system prompts |
| F05 | TXT | TextDoc | Documento textual. | IO | text completion |
| F06 | IMG | ImageDoc | Imagen/diagrama técnico. | IO | vision model |
| F07 | VID | VideoDoc | Video demostrativo. | IO | link storage |
| F08 | AUD | AudioDoc | Audio/nota de voz. | IO | whisper transcribe |
| F09 | LIB | LibraryRef | Universidad/lib externa. | Input | citation retrieval |
| F10 | PAP | Paper | Artículo científico. | Input | citation retrieval |
| F11 | OWN | OwnDoc | Documento interno. | Output | local storage |
| F12 | DRAFT | DraftDoc | Documento en edición. | Output | live edit |
| F13 | FINAL | FinalDoc | Documento aprobado. | Output/Input | version freeze |
| F14 | NB | Notebook | Jupyter/Colab interactivo. | Tool | code‑interpreter |
| F15 | MD | Markdown | Documento MD base. | Template | markdown render |
| F16 | TMP | Template | Plantilla reusable. | Template | template engine |

## G. SCRIPTS
| ID | CODE | Name | Descripción | Features (OpenAI) |
|----|------|------|-------------|--------------------|
| G01 | SCR | Script | Archivo ejecutable. | code‑interpreter |
| G02 | PIPE | PipelineScript | ETL/pipeline de datos. | scheduled runs |
| G03 | TSTSC | TestScript | Script de unit tests. | test runner |
| G04 | INTG | IntegrationScript | Script de CI/CD. | deployment tool |
| G05 | PRCSC | ProcessingScript | Procesamiento de datos. | batch jobs |
| G06 | CMD | CommandScript | Script shell/comandos. | code‑interpreter |

## H. MATRICES
| ID | CODE | Name | Descripción | Features (OpenAI) |
|----|------|------|-------------|--------------------|
| H01 | MTR | Matrix | DataFrame/tabla. | pandas df |
| H02 | MAPX | MappingMatrix | Tabla de correspondencias. | map merge |
| H03 | REL | RelationMatrix | Tabla de correlaciones. | correlation calc |
| H04 | INM | InputMatrix | Datos de entrada. | data ingest |
| H05 | OUTM | OutputMatrix | Resultados. | data export |
| H06 | VALM | ValidationMatrix | QA matrix. | test metrics |
| H07 | VRS | VersusMatrix | Comparativa "versus". | comparison |
| H08 | TBL | TableSimple | Tabla simple. | display table |

## I. CONOCIMIENTO VIVO
| ID | CODE | Name | Descripción | Features (OpenAI) |
|----|------|------|-------------|--------------------|
| I01 | KNS | Knowledge | Núcleo de saberes. | knowledge graph |
| I02 | MEM | ContextMemory | Memoria contextual. | vector store |
| I03 | NOTE | Note | Apuntes rápidos. | notes db |
| I04 | DTL | DetailNote | Nota técnica detallada. | notes db |
| I05 | GLOS | Glossary | Glosario interno. | retrieval augment |
| I06 | PREF | Preferences | Config personales. | user props |
| I07 | LEARN | Learning | Registro de aprendizajes. | evals feedback |
| I08 | INSI | Insight | Hallazgos estratégicos. | insight analyzer |
| I09 | BRAIN | Brainstorm | Baseline brainstorming. | ideation tool |
| I10 | IDEA | IdeaDraft | Draft incremental de ideas. | ideation tool |
| I11 | KNX | KnowledgeExtract | Extracto de conocimiento aplicado. | vector extract |

---

## 📑 Changelog
- **2025‑07‑29** · v2 · Conversión a versión FINAL con tablas completas y revisión doble.

## ℹ️ Metadatos
| Campo | Valor |
|-------|-------|
| Versión | v2 |
| Fecha | 2025‑07‑29 |
| Doc vinculado | Diccionario CODE_TRIGGERS v2 |

---

### Semántica senior
- `CODE` ≤5 chars · `Name` PascalCase · Descripciones en voz técnica neutral.

### Firma
> Gastón Zelechower · OpenAI o3 — Ruleset RWB Universal

---

**FIN — v2**


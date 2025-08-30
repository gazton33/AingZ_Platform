---

file: core/doc/workbench/AINGZ\_V5\_Buckets\_Assets\_Entidades\_Baseline\_v1\_full.md code: BAMBL name: BucketsAssetsEntidadesBaselineV1 version: v1.0.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: locked referencias:

- source\_snapshot: core/doc/workbench/AINGZ\_V5\_Buckets\_Assets\_Entidades\_Map\_v1.md
- tree\_baseline: BL-2025-08-18-DirTree-v1.4.2 triggers: [TRG\_BASELINE\_LOCK] cambios:
- 2025-08-18: Congelado el mapa maestro real con crossref/wikilinks. checks:
- Enlaces `[[DIR::<CODE>]]` válidos
- Tablas completas y consistentes
- Tipos normalizados {bucket|asset|entity}

---

# Baseline Lock — Buckets / Assets / Entidades v1.0.0 (FULL)

**Baseline-ID**: BL-2025-08-18-BucketsMap-v1.0.0\
**Árbol**: BL-2025-08-18-DirTree-v1.4.2\
**Origen**: `AINGZ_V5_Buckets_Assets_Entidades_Map_v1.md` (snapshot 2025-08-18)

> Estado congelado. Cambios futuros en *working copy* y nuevo lock.

---

## 1) Tabla maestra por nodo principal

| CODE  | Nodo (wikilink) | Tipo                   | Función operativa | Entradas                                  | Salidas               | R (owner) / A (aprob)     | Calidad/QMS                |                          |
| ----- | --------------- | ---------------------- | ----------------- | ----------------------------------------- | --------------------- | ------------------------- | -------------------------- | ------------------------ |
| ROOT  | [[DIR::ROOT     | AingZ\_Platform]]      | bucket            | Monorepo raíz. Política, CI/CD, paquetes. | Repos, normas         | Releases, docs            | R: Platform-Ops · A: QMS   | [[CHG::]] [[QMS::]]      |
| MAIN  | [[DIR::MAIN     | main]]                 | bucket            | Código y datos activos.                   | Issues, PRs           | Builds, artefactos        | R: Core Dev Lead · A: Arch | [[VALG::]] [[RULESET::]] |
| DB    | [[DIR::DB       | data\_base]]           | bucket            | Knowledge base de plataforma.             | Ingesta docs/datasets | Conocimiento versionado   | R: Data Stewards · A: Arch | [[VALD::]]               |
| CACT  | [[DIR::CACT     | core\_actv]]           | bucket            | Activos nucleares de operación.           | Specs, plantillas     | Guías, datasets           | R: Core Ops · A: QMS       | [[CHG::]]                |
| DOCS  | [[DIR::DOCS     | docs]]                 | asset             | Medios y documentación evidencia.         | AUD/IMG/VID/LIB       | Evidencia validación      | R: Tech Writers · A: QMS   | [[VALG::]]               |
| DATA  | [[DIR::DATA     | data]]                 | bucket            | Datos estructurados y metadatos.          | CSV/JSON/Parquet      | Tablas, catálogos         | R: Data Eng · A: Arch      | [[VALD::]]               |
| SEM   | [[DIR::SEM      | semantics]]            | entity            | Vocabulario controlado y reglas.          | Términos, reglas      | IDs, contratos            | R: Ontology Lead · A: Arch | [[RULESET::]]            |
| AILE  | [[DIR::AILE     | ai\_learn]]            | bucket            | Entrenamiento, evaluación y feedback IA.  | Datasets, prompts     | Evals, insights           | R: MLE · A: Arch           | [[VALG::]]               |
| DEVP  | [[DIR::DEVP     | develop]]              | bucket            | Config, setup, orquestación desacoplada.  | Config, specs         | Entornos y conectores     | R: DevOps · A: Arch        | [[QMS::]]                |
| OTPL  | [[DIR::OTPL     | out\_template]]        | asset             | Plantillas de salida estándar.            | Reqs, lineamientos    | Documentos estandarizados | R: QMS · A: Arch           | [[VALD::]]               |
| GUID  | [[DIR::GUID     | guides]]               | asset             | Guías operativas y playbooks humanos.     | Procedimientos        | SOPs                      | R: QMS · A: Arch           | [[QMS::]]                |
| WF    | [[DIR::WF       | wf\_playbooks]]        | asset             | Workflows ejecutables.                    | Inputs, triggers      | Runs, logs                | R: Platform-Ops · A: Arch  | [[VALG::]]               |
| KCTX  | [[DIR::KCTX     | kns\_ctx\_vivo]]       | asset             | Contexto vivo y snapshots.                | Snapshots             | Estados reproducibles     | R: Platform-Ops · A: QMS   | [[CHG::]]                |
| CDEV  | [[DIR::CDEV     | core\_dev]]            | bucket            | Desarrollo núcleo.                        | Issues, spikes        | Módulos core              | R: Core Dev Lead · A: Arch | [[VALG::]]               |
| CARC  | [[DIR::CARC     | core\_arch\_platform]] | bucket            | Arquitectura de plataforma.               | ADRs, blueprints      | Artefactos de arq         | R: Architect · A: CTO      | [[ADR::]]                |
| LOG   | [[DIR::LOG      | log]]                  | bucket            | Registros de cambios y validaciones.      | Commits, runs         | CHG, VALG                 | R: QMS · A: Arch           | [[QMS::]]                |
| GIT   | [[DIR::GIT      | .github]]              | asset             | CI/CD y automatizaciones.                 | Workflows             | Checks, deployments       | R: DevOps · A: Arch        | [[QMS::]]                |
| PKG   | [[DIR::PKG      | packages]]             | bucket            | Paquetes y módulos compartidos.           | Código                | Librerías                 | R: Core Dev · A: Arch      | [[VALG::]]               |
| RULE  | [[DIR::RULE     | ruleset]]              | entity            | Políticas y reglas del repo.              | Normas                | Enforcement               | R: QMS · A: Arch           | [[RULESET::]]            |
| SCRIP | [[DIR::SCRIP    | scripts]]              | asset             | Utilidades de mantenimiento.              | Tareas                | Scripts ejecutables       | R: DevOps · A: Arch        | [[VALG::]]               |

---

## 2) Semantics (SEM)

| CODE | Nodo        | Tipo              | Función | Entradas                                   | Salidas       | Crossref          |                   |
| ---- | ----------- | ----------------- | ------- | ------------------------------------------ | ------------- | ----------------- | ----------------- |
| GLOS | [[DIR::GLOS | glossary]]        | entity  | Definir términos y definiciones canónicas. | PRs, términos | IDs, definiciones | [[GLOS::MAIN]]    |
| DICT | [[DIR::DICT | dicts]]           | entity  | Diccionarios operativos de términos.       | CSV/MD        | Diccionarios      | [[RULESET::DICT]] |
| CDCT | [[DIR::CDCT | code\_dict]]      | entity  | Mapeos de código a significado/acción.     | Matrices      | Code→Sem          | [[TPL::CODEMAP]]  |
| TDCT | [[DIR::TDCT | trigger\_dict]]   | entity  | Catálogo de triggers y contratos.          | Triggers      | Firmas y rutas    | [[WF::INDEX]]     |
| ADCT | [[DIR::ADCT | app\_dict]]       | entity  | Alias y metadatos de aplicaciones.         | Apps          | Aliases           | [[RULESET::APPS]] |
| PDCT | [[DIR::PDCT | prompt\_dict]]    | entity  | Prompts estandarizados y roles.            | Prompts       | Catálogo          | [[TPL::PROMPTS]]  |
| INGP | [[DIR::INGP | ingest\_prompts]] | asset   | Prompts para ingesta y parsing.            | Docs          | Extractos         | [[WF::INGEST]]    |
| VOC  | [[DIR::VOC  | vocabulary]]      | entity  | Vocabulario controlado y sinónimos.        | Términos      | Lexicón           | [[GLOS::VOC]]     |
| RSET | [[DIR::RSET | ruleset]]         | entity  | Reglas de negocio/técnicas.                | Normas        | Reglas            | [[RULESET::MAIN]] |

---

## 3) AI Learn (AILE)

| CODE  | Nodo         | Tipo           | Función | Entradas                                | Salidas     | Crossref         |                   |
| ----- | ------------ | -------------- | ------- | --------------------------------------- | ----------- | ---------------- | ----------------- |
| LEARN | [[DIR::LEARN | learning]]     | asset   | Currícula y objetivos de entrenamiento. | Datasets    | Plan de training | [[WF::TRAIN]]     |
| EVAL  | [[DIR::EVAL  | evaluation]]   | asset   | Evals, métricas y suites.               | Suites      | Reportes         | [[VALG::EVALS]]   |
| INSI  | [[DIR::INSI  | insights]]     | asset   | Hallazgos y análisis.                   | Logs, evals | Insights         | [[CHG::INSIGHTS]] |
| FTUN  | [[DIR::FTUN  | fine\_tuning]] | asset   | Ajuste fino de modelos.                 | Datasets    | Modelos          | [[WF::FT]]        |
| FSHT  | [[DIR::FSHT  | few\_shot]]    | asset   | Ejemplos canónicos.                     | Casos       | Ejemplos         | [[TPL::FS]]       |
| RELV  | [[DIR::RELV  | relevance]]    | asset   | Ranking y recall.                       | Queries     | Scores           | [[WF::RAG]]       |
| TRNG  | [[DIR::TRNG  | training]]     | asset   | Sesiones de entrenamiento.              | Config      | Modelos          | [[WF::TRAIN]]     |
| FDBK  | [[DIR::FDBK  | feedback]]     | asset   | Retroalimentación y bucles.             | Feedback    | Cambios plan     | [[WF::FB]]        |

---

## 4) Out Templates (OTPL)

| CODE  | Nodo         | Tipo             | Función | Entradas                      | Salidas      | Crossref   |                  |
| ----- | ------------ | ---------------- | ------- | ----------------------------- | ------------ | ---------- | ---------------- |
| MTX   | [[DIR::MTX   | mtx]]            | asset   | Matrices comparativas.        | Criterios    | Scores     | [[TPL::MTX]]     |
| MATR  | [[DIR::MATR  | matrix]]         | asset   | Scoring reproducible.         | Pesos        | Puntajes   | [[TPL::MTX]]     |
| TBLS  | [[DIR::TBLS  | table]]          | asset   | Tablas estándar.              | Datos        | Tablas     | [[TPL::TABLE]]   |
| RCSH  | [[DIR::RCSH  | record\_sheet]]  | asset   | Planillas registrables.       | Datos        | Planillas  | [[TPL::RCSH]]    |
| MAPP  | [[DIR::MAPP  | mapping]]        | asset   | Mapeos de origen-destino.     | Campos       | Mapas      | [[TPL::MAP]]     |
| RELN  | [[DIR::RELN  | relation]]       | asset   | Relaciones entre entidades.   | Entidades    | Relaciones | [[TPL::REL]]     |
| VALD  | [[DIR::VALD  | validation]]     | asset   | Validaciones y checks.        | Reglas       | Logs       | [[QMS::VAL]]     |
| COMP  | [[DIR::COMP  | comparison]]     | asset   | Comparativas de alternativas. | Alternativas | Reportes   | [[TPL::COMP]]    |
| OTPD  | [[DIR::OTPD  | docs]]           | asset   | Documentos de salida.         | Reqs         | Docs       | [[TPL::DOC]]     |
| WSPC  | [[DIR::WSPC  | workspaces]]     | asset   | Espacios de trabajo.          | Config       | Entornos   | [[RULESET::ENV]] |
| PARCH | [[DIR::PARCH | platform\_arch]] | asset   | Artefactos de arquitectura.   | ADR, BP      | Blueprints | [[ADR::0001]]    |
| ATOOL | [[DIR::ATOOL | ai\_tools]]      | asset   | Herramientas IA empaquetadas. | Specs        | Tools      | [[WF::TOOLS]]    |

---

## 5) Guides (GUID)

| CODE | Nodo        | Tipo               | Función | Entradas                 | Salidas | Crossref   |                |
| ---- | ----------- | ------------------ | ------- | ------------------------ | ------- | ---------- | -------------- |
| PLIN | [[DIR::PLIN | planin]]           | asset   | Planeamiento y gobierno. | Reqs    | Planes     | [[TPL::PLAN]]  |
| MPLN | [[DIR::MPLN | mpln]]             | asset   | Master plan.             | Insumos | MPlan      | [[ADR::0001]]  |
| BCRT | [[DIR::BCRT | brainstorm\_crtv]] | asset   | Ideación estructurada.   | Ideas   | Backlog    | [[TPL::BRAIN]] |
| RCTL | [[DIR::RCTL | run\_control]]     | asset   | Control de ejecución/QA. | Reglas  | Checks     | [[QMS::RUN]]   |
| PIPE | [[DIR::PIPE | pipeline]]         | asset   | Flujos/ETL.              | Fuentes | Artefactos | [[WF::PIPE]]   |

---

## OutputTemplate

```yaml
output_example:
  status: BASELINE_LOCKED
  baseline_id: BL-2025-08-18-BucketsMap-v1.0.0
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - files_frozen: [core/doc/workbench/AINGZ_V5_Buckets_Assets_Entidades_Baseline_v1_full.md]
  log:
    - step1: qa_pass
    - step2: checkpoint
    - step3: freeze
```


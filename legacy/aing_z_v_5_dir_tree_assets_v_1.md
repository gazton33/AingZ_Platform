---

## file: core/doc/workbench/AINGZ\_V5\_Baselines\_Unificados\_v1\_4\_visual\_plus\_functions.md code: ARB\_AST\_VIZ name: BaselineV1\_4\_VisualFunctions version: v1.4 date: 2025-08-16 owner: AingZ\_Platform · QMS status: locked (derived) refs: baseline\_locked: core/doc/workbench/AINGZ\_V5\_Baselines\_Unificados\_v1\_4\_locked.md baseline\_prev: core/doc/workbench/AINGZ\_V5\_Baselines\_Unificados\_v1\_3\_locked.md glosario\_final: main/data\_base/core\_actv/data/semantics/glossary/GLOS\_AINGZ\_V5\_FULL\_v1\_0.md sem\_ruleset: main/data\_base/core\_actv/data/semantics/ruleset/SEM\_RULESET\_AINGZ\_V5\_v0\_1.md legacy\_ref: /mnt/data/aingz\_v\_5\_baselines\_unificados\_dir\_tree\_assets\_v\_1.md chkp: main/data\_base/core\_actv/data/guides/planin/chkp/CHKP\_2025\_08\_16\_GLOSv1\_0.md triggers: [TRG\_AUDIT\_TL, TRG\_CONSOLIDATE\_TL] chg: [CHG-2025-08-16-002, CHG-2025-08-16-003, CHG-2025-08-16-004, CHG-2025-08-16-005] chk: CHK#baseline\_v1\_4\_visual\_functions notes: "Vista enriquecida: funciones por bucket, descripciones ampliadas por asset, compatibilidad **legacy (wf|workflow)** → **wf\_playbooks**."

# AingZ V5 — **Dir Tree + Assets v1.4** · Visual + Functions (Enriched)

> **Objetivo**: mejorar **visualización** y **detalle funcional** del árbol **v1.4 (LOCKED)**. Incluye **descripciones de función por bucket** y **especificaciones ampliadas de assets** alineadas al **Glosario v1.0** y al **SEMR (RwB)**.

---

## 0) Leyenda de lectura rápida

- **[BKT]** = *Bucket/Folder* principal (función operativa)
- **(Inputs → Outputs)** = flujo típico de información
- **Governance** = rol custodio + QA
- **Legacy** = alias/paths históricos compatibles

---

## 1) Visual del árbol con funciones (anotado)

```text
main/
  data_base/
    core_actv/
      docs/                 [BKT] Fuentes documentales (entrada humana/externa)
        audio/              grabaciones y notas de voz → (transcripts, insights)
        image/              imágenes/diagramas → (annotations, assets derivados)
        video/              videos/presentaciones → (transcripts, clips)
        library/            bibliografía/corpus → (citables, refs)
        onboard/            notas internas → (contexto, decisions log)
      data/                 [BKT] Datos de trabajo y conocimiento estructurado
        semantics/          autoridad semántica → (glosario, diccionarios)
        ai_learn/           aprendizaje/evaluación → (labels, evals, ft)
        develop/            configuración y reglas → (ruleset, specs, setup)
        out_template/       plantillas de salida (estructuras de resultados)
          mtx/              matrices/tablas comunes
          docs/             plantillas de documentos
          workspaces/       plantillas de espacios de trabajo
          platform_arch/    plantillas de arquitectura de plataforma
          ai_tools/         plantillas de herramientas/agents AI
        guides/             guías operativas → (planificación, pipeline, run)
          planin/           planeamiento (MPLN/BLP/BLN/PLN/RMAP/TSK/CHK/CHKP)
          run_control/      control de ejecución (START/STOP/RESUME/ROLLBACK)
          pipeline/         procedimientos de proceso (CRTR/RLEV/...)
        wf_playbooks/       playbooks (paso a paso) → generan assets
      log/                  [BKT] QMS y evidencia → (CHG/VALOG/TRC/XRF/VER)
        changelog/          cambios/versionado semántico
        validation/         resultados de QA y validaciones
        qms/                trazabilidad y referencias cruzadas
```

> **Compatibilidad (legacy)**: donde la documentación antigua referencia `` o ``, el destino **v1.4** es `data/wf_playbooks/`.

---

## 2) Función por bucket (tabla ampliada)

| Bucket/Path            | Función (qué es)                                                                  | Inputs típicos                    | Outputs típicos                            | Consumers  | Governance             |
| ---------------------- | --------------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------ | ---------- | ---------------------- |
| `docs/*`               | Repositorio de **fuentes documentales** (entrada primaria)                        | audio, imágenes, videos, textos   | transcripts, annotations, refs             | AI/Analyst | Docs Owner + QA(CHK)   |
| `data/semantics/*`     | **Autoridad semántica** del proyecto                                              | LSWP, glosarios previos           | glosario, diccionarios, vocabulario        | All        | Semantic Owner + VALD  |
| `data/ai_learn/*`      | **Aprendizaje y evaluación** de modelos                                           | datasets, labels, prompts         | evals, ft artifacts, feedback              | AI/ML      | Learning Owner + EVAL  |
| `data/develop/*`       | **Reglas y configuración** de plataforma                                          | specs, configs, ruleset           | manifiestos, setup scripts                 | DevOps     | Dev Owner + RULE       |
| `data/out_template/*`  | **Plantillas de salida** para **resultados estructurados**                        | requirements, schema defs         | CSV/JSON/MD templates                      | All        | Templates Owner + VALD |
| `guides/planin/*`      | **Planeamiento** y dirección de trabajo                                           | objetivos, backlog                | MPLN, BLP, PLN, CHKP                       | PM/Arch    | Guides Owner           |
| `guides/run_control/*` | **Procedimientos de ejecución controlada**                                        | baseline\_locked, sem\_ruleset    | logs de run, checkpoints, restore evidence | PM/Ops     | Guides Owner + QMS     |
| `guides/pipeline/*`    | **Procedimientos técnicos** (crear, validar, migrar, limpiar, etc.)               | specs, playbooks                  | reportes, estados intermedios              | Dev/AI     | Guides Owner           |
| `wf_playbooks/*`       | **Instrucciones paso a paso** para generar **assets** con OutputTemplate embebido | fuentes, parámetros, herramientas | artefactos listos y evidencias             | AI/Dev     | Playbooks Owner + QA   |
| `log/*`                | **Calidad y conformidad (QMS)**                                                   | evidencias de QA, cambios         | CHG, VALOG, TRC, XRF, VER                  | All/QMS    | QMS Owner              |

---

## 3) Catálogo de assets — Especificaciones ampliadas

> **Formato** por asset: **Purpose** · **RequiredMeta** · **OptionalMeta** · **Formats** · **Lifecycle** · **Triggers**

### 3.1 `docs/*`

- **AUD · AudioDoc**\
  Purpose: fuente de audio para registro/ingest.\
  RequiredMeta: `title, date, source, speakers[]`\
  OptionalMeta: `language, duration, transcription_id`\
  Formats: `wav, mp3, m4a`\
  Lifecycle: ingest → transcribe → index → link a insights\
  Triggers: `TRG_CONSOLIDATE_TL`
- **IMG · ImageDoc**\
  Purpose: imagen/diagrama con descripción mínima y fuente.\
  RequiredMeta: `title, date, source`\
  OptionalMeta: `resolution, annotations[]`\
  Formats: `png, jpg, svg, pdf(page)`\
  Lifecycle: ingest → annotate → index\
  Triggers: `TRG_CONSOLIDATE_TL`
- **VID · VideoDoc**\
  Purpose: video/presentación; puede requerir transcripción.\
  RequiredMeta: `title, date, source`\
  OptionalMeta: `duration, transcription_id`\
  Formats: `mp4, mkv, webm`\
  Lifecycle: ingest → transcribe → clip/summary\
  Triggers: `TRG_CONSOLIDATE_TL`
- **LIB · LibraryRef**\
  Purpose: bibliografía/corpus externo citable.\
  RequiredMeta: `title, authors[], year, publisher|venue`\
  OptionalMeta: `doi|isbn, url`\
  Formats: `pdf, bib, md`\
  Lifecycle: ingest → cite → reference map\
  Triggers: `TRG_AUDIT_TL`
- **ONB · OnboardNotes**\
  Purpose: notas internas de onboarding.\
  RequiredMeta: `author, date`\
  OptionalMeta: `related_tasks[]`\
  Formats: `md, txt`\
  Lifecycle: capture → link → archive\
  Triggers: `TRG_CONSOLIDATE_TL`

### 3.2 `data/semantics/*`

- **GLOS · Glossary**\
  Purpose: autoridad semántica del proyecto.\
  RequiredMeta: `version, status, baseline_id`\
  OptionalMeta: `deprecations[], mapx_path`\
  Formats: `md, yaml`\
  Lifecycle: draft → valog → final → lock\
  Triggers: `TRG_AUDIT_TL`
- **DTRG · TriggerDict**\
  Purpose: diccionario de triggers + contrato/uso.\
  RequiredMeta: `trigger_id, contract`\
  Formats: `md, yaml`
- **DCD · CodeDict**\
  Purpose: catálogo de `CODE≤5` ↔ `Name`.\
  RequiredMeta: `code, name`\
  QA: unicidad/regex
- **DAPP · AppDict**\
  Purpose: apps/servicios internos.\
  RequiredMeta: `app_id, contract`
- **DPRM · PromptDict**\
  Purpose: prompts y campos parametrizables.\
  RequiredMeta: `prompt_id, input_schema`
- **IPRM · IngestPrompts**\
  Purpose: prompts de ingestión.\
  RequiredMeta: `pipeline_id, steps[]`
- **VCB · Vocabulary**\
  Purpose: vocabulario controlado.\
  RequiredMeta: `term, alias[]`
- **SEMR · SemRuleset**\
  Purpose: reglas RwB/semántica y operación.\
  RequiredMeta: `rules[], qa[]`

### 3.3 `data/ai_learn/*`

- **LEARN · Learning** — registros de aprendizaje (datasets, sesiones).
- **EVAL · Evaluation** — métricas, curvas, verdicts.
- **INSI · Insight** — hallazgos curados, decisiones.
- **FTUNE · FineTuning** — artefactos de ajuste fino.
- **FSHOT · FewShot** — conjuntos de ejemplos.
- **RLEV · Relevance** — labels/señales de relevancia.
- **TRN · Training** — datasets de entrenamiento.
- **FDBK · Feedback** — feedback interno/externo.

> **Meta común (AI Learn)**: `dataset_id|exp_id, model, split, metrics{}`; Formats: `jsonl, parquet, csv, md`.

### 3.4 `data/develop/*`

- **RULE · Ruleset** — normativa técnica (naming, contratos).
- **CFG · Configuration** — parámetros por entorno (YAML).
- **SETUP · SetupGuide** — guía de preparación.
- **CSTM · Customization** — ajustes/adaptaciones.
- **SPEC · Specs** — especificaciones funcionales/técnicas.
- **PREF · Preferences** — overrides no críticos.
- **CNCTR · Connectors** — integración a servicios externos.
- **ORCH · Orchestrator** — definiciones del orquestador/flow.

### 3.5 `data/out_template/*`

- **MTX sub-bucket**: `MTR, TBL, RSHT, MAPX, RELN, VALD, VRS`\
  Spec común: `schema_fields[], export{csv,json,yaml,md}, example_file`.
- **DOCS/WSPC/PARCH/ATOOL** (nuevos): ver esquemas en Glosario v1.0 §1.6;\
  Propósito: empaquetar resultados repetibles con **front‑matter** estándar.

### 3.6 `guides/*`

- **PLANIN** (`MPLN, BLP, BLN, PLN, RMAP, TSK, CHK, CHKP, FDBK, VALD, OBJU`)\
  Purpose: dirección, planeamiento y checkpoints.
- **RUN CONTROL** (`RCNT`)\
  Purpose: control seguro de ejecución; sub‑entradas **START/STOP/RESUME/ROLLBACK**;\
  Evidencias: `rcnt_*.log, rcnt_state.chk, rcnt_restore.evd`.
- **PIPELINE** (`CRTR, RLEV, AUDT, CNSL, MIGR, UPDT, CLNP, VALD, TST, LITW, RPT, CLON`)\
  Purpose: procedimientos técnicos por etapa.

### 3.7 `wf_playbooks/*`

- **WFPB · WorkflowPlaybook**\
  Purpose: guías paso a paso para generar un **asset**;\
  RequiredMeta: `inputs[], tools[], preconditions[]`;\
  Output: asset + **OutputTemplate** embebido;\
  **Legacy**: `wf/` | `workflow/`.

### 3.8 `log/*`

- **CHG** — cambios/publicación de versiones.
- **BIT** — bitácora extendida.
- **ADT** — evidencias de auditoría.
- **VALOG** — resultados de QA/tests.
- **TRC** — trazabilidad cruzada.
- **XRF** — referencias cruzadas.
- **VER** — versioning del sistema.

---

## 4) Compatibilidad y mapeo **legacy** → **v1.4**

| Legacy (antiguo)      | v1.4 (actual)             | Tipo    | Nota de migración                       |
| --------------------- | ------------------------- | ------- | --------------------------------------- |
| `wf/`, `workflow/`    | `data/wf_playbooks/`      | rename  | Actualizar crossrefs en docs y scripts  |
| `PIPE (script)`       | `guides/pipeline/*`       | norma   | Preferir `CRTR/UPDT/CLNP/...` por etapa |
| `RWB/RWS` (semántica) | `SPEC` (en develop/specs) | replace | Mantener como alias histórico en GLOS   |

> **CHG-2025-08-16-005 (propuesto)**: Documentar formalmente la compatibilidad `wf|workflow` → `wf_playbooks`.

---

## 5) Checklist de afinamiento (visual + funciones)

-

---

## OutputTemplate (de este documento)

```yaml
output_example:
  status: OK
  id_asset: baseline_v1_4_visual_functions
  generated_by: ai
  created_at: 2025-08-16T00:00:00-03:00
  params:
    - baseline_locked: AINGZ_V5_Baselines_Unificados_v1_4_locked.md
    - enrich: [bucket_functions, asset_specs, legacy_map]
  result:
    - tables: [bucket_functions, asset_catalog]
    - actions: [crossref_sweep, out_template_concrete_schemas]
  log:
    - step1: analyze_baseline
    - step2: enrich_specs
    - step3: publish_visual
```


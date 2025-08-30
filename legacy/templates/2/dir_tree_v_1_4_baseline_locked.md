---

file: core/doc/workbench/AINGZ\_V5\_DirTree\_v1\_4\_baseline\_locked.md code: ARBBL name: DirTreeV14BaselineLocked version: v1.4.2 date: 2025-08-18 owner: AingZ\_Platform · RwB status: locked referencias: [DirTreeV14Aligned, aing\_z\_v\_5\_dir\_tree\_v\_1.md] triggers: [TRG\_BASELINE\_LOCK] cambios:

- 2025-08-18: Freeze de la vista alineada con notas y códigos. checks:
- Vista ASCII con columnas fijas
- Índice de códigos presente
- Descripciones breves coherentes

---

# Baseline Lock — Árbol de Directorios v1.4.2

**Baseline-ID**: BL-2025-08-18-DirTree-v1.4.2\
**Origen**: DirTreeV14Aligned (v1.4.2)\
**Alcance**: Estructura visual con [CODE] y descripción alineados.

> Estado congelado. Cualquier cambio futuro debe realizarse en un *working copy* y proponer nuevo lock.

## Árbol congelado

```text
AingZ_Platform                                        [ROOT]  — raíz del repositorio
├── main                                              [MAIN]  — código y datos activos
│   ├── data_base                                     [DB]    — base de conocimiento
│   │   ├── core_actv                                 [CACT]  — activos nucleares
│   │   │   ├── docs                                  [DOCS]  — media y documentación
│   │   │   │   ├── audio                             [AUD]   — insumos de audio
│   │   │   │   ├── image                             [IMG]   — insumos de imagen
│   │   │   │   ├── video                             [VID]   — insumos de video
│   │   │   │   ├── library                           [LIB]   — papers y libros
│   │   │   │   └── onboard                           [ONB]   — materiales de onboarding
│   │   │   ├── data                                  [DATA]  — datasets y metadatos
│   │   │   │   ├── semantics                         [SEM]   — semántica de plataforma
│   │   │   │   │   ├── glossary                      [GLOS]  — glosarios
│   │   │   │   │   ├── dicts                         [DICT]  — diccionarios
│   │   │   │   │   ├── code_dict                     [CDCT]  — mapeos de código
│   │   │   │   │   ├── trigger_dict                  [TDCT]  — dicc. de triggers
│   │   │   │   │   ├── app_dict                      [ADCT]  — apps y aliases
│   │   │   │   │   ├── prompt_dict                   [PDCT]  — prompts estándar
│   │   │   │   │   ├── ingest_prompts                [INGP]  — prompts de ingesta
│   │   │   │   │   ├── vocabulary                    [VOC]   — vocabulario controlado
│   │   │   │   │   └── ruleset                        [RSET]  — reglas y políticas
│   │   │   │   ├── ai_learn                          [AILE]  — aprendizaje de la IA
│   │   │   │   │   ├── learning                      [LEARN] — currícula
│   │   │   │   │   ├── evaluation                    [EVAL]  — evals y métricas
│   │   │   │   │   ├── insights                      [INSI]  — hallazgos
│   │   │   │   │   ├── fine_tuning                   [FTUN]  — ajustes finos
│   │   │   │   │   ├── few_shot                      [FSHT]  — ejemplos canónicos
│   │   │   │   │   ├── relevance                     [RELV]  — ranking/recall
│   │   │   │   │   ├── training                      [TRNG]  — sesiones de training
│   │   │   │   │   └── feedback                      [FDBK]  — retroalimentación
│   │   │   │   ├── develop                           [DEVP]  — desarrollo de plataforma
│   │   │   │   │   ├── ruleset                       [RDEV]  — reglas de dev
│   │   │   │   │   ├── config                        [CNFG]  — configuración
│   │   │   │   │   ├── setup                         [SETUP] — instalación
│   │   │   │   │   ├── customization                 [CSTM]  — personalización
│   │   │   │   │   ├── specs                         [SPECS] — especificaciones
│   │   │   │   │   ├── preferences                   [PREF]  — preferencias
│   │   │   │   │   ├── connectors                    [CNTR]  — puertos/adaptadores
│   │   │   │   │   └── orchestrator                  [ORCH]  — orquestador/wf
│   │   │   │   ├── out_template                      [OTPL]  — plantillas de salida
│   │   │   │   │   ├── mtx                           [MTX]   — matrices comparativas
│   │   │   │   │   │   ├── matrix                    [MATR]  — scoring
│   │   │   │   │   │   ├── table                     [TBLS]  — tablas
│   │   │   │   │   │   ├── record_sheet              [RCSH]  — planillas
│   │   │   │   │   │   ├── mapping                   [MAPP]  — mapeos
│   │   │   │   │   │   ├── relation                  [RELN]  — relaciones
│   │   │   │   │   │   ├── validation                [VALD]  — validaciones
│   │   │   │   │   │   └── comparison                [COMP]  — comparativas
│   │   │   │   │   ├── docs                          [OTPD]  — docs para outputs
│   │   │   │   │   ├── workspaces                    [WSPC]  — espacios de trabajo
│   │   │   │   │   ├── platform_arch                 [PARCH] — arq de plataforma
│   │   │   │   │   └── ai_tools                      [ATOOL] — herramientas IA
│   │   │   │   └── guides                            [GUID]  — guías operativas
│   │   │   │       ├── planin                        [PLIN]  — planeamiento
│   │   │   │       │   ├── mpln                      [MPLN]  — master plan
│   │   │   │       │   └── brainstorm_crtv           [BCRT]  — ideación
│   │   │   │       ├── run_control                   [RCTL]  — ejecución/QA
│   │   │   │       └── pipeline                      [PIPE]  — flujos/ETL
│   │   │   ├── wf_playbooks                          [WF]    — playbooks de workflows
│   │   │   └── kns_ctx_vivo                          [KCTX]  — contexto vivo
│   │   ├── core_dev                                  [CDEV]  — desarrollo núcleo
│   │   └── core_arch_platform                         [CARC]  — arq. de plataforma
├── log                                               [LOG]   — cambios y calidad
│   ├── changelog                                     [CHG]   — registro de cambios
│   ├── validation                                    [VALG]  — logs de validación
│   └── qms                                           [QMS]   — calidad y normas
├── .github                                           [GIT]   — CI/CD y workflows
├── packages                                          [PKG]   — paquetes y módulos
├── ruleset                                           [RULE]  — políticas del repo
└── scripts                                           [SCRIP] — utilidades y tareas
```

---

## OutputTemplate

```yaml
output_example:
  status: BASELINE_LOCKED
  baseline_id: BL-2025-08-18-DirTree-v1.4.2
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - files_frozen: [core/doc/workbench/AINGZ_V5_DirTree_v1_4_baseline_locked.md]
  log:
    - step1: qa_pass
    - step2: checkpoint
    - step3: freeze
```


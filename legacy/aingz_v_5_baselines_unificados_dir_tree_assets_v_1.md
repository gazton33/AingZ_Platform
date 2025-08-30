---

## file: core/doc/workbench/AINGZ\_V5\_Baselines\_Unificados\_v1\_3\_locked.md

code: ARB+AST\_BASE name: AingzV5BaselinesUnificados version: v1.3 status: baseline\_locked date: 2025-08-15 owner: AingZ\_Platform · RwB notes: "Baseline final de Árbol + Assets. Vista de árbol mejorada. Incluye checklist aplicado, pendientes y ctx\_package. (Se mantiene separación out\_template/\* vs wf\_template/\*)"

**Baseline-ID:** BL-2025-08-15-ARB+AST-v1.3

---

# AINGZ V5 — Baselines Unificados (Directorio + Assets) — **LOCKED**

> Origen: snapshots Excalidraw + canvas previos. Esta versión consolida v1.1–v1.2, aplica correcciones de naming aprobadas (excepto unificación de templates), y queda como referencia estable para las próximas etapas.

---

## 1) Árbol de Directorios — **Vista Mejorada (Tree)**

```
AingZ_Platform/
├── main/
├── .github/
├── data_base/
│   ├── core_actv/
│   │   ├── docs/
│   │   │   ├── audio/            → [notas_de_voz, reuniones, entrevistas, podcast, audio_de_video]
│   │   │   ├── image/            → [fotos, imagenes, graficos, esquemas, diagramas, planos, explosiones]
│   │   │   ├── video/            → [videos, youtube, animaciones, presentaciones]
│   │   │   ├── library/          → [libros, manuales, guias, articulos, papers]
│   │   │   └── onboard/          → [notas, mensajes, observaciones]
│   │   ├── data/
│   │   │   ├── semantics/        → [glossary, dict_trigger, dict_code, dict_app, dict_prompt, ing_prompt, vocabulary]
│   │   │   ├── ai_learn/         → [learn, eval, insi, tune, shot, rel, trn, feedback]
│   │   │   ├── develop/          → [rulset, config, setup, custom, spec, preference, conectors, orquestador]
│   │   │   ├── out_template/
│   │   │   │   ├── mtx/          → [matrix, tabla, ficha, mapping, relation, validation, versus]
│   │   │   │   ├── docs/         → [pendiente]
│   │   │   │   ├── workspaces/   → [pendiente]
│   │   │   │   ├── platform_arch/→ [pendiente]
│   │   │   │   └── ai_tools/     → [pendiente]
│   │   │   └── guides/
│   │   │       ├── planin/
│   │   │       │   ├── mpln/     → [mplan, blueprint, baseline, /plans, /roadmaps, /task, /checklist, /checkpoint, /feedback, /validacion, /update_objective]
│   │   │       │   └── brainstorm_crtv/ → [brainstorm, insights, ideas, draft, notas, nodo(chkpnt), nodo_changes, snapshots]
│   │   │       ├── run_control/  → [pendiente]
│   │   │       └── pipeline/     → [creator, relev, auditoria, consolidado, migracion, update, cleanup, validation, test, literal_work, report, clone]
│   │   ├── kns_ctx_vivo/
│   │   └── wf_template/
│   ├── core_dev/
│   └── core_arch_platform/
├── log/
│   ├── changelog/                → [changelog, logbook, auditlog, validationlog]
│   └── qms/                      → [trace, crossref, version]
├── packages/
├── ruleset/
└── scripts/
```

> Leyenda: cada carpeta final muestra entre corchetes **los assets relevados**. Donde figura "pendiente" no hubo lista explícita en Excalidraw.

---

## 2) **Assets Baseline Unificado** (por ruta final)

> Formato: `path_final` → **Assets (fuente)** · *alias\_final (corrección aplicada)*

- `main/data_base/core_actv/docs/audio/` → notas\_de\_voz, reuniones, entrevistas, podcast, audio\_de\_video · *audio\_notes, meetings, interviews, podcast, audio\_from\_video*
- `main/data_base/core_actv/docs/image/` → fotos, imagenes, graficos, esquemas, diagramas, planos, explosiones · *photos, images, graphics, schematics, diagrams, blueprints, exploded\_views*
- `main/data_base/core_actv/docs/video/` → videos, youtube, animaciones, presentaciones · *videos, youtube, animations, presentations*
- `main/data_base/core_actv/docs/library/` → libros, manuales, guias, articulos, papers · *books, manuals, guides, articles, papers*
- `main/data_base/core_actv/docs/onboard/` → notas, mensajes, observaciones · *notes, messages, observations*
- `main/data_base/core_actv/data/semantics/` → glossary, dict\_trigger, dict\_code, dict\_app, dict\_prompt, ing\_prompt, vocabulary · *glossary, trigger\_dict, code\_dict, app\_dict, prompt\_dict, ingest\_prompts, vocabulary*
- `main/data_base/core_actv/data/ai_learn/` → learn, eval, insi, tune, shot, rel, trn, feedback · *learning, evaluation, insights, fine\_tuning, few\_shot, relevance, training, feedback*
- `main/data_base/core_actv/data/develop/` → rulset, config, setup, custom, spec, preference, conectors, orquestador · *ruleset, config, setup, customization, specs, preferences, connectors, orchestrator*
- `main/data_base/core_actv/data/out_template/mtx/` → matrix, tabla, ficha, mapping, relation, validation, versus · *matrix, table, record\_sheet, mapping, relation, validation, comparison*
- `main/data_base/core_actv/data/out_template/docs/` → **(pendiente)**
- `main/data_base/core_actv/data/out_template/workspaces/` → **(pendiente)**
- `main/data_base/core_actv/data/out_template/platform_arch/` → **(pendiente)**
- `main/data_base/core_actv/data/out_template/ai_tools/` → **(pendiente)**
- `main/data_base/core_actv/data/guides/planin/mpln/` → mplan, blueprint, baseline, /plans, /roadmaps, /task, /checklist, /checkpoint, /feedback, /validacion, /update\_objective · *master\_plan, blueprint, baseline, plans, roadmaps, tasks, checklists, checkpoints, feedback, validation, objective\_update*
- `main/data_base/core_actv/data/guides/planin/brainstorm_crtv/` → brainstorm, insights, ideas, draft, notas, nodo(chkpnt), nodo\_changes, snapshots · *brainstorm, insights, ideas, drafts, notes, node\_checkpoint, node\_changes, snapshots*
- `main/data_base/core_actv/data/guides/run_control/` → **(pendiente)**
- `main/data_base/core_actv/data/guides/pipeline/` → creator, relev, auditoria, consolidado, migracion, update, cleanup, validation, test, literal\_work, report, clone · *creator, relevance, audit, consolidation, migration, update, cleanup, validation, test, literal\_work, report, clone*
- `main/log/changelog/` → changelog, logbook, auditlog, validationlog · *change\_log, logbook, audit\_log, validation\_log*
- `main/log/qms/` → trace, crossref, version · *traceability, cross\_ref, versioning*

---

## 3) Correcciones de Naming **aplicadas en v1.3** (registro)

- docs/image/: `imagenes`→`images`, `graficos`→`graphics`, `esquemas`→`schematics`, `planos`→`blueprints`, `explosiones`→`exploded_views` ✅
- docs/video/: `presentaciones` (corrige `presentac`)→`presentations` ✅
- data/semantics/: `ing_prompt`→`ingest_prompts` ✅
- data/ai\_learn/: `insi`→`insights`, `rel`→`relevance`, `trn`→`training`, `tune`→`fine_tuning`, `shot`→`few_shot` ✅
- data/develop/: `rulset`→`ruleset`, `custom`→`customization`, `spec`→`specs`, `preference`→`preferences`, `conectors`→`connectors`, `orquestador`→`orchestrator` ✅
- guides/planin/mpln/: `update_objective`→`objective_update`, `validacion`→`validation` ✅
- guides/planin/brainstorm\_crtv/: normaliza `nodo`→`node`, `nodo_changes`→`node_changes`, typo "Barinstorm"→`Brainstorm` ✅
- log/: `auditlog`→`audit_log`, `validationlog`→`validation_log` ✅
- qms/: `crossref`→`cross_ref` ✅

> **Explícito:** NO se unifican `out_template/*` y `wf_template/*`. (Se mantiene separación hasta nuevo diseño.)

---

## 4) Pendientes (para próxima iteración)

- Definir assets para: `out_template/{docs, workspaces, platform_arch, ai_tools}` y `guides/run_control`.
- Completar glosario alineado a alias\_final y códigos.
- Iniciar ER model, CrossRef y esqueleto de Pipeline (solo after glosario).

---

## 5) Checklist — Próxima etapa (Glosario + Nueva Arch)

-

---

## 6) ctx\_package — Snapshots del Hilo

```yaml
ctx_package:
  id: BL-2025-08-15-ARB+AST-v1.3
  date: 2025-08-15
  sources:
    - excalidraw_blocks: [docs/*, data/* (out_template, guides), log/*]
    - canvas_docs:
        - Aingz V5 — Árbol De Directorios (baseline · 2025-08-15)
        - Aingz V5 — Baselines Unificados (dir Tree + Assets) · V1 (v1.1–v1.2)
        - Aingz V5 — Baselines Unificados (dir Tree + Assets) · v1.3 (Locked)
  decisions:
    - Mantener separación entre out_template/* y wf_template/*.
    - Aplicar correcciones de naming listadas.
    - Marcar como pendiente lo no especificado en Excalidraw.
  next:
    - Consolidar Glosario v5 y alinear con árbol + assets.
    - Iniciar modelo ER, CrossRef y Pipeline esqueleto.
```

---

## Estado

**baseline\_locked** — Documento listo como referencia estable. Cualquier cambio se hará en una copia **WIP** derivada de esta versión.


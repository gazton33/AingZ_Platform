---

## file: core/doc/workbench/AINGZ\_V5\_Baselines\_Unificados\_v1\_4\_ascii\_tree.md code: ARB\_AST\_ASC name: BaselineV1\_4\_AsciiTree version: v1.4 date: 2025-08-16 owner: AingZ\_Platform · QMS status: locked (derived) refs: source\_visual: core/doc/workbench/AINGZ\_V5\_Baselines\_Unificados\_v1\_4\_visual\_plus\_functions.md baseline\_locked: core/doc/workbench/AINGZ\_V5\_Baselines\_Unificados\_v1\_4\_locked.md glosario\_final: main/data\_base/core\_actv/data/semantics/glossary/GLOS\_AINGZ\_V5\_FULL\_v1\_0.md notes: "Árbol con **líneas ASCII** (├── │ └──) para no perder niveles. Sin anotaciones extensas; sólo nombres canónicos."

# AingZ V5 — Dir Tree v1.4 (ASCII Lines)

**Leyenda:** `├──` rama intermedia · `└──` última rama · `│` continuidad de nivel

```text
AingZ_Platform
├── main
│   ├── data_base
│   │   ├── core_actv
│   │   │   ├── docs
│   │   │   │   ├── audio
│   │   │   │   ├── image
│   │   │   │   ├── video
│   │   │   │   ├── library
│   │   │   │   └── onboard
│   │   │   ├── data
│   │   │   │   ├── semantics
│   │   │   │   │   ├── glossary
│   │   │   │   │   ├── dicts
│   │   │   │   │   ├── code_dict
│   │   │   │   │   ├── trigger_dict
│   │   │   │   │   ├── app_dict
│   │   │   │   │   ├── prompt_dict
│   │   │   │   │   ├── ingest_prompts
│   │   │   │   │   ├── vocabulary
│   │   │   │   │   └── ruleset
│   │   │   │   ├── ai_learn
│   │   │   │   │   ├── learning
│   │   │   │   │   ├── evaluation
│   │   │   │   │   ├── insights
│   │   │   │   │   ├── fine_tuning
│   │   │   │   │   ├── few_shot
│   │   │   │   │   ├── relevance
│   │   │   │   │   ├── training
│   │   │   │   │   └── feedback
│   │   │   │   ├── develop
│   │   │   │   │   ├── ruleset
│   │   │   │   │   ├── config
│   │   │   │   │   ├── setup
│   │   │   │   │   ├── customization
│   │   │   │   │   ├── specs
│   │   │   │   │   ├── preferences
│   │   │   │   │   ├── connectors
│   │   │   │   │   └── orchestrator
│   │   │   │   ├── out_template
│   │   │   │   │   ├── mtx
│   │   │   │   │   │   ├── matrix
│   │   │   │   │   │   ├── table
│   │   │   │   │   │   ├── record_sheet
│   │   │   │   │   │   ├── mapping
│   │   │   │   │   │   ├── relation
│   │   │   │   │   │   ├── validation
│   │   │   │   │   │   └── comparison
│   │   │   │   │   ├── docs
│   │   │   │   │   ├── workspaces
│   │   │   │   │   ├── platform_arch
│   │   │   │   │   └── ai_tools
│   │   │   │   └── guides
│   │   │   │       ├── planin
│   │   │   │       │   ├── mpln
│   │   │   │       │   └── brainstorm_crtv
│   │   │   │       ├── run_control
│   │   │   │       └── pipeline
│   │   │   ├── wf_playbooks
│   │   │   └── kns_ctx_vivo
│   │   ├── core_dev
│   │   └── core_arch_platform
├── log
│   ├── changelog
│   ├── validation
│   └── qms
├── .github
├── packages
├── ruleset
└── scripts
```

---

## OutputTemplate

```yaml
output_example:
  status: OK
  id_asset: baseline_v1_4_ascii_tree
  generated_by: ai
  created_at: 2025-08-16T00:00:00-03:00
  params:
    - source_visual: AINGZ_V5_Baselines_Unificados_v1_4_visual_plus_functions.md
  result:
    - tree: ascii_lines
  log:
    - step1: render
```


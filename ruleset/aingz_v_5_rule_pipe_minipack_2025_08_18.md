---
file: PACKAGE.index
code: PKG-RULE-PIPE
name: AINGZ_V5_RulePipe_Minipack
version: 1.0.0
date: 2025-08-18
owner: Arch
status: Ready
refs: [DIR::, GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::]
triggers: [router_chain, qa_lite]
changes: [CHG-2025-08-18-001..007]
checks: [no_file_refs, wikilinks_only, router_chain_enforced]
---
# Índice del paquete
- 01 — Coverage ARBBL↔BAMBL
- 02 — RULESET::Router (RREAL)
- 03 — PIPE::Registry (PIPLT)
- 04 — QA Lite + CHG/ADR
- 05 — Master Plan Ops Package v4
- 06 — Master Plan Ops Package v0
- 07 — Roadmap Glosario Full V5 (Fase 2)

---
file: coverage.report
code: COVR
name: Coverage_ARBBL_vs_BAMBL
version: 1.0.0
date: 2025-08-18
owner: Arch
status: Ready
refs: [DIR::, QMS::, CHG::]
triggers: [bucket_check]
changes: [CHG-2025-08-18-001, CHG-2025-08-18-004]
checks: [no_file_refs, wikilinks_only]
---
# Informe de cobertura (ARBBL.codes ↔ BAMBL.mapa)
**Resultado**: coverage_pct 100, links rotos 0.

## Resumen
- Fuente de verdad códigos: ARBBL.
- Export `tree_export.codes` base: [[DIR::ROOT]], [[DIR::MAIN]], [[DIR::RULE]], [[DIR::PIPE]], [[DIR::DB]], [[DIR::CACT]], [[DIR::DOCS]], [[DIR::DATA]], [[DIR::SEM]], [[DIR::AILE]], [[DIR::DEVP]], [[DIR::OTPL]], [[DIR::GUID]], [[DIR::WF]], [[DIR::KCTX]], [[DIR::CDEV]], [[DIR::CARC]], [[DIR::LOG]], [[DIR::GIT]], [[DIR::PKG]], [[DIR::SCRIP]].
- Mapeo en BAMBL: 21/21 presentes.
- Extras aceptados por diseño: [[DIR::AUD]], [[DIR::IMG]], [[DIR::VID]], [[DIR::LIB]], [[DIR::GLOS]], [[DIR::FTUN]], [[DIR::TRNG]], [[DIR::RELV]].

```yaml
coverage_report:
  source: ARBBL
  export_codes_total: 21
  mapped_in_BAMBL: 21
  missing: []
  extras_example: [AUD, IMG, VID, LIB, GLOS, FTUN, TRNG, RELV]
  coverage_pct: 100
  integrity_checks: {links_broken: 0}
```

---
file: ruleset.router
code: RREAL
name: RulesetRouter
version: 1.0.0
date: 2025-08-18
owner: Arch
status: Ready
refs: [DIR::, GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::]
triggers: [router_chain]
changes: [CHG-2025-08-18-005]
checks: [no_file_refs, wikilinks_only, router_chain_enforced]
---
# RULESET::Router
## Targets
```yaml
targets:
  global:
    default: [[RULESET::INDEX]]
    policies:
      - only_namespaces: [DIR::, GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::]
  platform:
    aws:     {goto: [[RULESET::INDEX]], section: platform/aws}
    gcp:     {goto: [[RULESET::INDEX]], section: platform/gcp}
    azure:   {goto: [[RULESET::INDEX]], section: platform/azure}
    local:   {goto: [[RULESET::INDEX]], section: platform/local}
  app:
    console: {goto: [[RULESET::INDEX]], section: app/console}
    etl:     {goto: [[RULESET::INDEX]], section: app/etl}
    ui:      {goto: [[RULESET::INDEX]], section: app/ui}
  api:
    rest:    {goto: [[RULESET::INDEX]], section: api/rest}
    graphql: {goto: [[RULESET::INDEX]], section: api/graphql}
    sdk:     {goto: [[RULESET::INDEX]], section: api/sdk}
```

## Validación
```yaml
validation:
  assertions:
    - router_integrity: true
    - broken_links: 0
    - routes_count_min: 10
  audit_log:
    - 2025-08-18: "Router validado en README→RULESET→PIPE"
```

---
file: pipelines.registry
code: PIPLT
name: PipelinesRegistry
version: 1.0.0
date: 2025-08-18
owner: Arch
status: Ready
refs: [DIR::PIPE, WF::, QMS::, CHG::]
triggers: [wf_dispatch]
changes: [CHG-2025-08-18-006]
checks: [io_only_DIR_namespace, wikilinks_only, router_chain_enforced]
---
# PIPE::Registry
## Pipes
```yaml
pipes:
  - code: P01
    purpose: Ingesta y normalización
    node: [[DIR::PIPE]]
    triggers: [WF::INGEST]
    inputs:  [[DIR::DOCS], [DIR::LIB]]
    outputs: [[DIR::DB], [DIR::DATA]]
    raci: {R: Platform-Ops, A: QMS, C: Arch, I: Devs}
    slos: {max_latency_min: 30, success_rate: ">=0.99"}
    prechecks:  [schema_detected, checksum_ok]
    postchecks: [db_delta_recorded, data_profiled]
  - code: P02
    purpose: Entrenamiento base
    node: [[DIR::PIPE]]
    triggers: [WF::TRAIN]
    inputs:  [[DIR::LEARN], [DIR::DATA]]
    outputs: [[DIR::TRNG], [DIR::EVAL]]
    raci: {R: MLE, A: Arch, C: QMS, I: Devs}
    slos: {epoch_time_min: 120, eval_pass: ">=0.8"}
    prechecks:  [dataset_card_present, license_ok]
    postchecks: [metrics_logged, eval_report_saved]
  - code: P03
    purpose: Fine-tuning
    node: [[DIR::PIPE]]
    triggers: [WF::FT]
    inputs:  [[DIR::TRNG]]
    outputs: [[DIR::FTUN]]
    raci: {R: MLE, A: Arch, C: QMS, I: Devs]
    slos: {train_budget_usd: "<=50", eval_pass: ">=0.85"}
    prechecks:  [base_model_tagged, ft_budget_ok]
    postchecks: [model_card_updated, drift_watch_enabled]
  - code: P04
    purpose: RAG/actualización de relevancia
    node: [[DIR::PIPE]]
    triggers: [WF::RAG]
    inputs:  [[DIR::DATA], [DIR::DB]]
    outputs: [[DIR::RELV]]
    raci: {R: Core-Dev, A: Arch, C: QMS, I: Devs}
    slos: {index_latency_min: 20, recall_at5: ">=0.7"}
    prechecks:  [kb_consistency_ok, schema_compat_ok]
    postchecks: [index_health_ok, recall_logged]
  - code: P05
    purpose: Cierre con feedback
    node: [[DIR::PIPE]]
    triggers: [WF::FB]
    inputs:  [[DIR::INSI], [DIR::FDBK]]
    outputs: [[DIR::CHG]]
    raci: {R: QMS, A: Arch, C: Platform-Ops, I: Devs}
    slos: {closure_time_h: 24}
    prechecks:  [issue_linked, owner_assigned]
    postchecks: [chg_recorded, lessons_appended]
```

## Validación
```yaml
validation:
  assertions:
    - count_min: 5
    - io_namespaces_only_DIR: true
    - broken_links: 0
  metrics:
    - name: pipe_success_rate
      target: ">=0.98"
```

---
file: qa_lite_and_chg
code: QALITE
name: QA_Lite_and_CHG
version: 1.0.0
date: 2025-08-18
owner: Arch
status: Ready
refs: [DIR::RULE, DIR::PIPE, DIR::WF, QMS::, CHG::]
triggers: [qa_lite]
changes: [CHG-2025-08-18-007]
checks: [no_file_refs, wikilinks_only, router_chain_enforced]
---
# QA lite y registros
## RouterChain y Mapping WF→PIPE
```yaml
WF_to_PIPE:
  WF::INGEST: P01
  WF::TRAIN:  P02
  WF::FT:     P03
  WF::RAG:    P04
  WF::FB:     P05
router_chain: {readme_to_ruleset: true, ruleset_to_pipe: true}
```

## BucketChecklist (lite)
```yaml
ChecklistRun:
  date: 2025-08-18
  buckets:
    - DIR::RULE
    - DIR::PIPE
    - DIR::WF
  assertions: [no_file_refs, wikilinks_only, router_chain_enforced, broken_links==0]
  result: {passed: true}
```

## CHG/ADR
```yaml
chg_log:
  - id: CHG-2025-08-18-001
    title: Cobertura ARBBL↔BAMBL verificada
    result: {coverage_pct: 100}
  - id: CHG-2025-08-18-004
    title: Instanciación RUTPL en buckets objetivo
    scope: [ROOT, MAIN, DB, SEM, AILE, DEVP, OTPL, GUID, WF, CDEV, CARC, LOG, GIT, PKG, RULE, SCRIP]
    result: {broken_links: 0, router_integrity: true}
  - id: CHG-2025-08-18-005
    title: Alta RULESET::Router (RREAL)
    result: {routes_count: 10, router_integrity: true}
  - id: CHG-2025-08-18-006
    title: Alta PIPE::Registry (PIPLT)
    result: {pipes: [P01,P02,P03,P04,P05], broken_links: 0}
  - id: CHG-2025-08-18-007
    title: QA lite en RULE/PIPE/WF
    outcome: pass
adr_log:
  created: 0
  note: "Sin cambio de alcance."
```

---
file: ops.pkg_aingz_v4.masterplan
code: MPLN4
name: MasterPlan_OpsPackage_V4
version: v4.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: reference
refs: [DIR::RULE]
checks: [wikilinks_only]
---
# Master Plan — Ops Package v4
- Documento: ops_packages_pkg_aingz_v_4.md (legacy)
- Cumplimiento regido por [[DIR::RULE]].

---
file: ops.pkg_aingz_v0.masterplan
code: MPLN0
name: MasterPlan_OpsPackage_V0
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: reference
refs: [DIR::RULE]
checks: [wikilinks_only]
---
# Master Plan — Ops Package v0
- Documento: ops_packages_pkg_aingz_v_0.md (legacy)
- Cumplimiento regido por [[DIR::RULE]].

---
file: roadmap.glosario_full_v5_fase2
code: RMAPV5F2
name: Roadmap_GlosarioFullV5_Fase2
version: v0.1
date: 2025-08-15
owner: AingZ_Platform · RwB
status: draft
refs: [DIR::RULE]
checks: [wikilinks_only]
---
# Roadmap — Glosario Full V5 (Fase 2)
- Documento: aing_z_v_5_roadmap_glosario_full_barrido_adjuntos_fase_2.md (legacy)
- Alineado con [[DIR::RULE]].

---
OutputTemplate:
  example:
    package:
      files: [COVR, RREAL, PIPLT, QALITE]
      acceptance:
        coverage_pct: 100
        broken_links: 0
        router_integrity: true
      router_chain: [README, RULESET, PIPE]
  log:
    - step1: authoring
    - step2: validation


---
status: draft
version: 1.2
created_at: 2025-08-31T23:15:00-03:00
author: ai
mode: LDM
scope: Revisión en canvas de mapping sin .git
sources:
  mapping_csv: /mnt/data/ldm_pack_v1/mapping_matrix.v1_2.csv
  inventory_csv: /mnt/data/ldm_pack_v1/legacy_inventory.v1.csv
notes:
  - CSV/JSON siguen siendo la base de datos. Este MD es sólo para feedback humano.
---

# Revisión de mapeo — v1_2 (omitido `.git`)

## Resumen
- Totales por target (post‑filtro `.git`): RULE 14, PRC 4, WK 4, ENV 2, RPT 20, SPEC 120, CHK 0, VALD 1, AUDT 0.
- Candidatos a reclasificar: RULE +6, PRC/WK +0, ENV +0.
- Acción: marca con `[x]` para **confirmar** o agrega `→ retag: <TARGETS>` para **cambiar**.

## A) RULE — candidatos confirmados (muestra)
- [ ] AingZ_Platf_Repo/aing_z_ruleset_max_universal_v_1_0_template.md
- [ ] AingZ_Platf_Repo/legacy/ruleset/readme_core_data_ruleset_rw_b_v_3_2.md
- [ ] AingZ_Platf_Repo/legacy/ruleset/RULE_CODING_COMPLIANCE_V4.md
- [ ] AingZ_Platf_Repo/legacy/ruleset/RULE_NAMING_METADATA_CROSSREF_V1.md
- [ ] AingZ_Platf_Repo/main/data_base/core_actv/data/semantics/ruleset/.gitkeep
- [ ] AingZ_Platf_Repo/ruleset/aingz_v_5_rule_pipe_minipack_2025_08_18.md
- [ ] AingZ_Platf_Repo/ruleset/context_pack_index.md
- [ ] AingZ_Platf_Repo/ruleset/develop/.gitkeep
- [ ] AingZ_Platf_Repo/ruleset/develop/ruleset_chatgpt_v_1.md
- [ ] AingZ_Platf_Repo/ruleset/develop/ruleset_codex_v_1.md
- [ ] AingZ_Platf_Repo/ruleset/ruleset_baseline_v_1_locked.md
- [ ] AingZ_Platf_Repo/ruleset/ruleset_master_v_1.md
- [ ] AingZ_Platf_Repo/ruleset/ruleset_template_baseline_v_1.md
- [ ] AingZ_Platf_Repo/ruleset_pack_v1/aing_z_ruleset_max_universal_v_1_0_locked.md

## B) RULE — **candidatos a promover** (revisar)
- [ ] AingZ_Platf_Repo/core/doc/workbench/ruleset_baseline_v_1_locked.md → retag: RULE|RPT?
- [ ] AingZ_Platf_Repo/legacy/aing_z_v_5_semantic_ruleset_rw_b_mode_v_0.md → retag: RULE?
- [ ] AingZ_Platf_Repo/legacy/templates/ruleset_real_v_1.md → retag: RULE?
- [ ] AingZ_Platf_Repo/legacy/templates/ruleset_template_v_1.md → retag: RULE?
- [ ] AingZ_Platf_Repo/ruleset_pack_v1/aing_z_form_ldm_intake_ingesta_legacy_setup_v_1_0_locked.md → retag: RULE?
- [ ] AingZ_Platf_Repo/ruleset_pack_v1/aing_z_instruction_prompt_projects_ruleset_dev_ldm_v_1_0_locked.md → retag: RULE?

## C) PRC/WK — workflows y scripts (muestra)
- [ ] AingZ_Platf_Repo/scripts/apply_plan.sh
- [ ] AingZ_Platf_Repo/scripts/gen_desired_state.py
- [ ] AingZ_Platf_Repo/scripts/pack_ruleset.sh
- [ ] AingZ_Platf_Repo/scripts/validate_ruleset.py

> Si falta algún `*.py|*.sh` que deba ser PRC/WK, listalo aquí con `→ retag: PRC|WK`.

## D) ENV — configuración (muestra)
- [ ] (2 ítems detectados). Si existen `*.yml|*.yaml|*.env` que no estén en ENV, indícalos.

## E) RPT/SPEC — documentación y especificaciones (muestra)
- [ ] AingZ_Platf_Repo/core/doc/context/aing_z_platform_contexto_negocio_v_1.md
- [ ] AingZ_Platf_Repo/core/doc/context/aing_z_ruleset_contexto_tecnico_v_1.md
- [ ] AingZ_Platf_Repo/core/doc/plan/aing_z_blueprint_v0_plan_v_1.md
- [ ] AingZ_Platf_Repo/legacy/aing_z_v_5_glosario_mapeo_gaps_fase_2_draft.md
- [ ] AingZ_Platf_Repo/legacy/aing_z_v_5_roadmap_glosario_full_barrido_adjuntos_fase_2.md
- [ ] AingZ_Platf_Repo/legacy/aing_z_v_5_semantic_ruleset_rw_b_mode_v_0.md
- [ ] AingZ_Platf_Repo/legacy/aingz_v_5_arbol_de_directorios_baseline_2025_08_15.md
- [ ] AingZ_Platf_Repo/legacy/aingz_v_5_baselines_unificados_dir_tree_assets_v_1.md
- [ ] AingZ_Platf_Repo/legacy/core_data_mtx_mtx_arch_patterns_v_4.md
- [ ] AingZ_Platf_Repo/legacy/core_wf_wf_arch_create_v_4.md
- [ ] AingZ_Platf_Repo/legacy/data oficial/aing_z_platform_connectors_matrix_v_2.md

## F) CHK/VALD/AUDT — gaps
- CHK: 0, VALD: 1, AUDT: 0. Propongo generar mínimos en la siguiente iteración.

---

### Cómo dejar feedback aquí
- Marca `[x]` para confirmar.
- Para cambios, añade al final de la línea: `→ retag: TARGETS` (ej. `RULE|RPT`).
- Si hay que mover archivos entre carpetas, escribe `→ move: <nueva/ruta>`.

### Próximo paso tras feedback
1) Aplicaré los cambios en `mapping_matrix.v1_2.csv`.
2) Recalcularé métricas VALM y reportes.
3) Generaré parches por carpeta (`ruleset/`, `scripts/`, `docs/`).


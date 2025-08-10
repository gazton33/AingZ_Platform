---
CODE: RPRT
ID: incoherencias_reporte_v4
VERSION: v4.0-2025-08-10
ROUTE: ops/reports/incoherencias.md
CROSSREF:
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---

# Reporte de Incoherencias — V4 (no-loss)

## Resumen

- Archivos MD analizados: **89**
- Incoherencias totales: **21**

### Por severidad

- CRITICO: **9**
- ALTO: **2**
- MEDIO: **9**
- BAJO: **1**

### Por tipo

- code_duplicate: **8**
- code_rule: **1**
- crossref_missing: **1**
- front_matter_incomplete: **1**
- front_matter_missing: **3**
- h1_duplicate: **1**
- id_duplicate: **1**
- outputtemplate_missing: **4**
- route_mismatch: **1**

## Detalle

- `/home/runner/work/AingZ_Platform/AingZ_Platform/library/intg/Corpus_Platform_V4.md` — **front_matter_missing** (CRITICO): Sin front-matter YAML al inicio
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops/log/harvest_readmes.md` — **front_matter_missing** (CRITICO): Sin front-matter YAML al inicio
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops/log/harvest_readmes.md` — **outputtemplate_missing** (CRITICO): Falta sección '## OutputTemplate'
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops/log/purge/purge_fixes_v2_2025-08-10T19:22:44Z.md` — **front_matter_incomplete** (ALTO): Faltan campos ['CODE', 'ID', 'VERSION', 'ROUTE', 'CROSSREF', 'AUTHOR', 'DATE']
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops/log/purge/purge_fixes_v2_2025-08-10T19:22:44Z.md` — **code_rule** (CRITICO): CODE inválido 'None' (<=5, SCREAMING_SNAKE)
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops/log/purge/purge_fixes_v2_2025-08-10T19:22:44Z.md` — **crossref_missing** (ALTO): CROSSREF ausente
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops/log/purge/purge_fixes_v2_2025-08-10T19:22:44Z.md` — **outputtemplate_missing** (CRITICO): Falta sección '## OutputTemplate'
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops/reports/incoherencias.md` — **route_mismatch** (CRITICO): ROUTE='ops/reports/incoherencias.md' no coincide con path real
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops/reports/incoherencias.md` — **outputtemplate_missing** (CRITICO): Falta sección '## OutputTemplate'
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops_ctx_ctx_package_v_4_closure.md` — **front_matter_missing** (CRITICO): Sin front-matter YAML al inicio
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops_ctx_ctx_package_v_4_closure.md` — **outputtemplate_missing** (CRITICO): Falta sección '## OutputTemplate'
- `/home/runner/work/AingZ_Platform/AingZ_Platform/core/data/dicts/rw_b_diccionario_code_triggers_v_2_20250729.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/triggers/rw_b_diccionario_code_triggers_v_2_20250729.md` — **id_duplicate** (MEDIO): Duplicado 'rw_b_diccionario_code_triggers_v_2_20250729_v4' en 2 archivos
- `/home/runner/work/AingZ_Platform/AingZ_Platform/README.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/readme_core_rw_b_v_3_2.md` — **code_duplicate** (MEDIO): Duplicado 'READM' en 2 archivos
- `/home/runner/work/AingZ_Platform/AingZ_Platform/core/data/dicts/readme_core_data_dicts_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/data/mplan/readme_core_data_mplan_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/data/mtx/readme_core_data_mtx_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/data/readme_core_data_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/data/rulset/readme_core_data_rulset_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/doc/audio/readme_core_doc_audio_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/doc/image/readme_core_doc_image_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/doc/onbrd/readme_core_doc_onbrd_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/doc/readme_core_doc_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/doc/video/readme_core_doc_video_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ai_learn/eval/readme_core_kns_ai_learn_eval_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ai_learn/feed/readme_core_kns_ai_learn_feed_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ai_learn/insi/readme_core_kns_ai_learn_insi_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ai_learn/learn/readme_core_kns_ai_learn_learn_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ai_learn/readme_core_kns_ai_learn_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ai_learn/rel/readme_core_kns_ai_learn_rel_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ai_learn/shot/readme_core_kns_ai_learn_shot_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ai_learn/trn/readme_core_kns_ai_learn_trn_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ai_learn/tune/readme_core_kns_ai_learn_tune_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/chkp/aingz_platform/readme_core_kns_chkp_aingz_platform_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/chkp/projects/readme_core_kns_chkp_projects_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/chkp/readme_core_kns_chkp_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ctx/aingz_platform/readme_core_kns_ctx_aingz_platform_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ctx/projects/readme_core_kns_ctx_projects_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ctx/readme_core_kns_ctx_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/glossary/readme_core_kns_glossary_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ideas_brainstorm/readme_core_kns_ideas_brainstorm_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/metrics/readme_core_kns_metrics_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/readme_core_kns_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/triggers/readme_core_kns_triggers_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/wf/readme_core_wf_rw_b_v_3_2.md` — **code_duplicate** (MEDIO): Duplicado 'CORE' en 31 archivos
- `/home/runner/work/AingZ_Platform/AingZ_Platform/core/data/dicts/rw_b_diccionario_code_triggers_v_2_20250729.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/data/template/readme_core_data_template_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/doc/template/readme_core_doc_template_rw_b_v_3_2.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/glossary/rw_b_glosario_code_v_2_20250729.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/triggers/rw_b_diccionario_code_triggers_v_2_20250729.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/rulset/RULE_CODING_COMPLIANCE_V4.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core_wf_intg_read_all_consolidate_v_4.md, /home/runner/work/AingZ_Platform/AingZ_Platform/informe_tareas_pendientes_v4.md, /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/temp/analisis_errors_agent_mode_config_v_4_20250807.md, /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/temp/informe_reforzar_readme_crossref_v_4_20250807.md, /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/temp/plan_agent_mode_scan_repo_v_4_20250807.md, /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/temp/reporte_coherencia_instrucciones_crossref_v_4_20250807.md, /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md, /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/BOOTSTRAP_V4_README.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/changelog.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/lessons_learned.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/log/diagnosis_baseline.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/templates/template_readme_rw_b_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/templates/template_readme_rw_b_v_4.md, /home/runner/work/AingZ_Platform/AingZ_Platform/packages/vds_core/templates/vds_core_templates_readme_v_3_1.md` — **code_duplicate** (MEDIO): Duplicado 'DOC' en 21 archivos
- `/home/runner/work/AingZ_Platform/AingZ_Platform/library/books/readme_library_books_rw_b_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/library/datasets/readme_library_datasets_rw_b_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/library/licencias/readme_library_licencias_rw_b_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/library/manuals/readme_library_manuals_rw_b_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/library/normas/readme_library_normas_rw_b_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/library/papers/readme_library_papers_rw_b_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/library/readme_library_rw_b_v_3_1.md` — **code_duplicate** (MEDIO): Duplicado 'LIBRA' en 7 archivos
- `/home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/bk_temp/lifecycle_bk_temp_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/legacy/lifecycle_legacy_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/lifecycle_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/mig/lifecycle_mig_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/temp/lifecycle_temp_readme_v_3_1.md` — **code_duplicate** (MEDIO): Duplicado 'LIFEC' en 5 archivos
- `/home/runner/work/AingZ_Platform/AingZ_Platform/ops/bootstrap_v_4_readme.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/log/ops_log_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/ops_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/pipelines/ops_pipelines_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/scripts/ops_scripts_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/ops/test/ops_test_readme_v_3_1.md` — **code_duplicate** (MEDIO): Duplicado 'OPS' en 6 archivos
- `/home/runner/work/AingZ_Platform/AingZ_Platform/packages/packages_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/packages/vds_core/onboarding/vds_core_onboarding_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/packages/vds_core/plugins/vds_core_plugins_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/packages/vds_core/tests/vds_core_tests_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/packages/vds_core/vds_core_readme_v_3_1.md` — **code_duplicate** (MEDIO): Duplicado 'PACKA' en 5 archivos
- `/home/runner/work/AingZ_Platform/AingZ_Platform/snapshots_ctx/codex/snapshots_ctx_codex_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/snapshots_ctx/common/snapshots_ctx_common_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/snapshots_ctx/gpt_4_1/snapshots_ctx_gpt_4_1_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/snapshots_ctx/gpt_4o/snapshots_ctx_gpt_4_o_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/snapshots_ctx/gpt_o3/snapshots_ctx_gpt_o_3_readme_v_3_1.md, /home/runner/work/AingZ_Platform/AingZ_Platform/snapshots_ctx/snapshots_ctx_readme_v_3_1.md` — **code_duplicate** (MEDIO): Duplicado 'SNAPS' en 6 archivos
- `/home/runner/work/AingZ_Platform/AingZ_Platform/core/data/dicts/rw_b_diccionario_code_triggers_v_2_20250729.md, /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/triggers/rw_b_diccionario_code_triggers_v_2_20250729.md` — **h1_duplicate** (BAJO): Duplicado '🚀 [RwB] DICCIONARIO CODE_TRIGGERS — v2 (2025‑07‑29)' en 2 archivos

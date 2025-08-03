# AingZ_Platform Repository Audit

## Directory Tree
```text
.
├── .editorconfig
├── .gitattributes
├── .github
│   └── workflows
│       └── validation.yml
├── .gitignore
├── LICENSE
├── README.md
├── SNAPSHOTS_CTX
│   ├── README.md
│   ├── ctx_connections_feedback_o3_o4_41_v1.md
│   ├── gpt4_1
│   │   └── README.md
│   ├── o3
│   │   └── README.md
│   └── o4
│       └── README.md
├── __pycache__
│   └── conftest.cpython-313-pytest-8.4.1.pyc
├── apps
│   └── README.md
├── bk_temp
│   ├── .gitignore
│   ├── README.md
│   ├── ai
│   │   ├── .gitignore
│   │   └── README.md
│   ├── ext
│   │   ├── .gitignore
│   │   └── README.md
│   └── int
│       ├── .gitignore
│       └── README.md
├── conftest.py
├── connectors
│   └── README.md
├── core
│   ├── README.md
│   ├── data
│   │   ├── README.md
│   │   ├── aing_z_platform_connectors_matrix_v_2.md
│   │   ├── blueprint_aingz_platform_v_1_20250731.md
│   │   ├── crossref_mapping_buckets_aingz_platform_v_1_20250731.md
│   │   ├── ctx_o_3_rw_b_total_20250731.md
│   │   ├── mplan
│   │   │   ├── README.md
│   │   │   └── o3_full_instructions.md
│   │   ├── mtx
│   │   │   ├── README.md
│   │   │   └── rw_b_assets_classification_matrix_v_1_20250729.md
│   │   ├── repo_monorepo_packages_blueprint_v1_20250731.md
│   │   ├── rulset
│   │   │   └── README.md
│   │   ├── system_prompt_aingz_models_o3_o4_41_v1.md
│   │   └── template
│   │       └── README.md
│   ├── doc
│   │   ├── README.md
│   │   ├── audio
│   │   │   └── README.md
│   │   ├── image
│   │   │   └── README.md
│   │   ├── library
│   │   │   └── README.md
│   │   ├── library_ext
│   │   │   └── README.md
│   │   ├── onbrd
│   │   │   └── README.md
│   │   ├── template
│   │   │   └── README.md
│   │   └── video
│   │       └── README.md
│   ├── kns
│   │   ├── README.md
│   │   ├── ai_learn
│   │   │   ├── README.md
│   │   │   ├── eval
│   │   │   │   └── README.md
│   │   │   ├── feed
│   │   │   │   └── README.md
│   │   │   ├── insi
│   │   │   │   └── insi_actv_kns_ctx_raw_v_1_20250725.md
│   │   │   ├── learn
│   │   │   │   ├── README.md
│   │   │   │   └── learn_actv_kns_ctx_raw_v_1_20250725.md
│   │   │   ├── rel
│   │   │   │   └── README.md
│   │   │   ├── shot
│   │   │   │   └── README.md
│   │   │   ├── trn
│   │   │   │   ├── README.md
│   │   │   │   └── trnlog_actv_kns_ctx_raw_v_1_20250725.md
│   │   │   └── tune
│   │   │       └── README.md
│   │   ├── chkp
│   │   │   ├── README.md
│   │   │   ├── aingz_platform
│   │   │   │   └── README.md
│   │   │   ├── projects
│   │   │   │   └── README.md
│   │   │   └── rw_b_kns_chkp_legacy_v_0.md
│   │   ├── ctx
│   │   │   ├── README.md
│   │   │   ├── aingz_platform
│   │   │   │   └── README.md
│   │   │   ├── kns_ctx_legacy_migracion_final_20250725.md
│   │   │   ├── projects
│   │   │   │   └── README.md
│   │   │   ├── rw_b_kns_ctx_v_0_lswp.md
│   │   │   ├── rw_b_kns_ctx_v_1_20250724.md
│   │   │   └── snaphots_ai
│   │   │       └── README.md
│   │   ├── glossary
│   │   │   ├── rw_b_glosario_code_v_2_20250729.md
│   │   │   ├── rw_b_glossary_rdm_v_0.md
│   │   │   └── rw_b_naming_convention.md
│   │   ├── ideas_brainstorm
│   │   │   ├── brain_actv_kns_ctx_raw_v_1_20250725.md
│   │   │   └── idea_actv_kns_ctx_raw_v_1_20250725.md
│   │   └── metrics
│   │       └── kpis_consolidacion.md
│   ├── log
│   │   ├── README.md
│   │   ├── bitacoras
│   │   │   └── README.md
│   │   ├── changelog
│   │   │   ├── README.md
│   │   │   └── chglog_actv_kns_ctx_raw_v_1_20250725.md
│   │   └── trazabilidad_total
│   │       └── README.md
│   ├── onbrd_welcome_onboarding_gz_rw_b_v_20250725.md
│   ├── rw_b_diccionario_code_triggers_v_2_20250729.md
│   ├── scr
│   │   └── README.md
│   └── wf
│       ├── README.md
│       ├── audt
│       │   └── README.md
│       ├── chg_log_wf_purgatorio_20250725.md
│       ├── mig_cons
│       │   └── README.md
│       ├── relv
│       │   └── README.md
│       ├── rw_b_wf_auditoria_cierre_hilo_actv_v_1_20250725.md
│       ├── rw_b_wf_auditoria_legacy_v_3_20250725.md
│       ├── rw_b_wf_dictado_v_1.md
│       ├── rw_b_wf_inicio_repo_check_v_1_20250731.md
│       ├── rw_b_wf_relev_hilo_assets_v_1_20250729.md
│       ├── rw_b_wf_relevamiento_ideas_actv_v_1_20250725.md
│       ├── tareas_acciones
│       │   └── README.md
│       ├── wf_cons_actv_transcripcion_raw_v_4_20250730_draft.md
│       ├── wf_migracion_final_legacy_rw_b_v_1_20250725.md
│       └── wk_feedtrn_eval_actv_raw_v_2_20250725.md
├── infra
│   ├── README.md
│   ├── git
│   │   └── README.md
│   ├── pipelines
│   │   └── README.md
│   ├── scr
│   │   └── README.md
│   ├── template
│   │   ├── naming
│   │   │   ├── rw_b_naming_ruleset_v_2_20250727.md
│   │   │   └── rw_b_naming_template_v_1.md
│   │   └── rdm_template
│   │       ├── rw_b_readme_ai_template_v_0.md
│   │       ├── rw_b_readme_human_template_v_0.md
│   │       └── rw_b_readme_template_rdm_v_0.md
│   └── test
│       ├── README.md
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-313.pyc
│       │   ├── test_class_scan.cpython-313-pytest-8.4.1.pyc
│       │   └── test_mapping.cpython-313-pytest-8.4.1.pyc
│       ├── test_class_scan.py
│       └── test_mapping.py
├── legacy
│   ├── README.md
│   ├── data
│   │   ├── README.md
│   │   ├── mplan
│   │   │   └── README.md
│   │   ├── mtx
│   │   │   └── README.md
│   │   ├── rulset
│   │   │   └── README.md
│   │   └── template
│   │       └── README.md
│   ├── doc
│   │   ├── README.md
│   │   ├── audio
│   │   │   └── README.md
│   │   ├── image
│   │   │   └── README.md
│   │   ├── library
│   │   │   └── README.md
│   │   ├── library_ext
│   │   │   └── README.md
│   │   ├── onbrd
│   │   │   └── README.md
│   │   ├── template
│   │   │   └── README.md
│   │   └── video
│   │       └── README.md
│   ├── kns
│   │   ├── README.md
│   │   ├── ai_learn
│   │   │   ├── README.md
│   │   │   ├── eval
│   │   │   │   └── README.md
│   │   │   ├── feed
│   │   │   │   └── README.md
│   │   │   ├── learn
│   │   │   │   └── README.md
│   │   │   ├── rel
│   │   │   │   └── README.md
│   │   │   ├── shot
│   │   │   │   └── README.md
│   │   │   ├── trn
│   │   │   │   └── README.md
│   │   │   └── tune
│   │   │       └── README.md
│   │   ├── chkp
│   │   │   ├── README.md
│   │   │   ├── aingz_platform
│   │   │   │   └── README.md
│   │   │   └── projects
│   │   │       └── README.md
│   │   └── ctx
│   │       ├── README.md
│   │       ├── aingz_platform
│   │       │   └── README.md
│   │       ├── projects
│   │       │   └── README.md
│   │       └── snaphots_ai
│   │           └── README.md
│   ├── log
│   │   ├── README.md
│   │   ├── bitacoras
│   │   │   └── README.md
│   │   ├── changelog
│   │   │   └── README.md
│   │   └── trazabilidad_total
│   │       └── README.md
│   ├── scr
│   │   └── README.md
│   └── wf
│       ├── README.md
│       ├── audt
│       │   └── README.md
│       ├── mig_cons
│       │   └── README.md
│       ├── relv
│       │   └── README.md
│       └── tareas_acciones
│           └── README.md
├── legacy_old
│   ├── lote_1
│   │   ├── README.md
│   │   ├── audit
│   │   │   ├── Lote_1_1
│   │   │   │   ├── faq_workflows_operativo_v_1_lote_1_20250724.md
│   │   │   │   ├── jerarquia_precedencia_instrucciones_v_1_lote_1_20250724.md
│   │   │   │   ├── matriz_features_prompts_v_1_lote_1_20250724.md
│   │   │   │   ├── readme_onbrd_v_1_lote_1_20250724.md
│   │   │   │   ├── rw_b_audt_mtxfaq_adjuntos_legacy_v_1_2_20250724.md
│   │   │   │   ├── rw_b_audt_mtxfeat_prompts_legacy_v_1_2_20250724.md
│   │   │   │   ├── rw_b_audt_mtxinstr_legacy_v_1_2_20250724.md
│   │   │   │   ├── rw_b_audt_mtxjerarq_instr_legacy_v_1_2_20250724.md
│   │   │   │   ├── rw_b_audt_onbrd_aingz_legacy_v_1_2_20250724.md
│   │   │   │   ├── rw_b_plan_consolidacion_lote_1_v_1_20250724.md
│   │   │   │   └── rw_b_review_consolidacion_auditoria_lote_1_v_1_20250724.md
│   │   │   └── Lote_1_2
│   │   │       ├── auditoria_aing_z_repo_legacy_barrido_raw_v_1_20250725.md
│   │   │       ├── auditoria_aing_z_repo_raw_gold_scaffold_v_1_20250725.md
│   │   │       ├── auditoria_lote_2_readme_v_1_20250725.md
│   │   │       ├── auditoria_rawgold_scaffold_readme_v_1_20250725.md
│   │   │       ├── auditoria_readme_base_aingz_t_3_infra_v_1_20250725.md
│   │   │       ├── auditoria_readme_integracion_t_2_memorias_historiales_v_1_20250725.md
│   │   │       ├── auditoria_readme_master_plan_v_1_20250725.md
│   │   │       ├── auditoria_readme_matriz_memorias_historiales_v_1_20250725.md
│   │   │       ├── auditoria_readme_raiz_lote_2_v_1_20250725.md
│   │   │       ├── auditoria_t_3_raw_gold_canvas_integrado_final_v_2_v_1_20250725.md
│   │   │       ├── auditoria_t_3_raw_gold_matriz_final_v_1_20250725.md
│   │   │       ├── mapeo_consolidado_lote_2_v_1_20250725.md
│   │   │       └── revision_cruzada_auditorias_lote_2_v_1_20250725.md
│   │   └── originals
│   │       ├── Lote_1_1
│   │       │   ├── Legacy_MTX_features_prompts.md
│   │       │   ├── Legacy_MTX_instrucciones.md
│   │       │   ├── Legacy_MTX_jerarquia_instrucciones.md
│   │       │   ├── Legacy_MTXfaq_avanzada_gestion_de_adjuntos.md
│   │       │   ├── Legacy_onboarding_gz.md
│   │       │   └── README.md
│   │       └── Lote_1_2
│   │           ├── README.md
│   │           ├── aing_z_repo_legacy_barrido_raw.md
│   │           ├── aing_z_repo_raw_gold_scaffold.md
│   │           ├── faq_workflows_operativo_v_1_lote_1_20250724.md
│   │           ├── jerarquia_precedencia_instrucciones_v_1_lote_1_20250724.md
│   │           ├── matriz_features_prompts_v_1_lote_1_20250724.md
│   │           ├── rawgold_scaffold_readme.md
│   │           ├── readme_base_aingz_t_3_infra.md
│   │           ├── readme_integracion_t_2_memorias_historiales.md
│   │           ├── readme_master_plan.md
│   │           ├── readme_matriz_memorias_historiales.md
│   │           ├── readme_onbrd_v_1_lote_1_20250724.md
│   │           ├── t_3_raw_gold_canvas_integrado_final_v_2.md
│   │           └── t_3_raw_gold_matriz_final.md
│   ├── lote_2
│   │   ├── README.md
│   │   ├── audit
│   │   │   ├── KNS
│   │   │   │   ├── rw_b_audt_kns_gz_project_insights_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_kns_matriz_precedencia_templates_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_kns_memorias_feedback_reglas_oro_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_kns_readme_knowledge_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_kns_t_3_raw_gold_matriz_final_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_matriz_extendida_features_chatgpt_workflow_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_matriz_raw_features_chatgpt_workflow_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_profundizacion_matriz_precedencia_features_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_readme_explicativo_matriz_features_lote_2_20250725.md
│   │   │   │   ├── rw_b_mapeo_global_kns_lote_2_20250725.md
│   │   │   │   └── rw_b_resumen_auditoria_kns_matrices_lote_2_20250725.md
│   │   │   ├── Tmpl
│   │   │   │   ├── rw_b_audt_template_casos_uso_precedencia_infra_full_custom_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_template_prompt_custom_gpt_lote_2_20250725.md
│   │   │   │   └── rw_b_resumen_auditoria_templates_lote_2_20250725.md
│   │   │   ├── WF
│   │   │   │   ├── rw_b_audt_macro_plan_migracion_v_2_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_readme_workflows_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_workflow_gpt_raw_v_1_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_workflow_gpt_raw_v_1_v_1_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_workflow_gz_project_template_lote_2_20250725.md
│   │   │   │   └── rw_b_resumen_auditoria_wf_lote_2_20250725.md
│   │   │   ├── mtx
│   │   │   │   ├── rw_b_audt_checklist_testing_memorias_historiales_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_control_cruce_matriz_raw_vs_extendida_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_control_trazabilidad_fuentes_chatgpt_workflow_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_ejemplo_integracion_memoria_feedback_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_leccion_aprendida_upgrade_memorias_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_matrices_readme_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_matriz_memorias_historiales_chatgpt_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_matriz_precedencia_instrucciones_full_custom_infraestructura_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_plantilla_snapshot_memoria_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_rw_b_matriz_triggers_contexto_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_t_2_2_raw_gold_matriz_historiales_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_t_3_raw_gold_matriz_final_lote_2_20250725.md
│   │   │   │   ├── rw_b_mapeo_global_matrices_legacy_lote_2_completo_20250725.md
│   │   │   │   └── rw_b_resumen_auditoria_matrices_legacy_lote_2_20250725.md
│   │   │   └── rw_b_barrido_global_auditorias_sesion_lote_2_20250725.md
│   │   └── originals
│   │       ├── Lote_knowledge
│   │       │   ├── knowledge_base_aingz_t_3.md
│   │       │   ├── knowledge_base_matriz_precedencia_templates_universales_raw.md
│   │       │   ├── knowledge_gz_project_insights.md
│   │       │   ├── knowledge_memorias_feedback_reglas_oro.md
│   │       │   ├── mtx
│   │       │   │   ├── matriz_extendida_features_chatgpt_workflow.md
│   │       │   │   ├── matriz_raw_features_chatgpt_workflow.md
│   │       │   │   ├── profundizacion_matriz_precedencia_instrucciones_y_features_aing_z_repo.md
│   │       │   │   └── readme_explicativo_matriz_features.md
│   │       │   ├── readme_knowledge.md
│   │       │   └── t_3_raw_gold_matriz_final.md
│   │       ├── Lote_matrices
│   │       │   ├── checklist_testing_memorias_historiales.md
│   │       │   ├── control_cruce_matriz_raw_vs_extendida.md
│   │       │   ├── control_trazabilidad_fuentes_chatgpt_workflow.md
│   │       │   ├── ejemplo_integracion_memoria_feedback.md
│   │       │   ├── leccion_aprendida_upgrade_memorias.md
│   │       │   ├── matrices_readme.md
│   │       │   ├── matriz_memorias_historiales_chatgpt.md
│   │       │   ├── matriz_precedencia_instrucciones_full_custom_infraestructura.md
│   │       │   ├── plantilla_snapshot_memoria.md
│   │       │   ├── rw_b_matriz_triggers_contexto.md
│   │       │   ├── t_2_2_raw_gold_matriz_historiales.md
│   │       │   └── t_3_raw_gold_matriz_final.md
│   │       ├── Lote_templates
│   │       │   ├── plantilla_prompt_custom_gpt.md
│   │       │   └── templates_casos_uso_precedencia_infraestructura_full_custom.md
│   │       ├── Lote_workflows
│   │       │   ├── readme_workflows.md
│   │       │   ├── rw_b_macro_plan_migracion_v_2.md
│   │       │   ├── workflow_gpt_raw.md
│   │       │   ├── workflow_gpt_raw_v_1.md
│   │       │   └── workflow_gz_project_template.md
│   │       └── README.md
│   ├── lote_3
│   │   ├── README.md
│   │   ├── audit
│   │   │   ├── Gem_Dig
│   │   │   │   ├── rw_b_audt_cv_gaston_2020_20250725.md
│   │   │   │   ├── rw_b_audt_dr_gz_web_1_perfil_publico_20250725.md
│   │   │   │   ├── rw_b_audt_gem_dig_gz_gpt_raw_20250725.md
│   │   │   │   ├── rw_b_audt_gem_dig_gz_gpt_raw_v_1_20250725.md
│   │   │   │   ├── rw_b_audt_json_gemelo_digital_bloques_1_2_20250725.md
│   │   │   │   ├── rw_b_audt_json_gemelo_digital_bloques_3_4_20250725.md
│   │   │   │   ├── rw_b_audt_json_gemelo_digital_bloques_5_6_20250725.md
│   │   │   │   ├── rw_b_audt_json_gemelo_digital_bloques_7_8_20250725.md
│   │   │   │   ├── rw_b_mapeo_global_auditoria_gemelo_digital_gz_20250725.md
│   │   │   │   ├── rw_b_mapeo_global_jsons_gemelo_digital_gz_20250725.md
│   │   │   │   └── rw_b_resumen_mapping_gemelo_digital_gz_lote_2_20250725.md
│   │   │   ├── Inventarios
│   │   │   │   ├── rw_b_audt_bike_electrical_knowledge_v_2_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_ficha_tec_gz_n_56_vz_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_gz_e_bike_knowledge_v_1_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_gz_e_bike_knowledge_v_2_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_inventario_prompt_template_raw_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_reporte_hw_gz_n_56_vz_lote_2_20250725.md
│   │   │   │   ├── rw_b_audt_script_hw_info_gz_n_56_vz_lote_2_20250725.md
│   │   │   │   ├── rw_b_mapeo_global_auditoria_inventario_gz_lote_2_20250725.md
│   │   │   │   └── rw_b_resumen_mapping_inventario_gz_lote_2_20250725.md
│   │   │   └── rw_b_ctx_gemelo_digital_inventario_20250725.md
│   │   └── originals
│   │       ├── Lote_Gem_Digitales
│   │       │   ├── Bloque 1.json
│   │       │   ├── Bloque 2.json
│   │       │   ├── Bloque 3.json
│   │       │   ├── Bloque 4.json
│   │       │   ├── Bloque 5.json
│   │       │   ├── Bloque 6.json
│   │       │   ├── Bloque 7.json
│   │       │   ├── Bloque 8.json
│   │       │   ├── Cv Gaston 2020.doc
│   │       │   ├── DR GZ Web 1.pdf
│   │       │   ├── gem_dig_gz_gpt_raw.md
│   │       │   └── gem_dig_gz_gpt_raw_v_1.md
│   │       └── Lote_Inventario
│   │           ├── bike_electrical_knowledge_v_2.md
│   │           ├── gz_e_bike_knowledge v2.md
│   │           ├── gz_e_bike_knowledge.md
│   │           ├── gz_n_56_vz_tech.md
│   │           ├── inventario_tecnico_prompt_y_template_raw.md
│   │           ├── reporte_hw_gz_n56vz_2025-07-15_19-51.csv
│   │           └── reporte_hw_gz_n56vz_2025-07-15_19-51.md
│   └── lote_4
│       ├── README.md
│       └── originals
│           ├── Lote_Gem_Digitales
│           │   ├── Bloque 1.json
│           │   ├── Bloque 2.json
│           │   ├── Bloque 3.json
│           │   ├── Bloque 4.json
│           │   ├── Bloque 5.json
│           │   ├── Bloque 6.json
│           │   ├── Bloque 7.json
│           │   ├── Bloque 8.json
│           │   ├── Cv Gaston 2020.doc
│           │   ├── DR GZ Web 1.pdf
│           │   ├── gem_dig_gz_gpt_raw.md
│           │   └── gem_dig_gz_gpt_raw_v_1.md
│           ├── Lote_Inventario
│           │   ├── bike_electrical_knowledge_v_2.md
│           │   ├── gz_e_bike_knowledge v2.md
│           │   ├── gz_e_bike_knowledge.md
│           │   ├── gz_n_56_vz_tech.md
│           │   ├── inventario_tecnico_prompt_y_template_raw.md
│           │   ├── reporte_hw_gz_n56vz_2025-07-15_19-51.csv
│           │   └── reporte_hw_gz_n56vz_2025-07-15_19-51.md
│           └── bliblioteca_refencia
│               ├── 02_capacidades_y_limitaciones_agent_mode.md
│               ├── Análisis del repositorio.pdf
│               ├── matriz_limites_contexto_chatgpt_v_1.md
│               └── openai
│                   ├── Docs_OpenAi
│                   │   ├── 1.Get_Started.md
│                   │   ├── 10.Best_Practices.md
│                   │   ├── 11.Assistants_Api.md
│                   │   ├── 12.0.Resources.md
│                   │   ├── 12.1.ChatGPT_Actions.md
│                   │   ├── 2.Core_Concepts.md
│                   │   ├── 3.Api_Guides.md
│                   │   ├── 4.Tools.md
│                   │   ├── 5.Agents.md
│                   │   ├── 6.Realtime_Api.md
│                   │   ├── 7.Model_Optimization.md
│                   │   ├── 8.Specialized_Models.md
│                   │   └── 9.Codex.md
│                   └── Help_OpenAi
│                       ├── Buildings_GPTs.md
│                       ├── ChatGPT.md
│                       ├── GPTs.md
│                       └── Sharing_GPTs.md
├── log
│   ├── README.md
│   ├── bitacoras
│   │   └── README.md
│   ├── changelog
│   │   └── README.md
│   ├── chglog_main_rwb_v_5_20250730_actv.md
│   └── trazabilidad_total
│       └── README.md
├── mig
│   ├── README.md
│   ├── data
│   │   ├── README.md
│   │   ├── mplan
│   │   │   └── README.md
│   │   ├── mtx
│   │   │   └── README.md
│   │   ├── rulset
│   │   │   └── README.md
│   │   └── template
│   │       └── README.md
│   ├── doc
│   │   ├── README.md
│   │   ├── audio
│   │   │   └── README.md
│   │   ├── image
│   │   │   └── README.md
│   │   ├── library
│   │   │   └── README.md
│   │   ├── library_ext
│   │   │   └── README.md
│   │   ├── onbrd
│   │   │   └── README.md
│   │   ├── template
│   │   │   └── README.md
│   │   └── video
│   │       └── README.md
│   ├── kns
│   │   ├── README.md
│   │   ├── ai_learn
│   │   │   ├── README.md
│   │   │   ├── eval
│   │   │   │   └── README.md
│   │   │   ├── feed
│   │   │   │   └── README.md
│   │   │   ├── learn
│   │   │   │   └── README.md
│   │   │   ├── rel
│   │   │   │   └── README.md
│   │   │   ├── shot
│   │   │   │   └── README.md
│   │   │   ├── trn
│   │   │   │   └── README.md
│   │   │   └── tune
│   │   │       └── README.md
│   │   ├── chkp
│   │   │   ├── README.md
│   │   │   ├── aingz_platform
│   │   │   │   └── README.md
│   │   │   └── projects
│   │   │       └── README.md
│   │   └── ctx
│   │       ├── README.md
│   │       ├── aingz_platform
│   │       │   └── README.md
│   │       ├── projects
│   │       │   └── README.md
│   │       └── snaphots_ai
│   │           └── README.md
│   ├── log
│   │   ├── README.md
│   │   ├── bitacoras
│   │   │   └── README.md
│   │   ├── changelog
│   │   │   └── README.md
│   │   └── trazabilidad_total
│   │       └── README.md
│   ├── scr
│   │   └── README.md
│   └── wf
│       ├── README.md
│       ├── audt
│       │   └── README.md
│       ├── mig_cons
│       │   └── README.md
│       ├── relv
│       │   └── README.md
│       └── tareas_acciones
│           └── README.md
├── packages
│   └── README.md
├── requirements.txt
├── scripts
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   ├── class_scan.cpython-313.pyc
│   │   └── mapping.cpython-313.pyc
│   ├── audit_naming.py
│   ├── check_glossary_refs.py
│   ├── class_scan.py
│   ├── mapping.py
│   ├── normalize_readmes.py
│   ├── report_kpis.py
│   └── update_readme_refs.py
└── tmp_staging
    ├── README.md
    ├── data
    │   ├── README.md
    │   ├── arch_research_core_rw_b_v_1.md
    │   ├── barrido_literal_ctx_vivo_y_feedback_aprendizaje.md
    │   ├── barrido_literal_redefinicion_legacy.md
    │   ├── dir_arch_plan_v_5_integracion_matrix.md
    │   ├── directorio_activos_desarrollo_staging.md
    │   ├── idea_brainstorm_limites_ctx_tokens_md.md
    │   ├── kns_ctx_o_3_41_analisis_integracion.md
    │   ├── mplan
    │   │   └── README.md
    │   ├── mpln_master_plan_aingz_rw_b_v_20250730_v_4_activo.md
    │   ├── mtx
    │   │   └── README.md
    │   ├── politica_cierre_eliminacion_purgatorio.md
    │   ├── readme_legacy_core_rw_b.md
    │   ├── registro_ctx_modelos_naming_optimizacion.md
    │   ├── registro_trazabilidad_total.md
    │   ├── rulset
    │   │   └── README.md
    │   ├── rw_b_checklist_avances_v_1_20250730.md
    │   ├── rw_b_dir_arch_plan_v_4_20250729.md
    │   └── template
    │       └── README.md
    ├── doc
    │   ├── README.md
    │   ├── audio
    │   │   └── README.md
    │   ├── image
    │   │   └── README.md
    │   ├── library
    │   │   └── README.md
    │   ├── library_ext
    │   │   └── README.md
    │   ├── onbrd
    │   │   └── README.md
    │   ├── template
    │   │   └── README.md
    │   └── video
    │       └── README.md
    ├── kns
    │   ├── README.md
    │   ├── ai_learn
    │   │   ├── README.md
    │   │   ├── eval
    │   │   │   └── README.md
    │   │   ├── feed
    │   │   │   └── README.md
    │   │   ├── learn
    │   │   │   └── README.md
    │   │   ├── rel
    │   │   │   └── README.md
    │   │   ├── shot
    │   │   │   └── README.md
    │   │   ├── trn
    │   │   │   └── README.md
    │   │   └── tune
    │   │       └── README.md
    │   ├── chkp
    │   │   ├── README.md
    │   │   ├── aingz_platform
    │   │   │   └── README.md
    │   │   └── projects
    │   │       └── README.md
    │   └── ctx
    │       ├── README.md
    │       ├── aingz_platform
    │       │   └── README.md
    │       ├── projects
    │       │   └── README.md
    │       └── snaphots_ai
    │           └── README.md
    ├── log
    │   ├── README.md
    │   ├── bitacoras
    │   │   └── README.md
    │   ├── changelog
    │   │   └── README.md
    │   └── trazabilidad_total
    │       └── README.md
    ├── scr
    │   └── README.md
    └── wf
        ├── README.md
        ├── audt
        │   └── README.md
        ├── mig_cons
        │   └── README.md
        ├── relv
        │   └── README.md
        └── tareas_acciones
            └── README.md

229 directories, 457 files
```

## File Listing
```text
./bk_temp/ai/.gitignore
./bk_temp/ai/README.md
./bk_temp/.gitignore
./bk_temp/README.md
./bk_temp/ext/.gitignore
./bk_temp/ext/README.md
./bk_temp/int/.gitignore
./bk_temp/int/README.md
./scripts/mapping.py
./scripts/__init__.py
./scripts/__pycache__/class_scan.cpython-313.pyc
./scripts/__pycache__/__init__.cpython-313.pyc
./scripts/__pycache__/mapping.cpython-313.pyc
./scripts/update_readme_refs.py
./scripts/class_scan.py
./scripts/check_glossary_refs.py
./scripts/audit_naming.py
./scripts/report_kpis.py
./scripts/normalize_readmes.py
./conftest.py
./__pycache__/conftest.cpython-313-pytest-8.4.1.pyc
./legacy/scr/README.md
./legacy/doc/library/README.md
./legacy/doc/image/README.md
./legacy/doc/onbrd/README.md
./legacy/doc/video/README.md
./legacy/doc/library_ext/README.md
./legacy/doc/template/README.md
./legacy/doc/README.md
./legacy/doc/audio/README.md
./legacy/log/changelog/README.md
./legacy/log/trazabilidad_total/README.md
./legacy/log/README.md
./legacy/log/bitacoras/README.md
./legacy/data/mplan/README.md
./legacy/data/mtx/README.md
./legacy/data/template/README.md
./legacy/data/README.md
./legacy/data/rulset/README.md
./legacy/kns/ai_learn/shot/README.md
./legacy/kns/ai_learn/tune/README.md
./legacy/kns/ai_learn/learn/README.md
./legacy/kns/ai_learn/trn/README.md
./legacy/kns/ai_learn/eval/README.md
./legacy/kns/ai_learn/README.md
./legacy/kns/ai_learn/rel/README.md
./legacy/kns/ai_learn/feed/README.md
./legacy/kns/chkp/projects/README.md
./legacy/kns/chkp/README.md
./legacy/kns/chkp/aingz_platform/README.md
./legacy/kns/ctx/snaphots_ai/README.md
./legacy/kns/ctx/projects/README.md
./legacy/kns/ctx/README.md
./legacy/kns/ctx/aingz_platform/README.md
./legacy/kns/README.md
./legacy/wf/audt/README.md
./legacy/wf/mig_cons/README.md
./legacy/wf/tareas_acciones/README.md
./legacy/wf/relv/README.md
./legacy/wf/README.md
./legacy/README.md
./.gitattributes
./log/changelog/README.md
./log/trazabilidad_total/README.md
./log/chglog_main_rwb_v_5_20250730_actv.md
./log/README.md
./log/bitacoras/README.md
./tmp_staging/scr/README.md
./tmp_staging/doc/library/README.md
./tmp_staging/doc/image/README.md
./tmp_staging/doc/onbrd/README.md
./tmp_staging/doc/video/README.md
./tmp_staging/doc/library_ext/README.md
./tmp_staging/doc/template/README.md
./tmp_staging/doc/README.md
./tmp_staging/doc/audio/README.md
./tmp_staging/log/changelog/README.md
./tmp_staging/log/trazabilidad_total/README.md
./tmp_staging/log/README.md
./tmp_staging/log/bitacoras/README.md
./tmp_staging/data/directorio_activos_desarrollo_staging.md
./tmp_staging/data/readme_legacy_core_rw_b.md
./tmp_staging/data/mplan/README.md
./tmp_staging/data/mpln_master_plan_aingz_rw_b_v_20250730_v_4_activo.md
./tmp_staging/data/kns_ctx_o_3_41_analisis_integracion.md
./tmp_staging/data/mtx/README.md
./tmp_staging/data/rw_b_dir_arch_plan_v_4_20250729.md
./tmp_staging/data/barrido_literal_redefinicion_legacy.md
./tmp_staging/data/registro_ctx_modelos_naming_optimizacion.md
./tmp_staging/data/registro_trazabilidad_total.md
./tmp_staging/data/idea_brainstorm_limites_ctx_tokens_md.md
./tmp_staging/data/politica_cierre_eliminacion_purgatorio.md
./tmp_staging/data/rw_b_checklist_avances_v_1_20250730.md
./tmp_staging/data/template/README.md
./tmp_staging/data/barrido_literal_ctx_vivo_y_feedback_aprendizaje.md
./tmp_staging/data/README.md
./tmp_staging/data/dir_arch_plan_v_5_integracion_matrix.md
./tmp_staging/data/rulset/README.md
./tmp_staging/data/arch_research_core_rw_b_v_1.md
./tmp_staging/kns/ai_learn/shot/README.md
./tmp_staging/kns/ai_learn/tune/README.md
./tmp_staging/kns/ai_learn/learn/README.md
./tmp_staging/kns/ai_learn/trn/README.md
./tmp_staging/kns/ai_learn/eval/README.md
./tmp_staging/kns/ai_learn/README.md
./tmp_staging/kns/ai_learn/rel/README.md
./tmp_staging/kns/ai_learn/feed/README.md
./tmp_staging/kns/chkp/projects/README.md
./tmp_staging/kns/chkp/README.md
./tmp_staging/kns/chkp/aingz_platform/README.md
./tmp_staging/kns/ctx/snaphots_ai/README.md
./tmp_staging/kns/ctx/projects/README.md
./tmp_staging/kns/ctx/README.md
./tmp_staging/kns/ctx/aingz_platform/README.md
./tmp_staging/kns/README.md
./tmp_staging/wf/audt/README.md
./tmp_staging/wf/mig_cons/README.md
./tmp_staging/wf/tareas_acciones/README.md
./tmp_staging/wf/relv/README.md
./tmp_staging/wf/README.md
./tmp_staging/README.md
./infra/scr/README.md
./infra/pipelines/README.md
./infra/test/__init__.py
./infra/test/__pycache__/test_class_scan.cpython-313-pytest-8.4.1.pyc
./infra/test/__pycache__/__init__.cpython-313.pyc
./infra/test/__pycache__/test_mapping.cpython-313-pytest-8.4.1.pyc
./infra/test/test_class_scan.py
./infra/test/test_mapping.py
./infra/test/README.md
./infra/template/rdm_template/rw_b_readme_ai_template_v_0.md
./infra/template/rdm_template/rw_b_readme_template_rdm_v_0.md
./infra/template/rdm_template/rw_b_readme_human_template_v_0.md
./infra/template/naming/rw_b_naming_template_v_1.md
./infra/template/naming/rw_b_naming_ruleset_v_2_20250727.md
./infra/README.md
./infra/git/README.md
./LICENSE
./apps/README.md
./packages/README.md
./mig/scr/README.md
./mig/doc/library/README.md
./mig/doc/image/README.md
./mig/doc/onbrd/README.md
./mig/doc/video/README.md
./mig/doc/library_ext/README.md
./mig/doc/template/README.md
./mig/doc/README.md
./mig/doc/audio/README.md
./mig/log/changelog/README.md
./mig/log/trazabilidad_total/README.md
./mig/log/README.md
./mig/log/bitacoras/README.md
./mig/data/mplan/README.md
./mig/data/mtx/README.md
./mig/data/template/README.md
./mig/data/README.md
./mig/data/rulset/README.md
./mig/kns/ai_learn/shot/README.md
./mig/kns/ai_learn/tune/README.md
./mig/kns/ai_learn/learn/README.md
./mig/kns/ai_learn/trn/README.md
./mig/kns/ai_learn/eval/README.md
./mig/kns/ai_learn/README.md
./mig/kns/ai_learn/rel/README.md
./mig/kns/ai_learn/feed/README.md
./mig/kns/chkp/projects/README.md
./mig/kns/chkp/README.md
./mig/kns/chkp/aingz_platform/README.md
./mig/kns/ctx/snaphots_ai/README.md
./mig/kns/ctx/projects/README.md
./mig/kns/ctx/README.md
./mig/kns/ctx/aingz_platform/README.md
./mig/kns/README.md
./mig/wf/audt/README.md
./mig/wf/mig_cons/README.md
./mig/wf/tareas_acciones/README.md
./mig/wf/relv/README.md
./mig/wf/README.md
./mig/README.md
./.gitignore
./SNAPSHOTS_CTX/o4/README.md
./SNAPSHOTS_CTX/ctx_connections_feedback_o3_o4_41_v1.md
./SNAPSHOTS_CTX/gpt4_1/README.md
./SNAPSHOTS_CTX/o3/README.md
./SNAPSHOTS_CTX/README.md
./legacy_old/lote_1/originals/Lote_1_1/Legacy_onboarding_gz.md
./legacy_old/lote_1/originals/Lote_1_1/Legacy_MTX_jerarquia_instrucciones.md
./legacy_old/lote_1/originals/Lote_1_1/Legacy_MTXfaq_avanzada_gestion_de_adjuntos.md
./legacy_old/lote_1/originals/Lote_1_1/Legacy_MTX_instrucciones.md
./legacy_old/lote_1/originals/Lote_1_1/README.md
./legacy_old/lote_1/originals/Lote_1_1/Legacy_MTX_features_prompts.md
./legacy_old/lote_1/originals/Lote_1_2/jerarquia_precedencia_instrucciones_v_1_lote_1_20250724.md
./legacy_old/lote_1/originals/Lote_1_2/aing_z_repo_raw_gold_scaffold.md
./legacy_old/lote_1/originals/Lote_1_2/readme_base_aingz_t_3_infra.md
./legacy_old/lote_1/originals/Lote_1_2/aing_z_repo_legacy_barrido_raw.md
./legacy_old/lote_1/originals/Lote_1_2/faq_workflows_operativo_v_1_lote_1_20250724.md
./legacy_old/lote_1/originals/Lote_1_2/matriz_features_prompts_v_1_lote_1_20250724.md
./legacy_old/lote_1/originals/Lote_1_2/t_3_raw_gold_canvas_integrado_final_v_2.md
./legacy_old/lote_1/originals/Lote_1_2/readme_master_plan.md
./legacy_old/lote_1/originals/Lote_1_2/readme_onbrd_v_1_lote_1_20250724.md
./legacy_old/lote_1/originals/Lote_1_2/rawgold_scaffold_readme.md
./legacy_old/lote_1/originals/Lote_1_2/README.md
./legacy_old/lote_1/originals/Lote_1_2/readme_matriz_memorias_historiales.md
./legacy_old/lote_1/originals/Lote_1_2/readme_integracion_t_2_memorias_historiales.md
./legacy_old/lote_1/originals/Lote_1_2/t_3_raw_gold_matriz_final.md
./legacy_old/lote_1/README.md
./legacy_old/lote_1/audit/Lote_1_1/jerarquia_precedencia_instrucciones_v_1_lote_1_20250724.md
./legacy_old/lote_1/audit/Lote_1_1/rw_b_audt_mtxinstr_legacy_v_1_2_20250724.md
./legacy_old/lote_1/audit/Lote_1_1/rw_b_audt_mtxjerarq_instr_legacy_v_1_2_20250724.md
./legacy_old/lote_1/audit/Lote_1_1/rw_b_review_consolidacion_auditoria_lote_1_v_1_20250724.md
./legacy_old/lote_1/audit/Lote_1_1/faq_workflows_operativo_v_1_lote_1_20250724.md
./legacy_old/lote_1/audit/Lote_1_1/matriz_features_prompts_v_1_lote_1_20250724.md
./legacy_old/lote_1/audit/Lote_1_1/rw_b_audt_mtxfaq_adjuntos_legacy_v_1_2_20250724.md
./legacy_old/lote_1/audit/Lote_1_1/rw_b_plan_consolidacion_lote_1_v_1_20250724.md
./legacy_old/lote_1/audit/Lote_1_1/readme_onbrd_v_1_lote_1_20250724.md
./legacy_old/lote_1/audit/Lote_1_1/rw_b_audt_mtxfeat_prompts_legacy_v_1_2_20250724.md
./legacy_old/lote_1/audit/Lote_1_1/rw_b_audt_onbrd_aingz_legacy_v_1_2_20250724.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_lote_2_readme_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_readme_raiz_lote_2_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/mapeo_consolidado_lote_2_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_readme_integracion_t_2_memorias_historiales_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_rawgold_scaffold_readme_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_readme_master_plan_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_aing_z_repo_legacy_barrido_raw_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_readme_base_aingz_t_3_infra_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_aing_z_repo_raw_gold_scaffold_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/revision_cruzada_auditorias_lote_2_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_t_3_raw_gold_matriz_final_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_t_3_raw_gold_canvas_integrado_final_v_2_v_1_20250725.md
./legacy_old/lote_1/audit/Lote_1_2/auditoria_readme_matriz_memorias_historiales_v_1_20250725.md
./legacy_old/lote_3/originals/Lote_Gem_Digitales/gem_dig_gz_gpt_raw.md
./legacy_old/lote_3/originals/Lote_Gem_Digitales/Bloque 7.json
./legacy_old/lote_3/originals/Lote_Gem_Digitales/Bloque 6.json
./legacy_old/lote_3/originals/Lote_Gem_Digitales/Bloque 5.json
./legacy_old/lote_3/originals/Lote_Gem_Digitales/Bloque 2.json
./legacy_old/lote_3/originals/Lote_Gem_Digitales/Bloque 3.json
./legacy_old/lote_3/originals/Lote_Gem_Digitales/Bloque 8.json
./legacy_old/lote_3/originals/Lote_Gem_Digitales/DR GZ Web 1.pdf
./legacy_old/lote_3/originals/Lote_Gem_Digitales/Bloque 4.json
./legacy_old/lote_3/originals/Lote_Gem_Digitales/Bloque 1.json
./legacy_old/lote_3/originals/Lote_Gem_Digitales/Cv Gaston 2020.doc
./legacy_old/lote_3/originals/Lote_Gem_Digitales/gem_dig_gz_gpt_raw_v_1.md
./legacy_old/lote_3/originals/Lote_Inventario/reporte_hw_gz_n56vz_2025-07-15_19-51.md
./legacy_old/lote_3/originals/Lote_Inventario/inventario_tecnico_prompt_y_template_raw.md
./legacy_old/lote_3/originals/Lote_Inventario/gz_n_56_vz_tech.md
./legacy_old/lote_3/originals/Lote_Inventario/reporte_hw_gz_n56vz_2025-07-15_19-51.csv
./legacy_old/lote_3/originals/Lote_Inventario/gz_e_bike_knowledge v2.md
./legacy_old/lote_3/originals/Lote_Inventario/gz_e_bike_knowledge.md
./legacy_old/lote_3/originals/Lote_Inventario/bike_electrical_knowledge_v_2.md
./legacy_old/lote_3/README.md
./legacy_old/lote_3/audit/Inventarios/rw_b_audt_bike_electrical_knowledge_v_2_lote_2_20250725.md
./legacy_old/lote_3/audit/Inventarios/rw_b_audt_inventario_prompt_template_raw_lote_2_20250725.md
./legacy_old/lote_3/audit/Inventarios/rw_b_mapeo_global_auditoria_inventario_gz_lote_2_20250725.md
./legacy_old/lote_3/audit/Inventarios/rw_b_resumen_mapping_inventario_gz_lote_2_20250725.md
./legacy_old/lote_3/audit/Inventarios/rw_b_audt_script_hw_info_gz_n_56_vz_lote_2_20250725.md
./legacy_old/lote_3/audit/Inventarios/rw_b_audt_reporte_hw_gz_n_56_vz_lote_2_20250725.md
./legacy_old/lote_3/audit/Inventarios/rw_b_audt_gz_e_bike_knowledge_v_1_lote_2_20250725.md
./legacy_old/lote_3/audit/Inventarios/rw_b_audt_ficha_tec_gz_n_56_vz_lote_2_20250725.md
./legacy_old/lote_3/audit/Inventarios/rw_b_audt_gz_e_bike_knowledge_v_2_lote_2_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_audt_cv_gaston_2020_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_mapeo_global_auditoria_gemelo_digital_gz_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_mapeo_global_jsons_gemelo_digital_gz_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_audt_json_gemelo_digital_bloques_3_4_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_audt_gem_dig_gz_gpt_raw_v_1_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_audt_json_gemelo_digital_bloques_5_6_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_audt_json_gemelo_digital_bloques_1_2_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_audt_gem_dig_gz_gpt_raw_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_audt_json_gemelo_digital_bloques_7_8_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_resumen_mapping_gemelo_digital_gz_lote_2_20250725.md
./legacy_old/lote_3/audit/Gem_Dig/rw_b_audt_dr_gz_web_1_perfil_publico_20250725.md
./legacy_old/lote_3/audit/rw_b_ctx_gemelo_digital_inventario_20250725.md
./legacy_old/lote_4/originals/bliblioteca_refencia/matriz_limites_contexto_chatgpt_v_1.md
./legacy_old/lote_4/originals/bliblioteca_refencia/02_capacidades_y_limitaciones_agent_mode.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Help_OpenAi/Buildings_GPTs.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Help_OpenAi/Sharing_GPTs.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Help_OpenAi/GPTs.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Help_OpenAi/ChatGPT.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/4.Tools.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/9.Codex.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/7.Model_Optimization.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/11.Assistants_Api.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/5.Agents.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/8.Specialized_Models.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/12.0.Resources.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/3.Api_Guides.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/2.Core_Concepts.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/1.Get_Started.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/10.Best_Practices.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/6.Realtime_Api.md
./legacy_old/lote_4/originals/bliblioteca_refencia/openai/Docs_OpenAi/12.1.ChatGPT_Actions.md
./legacy_old/lote_4/originals/bliblioteca_refencia/Análisis del repositorio.pdf
./legacy_old/lote_4/originals/Lote_Gem_Digitales/gem_dig_gz_gpt_raw.md
./legacy_old/lote_4/originals/Lote_Gem_Digitales/Bloque 7.json
./legacy_old/lote_4/originals/Lote_Gem_Digitales/Bloque 6.json
./legacy_old/lote_4/originals/Lote_Gem_Digitales/Bloque 5.json
./legacy_old/lote_4/originals/Lote_Gem_Digitales/Bloque 2.json
./legacy_old/lote_4/originals/Lote_Gem_Digitales/Bloque 3.json
./legacy_old/lote_4/originals/Lote_Gem_Digitales/Bloque 8.json
./legacy_old/lote_4/originals/Lote_Gem_Digitales/DR GZ Web 1.pdf
./legacy_old/lote_4/originals/Lote_Gem_Digitales/Bloque 4.json
./legacy_old/lote_4/originals/Lote_Gem_Digitales/Bloque 1.json
./legacy_old/lote_4/originals/Lote_Gem_Digitales/Cv Gaston 2020.doc
./legacy_old/lote_4/originals/Lote_Gem_Digitales/gem_dig_gz_gpt_raw_v_1.md
./legacy_old/lote_4/originals/Lote_Inventario/reporte_hw_gz_n56vz_2025-07-15_19-51.md
./legacy_old/lote_4/originals/Lote_Inventario/inventario_tecnico_prompt_y_template_raw.md
./legacy_old/lote_4/originals/Lote_Inventario/gz_n_56_vz_tech.md
./legacy_old/lote_4/originals/Lote_Inventario/reporte_hw_gz_n56vz_2025-07-15_19-51.csv
./legacy_old/lote_4/originals/Lote_Inventario/gz_e_bike_knowledge v2.md
./legacy_old/lote_4/originals/Lote_Inventario/gz_e_bike_knowledge.md
./legacy_old/lote_4/originals/Lote_Inventario/bike_electrical_knowledge_v_2.md
./legacy_old/lote_4/README.md
./legacy_old/lote_2/originals/Lote_matrices/plantilla_snapshot_memoria.md
./legacy_old/lote_2/originals/Lote_matrices/matriz_precedencia_instrucciones_full_custom_infraestructura.md
./legacy_old/lote_2/originals/Lote_matrices/ejemplo_integracion_memoria_feedback.md
./legacy_old/lote_2/originals/Lote_matrices/control_trazabilidad_fuentes_chatgpt_workflow.md
./legacy_old/lote_2/originals/Lote_matrices/matriz_memorias_historiales_chatgpt.md
./legacy_old/lote_2/originals/Lote_matrices/leccion_aprendida_upgrade_memorias.md
./legacy_old/lote_2/originals/Lote_matrices/checklist_testing_memorias_historiales.md
./legacy_old/lote_2/originals/Lote_matrices/control_cruce_matriz_raw_vs_extendida.md
./legacy_old/lote_2/originals/Lote_matrices/matrices_readme.md
./legacy_old/lote_2/originals/Lote_matrices/t_2_2_raw_gold_matriz_historiales.md
./legacy_old/lote_2/originals/Lote_matrices/rw_b_matriz_triggers_contexto.md
./legacy_old/lote_2/originals/Lote_matrices/t_3_raw_gold_matriz_final.md
./legacy_old/lote_2/originals/Lote_knowledge/knowledge_base_aingz_t_3.md
./legacy_old/lote_2/originals/Lote_knowledge/mtx/profundizacion_matriz_precedencia_instrucciones_y_features_aing_z_repo.md
./legacy_old/lote_2/originals/Lote_knowledge/mtx/matriz_raw_features_chatgpt_workflow.md
./legacy_old/lote_2/originals/Lote_knowledge/mtx/matriz_extendida_features_chatgpt_workflow.md
./legacy_old/lote_2/originals/Lote_knowledge/mtx/readme_explicativo_matriz_features.md
./legacy_old/lote_2/originals/Lote_knowledge/knowledge_base_matriz_precedencia_templates_universales_raw.md
./legacy_old/lote_2/originals/Lote_knowledge/readme_knowledge.md
./legacy_old/lote_2/originals/Lote_knowledge/knowledge_memorias_feedback_reglas_oro.md
./legacy_old/lote_2/originals/Lote_knowledge/knowledge_gz_project_insights.md
./legacy_old/lote_2/originals/Lote_knowledge/t_3_raw_gold_matriz_final.md
./legacy_old/lote_2/originals/Lote_templates/templates_casos_uso_precedencia_infraestructura_full_custom.md
./legacy_old/lote_2/originals/Lote_templates/plantilla_prompt_custom_gpt.md
./legacy_old/lote_2/originals/README.md
./legacy_old/lote_2/originals/Lote_workflows/readme_workflows.md
./legacy_old/lote_2/originals/Lote_workflows/workflow_gpt_raw_v_1.md
./legacy_old/lote_2/originals/Lote_workflows/rw_b_macro_plan_migracion_v_2.md
./legacy_old/lote_2/originals/Lote_workflows/workflow_gz_project_template.md
./legacy_old/lote_2/originals/Lote_workflows/workflow_gpt_raw.md
./legacy_old/lote_2/README.md
./legacy_old/lote_2/audit/KNS/rw_b_resumen_auditoria_kns_matrices_lote_2_20250725.md
./legacy_old/lote_2/audit/KNS/rw_b_audt_matriz_extendida_features_chatgpt_workflow_lote_2_20250725.md
./legacy_old/lote_2/audit/KNS/rw_b_audt_readme_explicativo_matriz_features_lote_2_20250725.md
./legacy_old/lote_2/audit/KNS/rw_b_mapeo_global_kns_lote_2_20250725.md
./legacy_old/lote_2/audit/KNS/rw_b_audt_profundizacion_matriz_precedencia_features_lote_2_20250725.md
./legacy_old/lote_2/audit/KNS/rw_b_audt_matriz_raw_features_chatgpt_workflow_lote_2_20250725.md
./legacy_old/lote_2/audit/KNS/rw_b_audt_kns_memorias_feedback_reglas_oro_lote_2_20250725.md
./legacy_old/lote_2/audit/KNS/rw_b_audt_kns_readme_knowledge_lote_2_20250725.md
./legacy_old/lote_2/audit/KNS/rw_b_audt_kns_matriz_precedencia_templates_lote_2_20250725.md
./legacy_old/lote_2/audit/KNS/rw_b_audt_kns_t_3_raw_gold_matriz_final_lote_2_20250725.md
./legacy_old/lote_2/audit/KNS/rw_b_audt_kns_gz_project_insights_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_matriz_memorias_historiales_chatgpt_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_matrices_readme_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_ejemplo_integracion_memoria_feedback_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_t_2_2_raw_gold_matriz_historiales_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_control_trazabilidad_fuentes_chatgpt_workflow_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_control_cruce_matriz_raw_vs_extendida_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_plantilla_snapshot_memoria_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_mapeo_global_matrices_legacy_lote_2_completo_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_checklist_testing_memorias_historiales_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_t_3_raw_gold_matriz_final_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_leccion_aprendida_upgrade_memorias_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_rw_b_matriz_triggers_contexto_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_audt_matriz_precedencia_instrucciones_full_custom_infraestructura_lote_2_20250725.md
./legacy_old/lote_2/audit/mtx/rw_b_resumen_auditoria_matrices_legacy_lote_2_20250725.md
./legacy_old/lote_2/audit/rw_b_barrido_global_auditorias_sesion_lote_2_20250725.md
./legacy_old/lote_2/audit/WF/rw_b_audt_readme_workflows_lote_2_20250725.md
./legacy_old/lote_2/audit/WF/rw_b_audt_workflow_gpt_raw_v_1_v_1_lote_2_20250725.md
./legacy_old/lote_2/audit/WF/rw_b_audt_macro_plan_migracion_v_2_lote_2_20250725.md
./legacy_old/lote_2/audit/WF/rw_b_audt_workflow_gpt_raw_v_1_lote_2_20250725.md
./legacy_old/lote_2/audit/WF/rw_b_resumen_auditoria_wf_lote_2_20250725.md
./legacy_old/lote_2/audit/WF/rw_b_audt_workflow_gz_project_template_lote_2_20250725.md
./legacy_old/lote_2/audit/Tmpl/rw_b_resumen_auditoria_templates_lote_2_20250725.md
./legacy_old/lote_2/audit/Tmpl/rw_b_audt_template_prompt_custom_gpt_lote_2_20250725.md
./legacy_old/lote_2/audit/Tmpl/rw_b_audt_template_casos_uso_precedencia_infra_full_custom_lote_2_20250725.md
./.editorconfig
./.github/workflows/validation.yml
./README.md
./requirements.txt
./core/scr/README.md
./core/rw_b_diccionario_code_triggers_v_2_20250729.md
./core/doc/library/README.md
./core/doc/image/README.md
./core/doc/onbrd/README.md
./core/doc/video/README.md
./core/doc/library_ext/README.md
./core/doc/template/README.md
./core/doc/README.md
./core/doc/audio/README.md
./core/log/changelog/chglog_actv_kns_ctx_raw_v_1_20250725.md
./core/log/changelog/README.md
./core/log/trazabilidad_total/README.md
./core/log/README.md
./core/log/bitacoras/README.md
./core/data/repo_monorepo_packages_blueprint_v1_20250731.md
./core/data/crossref_mapping_buckets_aingz_platform_v_1_20250731.md
./core/data/blueprint_aingz_platform_v_1_20250731.md
./core/data/mplan/README.md
./core/data/mplan/o3_full_instructions.md
./core/data/mtx/rw_b_assets_classification_matrix_v_1_20250729.md
./core/data/mtx/README.md
./core/data/ctx_o_3_rw_b_total_20250731.md
./core/data/system_prompt_aingz_models_o3_o4_41_v1.md
./core/data/aing_z_platform_connectors_matrix_v_2.md
./core/data/template/README.md
./core/data/README.md
./core/data/rulset/README.md
./core/kns/metrics/kpis_consolidacion.md
./core/kns/ai_learn/shot/README.md
./core/kns/ai_learn/tune/README.md
./core/kns/ai_learn/learn/learn_actv_kns_ctx_raw_v_1_20250725.md
./core/kns/ai_learn/learn/README.md
./core/kns/ai_learn/trn/README.md
./core/kns/ai_learn/trn/trnlog_actv_kns_ctx_raw_v_1_20250725.md
./core/kns/ai_learn/eval/README.md
./core/kns/ai_learn/insi/insi_actv_kns_ctx_raw_v_1_20250725.md
./core/kns/ai_learn/README.md
./core/kns/ai_learn/rel/README.md
./core/kns/ai_learn/feed/README.md
./core/kns/chkp/projects/README.md
./core/kns/chkp/rw_b_kns_chkp_legacy_v_0.md
./core/kns/chkp/README.md
./core/kns/chkp/aingz_platform/README.md
./core/kns/glossary/rw_b_glossary_rdm_v_0.md
./core/kns/glossary/rw_b_naming_convention.md
./core/kns/glossary/rw_b_glosario_code_v_2_20250729.md
./core/kns/ctx/rw_b_kns_ctx_v_1_20250724.md
./core/kns/ctx/snaphots_ai/README.md
./core/kns/ctx/projects/README.md
./core/kns/ctx/rw_b_kns_ctx_v_0_lswp.md
./core/kns/ctx/kns_ctx_legacy_migracion_final_20250725.md
./core/kns/ctx/README.md
./core/kns/ctx/aingz_platform/README.md
./core/kns/ideas_brainstorm/idea_actv_kns_ctx_raw_v_1_20250725.md
./core/kns/ideas_brainstorm/brain_actv_kns_ctx_raw_v_1_20250725.md
./core/kns/README.md
./core/wf/wf_migracion_final_legacy_rw_b_v_1_20250725.md
./core/wf/audt/README.md
./core/wf/rw_b_wf_auditoria_cierre_hilo_actv_v_1_20250725.md
./core/wf/wf_cons_actv_transcripcion_raw_v_4_20250730_draft.md
./core/wf/chg_log_wf_purgatorio_20250725.md
./core/wf/wk_feedtrn_eval_actv_raw_v_2_20250725.md
./core/wf/rw_b_wf_auditoria_legacy_v_3_20250725.md
./core/wf/mig_cons/README.md
./core/wf/tareas_acciones/README.md
./core/wf/rw_b_wf_relevamiento_ideas_actv_v_1_20250725.md
./core/wf/rw_b_wf_dictado_v_1.md
./core/wf/relv/README.md
./core/wf/README.md
./core/wf/rw_b_wf_inicio_repo_check_v_1_20250731.md
./core/wf/rw_b_wf_relev_hilo_assets_v_1_20250729.md
./core/onbrd_welcome_onboarding_gz_rw_b_v_20250725.md
./core/README.md
./connectors/README.md
```

## Context from core/data
- El blueprint de la plataforma define un ruleset universal que abarca repos, packages, conectores y apps, con un ciclo de vida que va de LEGACY a CORE y backups estructurados.
- El documento de crossref establece que todas las referencias se manejan a nivel de buckets y proporciona una tabla de mapeo entre directorios principales.

## Blueprint roadmap para consolidación
1. Implementar la arquitectura de buckets descrita en el blueprint asegurando naming `SRC·STG·ROLE` y README con crossref.
2. Automatizar scripts que generen estructuras, README y mapping central según el esquema propuesto en crossref.
3. Integrar pipelines de auditoría y backups para mantener trazabilidad y cumplimiento del ruleset RwB+.
4. Centralizar documentación y onboarding en DOC/MPLN y ONBRD según las directrices de `core/data`.

# Auditoría del bucket `core`

## 1. Mapeo del árbol y estructura

Estructura completa de directorios bajo `core/`:

- `core/`  
- `core/data/`  
  - `core/data/mplan/`  
  - `core/data/mtx/`  
  - `core/data/rulset/`  
  - `core/data/template/`  
- `core/doc/`  
  - `core/doc/audio/`  
  - `core/doc/image/`  
  - `core/doc/library/`  
  - `core/doc/library_ext/`  
  - `core/doc/onbrd/`  
  - `core/doc/template/`  
  - `core/doc/video/`  
- `core/kns/`  
  - `core/kns/ai_learn/`  
    - `core/kns/ai_learn/eval/`  
    - `core/kns/ai_learn/feed/`  
    - `core/kns/ai_learn/insi/`  
    - `core/kns/ai_learn/learn/`  
    - `core/kns/ai_learn/rel/`  
    - `core/kns/ai_learn/shot/`  
    - `core/kns/ai_learn/trn/`  
    - `core/kns/ai_learn/tune/`  
  - `core/kns/chkp/`  
    - `core/kns/chkp/aingz_platform/`  
    - `core/kns/chkp/projects/`  
  - `core/kns/ctx/`  
    - `core/kns/ctx/aingz_platform/`  
    - `core/kns/ctx/projects/`  
    - `core/kns/ctx/snaphots_ai/`  
  - `core/kns/glossary/`  
  - `core/kns/ideas_brainstorm/`  
  - `core/kns/metrics/`  
- `core/log/`  
  - `core/log/bitacoras/`  
  - `core/log/changelog/`  
  - `core/log/trazabilidad_total/`  
- `core/scr/`  
- `core/wf/`  
  - `core/wf/audt/`  
  - `core/wf/mig_cons/`  
  - `core/wf/relv/`  
  - `core/wf/tareas_acciones/`

## 2. Metadatos, naming y compliance

| Archivo (ruta relativa) | Tipo | Naming universal | YAML | Status/Autor/Fecha |
|---|---|---|---|---|
| core/README.md | README | Sí | No | Sí |
| core/onbrd_welcome_onboarding_gz_rw_b_v_20250725.md | Doc/onboarding | Sí | No | No |
| core/rw_b_diccionario_code_triggers_v_2_20250729.md | Diccionario/triggers | Sí | No | No |
| core/data/README.md | README | Sí | No | Sí |
| core/data/aing_z_platform_connectors_matrix_v_2.md | Matriz | Sí | No | No |
| core/data/blueprint_aingz_platform_v_1_20250731.md | Blueprint | Sí | No | No |
| core/data/crossref_mapping_buckets_aingz_platform_v_1_20250731.md | Crossref | Sí | No | No |
| core/data/ctx_o_3_rw_b_total_20250731.md | Contexto | Sí | No | No |
| core/data/mplan/README.md | README | Sí | No | Sí |
| core/data/mplan/o3_full_instructions.md | Instrucciones | Sí | No | No |
| core/data/mtx/README.md | README | Sí | No | Sí |
| core/data/mtx/rw_b_assets_classification_matrix_v_1_20250729.md | Matriz | Sí | No | No |
| core/data/repo_monorepo_packages_blueprint_v1_20250731.md | Blueprint | Sí | No | No |
| core/data/rulset/README.md | README | Sí | No | Sí |
| core/data/system_prompt_aingz_models_o3_o4_41_v1.md | System prompt | Sí | No | No |
| core/data/template/README.md | README | Sí | No | Sí |
| core/doc/README.md | README | Sí | No | No |
| core/doc/audio/README.md | README | Sí | No | Sí |
| core/doc/image/README.md | README | Sí | No | No |
| core/doc/library/README.md | README | Sí | No | Sí |
| core/doc/library_ext/README.md | README | Sí | No | Sí |
| core/doc/onbrd/README.md | README | Sí | No | Sí |
| core/doc/template/README.md | README | Sí | No | Sí |
| core/doc/video/README.md | README | Sí | No | Sí |
| core/kns/README.md | README (plantilla) | Sí | No | Sí |
| core/kns/ai_learn/README.md | README | Sí | No | No |
| core/kns/ai_learn/eval/README.md | README | Sí | No | No |
| core/kns/ai_learn/feed/README.md | README | Sí | No | No |
| core/kns/ai_learn/insi/insi_actv_kns_ctx_raw_v_1_20250725.md | Insight | Sí | No | No |
| core/kns/ai_learn/learn/README.md | README | Sí | No | No |
| core/kns/ai_learn/learn/learn_actv_kns_ctx_raw_v_1_20250725.md | Registro learn | Sí | No | No |
| core/kns/ai_learn/rel/README.md | README | Sí | No | No |
| core/kns/ai_learn/shot/README.md | README | Sí | No | No |
| core/kns/ai_learn/trn/README.md | README | Sí | No | No |
| core/kns/ai_learn/trn/trnlog_actv_kns_ctx_raw_v_1_20250725.md | Log entrenamiento | Sí | No | No |
| core/kns/ai_learn/tune/README.md | README | Sí | No | No |
| core/kns/chkp/README.md | README | Sí | No | No |
| core/kns/chkp/aingz_platform/README.md | README | Sí | No | No |
| core/kns/chkp/projects/README.md | README | Sí | No | No |
| core/kns/chkp/rw_b_kns_chkp_legacy_v_0.md | Legacy | Sí | No | No |
| core/kns/ctx/README.md | README | Sí | No | No |
| core/kns/ctx/aingz_platform/README.md | README | Sí | No | No |
| core/kns/ctx/kns_ctx_legacy_migracion_final_20250725.md | Legacy | Parcial (sin prefijo RwB) | No | No |
| core/kns/ctx/projects/README.md | README | Sí | No | No |
| core/kns/ctx/rw_b_kns_ctx_v_0_lswp.md | Contexto v0 | Sí | No | No |
| core/kns/ctx/rw_b_kns_ctx_v_1_20250724.md | Contexto v1 | Sí | No | No |
| core/kns/ctx/snaphots_ai/README.md | README | Sí | No | Sí |
| core/kns/glossary/rw_b_glosario_code_v_2_20250729.md | Glosario | Sí | No | No |
| core/kns/glossary/rw_b_glossary_rdm_v_0.md | Glosario | Sí | No | No |
| core/kns/glossary/rw_b_naming_convention.md | Glosario | Sí | No | Sí |
| core/kns/ideas_brainstorm/brain_actv_kns_ctx_raw_v_1_20250725.md | Brainstorm | Sí | No | No |
| core/kns/ideas_brainstorm/idea_actv_kns_ctx_raw_v_1_20250725.md | Brainstorm | Sí | No | No |
| core/kns/metrics/kpis_consolidacion.md | Métricas | No | No | No |
| core/log/README.md | README | Sí | No | No |
| core/log/bitacoras/README.md | README | Sí | No | No |
| core/log/changelog/README.md | README | Sí | No | No |
| core/log/changelog/chglog_actv_kns_ctx_raw_v_1_20250725.md | Changelog | Sí | No | No |
| core/log/trazabilidad_total/README.md | README | Sí | No | No |
| core/scr/README.md | README | Sí | No | No |
| core/wf/README.md | README | Sí | No | No |
| core/wf/audt/README.md | README | Sí | No | Sí |
| core/wf/chg_log_wf_purgatorio_20250725.md | Workflow | Sí | No | No |
| core/wf/mig_cons/README.md | README | Sí | No | Sí |
| core/wf/relv/README.md | README | Sí | No | No |
| core/wf/rw_b_wf_auditoria_cierre_hilo_actv_v_1_20250725.md | Workflow | Sí | No | No |
| core/wf/rw_b_wf_auditoria_legacy_v_3_20250725.md | Workflow | Sí | No | No |
| core/wf/rw_b_wf_dictado_v_1.md | Workflow | Sí | No | No |
| core/wf/rw_b_wf_inicio_repo_check_v_1_20250731.md | Workflow | Sí | No | No |
| core/wf/rw_b_wf_relev_hilo_assets_v_1_20250729.md | Workflow | Sí | No | No |
| core/wf/rw_b_wf_relevamiento_ideas_actv_v_1_20250725.md | Workflow | Sí | No | No |
| core/wf/tareas_acciones/README.md | README | Sí | No | No |
| core/wf/wf_cons_actv_transcripcion_raw_v_4_20250730_draft.md | Workflow | Sí | No | Sí |
| core/wf/wf_migracion_final_legacy_rw_b_v_1_20250725.md | Workflow | Sí | No | No |
| core/wf/wk_feedtrn_eval_actv_raw_v_2_20250725.md | Workflow | Sí | No | No |

**Observaciones generales:**

- Ningún archivo posee front matter YAML.
- Las líneas de estado y autor se hallan en un subconjunto de archivos (18 elementos listados arriba).
- Ningún archivo declara explícitamente `owner` o `rol`; sólo se observa autor en algunos casos.

## 3. Crossref y documentación

- Los READMEs principales incluyen secciones de “Crossref y Mapping” con enlaces a buckets y al “Mapa Global”.
- Muchos READMEs son plantillas vacías sin referencias a blueprint, master plan, checklist o workflows.
- Algunos documentos en `data/` presentan tablas de inventario que sirven de referencia para estructura y buenas prácticas.
- No se detectaron referencias directas a checklists en la mayoría de los READMEs.

## 4. Gap analysis y legacy

**Faltan READMEs:**
- `core/kns/ai_learn/insi/`
- `core/kns/glossary/`
- `core/kns/ideas_brainstorm/`
- `core/kns/metrics/`

**READMEs incompletos o sin crossref:**
- `core/wf/README.md`
- `core/log/README.md`
- `core/doc/README.md`

**Archivos legacy/duplicados:**
- `core/kns/chkp/rw_b_kns_chkp_legacy_v_0.md`
- `core/kns/ctx/kns_ctx_legacy_migracion_final_20250725.md`
- `core/kns/ctx/rw_b_kns_ctx_v_0_lswp.md`

**Desviaciones de naming:**
- `core/kns/ctx/kns_ctx_legacy_migracion_final_20250725.md` (sin prefijo `rw_b_`).
- `core/kns/metrics/kpis_consolidacion.md` (naming genérico sin codificación RwB).

**Metadatos ausentes:**
- Ausencia total de front matter YAML y de campos de owner/rol.
- `STATUS` y fecha presentes solo en algunos READMEs; muchos carecen de cualquier metadato temporal.

## 5. Funcionalidad, triggers y referencias

- `core/wf/` contiene flujos de trabajo operativos (auditorías, relevamientos, migraciones, dictado) con pasos secuenciales sin inputs/outputs formales.
- `core/rw_b_diccionario_code_triggers_v_2_20250729.md` ofrece un catálogo de “code triggers” para prompts y scripts.
- `core/kns/` alberga conocimiento vivo (lessons, brainstorms, logs de entrenamiento) actuando como repositorio de insights.
- No se identificaron scripts ejecutables en `core/scr/`; sólo un README placeholder.
- Referencias a glosario están dispersas en `core/kns/glossary/` pero falta un índice central.

## 6. Acciones recomendadas hacia compliance pleno RwB

1. **Metadatos y naming**: introducir front matter YAML con `rol`, `status`, `owner` y `fecha` en todos los archivos; normalizar nombres faltantes y gestionar legacy.
2. **Documentación y crossref**: completar READMEs placeholders y añadir crossrefs a blueprint, master plan, checklists y workflows.
3. **Inventarios y tablas**: consolidar una tabla de inventario global de assets con versiones, owners y estado PDCA.
4. **Gestión de legacy**: revisar y migrar archivos con sufijo `legacy` o versión `v0`, documentando acciones de limpieza.
5. **Onboarding y glosario**: generar un índice central enlazando glosario, diccionario de triggers y lessons learned; actualizar el doc de onboarding.
6. **Automatización futura**: explorar scripts en `core/scr/` para verificación automática de metadatos, naming y crossrefs, integrando triggers del diccionario.

## Notas para onboarding y refactor incremental

- Priorizar la normalización de metadatos y naming antes de ampliar estructura.
- Incorporar revisiones periódicas (PDCA) en `log/changelog` para asegurar trazabilidad.
- Establecer un checklist de incorporación que guíe la creación de nuevos buckets y la documentación obligatoria.
- Reforzar la relación entre `core/` y los buckets `bk_temp`, `legacy` y `mig` para asegurar el flujo LEGACY→TMP→MIG→CORE→bk_temp descrito en los READMEs principales.


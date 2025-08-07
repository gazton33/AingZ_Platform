
# [RwB] README.md — Platform ROOT (V3.x.x auditado · roadmap V4, 2025-08-06)

---

## 1. Estado Actual
Este repositorio contiene la **versión operativa V3.x.x** de la plataforma AingZ/RwB. Toda la arquitectura, carpetas y naming actual corresponden al estándar v3.x, salvo los siguientes archivos raíz que preparan la transición y documentación para V4:

- `rw_b_blueprint_v_4_extendido_2025_08_06.md` (blueprint futuro)
- `rw_b_master_plan_v_4_extendido_2025_08_06.md` (master plan futuro)
- `prompt_codex_baseline_v_4_check.md` (prompt Codex para migración/chequeo)
- `readme.md` (este archivo)

**IMPORTANTE:** El árbol `core/`, `data/`, `doc/`, `kns/` y subcarpetas mantienen metadatos y naming de V3.x.x.

---

## 2. Estructura real del repo (auditada)

```plaintext
platform/
  prompt_codex_baseline_v_4_check.md
  readme.md
  rw_b_blueprint_v_4_extendido_2025_08_06.md
  rw_b_master_plan_v_4_extendido_2025_08_06.md
  core/
    readme_core_rw_b_v_3_2.md
    data/
      readme_core_data_rw_b_v_3_2.md
      dicts/
        readme_core_data_dicts_rw_b_v_3_2.md
        rw_b_diccionario_code_triggers_v_2_20250729.md
      mplan/
        readme_core_data_mplan_rw_b_v_3_2.md
      mtx/
        readme_core_data_mtx_rw_b_v_3_2.md
      rulset/
        readme_core_data_rulset_rw_b_v_3_2.md
      template/
        readme_core_data_template_rw_b_v_3_2.md
    doc/
      readme_core_doc_audio_rw_b_v_3_2.md
      readme_core_doc_image_rw_b_v_3_2.md
      readme_core_doc_onbrd_rw_b_v_3_2.md
      readme_core_doc_rw_b_v_3_2.md
      readme_core_doc_template_rw_b_v_3_2.md
      readme_core_doc_video_rw_b_v_3_2.md
    kns/
      readme_core_kns_rw_b_v_3_2.md
      ai_learn/
        readme_core_kns_ai_learn_rw_b_v_3_2.md
        eval/
          readme_core_kns_ai_learn_eval_rw_b_v_3_2.md
        feed/
          readme_core_kns_ai_learn_feed_rw_b_v_3_2.md
        insi/
          readme_core_kns_ai_learn_insi_rw_b_v_3_2.md
        learn/
          readme_core_kns_ai_learn_learn_rw_b_v_3_2.md
```

---

## 3. Limitaciones actuales y advertencias
- Todo el core, naming, crossref y templates siguen la lógica V3.x.x.
- No se encuentran carpetas ni readme estandarizados bajo reglas V4 (naming, outputtemplate, metadatos YAML, crossref V4).
- **No realizar cambios estructurales sin checklist y plan de migración.**

---

## 4. Objetivo inmediato: transición y compliance V4
### El objetivo clave es:
- Migrar 100% del repo a estándar **V4** según blueprint y master plan adjuntos.
- Ejecutar el Prompt Codex Baseline para:
    1. Barrido literal (listar todo el árbol y archivos, identificar faltantes para V4)
    2. Detectar y crear carpetas y README bajo estándar V4 (naming, metadatos, crossref)
    3. Generar diagnóstico de discrepancias y registrar en checklist
    4. Versionar y documentar cada migración/cambio en changelog y lessons learned
- Eliminar toda referencia y asset legacy V3.x.x una vez migrado el árbol completo.

---

## 5. Pendientes críticos para alcanzar V4
- [ ] Crear todas las carpetas, buckets y subcarpetas faltantes según Blueprint V4
- [ ] Reescribir todos los README usando outputtemplate y crossref estándar V4
- [ ] Normalizar naming y rutas bajo la regla de máxima jerarquía (naming universal, outputtemplate, versionado, crossref)
- [ ] Implementar metadatos YAML y bloques outputtemplate en todos los activos
- [ ] Estandarizar onboarding, feedback y workflows con referencia directa a blueprint, masterplan y glosario V4
- [ ] Automatizar triggers y reporting según diccionario CODE_TRIGGERS v2
- [ ] Validar todo asset, carpeta y pipeline con el prompt Codex Baseline
- [ ] Actualizar este README a formato V4 y migrar a ruta/documento definitivo

---

## 6. Bloque IA / ingestión automática
```yaml
file: readme.md
version: v3.xx-audit-20250806
blueprint: rw_b_blueprint_v_4_extendido_2025_08_06.md
masterplan: rw_b_master_plan_v_4_extendido_2025_08_06.md
prompt_codex: prompt_codex_baseline_v_4_check.md
status: migracion-pendiente-v4
note: "Toda la estructura core sigue V3.xx. Roadmap de migración y compliance activo."
```
---

**Fin README raíz V3.x.x + objetivos V4**

---
CODE: README_ROOT
ID: root_readme
VERSION: v4.0-2025-08-07
ROUTE: README.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
AUTHOR: AingZ_Platform
DATE: 2025-08-07
---
# [RwB] README.md — Platform ROOT (V4, 2025-08-07, versión reforzada)

## 1. Estado y advertencia
*Este README ha sido reforzado para operar bajo arquitectura V4, con instrucciones explícitas para Codex u otros agentes LLM. Debe escanear y actualizar dinámicamente cualquier referencia o crossref afectada por el movimiento de archivos clave.*

---

## 2. Propósito y situación del repo
- El objetivo es alcanzar compliance V4, consolidando el árbol y todos los assets según blueprint y master plan vigentes.
- Se detectó que archivos críticos (blueprint, master plan, prompt Codex, este README) pueden haber sido movidos de la raíz a subcarpetas (`core/lifecycle/temp`, `ops/`, etc.).
- Los crossref deben reflejar siempre la **ubicación real** y actualizada de estos archivos en todo el repo.

---

## 3. Crossref dinámico y referencia clave
- Todos los scripts y README **deben detectar automáticamente** la ruta actual de:
  - `lifecycle/temp/prompt_codex_baseline_v_4_check.md`
  - `lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md`
  - `lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md`
  - Cualquier README clave y ruleset (`core/rulset/RULE_CODING_COMPLIANCE_V4.md`)
- Al detectar cambios de ubicación:
  - **Actualizar crossref en todos los README afectados**
  - Registrar cambio en changelog y lessons learned

---

## 4. ⚠️ Validación Automática (para Codex y humanos)
1. Ejecuta barrido completo del repo (`LITW //sweep`, o script Python de walk).
2. Detecta la ubicación real de todos los archivos clave listados arriba.
3. Actualiza el bloque crossref de este y todos los README, usando la ruta real detectada.
4. Refuerza que todos los README incluyan:
   - Descripción y objetivos actuales (no legacy)
   - Crossref vivo (ruta exacta a blueprint, masterplan, prompt Codex, ruleset)
   - Metadatos YAML y OutputTemplate, alineados a V4
5. Ejecuta triggers QA (`TRG_AUDIT_TL`, `TRG_CONSOLIDATE_TL`, `TRG_LSWP`) y registra resultado en changelog.
6. Documenta cada ciclo, excepción y workaround en lessons learned y checklist incremental.

---

## 5. Pendientes críticos y acciones recomendadas inmediatas (para Codex)
- [ ] Buscar y actualizar crossref en todos los README del repo (no solo raíz) tras cualquier cambio de ubicación de archivo clave.
- [ ] Implementar barrido literal 100% repo antes de cualquier edición de crossref.
- [ ] Generar/actualizar `core/rulset/RULE_CODING_COMPLIANCE_V4.md` y referenciarlo dinámicamente en los README.
- [ ] Validar que todos los README, assets y workflows tengan metadatos YAML, descripción actualizada y OutputTemplate.
- [ ] Registrar todo fix o hallazgo en changelog y lessons learned.
- [ ] Configurar y testear cualquier secret/token necesario para GitHub Actions o CI:
    - Si CI/CD automático: crear secret `GH_TOKEN_RW_B_CI` con permisos `repo, workflow`.
    - Si solo trabajo local/manual: omitir (no es requerido para Codex local).
- [ ] Actualizar/crear `requirements.txt` con dependencias (`openai`, `pyyaml`, `pytest`, etc.) si vas a correr CI/CD.

---

## 6. Bloque IA / ingestión automática
```yaml
file: readme.md
version: v4.0-20250807
crossref_blueprint: lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
crossref_masterplan: lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
crossref_prompt_codex: lifecycle/temp/prompt_codex_baseline_v_4_check.md
crossref_ruleset: core/rulset/RULE_CODING_COMPLIANCE_V4.md
status: migracion-actualizacion-v4
note: "Validar crossref dinámico y barrido 100% repo tras cada ciclo."
```

---

**Fin README raíz V4 (con crossref dinámico)**

## OutputTemplate
```yaml
CODE:
ID:
VERSION:
ROUTE:
CROSSREF:
AUTHOR:
DATE:
```

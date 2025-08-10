---
CODE: LIBRA
ID: readme_library_intg_rw_b_v_3_1_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/library/intg/readme_library_intg_rw_b_v_3_1.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# 📚 README — Subcarpeta `intg/` (RwB v3.1)

## 1. Rol y propósito
Contenedor para recursos de **integración**: corpus consolidado, mappings y documentación transversal que enlaza buckets y workflows de la plataforma. Facilita interoperabilidad entre componentes humanos e IA.

## 2. Estructura y criterios
- `Corpus_Platform_V4.md`: corpus global con metadatos y crossrefs.
- Cada nuevo archivo debe incluir cabecera YAML v4 y referencias cruzadas obligatorias.
- Organizar por ámbito o sistema integrado, manteniendo versionado semántico.

## 3. Naming y versionado
- `intg_{descripcion}_rw_b_v_3_1.md`
- Metadatos YAML y OutputTemplate obligatorios para cada archivo.

## 4. Crossref obligatoria
- [README library/](../readme_library_rw_b_v_3_1.md)
- [Blueprint v4](../../lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md)
- [Master Plan v4](../../lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md)
- [Prompt Codex Baseline v4](../../lifecycle/temp/prompt_codex_baseline_v_4_check.md)
- [Ruleset Coding Compliance v4](../../core/rulset/RULE_CODING_COMPLIANCE_V4.md)

## 5. Buenas prácticas y lessons learned
- Registrar cada integración con contexto, versión y enlaces de origen.
- Mantener actualizados los crossrefs para evitar drift entre buckets.
- Validar compatibilidad de licencias y datos antes de incorporar nuevos corpus.

---
**FIN README — intg/**

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

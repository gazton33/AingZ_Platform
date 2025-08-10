---
CODE: LIBRA
ID: readme_library_normas_rw_b_v_3_1_v4
VERSION: v4.0-2025-08-10
ROUTE: library/normas/readme_library_normas_rw_b_v_3_1.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# 📑 README — Subcarpeta `normas/` (RwB v3.1)

## 1. Rol y propósito
Subcarpeta dedicada a la gestión y trazabilidad de **normas técnicas, estándares y reglamentos** aplicables a los proyectos y workflows RwB.

## 2. Estructura y criterios
- Ingresar únicamente normas completas y oficiales (ISO, IRAM, UNE, etc.).
- Incluir metadatos mínimos: nombre, organización emisora, año, versión, referencia oficial, licencia.
- Formatos: PDF (preferido), TXT (solo si es permitido).

## 3. Naming y versionado
- `norma_{nombre}_org_año_ver_rw_b_v_3_1.pdf`
- Mantener tabla de normas y fuentes en README.

## 4. Crossref obligatoria
- [README library/](../readme_library_rw_b_v_3_1.md)
- [Blueprint v3](../../../blueprint_rw_b_platform_v_3_20250803.md)
- [Checklist Root](../../../checklist_root_rw_b_v_3_20250805.md)

## 5. Buenas prácticas y lessons learned
- Verificar autenticidad y vigencia de la norma antes de registrar.
- Documentar cambios de versión, traducciones, derogaciones y equivalencias.
- Registrar uso e integración en workflows y assets dependientes.

## 6. Tabla de normas (ejemplo)

| Nombre        | Organización | Año | Versión | Ref. Oficial | Licencia | Estado |
|---------------|--------------|-----|---------|--------------|----------|--------|
| ISO 9001      | ISO          | 2015| 1.0     | ISO9001:2015 | Oficial  | ✅     |
| IRAM 45001    | IRAM         | 2018| 2.1     | IRAM45001    | Académico| ✅     |

---
**FIN README — normas/**

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

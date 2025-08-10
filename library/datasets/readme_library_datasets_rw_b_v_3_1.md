---
CODE: LIBRA
ID: readme_library_datasets_rw_b_v_3_1_v4
VERSION: v4.0-2025-08-10
ROUTE: library/datasets/readme_library_datasets_rw_b_v_3_1.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# 📊 README — Subcarpeta `datasets/` (RwB v3.1)

## 1. Rol y propósito
Subcarpeta destinada a la gestión, trazabilidad y versionado de **datasets** utilizados en entrenamiento, análisis y workflows IA/humano.

## 2. Estructura y criterios
- Almacenar datasets originales, autorizados o generados en proyectos RwB.
- Metadatos mínimos: nombre, fuente, fecha de obtención, formato, licencia, uso previsto.
- Formatos aceptados: CSV, JSON, XLSX, TXT, otros estructurados.

## 3. Naming y versionado
- `dataset_{nombre}_fuente_fecha_rw_b_v_3_1.csv`
- Tabla de datasets, versiones y uso en README.

## 4. Crossref obligatoria
- [README library/](../readme_library_rw_b_v_3_1.md)
- [Blueprint v3](../../../blueprint_rw_b_platform_v_3_20250803.md)
- [Checklist Root](../../../checklist_root_rw_b_v_3_20250805.md)

## 5. Buenas prácticas y lessons learned
- Documentar licencia y restricciones de uso en cada dataset.
- Registrar cambios, preprocesados, limpieza o splits en README.
- Auditar compatibilidad y trazabilidad antes de incorporar a pipelines.

## 6. Tabla de datasets (ejemplo)

| Nombre         | Fuente         | Fecha      | Formato | Licencia        | Uso          | Estado |
|----------------|---------------|------------|---------|-----------------|--------------|--------|
| Text8          | Wikipedia     | 2022-09-15 | TXT     | Open            | NLP Train    | ✅     |
| HydraulicsData | HidroLab      | 2023-01-10 | CSV     | Académico       | Engineering  | ✅     |

---
**FIN README — datasets/**

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

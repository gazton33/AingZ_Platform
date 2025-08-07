---
file: readme_library_datasets_rw_b_v_3_1.md
version: v3.1-2025-08-05
status: active
role: readme
owner: AingZ_Platform · RwB
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


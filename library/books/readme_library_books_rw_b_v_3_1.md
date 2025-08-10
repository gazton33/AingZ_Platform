---
CODE: LIBRA
ID: readme_library_books_rw_b_v_3_1_v4
VERSION: v4.0-2025-08-10
ROUTE: library/books/readme_library_books_rw_b_v_3_1.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# 📚 README — Subcarpeta `books/` (RwB v3.1)

## 1. Rol y propósito
Subcarpeta dedicada al almacenamiento, organización y versionado de **libros y obras de referencia** relevantes para los dominios de la plataforma.

## 2. Estructura y criterios
- Almacenar únicamente libros completos, digitalizados o en acceso autorizado.
- Incluir metadatos mínimos: título, autor, año, edición, fuente/origen, licencia.
- Usar formatos PDF, EPUB, TXT u otros estandarizados.

## 3. Naming y versionado
- `book_{titulo}_autor_año_{ed}_rw_b_v_3_1.pdf`
- Documentar versiones, cambios y fuentes en README.

## 4. Crossref obligatoria
- [README library/](../readme_library_rw_b_v_3_1.md)
- [Blueprint v3](../../../blueprint_rw_b_platform_v_3_20250803.md)
- [Checklist Root](../../../checklist_root_rw_b_v_3_20250805.md)

## 5. Buenas prácticas y lessons learned
- Verificar integridad del archivo y derechos de uso antes de subir.
- Actualizar tabla de libros y metadatos en README tras cada alta/baja.
- Documentar excepciones, cambios de formato o licencias especiales.

## 6. Tabla de libros (ejemplo)

| Título                     | Autor           | Año | Edición | Formato | Licencia         | Estado   |
|---------------------------|-----------------|-----|---------|---------|------------------|----------|
| Ingeniería de Software    | Sommerville     | 2020| 10ª     | PDF     | Educational Use  | ✅       |
| The Art of Computer Prog. | D. Knuth        | 2011| 3ª      | PDF     | Personal/Academ. | ✅       |

---
**FIN README — books/**

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

---
CODE: DOC
ID: readme_core_doc_template_rw_b_v_3_2_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/core/doc/template/readme_core_doc_template_rw_b_v_3_2.md
CROSSREF:
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# 📑 core/doc/template/ — Plantillas Modelo de Documentación (v3.2)

## 1. Descripción, función, objetivos y contexto

La carpeta `core/doc/template/` centraliza **todas las plantillas modelo de documentación** utilizadas para generar, estandarizar y actualizar los assets documentales del core AingZ/RwB.

### Funciones principales:

- Almacenar modelos y scaffolds para la documentación específica del core (guías, reportes, onboarding, instructivos, etc.).
- Facilitar la generación y actualización rápida de docs bajo políticas de compliance, naming y versionado.
- Asegurar la consistencia y trazabilidad en todos los documentos generados internamente.

### Integraciones y sistemas relacionados:

- Referencia cruzada con templates universales de `ops/templates/` y plantillas estructurales de `data/template/`.
- Usadas en workflows, reporting y onboarding desde `doc/` y `wf/`.

## 2. Estructura interna

| Archivo/Subcarpeta         | Propósito                          | Estado |
| -------------------------- | ---------------------------------- | ------ |
| plantilla\_guia\_doc.md    | Scaffold/modelo de guía/documento  | Activo |
| plantilla\_reporte\_doc.md | Scaffold/modelo de reporte técnico | Activo |
| ...                        | Otras plantillas modelo de docs    | Activo |

## 3. Metadatos y compliance

- **Versión:** v3.2 — 2025-08-06
- **Owner/Responsable:** AingZ\_Platform · RwB
- **Crossref obligatoria:** Blueprint, master plan, checklist, template universal README (ops/templates/)
- **Naming/Versionado:** Cumplimiento estricto de políticas RwB v3.2
- **Estado:** Activo

## 4. Ciclo de vida y flujos

```mermaid
graph TD;
  A[Creación/update de plantilla] --> B[Validación compliance y naming]
  B --> C[Crossref en README y checklist]
  C --> D[Uso en docs internos y reporting]
  D --> E[Lessons learned y cierre de ciclo]
```

## 5. Changelog local

- 2025-08-06: Versión v3.2, compliance plantillas docs.

## 6. Observaciones / Lessons learned

- Mantener solo plantillas modelo para docs del core (el resto en ops/templates/).
- Sincronizar naming, versión y metadatos con cambios en políticas y rulesets.

---

**FIN README core/doc/template/ v3.2**

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

---
file: readme_core_wf_rw_b_v_3_2.md
version: v3.2-2025-08-06
status: active
role: readme
owner: AingZ_Platform · RwB
crossref:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
  - core/kns/glossary/rw_b_glosario_code_v_2_20250729.md
  - core/data/dicts/rw_b_diccionario_code_triggers_v_2_20250729.md
  - ops/templates/template_readme_rw_b_v_4.md
changelog:
  - 2025-08-06: Consolidación árbol y README wf/ core v3.2, integración de workflows y compliance.
---
# 🔄 core/wf/ — Workflows, Auditorías y Macroprocesos Operativos (v3.2)

## 1. Descripción, función, objetivos y contexto

La carpeta `core/wf/` centraliza **todos los workflows activos, auditorías y macroprocesos operativos** de la plataforma AingZ/RwB.

### Funciones principales:

- Definir y documentar todos los flujos de trabajo críticos (auditorías, migraciones, relevamientos, macro tareas) que rigen la evolución del core y la plataforma.
- Asegurar trazabilidad, compliance y registro incremental de acciones, auditorías y migraciones.
- Facilitar la automatización y revisión sistemática de procesos (PDCA, validación y consolidación de activos).
- Integrar con pipelines de `ops/` para logging, testeo, automatización y reporting continuo.

### Integraciones y sistemas relacionados:

- Interconexión directa con assets de `data/` (matrices, reglas, diccionarios) y contextos de `kns/` (glosario, checkpoints, métricas).
- Vinculación con documentación de `doc/` para guías, onboarding y reporting de workflows.
- Crossref a blueprint, master plan y checklist para garantizar alineación y compliance.

## 2. Estructura interna

| Subcarpeta / Archivo | Propósito                                   | Estado |
| -------------------- | ------------------------------------------- | ------ |
| audt/                | Auditorías de estructura, compliance y PDCA | Activo |
| mig\_cons/           | Migraciones y consolidaciones de activos    | Activo |
| relv/                | Relevamientos, inventarios, registros       | Activo |
| tareas\_acciones/    | Macro tareas, acciones y seguimiento        | Activo |

## 3. Metadatos y compliance

- **Versión:** v3.2 — 2025-08-06
- **Owner/Responsable:** AingZ\_Platform · RwB
- **Crossref obligatoria:** Blueprint, master plan, checklist, triggers, glosario, template universal README (ops/templates/)
- **Naming/Versionado:** Cumplimiento estricto de políticas RwB v3.2
- **Estado:** Activo

## 4. Ciclo de vida y flujos

```mermaid
graph TD;
  A[Definición de workflow] --> B[Validación compliance y naming]
  B --> C[Ejecución y logging]
  C --> D[Auditoría y reporting]
  D --> E[Lessons learned y mejora continua]
```

## 5. Changelog local

- 2025-08-06: Versión v3.2, integración workflows y ajuste compliance Master Plan.

## 6. Observaciones / Lessons learned

- Todo workflow debe tener ciclo PDCA documentado y trazabilidad de auditoría.
- No integrar workflows legacy sin revisión y registro de compliance.

---

**FIN README core/wf/ v3.2**


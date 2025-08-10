---
CODE: CORE
ID: readme_core_kns_chkp_rw_b_v_3_2_v4
VERSION: v4.0-2025-08-10
ROUTE: core/kns/chkp/readme_core_kns_chkp_rw_b_v_3_2.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# ✅ core/kns/chkp/ — Checkpoints y Snapshots de Plataforma/Proyectos (v3.2)

## 1. Descripción, función, objetivos y contexto

La carpeta `core/kns/chkp/` centraliza **todos los checkpoints, snapshots y estados de avance** tanto de la plataforma global como de cada proyecto/ramas en la plataforma AingZ/RwB.

### Funciones principales:

- Almacenar snapshots de estados, avances y releases de plataforma y proyectos clave.
- Facilitar rollback, auditoría, validación y consolidación de cambios en cualquier nivel del core.
- Garantizar trazabilidad y control incremental del contexto vivo y releases de activos críticos.

### Integraciones y sistemas relacionados:

- Crossref con lessons, reporting y migraciones (`ai_learn/`, `wf/`).
- Checkpoints documentados alimentan auditoría, onboarding y mejora continua a nivel plataforma/proyectos.

## 2. Estructura interna

| Subcarpeta/Archivo | Propósito                              | Estado |
| ------------------ | -------------------------------------- | ------ |
| aingz\_platform/   | Checkpoints y snapshots globales       | Activo |
| projects/          | Checkpoints por proyecto/ramas         | Activo |
| ...                | Otros snapshots/checkpoints relevantes | Activo |

## 3. Metadatos y compliance

- **Versión:** v3.2 — 2025-08-06
- **Owner/Responsable:** AingZ\_Platform · RwB
- **Crossref obligatoria:** Blueprint, master plan, checklist, template universal README (ops/templates/)
- **Naming/Versionado:** Cumplimiento estricto de políticas RwB v3.2
- **Estado:** Activo

## 4. Ciclo de vida y flujos

```mermaid
graph TD;
  A[Ingreso/update de checkpoint/snapshot] --> B[Validación compliance y naming]
  B --> C[Crossref en README, auditoría y checklist]
  C --> D[Análisis, rollback y lessons]
  D --> E[Lessons learned y cierre de ciclo]
```

## 5. Changelog local

- 2025-08-06: Versión v3.2, compliance checkpoints de plataforma y proyectos.

## 6. Observaciones / Lessons learned

- Todos los checkpoints deben estar versionados y trazables, listos para rollback y auditoría.
- Mantener sincronización incremental y crossref con lessons, reporting y migraciones.

---

**FIN README core/kns/chkp/ v3.2**

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

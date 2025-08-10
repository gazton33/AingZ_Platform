---
CODE: SNAPS
ID: snapshots_ctx_codex_readme_v_3_1_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/snapshots_ctx/codex/snapshots_ctx_codex_readme_v_3_1.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
## Índice

1. [Descripción General](#1-descripción-general)
2. [Estructura Interna](#2-estructura-interna)
3. [Cross‑References](#3-cross-references)
4. [Flujos & Workflows](#4-flujos--workflows)
5. [Compliance & Buenas Prácticas](#5-compliance--buenas-practicas)
6. [Changelog](#6-changelog)
7. [Metadatos IA](#7-metadatos-ia)

---

## 1. Descripción General

Bucket principal para almacenamiento y versionado de snapshots de contexto, dumps de sesión (IA/humanos), backups temporales y registros de evolución de contexto global. Permite trazabilidad total para debugging, auditoría, rollback o análisis forense.

---

## 2. Estructura Interna

| Path       | Rol        | Descripción breve                        |
| ---------- | ---------- | ---------------------------------------- |
| ./         | Contenedor | README + metadatos                       |
| common/    | Common     | Snapshots y dumps genéricos o cruzados   |
| gpt\_4\_1/ | GPT-4.1    | Snapshots de sesiones IA GPT-4.1         |
| gpt\_4o/   | GPT-4o     | Snapshots de sesiones IA GPT-4o          |
| gpt\_o3/   | GPT-o3     | Snapshots de sesiones IA GPT-o3          |
| codex/     | Codex      | Snapshots, dumps y sesiones OpenAI Codex |

---

## 3. Cross‑References

- **Blueprint v3** → [`../../lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md`](../../lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md)
- **Master Plan v3** → [`../../lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md`](../../lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md)
- **Checklist Root v3** → [`../checklist_root_rw_b_v_3_20250803.md`](../checklist_root_rw_b_v_3_20250803.md)
- **Triggers**: `TRG_AUDIT_LEGACY`, `TRG_PURGE_AI`

---

## 4. Flujos & Workflows

```mermaid
flowchart TD
  SNAP[Generar snapshot] --> REG[Registrar en bucket específico]
  REG --> AUDIT[Auditoría/QA]
  AUDIT --> USO[Uso para rollback, debug o análisis]
```

---

## 5. Compliance & Buenas Prácticas

- Mantener metadatos y changelog por snapshot/dump relevante.
- No eliminar ni sobrescribir snapshots sin doble validación y backup.
- Registrar triggers y referencias cruzadas para cada snapshot relevante.
- Snapshots Codex: registrar input/output, versión y contexto de ejecución para trazabilidad IA-código.

---

## 6. Changelog

| Fecha      | Versión | Autor       | Cambios                                         |
| ---------- | ------- | ----------- | ----------------------------------------------- |
| 2025-08-05 | v3.1    | ChatGPT 4.1 | README inicial snapshots\_ctx/ enriched + Codex |

---

## 7. Metadatos IA

```yaml
bucket: snapshots_ctx
version: v3.1
updated: 2025-08-05
blueprint_ref: ../../lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
master_plan_ref: ../../lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
triggers:
  - TRG_AUDIT_LEGACY
  - TRG_PURGE_AI
```

---

**FIN README snapshots\_ctx/ v3.1**

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

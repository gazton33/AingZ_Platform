---
CODE: SNAPS
ID: snapshots_ctx_gpt_4_o_readme_v_3_1_v4
VERSION: v4.0-2025-08-10
ROUTE: snapshots_ctx/gpt_4o/snapshots_ctx_gpt_4_o_readme_v_3_1.md
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
4. [Flujos y Buenas Prácticas](#4-flujos-y-buenas-practicas)
5. [Compliance & Changelog](#5-compliance--changelog)
6. [Metadatos IA](#6-metadatos-ia)

---

## 1. Descripción General

Repositorio específico para snapshots, dumps de contexto, logs y outputs generados en flujos de trabajo, sesiones interactivas y pruebas con el modelo IA GPT-4o (Omni). Permite trazabilidad, debugging, rollback y auditoría específica para este modelo y su integración multi-modal.

---

## 2. Estructura Interna

| Path | Rol        | Descripción breve                   |
| ---- | ---------- | ----------------------------------- |
| ./   | Contenedor | README + metadatos                  |
| \*   | Snapshot   | Snapshots, dumps y registros GPT-4o |

---

## 3. Cross‑References

- **Blueprint v3** → [`../../../blueprint_rw_b_platform_v_3_20250803.md`](../../../blueprint_rw_b_platform_v_3_20250803.md)
- **Master Plan v3** → [`../../../mpln_master_plan_rw_b_v_3_20250803.md`](../../../mpln_master_plan_rw_b_v_3_20250803.md)
- **Checklist Root v3** → [`../../../checklist_root_rw_b_v_3_20250803.md`](../../../checklist_root_rw_b_v_3_20250803.md)
- **Triggers**: `TRG_AUDIT_LEGACY`, `TRG_PURGE_AI`

---

## 4. Flujos y Buenas Prácticas

- Documentar fecha, usuario, prompt, contexto y objetivo de cada snapshot.
- Identificar tipo de input/output (texto, voz, imagen, código, etc.) para trazabilidad multi-modal.
- No eliminar ni sobreescribir dumps críticos sin registro y backup previo.

---

## 5. Compliance & Changelog

| Área    | Regla                 | Fuente         |
| ------- | --------------------- | -------------- |
| Naming  | `naming_universal_v3` | Blueprint §2.2 |
| Context | Trazabilidad total    | Master Plan §3 |

| Fecha      | Versión | Autor       | Cambios                          |
| ---------- | ------- | ----------- | -------------------------------- |
| 2025-08-05 | v3.1    | ChatGPT 4.1 | README inicial gpt\_4o/ enriched |

---

## 6. Metadatos IA

```yaml
bucket: snapshots_ctx/gpt_4o
version: v3.1
updated: 2025-08-05
blueprint_ref: ../../../blueprint_rw_b_platform_v_3_20250803.md
master_plan_ref: ../../../mpln_master_plan_rw_b_v_3_20250803.md
triggers:
  - TRG_AUDIT_LEGACY
  - TRG_PURGE_AI
```

---

**FIN README snapshots\_ctx/gpt\_4o/ v3.1**

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

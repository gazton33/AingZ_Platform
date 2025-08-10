---
CODE: LIFEC
ID: lifecycle_temp_readme_v_3_1_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/temp/lifecycle_temp_readme_v_3_1.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# [RwB] lifecycle/temp/ — README (v3.1)

> **Tagline:** Staging temporal, pruebas y assets en tránsito; zona segura para activos a validar o transformar antes de migrar a core o descarte.

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

Carpeta para staging temporal de activos en proceso de auditoría, validación, edición o transformación. Todo archivo aquí es transitorio y debe tener registro de propósito, fecha de ingreso y acción pendiente.

---

## 2. Estructura Interna

| Path     | Rol      | Descripción breve                           |
| -------- | -------- | ------------------------------------------ |
| ./       | Contenedor | README + metadatos                        |
| *        | Temp     | Activos temporales, scripts o snapshots     |

---

## 3. Cross‑References

- **Blueprint v3** → [`../../../blueprint_rw_b_platform_v_3_20250803.md`](../../../blueprint_rw_b_platform_v_3_20250803.md)
- **Master Plan v3** → [`../../../mpln_master_plan_rw_b_v_3_20250803.md`](../../../mpln_master_plan_rw_b_v_3_20250803.md)
- **Checklist Root v3** → [`../../../checklist_root_rw_b_v_3_20250803.md`](../../../checklist_root_rw_b_v_3_20250803.md)
- **Triggers**: `TRG_AUDIT_LEGACY`, `TRG_CONSOLIDATE_TL`

---

## 4. Flujos y Buenas Prácticas
- Registrar propósito y vencimiento de cada asset temporal.
- Eliminar o migrar assets apenas termine la validación o prueba.
- Evitar acumulación de “basura” digital fuera de ciclo de vida planificado.

---

## 5. Compliance & Changelog

| Área    | Regla                  | Fuente         |
| ------- | ---------------------- | -------------- |
| Naming  | `naming_universal_v3`  | Blueprint §2.2 |
| Temp    | Eliminación obligatoria| Master Plan §3 |

| Fecha      | Versión | Autor       | Cambios                        |
| ---------- | ------- | ----------- | ------------------------------ |
| 2025-08-05 | v3.1    | ChatGPT 4.1 | README inicial temp/ enriched  |

---

## 6. Metadatos IA
```yaml
bucket: lifecycle/temp
version: v3.1
updated: 2025-08-05
blueprint_ref: ../../../blueprint_rw_b_platform_v_3_20250803.md
master_plan_ref: ../../../mpln_master_plan_rw_b_v_3_20250803.md
triggers:
  - TRG_AUDIT_LEGACY
  - TRG_CONSOLIDATE_TL
```

---

**FIN README lifecycle/temp/ v3.1**

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

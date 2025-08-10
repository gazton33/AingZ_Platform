---
CODE: LIFEC
ID: lifecycle_bk_temp_readme_v_3_1_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/bk_temp/lifecycle_bk_temp_readme_v_3_1.md
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

Carpeta para staging temporal de backups críticos, snapshots y respaldos de workflows, assets y datos sensibles. Aquí se validan, versionan y resguardan los archivos antes de su integración final o eliminación planificada según blueprint y ciclo PDCA.

---

## 2. Estructura Interna

| Path | Rol        | Descripción breve                          |
| ---- | ---------- | ------------------------------------------ |
| ./   | Contenedor | README + metadatos                         |
| \*   | Backup     | Backups, snapshots y resguardos temporales |

---

## 3. Cross‑References

- **Blueprint v3** → [`../temp/rw_b_blueprint_v_4_extendido_2025_08_06.md`](../temp/rw_b_blueprint_v_4_extendido_2025_08_06.md)
- **Master Plan v3** → [`../temp/rw_b_master_plan_v_4_extendido_2025_08_06.md`](../temp/rw_b_master_plan_v_4_extendido_2025_08_06.md)
- **Checklist Root v3** → [`../../../checklist_root_rw_b_v_3_20250803.md`](../../../checklist_root_rw_b_v_3_20250803.md)
- **Triggers**: `TRG_AUDIT_LEGACY`, `TRG_PURGE_AI`

---

## 4. Flujos y Buenas Prácticas

- Registrar origen, fecha y motivo de cada backup.
- No mantener backups fuera del ciclo de validación o sin responsable designado.
- Respetar políticas de retención y eliminación segura según compliance.

---

## 5. Compliance & Changelog

| Área   | Regla                  | Fuente         |
| ------ | ---------------------- | -------------- |
| Naming | `naming_universal_v3`  | Blueprint §2.2 |
| Backup | Validación obligatoria | Master Plan §3 |

| Fecha      | Versión | Autor       | Cambios                           |
| ---------- | ------- | ----------- | --------------------------------- |
| 2025-08-05 | v3.1    | ChatGPT 4.1 | README inicial bk\_temp/ enriched |

---

## 6. Metadatos IA

```yaml
bucket: lifecycle/bk_temp
version: v3.1
updated: 2025-08-05
blueprint_ref: ../temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
master_plan_ref: ../temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
triggers:
  - TRG_AUDIT_LEGACY
  - TRG_PURGE_AI
```

---

**FIN README lifecycle/bk\_temp/ v3.1**

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

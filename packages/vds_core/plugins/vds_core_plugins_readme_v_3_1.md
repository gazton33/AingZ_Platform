---
CODE: PACKA
ID: vds_core_plugins_readme_v_3_1_v4
VERSION: v4.0-2025-08-10
ROUTE: packages/vds_core/plugins/vds_core_plugins_readme_v_3_1.md
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
4. [Política y Buenas Prácticas](#4-politica-y-buenas-practicas)
5. [Quick Start / Futuras Integraciones](#5-quick-start--futuras-integraciones)
6. [Compliance & Governance](#6-compliance--governance)
7. [Changelog](#7-changelog)
8. [Metadatos IA](#8-metadatos-ia)

---

## 1. Descripción General

Carpeta destinada a alojar plugins autocontenidos de la plataforma: cada subcarpeta será un procedimiento o microservicio especializado (e.g. relevamientos, inventario, organizador, etc). Los plugins pueden ser escalados a packages independientes según crecimiento, siempre bajo compliance RwB.

---

## 2. Estructura Interna

| Path           | Rol        | Descripción breve                                        |
| -------------- | ---------- | -------------------------------------------------------- |
| ./             | Contenedor | README + metadatos                                       |
| relevamientos/ | Plugin     | Procedimientos de relevamiento de datos y activos        |
| inventario/    | Plugin     | Inventario y tracking de activos                         |
| organizador/   | Plugin     | Organización y agrupamiento de assets                    |
| ...otros/      | Plugin     | Plugins futuros, cada uno con su README y assets propios |

> **Nota:** Este README solo documenta la estructura general y reglas; cada plugin tendrá su propio README y docs cuando sea consolidado.

---

## 3. Cross‑References

- **Blueprint v3** → [`../../../blueprint_rw_b_platform_v_3_20250803.md`](../../../blueprint_rw_b_platform_v_3_20250803.md)
- **Master Plan v3** → [`../../../mpln_master_plan_rw_b_v_3_20250803.md`](../../../mpln_master_plan_rw_b_v_3_20250803.md)
- **Checklist Root v3** → [`../../../checklist_root_rw_b_v_3_20250803.md`](../../../checklist_root_rw_b_v_3_20250803.md)
- **Core README** → [`../README.md`](../README.md)

---

## 4. Política y Buenas Prácticas

- Cada plugin debe estar autocontenido: scripts, docs, assets y testing propios.
- Naming y estructura deben seguir blueprint v3 y compliance RwB.
- No agregar lógica ni carpetas fuera de la estructura documentada.
- Cuando un plugin esté consolidado, crear README propio con su estructura y quickstart.

---

## 5. Quick Start / Futuras Integraciones

- Para integrar o desarrollar un plugin: crear subcarpeta bajo `/plugins/`, iniciar README y seguir políticas blueprint.
- Cada plugin puede ser migrado a package independiente según necesidad de escalado o versionado.

---

## 6. Compliance & Governance

| Área    | Regla                 | Fuente         |
| ------- | --------------------- | -------------- |
| Naming  | `naming_universal_v3` | Blueprint §2.2 |
| Plugins | Autocontenidos        | Master Plan §3 |

---

## 7. Changelog

| Fecha      | Versión | Autor       | Cambios                          |
| ---------- | ------- | ----------- | -------------------------------- |
| 2025-08-05 | v3.1    | ChatGPT 4.1 | README inicial plugins/ enriched |

---

## 8. Metadatos IA

```yaml
bucket: packages/vds_core/plugins
version: v3.1
updated: 2025-08-05
blueprint_ref: ../../../blueprint_rw_b_platform_v_3_20250803.md
master_plan_ref: ../../../mpln_master_plan_rw_b_v_3_20250803.md
triggers:
  - TRG_AUDIT_LEGACY
  - TRG_CONSOLIDATE_TL
  - TRG_PURGE_AI
```

---

**FIN README packages/vds\_core/plugins/ v3.1**

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

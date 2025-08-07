---

## file: README.md version: v3.1-2025-08-05 bucket: lifecycle/legacy blueprint: ../../../blueprint\_rw\_b\_platform\_v\_3\_20250803.md status: active updated: 2025-08-05 role: documentation owner: AingZ\_Platform · RwB

# [RwB] lifecycle/legacy/ — README (v3.1)

> **Tagline:** Almacén controlado de activos legacy: staging seguro para archivos, datos y scripts previos a migración o descarte definitivo.

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

Carpeta para staging de activos heredados o desfasados, en espera de auditoría, migración a core/ o descarte definitivo. Todos los archivos deben mantener registro de origen, fecha, motivo de paso a legacy y estado.

---

## 2. Estructura Interna

| Path | Rol        | Descripción breve                    |
| ---- | ---------- | ------------------------------------ |
| ./   | Contenedor | README + metadatos                   |
| \*   | Legacy     | Archivos/datos/snapshots en revisión |

---

## 3. Cross‑References

- **Blueprint v3** → [`../../../blueprint_rw_b_platform_v_3_20250803.md`](../../../blueprint_rw_b_platform_v_3_20250803.md)
- **Master Plan v3** → [`../../../mpln_master_plan_rw_b_v_3_20250803.md`](../../../mpln_master_plan_rw_b_v_3_20250803.md)
- **Checklist Root v3** → [`../../../checklist_root_rw_b_v_3_20250803.md`](../../../checklist_root_rw_b_v_3_20250803.md)
- **Triggers**: `TRG_AUDIT_LEGACY`, `TRG_PURGE_AI`

---

## 4. Flujos y Buenas Prácticas

- Auditar activos legacy antes de cualquier migración.
- Documentar estado de cada archivo (origen, fecha, acción pendiente).
- No mantener activos sin registrar o sin metadatos.

---

## 5. Compliance & Changelog

| Área   | Regla                 | Fuente         |
| ------ | --------------------- | -------------- |
| Naming | `naming_universal_v3` | Blueprint §2.2 |
| Legacy | Audit obligatorio     | Master Plan §3 |

| Fecha      | Versión | Autor       | Cambios                         |
| ---------- | ------- | ----------- | ------------------------------- |
| 2025-08-05 | v3.1    | ChatGPT 4.1 | README inicial legacy/ enriched |

---

## 6. Metadatos IA

```yaml
bucket: lifecycle/legacy
version: v3.1
updated: 2025-08-05
blueprint_ref: ../../../blueprint_rw_b_platform_v_3_20250803.md
master_plan_ref: ../../../mpln_master_plan_rw_b_v_3_20250803.md
triggers:
  - TRG_AUDIT_LEGACY
  - TRG_PURGE_AI
```

---

**FIN README lifecycle/legacy/ v3.1**


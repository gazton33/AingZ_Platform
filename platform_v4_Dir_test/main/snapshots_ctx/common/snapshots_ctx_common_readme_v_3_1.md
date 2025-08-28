---

## file: README.md version: v3.1-2025-08-05 bucket: snapshots\_ctx/common blueprint: ../../../blueprint\_rw\_b\_platform\_v\_3\_20250803.md status: active updated: 2025-08-05 role: documentation owner: AingZ\_Platform · RwB

# [RwB] snapshots\_ctx/common/ — README (v3.1)

> **Tagline:** Snapshots y dumps de contexto comunes, multi-modelo o multi-sesión; referencia central para IA/humano y flujos cruzados.

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

Espacio centralizado para snapshots, dumps y registros de contexto generados en flujos multi-modelo, sesiones mixtas IA/humano o procesos que requieren persistencia transversal a distintos contextos. Permite debugging, análisis y rollback general.

---

## 2. Estructura Interna

| Path | Rol        | Descripción breve                           |
| ---- | ---------- | ------------------------------------------- |
| ./   | Contenedor | README + metadatos                          |
| \*   | Snapshot   | Archivos de snapshot comunes/multi-contexto |

---

## 3. Cross‑References

- **Blueprint v3** → [`../../../blueprint_rw_b_platform_v_3_20250803.md`](../../../blueprint_rw_b_platform_v_3_20250803.md)
- **Master Plan v3** → [`../../../mpln_master_plan_rw_b_v_3_20250803.md`](../../../mpln_master_plan_rw_b_v_3_20250803.md)
- **Checklist Root v3** → [`../../../checklist_root_rw_b_v_3_20250803.md`](../../../checklist_root_rw_b_v_3_20250803.md)
- **Triggers**: `TRG_AUDIT_LEGACY`, `TRG_PURGE_AI`

---

## 4. Flujos y Buenas Prácticas

- Documentar modelo/sesión/origen de cada snapshot.
- Mantener registros claros para debugging y análisis transversal.
- Evitar duplicidad o pérdida de contexto en dumps críticos.

---

## 5. Compliance & Changelog

| Área    | Regla                 | Fuente         |
| ------- | --------------------- | -------------- |
| Naming  | `naming_universal_v3` | Blueprint §2.2 |
| Context | Registro obligatorio  | Master Plan §3 |

| Fecha      | Versión | Autor       | Cambios                         |
| ---------- | ------- | ----------- | ------------------------------- |
| 2025-08-05 | v3.1    | ChatGPT 4.1 | README inicial common/ enriched |

---

## 6. Metadatos IA

```yaml
bucket: snapshots_ctx/common
version: v3.1
updated: 2025-08-05
blueprint_ref: ../../../blueprint_rw_b_platform_v_3_20250803.md
master_plan_ref: ../../../mpln_master_plan_rw_b_v_3_20250803.md
triggers:
  - TRG_AUDIT_LEGACY
  - TRG_PURGE_AI
```

---

**FIN README snapshots\_ctx/common/ v3.1**


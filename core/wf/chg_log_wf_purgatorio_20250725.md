# CHG_LOG_WF_PURGATORIO_20250725.md — Changelog y bitácora de purga de versiones históricas de Workflows (WF)

---

## 1. Contexto
- En fecha 2025-07-25, se realizó un barrido y mapeo completo de todos los workflows (WF) de auditoría, migración, consolidación y relevamiento en el stack AingZ/RwB.
- Se detectaron y clasificaron versiones activas vs históricas (legacy) para limpieza del directorio `WF/` y organización en backup/PURGATORIO.

---

## 2. Archivos movidos a backup/PURGATORIO
- `rw_b_wf_consolidacion_files_activos_v_1_20250725.md` (backup legacy, superada por v2)
- `rw_b_wf_auditoria_legacy_v_2_20250724.md` (backup legacy, superada por v3)

---

## 3. Archivos activos/actuales (WF/)
- `rw_b_wf_consolidacion_files_activos_v_2_20250725.md`
- `rw_b_wf_auditoria_legacy_v_3_20250725.md`
- `wf_migracion_final_legacy_rw_b_v_1_20250725.md`
- `rw_b_wf_relevamiento_ideas_v_1.md`
- `rw_b_wf_auditoria_cierre_hilo_v_1_20250724.md`

---

## 4. Lessons learned y confirmación
- El control de versiones, naming y organización modular de workflows facilita la trazabilidad, la purga incremental y el onboarding futuro.
- Toda versión histórica debe quedar referenciada en el changelog y logs de consolidación/auditoría.
- Listo para avanzar con próximos ciclos usando solo las releases recomendadas y documentando lessons en memoria viva.

---


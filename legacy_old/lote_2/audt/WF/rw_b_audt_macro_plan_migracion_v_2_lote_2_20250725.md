# RwB_AUDT_MACRO_PLAN_MIGRACION_v2_LOTE2_20250725.md — Auditoría estructural legacy (Draft)

---

## 1. Propósito/contexto
Auditoría del macro-plan universal de migración (v2) para el stack AingZ_Repo. Documento matriz que define el pipeline, reglas y checkpoints de todo proceso migratorio/auditoría en el sistema.

---

## 2. Barrido literal selectivo y mapeo estructural
- **Bloques críticos:**
  - Pasos clave del macro-plan: clasificación de archivos, reordenamiento, auditoría legacy, adaptación/transformación, templateo, integración, feedback, cierre de ciclo, registro en logs y memoria viva.
  - Mapeo directo a workflows, templates, memoria viva y control de versiones.
  - Instrucciones para no migrar ni purgar legacy sin validación completa, review cruzada y lessons learned.
  - Checklist de readiness: logs, changelog, feedback y lessons completados antes de migración/fusión.
- **Mapeo glosario/estructura:**
  - Clase “MACROPLAN/MIGRACION”; función “pipeline central”, bloque “control/procedimiento universal”.
  - Referencias cruzadas a todos los workflows del repo y outputs de auditoría/migración.

---

## 3. Análisis de integración y mejoras
- El documento es “pivote” para cualquier ciclo migratorio o de auditoría; debe estar versionado y actualizado en la raíz del stack.
- Propuesta: Checklist universal para readiness antes de cualquier acción destructiva, linkeado desde cada template y output relevante.
- Sugerir subdirectorio “control/macroplan” con versión fija para revisión previa a cambios globales.

---

## 4. Checklist de cobertura y reproducibilidad (visual-friendly)
- Bloques críticos extraídos y mapeados: OK
- Referenciado a glosario y estructura “control/procedimiento”: OK
- Propuesta de checklist readiness universal: OK
- Feedback y lessons registered: OK
- Legacy original referenciado (rw_b_macro_plan_migracion_v_2.md): OK
- Auto-reproducible con legacy accesible: OK

---

## 5. Feedback, lessons learned, riesgos
- Si el macro-plan no se actualiza, cualquier migración posterior puede perder cobertura crítica o crear inconsistencias entre versiones.
- Propuesta: Instalar triggers automáticos para revisión de logs y lessons antes de permitir migración, y dejar aviso de deprecated sólo en macroplan, no en legacy.

---


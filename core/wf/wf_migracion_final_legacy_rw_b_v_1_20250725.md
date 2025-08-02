# WF_Migracion_Final_Legacy_RwB_v1_20250725.md

> Workflow literal y versionado para la tarea de migración final de legacy consolidada a la infraestructura definitiva (AingZ_Repo). Extensión del WF de auditoría, alineado a lessons y feedback recientes.

---

## 1. Objetivo
- Migrar, consolidar y actualizar todos los conocimientos, datos, matrices y visualizaciones de la legacy auditada en los 3 lotes a la nueva estructura definitiva del repositorio.
- Garantizar que no se pierda ningún insight, contexto, naming o aprendizaje relevante; solo eliminar la legacy/backups una vez migrado y validado.

---

## 2. Pipeline de la migración final

1. **Preparación**
   - Checklist de auditoría, outputs consolidados y revisión cruzada 100% completados.
   - Definir mapping de archivos legacy → estructura target (directorio, naming, versión).
   - Definir responsables de revisión/firma (humano + IA).
2. **Migración literal**
   - Acceso a backups/legacy originales.
   - Extraer información literal: datos, visualizaciones, metadatos, lessons y changelogs.
   - Adaptar formato a la nueva semántica/naming/contexto actual.
   - Volcar todo el contenido migrado en archivos target, estructurando en markdown y referenciando lessons y tags.
3. **Integración y revisión**
   - Validar que todos los datos, visuales y aprendizajes clave estén en los nuevos archivos.
   - Checklist de conformidad (coverage, trazabilidad, versionado, onboarding, compliance, lessons learned).
   - Revisión cruzada: detectar gaps, redundancias, insights no migrados o conflictos semánticos.
   - Ajustar archivos y estructura hasta cierre total de gaps.
4. **Cierre y purga de legacy**
   - Generar changelog de migración y lessons learned.
   - Solo tras validación 100%: marcar legacy/backups como obsoletos y proceder a eliminación segura.
   - Dejar registro referenciado del cierre, triggers, lessons y mejoras para ciclos futuros.

---

## 3. Lessons y recomendaciones activas
• Documentar triggers, insights y feedback de todo el ciclo
• No migrar “a ciegas” ni hacer purga sin revisión/firma
• Checklist y logs versionados deben quedar como referencia
• El output migrado debe ser auto-contenido y onboarding para todo el equipo

---

*Fin WF Migración Final Legacy RwB (v1).*


## Referencias
- [Changelog](../Learn/chglog/rw_b_chglog_v_2_20250724.md)

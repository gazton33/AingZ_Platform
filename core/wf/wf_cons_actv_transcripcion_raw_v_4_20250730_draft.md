# WF_CONS_ACTV_TRANSCRIPCION_RAW_v4 (2025-07-30)

> **STATUS:** `DRAFT·REVISION_PENDING`
>
> Workflow maestro para **consolidación y actualización de activos en desarrollo** (no legacy), fusionando nuevas versiones funcionales/QA con los activos base actuales. **No** orientado a migración de históricos/legacy; orientado a evolución, depuración y eliminación de archivos superados.

---

## 1. Objetivo
Consolidar versiones nuevas y activos en curso —README, MasterPlan, Changelog, matrices— con sus respectivas bases activas, garantizando:
- ÚNICO archivo ACTIVO por cada activo principal.
- Fusión literal/semántica y documentación de cada consolidación.
- Eliminación segura de archivos superados.
- Sin referencias ni dependencias de archivos obsoletos (salvo casos excepcionales justificados).

---

## 2. Alcance
- Aplica a la **evolución iterativa** de documentación, blueprints, workflows, QA/checklists, matrices, onboarding, etc.
- Se excluyen migraciones legacy e históricos.

---

## 3. Pipeline consolidación (v4)
1. **Identificación y selección de versiones**
   - Identificar todos los archivos en desarrollo + la versión ACTIVA actual.
   - Listar explícitamente rutas, nombres, versiones y propósito de cada ítem a consolidar.
2. **Fusión literal/semántica**
   - Integrar bloques, datos, matrices y secciones nuevas preservando lo vigente.
   - Resolver conflictos: prioridad a última versión funcional y feedback QA.
   - Evitar referencias a archivos viejos (TODO debe quedar auto-contenido).
3. **QA incremental**
   - Checklist de omisiones, duplicados, coherencia naming y versionado.
   - Validar rutas, índices, matrices y enlaces internos tras la consolidación.
4. **Actualización de logs y matriz**
   - Loguear la consolidación en el changelog y matriz central.
   - Documentar reglas y criterios aplicados en cada caso.
5. **Depuración final**
   - Eliminar, comprimir o mover a histórico todos los archivos superados.
   - Dejar en el repo sólo la versión ACTIVA final, más backups justificados.

---

## 4. Checklist operativo
- [ ] Todas las versiones a fusionar listadas y explicitadas.
- [ ] Backup previo automático/manual.
- [ ] Consolidación fusión literal/semántica aplicada.
- [ ] Revisión QA: sin duplicados, omisiones, referencias a archivos obsoletos.
- [ ] Logs, matriz y README actualizados.
- [ ] Repo limpio: solo ACTIVO/s y backups necesarios.

---

## 5. Outputs
- Único archivo `*_ACTIVO.md` por cada activo principal.
- Log actualizado, matriz y README referenciando solo activos.

---

## 6. Criterios de aceptación
- 100% de los archivos principales consolidados y auto-contenidos.
- No hay referencias a archivos previos (ni README, ni matrices, ni changelog, ni masterplan, ni docs).
- Integración documentada, logueada y QA pasada.

---

### Firma
> Gastón Zelechower · OpenAI o3 — Ruleset RWB Universal

---

**FIN WF_CONS_ACTV_TRANSCRIPCION_RAW_v4**


# [BARRIDO\_LITERAL] — Redefinición y semántica para la carpeta LEGACY

---

## 1. Concepto unificado de LEGACY

> **LEGACY** es el *único bucket de staging obligatorio para todo documento o archivo antiguo, externo u oficial, independientemente de su origen*, que aún no cumple con los estándares actuales de naming, metadata, estructura, semántica y trazabilidad RwB.

- **Función:**
  - *Zona de cuarentena controlada*.
  - Cada documento aquí requiere procesamiento, transformación o curaduría antes de pasar al ciclo de vida activo.
- **Criterios de ingreso:**
  - Origen irrelevante: puede ser propio (v1, drafts viejos), externo, oficial, PDF, digitalización de papel, etc.
  - No cumple naming/estructura/metadata RwB.
  - Requiere análisis, clasificación, transformación, versionado, mapeo y/o enriquecimiento.

---

## 2. Semántica y reglas para LEGACY

- **Ubicación física**:
  - `/PURGATORIO/LEGACY/` (v4 actual), pero podría moverse a `/MAIN/LEGACY/` en la estructura CORE si se revalida en blueprint final.
- **Naming de archivos:**
  - **Sin modificar** hasta ser procesados. Pueden mantener el nombre de origen, pero se registran en mapping y logbook.
  - Al pasar a activos: **obligatorio naming **``** + versión/documentación RwB**.
- **Metadata de entrada (opcional pero recomendado):**
  - Registrar fuente, fecha de ingreso a LEGACY, estado de procesamiento, responsable de curaduría y mapeo destino previsto.
- **Referencia cruzada:**
  - Cada archivo legacy debe tener una entrada en el **registro de trazabilidad** y estar listado para integración según los workflows de auditoría y migración.
- **Estado:**
  - Todo archivo en LEGACY es considerado **pendiente**, **inseguro** y **no usable** en workflows activos, hasta ser procesado.
- **Workflows aplicables:**
  - Auditoría, migración, mapeo, consolidación, transformación, QA y validación cruzada.

---

## 3. Ciclo de vida literal de un archivo en LEGACY

1. **Ingreso** a `/PURGATORIO/LEGACY/`\
   → Registrar en mapping/bitácora.
2. **Auditoría y análisis** inicial (mapeo, clasificación, detección de gaps, definición de destino).
3. **Procesamiento/transición:**
   - Renombrar y enriquecer metadata según glosario y Matrix.
   - Adaptar a formato/documentación/naming activo.
   - Validar con checklist QA y workflows.
4. **Consolidación:**
   - Mover a carpeta definitiva según su nueva función.
   - Actualizar logs, changelog y matriz.
5. **Purga de original:**
   - Solo tras validación y referencia cruzada, eliminar o archivar original (mantener solo si legal/histórico lo exige).

---

## 4. Semántica y sugerencias para documentación

- **README de LEGACY:**
  - Explicar literalmente: "TODO archivo aquí es *pre-integración*, pendiente de procesamiento. NO es activo ni referencia válida hasta ser migrado/curado."
  - Checklist: ¿Está registrado? ¿Tiene mapping? ¿Fue procesado? ¿Destino definido?
- **Workflow visible:**
  - Indicar pasos para curaduría, triggers y responsables.
- **Tags/estado:**
  - `STA=PENDING` hasta migrar; luego `STA=ACTV/BACKUP/PURG` según ciclo.

---

## 5. Ejemplo visual de ciclo LEGACY

```mermaid
flowchart TD
    A[Ingreso archivo antiguo (cualquier fuente)] --> B[Ubicación en /PURGATORIO/LEGACY/]
    B --> C[Registro en mapping y logbook]
    C --> D[Auditoría y mapeo destino]
    D --> E[Procesamiento/renombrado/nuevo formato]
    E --> F[QA y validación]
    F --> G[Migración a carpeta definitiva (asset/data/doc/etc.)]
    G --> H[Actualizar logs/changelog/matriz]
    H --> I[Purga/eliminación/archivo original]
```

---

## 6. Ventajas del enfoque

- **Trazabilidad total:** cada documento antiguo es rastreable y no se pierde ni “contamina” el core activo.
- **Flexibilidad y seguridad:** puedes recibir *cualquier* archivo externo sin riesgo para el repo hasta procesarlo.
- **Curaduría controlada:** nada se integra sin pasar por QA y naming RwB.


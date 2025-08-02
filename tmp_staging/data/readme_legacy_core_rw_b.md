# README\_LEGACY\_CORE\_RW\_B.md

> Definición, alcance y procedimiento de la carpeta LEGACY para el repositorio RwB CORE.

---

## 1. Concepto fundamental

- **LEGACY** es la zona de staging exclusiva y obligatoria para todo documento, archivo o asset antiguo, externo, oficial o propio que aún no cumple con los estándares de naming, estructura, metadatos o semántica RwB.
- Origen irrelevante: puede ser propio, externo, oficial, digitalizado o recibido en cualquier formato (PDF, libro, manual, etc).

---

## 2. Función y reglas de operación

- **Función:** Contener todos los archivos “pre-integración” pendientes de análisis, auditoría, curaduría y transformación antes de ser activos en el core del repo.
- **Ingreso:** Todo archivo no conforme se guarda aquí sin renombrar ni modificar, solo se registra en mapping/trazabilidad.
- **Prohibido usar/citar archivos legacy en activos principales** hasta pasar por auditoría y migración.
- **Se requiere:**
  - Registrar en mapping/logbook (fuente, fecha, estado, responsable, destino previsto).
  - Iniciar workflow de auditoría/curaduría (auditoría, mapeo, transformación, QA).

---

## 3. Ciclo de vida literal

1. Ingreso a `/LEGACY` y registro en mapping.
2. Auditoría inicial y definición de destino.
3. Procesamiento y adaptación (naming, metadata, formato RwB).
4. Consolidación: integración a core, base, biblioteca, etc.
5. Eliminación del archivo original legacy (salvo obligación legal, se guarda en backup comprimido).
6. Logs y changelog siempre actualizados.

---

## 4. Notas y recomendaciones

- Ningún archivo en LEGACY es activo ni referencia válida hasta migrar.
- Uso exclusivo para staging y procesamiento, no como backup permanente.
- Checklist y workflow literal deben regir el ciclo de vida.

---

## 5. Ejemplo visual

```mermaid
flowchart TD
    A[Ingreso archivo antiguo (cualquier fuente)] --> B[LEGACY]
    B --> C[Auditoría/mapping]
    C --> D[Procesamiento/curaduría]
    D --> E[Consolidación en core/base]
    E --> F[Backup comprimido (si externo) o eliminación (si propio)]
```


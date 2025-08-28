# 📂 DIRECTORIO DE ACTIVOS EN DESARROLLO (STAGING)

---

## Propósito
- Contenedor temporal para todo archivo **activo** que está en desarrollo, revisión, aprendizaje, feedback o validación antes de su consolidación en el core del repo.
- Incluye archivos provenientes de **LEGACY** bajo auditoría, y archivos nuevos/intermedios de workflows internos.

---

## Qué almacena
- **Archivos auditados de legacy**: cada archivo extraído de LEGACY y bajo auditoría activa, más sus outputs de auditoría/documentación, hasta ser consolidado.
- **Outputs intermedios de workflows**: drafts, evaluaciones, feedback, experimentos, versiones temporales de scripts, matrices, docs.
- **Aprendizajes y modificaciones** en curso: cambios en workflows, lecciones aprendidas, insights, knowledge generados por nuevos ciclos, tareas, hilos, hasta estar listos para integración al core.
- **Cualquier archivo pendiente** de validación, migración, consolidación (features, upgrades, testing, QA en proceso).

---

## Flujo típico
1. Archivo entra a **staging** (desde LEGACY tras auditoría, o como output nuevo/intermedio).
2. Se procesa, revisa, itera, versiona y/o valida.
3. Cuando cumple criterios (QA, naming, procedencia, versionado, feedback cerrado), se **mueve/consolida**:
   - Al core/main como asset definitivo (nuevo archivo).
   - Integrado en una base o asset existente.
   - O bien, se elimina si no es relevante.

---

## Ventajas
- Separa claramente lo “en desarrollo” de lo activo/validado.
- Permite flujos iterativos, revisiones, feedback y control de calidad incremental, sin contaminar la base activa.
- Sirve como staging para consolidación, merge y refactorización incremental.


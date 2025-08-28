# [BARRIDO_LITERAL] — WF_RELEVAMIENTO_PDF_LIBROS_v1

---

## 🔴 Nota de máxima jerarquía · Relevamiento y Adaptación de Libros PDF

> **Este documento consolidado será el archivo de referencia oficial en nuestra biblioteca y la única fuente a consultar para investigación y procesos derivados.**
>
> - **Todo texto incluido debe ser una copia literal, íntegra y exacta del capítulo, sección o punto elegido, sin simplificaciones, interpretaciones ni resúmenes** (salvo resumen explícito de temas adyacentes o de contexto no elegido, el cual debe estar claramente identificado como tal).
> - **No se permite modificar ni parafrasear el contenido seleccionado.**
> - El índice debe listar todos los temas/títulos/capítulos, aunque no estén incluidos íntegramente, para asegurar la trazabilidad y permitir la actualización incremental futura.
> - En los casos en que el tema consultado esté fuera del coverage, el workflow debe instruir automáticamente la subida/relectura del PDF original y la extensión/actualización del archivo consolidado.
> - **Este documento debe ser apto para auditoría y uso humano/IA, garantizando integridad, literalidad y trazabilidad absoluta.**

---

## Instrucción adicional de workflow

- **Al iniciar la rutina, se debe abrir el canvas y generar automáticamente una guía/checklist para el usuario, donde se solicite:**
  - Modelos IA a emplear en cada paso (ej: 4.1 para barrido, O3 para feedback, etc).
  - Objetivos y preguntas de investigación para cada etapa.
  - Criterios de validación y control para seguir el procedimiento completo y correcto, hasta la generación del archivo final.

---

## 1. Objetivo
- Permitir la integración eficiente de libros en PDF en el core de research, garantizando control, curaduría, naming y trazabilidad para su uso activo en assets, research o bibliotecas internas.
- Asegurar que todo análisis, extracción, síntesis y almacenamiento cumpla el ciclo de vida RwB y los límites de contexto IA.

---

## 2. Etapas del workflow (literal, alineado a RwB)

### A. INGRESO Y REGISTRO (LEGACY)
1. Todo libro PDF (o fuente externa) ingresa en `/PURGATORIO/LEGACY/` o bucket análogo de staging, sin alterar su nombre original.
2. Registrar en mapping/logbook: fuente, fecha, responsable, estado inicial, destino previsto.
3. Prohibido su uso/citación en activos principales antes de pasar por curaduría/auditoría.

### B. AUDITORÍA Y MAPEO INICIAL
4. Auditoría de estructura y calidad (completo, dañado, OCR, idioma, metadata básica).
5. Clasificar: relevancia, prioridad, nivel de integración esperada (research, biblioteca, doc auxiliar, descarte).
6. Registrar todo el proceso en mapping y checklist (`CHK`, `BIT`).

### C. EXTRACCIÓN, CURADURÍA Y ADAPTACIÓN
7. Extraer partes clave, capítulos, tablas, imágenes o datasets relevantes (chunking, OCR si aplica).
8. Adaptar contenido a formato RwB: naming (`SRC·STG·ROLE`), slices optimizados para IA (snapshots, insights), metadata extendida (tokens, modelo, coverage, referencias).
9. Validar la literalidad, cobertura y tokens frente a la matriz del modelo target (`/DATA/` o `/SNAPSHOTS_CTX/`).

### D. CONSOLIDACIÓN Y OUTPUTS
10. Consolidar outputs en buckets definitivos:
   - Research (`/RESEARCH/`): análisis profundo, benchmarks, síntesis de findings.
   - Data (`/DATA/`): tablas, datasets estructurados.
   - Assets (`/ASSETS/`): extractos listos para reutilización directa.
   - Training/Learning (`/KNS/TL/`, `/KNS/LEARN/`): insights, lecciones, feedback iterativo.
   - Backup (`/BACKUP/`): versión PDF original comprimida + snapshot de outputs.
11. Actualizar logs (`LOG`, `CHGLOG`), mapping y matriz.

### E. DEPURACIÓN Y CIERRE
12. Una vez auditado, integrado y versionado el output relevante, eliminar/eliminar archivo PDF original (salvo obligación legal/histórica, guardar solo backup comprimido).
13. Prohibido mantener “residuos” fuera del core/backup.

---

## 3. Naming, metadata y snapshotting (extracto clave)
- Todo output debe usar naming Matrix: `SRC·STG·ROLE`, versión y metadatos explícitos.
- Outputs IA (snapshots, insights, slices) deben ser chunked y auditados por tokens, modelo y coverage.
- Registrar fecha, fuente, responsable, tokens usados y coverage en cabecera.

---

## 4. Triggers y checklist de control (BARRIDO_LITERAL)
- [ ] ¿Fue registrado el PDF en mapping/logbook?
- [ ] ¿Auditoría de integridad/estructura realizada?
- [ ] ¿Clasificación y relevancia documentada?
- [ ] ¿Outputs chunked, versionados y alineados a modelo?
- [ ] ¿Tokens y coverage validados?
- [ ] ¿Consolidación en bucket destino y log actualizado?
- [ ] ¿Backup y depuración cerrados?

---

## 5. Integración en workflows y scripts
- Este WF debe integrarse como macro en flujos de research, onboarding, training y auditoría.
- Scripts de chunking/OCR/resumen deben alinearse a naming y triggers Matrix.
- Outputs listos para embedding, consulta IA, documentación y reutilización estructurada.

---

## 6. Referencias
- DIR_ARCH_PLAN v5, Blueprint Matrix, Glosario CODE v2, Diccionario Code Triggers, Checklist CHK, Scripts SCR, Matriz de límites de contexto IA, Learn/Feedback.

---

> Status: [BARRIDO_LITERAL] · [REVISION_PENDING]
> Última edición: GPT-4.1 · Fecha: 2025-08-02 · Autoría: GZelechower & GPT

---

**FIN WF_RELEVAMIENTO_PDF_LIBROS_v1**


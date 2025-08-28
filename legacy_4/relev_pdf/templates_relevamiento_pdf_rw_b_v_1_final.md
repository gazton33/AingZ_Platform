# [RwB] Templates · Relevamiento y Adaptación de Libros PDF · v1 FINAL

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

# Templates actualizados

## 1. Template — Auditoría Literal 100% (Modelo 4.1)

[ver canvas]

## 2. Template — Feedback con Usuario (Definición de Objetivo)

[ver canvas]

## 3. Template — Auditoría Temática (Barrido Focalizado)

[ver canvas]

## 4. Template — Validación/Feedback Final

[ver canvas]

## 5. Template — Consolidado Final (Con Índice Literal y Trazabilidad)

```markdown
# [CONSOLIDADO_PDF_RW_B] — Integración lista para migración

**Documento origen:** {NOMBRE_PDF}
**Fuente:** {fuente}
**Fecha consolidación:** {YYYY-MM-DD}
**Modelo:** GPT-4.1 + O3
**Tokens total:** {número}
**Usuario/IA:** {nombres}
**Referencia backup:** {ruta/backup.zip}
**Código Matrix:** {SRC·STG·ROLE}

---

## 1. Índice literal del PDF (capítulos/títulos)
| # | Título/Sección | Página(s) | Incluido en archivo | Cobertura |
|---|----------------|-----------|--------------------|-----------|
| 1 |                |           | Sí/No              | Completo/Parcial |
| ... |              |           |                    |           |

---

## 2. Extractos literales completos
> A continuación, se copian textualmente (sin cambios) los capítulos/secciones elegidos como referencia.

---

## 3. Resumen de temas adyacentes
> Breve resumen de temas que, sin ser el foco, son adyacentes a lo seleccionado y pueden ser útiles para futuras extensiones.

---

## 4. Índice de temas no relacionados
> Listado de títulos/secciones del libro no incluidos ni adyacentes a la selección, para control de coverage y futuras auditorías.

---

## 5. Metadatos y trazabilidad
- Fecha de backup: {YYYY-MM-DD}
- Tokens usados: {número}
- Modelo(s): {gpt-4.1/o3}
- Responsable: {usuario}
- Feedbacks históricos: {enlaces a archivos feedback}
- Coverage: {porcentaje/explicación}

---

## 6. Referencias cruzadas y triggers de actualización
- [ ] Link directo a backup en `/BACKUP/`
- [ ] Referencia en mapping/logbook
- [ ] Indexación para embedding/consultas IA
- [ ] Propuesta automática de actualización si se consulta un tema NO incluido

---

**Checklist de cierre**
- [ ] Archivo validado y consolidado
- [ ] Backup PDF comprimido presente
- [ ] Todo referenciado en Matrix y mapping
- [ ] Ready for use/integración

---
```

---

> Todos los templates y rutinas están actualizados. Integrar siempre el bloque de máxima jerarquía en el consolidado y workflow antes de cualquier uso en research, training o downstream tasks.


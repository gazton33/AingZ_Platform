# WORKFLOW — Plantilla & Lecciones del Proyecto GZ + ChatGPT

> Proyecto: **AingZ_Repo / ChatGPT Advanced Workflows**
> Última actualización: 2025-07-10

---

## 1. Descripción general
Workflow maestro para construcción y control de sistemas IA documentados, modulares y auditables. Integra: creación de matriz, mapeo de features, control de calidad y documentación viva.

## 2. Etapas del workflow
1. **Planificación**
   - Definir propósito, entorno y requerimientos del workflow.
   - Abrir README y croquis de arquitectura en `/docs`.
2. **Extracción & Matriz RAW**
   - Generar matriz inicial de features en knowledge base (bilingüe, con clase, naming, descripción).
   - Revisar que ninguna funcionalidad “core” quede fuera.
3. **Expansión a matriz extendida**
   - Asignar códigos, clases, nombres EN, abreviaturas.
   - Agregar descripción técnica y actualizar control de fuentes.
4. **Control cruzado & validación**
   - Comparar matriz extendida vs. RAW, anotar diferencias, resolver gaps.
   - Dejar registro del control en `/matrices`.
5. **Mapeo de features**
   - Definir para cada feature: prompt, acción, knowledge, script, frecuencia.
   - Agregar visualizaciones (croquis, diagramas de flujo, matriz cruzada).
6. **Carga al repositorio**
   - Subir archivos a carpetas según estructura definida.
   - Actualizar README y archivos de control/trazabilidad.
7. **Iteración, feedback y actualización**
   - Documentar feedback, problemas y decisiones en knowledge base.
   - Marcar features deprecated y registrar upgrades.

## 3. ¿Qué repetir y qué evitar?
- **Sí:** Controlar siempre la cobertura entre matrices; mantener naming técnico bilingüe; versionar todo; documentar errores y decisiones.
- **No:** Publicar cambios sin validación, perder trazabilidad de fuentes, cambiar naming sin control, descuidar documentación viva.

## 4. Referencias y dependencias
- [matriz_extendida_features_chatgpt_workflow.md](../knowledges/matriz_extendida_features_chatgpt_workflow.md)
- [knowledge_gz_project_insights.md](../knowledges/knowledge_gz_project_insights.md)
- [croquis-mapeo-features-prompts.md](../doc/croquis-mapeo-features-prompts.md)
- [control-cruce-matriz-raw-vs-extendida.md](../matrices/control-cruce-matriz-raw-vs-extendida.md)

---

> **Nota:** Esta plantilla y workflow se actualizan y expanden tras cada ciclo de aprendizaje/feedback. Usar como referencia viva para nuevos módulos IA/documentación.


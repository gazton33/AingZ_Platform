# RwB_AUDT_README_WORKFLOWS_LOTE2_20250725.md — Auditoría estructural legacy (Draft)

---

## 1. Propósito/contexto
Auditoría del README de workflows: explica el propósito, uso, referencias y buenas prácticas para la carpeta central de workflows en el stack IA/ChatGPT (AingZ_Repo).

---

## 2. Barrido literal selectivo y mapeo estructural
- **Bloques críticos:**
  - Descripción de propósito y alcance de la carpeta workflows.
  - Guía para uso, referencias cruzadas, ciclo de feedback y mejores prácticas.
  - Instrucciones de versionado, logs, y regla: NO borrar workflows viejos (solo marcar como deprecated para trazabilidad).
- **Mapeo glosario/estructura:**
  - Clase “README/WF”; función “documentación/guía de uso”, bloque “entrypoint/directorio”.
  - Referencia a todos los workflows principales y reglas de versionado.

---

## 3. Análisis de integración y mejoras
- El README es guía y entrypoint; debe mantenerse en la raíz de la carpeta workflows y actualizarse con cada nuevo ciclo.
- Propuesta: Sumar changelog interno y links a auditorías de workflows anteriores/deprecated.
- Sugerir subdirectorio “workflows/deprecated” solo para tracking y revisión histórica.

---

## 4. Checklist de cobertura y reproducibilidad (visual-friendly)
- Bloques críticos extraídos y mapeados: OK
- Referencias cruzadas y reglas de versionado: OK
- Changelog y tracking sugeridos: OK
- Legacy original referenciado (readme_workflows.md): OK
- Auto-reproducible con legacy accesible: OK

---

## 5. Feedback, lessons learned, riesgos
- Si el README no se mantiene vivo y versionado, puede haber pérdidas de contexto y uso erróneo de workflows históricos.
- Propuesta: Documentar todos los cambios/ciclos en changelog y actualizar README con cada iteración.

---


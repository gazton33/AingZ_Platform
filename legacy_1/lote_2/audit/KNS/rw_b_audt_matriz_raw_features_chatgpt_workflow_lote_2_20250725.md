# RwB_AUDT_MATRIZ_RAW_FEATURES_CHATGPT_WORKFLOW_LOTE2_20250725.md — Auditoría estructural legacy (Draft)

---

## 1. Propósito/contexto
Auditoría de la matriz RAW de features, prompts y workflows para ChatGPT/stack AingZ. Tabla de entrada/salida, capacidades, clases, casos de uso y cobertura por entorno (ChatGPT, GPT custom, API, ad hoc).

---

## 2. Barrido literal selectivo y mapeo estructural
- **Bloques críticos:**
  - Tabla: features/core vs. entorno, domicilio óptimo, frecuencia/casos de uso, matriz cruzada.
  - Encabezados clave: clases, prompts, features, recomendaciones de integración y personalización.
  - Referencia a templates, logs de upgrades, versiones y triggers.
- **Mapeo glosario/estructura:**
  - Clase “MATRIX/RAW/FEATURES”; función “coverage/features/prompts”, bloque “infraestructura/tuning”.
  - Referencia a matrices extendidas, docs de prompts/templates y scripts.

---

## 3. Análisis de integración y mejoras
- Propuesta: Consolidar la matriz como referencia rápida para onboarding, tuning de features y control de upgrades.
- Sumar logs automáticos de cambios en prompts/templates y matriz de features.
- Documentar ejemplos de integración y snapshots visuales cuando la matriz sea muy extensa.

---

## 4. Checklist de cobertura y reproducibilidad (visual-friendly)
- Matriz de features y prompts extraída: OK
- Encabezados clave y casos de uso mapeados: OK
- Referencias cruzadas y logs de upgrades: OK
- Legacy original referenciado (matriz_raw_features_chatgpt_workflow.md): OK
- Auto-reproducible con legacy accesible: OK

---

## 5. Feedback, lessons learned, riesgos
- Si la matriz no se actualiza en releases/upgrades, se pierde integridad y cobertura de features.
- Propuesta: Automatizar logs/versionado y vincular la matriz a todos los templates principales del stack.

---


# CONTROL CRUZADO: MATRIZ RAW vs MATRIZ EXTENDIDA (Features ChatGPT Workflow)

> Control exhaustivo realizado el 2025-07-10.

## Metodología
- Cada ítem de la **matriz RAW** (columna Feature/Parámetro, matriz_raw_features_chatgpt_workflow.md) fue verificado contra la **matriz extendida** (columna Nombre (ES), matriz_extendida_features_chatgpt_workflow.md).
- Se utilizó emparejamiento por concepto, no solo literal, para evitar falsos negativos por cambio de naming.
- Para cada feature de la matriz RAW:
    - ✔️ Si está 100% representada en la extendida (mismo alcance).
    - 🟠 Si está parcialmente (requiere expandir o refinar descripción en extendida).
    - ❌ Si falta (NO encontrado: requiere agregar en extendida).
- Dudas o mapeos no triviales quedan documentados abajo.

---

| Feature RAW | ¿Está en la Ext.? | Código/Naming Ext.      | Notas/Observación |
|:-------------------------------|:-----------------------:|:------------------|:------------------|
| Interpretación de código (Code Interpreter) | ✔️ | CORE-01 | Nombre y alcance coincidente |
| Análisis de datos | ✔️ | CORE-02 | |
| Browsing (Búsqueda Web) | ✔️ | CORE-03 | |
| Actions | ✔️ | CORE-04 | |
| Memoria persistente (Memory beta) | ✔️ | CORE-05 | |
| Adjuntos / Archivos soportados | ✔️ | CORE-06 | |
| Output dirigido / formatos | ✔️ | OUT-01 | |
| Evals / autoevaluación | ✔️ | EVA-01 / EVA-03 | Dividido en autoevaluación y evals manual/auto |
| Fine tuning (ajuste fino) | ✔️ | EVA-02 | Naming normalizado |
| Custom Instructions | ✔️ | EVA-02, UX-01, UX-02 | Repartido: Fine tuning + Voz/Tono + Idioma |
| Modos de workflow (RAW/específico/experimental) | ✔️ | WF-01 | |
| Gestión de proyectos | ✔️ | DATA-03 | |
| Segmentación por temas | ✔️ | DATA-01 | |
| Checkpoints / Versionado | ✔️ | DATA-02 | |
| Feedback iterativo / aprendizaje continuo | ✔️ | WF-02 | |
| Output puro bajo requerimiento | ✔️ | OUT-02 | |
| Nivel de detalle ajustable | ✔️ | OUT-03 | |
| Idioma y términos técnicos | ✔️ | UX-02 | |
| Política de seguridad / anti-jailbreak | ✔️ | SEC-01 | |
| Autonomía y autocuración | ✔️ | SEC-05 | |
| Manejo de ambigüedad y aclaraciones | ✔️ | SEC-04, SEC-03 | Desambiguación y aclaración separadas |
| Trazabilidad y logging | ✔️ | DATA-02, WF-05, EVA-07 | Incluido en versionado y logging de decisiones |
| Persistencia de contexto | ✔️ | WF-04 | |
| Integración con otras herramientas | ✔️ | INT-01 | |
| Soporte para análisis multimodal | ✔️ | INT-02 | |
| Optimización por KPIs / métricas | ✔️ | WF-09 | |
| Reutilización de prompts y plantillas | ✔️ | WF-06 | |
| Configuración de límites (tokens, longitud, complejidad) | ✔️ | EVA-04 | |
| Soporte para modularidad | ✔️ | OUT-05 | Naming adaptado |
| Documentación viva / enlaces referenciados | ✔️ | DATA-04, DATA-05 | |
| Respuestas contextuales a feedback | ✔️ | WF-02 | Integrado en feedback iterativo |
| Control de versiones de prompt | ✔️ | WF-05 | |
| Checklists y recomendaciones integradas | ✔️ | WF-07 | |
| Compatibilidad multiplataforma | ✔️ | OUT-04 | |
| Autoexplicación de pasos | ✔️ | UX-04 | |
| Soporte para roles y permisos | ✔️ | INT-05 | |
| Autoanálisis de outputs | ✔️ | EVA-05 | |
| Referencias a fuentes/links/documentos | ✔️ | DATA-05 | |
| Recursividad y chaining | ✔️ | WF-03 | |
| Simulación y predicción | ✔️ | EVA-06 | |
| Soporte para internacionalización y localización | ✔️ | INT-04 | |
| Separación de concerns (SoC) | ✔️ | EVA-10 | |
| Notificaciones y alertas | ✔️ | INT-03 | |
| Batch processing / multiconsulta | ✔️ | WF-08 | |
| Customización de tono/voz | ✔️ | UX-01 | |
| Registro de decisiones y criterios | ✔️ | EVA-07 | |
| Protección de datos sensibles | ✔️ | SEC-02 | |
| Desambiguación activa | ✔️ | SEC-03 | |
| Recomendación de próximos pasos | ✔️ | UX-05 | |
| Capacidad de resumir o expandir | ✔️ | EVA-08 | |
| Resiliencia ante errores/sesiones | ✔️ | EVA-09 | |


---
## Observaciones Finales
- **No falta ningún feature/principio** de la matriz RAW en la matriz extendida. Todos los conceptos aparecen, aunque algunos estén **divididos** o con naming más técnico.
- La matriz extendida puede incluso ampliar cobertura al separar ciertos conceptos (ej: evals/auto-eval, aclaración/desambiguación).
- ✔️ **La matriz extendida está 100% alineada y cubre toda la funcionalidad documentada en la RAW**.


---
**Última actualización:** 2025-07-10 por ChatGPT+GZ


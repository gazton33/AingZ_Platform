# CONTROL Y TRAZABILIDAD DE FUENTES — MATRIZ DE FEATURES CHATGPT WORKFLOW

> **Propósito:**
> Este archivo registra la fuente principal y detalles de actualización de cada feature/documento de la matriz extendida. Sirve como bitácora de referencia, verificación y auditoría.

| Código    | Fuente principal              | Sección o archivo       | Fecha última verif. | Versión doc | Comentario/Notas                      |
|:---------:|:-----------------------------|:-----------------------|:--------------------|:-----------:|:--------------------------------------|
| CORE-01   | README, Docs OpenAI, workflow| README, code-interpreter| 2025-07-10          | v1.0        | Confirmado función core de plataforma |
| CORE-02   | README, workflow_gpt_raw      | Data analysis, samples | 2025-07-10          | v1.0        | Incluye CSV/XLSX/JSON/IMG/PDF         |
| CORE-03   | README, Docs OpenAI           | browsing, features     | 2025-07-10          | v1.0        | Incluye limits, casos edge web        |
| CORE-04   | workflow_gpt_raw, README      | Actions, API           | 2025-07-10          | v1.0        |                                       |
| CORE-05   | workflow_gpt_raw, Docs OpenAI | Memory beta, workflow  | 2025-07-10          | v1.0        | Confirmado persistencia               |
| CORE-06   | README, workflow_gpt_raw      | Attachments, input     | 2025-07-10          | v1.0        | Multimodal soportado                  |
| OUT-01    | workflow_gpt_raw, README      | Output, formatting     | 2025-07-10          | v1.0        | Formatos: JSON, MD, YAML, tabla, etc. |
| OUT-02    | workflow_gpt_raw              | Output pure            | 2025-07-10          | v1.0        | Restricción en workflows operativos   |
| OUT-03    | workflow_gpt_raw, README      | Detail level           | 2025-07-10          | v1.0        | Parámetro ajustable                   |
| OUT-04    | README, Docs OpenAI           | Multiplatform          | 2025-07-10          | v1.0        | Pruebas mobile, API, export           |
| OUT-05    | workflow_gpt_raw              | Modular output         | 2025-07-10          | v1.0        | Modularidad explícita                 |
| DATA-01   | workflow_gpt_raw, README      | Topic segmentation     | 2025-07-10          | v1.0        | Organiza y filtra tareas/contenido    |
| DATA-02   | workflow_gpt_raw              | Checkpoints/versioning | 2025-07-10          | v1.0        | Snapshots y rollback                  |
| DATA-03   | workflow_gpt_raw              | Project management     | 2025-07-10          | v1.0        | Gestión proyectos multi-hilo          |
| DATA-04   | README, Docs OpenAI           | Living doc             | 2025-07-10          | v1.0        | Manifiesto, docs vivas, diagrams      |
| DATA-05   | workflow_gpt_raw, README      | References/links       | 2025-07-10          | v1.0        | Links, archivos, trackers             |
| WF-01     | workflow_gpt_raw              | RAW/Specific modes     | 2025-07-10          | v1.0        | Alternancia clave workflow            |
| WF-02     | workflow_gpt_raw              | Iterative feedback     | 2025-07-10          | v1.0        | Feedback en loop                      |
| WF-03     | workflow_gpt_raw, README      | Recursion/chaining     | 2025-07-10          | v1.0        | Chaining prompts/tasks                |
| WF-04     | workflow_gpt_raw, Docs OpenAI | Context persistence    | 2025-07-10          | v1.0        | Contexto conservado en sesión         |
| WF-05     | workflow_gpt_raw              | Prompt version control | 2025-07-10          | v1.0        | Histórico de prompts                  |
| WF-06     | workflow_gpt_raw              | Prompt/template reuse  | 2025-07-10          | v1.0        | Uso repetido de plantillas            |
| WF-07     | workflow_gpt_raw              | Checklists integrated  | 2025-07-10          | v1.0        | Pasos críticos por tarea              |
| WF-08     | workflow_gpt_raw              | Batch processing       | 2025-07-10          | v1.0        | Multi-task, multiconsulta             |
| WF-09     | workflow_gpt_raw, README      | KPI-driven             | 2025-07-10          | v1.0        | Métricas y prioridades                |
| SEC-01    | README, Docs OpenAI           | Security/anti-jailbreak| 2025-07-10          | v1.0        | Políticas y límites plataforma        |
| SEC-02    | workflow_gpt_raw              | Data protection        | 2025-07-10          | v1.0        | Anonimización y compliance            |
| SEC-03    | workflow_gpt_raw              | Disambiguation         | 2025-07-10          | v1.0        | Aclaración y precisión output         |
| SEC-04    | workflow_gpt_raw, README      | Ambiguity handling     | 2025-07-10          | v1.0        | Pedidos de aclaración automáticos     |
| SEC-05    | workflow_gpt_raw              | Self-healing           | 2025-07-10          | v1.0        | Detección/corrección errores          |
| UX-01     | README, workflow_gpt_raw      | Voice/tone customization| 2025-07-10         | v1.0        | Personalización contexto/cultura      |
| UX-02     | README, workflow_gpt_raw      | Lang/tech terms        | 2025-07-10          | v1.0        | Bilingüismo, tecnicismos              |
| UX-03     | workflow_gpt_raw, README      | Explanation level      | 2025-07-10          | v1.0        | Output custom según detalle           |
| UX-04     | workflow_gpt_raw              | Self-explanation       | 2025-07-10          | v1.0        | Paso a paso interno                   |
| UX-05     | workflow_gpt_raw              | Next steps suggestion  | 2025-07-10          | v1.0        | Sugerencias proactivas                |
| INT-01    | workflow_gpt_raw              | Tools integration      | 2025-07-10          | v1.0        | APIs, sistemas externos, automatización|
| INT-02    | README, Docs OpenAI           | Multimodal analysis    | 2025-07-10          | v1.0        | Análisis texto, imagen, datos         |
| INT-03    | workflow_gpt_raw, README      | Notifications/alerts   | 2025-07-10          | v1.0        | Alertas, errores, cambios             |
| INT-04    | README, Docs OpenAI           | Internationalization   | 2025-07-10          | v1.0        | Idioma, moneda, formato adaptativo    |
| INT-05    | workflow_gpt_raw              | Roles/permissions      | 2025-07-10          | v1.0        | Respuestas segmentadas por rol        |
| EVA-01    | workflow_gpt_raw              | Output self-eval       | 2025-07-10          | v1.0        | Evaluación automática                 |
| EVA-02    | workflow_gpt_raw              | Fine-tuning            | 2025-07-10          | v1.0        | Personalización avanzada              |
| EVA-03    | workflow_gpt_raw, README      | Evals                  | 2025-07-10          | v1.0        | Evaluación/calidad de outputs         |
| EVA-04    | workflow_gpt_raw              | Limits optimization    | 2025-07-10          | v1.0        | Respuestas dentro de límites          |
| EVA-05    | workflow_gpt_raw              | Output self-analysis   | 2025-07-10          | v1.0        | Autoanálisis previo a output          |
| EVA-06    | workflow_gpt_raw, README      | Simulation/prediction  | 2025-07-10          | v1.0        | Modelado y escenarios                 |
| EVA-07    | workflow_gpt_raw              | Decision logging       | 2025-07-10          | v1.0        | Registro de decisiones clave          |
| EVA-08    | workflow_gpt_raw, README      | Summarize/expand       | 2025-07-10          | v1.0        | Resumir o expandir outputs            |
| EVA-09    | workflow_gpt_raw              | Session resilience     | 2025-07-10          | v1.0        | Mantener contexto tras errores        |
| EVA-10    | workflow_gpt_raw              | Separation of Concerns | 2025-07-10          | v1.0        | SoC para upgrades y debugging         |

---

> **Nota:** Actualiza la fecha y versión cada vez que modifiques la feature en la matriz principal. Ante nuevos features, clona la fila y agrega las fuentes relevantes.
> Para privacidad y compliance, nunca copies datos sensibles o claves personales de archivos de workflow sin anonimizar/filtrar previamente.


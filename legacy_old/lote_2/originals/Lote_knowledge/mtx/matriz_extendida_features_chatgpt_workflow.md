# MATRIZ EXTENDIDA DE FEATURES — CHATGPT WORKFLOW

| Código   | Clase        | Nombre (ES)                | Nombre (EN)             | Abrev.   | Descripción técnica breve                                                                              |
|:--------:|:------------:|:---------------------------|:------------------------|:--------:|:------------------------------------------------------------------------------------------------------|
| CORE-01  | CORE         | Interpretación de código   | Code Interpreter        | CI       | Ejecuta código Python, resuelve cálculos, grafica y automatiza tareas técnicas en la conversación.    |
| CORE-02  | CORE         | Análisis de datos          | Data Analysis           | DA       | Procesa, limpia y resume archivos adjuntos: CSV, XLSX, JSON, imágenes, PDFs, logs, etc.               |
| CORE-03  | CORE         | Búsqueda web               | Browsing                | BRW      | Accede a información online actualizada y datos en tiempo real.                                       |
| CORE-04  | CORE         | Acciones e integraciones   | Actions                 | ACT      | Ejecuta acciones externas vía API, calendar, webhooks y conecta con otros sistemas.                   |
| CORE-05  | CORE         | Memoria persistente        | Memory (Persistent)     | MEM      | Guarda y recupera información relevante, contexto, feedback y estado entre sesiones.                  |
| CORE-06  | CORE         | Adjuntos                   | Attachments             | ATT      | Soporta carga, lectura y análisis de archivos (imágenes, PDFs, docs) en el chat.                      |
| OUT-01   | OUTPUT       | Output dirigido            | Targeted Output         | TO       | Responde en formato solicitado: JSON, Markdown, YAML, tablas, código, diagramas, etc.                 |
| OUT-02   | OUTPUT       | Output puro                | Pure Output             | PO       | Entrega solo el formato requerido, sin explicaciones ni comentarios extra.                            |
| OUT-03   | OUTPUT       | Nivel de detalle ajustable | Adjustable Detail Level | ADL      | Responde en modo resumen, detallado o paso a paso según lo requiera el usuario.                       |
| OUT-04   | OUTPUT       | Compatibilidad multiplataforma | Multiplatform Compatibility | MPC      | Outputs y prompts adaptables a distintos entornos (web, móvil, API, CI/CD).                           |
| OUT-05   | OUTPUT       | Output modular             | Modular Output          | MO       | Divide respuestas en bloques o módulos independientes y reutilizables.                                |
| DATA-01  | DATA         | Segmentación por temas     | Topic Segmentation      | TS       | Organiza info por tópicos, módulos o fases dentro del workflow.                                       |
| DATA-02  | DATA         | Checkpoints/versionado     | Checkpoints/Versioning  | CPV      | Registro y gestión de versiones, estados y snapshots de proyectos/prompts.                            |
| DATA-03  | DATA         | Gestión de proyectos       | Project Management      | PM       | Segmenta y prioriza tareas, hitos y feedback por proyecto/hilo.                                       |
| DATA-04  | DATA         | Documentación viva         | Living Documentation    | LD       | Integra y referencia docs vivas, manifiestos, diagramas y recursos.                                   |
| DATA-05  | DATA         | Referencias externas       | References/Links        | REF      | Incluye links, fuentes originales, archivos e issue trackers en la conversación.                      |
| WF-01    | WORKFLOW     | Modos RAW/específico       | RAW/Specific Modes      | RAW/SPC  | Alterna entre exploración amplia (RAW) y foco profundo (específico).                                  |
| WF-02    | WORKFLOW     | Feedback iterativo         | Iterative Feedback      | IFB      | Integra feedback y correcciones del usuario en tiempo real.                                           |
| WF-03    | WORKFLOW     | Recursividad/chaining      | Recursion/Chaining      | RC       | Encadena tareas, sub-prompts o módulos para resolver problemas complejos.                             |
| WF-04    | WORKFLOW     | Persistencia de contexto   | Context Persistence     | CTX      | Mantiene y recuerda detalles clave a lo largo del proyecto/conversación.                              |
| WF-05    | WORKFLOW     | Control de versiones prompt| Prompt Version Control  | PVC      | Gestiona diferentes versiones/evoluciones de prompts y respuestas.                                    |
| WF-06    | WORKFLOW     | Reutilización de plantillas| Prompt/Template Reuse   | PTR      | Crea, guarda y ajusta prompts/modos reutilizables.                                                    |
| WF-07    | WORKFLOW     | Checklists integradas      | Integrated Checklists   | ICL      | Incluye listas de pasos o controles críticos en cada respuesta o tarea.                               |
| WF-08    | WORKFLOW     | Batch/multiconsulta        | Batch Processing        | BP       | Procesa múltiples consultas/tareas en paralelo o por lotes.                                           |
| WF-09    | WORKFLOW     | Optimización por KPIs      | KPI-driven Optimization | KPI      | Prioriza soluciones/tareas basadas en indicadores de rendimiento definidos.                           |
| SEC-01   | SECURITY     | Seguridad/anti-jailbreak   | Security/Anti-jailbreak | SEC      | Cumple normas de contenido, ética, privacidad y bloquea intentos de manipulación.                     |
| SEC-02   | SECURITY     | Protección de datos        | Data Protection         | DP       | Filtra o anonimiza información sensible/confidencial.                                                 |
| SEC-03   | SECURITY     | Desambiguación activa      | Active Disambiguation   | ADIS     | Elimina dobles sentidos, clarifica términos y supuestos.                                              |
| SEC-04   | SECURITY     | Manejo de ambigüedad       | Ambiguity Handling      | AH       | Solicita aclaraciones ante instrucciones incompletas/ambiguas.                                        |
| SEC-05   | SECURITY     | Autonomía/autocuración     | Autonomy/Self-Healing   | ASH      | Detecta y corrige errores o inconsistencias automáticamente.                                          |
| UX-01    | USER-EXP     | Personalización de voz/tono| Voice/Tone Customization| VTC      | Ajusta voz, tono y formalidad según contexto/cultura/proyecto.                                        |
| UX-02    | USER-EXP     | Idioma y términos técnicos | Language & Tech Terms   | LTT      | Configura idioma (ES/EN) y uso de términos técnicos bilingües.                                        |
| UX-03    | USER-EXP     | Nivel de explicación       | Explanation Level       | EXPL     | Responde con explicaciones breves, extendidas o solo código según pedido.                             |
| UX-04    | USER-EXP     | Autoexplicación de pasos   | Self-Explanation        | SE       | Explica brevemente los pasos internos de procesos complejos.                                          |
| UX-05    | USER-EXP     | Sugerencia de próximos pasos| Next Steps Suggestion  | NSS      | Recomienda acciones, módulos o recursos a seguir en el workflow.                                      |
| INT-01   | INTEGRATION  | Integración de herramientas| Tools Integration       | TI       | Conecta, coordina o automatiza acciones con plataformas externas, APIs, calendarios, etc.             |
| INT-02   | INTEGRATION  | Soporte análisis multimodal| Multimodal Analysis     | MMA      | Relaciona y analiza texto, imagen, datos estructurados simultáneamente.                               |
| INT-03   | INTEGRATION  | Notificaciones/alertas     | Notifications/Alerts    | NTA      | Integra sistemas de alerta/notificación para hitos, errores, cambios de workflow.                     |
| INT-04   | INTEGRATION  | Internacionalización       | Internationalization    | INTL     | Adapta lenguaje, formatos, moneda, etc. según región/estándar.                                        |
| INT-05   | INTEGRATION  | Roles y permisos           | Roles & Permissions     | RP       | Configura respuestas según rol/perfil del usuario o contexto.                                         |
| EVA-01   | EVAL         | Autoevaluación de outputs  | Output Self-Eval        | OSE      | Evalúa calidad, claridad o completitud de respuestas antes de mostrar al usuario.                     |
| EVA-02   | EVAL         | Fine tuning                | Fine-Tuning             | FT       | Personaliza el modelo: vocabulario, reglas, estilo y reglas de negocio.                               |
| EVA-03   | EVAL         | Evals automáticas/manuales | Evals                   | EVL      | Evalúa, compara y califica outputs o prompts automáticamente.                                         |
| EVA-04   | EVAL         | Optimización de límites    | Limits Optimization     | LO       | Adapta respuestas para cumplir límites de tokens, longitud o complejidad.                             |
| EVA-05   | EVAL         | Autoanálisis de outputs    | Output Self-Analysis    | OSA      | Autoevalúa pertinencia o errores en respuestas antes de entregarlas.                                  |
| EVA-06   | EVAL         | Simulación/predicción      | Simulation/Prediction   | SIM      | Permite escenarios hipotéticos, análisis what-if y predicciones razonadas.                            |
| EVA-07   | EVAL         | Registro de criterios      | Decision Logging        | DL       | Registra las razones detrás de decisiones críticas en la conversación/proyecto.                        |
| EVA-08   | EVAL         | Resumir/expandir outputs   | Summarize/Expand        | S/E      | Resumir grandes volúmenes o expandir detalles según necesidad del usuario.                             |
| EVA-09   | EVAL         | Resiliencia de sesiones    | Session Resilience      | SR       | Retoma contexto y evita pérdida de información ante cortes/reinicios de sesión.                        |
| EVA-10   | EVAL         | Separación de concerns     | Separation of Concerns  | SoC      | Separa lógica, datos y presentación para facilitar upgrades y minimizar errores.                       |


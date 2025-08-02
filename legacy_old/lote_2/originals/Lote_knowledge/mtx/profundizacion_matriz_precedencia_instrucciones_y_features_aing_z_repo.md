# Profundización — Matriz de Precedencia, Adjuntos y Features en AingZ_Repo

> Versión detallada | 2025-07-13 | Autor: GZ (AingZ)

---

## 1. ¿Cómo actúan los adjuntos de conocimiento (Attachments, ATT)?

- **Adjuntos** (feature CORE-06, ATT) permiten cargar archivos (PDF, CSV, imágenes, docs, logs, etc.) y analizarlos durante la conversación.
- Su disponibilidad es contextual: quedan accesibles a nivel de sesión/conversación o pueden formar parte de la knowledge base si se integran a memoria persistente (CORE-05, MEM).
- **No anulan instrucciones globales**, pero pueden influenciar el output si la instrucción lo permite (por ejemplo, si un prompt solicita "resumí este PDF en inglés" y la personalización global es español, el prompt local prevalece sólo para esa respuesta).
- Se relacionan con:
    - **CORE-02 (DA):** Procesamiento y análisis de datos adjuntos.
    - **DATA-04 (LD):** Documentación viva, referencias técnicas y evidencia embebida.
    - **DATA-05 (REF):** Registro y trazabilidad de fuentes externas.
    - **WF-04 (CTX):** Contexto enriquecido para la conversación.

---

## 2. ¿Personalización Global es universal a todo, inclusive GPTs?

- **Sí, la personalización global** (🔵) afecta a todo: proyectos, GPTs, workflows y sesiones, **a menos que una instrucción más específica la anule** (por prompt, sesión, GPT custom, etc.).
- Ejemplo: Si el idioma global es español, un asistente personalizado arrancará con ese idioma salvo que en su configuración específica se indique lo contrario (override local).
- **Nunca puede anular límites éticos/compliance**.

---

## 3. Gestión de workflows, entrenamiento, evaluación y templates universales

### a. **Workflows (WF-xx)**
- Se gestionan como secuencias de acciones con precedencia y control de versiones (WF-05, PVC).
- Permiten encadenar tareas, guardar sub-prompts y estructurar pasos reutilizables (WF-03, RC).
- Soportan modos RAW (exploratorio) y específico, ajustando la profundidad y amplitud del análisis (WF-01, RAW/SPC).

### b. **Entrenamiento y Evaluación**
- **Entrenamiento (EVA-02, FT):** Personalización avanzada de asistentes, adaptando vocabulario, estilo y reglas.
- **Evaluación (EVA-01, OSE; EVA-03, EVL):** Incluye autoevaluación de outputs, testing automático/manual y logging de decisiones (EVA-07, DL).
- Todos los procesos de entrenamiento y evaluación deben quedar trazados (DATA-02, CPV) y versionados para permitir rollback y análisis histórico.

### c. **Templates universales y documentación viva**
- Los **templates** (WF-06, PTR) permiten guardar prompts, workflows y configuraciones para rápida reutilización, asegurando coherencia en outputs y procedimientos.
- La **documentación viva** (DATA-04, LD) integra todos los templates, ejemplos y learnings actualizados al día.
- Templates y documentación deben estar referenciados cruzadamente con los README y knowledge base del repo.

---

## 4. **Relación y sinergia entre features y capas**

| Feature/Clase  | Actúa sobre     | Persiste | ¿Puede ser anulada? | Uso típico         | Ejemplo operativo   |
|----------------|----------------|----------|---------------------|--------------------|---------------------|
| ATT            | Sesión         | No*      | N/A                 | Input de datos     | Adjuntar PDF en sesión, resumirlo, no modifica global |
| MEM            | Todas          | Sí       | Solo por superior   | Recordar contexto  | Guardar aprendizajes, feedback iterativo              |
| PVC            | Prompt, GPT    | Sí       | Solo por versión    | Control de cambios | Testing de prompts/versiones en asistentes            |
| PTR            | Todos          | Sí       | Solo por update     | Reutilización      | Plantillas de onboarding, respuestas estándar         |
| OSE/EVL        | Output/Workflow| No       | N/A                 | QA y autoeval      | Logging de calidad de respuesta, feedback             |

\* Persiste solo si se integra a knowledge base/memoria (ej: un adjunto procesado puede ser guardado como fuente o evidencia en la KB).

---

## 5. **Reglas avanzadas y recomendaciones**

- **Toda acción relevante (entrenamiento, override, testing) debe registrarse en knowledge base o logs**.
- Para garantizar trazabilidad, los adjuntos relevantes deben ser referenciados por ruta/nombre en los outputs.
- Los templates universales deben estar versionados y asociados a flujos de onboarding y mantenimiento.
- Cada workflow debe documentar explícitamente su relación con las capas de instrucciones y las features utilizadas (ejemplo: “este workflow usa ATT, MEM, WF-03 y OUT-01”).

---

¿Expandimos con ejemplos de override de adjuntos, integración en workflows reales, o prefieres modelar un template universal completo para la gestión de sesiones y adjuntos?


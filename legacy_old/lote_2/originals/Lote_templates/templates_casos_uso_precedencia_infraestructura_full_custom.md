# TEMPLATES DE CASOS DE USO — PRECEDENCIA & INFRAESTRUCTURA FULL CUSTOM (AingZ_Repo)

> Plantillas y guías base para implementación y adaptación según entorno de uso — Versión 2025-07-13

---

## 1. Personalización Global (🔵)

### a. Propósito
Configurar reglas, templates y workflows universales que rijan todas las sesiones, asistentes y proyectos.

### b. Template base
```markdown
# Personalización Global
- Idioma predeterminado: Español
- Privacidad: ON
- Workflow universal: [workflow_analisis_estandar.md](./WF/universales/workflow_analisis_estandar.md)
- Plantillas recomendadas:
    - Respuesta estándar: [template_respuesta.md](./plantillas/template_respuesta.md)
    - Evaluación: [template_eval.md](./plantillas/template_eval.md)
- Regla: “Por defecto, aplica el workflow universal salvo override por capa inferior.”
- Referencias clave: README, knowledge base, matrices extendidas.
```

### c. Inputs permitidos
- Adjuntos temporales en cada chat.
- Referencias y links a recursos globales.
- Prompts puntuales.

### d. Output y persistencia
- Todos los outputs relevantes deben poder ser exportados y versionados en la knowledge base y logs.

### e. Cuándo preferir este entorno
- Necesidad de coherencia máxima y reglas/plantillas unificadas para toda la organización.
- Automatización de onboarding y QA cross-project.
- Cuando la personalización y compliance son críticas y se requiere control centralizado.

---

## 2. Proyectos / Workspaces (🟢)

### a. Propósito
Gestionar reglas, objetivos y workflows específicos por proyecto, habilitando personalización granular, integración de plantillas y registro detallado.

### b. Template base
```markdown
# Proyecto: [Nombre]
- Objetivo: [Definir]
- Metodología: [RAW/Específico]
- Templates/workflows aplicados:
    - Análisis: [workflow_analisis_X.md](../WF/analisis_X.md)
    - Output: [template_output_X.md](../plantillas/template_output_X.md)
- Referencias: [README del proyecto](./README.md), knowledge base, matriz de features.
- Checkpoints/versionado: Activado (DATA-02, CPV).
- Logging de overrides/anulaciones: ON
```

### c. Inputs permitidos
- Adjuntos, datasets, workflows y plantillas específicos.
- Inputs manuales y automáticos (integración continua, API, etc).

### d. Output y persistencia
- Outputs y aprendizajes se documentan en la knowledge base del proyecto y se exportan a la base global si son universales.

### e. Cuándo preferir este entorno
- Necesidad de segmentar equipos, tareas o entregables.
- Proyectos con lógica, reglas o flujos propios, distintos del global.
- Se requiere trazabilidad y control de versiones granular.

---

## 3. GPTs / Asistentes Personalizados (🟡)

### a. Propósito
Definir lógica, skills, límites y plantillas para un asistente IA particular, maximizando autonomía, especialización y experiencia custom.

### b. Template base
```markdown
# Asistente: [Nombre del GPT/Asistente]
- Skillset principal: [Listar]
- Tono y voz: [Formal/Informal/Técnico/etc]
- Templates y workflows asignados:
    - Respuestas técnicas: [template_tecnico.md](../plantillas/template_tecnico.md)
    - Procedimientos: [workflow_operativo.md](../WF/workflow_operativo.md)
- Integraciones: [APIs, herramientas externas]
- Límites: [Ética, privacidad, contexto permitido]
- Logging de actividad y feedback: ON
```

### c. Inputs permitidos
- Instrucciones y prompts ad-hoc.
- Inputs automáticos (vía API, webhooks, apps integradas).
- Plantillas y adjuntos custom.

### d. Output y persistencia
- Respuestas quedan logueadas por sesión/asistente.
- Aprendizajes se pueden trasladar a nivel global o de proyecto según pertinencia.

### e. Cuándo preferir este entorno
- Necesidad de asistentes especializados o para casos de uso recurrentes.
- Cuando se requiere máxima autonomía, integración o personalización en canales específicos.
- QA, soporte, capacitación, onboarding automatizado, etc.

---

# FIN


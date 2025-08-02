# KNOWLEDGE BASE — MATRIZ DE PRECEDENCIA & TEMPLATES UNIVERSALES (RAW)

> Recopilación estructurada y sintética — Versión 2025-07-13

---

## 1. Jerarquía y Precedencia de Instrucciones (Matriz)

| Nivel/Capa                   | Precedencia  | Persistencia     | ¿Anulable?        | Ejemplo de Input/Regla             | Features/módulos asociados             |
| ---------------------------- | ------------ | ---------------- | ----------------- | ---------------------------------- | -------------------------------------- |
| 🟥 Límites Éticos/Compliance | Absoluta     | Permanente       | ❌ No              | "Nunca compartas datos sensibles"  | SEC-01, SEC-02, SEC-03, SEC-04, SEC-05 |
| 🔵 Personalización Global    | Global       | Permanente       | ☑️ Por capa sup.  | "Responde en español"              | UX-01, UX-02, OUT-01, INT-04           |
| 🟢 Proyecto / Workspace      | Proyecto     | Hasta cierre     | ☑️ Por lower      | "Prioriza KPIs de sustentabilidad" | DATA-03, OUT-05, WF-09                 |
| 🟡 GPT/Asistente Pers.       | Asistente    | Sesión/instancia | ☑️ Por lower      | "Utiliza términos técnicos"        | EVA-02, UX-02, INT-05                  |
| 🟠 Conversación / Sesión     | Sesión       | Hasta cierre     | ☑️ Por prompt     | "Resume todo en tablas"            | WF-03, OUT-01, OUT-03, WF-02           |
| 🟨 Prompt / Comando          | Local máxima | Solo respuesta   | ☑️ Solo esa resp. | "Responde solo en JSON"            | OUT-02, OUT-01, OUT-03, WF-01          |

---

## 2. Interrelaciones y Herencia

- Herencia descendente: Global → Proyecto → GPT/Asistente → Sesión → Prompt.
- Anulación por override específico en capa inferior (prompt/sesión/GPT).
- Límite absoluto no anulable: Ética/Compliance.
- Persistencia solo si integra memoria (MEM), knowledge base o es registrada por workflow.

---

## 3. Input, Output y Gestión de Templates/Workflows Universales

### Input/Referencia

- **Adjuntos** (ATT): carga de archivos durante sesión/chat; pueden ser procesados, pero no persisten salvo acción manual.
- **Repositorios**: se referencia README, workflows universales, plantillas desde estructura centralizada (GitHub, Drive, Notion).
- **Instrucciones Globales**: referencia a workflows/templates universales en personalización global (ej: “usar workflow universal X en toda tarea”).
- **Carga Manual**: adjuntar/pastear template o flujo al inicio del chat para su uso inmediato.

### Output/Persistencia

- **Knowledge Base**: outputs relevantes se exportan manualmente a la KB o integran por instrucción explícita.
- **Versionado**: cada template/workflow tiene control de versiones (PVC) y se registra cambio en README y logs.
- **Documentación Viva**: toda integración, cambio o aprendizaje debe estar referenciado y accesible en la documentación principal.

### Gestión

- **Templates Universales**: ubicados en carpeta central; referenciados en global y en todos los README.
- **Workflows**: pueden cargarse de forma manual o automática (si la plataforma lo permite) y usarse por instrucción global, prompt puntual o adjunto.
- **Logs de override/conflictos**: registro de toda anulación de instrucciones en logs o knowledge base.
- **Auditoría**: siempre documentar versión, fecha, autor, referencia cruzada.

---

## 4. Features Relacionadas (matriz extendida)

- **SEC:** Ética, seguridad, compliance, autocuración.
- **CORE:** Adjuntos, análisis de datos, memoria.
- **DATA:** Gestión de proyectos, versionado, documentación viva, referencias.
- **WF:** RAW/específico, feedback iterativo, chaining, persistencia, control de versiones, reutilización, checklists.
- **OUT:** Output dirigido, modular, nivel de detalle, multiplataforma.
- **EVA:** Fine-tuning, autoevaluación, logging, resiliencia.
- **INT:** Roles, internacionalización, integración externa.
- **UX:** Personalización de tono, idioma, explicación, next steps.

---

## 5. Ejemplo de Template Universal y Personalización Global

```markdown
# Personalización Global (fragmento)
- Idioma por defecto: Español
- Límites de privacidad: ON
- Workflow universal: [workflow_analisis_estandar.md](./WF/universales/workflow_analisis_estandar.md)
- Regla: “Por defecto, aplica el workflow universal salvo indicación contraria.”
```

---

## 6. Casos de Input/Output

- Adjuntar workflow universal en un nuevo chat para que rija la sesión.
- Referenciar template global desde cualquier prompt: “Usar workflow universal X para esta tarea”.
- Outputs de workflows o análisis deben ser exportados/versionados a knowledge base o repositorio.

---

## 7. Logging de Excepciones/Overrides

| Fecha      | Nivel/Capa afectada | Instrucción original | Anulación por | Justificación      | Log/Referencia   |
| ---------- | ------------------- | -------------------- | ------------- | ------------------ | ---------------- |
| 2025-07-13 | Proyecto            | "Output en español"  | Prompt        | Prueba multilingüe | Session\_134.log |

---

# FIN


# MATRIZ DE PRECEDENCIA DE INSTRUCCIONES — FULL CUSTOM INFRAESTRUCTURA (AingZ_Repo)

> Versión 2025-07-13 — Enfoque: Uso avanzado y trazabilidad máxima. Excluye input puntual de chat/adjunto nuevo (ver nota final).

---

| Nivel/Capa                | Precedencia   | Persistencia   | ¿Anulable?      | Input habilitado                | Ejemplo de Input/Regla                                 | Features/módulos asociados                      |
|---------------------------|---------------|---------------|-----------------|-------------------------------|-------------------------------------------------------|-------------------------------------------------|
| 🟥 Límites Éticos/Compliance | Absoluta      | Permanente     | ❌ No           | Personalización Global / Proyecto / GPT | "Nunca compartas datos sensibles"                    | SEC-01, SEC-02, SEC-03, SEC-04, SEC-05         |
| 🔵 Personalización Global  | Global        | Permanente     | ☑️ Por capa superior | Infraestructura centralizada, templates universales | "Responde en español"                                | UX-01, UX-02, OUT-01, INT-04                   |
| 🟢 Proyecto / Workspace    | Proyecto      | Hasta cierre   | ☑️ Por inferior  | Workflows, templates, repositorios segmentados       | "Prioriza KPIs de sustentabilidad"                   | DATA-03, OUT-05, WF-09                         |
| 🟡 GPT/Asistente Personalizado | Asistente     | Instancia/sesión | ☑️ Por inferior  | Configuración custom (skills, roles, templates)      | "Utiliza términos técnicos"                           | EVA-02, UX-02, INT-05                          |
| 🟠 Conversación / Sesión   | Sesión        | Hasta cierre   | ☑️ Por prompt    | Plantillas cargadas al inicio, configuración previa  | "Resume todo en tablas"                              | WF-03, OUT-01, OUT-03, WF-02                   |
| 🟨 Prompt / Comando        | Local máxima  | Solo respuesta | ☑️ Solo esa resp.| No considerado (input chat/adjunto nuevo)*           | "Responde solo en JSON"                              | OUT-02, OUT-01, OUT-03, WF-01                  |

---

## Interrelaciones, herencia y uso
- Herencia descendente: Global → Proyecto → GPT/Asistente → Sesión.
- Anulación solo por override explícito en capa inferior preexistente.
- Límite absoluto no anulable: Ética/Compliance.
- **Adjuntos cargados o prompts en chat nuevo** no alteran ni modifican la matriz de precedencia para la infraestructura: solo impactan la sesión actual y se excluyen en la lógica de precedencia estructural.

---

## Possibilidades de Input habilitado por capa
- **Personalización Global:** Templates universales, workflows globales, integración a nivel infraestructura (no adjuntos puntuales de chat).
- **Proyecto:** Workflows, plantillas y configuraciones segmentadas asociadas a repositorio del proyecto, onboarding y outputs registrados.
- **GPT/Asistente:** Skills, roles, workflows y plantillas específicas del asistente, lógica custom (por configuración, no por chat).
- **Sesión:** Plantillas cargadas por workflow, configuración previa o memoria (no por adjunto o prompt puntual en chat).

---

## Features/Módulos integrados
- **SEC:** Ética, seguridad, compliance.
- **CORE:** Memoria persistente, análisis de datos, interpretación de código.
- **DATA:** Gestión de proyectos, documentación viva, versionado, referencias.
- **WF:** Persistencia de contexto, workflows, chaining, templates reutilizables, control de versiones.
- **OUT:** Output dirigido/modular, nivel de detalle, multiplataforma.
- **EVA:** Fine-tuning, autoevaluación, logging.
- **INT:** Roles, integración externa, internacionalización.
- **UX:** Personalización de voz, tono, idioma.

---

## Nota Final
*La matriz excluye explícitamente inputs ad-hoc de chat nuevo (adjuntos/prompt), que solo afectan la sesión puntual y no la infraestructura, precedencia ni lógica de configuración estructural del sistema.*

# FIN


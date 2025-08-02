# Diagrama Visual — Jerarquía de Instrucciones (AingZ\_Repo)

> Borrador visual | Versión 2025-07-13 | Autor: GZ (AingZ)

---

## DIAGRAMA (formato texto, para pasar a herramienta visual si lo deseas)

```mermaid
graph TD
    SUB["🚦Límites Éticos / Seguridad / Compliance<br/>(No anulable)"]:::etico
    GLO["🌐 Personalización Global<br/>(Perfil/Org)"]:::global
    PRO["🗂️ Proyecto / Workspace"]:::proyecto
    GPT["🤖 GPT / Asistente Personalizado"]:::gpt
    SES["💬 Conversación / Sesión"]:::sesion
    PRM["⚡ Prompt / Comando Específico"]:::prompt
    SUB-->|Prevalece sobre todo|SUB
    GLO-->PRO
    PRO-->GPT
    GPT-->SES
    SES-->PRM
    PRM-->|Puede anular|SES
    PRM-->|Puede anular|GPT
    PRM-->|Puede anular|PRO
    PRM-->|Puede anular|GLO
    style SUB fill:#FFCCCC,stroke:#E53E3E,stroke-width:2px
    style GLO fill:#BEE3F8,stroke:#3182CE,stroke-width:2px
    style PRO fill:#C6F6D5,stroke:#2F855A,stroke-width:2px
    style GPT fill:#FAF089,stroke:#ECC94B,stroke-width:2px
    style SES fill:#FBD38D,stroke:#DD6B20,stroke-width:2px
    style PRM fill:#FFF9C4,stroke:#F6E05E,stroke-width:2px
```

---

## LEYENDA

- **🚦 Límites Éticos / Seguridad / Compliance:** No pueden ser anulados por ninguna instrucción inferior.
- **🌐 Personalización Global:** Valores, políticas y parámetros que aplican a todo el entorno/organización.
- **🗂️ Proyecto / Workspace:** Objetivos, reglas y outputs específicos de un área o proyecto.
- **🤖 GPT / Asistente Personalizado:** Skills, reglas y personalidad asignada a un asistente concreto.
- **💬 Conversación / Sesión:** Instrucciones temporales dadas en el contexto de una conversación activa.
- **⚡ Prompt / Comando Específico:** Instrucciones puntuales o excepcionales que pueden anular instrucciones de capas superiores solo para esa respuesta.

---

## OBSERVACIONES Y REGLAS CLAVE

- **Precedencia:**
  - El prompt/comando puntual tiene máxima precedencia para la respuesta actual.
  - Las capas se heredan descendiendo (global → proyecto → gpt → sesión → prompt).
  - Excepciones y límites (ética/seguridad/compliance) siempre prevalecen.
- **Anulación:**
  - Un prompt puede anular instrucciones superiores SOLO de forma temporal.
  - Para anulación persistente, se debe modificar la instrucción en la capa superior correspondiente.
- **Herencia:**
  - Todo lo no explicitamente anulado se hereda de la capa superior más cercana.
- **Conflicto:**
  - Si dos instrucciones de igual peso compiten, se prioriza la más reciente o la más específica.
- **Memoria y Feedback:**
  - La memoria puede hacer persistente una instrucción dada en capa inferior, si así se configura (ver features MEM, IFB, CTX de la matriz).

---

## REFERENCIAS Y FUENTES

- [README master\_plan](README.md)
- [master\_plan\_aingz\_infrastructure.md](master_plan_aingz_infrastructure.md)
- [matriz\_extendida\_features\_chatgpt\_workflow.md](matriz_extendida_features_chatgpt_workflow.md)
- [doc/croquis-mapeo-features-prompts.md](doc/croquis-mapeo-features-prompts.md)
- [matrices/control\_trazabilidad\_fuentes\_chatgpt\_workflow.md](matrices/control_trazabilidad_fuentes_chatgpt_workflow.md)

---

¿Te gustaría que exporte este diagrama a PNG/SVG o lo subo a alguna herramienta visual (excalidraw, diagrams.net, etc)?


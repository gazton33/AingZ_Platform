---

## file: ruleset\_max\_plan\_plus\_ssot\_v2.md version: 2.0 status: canonical created\_at: 2025-09-21 owner: AingZ\_Platform scope: ChatGPT Plan Plus semantic: RULESET\_MAX ssot: true purpose: Documento único y suficiente de DB para Plan Plus; integra todo lo validado en este hilo + Canvas. notes: "Sin bloques de test. Solo resultados confirmados y objetos a validar en próximas iteraciones."

# Precedencia efectiva

1. **Project Instructions** → 2) **Custom Instructions** (global) → 3) **Instrucciones del GPT** → 4) **Herramientas/Capacidades** → 5) Preferencias de app.

---

# Matriz RULESET\_MAX — Plan Plus (SSOT)

| CODE\_MAP | layer   | object                         | scope         | limits\_plus                                                               | precedence\_note                        | status       | updated\_at | notes\_migration                          |
| --------- | ------- | ------------------------------ | ------------- | -------------------------------------------------------------------------- | --------------------------------------- | ------------ | ----------- | ----------------------------------------- |
| RULE      | GLOBAL  | enable\_customization          | cuenta        | toggle on/off                                                              | Afecta solo **nuevos** chats            | active       | 2025-09-21  | Map→ RULE.GLOBAL.ENABLE\_CUSTOMIZATION    |
| RULE      | GLOBAL  | custom\_instructions\_fields   | cuenta        | **1500** chars **incl. espacios y ENTER**                                  | Overridden por **Project Instructions** | validated    | 2025-09-21  | Map→ RULE.GLOBAL.CI.FIELDS                |
| RULE      | GLOBAL  | about\_you\_fields             | cuenta        | **1500** chars **incl. espacios y ENTER** (Apodo, Ocupación, Más sobre ti) | —                                       | validated    | 2025-09-21  | Map→ RULE.GLOBAL.ABOUT\_YOU               |
| RULE      | GLOBAL  | personality\_selector          | cuenta        | Presets: **Predeterminada, Cínica, Robot, Atenta, Friki**                  | CI/Project pueden override estilo       | active       | 2025-09-21  | Map→ RULE.GLOBAL.PERSONALITY              |
| ENV       | GLOBAL  | memory\_reference\_saved       | cuenta        | toggle on/off                                                              | Interactúa con `reference_history`      | active       | 2025-09-21  | Map→ ENV.GLOBAL.MEM.REF\_SAVED            |
| ENV       | GLOBAL  | memory\_reference\_history     | cuenta        | toggle on/off                                                              | Requiere `ref_saved` on                 | active       | 2025-09-21  | Map→ ENV.GLOBAL.MEM.REF\_HISTORY          |
| SPEC      | GLOBAL  | recording\_history\_access     | cuenta        | Toggle: **Consultar historial de grabaciones**                             | Acceso condicionado por consentimiento  | active       | 2025-09-21  | Map→ SPEC.GLOBAL.REC.HISTORY              |
| ENV       | GLOBAL  | memory\_saved\_item\_limit     | cuenta        | **999** chars por entrada (contenido íntegro)                              | Solo Memoria **global**                 | validated    | 2025-09-21  | Usar payload compacto; punteros para >999 |
| ENV       | GLOBAL  | memory\_saved\_count\_observed | cuenta        | **≥ 72** entradas sin rechazo (tope no medido)                             | Continuar medición por lotes de 30      | observed     | 2025-09-21  | Programar corrida de tope real            |
| PRC       | GLOBAL  | memory\_saved\_ops\_procedure  | cuenta        | Activación, verificación UI, limpieza                                      | —                                       | active       | 2025-09-21  | Procedimiento documentado 2025‑09‑21      |
| PRC       | PROJECT | project\_instructions          | proyecto      | —                                                                          | **Override** sobre CI y Personality     | active       | 2025-09-21  | Map→ PRC.PROJECT.INSTRUCTIONS             |
| ENV       | PROJECT | project\_files                 | proyecto      | Límite según Plus (no cuantificado aquí)                                   | —                                       | to\_validate | 2025-09-21  | Medir en sesión dedicada                  |
| RULE      | GPT     | gpt\_instructions              | GPT           | —                                                                          | Solo dentro del GPT                     | active       | 2025-09-21  | Map→ RULE.GPT.INSTR                       |
| ENV       | GPT     | gpt\_knowledge                 | GPT           | Límite por archivo y tokens (no cuantificado aquí)                         | No comparte con otros GPT               | to\_validate | 2025-09-21  | Medir/confirmar antes de poblar DB        |
| SPEC      | GPT     | gpt\_actions\_capabilities     | GPT           | Depende de disponibilidad en Plus                                          | Priorización por herramienta invocada   | active       | 2025-09-21  | Map→ SPEC.GPT.ACTIONS                     |
| SPEC      | TOOLS   | deep\_research                 | chat/proyecto | Disponible en Plus si habilitado                                           | Usa web y archivos con citación         | active       | 2025-09-21  | Map→ SPEC.TOOLS.DEEP\_RESEARCH            |
| SPEC      | TOOLS   | data\_analysis\_python         | chat/archivo  | Intérprete Python                                                          | Tablas/plots                            | active       | 2025-09-21  | Map→ SPEC.TOOLS.PY                        |
| WK        | TOOLS   | canvas                         | chat/proyecto | Lienzo de texto/código                                                     | Co‑edición lateral                      | active       | 2025-09-21  | Map→ WK.TOOLS.CANVAS                      |
| WK        | TOOLS   | tasks\_automations             | cuenta        | Recordatorios/acciones programadas                                         | Soporte por app                         | active       | 2025-09-21  | Map→ WK.TOOLS.TASKS                       |
| ENV       | APP     | advanced\_web\_search          | dispositivo   | Toggle **Búsqueda en Internet**                                            | Permite citar web                       | active       | 2025-09-21  | Map→ ENV.APP.WEB\_SEARCH                  |
| ENV       | APP     | advanced\_programming          | dispositivo   | Toggle **Programar**                                                       | Intérprete de código                    | active       | 2025-09-21  | Map→ ENV.APP.PROGRAMMING                  |
| ENV       | APP     | advanced\_canvas               | dispositivo   | Toggle **Lienzo**                                                          | Activa Canvas en chat                   | active       | 2025-09-21  | Map→ ENV.APP.CANVAS                       |
| ENV       | APP     | advanced\_voice                | dispositivo   | Toggle **Voz avanzada**                                                    | Depende de app/región                   | active       | 2025-09-21  | Map→ ENV.APP.VOICE                        |
| ENV       | UPLOADS | uploads\_limits                | chat/proyecto | Límites según Plus (no cuantificados aquí)                                 | Restringe contexto                      | to\_validate | 2025-09-21  | Confirmar tamaños/tokens                  |
| SPEC      | CONNECT | connectors\_chat               | cuenta/org    | Alcance limitado en Plus                                                   | Depende de región                       | to\_validate | 2025-09-21  | Ver disponibilidad real                   |

---

## Campos DB (esquema)

```yaml
schema:
  - CODE_MAP: [RULE, SPEC, ENV, PRC, WK, CHK, VALD, AUDT]
  - layer: [GLOBAL, PROJECT, GPT, TOOLS, CONNECT, UPLOADS, PRIV, APP, MODELOS]
  - object: string
  - scope: string
  - limits_plus: string
  - precedence_note: string
  - status: [active, validated, observed, to_validate, beta, deprecated, n/a]
  - updated_at: date
  - notes_migration: string
```

## Notas operativas

- **Memoria global**: límite **999** por entrada y **≥72** observadas sin rechazo. Para >999, guardar **punteros** o **fragmentar**.
- **Customize**: 4 campos principales con **1500** caracteres incluyendo espacios y ENTER. Personalidades: Predeterminada, Cínica, Robot, Atenta, Friki.
- **Proyectos**: Project Instructions tienen precedencia.
- **Avanzado (app)**: toggles de Web, Programar, Lienzo, Voz.

## Alcances pendientes de cuantificar (mantener "to\_validate")

- Límites exactos de **Project files**, **GPT Knowledge** y **Uploads** en Plus.
- Disponibilidad regional de **Connectors**.

## Estado de purga: EJECUTADA — 2025-09-21

- Documentos marcados **deprecated** y consolidados en este SSOT v2:
  - "Matriz RULESET\_MAX — Configuración ChatGPT (Plan Plus) — Draft v0"
  - "Customize — Opciones completas (Plan Plus) — Draft v0"
  - "Customize — Validación UI y Test Plan (Plus) — Draft v0"
  - "Customize — Strings de prueba exactos (Plan Plus) — Pack v0"
  - "RULESET\_MAX — Memoria guardada global (Plus) — v1"
- Documento canónico activo: **ruleset\_max\_plan\_plus\_ssot\_v2.md** (este archivo).

---

## OutputTemplate

```yaml
output_example:
  status: OK
  generated_by: ai
  created_at: 2025-09-21T13:00:00-03:00
  params:
    - work_type: Migracion
    - priorities: [evolvability, reliability, performance, simplicity, cost, auditability]
    - mode: RULESET_MAX
  result:
    - ready_to_use: true
    - matrices: [ruleset_max_plan_plus_ssot_v2]
  log: [merge, dedup, purge_plan]
```


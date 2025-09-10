---

id: ruleset\_obsidian\_canvas\_stack\_v1\_0 version: 1.0.0 created\_at: 2025-08-31T20:45:00-03:00 authors: [ai] scope: Obsidian Desktop + Canvas + Template IA↔Humano status: draft links: template\_ref: Template IA↔humano — Obsidian + Canvas V1 policies:

- No asíncrono.
- Sin PII.
- Cambios bajo control Git.

---

# RULESET — Obsidian+Canvas Stack Inventory & Form

> Propósito: registrar el stack real (core + community) y validar requisitos de configuración para operar el template IA↔Humano. Llenar y marcar.

## A) Contexto del hilo

- Plataforma: Obsidian Desktop
- Vista: plugins core y community activos según capturas provistas el 2025-08-31.
- Objetivo: habilitar interacción IA↔humano con botones, formularios, metadatos y vistas.

## B) Inventario de plugins — Community

> Estado según capturas del 2025-08-31. Marca Validado cuando lo confirmes en tu bóveda.

| Plugin        | Versión | Activo | Validado | Uso                                      | Nota |
| ------------- | ------- | ------ | -------- | ---------------------------------------- | ---- |
| Buttons       | 0.9.13  | [x]    | [ ]      | Botones que disparan comandos/plantillas |      |
| Calendar      | 1.5.10  | [x]    | [ ]      | Vista de calendario para sesiones        |      |
| Commander     | 0.5.4   | [x]    | [ ]      | Comandos en UI y macros                  |      |
| Dataview      | 0.5.68  | [x]    | [ ]      | Consultas y tablas                       |      |
| Excalidraw    | 2.15.1  | [x]    | [ ]      | Diagramas y mapas                        |      |
| Git           | 2.35.0  | [x]    | [ ]      | Versionado y backup                      |      |
| Kanban        | 2.0.51  | [x]    | [ ]      | Tablero de estados                       |      |
| Linter        | 1.29.2  | [x]    | [ ]      | Normalización YAML/MD                    |      |
| Meta Bind     | 1.4.5   | [x]    | [ ]      | Inputs ligados a properties              |      |
| Metadata Menu | 0.8.9   | [x]    | [ ]      | Tipado/edición de properties             |      |
| Modal Forms   | 1.61.0  | [x]    | [ ]      | Formularios de alta/edición              |      |
| QuickAdd      | 2.1.0   | [x]    | [ ]      | Capturas y macros                        |      |
| Tasks         | 7.21.0  | [x]    | [ ]      | Gestión de tareas avanzada               |      |
| Templater     | 2.14.1  | [x]    | [ ]      | Plantillas JS                            |      |
| Tracker       | 1.17.0  | [x]    | [ ]      | Métricas y gráficos                      |      |

## C) Inventario de plugins — Core

> El usuario indicó “core todos activos”. `Publish` aparece apagado en capturas.

| Plugin Core         | Activo | Nota           |
| ------------------- | ------ | -------------- |
| Audio recorder      | [x]    |                |
| Backlinks           | [x]    |                |
| Bases               | [x]    |                |
| Bookmarks           | [x]    |                |
| Canvas              | [x]    |                |
| Command palette     | [x]    |                |
| Daily notes         | [x]    |                |
| File recovery       | [x]    |                |
| Files               | [x]    |                |
| Footnotes view      | [x]    |                |
| Format converter    | [x]    |                |
| Graph view          | [x]    |                |
| Note composer       | [x]    |                |
| Outgoing links      | [x]    |                |
| Outline             | [x]    |                |
| Page preview        | [x]    |                |
| Properties view     | [x]    |                |
| Publish             | [ ]    | OFF en captura |
| Quick switcher      | [x]    |                |
| Random note         | [x]    |                |
| Search              | [x]    |                |
| Slash commands      | [x]    |                |
| Slides              | [x]    |                |
| Sync                | [x]    |                |
| Tags view           | [x]    |                |
| Templates           | [x]    |                |
| Unique note creator | [x]    |                |
| Web viewer          | [x]    |                |
| Word count          | [x]    |                |
| Workspaces          | [x]    |                |



> Marca los que queden activos en este proyecto.

-

## D) Config mínima requerida (rellenar)

- **Carpeta base del proyecto**: `{{VALUE:carpeta_base}}`
- **Carpeta de templates (Templater)**: `{{VALUE:tpl_dir}}`
- **Archivo template IA↔Humano por defecto**: `{{VALUE:tpl_file}}`
- **Form Modal Forms (ID)**: `{{VALUE:mf_form_id}}`
- **Estados Tasks custom**: `{{VALUE:tasks_statuses}}`
- **Frecuencia de Git auto‑commit**: `{{VALUE:git_freq}}`
- **Tabla DB Folder (si aplica)**: `{{VALUE:dbf_path}}`

## E) Checks de operación

-

## F) Matriz de compatibilidad (selección)

| Módulo         | Plugin      | Requerido | Estado | Nota |
| -------------- | ----------- | --------- | ------ | ---- |
| Captura sesión | QuickAdd    | Sí        | [ ]    |      |
| Form de alta   | Modal Forms | Sí        | [ ]    |      |
| Inputs UI      | Meta Bind   | Sí        | [ ]    |      |
| Botones        | Buttons     | Sí        | [ ]    |      |
| Plantillas     | Templater   | Sí        | [ ]    |      |
| Tareas         | Tasks       | Sí        | [ ]    |      |
| Vistas         | Dataview    | Sí        | [ ]    |      |
| Métricas       | Tracker     | Opcional  | [ ]    |      |
| Diagramas      | Excalidraw  | Opcional  | [ ]    |      |
| Tablero        | Kanban      | Opcional  | [ ]    |      |
| Versionado     | Git         | Sí        | [ ]    |      |
| Normalización  | Linter      | Sí        | [ ]    |      |

## G) Acciones de setup

-

## H) Tokens de post‑proceso

- `→ move: <ruta>`
- `→ note: <texto>`
- `→ tag: <RULE|SPEC|PRC|ENV|CHK|VALD|AUDT|RPT>`

## E2) Excalidraw — configuración requerida (máxima jerarquía)

-

## J) Pipelines operativos (stack actual)

**P0 — Ingesta estructurada**\
Buttons ▶ QuickAdd ▶ Modal Forms ▶ Templater ▶ Meta Bind → Front‑matter listo.

- Salida: nota de sesión en `{{VALUE:carpeta_base}}` con properties completas.

**P1 — Plan & tareas**\
Meta Bind (edición rápida) + Tasks (due/recurrencia) + Dataview (vista).

- Salida: tabla TASK y filtros por estado/fecha.

**P2 — Diagrama primero (Excalidraw)**\
Crear/actualizar `00_INDEX.excalidraw` con nodos: Objetivo, Entradas, Tareas, ADR, Métricas.

- Salida: links funcionales y embed del índice en la nota madre.

**P3 — Métricas**\
Tracker ← front‑matter (`coverage_pct`, `latency_budget`, `confianza_media`).

- Salida: gráfico de línea/barra en panel “Métricas”.

**P4 — Versionado**\
Obsidian Git auto‑commit + manual antes de cambios mayores.

- Salida: historial limpio por lote (ingesta, diagrama, cierre).

**P5 — Review / Lock**\
Linter + Checklist de entrega → tag `locked` y release.

## K) Plan de pruebas rápido (tick al validar)

-

## L) Snippets listos para pegar

**Botón — Nueva sesión IA**

```button
name Nueva sesión IA
type command
action Templater: Create new note from template
```

**Meta Bind — selector de horizonte**

```meta-bind-input
frontmatterKey: horizon
type: select
options: [MVP, 6-12m, >12m]
```

**Tasks — consulta básica**

```tasks
not done
path includes {{VALUE:carpeta_base}}
sort by due
```

**Dataview — tabla de sesiones**

```dataview
TABLE file.link AS Nota, objective, horizon
FROM "{{VALUE:carpeta_base}}"
WHERE !completed
SORT file.ctime DESC
```

## I) Cierre

-


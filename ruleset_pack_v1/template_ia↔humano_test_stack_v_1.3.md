---
id: ai_human_test_stack_v1_3
version: 1.3.0
created_at: 2025-09-02T09:00:00-03:00
authors: [ai]
status: test
scope: Obsidian Desktop (Core‑first: Bases, Canvas, Properties)
stack_core:
  - Bases
  - Canvas
  - Properties
  - Properties view
stack_community:
  - Buttons
  - QuickAdd
  - Modal Forms
  - Templater
  - Meta Bind
  - Metadata Menu (opcional)
  - Dataview (opcional)
  - Tasks
  - Tracker (opcional)
  - Kanban (opcional)
policies:
  - Sin PII
  - No asíncrono
  - Versionado fuera de Obsidian (CLI/externo). Obsidian Sync opcional (pago).
---

# Template IA↔Humano — TEST del stack (Core‑first, sin Git)

> Objetivo: validar un flujo completo usando **Bases + Properties + Canvas** como núcleo, y comunidad sólo donde no exista equivalente core.

## 0) Config mínima
- **carpeta_base**: `{{VALUE:carpeta_base}}`
- **folder_sessions**: `sessions/`
- **folder_diagrams**: `diagrams/`
- **tpl_dir**: `{{VALUE:tpl_dir}}`
- **tpl_file**: `{{VALUE:tpl_file}}`
- **mf_form_id**: `{{VALUE:mf_form_id}}`

## 1) Semilla de sesión (front‑matter)
```yaml
---
id: ai_sess_<YYYYMMDD_HHmm>
objective: ""
horizon: MVP
stakeholders: [GZ]
status: draft
coverage_pct: 0
latency_budget: 0
due:  
tags: [ai/humano, stack/test]
---
```

## 2) Propiedades (core)
- Abrir **Properties view → File properties** para editar `objective,horizon,status,due`.
- Usar **All properties** para auditar tipos y reutilización.

## 3) Base maestra (core Bases)
1. Crear **Base** `AI_HUM_SESIONES` apuntando a `sessions/`.
2. Columnas: `file (link)`, `objective (text)`, `horizon (select)`, `status (select)`, `due (date)`, `coverage_pct (number)`, `latency_budget (number)`, `stakeholders (list)`, `tags (tags)`.
3. Vista `open`: filtro `status != locked`, orden por `due` asc.

**Ejemplo de `.base` (YAML sintético)**
```yaml
version: 1
source: { path: "sessions/" }
views:
  - id: open
    type: table
    columns:
      - { key: file }
      - { key: objective }
      - { key: horizon }
      - { key: status }
      - { key: due }
      - { key: coverage_pct }
      - { key: latency_budget }
    filter: 'status != "locked"'
    sort: [{ key: due, dir: asc }]
```

**Cross‑check con Dataview (opcional)**
```dataview
TABLE file.link AS Nota, objective, horizon, status, due
FROM "{{VALUE:carpeta_base}}/sessions"
WHERE status != "locked"
SORT due ASC
```

## 4) HUB visual (core Canvas)
- Crear `diagrams/00_INDEX.excalidraw` como mapa con nodos **Objetivo / Entradas / Tareas / ADR / Métricas**.
- Enlazar cada nodo a secciones de esta nota.
- Embed:
```
![[diagrams/00_INDEX.excalidraw|900]]
```

## 5) Captura y formularios (community donde aporta valor)
**Buttons**
```button
name Nueva sesión IA
type command
action Templater: Create new note from template
```
**Modal Forms + Templater**
```tpl
<%*
const mf = app.plugins.plugins.modalforms?.api;
if (mf) {
  const data = await mf.openForm('{{VALUE:mf_form_id}}');
  if (data) await app.fileManager.processFrontMatter(tp.config.target_file, fm => Object.assign(fm, data.getData()));
}
-%>
```
**Meta Bind**
```meta-bind-input
frontmatterKey: status
type: select
options: [draft, active, review, locked]
```

## 6) Tareas y métricas
**Tasks**
```tasks
not done
path includes {{VALUE:carpeta_base}}/sessions
sort by due
```
**Tracker (opcional)**
````markdown
```tracker
searchType: frontmatter
searchTarget: coverage_pct
folder: {{VALUE:carpeta_base}}/sessions
output: line
```
````

## 7) Sustituciones Core↔Community
| Capacidad | Core preferido | Alternativa community | Selección |
|---|---|---|---|
| Tablas/DB | **Bases** | Database Folder | [x] Core |
| Propiedades UI | **Properties view** | Metadata Menu | [x] Core / [ ] Community |
| Vistas/consultas | — | **Dataview** | [ ] Core / [x] Community (opcional) |
| Tareas | — | **Tasks** | [x] Community |
| Diagramas | **Canvas** (+ Excalidraw para dibujo) | — | [x] Core + Community |
| Versionado | **Externo / Obsidian Sync (pago)** | Obsidian‑Git (no usar) | [x] Externo |

## 8) Plan de pruebas ampliado
- [ ] P0 Alta: botón crea nota en `sessions/` desde el template.
- [ ] P0 Form: Modal Forms guarda `objective,horizon,status,due` en front‑matter.
- [ ] P1 Bases: vista `open` muestra ≥1 fila y permite edición inline.
- [ ] P1 Cross‑check: mismo conteo en Bases y Dataview.
- [ ] P2 Canvas: embed `00_INDEX.excalidraw` visible; enlaces shape→sección operativos.
- [ ] P3 Tasks: bloque lista pendientes sin errores.
- [ ] P4 Tracker: línea de `coverage_pct` renderizada.
- [ ] P5 Lock: cambiar `status→locked` y verificar exclusión en vistas.

## 9) ADR‑mini
- **Contexto**: Core‑first para DB/propiedades; sin Git interno.
- **Decisión**: Adoptar Bases + Properties + Canvas; mantener Tasks/Buttons/Forms.
- **Consecuencias**: Menos dependencias; edición inline en Base; validación cruzada con Dataview.
- **Evidencia**: §8 aprobado.

## 10) Checklist de cierre
- [ ] RULESET validado (core‑first)  
- [ ] `locked` aplicado
- [ ] Snapshot de capturas actualizado  
- [ ] Respaldo externo/Sync verificado


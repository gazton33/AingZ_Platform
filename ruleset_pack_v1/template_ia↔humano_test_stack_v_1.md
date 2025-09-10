---
id: ai_human_test_stack_v1_2
version: 1.2.0
created_at: 2025-08-31T21:20:00-03:00
authors: [ai]
status: test
scope: Obsidian Desktop + Canvas + Excalidraw prioridad
stack_min:
  community:
    - {name: Buttons, version: 0.9.13}
    - {name: Calendar, version: 1.5.10}
    - {name: Commander, version: 0.5.4}
    - {name: Dataview, version: 0.5.68}
    - {name: Excalidraw, version: 2.15.1}
    - {name: Git, version: 2.35.0}
    - {name: Kanban, version: 2.0.51}
    - {name: Linter, version: 1.29.2}
    - {name: Meta Bind, version: 1.4.5}
    - {name: Metadata Menu, version: 0.8.9}
    - {name: Modal Forms, version: 1.61.0}
    - {name: QuickAdd, version: 2.1.0}
    - {name: Tasks, version: 7.21.0}
    - {name: Templater, version: 2.14.1}
    - {name: Tracker, version: 1.17.0}
  core:
    active: true
policies:
  - No asíncrono
  - Sin PII
  - Cambios bajo control Git
---

# Template IA↔Humano — TEST del stack (Core‑first + Bases)

> Meta: validar el pipeline con **prioridad Core** donde haya solapamiento. Excalidraw es hub visual de máxima jerarquía.

## 0) Config mínima
- **carpeta_base**: `{{VALUE:carpeta_base}}`
- **tpl_dir**: `{{VALUE:tpl_dir}}`
- **tpl_file**: `{{VALUE:tpl_file}}`
- **mf_form_id**: `{{VALUE:mf_form_id}}`
- **git_auto_commit**: `{{VALUE:git_freq}}`
- **folder_diagrams**: `diagrams/`
- **folder_sessions**: `sessions/`

## 1) Semilla de nota de sesión (front‑matter)
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

## 2) Botonera
**Nueva sesión IA**
```button
name Nueva sesión IA
type command
action Templater: Create new note from template
```

**Cadena con QuickAdd (opcional)**
```button
name Alta sesión IA (QA)
type command
action QuickAdd: Choice: Alta sesión IA
```

## 3) Alta por formulario (Modal Forms)
```tpl
<%*
const mf = app.plugins.plugins.modalforms?.api;
if (mf) {
  const data = await mf.openForm('{{VALUE:mf_form_id}}');
  if (data) await app.fileManager.processFrontMatter(tp.config.target_file, fm => Object.assign(fm, data.getData()));
}
-%>
```

**Sugerencia de campos del form**
- objective: text
- horizon: select [MVP, 6-12m, >12m]
- stakeholders: multiselect [GZ, Equipo]
- status: select [draft, active, review, locked]
- due: date
- coverage_pct: number
- latency_budget: number

## 4) Inputs vinculados (Meta Bind)
```meta-bind-input
frontmatterKey: status
type: select
options: [draft, active, review, locked]
```

## 5) HUB visual — Excalidraw
- Crear `diagrams/00_INDEX.excalidraw`.
- Nodos: **Objetivo**, **Entradas**, **Tareas**, **ADR**, **Métricas**.
- Enlazar cada nodo a secciones de esta nota.
- Activar **auto‑export SVG keep‑in‑sync**.

**Embed**
```
![[diagrams/00_INDEX.excalidraw|900]]
```

## 6) Base de datos — enfoque Core (Bases)
> Core **Bases** reemplaza tablas tipo “database” de terceros. Usarlo como vista maestra.

1. Crear Base llamada `AI_HUM_SESIONES` apuntando a `sessions/`.
2. Definir columnas:
   - `file` (link) — primaria
   - `objective` (text)
   - `horizon` (select)
   - `status` (select)
   - `due` (date)
   - `coverage_pct` (number)
   - `latency_budget` (number)
   - `stakeholders` (list)
   - `tags` (tags)
3. Habilitar filtros: `status != locked` y orden por `due` asc.
4. Guardar vista `AI_HUM_SESIONES::open`.

**Cross‑check con Dataview**
```dataview
TABLE file.link AS Nota, objective, horizon, status, due
FROM "{{VALUE:carpeta_base}}/sessions"
WHERE status != "locked"
SORT due ASC
```

> Criterio de aceptación: **conteo filas** Bases == Dataview, y columnas no vacías en `objective,horizon,status`.

## 7) Tareas (Tasks)
```tasks
not done
path includes {{VALUE:carpeta_base}}/sessions
sort by due
```

## 8) Métricas (Tracker)
````markdown
```tracker
searchType: frontmatter
searchTarget: coverage_pct
folder: {{VALUE:carpeta_base}}/sessions
output: line
```
````

## 9) Kanban (opcional)
- Crear `kanban/ai_hum_sesiones.md` con columnas `Backlog|Doing|Review|Done`.
- Arrastrar enlaces de sesiones.

## 10) Git y Linter
- Git: auto‑commit cada `{{VALUE:git_freq}}`; manual antes de lock.
- Linter: normalizar YAML al guardar.

## 11) Matriz Core‑first (sustituciones)
| Capacidad | Preferencia Core | Alternativa community | Selección |
|---|---|---|---|
| Tablas tipo DB | **Bases** | Database Folder (no requerido) | [ ] Core [ ] Community |
| Vistas y consultas | **Dataview** | Projects | [x] Core [ ] Community |
| Propiedades UI | **Properties view** | Metadata Menu | [x] Core [ ] Community |
| Tareas | — | **Tasks** | [ ] Core [x] Community |
| Diagramas | — | **Excalidraw** | [ ] Core [x] Community |
| Botones/macros | — | **Buttons/QuickAdd/Commander** | [ ] Core [x] Community |

## 12) Plan de pruebas ampliado
- [ ] P0 Ingesta: botón crea nota desde template en `sessions/`.
- [ ] P0 Form: Modal Forms guarda `objective,horizon,status,due`.
- [ ] P1 Bases: vista `AI_HUM_SESIONES::open` muestra ≥1 fila.
- [ ] P1 Cross‑check: Dataview y Bases devuelven mismo conteo.
- [ ] P2 Tareas: bloque Tasks lista pendientes sin error.
- [ ] P2 Excalidraw: embed ok; enlaces shape→sección operativos.
- [ ] P3 Tracker: línea de `coverage_pct` renderizada.
- [ ] P4 Git: commit auto + manual visibles en historial.
- [ ] P5 Linter: YAML normalizado.
- [ ] P6 Lock: status→`locked`, exclusión en vistas.

## 13) ADR‑mini
- **Contexto**: Core‑first para DB y propiedades.
- **Decisión**: Adoptar Bases+Dataview; mantener Tasks/Excalidraw/Buttons.
- **Consecuencias**: Menos dependencias externas; vistas estables; queries Dataview para validación.
- **Evidencia**: pruebas §12 aprobadas.

## 14) Checklist de cierre
- [ ] RULESET validado  
- [ ] `locked` aplicado  
- [ ] Commit: `test(stack): core-first OK`  
- [ ] Snapshot de capturas actualizado


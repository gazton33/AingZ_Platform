---

## id: test\_obsidian\_stack\_all\_plugins version: 1.0.2 created\_at: 2025-09-09T00:00:00Z authors: [ai] scope: Obsidian Desktop — Core-first (Bases/Canvas/Properties) notes: Checklist ejecutable para validar el stack antes del RULESET final. tags: [stack/test, obsidian]

# Test Suite — Obsidian Plugins (Core + Community)

> Meta: ejecutar y marcar. Objetivo de aceptación: **≥ 95%** casos OK. Git community excluido.

## 0) Pre‑flight

-

```
---
id: ai_sess_20250902_0000
objective: "prueba stack"
horizon: MVP
status: draft
due: 2025-09-03
coverage_pct: 10
latency_budget: 0
stakeholders: [GZ]
tags: [stack/test]
---
- [ ] Tarea demo 📅 2025-09-03
```

-

### 0.1) Diagnóstico rápido

- **"Invalid properties" en esta nota** → el front‑matter estaba roto. Ya corregido a YAML. Si persiste, elimina cualquier línea que empiece con `## id:` arriba y deja solo el bloque entre `---`.
- **Dataview: No results** → confirma que el archivo `_seed.md` está dentro de `/sessions` y que los nombres de carpeta coinciden. Ejecuta `Dataview: Force refresh` si es necesario.
- **Tasks muestra 0** → asegúrate de que la tarea de ejemplo esté en `sessions/_seed.md` y tenga fecha `📅 YYYY-MM-DD`.

---

## id: ai\_sess\_20250902\_0000 objective: "prueba stack" horizon: MVP status: draft due: 2025-09-03 coverage\_pct: 10 latency\_budget: 0 stakeholders: [GZ] tags: [stack/test]

-

````

-

---

## 1) CORE — pruebas funcionales

### 1.1 Audio recorder

- Acción: Ribbon → micrófono → grabar 5s → stop.
- Esperado: archivo `.m4a` incrustado en la nota.

### 1.2 Backlinks / Outgoing links

- Acción: crear nota `A`, enlazar a `B`; abrir `B`.
- Esperado: `Backlinks` muestra `A`; `Outgoing links` de `A` lista `B`.

### 1.3 Bases (core DB)

- Acción: crear Base `AI_HUM_SESIONES` apuntando a `/sessions`. Columnas: `file,objective,horizon,status,due,coverage_pct,latency_budget,stakeholders,tags`. Vista `open` filtro `status != locked`.
- Esperado: edición inline de `objective/status`; orden por `due`.

### 1.4 Bookmarks

- Acción: marcar esta nota y la base `AI_HUM_SESIONES`.
- Esperado: acceso rápido en la pestaña Bookmarks.

### 1.5 Canvas

- Acción: `boards/stack_overview.canvas` con 2 tarjetas (esta nota y la Base) unidas por una flecha.
- Esperado: guardado `.canvas` y navegación correcta.

### 1.6 Command palette / Quick switcher / Search / Slash commands

- Acción: `Ctrl/Cmd+P`, `Ctrl/Cmd+O`, `Ctrl/Cmd+Shift+F`, escribir `/` y ejecutar un comando.
- Esperado: comandos abren vistas; búsqueda devuelve resultados.

### 1.7 Daily notes / Calendar (core)

- Acción: abrir nota diaria; si usas Calendar community, también desde el widget.
- Esperado: crea/abre `YYYY‑MM‑DD.md` en carpeta de diarios.

### 1.8 Files / File recovery

- Acción: crear `sessions/test_core.md`; editar; restaurar una versión desde **File recovery**.
- Esperado: snapshot visible y restaurable.

### 1.9 Footnotes view

- Acción: añadir `Texto con referencia[^1]` y `[^1]: nota al pie`.
- Esperado: panel Footnotes lista y navega a la nota al pie.

### 1.10 Format converter

- Acción: ejecutar conversión sobre una nota de prueba con propiedades antiguas.
- Esperado: propiedades migradas al formato actual.

### 1.11 Graph view

- Acción: abrir grafo global; filtrar por tag `#stack/test`.
- Esperado: nodos filtrados y clic navegable.

### 1.12 Note composer

- Acción: seleccionar un párrafo y extraer a nueva nota.
- Esperado: se crea nota y se reemplaza por link.

### 1.13 Outline / Page preview

- Acción: navegar por encabezados y previsualizar links con hover.
- Esperado: scroll correcto; preview visible.

### 1.14 Properties view

- Acción: cambiar `status` a `review` desde *File properties*.
- Esperado: tipo select respetado; aparece en *All properties*.

### 1.15 Slides

- Acción: crear nota con separadores `---` y ejecutar **Start presentation**.
- Esperado: presentación en pantalla.

### 1.16 Sync (opcional)

- Acción: si tienes Sync, comprobar subida/captura en segundo dispositivo.
- Esperado: archivos sincronizados.

### 1.17 Tags view / Templates / Unique note creator / Web viewer / Word count / Workspaces

- Acción:
  - Tags: abrir vista y filtrar `#stack/test`.
  - Templates: insertar una plantilla de `/templates`.
  - Unique note: crear nueva nota única.
  - Web viewer: abrir `https://obsidian.md`.
  - Word count: observar barra de estado.
  - Workspaces: guardar layout `TEST_STACK` y cargarlo.
- Esperado: todas las operaciones completan.

---

## 2) COMMUNITY — pruebas funcionales

### 2.1 Buttons

- Snippet:

```button
name Nueva sesión IA
type command
action Templater: Create new note from template
````

- Esperado: crea nota desde plantilla.

### 2.2 Calendar

- Acción: abrir vista y navegar a la nota diaria.
- Esperado: coherente con Daily notes.

### 2.3 Commander

- Acción: agregar comando “Abrir Base AI\_HUM\_SESIONES” al ribbon.
- Esperado: botón visible y funcional.

### 2.4 Dataview

- Snippet:

```dataview
TABLE file.link AS Nota, objective, horizon, status, due
FROM "sessions"
WHERE status != "locked"
SORT due ASC
```

- Esperado: tabla renderizada con filas.

### 2.5 Excalidraw

- Acción: `diagrams/00_INDEX.excalidraw` con 3 nodos enlazados a secciones de esta nota.
- Esperado: embed `![[diagrams/00_INDEX.excalidraw|900]]` visible; auto‑export SVG activo.

### 2.6 Linter

- Acción: ejecutar al guardar y manual. Reglas: YAML y headings.
- Esperado: front‑matter ordenado; espacios normalizados.

### 2.7 Meta Bind

- Snippet:

```meta-bind-input
frontmatterKey: status
type: select
options: [draft, active, review, locked]
```

- Esperado: cambio refleja en propiedades.

### 2.8 Modal Forms

- Snippet (Templater):

```tpl
<%*
const mf = app.plugins.plugins.modalforms?.api;
if (mf) {
  const data = await mf.openForm('alta_sesion');
  if (data) await app.fileManager.processFrontMatter(tp.config.target_file, fm => Object.assign(fm, data.getData()));
}
-%>
```

- Esperado: escribe `objective,horizon,status,due` en front‑matter.

### 2.9 QuickAdd

- Acción: crear Choice `Alta sesión IA` (Template/Macro) y ejecutarla.
- Esperado: nota creada en `/sessions`.

### 2.10 Tasks

- Snippet:

```tasks
not done
path includes sessions
sort by due
```

- Esperado: lista de tareas con `due`; marcar done actualiza.

### 2.11 Templater

- Acción: insertar plantilla con variables `tp.date.now()` y `tp.file.title`.
- Esperado: valores renderizados; JS ejecutado.

### 2.12 Tracker

- Snippet:

````markdown
```tracker
searchType: frontmatter
searchTarget: coverage_pct
folder: sessions
output: line
```
````

- Esperado: gráfico visible.

### 2.13 Git (excluido)

- Acción: n/a. Usar versionado externo o Sync.

---

## 3) Cross‑checks y criterios de aceptación

-

**Criterio de aceptación global**: **Pass rate ≥ 95%** sin errores críticos.

## 4) Registro de resultados

Registro de resultados

- Casos totales:
- Casos OK:
- **Pass rate**:
- Bloqueos:

## 5) Cierre

-


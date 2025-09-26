---
asset_id: "<% tp.date.now('YYYYMMDDHHmm') %>_SPECTRUM_<% tp.file.title.replace(/\s+/g, '_').toUpperCase() %>"
asset_name: "<% tp.file.title %>"
asset_type: "master_template_proposal"
asset_version: "0.9.0"
asset_owner: "AingZ_Platform"
asset_status: "in_review"
asset_tags:
  - spectrum
  - knowledge
  - evidence
asset_created: "<% tp.date.now('YYYY-MM-DD') %>"
asset_updated: "<% tp.date.now('YYYY-MM-DD') %>"
context_domain: "Gestión de conocimiento"
context_objectives:
  - "Curar conocimiento vivo con trazabilidad total."
  - "Maximizar visualización Obsidian (Tabs, Canvas, Excalidraw)."
ai_handshake_codex_mode: "structured_markdown"
ai_handshake_codex_contract: "Mantener consultas Dataview/Tasks consistentes y registrar fuentes."
ai_handshake_gpt5_mode: "reasoning_markdown"
ai_handshake_gpt5_contract: "Analizar brechas de conocimiento y proponer acciones."
compat_platforms:
  - Obsidian
  - VSCode
  - GitHub
  - Codex
  - GPT5
compat_plugins_required:
  - Dataview
  - Buttons
  - QuickAdd
  - Tasks
  - Tracker
  - Excalidraw
compat_plugins_optional:
  - Canvas
  - Charts
  - BRAT
  - Citation
---

# [[Spectrum Knowledge Template · Matriz Viva]]

> [!summary] Navegación principal
> [[#00 · Setup]] · [[#05 · Handshake AI↔Humano]] · [[#10 · Contexto & Alcances]] · [[#20 · Fuentes & Evidencias]] · [[#30 · Canvas/Excalidraw]] · [[#40 · Insights & Acciones]] · [[#50 · KPIs & Coverage]] · [[#60 · Feedback & WK.log]]

---

## 00 · Setup

```button
name 📚 Indexar fuente
type command
action QuickAdd:Spectrum · Nueva Fuente
color blue
```

```button
name ♻️ Refrescar consultas
type command
action Dataview:Refresh current view
color purple
```

- [ ] Definir taxonomía principal (`tags`).
- [ ] Registrar reglas aplicables (`ruleset`).
- [ ] Sincronizar assets gráficos con [[#30 · Canvas/Excalidraw]].

---

## 05 · Handshake AI↔Humano

| Actor | Responsabilidad | Formato de entrega |
| --- | --- | --- |
| Codex | Normalizar fuentes y properties | Markdown estructurado + Dataview |
| GPT5 | Analizar brechas y síntesis | Insight reasoning + KPIs |
| Humano | Curador/a | Validar veracidad y actualizar Legacy |

> [!tip] Ajusta la tabla según requerimientos específicos de tu equipo.

---

## 10 · Contexto & Alcances

| Dominio | Límites | Stakeholders | Estado |
| --- | --- | --- | --- |
|  |  |  | - [ ] |
|  |  |  | - [ ] |

> [!question]- Guía
> - ¿Qué knowledge packs se incluyen/excluyen?
> - ¿Qué compromisos de actualización existen?

---

## 20 · Fuentes & Evidencias

```dataview
TABLE file.link AS "Fuente", file.folder AS "Ubicación", file.mtime AS "Actualizado"
FROM ""
WHERE contains(file.tags, "knowledge") or contains(file.tags, "evidence")
SORT file.mtime desc
LIMIT 12
```

```tasks
not done
description includes "evidencia"
```

> [!note] Anexa capturas, PDFs o datasets en `attachments/` y enlaza mediante `![[path/to/file]]`.

---

## 30 · Canvas/Excalidraw

> [!info] Visualiza relaciones complejas mediante Canvas y Excalidraw.

![[<% tp.file.title %>.canvas]]

![[<% tp.file.title %>.excalidraw]]

- [ ] Documentar cambios visuales con timestamp.
- [ ] Coordinar con Codex para actualizar automatizaciones vinculadas.

---

## 40 · Insights & Acciones

```tabs
tab: Insights
- Insight crítico · Impacto:
- Insight emergente · Impacto:
tab: Acciones
- [ ] Acción 1 · Owner:  · Fecha objetivo:
- [ ] Acción 2 · Owner:  · Fecha objetivo:
```

> [!tip] Utiliza etiquetas `#spectrum-insight` y `#spectrum-action` para rastrear desde Dataview.

---

## 50 · KPIs & Coverage

| KPI | Fórmula | Meta | Valor |
| --- | --- | --- | --- |
| Coverage | (# fuentes catalogadas / total esperado) | 95% |  |
| RefreshRate | (promedio días entre actualizaciones) | <= 10 |  |
| EvidenceTrace | (# evidencias con fuente verificada / total) | 100% |  |

```tracker
searchType: task
searchTarget: "#spectrum-action"
startDate: 2024-01-01
endDate: 2024-12-31
summary:
  template: "Acciones Spectrum completadas: {{count}}"
```

---

## 60 · Feedback & WK.log

- 📅 <% tp.date.now("YYYY-MM-DD HH:mm") %> · Evento:  · Resultado:
- 📅  · Evento:  · Resultado:

```tasks
not done
description includes "spectrum feedback"
```

> [!done] Actualiza `asset_status` y sincroniza con el Legacy tras cada ciclo de actualización.

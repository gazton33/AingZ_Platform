---
asset_id: "<% tp.date.now('YYYYMMDDHHmm') %>_NEXUS_<% tp.file.title.replace(/\s+/g, '_').toUpperCase() %>"
asset_name: "<% tp.file.title %>"
asset_type: "master_template_proposal"
asset_version: "0.9.0"
asset_owner: "AingZ_Platform"
asset_status: "in_review"
asset_tags:
  - nexus
  - strategy
  - execution
asset_created: "<% tp.date.now('YYYY-MM-DD') %>"
asset_updated: "<% tp.date.now('YYYY-MM-DD') %>"
context_domain: "Estrategia ↔ Ejecución"
context_objectives:
  - "Conectar visión estratégica con hojas de ruta operativas."
  - "Mantener trazabilidad de impactos y sostenibilidad."
ai_handshake_codex_mode: "structured_markdown"
ai_handshake_codex_contract: "Respetar Tabs, callouts y tablas dinámicas; actualizar KPIs al cierre."
ai_handshake_gpt5_mode: "reasoning_markdown"
ai_handshake_gpt5_contract: "Evaluar decisiones frente a metas de sostenibilidad y autonomía."
compat_platforms:
  - Obsidian
  - VSCode
  - GitHub
  - Codex
  - GPT5
compat_plugins_required:
  - Templater
  - Buttons
  - Dataview
  - Tabs
  - Tracker
  - Tasks
compat_plugins_optional:
  - Excalidraw
  - Projects
  - Canvas
  - Charts
---

# [[Nexus Master Template · Estrategia Viva]]

> [!summary] Flujo rápido
> [[#00 · Setup]] · [[#01 · Handshake AI↔Humano]] · [[#10 · Contexto Estratégico]] · [[#20 · Roadmap Dinámico]] · [[#30 · Inteligencia & Insights]] · [[#40 · Impacto & Sostenibilidad]] · [[#50 · WK.log & Feedback]] · [[#60 · Checklist Final]]

---

## 00 · Setup

```button
name ➕ Instanciar Nota Hija
type command
action QuickAdd:Nexus · Nueva Nota Hija
color blue
```

```button
name ♻️ Refrescar Paneles
type command
action Dataview:Refresh current view
color purple
```

- [ ] Nombrar archivo siguiendo `YYYYMMDD_tema_nexus`.
- [ ] Confirmar objetivos estratégicos en [[#10 · Contexto Estratégico]].
- [ ] Sincronizar roles con stakeholders humanos y Codex/GPT5.

---

## 01 · Handshake AI↔Humano

| Actor | Rol | Mandato |
| --- | --- | --- |
| Codex | Arquitecto técnico | Mantener consistencia de estructuras y automatizaciones. |
| GPT5 | Analista estratégico | Evaluar impactos de decisiones y registrar supuestos. |
| Humano | Lead | Aprobar cambios críticos y consolidar feedback. |

> [!info] Documenta cualquier ajuste de mandato directamente en la tabla anterior para mantener trazabilidad contractual.

---

## 10 · Contexto Estratégico

```dataviewjs
const perspective = dv.current().file.frontmatter.context_objectives ?? [];
dv.paragraph(`**Objetivos declarados:** ${perspective.join('; ')}`);
```

| Pilar | Meta | Horizonte | Indicador | Estado |
| --- | --- | --- | --- | --- |
| Estrategia |  |  |  | - [ ] |
| Producto |  |  |  | - [ ] |
| Tecnología |  |  |  | - [ ] |
| Personas |  |  |  | - [ ] |

> [!question]- Exploración
> - ¿Qué hipótesis críticas deben validarse?
> - ¿Qué riesgos sistémicos amenazan la sostenibilidad?

---

## 20 · Roadmap Dinámico

```tabs
tab: Q1
- [ ] Hito 1 · Owner:  · Fecha objetivo: 
- [ ] Hito 2 · Owner:  · Fecha objetivo: 
tab: Q2
- [ ] Hito 3 · Owner:  · Fecha objetivo: 
- [ ] Hito 4 · Owner:  · Fecha objetivo: 
tab: Q3
- [ ] Hito 5 · Owner:  · Fecha objetivo: 
tab: Q4
- [ ] Hito 6 · Owner:  · Fecha objetivo: 
```

> [!tip] Etiqueta tareas con `#nexus-roadmap` para análisis automático.

---

## 30 · Inteligencia & Insights

```dataview
TABLE file.link AS "Fuente", file.mtime AS "Última actualización"
FROM ""
WHERE contains(file.tags, "insight")
SORT file.mtime desc
LIMIT 8
```

> [!abstract]+ Insights clave
> - Insight 1 → Implicancias:
> - Insight 2 → Implicancias:
> - Insight 3 → Implicancias:

---

## 40 · Impacto & Sostenibilidad

| KPI | Fórmula | Meta | Valor | Responsable |
| --- | --- | --- | --- | --- |
| TemplateCoverage | (# notas alineadas / # notas totales) | 90% |  |  |
| InteractionDepth | (# bloques interactivos usados / # bloques disponibles) | 80% |  |  |
| SustainabilityTrace | (# decisiones con impacto documentado / total) | 100% |  |  |

```tracker
searchType: task
searchTarget: "#sostenibilidad"
startDate: 2024-01-01
endDate: 2024-12-31
summary:
  template: "Acciones sostenibles completadas: {{count}}"
```

---

## 50 · WK.log & Feedback

- 📅 <% tp.date.now("YYYY-MM-DD HH:mm") %> · Actor:  · Evento:
- 📅  · Actor:  · Evento:
- 📅  · Actor:  · Evento:

```tasks
not done
description includes "feedback"
```

---

## 60 · Checklist Final

- [ ] Roadmap actualizado y compartido.
- [ ] KPIs revisados y registrados.
- [ ] Feedback consolidado y acciones asignadas.
- [ ] `asset_status` ajustado (`in_review`/`approved`).

> [!done] Tras completarlo, sincronizar cambios en repositorios asociados y documentar en el Legacy correspondiente.

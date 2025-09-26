---
asset_id: "<% tp.date.now('YYYYMMDDHHmm') %>_ORBIT_CONT_<% tp.file.title.replace(/\s+/g, '_').toUpperCase() %>"
asset_name: "<% tp.file.title %>"
asset_type: "master_template_proposal"
asset_version: "0.9.0"
asset_owner: "AingZ_Platform"
asset_status: "in_review"
asset_tags:
  - orbit
  - lifecycle
  - sustainability
asset_created: "<% tp.date.now('YYYY-MM-DD') %>"
asset_updated: "<% tp.date.now('YYYY-MM-DD') %>"
context_domain: "Ciclos de proyectos"
context_objectives:
  - "Asegurar stage-gates claros con métricas de sostenibilidad."
  - "Integrar automatizaciones y feedback continuo."
ai_handshake_codex_mode: "structured_markdown"
ai_handshake_codex_contract: "Ejecutar y registrar acciones en Buttons/Tasks; mantener trackers alineados."
ai_handshake_gpt5_mode: "reasoning_markdown"
ai_handshake_gpt5_contract: "Evaluar decisiones de stage-gate con perspectiva sistémica."
compat_platforms:
  - Obsidian
  - VSCode
  - GitHub
  - Codex
  - GPT5
compat_plugins_required:
  - Buttons
  - Dataview
  - Tasks
  - Tracker
  - Excalidraw
  - QuickAdd
compat_plugins_optional:
  - Tabs
  - Projects
  - Calendar
  - Kanban
---

# [[Orbit Continuum Template · Ciclo Vivo]]

> [!summary] Flujo de navegación
> [[#00 · Setup]] · [[#05 · Orbit Stage Map]] · [[#10 · Discover]] · [[#20 · Design]] · [[#30 · Deploy]] · [[#40 · Sustain]] · [[#50 · KPI Orbit]] · [[#60 · Feedback Loop]]

---

## 00 · Setup

```button
name ⚙️ Crear Stage Note
type command
action QuickAdd:Orbit · Nueva Stage Note
color teal
```

```button
name 🧭 Abrir Canvas Orbit
type command
action Canvas:Open
color orange
```

- [ ] Definir scope del ciclo actual.
- [ ] Confirmar stakeholders y responsables.
- [ ] Revisar reglas aplicables en [[ruleset/ruleset_master_v_1]].

---

## 05 · Orbit Stage Map

```mermaid
gantt
    title Orbit Continuum
    section Discover
    Research :done, d1, 2024-09-01, 7d
    section Design
    Prototype :active, d2, 2024-09-08, 10d
    section Deploy
    Rollout :d3, after d2, 14d
    section Sustain
    Monitoring :d4, after d3, 14d
```

- [ ] Actualizar fechas según planificación real.
- [ ] Documentar dependencias críticas en comentarios.

---

## 10 · Discover

| Actividad | Responsable | Evidencia | Estado |
| --- | --- | --- | --- |
|  |  |  | - [ ] |
|  |  |  | - [ ] |

```tasks
not done
path includes "discover"
```

> [!note] Adjunta descubrimientos clave en `legacy_reference_pool/` o en evidencias locales.

---

## 20 · Design

> [!todo]+ Artefactos esenciales
> - [ ] Wireframes actualizados en Excalidraw: `![[<% tp.file.title %>_design.excalidraw]]`
> - [ ] Documentación técnica en `/design/`
> - [ ] Revisión de accesibilidad completada

```dataview
TABLE file.link AS "Asset", file.mtime AS "Actualizado"
FROM ""
WHERE contains(file.name, "design")
SORT file.mtime desc
LIMIT 6
```

---

## 30 · Deploy

| Item | Owner | Script/Automation | Estado |
| --- | --- | --- | --- |
|  |  |  | - [ ] |
|  |  |  | - [ ] |

```tasks
not done
path includes "deploy"
```

> [!warning] Verifica pipelines CI/CD antes de marcar como completado.

---

## 40 · Sustain

- [ ] Implementar monitoreo (Grafana/Prometheus).
- [ ] Ejecutar evaluación de emisiones/energía.
- [ ] Planificar retroalimentación de usuarios.

```tracker
searchType: task
searchTarget: "#orbit-sustain"
startDate: 2024-01-01
endDate: 2024-12-31
summary:
  template: "Acciones Sustain completadas: {{count}}"
```

---

## 50 · KPI Orbit

| KPI | Fórmula | Meta | Valor | Observaciones |
| --- | --- | --- | --- | --- |
| StageOnTime | (# stages on-time / total stages) | 95% |  |  |
| FeedbackLoopTime | (fecha feedback - fecha deploy) | <= 7 días |  |  |
| SustainabilityScore | (puntuación agregada auditoría) | >= 85 |  |  |

```dataview
TABLE file.link AS "Stage", asset_status
FROM "templates/master_template_proposals/next_gen_master_templates"
WHERE asset_type = "master_template_proposal" and contains(asset_tags, "orbit")
LIMIT 5
```

---

## 60 · Feedback Loop

- 📅 <% tp.date.now("YYYY-MM-DD HH:mm") %> · Stage:  · Lección:
- 📅  · Stage:  · Lección:

```tasks
not done
description includes "retro"
```

> [!done] Al cierre del ciclo, actualizar `asset_status` y enviar resumen al Legacy correspondiente.

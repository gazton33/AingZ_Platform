asset_id: "<% tp.date.now('YYYYMMDDHHmm') %>_ARCH_FORM_<% tp.file.title.replace(/\s+/g, '_').toUpperCase() %>"
asset_name: "<% tp.file.title %>"
asset_type: "architecture_form"
asset_version: "1.0.0"
asset_owner: "AingZ_Platform"
asset_status: "draft"
asset_tags:
  - architecture
  - obsidian/form
  - ai-collab
asset_created: "<% tp.date.now('YYYY-MM-DD') %>"
asset_updated: "<% tp.date.now('YYYY-MM-DD') %>"
context_scope: "platform"
context_repo_primary: "AingZ_Platform · https://github.com/AingZ/AingZ_Platform"
context_mission: "Orquestar la arquitectura de la plataforma, directorios y assets críticos."
context_kpis:
  - ArchitectureCoverage
  - FeedbackLoopTime
  - AssetTraceability
compat_platforms:
  - Obsidian
  - VSCode
  - GitHub
  - Codex
  - GPT5
compat_plugins_required:
  - Templater
  - Buttons
  - Excalidraw
  - Dataview
  - Tasks
  - Tracker
compat_plugins_optional:
  - Canvas
  - Projects
  - Periodic Notes
ai_handshake_codex_mode: "structured_markdown"
ai_handshake_codex_mandate: "Mantener bloques interactivos y wikilinks intactos; documentar comandos ejecutados."
ai_handshake_gpt5_mode: "reasoning_markdown"
ai_handshake_gpt5_mandate: "Explicar decisiones arquitectónicas y sus impactos en sostenibilidad y eficiencia."
governance_ruleset: "[[ruleset/ruleset_master_v_1]]"
governance_legacy_reference: "[[templates/architecture_interactive_forms/architecture_assets_inventory|Inventario Arquitectura]]"
governance_change_log: "Registrar eventos clave en [[#80 · WK.log & Feedback]]."
---

# [[Formulario Maestro · Arquitectura Dinámica]]

> [!summary] Navegación inmediata
> [[#00 · Setup]] · [[#10 · Brief Arquitectónico]] · [[#20 · Directorios & Jerarquías]] · [[#30 · Assets & Contratos]] · [[#40 · Diagramación Excalidraw]] · [[#50 · Flujos & Automatización]] · [[#60 · Evaluación & KPIs]] · [[#80 · WK.log & Feedback]] · [[#99 · Checklist Final]]

---

## 00 · Setup

```button
name 🧭 Abrir diagrama Excalidraw existente
type command
action Excalidraw:Open drawing
color orange
```

```button
name ✳️ Crear copia de diagrama base
type command
action QuickAdd:Excalidraw · Nueva Arquitectura
color teal
```

```button
name ♻️ Refrescar paneles Dataview
type command
action Dataview:Refresh current view
color purple
```

- [ ] Confirmar que el archivo Excalidraw activo está referenciado en [[#40 · Diagramación Excalidraw]].
- [ ] Sincronizar los campos de `context.mission` y `context.kpis`.
- [ ] Notificar al equipo AI (Codex/GPT5) sobre cambios estructurales en [[#80 · WK.log & Feedback]].

> [!hint] Ajusta los nombres de comandos `QuickAdd`/`Excalidraw` según la configuración de tu vault.

---

## 10 · Brief Arquitectónico

> [!quote] Contexto general
> Describe la situación actual, restricciones técnicas y oportunidades clave.

| Elemento | Detalle | Estado |
| -------- | ------- | ------ |
| Propósito principal |  | - [ ] |
| Horizonte temporal |  | - [ ] |
| Dependencias críticas |  | - [ ] |
| Sostenibilidad (energía, cómputo, emisiones) |  | - [ ] |

> [!faq]- Preguntas guía
> - ¿Qué áreas de negocio cubre esta arquitectura?
> - ¿Cuáles son los riesgos prioritarios a mitigar?
> - ¿Cómo se integran los modelos Codex/GPT5 en el flujo?

---

## 20 · Directorios & Jerarquías

> [!todo]+ Mapa del árbol de directorios
> 1. Documenta el estado actual del árbol (`dir tree`).
> 2. Marca cambios planificados versus ejecutados.
> 3. Identifica propietarios para cada nodo crítico.

### 20.1 · Snapshot actual

```dataview
TABLE file.folder AS "Ubicación", file.name AS "Recurso"
FROM ""
WHERE contains(file.folder, "<ruta/repositorio>")
SORT file.folder ASC
LIMIT 40
```

> [!warning] Personaliza la consulta anterior para apuntar al repositorio o carpeta objetivo antes de usarla.

### 20.2 · Plan de evolución

- [ ] Nodo principal:  → Responsable: 
- [ ] Subsistema:  → Responsable: 
- [ ] Carpeta crítica:  → Responsable: 
- [ ] Scripts/Automation:  → Responsable: 

> [!tip] Usa `tasks` con etiquetas (`#dir-update`) para que Dataview consolide acciones pendientes.

---

## 30 · Assets & Contratos

| Asset | Ubicación | Responsable | Estado |
| ----- | --------- | ----------- | ------ |
|  |  |  | - [ ] |
|  |  |  | - [ ] |
|  |  |  | - [ ] |

> [!example]- Referencias directas
> - `[[templates/master_template_proposals/obsidian_master_template_aingz_master|Orbit·Spectrum V1]]`
> - `[[templates/architecture_interactive_forms/architecture_assets_inventory|Inventario Arquitectura]]`
> - `[[platform_arch_v5.excalidraw]]`

```tasks
not done
path includes templates
description includes "asset"
```

---

## 40 · Diagramación Excalidraw

> [!info] Conexión visual
> Inserta el diagrama activo mediante wikilink para edición directa en Obsidian.

![[platform_arch_v5.excalidraw]]

- [ ] Actualizar diagrama con la fecha y versión del presente formulario.
- [ ] Alinear capas/elementos con los nodos descritos en [[#20 · Directorios & Jerarquías]].
- [ ] Adjuntar notas de decisiones relevantes usando sticky notes dentro de Excalidraw.

> [!tip] Si generas un nuevo diagrama, reemplaza la referencia anterior por `![[<% tp.file.title %>.excalidraw]]`.

---

## 50 · Flujos & Automatización

> [!todo]+ Modelado operativo
> Lista los flujos de trabajo, automatizaciones y pipelines que impactan la arquitectura.

| Flujo | Herramientas | Trigger | Estado |
| ----- | ------------ | ------- | ------ |
|  |  |  | - [ ] |
|  |  |  | - [ ] |
|  |  |  | - [ ] |

```tracker
searchType: task
searchTarget: "#automation"
startDate: 2024-01-01
endDate: 2024-12-31
summary:
  template: "Automatizaciones completadas: {{count}}"
```

---

## 60 · Evaluación & KPIs

> [!hint] Calcula métricas clave para evaluar la arquitectura.

| KPI | Fórmula | Valor actual | Responsable |
| --- | ------- | ------------ | ----------- |
| ArchitectureCoverage | (# nodos documentados / # nodos totales) |  |  |
| FeedbackLoopTime | (fecha cierre - fecha apertura) |  |  |
| AssetTraceability | (% assets con responsable asignado) |  |  |

```dataview
TABLE WITHOUT ID file.link AS "Formulario", asset_status AS "Estado"
FROM "templates/architecture_interactive_forms"
WHERE asset_type = "architecture_form" and file.name != this.file.name
SORT file.ctime desc
LIMIT 10
```

> [!warning] Requiere que las copias del formulario mantengan el frontmatter `asset_status` actualizado.

---

## 80 · WK.log & Feedback

> [!abstract]+ Registro iterativo
> Mantén trazabilidad de decisiones, acciones ejecutadas y feedback recibido.

- 📅 <% tp.date.now("YYYY-MM-DD HH:mm") %> · Responsable:  · Resumen: 
- 📅  · Responsable:  · Resumen: 
- 📅  · Responsable:  · Resumen: 

> [!tip] Etiqueta entradas relevantes con `#architecture-log` para consultas futuras.

---

## 99 · Checklist Final

- [ ] Validar que todos los campos obligatorios estén completos.
- [ ] Sincronizar decisiones en la base de conocimiento (`legacy_reference` o dashboards externos).
- [ ] Compartir enlace y resumen con stakeholders clave.
- [ ] Registrar lecciones aprendidas en [[templates/master_template_proposals/legacy_reference_pool/README|Legacy Reference Pool]].

> [!done] Cuando todas las casillas estén marcadas, actualiza `asset_status` a `completed` y archiva una copia inmutable.


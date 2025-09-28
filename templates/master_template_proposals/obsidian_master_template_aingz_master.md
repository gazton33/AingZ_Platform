asset_id: "<% tp.date.now('YYYYMMDDHHmm') %>_<% tp.file.title.replace(/\s+/g, '_').toUpperCase() %>"
asset_name: "<% tp.file.title %>"
asset_type: "master_template"
asset_version: "1.0.0"
asset_owner: "AingZ_Platform"
asset_status: "validated"
asset_tags:
  - obsidian/master
  - ai-collab
  - sustainability
asset_created: "<% tp.date.now('YYYY-MM-DD') %>"
asset_updated: "<% tp.date.now('YYYY-MM-DD') %>"
context_domain: ""
context_mission: ""
context_goals:
  - ""
context_stakeholders:
  - "role: ; contact: "
context_risks:
  - ""
compat_platforms:
  - Obsidian
  - VSCode
  - GitHub
  - Codex
  - GPT5
compat_plugins_required:
  - Dataview
  - Templater
  - Buttons
  - QuickAdd
  - Tracker
  - Tasks
  - Calendar
compat_plugins_optional:
  - Canvas
  - Excalidraw
  - Projects
  - BRAT
  - Periodic Notes
compat_notes: "Duplicar con Templater/QuickAdd antes de editar."
ai_handshake_codex_mode: "structured_markdown"
ai_handshake_codex_contract: "Mantener YAML, callouts y bloques interactivos intactos."
ai_handshake_codex_prompts:
  - "Responder con listas accionables"
  - "Actualizar checklists y WK.log al final de cada intervención"
ai_handshake_gpt5_mode: "reasoning_markdown"
ai_handshake_gpt5_contract: "Explicar decisiones en [[#50 · Feedback y WK.log]] con timestamp."
ai_handshake_gpt5_prompts:
  - "Aplicar análisis sistémico con perspectiva de sostenibilidad"
  - "Proponer optimizaciones cuantificables (KPIs)"
governance_ruleset: "[[ruleset/ruleset_master_v_1]]"
governance_reference_legacy: "[[templates/master_template_proposals/legacy_reference_pool/README|Legacy Reference Pool]]"
governance_change_control: "Registrar decisiones estratégicas en [[#50 · Feedback y WK.log]]."
---

%% -------------------------------------------------------------
%% Guía rápida: la IA (Codex / GPT5) y los humanos deben seguir
%% estas instrucciones sin eliminar bloques estructurales.
%% -------------------------------------------------------------

# [[A·Master Template · Orbit-Spectrum V1]]

> [!summary] Navegación inmediata
> [[#00 · Setup Rápido]] · [[#01 · AI ↔ Humano Handshake]] · [[#02 · Contratos y Metadata]] · [[#10 · Contexto Estratégico]] · [[#20 · Flujo Operativo]] · [[#30 · Data & Inteligencia]] · [[#40 · Impacto & Sostenibilidad]] · [[#50 · Feedback y WK.log]] · [[#60 · Anexos & Referencias]] · [[#99 · Checklist de Cierre]]

---

## 00 · Setup Rápido

> [!abstract]+ Activación inicial
> 1. Renombrar la nota siguiendo `YYYYMMDD_<TemaClave>`.
> 2. Ejecutar la acción QuickAdd `MT · Nueva Nota` para clonar propiedades comunes.
> 3. Validar que los campos de [[#02 · Contratos y Metadata]] estén completos.

```button
name ➕ Instanciar Plantilla Hija
type command
action QuickAdd:MT · Nueva Nota Hija
color blue
```

```button
name ♻️ Refrescar Dataview
type command
action Dataview:Refresh current view
color purple
```

- [ ] Confirmar que `ai_handshake` contiene las instrucciones vigentes.
- [ ] Registrar responsables en `context.stakeholders`.
- [ ] Sincronizar tags con la taxonomía del [[ruleset/ruleset_master_v_1]].

> [!hint] Ajusta el campo `action` de cada botón según los IDs de comando disponibles en tu vault (`Settings → Buttons`).

---

## 01 · AI ↔ Humano Handshake

> [!info] Codex
> - Interpretar secciones tituladas con `##` como módulos independientes.
> - No modificar frontmatter salvo que se solicite explícitamente.
> - Documentar comandos ejecutados dentro de [[#50 · Feedback y WK.log]].

> [!tip] GPT5
> - Mantener trazabilidad de decisiones en subtareas `- [ ]` y justificar cambios significativos.
> - Antes de cerrar, completar el bloque [[#99 · Checklist de Cierre]] con hallazgos clave.

> [!warning] Bloques protegidos
> - No eliminar los bloques `button`, `dataview`, `tasks`, `tracker` ni las secciones con `%%`.
> - Respetar los wikilinks internos (`[[#Sección]]`) para asegurar navegabilidad en Obsidian.

---

## 02 · Contratos y Metadata

> [!todo]+ Campos obligatorios (RULESET)
> - `asset.domain`, `context.mission`, `compat.platforms`
> - `governance.ruleset`, `governance.change_control`
> - `ai_handshake` actualizado según el modo de colaboración.

| Campo | Descripción | Estado |
| ----- | ----------- | ------ |
| `mission` | Objetivo operativo principal | - [ ] |
| `goals` | Metas cuantificables vinculadas a KPIs | - [ ] |
| `risks` | Riesgos críticos con planes de mitigación | - [ ] |
| `stakeholders` | Roles clave y responsables | - [ ] |

> [!note] Sincronización automática
> Usa el botón `♻️ Refrescar Dataview` tras editar frontmatter para actualizar paneles derivados.

---

## 10 · Contexto Estratégico

> [!quote] Narrativa
> Resume el propósito, alcance y horizonte temporal del asset.

> [!example]- Modo Ejecutivo
> - Hito clave #1: _...
> - Dependencias críticas: _...
> - KPIs vinculados: `TemplateCoverage`, `InteractionDepth`.

> [!faq]- Modo Profundo (plegable)
> - ¿Qué supuestos guían este trabajo?
> - ¿Cómo se relaciona con [[legacy_reference_pool/README|Legacy Reference Pool]]?
> - ¿Qué recursos adicionales se necesitan?

---

## 20 · Flujo Operativo

> [!todo]+ Stage Gates
> 1. **Discovery** → [[#30 · Data & Inteligencia]]
> 2. **Design** → prototipos en Canvas/Excalidraw (`![[canvas/<% tp.file.title %>.canvas]]`)
> 3. **Delivery** → tareas operativas en lista siguiente
> 4. **Sustain** → validación de KPIs y documentación final

### 20.1 · Plan de tareas

- [ ] Discovery · Investigación preliminar (responsable: )
- [ ] Design · Construcción de solución (responsable: )
- [ ] Delivery · Implementación / despliegue (responsable: )
- [ ] Sustain · Seguimiento y ajustes (responsable: )

```tasks
not done
path includes <% tp.file.title %>
short mode
group by filename
sort by priority
```

> [!tip] Usa `QuickAdd` para crear subtareas siguiendo la convención `YYYYMMDD · Acción · Responsable`.

---

## 30 · Data & Inteligencia

> [!info] Tablero Dataview
> Visualiza notas relacionadas que comparten el mismo tag o `asset.id`.

```dataview
TABLE file.mtime as "Última edición", mission, status, impact_carbon
FROM ""
WHERE contains(file.tags, "obsidian/master") AND file.name != this.file.name
SORT file.mtime DESC
```

> [!hint]- Integración externa
> - Embed datasets relevantes: `![[data/<nombre_dataset>.csv]]`
> - Usa `dataviewjs` para cálculos personalizados si se requieren métricas avanzadas.

---

## 40 · Impacto & Sostenibilidad

> [!todo]+ Indicadores principales
> - `impact_carbon` (kg CO2e)
> - `impact_water` (L)
> - `impact_social` (breve descripción)

```tracker
searchType: dvField
searchTarget: impact_carbon
datasetName: "Huella de Carbono"
accumulation: sum
startDate: <% tp.date.now('YYYY-MM-01') %>
endDate: <% tp.date.now('YYYY-MM-DD') %>
lineChart:
    title: "Tendencia mensual"
```

> [!warning] Si algún indicador supera el umbral pactado en [[ruleset/ruleset_master_v_1]], activar plan de mitigación y documentarlo en [[#50 · Feedback y WK.log]].

---

## 50 · Feedback y WK.log

> [!note] Registrar cada intervención de IA/humano con timestamp ISO8601.

| Fecha/Hora | Autor | Rol | Resumen | Próximo paso |
| ---------- | ----- | --- | ------- | ------------- |
| <% tp.date.now('YYYY-MM-DDTHH:mm') %> |  |  |  |  |

> [!todo]- Retroalimentación pendiente
> - [ ] Validar entregables con responsables humanos
> - [ ] Documentar aprendizajes clave en RULESET o Legacy si aplica

---

## 60 · Anexos & Referencias

> [!tip] Recursos vinculados
> - [[ruleset/ruleset_master_v_1]] (contrato vigente)
> - [[aing_z_ruleset_max_universal_v_1_0_template]]
> - [[templates/master_template_proposals/legacy_reference_pool/README|Legacy Reference Pool]]
> - ![[canvas/<% tp.file.title %> · mapa.canvas]] *(crear si se necesita visualización)*

> [!example]- Evidencias multimedia
> - Capturas: `![[evidence/<% tp.date.now('YYYYMMDD') %>_screenshot.png]]`
> - Audio/Video: `![[evidence/<% tp.date.now('YYYYMMDD') %>_brief.mp4]]`

---

## 99 · Checklist de Cierre

- [ ] WK.log actualizado y compartido
- [ ] KPIs revisados y en rango
- [ ] Feedback integrado al [[templates/master_template_proposals/legacy_reference_pool/README|Legacy Reference Pool]] si aplica
- [ ] Estado final comunicado (Codex/GPT5 + humano)
- [ ] Nota archivada o marcada como `status: completed`

> [!success] Cuando todos los checks estén completos, actualizar `asset_status` a `completed` y mover la nota al archivo correspondiente.

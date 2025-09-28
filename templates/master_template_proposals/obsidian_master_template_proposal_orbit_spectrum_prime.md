---
asset:
  id: obsidian_master_template_orbit_spectrum_prime_2025_09
  name: ObsidianMasterTemplateOrbitSpectrumPrime
  version: 0.2.0
  owner: AingZ_Platform
  status: working
context:
  dom: RegenerativeProjects
  goals:
    - orchestrate_end_to_end_cycles_with_active_knowledge_graphs
    - enable_hybrid_ai_human_collaboration
    - guarantee_traceable_impact_metrics
  risks:
    - knowledge_action_drift
    - checklist_fatigue
compat:
  platforms: [Obsidian, VSCode, GitHub, CODEX]
  connectors: [GitHub, Notion, Zotero]
  notes: "Fusión de ORBIT (ciclos) + SPECTRUM (knowledge fabric) con soporte multicanal."
obsidian:
  cssclass: cards tabs layout-widescreen
  required_plugins: [Dataview, DataviewJS, Buttons, Tracker, Calendar, QuickAdd, Tasks, Templater, Excalidraw, Canvas, Admonition, StyleSettings]
  automation:
    quickadd_commands: ["Nueva bitácora", "Registrar hito", "Añadir bibliografía"]
---

# {{VALUE:project_name?Proyecto ORBIT·SPECTRUM}}

> [!success] Panel de misión · **Discover → Design → Deploy → Sustain**
> - Estado actual: `<status>` · Stage activo: `<stage_active>`
> - Due date objetivo: `<due_date>` · Score madurez: `<maturity_score>/100`
> - Impacto esperado (CO₂e / Social): `<impact_carbon_target>` / `<impact_social_target>`

---

## 0. Frontmatter maestro (copiar a properties)

```yaml
project_id: <uid>
owner: <responsable>
co_owner: [<nombre>]
stakeholders: [<stakeholder1>, <stakeholder2>]
review_cadence: P14D
stage: <discover|design|deploy|sustain>
status: <ideation|active|hold|closed>
impact_carbon_target: <kg_co2_eq>
impact_carbon_actual: <kg_co2_eq>
impact_social_target: <indicador>
impact_social_actual: <indicador>
confidence: <0-100>
relevance_score: <0-100>
source_primary: <fuente principal>
related_canvas: {{VALUE:project_name?Proyecto ORBIT·SPECTRUM}}.canvas
related_excalidraw: {{VALUE:project_name?Proyecto ORBIT·SPECTRUM}}.excalidraw
legacy_refs: [[templates/master_template_proposals/legacy_reference_pool/]]
```

> [!info] Sincronización rápida
> - **Obsidian**: ejecutar `Templater: Replace templates in the active file` tras pegar frontmatter.
> - **VSCode / GitHub**: mantener bloques YAML y tableros plegables para compatibilidad markdown.
> - **Codex / ChatGPT**: invocar sección `## 7. Handshake AI↔Human` para orquestar instrucciones dinámicas.

---

## 1. Radar cognitivo & mapa de contexto

> [!map]- Visualizaciones clave (Spectrum core)
> - Canvas :: `![[{{VALUE:project_name?Proyecto ORBIT·SPECTRUM}}.canvas]]`
> - Excalidraw :: `![[{{VALUE:project_name?Proyecto ORBIT·SPECTRUM}}.excalidraw]]`
> - Grafo local :: `[[=this.file.path]]`

```dataviewjs
const neighbors = dv.current().file.outlinks.concat(dv.current().file.inlinks);
const counts = {};
neighbors.forEach(link => {
  const path = link.path;
  counts[path] = (counts[path] ?? 0) + 1;
});
const rows = Object.entries(counts).map(([path, weight]) => ({
  note: dv.fileLink(path),
  weight
})).sort((a, b) => b.weight - a.weight);
dv.table(["Nota relacionada", "Peso"], rows.slice(0, 10));
```

```ad-note
title: Anclas de referencia
collapse: closed
```
> - Glosario: [[ruleset/aing_z_ruleset_max_universal_v_1_0_template]]
> - Legacy Pool: [[templates/master_template_proposals/legacy_reference_pool/]]
> - Reglas adicionales: <enlace>

---

## 2. Discover · Hipótesis & evidencia

> [!question]- Preguntas guía
> - ¿Qué problema resolvemos y para quién?
> - ¿Qué evidencia valida la urgencia?
> - ¿Cómo cuantificamos el impacto socioambiental potencial?

```dataview
TABLE WITHOUT ID evidence_type as "Tipo", source as "Fuente", confidence as "Confianza"
FROM ""
WHERE stage = "discover" and project = this.file.name
SORT confidence desc
```

> [!todo] Checklist Discover (Tasks)
> - [ ] Mapear stakeholders críticos `#task/high`
> - [ ] Completar análisis de ciclo de vida `#task/high`
> - [ ] Documentar riesgos regulatorios `#task/med`

```button
name Pasar a Design
type append
action ## Gate Design\n- {{DATE:YYYY-MM-DD}} — Checklist Discover completada ✅
```

---

## 3. Design · Blueprint sostenible

> [!example]- Blueprint mermaid
> ```mermaid
> flowchart LR
>   A[Need] --> B(Concept)
>   B --> C{Evaluación ambiental}
>   C -->|OK| D[Prototype]
>   C -->|Rework| B
>   D --> E((MVP listo))
> ```

```dataviewjs
const prototypes = dv.pages().where(p => p.stage == "design" && p.type == "prototype" && p.project == dv.current().file.name);
const items = prototypes.array().map(p => ({
  title: p.file.link,
  readiness: p.readiness ?? 0,
  energy: p.energy_intensity ?? "n/d"
}));
dv.list(items.map(it => `${it.title} — readiness: ${it.readiness}% · energía: ${it.energy}`));
```

> [!warning]- Gate de salida
> - [ ] Validación con usuarios clave (≥3 entrevistas)
> - [ ] Cálculo de impacto carbono < límite objetivo
> - [ ] MVP aprobado por comité

```button
name Registrar comité Design
type append
action ### Comité Design\n- {{DATE:YYYY-MM-DD}} — Resultado: <Aprobado/Iterar>\n- Observaciones: <texto>
```

---

## 4. Deploy · Operación regenerativa

> [!tip] Sprint board & entregables
> - Actualizar en [[SprintBoard/{{tp_title}}|SprintBoard]]
> - Documentar entregables en carpeta `/deploy`

```dataview
TABLE milestone as "Entregable", due, owner, status
FROM ""
WHERE stage = "deploy" and project = this.file.name
SORT due asc
```

> [!todo]- Checklist sostenibilidad operativa
> - [ ] Energía 100% renovable en despliegue
> - [ ] Métricas de emisión monitorizadas
> - [ ] Plan de remediación documentado

```button
name Abrir bitácora diaria
type command
action QuickAdd: Nueva bitácora
```

---

## 5. Sustain · Métricas vivas & alertas

```tracker
searchType: frontmatter
searchTarget: impact_carbon_actual
datasetName: Carbono actual
line:
  title: "Kg CO₂ eq"
  color: "#3B8D4E"
```

```tracker
searchType: frontmatter
searchTarget: satisfaction_index
datasetName: Satisfacción
line:
  title: "Índice"
  color: "#1F6FEB"
```

```dataview
LIST from "" WHERE stage = "sustain" and type = "learning" and project = this.file.name
```

```tasks
not done
path includes {{tp_title}}
tag includes #alerta
```

> [!bug] Gestionar alertas críticas en menos de 48h.

---

## 6. Evidencias, bibliografía y DO/DON'T

```ad-example
title: Evidencia clave
collapse: open
```
> - Punto de datos A: <detalle>
> - Punto de datos B: <detalle>
> - Modelos asociados: <modelo>

```ad-info
title: Riesgos y límites
collapse: open
```
> - Riesgo 1: <detalle>
> - Riesgo 2: <detalle>
> - Gap: <detalle>

> [!check]- DO
> - Aplicar en proyectos con <condición>
> - Mantener trazas en `WK.log`
> - Validar métricas de impacto antes de escalar

> [!failure]- DON'T
> - Usar sin validación de contexto
> - Compartir sin limpiar datos sensibles
> - Desalinear nomenclatura del glosario V5

```dataview
TABLE source as "Fuente", type as "Tipo", year, access, reliability
FROM ""
WHERE type = "reference" and project = this.file.name
SORT reliability desc
```

```button
name Importar desde Zotero
type command
action MetaEdit: Zotero Import
```

```dataviewjs
const bib = dv.pages().where(p => p.collection == "bibliography" && p.projects && p.projects.includes(dv.current().file.name));
dv.list(bib.map(b => `${b.file.link} — ${b.authors ?? "s.d."} (${b.year ?? "s.f."})`));
```

---

## 7. Handshake AI ↔ Human (Operación multicanal)

```yaml
ai_interface:
  prompts:
    - name: codex_sync
      goal: "Actualizar propiedades críticas desde VSCode/GitHub"
      instructions: |
        - Leer sección "0. Frontmatter maestro" y sincronizar campos faltantes.
        - Resumir blockers en menos de 80 palabras.
        - Ejecutar action `Registrar comité Design` si stage = design.
    - name: chatgpt_feedback
      goal: "Facilitar retroalimentación rápida"
      instructions: |
        - Revisar `## 5. Sustain` para alertas activas.
        - Proponer 2 acciones mitigadoras y asignar owner.
        - Preguntar confirmación humana antes de cerrar tareas.
  audit_log:
    last_ai_touch: <YYYY-MM-DDThh:mmZ>
    human_ack: <@persona>
```

> [!tip]- VSCode / GitHub quick commands
> - Utilizar Snippets `orbit-spectrum` para insertar secciones.
> - Ejecutar `Markdown: Toggle Fold Level 2` para navegar por etapas.
> - Referenciar issues relacionados: `Closes #<id>`.

---

## 8. WK.log · Aprendizajes y retroalimentación

```yaml
wk_entry:
  when: {{DATE:YYYY-MM-DDTHH:mm}}
  actor: ai|human
  connector: <GitHub/Zotero/Obsidian>
  findings:
    - <aprendizaje>
  next:
    - <acción>
```

```tasks
not done
path includes {{tp_title}}
tag includes #knowledge/todo
```

> [!summary]- Feedback stakeholders
> - `{{DATE:YYYY-MM-DD}}` — `@persona`: <feedback>
> - `{{DATE:YYYY-MM-DD}}` — `@persona`: <feedback>

---

## 9. OutputTemplate y gobernanza

```yaml
OutputTemplate:
  deliverable: ProjectKnowledgeMasterRecord
  exports:
    - format: markdown
    - format: json
    - format: pdf
    - format: opml
  validations:
    - name: Tasks plugin
      command: Tasks: Create or update checklist
    - name: Dataview
      command: Dataview: Force refresh current view
    - name: Linter
      command: Linter: Lint current file
  review:
    owner: {{VALUE:owner?"@pending"}}
    cadence: {{VALUE:review_cadence?P14D}}
```

> [!quote]- Compromiso ORBIT·SPECTRUM
> "Cada decisión se basa en evidencia viva y métricas transparentes."

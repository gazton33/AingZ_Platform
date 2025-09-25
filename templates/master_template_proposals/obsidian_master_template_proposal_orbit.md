---
asset:
  id: obsidian_master_template_orbit_2025_09
  name: ObsidianMasterTemplateOrbit
  version: 0.1.0
  owner: AingZ_Platform
  status: draft
context:
  dom: SustainableProjects
  goals:
    - orchestrate_end_to_end_project_cycles
    - embed_environmental_kpis
  risks:
    - missed_stage_gates
    - insufficient_feedback_logging
compat:
  platforms: [Obsidian, GPT5]
  connectors: [GitHub, Notion]
  notes: "Optimizado para proyectos iterativos con entregas quincenales."
obsidian:
  cssclass: cards tabs
  required_plugins: [Dataview, Buttons, Tracker, Calendar, QuickAdd, Tasks]
  automation:
    quickadd_commands: ["Nueva bitácora", "Registrar hito"]
---

# {{VALUE:project_name?Proyecto sin nombre}}

> [!success] Círculo ORBIT
> **Discover → Design → Deploy → Sustain**
>
> - Hito activo: `<stage_active>`
> - Fecha de cierre prevista: `<due_date>`
> - Scorecard de madurez: `<maturity_score>/100`

---

## 0. Properties obligatorias

```yaml
project_id: <uid>
owner: <responsable>
co_owner: [<nombre>]
stakeholders: [<stakeholder1>, <stakeholder2>]
impact_carbon_target: <kg_co2_eq>
impact_social_target: <indicador>
review_cadence: P14D
```

---

## 1. Discover

> [!question]- Preguntas guía
> - ¿Qué problema resolvemos?
> - ¿Qué evidencia valida el dolor?
> - ¿Cómo medimos el impacto ambiental y social?

```dataview
TABLE WITHOUT ID evidence_type as "Tipo", source as "Fuente", confidence as "Confianza"
FROM ""
WHERE stage = "discover" and project = this.file.name
SORT confidence desc
```

> [!todo] Acciones Discover
> - [ ] Mapear stakeholders críticos `#task/high`
> - [ ] Completar análisis de ciclo de vida `#task/high`
> - [ ] Documentar riesgos regulatorios `#task/med`

```button
name Pasar a Design
type append
action ## Hito Design\n- {{DATE:YYYY-MM-DD}} — Checklist de entrada completada ✅
```

---

## 2. Design

> [!example]- Blueprint sostenible
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

> [!warning]- Gate de salida (Checklist)
> - [ ] Validación con usuarios clave (≥3 entrevistas)
> - [ ] Cálculo de impacto carbono < límite objetivo
> - [ ] MVP aprobado por comité

```button
name Registrar decisión del comité
type append
action ### Comité Design\n- {{DATE:YYYY-MM-DD}} — Resultado: <Aprobado/Iterar>\n- Observaciones: <texto>
```

---

## 3. Deploy

> [!tip] Sprint board
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

## 4. Sustain

> [!note]- Métricas vivas
> ```tracker
> searchType: frontmatter
> searchTarget: impact_carbon_actual
> datasetName: Carbono actual
> line:
>   title: "Kg CO₂ eq"
>   color: "#3B8D4E"
> ```
>
> ```tracker
> searchType: frontmatter
> searchTarget: satisfaction_index
> datasetName: Satisfacción
> line:
>   title: "Índice"
>   color: "#1F6FEB"
> ```

```dataview
LIST from "" WHERE stage = "sustain" and type = "learning" and project = this.file.name
```

> [!bug]- Alertas activas (Tasks)
> ```tasks
> not done
> path includes {{tp_title}}
> tag includes #alerta
> ```

---

## 5. Feedback & aprendizajes

> [!summary]- Retroalimentación de stakeholders
> - `{{DATE:YYYY-MM-DD}}` — `@persona`: <feedback>
> - `{{DATE:YYYY-MM-DD}}` — `@persona`: <feedback>

```dataview
TABLE reviewer as "Revisor", decision as "Decisión", notes as "Notas"
FROM ""
WHERE type = "review" and project = this.file.name
SORT date desc
```

> [!quote]- Compromiso ORBIT
> "No hay despliegue sin evidencia de impacto positivo neto."

---

## 6. OutputTemplate y próximos pasos

```yaml
OutputTemplate:
  deliverable: ProjectMasterRecord
  exports:
    - format: markdown
    - format: json
    - format: pdf
  validations:
    - name: Tasks plugin
      command: Tasks: Create or update checklist
    - name: Linter
      command: Linter: Lint current file
  follow_up:
    cadence: {{VALUE:review_cadence?P14D}}
    owner: {{VALUE:owner?"@pending"}}
```

---
asset:
  id: "<% tp.date.now('YYYYMMDDHHmm') %>_ORBIT_MODULE_<% tp.file.title.replace(/\\s+/g, '_').toUpperCase() %>"
  name: "<% tp.file.title %>"
  type: module_template
  parent: obsidian_master_template_aingz_master
  version: "0.1.0"
  owner: "AingZ_Platform"
  status: "draft"
  tags:
    - obsidian/module
    - orbit/project
  created: "<% tp.date.now('YYYY-MM-DD') %>"
  updated: "<% tp.date.now('YYYY-MM-DD') %>"
context:
  project_stage: "discover"
  sustainability_focus: "carbon"
  delivery_mode: "hybrid"
compat:
  platforms: ["Obsidian", "GitHub"]
  plugins:
    required: ["Templater", "Dataview", "Buttons", "QuickAdd", "Tasks"]
    optional: ["Tracker", "Calendar"]
ai_handshake:
  codex:
    mode: "structured_markdown"
    output_contract: "Mantener frontmatter y secciones 10-40 consistentes; actualizar checklists según project_stage."
    prompts:
      - "Priorizar hitos del ciclo Discover→Deploy"
      - "Registrar variaciones en tareas como checklist"
  gpt5:
    mode: "reasoning_markdown"
    output_contract: "Explicar decisiones estratégicas en bloque 40 con métricas cuantificables."
    prompts:
      - "Evaluar riesgos-operativos por stage"
      - "Sugerir KPIs ambientales y sociales"
---

# {{VALUE:project_name?Proyecto orbit}}

> [!info] Módulo Orbit · Proyecto
> Aplica cuando `context.project_stage` = `<discover/design/deploy/sustain>`.
> 
> - Stage activo: `<% tp.frontmatter()["context"].project_stage %>`
> - Foco de sostenibilidad: `<% tp.frontmatter()["context"].sustainability_focus %>`
> - Modo de entrega: `<% tp.frontmatter()["context"].delivery_mode %>`

---

## 10 · Contexto Estratégico

> [!quote] Narrativa por stage
> Describe el propósito del proyecto según la etapa `context.project_stage`.

> [!example]- Alineación rápida
> - Objetivo inmediato: _...
> - Dependencias críticas: _...
> - KPI clave (ambiental/social): _...

> [!faq]- Profundizar
> - ¿Qué aprendizajes previos informan esta etapa?
> - ¿Qué stakeholders lideran las decisiones actuales?
> - ¿Cómo contribuye al roadmap Orbit global?

---

## 20 · Flujo Operativo

> [!todo]+ Stage Gates adaptativos
> 1. **Discover** → validar problema y baseline de impacto.
> 2. **Design** → prototipo listo con métricas sostenibles.
> 3. **Deploy** → despliegue documentado y checklist ambiental completado.
> 4. **Sustain** → seguimiento de KPIs y planes de mejora.

### 20.1 · Plan táctico

- [ ] `<% tp.frontmatter()["context"].project_stage %>` · Acción prioritaria (owner: )
- [ ] Próximo stage · Preparación clave (owner: )
- [ ] Riesgo ambiental mitigado (owner: )
- [ ] Coordinación con stakeholders (owner: )

```tasks
not done
path includes <% tp.file.title %>
short mode
group by status
```

> [!tip] Usa QuickAdd `Orbit · Nueva Bitácora` para documentar avances diarios por etapa.

---

## 30 · Data & Inteligencia

> [!info] Dataview por stage
> Visualiza evidencias y experimentos relacionados con `context.project_stage`.

```dataview
TABLE file.mtime as "Última edición", stage, owner, readiness
FROM ""
WHERE stage = "<% tp.frontmatter()["context"].project_stage %>" AND project = this.file.name
SORT file.mtime DESC
```

> [!hint]- Integración externa
> - Adjunta datasets con emisiones proyectadas (`data/orbit/<stage>.csv`).
> - Usa `dataviewjs` para simular escenarios de impacto.

---

## 40 · Impacto & Sostenibilidad

> [!todo]+ Indicadores específicos
> - `impact_carbon_target` (kg CO2e)
> - `impact_social_target` (beneficiarios)
> - `impact_circularity` (% materiales reutilizados)

```tracker
searchType: frontmatter
searchTarget: impact_carbon_actual
datasetName: "Carbono real"
line:
  title: "Kg CO₂"
  color: "#3B8D4E"
```

> [!warning] Si el impacto real supera el target, documentar mitigaciones en bitácoras y actualizar stakeholders.


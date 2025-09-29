---
legacy_ref: true
scope: [template, analytics]
review_cycle: biweekly
source: templates/master_template_proposals/kpi_dashboard
notes: "Documenta decisiones basadas en KPIs para la evolución del master template."
---

# Changelog quincenal orientado a KPIs

> [!summary] Objetivo
> Registrar ajustes aplicados o planificados según los KPIs de adopción del master template, conectando el WK.log operativo con la documentación histórica del Legacy Reference Pool.

---

## Cómo usar este changelog

1. Revisa el panel [[templates/master_template_proposals/kpi_dashboard#^kpi-dashboard-snapshot|KPI Snapshot]] antes de cerrar cada periodo quincenal.
2. Resume aquí las decisiones tomadas, enlaces a commits/notas relacionadas y el impacto esperado.
3. Actualiza la sección `## Próximos focos` con los siguientes experimentos o ajustes a validar.

---

## Periodos recientes

> [!example]- Plantilla de registro quincenal
> ### <% tp.date.now('YYYY-MM-DD') %> · Periodo <% tp.date.now('GGGG-[W]WW') %>
> - **TemplateCoverage:** _<anotar valor del dashboard>_
> - **InteractionDepth:** _<anotar valor del dashboard>_
> - **SustainabilityTrace:** _<anotar valor del dashboard>_
> - **FeedbackLoopTime:** _<anotar valor del dashboard>_
> - **Ajustes aplicados:**
>   - _Ej.: Actualización de botones en sección 20 para aumentar interacción._
> - **Evidencias / referencias:**
>   - _Ej.: Commit `abc123`, nota `[[20240915_proyecto_x]]`._
> - **Resultados esperados:** _<impacto medible>_

```dataview
TABLE without id file.link AS "Nota", file.mtime AS "Última actualización"
FROM "templates/master_template_proposals"
WHERE file.mtime >= date(today) - dur(14 days)
  AND (contains(file.path, "obsidian_master_template_aingz_master") OR contains(file.path, "modules"))
SORT file.mtime DESC
```

---

## Próximos focos

- [ ] _Ej.: Diseñar snippet Templater para precargar `impact_carbon` en notas hijas._
- [ ] _Ej.: Validar tareas con tag `#feedback/loop` y cerrar ciclos atrasados._
- [ ] _Ej.: Evaluar impacto de nuevas métricas propuestas por el equipo._

---

> [!tip] Mantén un enlace directo desde el índice principal de master templates para garantizar que cada iteración documentada sea revisada durante las rondas de validación.

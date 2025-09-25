---
asset:
  id: obsidian_master_template_catalog_2025_09
  name: ObsidianMasterTemplateCatalog
  version: 1.0.0
  owner: AingZ_Platform
  status: validated
context:
  domain: KnowledgeArchitecture
  goals:
    - centralize_validated_master_template
    - document_usage_contracts
  risks:
    - drift_against_ruleset
    - loss_of_interactive_blocks
compat:
  platforms: [Obsidian, VSCode, GitHub]
  connectors: [Codex, GPT5]
  notes: "Este índice refleja únicamente la versión validada del master template."
---

# Master Template Orbit·Spectrum V1 (Validado)

- **Plantilla activa:** [[obsidian_master_template_aingz_master|A·Master Template · Orbit-Spectrum V1]]
- **Última revisión:** <% tp.date.now('YYYY-MM-DD') %>
- **Responsable de curaduría:** Equipo híbrido (AI Codex/GPT5 + humanos AingZ)

> [!summary] ¿Por qué se consolidó esta versión?
> - Integra el análisis de assets del repositorio y el legado curado en [[legacy_reference_pool/README|Legacy Reference Pool]].
> - Maximiza interactividad Obsidian (Buttons, Dataview, Tasks, Tracker, Canvas, wikilinks).
> - Contiene contratos explícitos para Codex y GPT5, garantizando reproducibilidad en múltiples plataformas (VSCode, GitHub, Obsidian).

---

## Cómo utilizar la plantilla

1. Ejecutar `QuickAdd → MT · Nueva Nota` o `Templater → Insert template → A·Master Template · Orbit-Spectrum V1`.
2. Completar la cabecera YAML antes de editar el cuerpo.
3. Seguir las instrucciones en [[obsidian_master_template_aingz_master#00 · Setup Rápido]].
4. Documentar cualquier personalización en [[obsidian_master_template_aingz_master#50 · Feedback y WK.log]] y, si aplica, anexar evidencia al [[legacy_reference_pool/README|Legacy Reference Pool]].

> [!warning] Bloques protegidos
> No eliminar callouts, botones, queries ni checklists definidos en la plantilla. Son necesarios para la colaboración AI↔humano.

---

## Mantenimiento y evolución

- Cualquier ajuste mayor debe registrarse como propuesta en `legacy_reference_pool` antes de actualizar la versión validada.
- Seguir los KPIs definidos en [[assets_landscape_analysis.md#7-kpi-propuestos-para-evaluar-adopción|KPIs de adopción]] para medir efectividad.
- Cuando se valide una nueva iteración, actualizar este índice y mover la versión previa al repositorio histórico.

---

## Recursos vinculados

| Recurso | Descripción | Uso |
| ------- | ----------- | --- |
| [[assets_landscape_analysis.md]] | Análisis integral de assets Markdown | Identificar requisitos y KPIs.
| [[obsidian_master_template_aingz_master]] | Plantilla validada | Base obligatoria para nuevas notas.
| [[legacy_reference_pool/README]] | Referencias históricas | Consultar experimentos y reglas previas.

> [!tip] Mantén sincronizado este índice con GitHub y Obsidian para que Codex/GPT5 accedan siempre a la versión oficial.

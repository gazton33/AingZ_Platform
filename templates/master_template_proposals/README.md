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
=======
  id: obsidian_master_templates_index_2025_09
  name: ObsidianMasterTemplatesIndex
  version: 0.1.0
  owner: AingZ_Platform
  status: draft
context:
  dom: KnowledgeArchitecture
  goals:
    - index_template_proposals
    - document_selection_criteria
  risks:
    - misalignment_with_ruleset
    - usability_overload
compat:
  platforms: [Obsidian]
  connectors: [GitHub]
  notes: "Master templates en exploración."
---

# Índice de propuestas para el nuevo master template Obsidian

| Código | Nombre | Enfoque principal | Highlight interactivo |
| ------ | ------ | ----------------- | ---------------------- |
| `NEXUS` | [obsidian_master_template_proposal_nexus](obsidian_master_template_proposal_nexus.md) | Orquestación integral (estrategia + ejecución) | Tabs CSS + callouts DO/DON'T + Dashboard Dataview |
| `ORBIT` | [obsidian_master_template_proposal_orbit](obsidian_master_template_proposal_orbit.md) | Ciclo de proyectos sostenibles | Timeline Buttons + Tracker KPIs |
| `SPECTRUM` | [obsidian_master_template_proposal_spectrum](obsidian_master_template_proposal_spectrum.md) | Gestión de conocimiento y evidencias | Canvas embed + bibliografía dinámica |
| `ORBIT·SPECTRUM PRIME` | [obsidian_master_template_proposal_orbit_spectrum_prime](obsidian_master_template_proposal_orbit_spectrum_prime.md) | Fusión ciclo-proyecto + knowledge fabric con co-working IA/humano | Dataview híbrido + Handshake AI + Canvas/Excalidraw |


## Criterios de evaluación sugeridos

1. **Alineación con RULESET_MAX**: campos obligatorios (`asset`, `context`, `compat`) y contratos visibles.
2. **Eficiencia operativa**: número de acciones críticas accesibles sin abandonar la nota (Buttons, QuickAdd, Dataview inline).
3. **Sostenibilidad y trazabilidad**: properties para impacto ambiental y `WK.log` para retroalimentación.
4. **Escalabilidad**: capacidad de duplicar/parametrizar vía Templater y Dataview.
5. **Experiencia de usuario**: claridad visual, modulación por modos (ejecutivo, foco, bitácora).

> Seleccionar 1 propuesta como base maestra e iterar en modo `working`. Las otras pueden preservarse como variantes o componentes modulares.

## Legacy Reference Pool

- Carpeta dedicada: [`legacy_reference_pool`](legacy_reference_pool/)
- Uso: adjuntar reglas, experimentos y artefactos históricos con frontmatter `legacy_ref: true` para acelerar revisiones.


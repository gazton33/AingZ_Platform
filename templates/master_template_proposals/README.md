---
asset:
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

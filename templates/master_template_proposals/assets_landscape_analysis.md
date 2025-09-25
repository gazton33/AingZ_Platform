---
asset:
  id: repo_asset_landscape_obsidian_2025_09
  name: ObsidianAssetLandscape

  version: 1.1.0
  owner: AingZ_Platform
  status: validated

  version: 0.1.0
  owner: AingZ_Platform
  status: draft

context:
  dom: KnowledgeArchitecture
  goals:
    - map_existing_markdown_assets
    - derive_requirements_for_master_template
  risks:
    - outdated_contracts
    - inconsistent_front_matter
compat:
  platforms: [Obsidian, GPT5, CODEX]
  connectors: [GitHub]

  notes: "Actualizado tras validar el master template Orbit·Spectrum V1."

---

# Panorama de assets Markdown vigentes

> Objetivo: obtener una visión holística de los artefactos activos para fundamentar un nuevo master template compatible con Obsidian y los lineamientos V5.

## 1. Baselines bloqueados

| Ruta | Propósito | Observaciones clave |
| ---- | --------- | ------------------- |
| `core/doc/workbench/AINGZ_V5_Baselines_Unificados_v1_4_1_locked.md` | Consolidado normativo V5 | Define taxonomía y nomenclaturas, sirve como contrato fuente para semántica y jerarquías operativas. |
| `core/doc/workbench/ruleset_baseline_v_1_locked.md` | RULESET base | Enfatiza contratos claros, unicidad de IDs y estructuras modulares RULE/SPEC/ENV/PRC. |
| `core/doc/workbench/glossary_baseline_v_1_locked.md` | Glosario | Garantiza semántica única con definiciones inmutables, imprescindible para properties en Obsidian. |

## 2. Rulesets y contratos activos

- `ruleset/ruleset_master_v_1.md` establece las políticas unificadas para plataformas GPT, Codex, GitHub y Obsidian, incluyendo requisitos de front‑matter y OutputTemplate obligatorio.
- `aing_z_ruleset_max_universal_v_1_0_template.md` codifica el contrato universal con cabecera YAML y jerarquía RULE/SPEC/ENV/PRC, reforzando evidencias, trazabilidad y seguridad.

## 3. Knowledge packs y contextos operativos

| Asset | Rol | Oportunidades para el master template |
| ----- | --- | ------------------------------------- |
| `chat_gpt_plus_knowledge_context_pack_v_1.md` | Paquete de contexto rápido | Estructura ligera con secciones de contexto y prompts; útil para callouts de misión y DO/DON'T. |
| `codex_knowledge_context_pack_literal.md` | Contexto literal | Contiene enumeraciones y snippets reutilizables, ideal para secciones plegables (`> [!example]`) en la plantilla. |
| `kb_obsidian_plugins_core_community_unificado_v_2025_09_02.md` | Inventario Obsidian | Lista plugins core/community activos, habilita uso de Dataview, Buttons, Tracker, Templater y Canvas como elementos soportados. |

## 4. Recursos operativos complementarios

- `test_suite_obsidian_plugins_core_community_v_1.md` documenta verificaciones sugeridas para plugins, relevante para checklists automatizadas.
- `ruleset/context_pack_index.md` inventaría context packs y minipacks, mostrando conveniencia de tablas índice y enlaces cruzados.
- `main/data_base` replica baselines en modo distribuido (`glossary`, `dir_tree`, `core_actv`), indicando necesidad de queries Dataview o `dataviewjs` para sincronización ligera dentro del vault.

## 5. Requisitos derivados para el nuevo master template

1. **Front‑matter estricto**: campos `asset`, `context`, `compat` alineados con RULESET_MAX.
2. **Interactividad Obsidian**: compatibilidad con callouts, Tabs (cssclass), Dataview, Buttons y Canvas embeds.
3. **Contratos visibles**: secciones para Inputs/Outputs, checkpoints y logging (`WK.log`).
4. **Modos de vista**: bloques plegables para modo Focus, Resumen ejecutivo y Detalle técnico.
5. **Instrumentación KPI**: tablas dinámicas y trackers para métricas de sostenibilidad e impacto.

## 6. Master template validado

- Plantilla oficial: [[obsidian_master_template_aingz_master]] (`status: validated`).
- Origen: integración de aprendizajes de `legacy_reference_pool` + propuestas Orbit/Spectrum.
- Diferenciadores clave:
  - Contrato AI↔humano explícito (sección [[obsidian_master_template_aingz_master#01 · AI ↔ Humano Handshake]]).
  - Interactividad ampliada (Buttons, Dataview, Tasks, Tracker, Canvas placeholders) con wikilinks para navegación Obsidian.
  - KPIs y sostenibilidad incorporados en [[obsidian_master_template_aingz_master#40 · Impacto & Sostenibilidad]].

## 7. KPI propuestos para evaluar adopción


| KPI | Descripción | Métrica asociada |
| --- | ----------- | ---------------- |
| `TemplateCoverage` | % de notas nuevas que usan el master template | `#NotasTemplate / #NotasNuevas` (Dataview). |
| `InteractionDepth` | Promedio de componentes interactivos utilizados por nota | Conteo de callouts, tasks y embeds. |
| `SustainabilityTrace` | Notas con properties de impacto ambiental completadas | `dv.pages().where(p => p.impact_carbon)` |
| `FeedbackLoopTime` | Tiempo desde creación a primera retroalimentación registrada | `date(first_feedback) - date(created)`. |

---

> Próximo paso: monitorear KPIs, registrar insights en `legacy_reference_pool` y, si es necesario, preparar una nueva propuesta para revisión formal.


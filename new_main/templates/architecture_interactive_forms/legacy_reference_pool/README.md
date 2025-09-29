---
asset_id: "legacy_pool_architecture_forms_v1"
asset_type: "reference_pool"
asset_version: "1.0.0"
asset_owner: "AingZ_Platform"
asset_status: "active"
asset_tags:
  - architecture
  - legacy
  - reference
asset_updated: "2024-09-30"
---

# Legacy Reference Pool · Formularios Arquitectura

> [!info] Propósito
> Centralizar anexos, decisiones históricas y snapshots vinculados a los formularios de arquitectura y dir tree para acelerar iteraciones futuras sin releer todo el repositorio.

## Convenciones de carga

| Campo | Requisito |
| --- | --- |
| Nombre de archivo | `YYYYMMDD_contexto_descriptivo.md` |
| Frontmatter mínimo | `asset_id`, `asset_status`, `origen_repo`, `resumen` |
| Enlaces recomendados | Wikilinks a rulesets, diagramas Excalidraw, commits relevantes |

## Carpetas sugeridas

- `decisions/` · Registro de decisiones con impacto arquitectónico.
- `snapshots/` · Capturas Mermaid/Excalidraw versionadas.
- `evidence/` · Adjuntos técnicos (logs, métricas, auditorías).

> [!tip] Para activos grandes, almacenar en `attachments/` y enlazar mediante `![[path/to/file]]`.

## Integraciones clave

- `[[ruleset/ruleset_master_v_1]]`
- `[[templates/master_template_proposals/legacy_reference_pool/README|Legacy Master Templates]]`
- `[[templates/architecture_interactive_forms/obsidian_architecture_master_form|Formulario Maestro Arquitectura]]`
- `[[templates/architecture_interactive_forms/dir_tree_creator_form|Dir Tree Creator]]`

> [!warning] Mantén `asset_status` actualizado (`active`, `deprecated`, `archived`) para permitir consultas Dataview globales.

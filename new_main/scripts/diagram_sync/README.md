# Diagram Sync Toolkit (Seed)

Este directorio concentra utilidades para sincronizar diagramas Mermaid ↔ Excalidraw ↔ YAML.

## Objetivos
- Automatizar la extracción de nodos desde `*.excalidraw` y generar snapshots YAML.
- Regenerar diagramas Mermaid a partir del snapshot para mantener la documentación alineada.
- Validar diffs entre versiones del árbol y emitir reportes de cobertura de assets.

## Tareas pendientes
- [ ] Implementar script (Python/Node) que use `lz-string` para descomprimir `dir_tree_draft.excalidraw`.
- [ ] Emitir `dir_tree_snapshot.yaml` y compararlo con el bloque en `templates/architecture_interactive_forms/dir_tree_creator_form.md`.
- [ ] Integrar validaciones en pipelines (GitHub Actions / Scripts locales).


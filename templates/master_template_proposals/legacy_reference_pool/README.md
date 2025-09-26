# Legacy Reference Pool for Master Templates

Este contenedor centraliza materiales históricos, reglas previas y artefactos de soporte relacionados con el desarrollo de los master templates y RULESET.

## Propósito
- Facilitar la consulta incremental sin reanalizar todo el repositorio.
- Versionar lineamientos, experimentos y ejemplos relevantes para la evolución de la plantilla maestra.
- Servir como punto de carga de anexos (`.md`, `.json`, `.canvas`, `.excalidraw`, etc.) que deban incorporarse en futuras iteraciones.

## Convenciones de carga
1. **Naming**: `YYYYMMDD_contexto_descripcion.md` (adaptar extensión según corresponda).
2. **Frontmatter recomendado**:
   ```yaml
   legacy_ref: true
   scope: [template, ruleset]
   source: <origen>
   notes: <detalle breve>
   ```
3. **Referencias cruzadas**: incluir enlaces de retorno hacia la versión activa del master template o al RULESET vigente.
4. **Control de cambios**: resumir en la parte superior qué conocimiento aporta y si reemplaza documentos previos.

## Workflow sugerido
- Al incorporar nuevo material, registrar un breve changelog en `templates/master_template_proposals/README.md` dentro de la sección de notas futuras.
- Utilizar este folder como staging para insights que la IA (Codex / ChatGPT) y el equipo humano puedan incorporar en sesiones de co-diseño.

> Mantener el contenido curado y etiquetado para habilitar búsquedas rápidas desde Dataview (`WHERE legacy_ref = true`).
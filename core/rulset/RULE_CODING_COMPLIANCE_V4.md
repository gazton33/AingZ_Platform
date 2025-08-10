---
CODE: DOC
ID: RULE_CODING_COMPLIANCE_V4_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/core/rulset/RULE_CODING_COMPLIANCE_V4.md
CROSSREF:
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - core/rulset/RULE_NAMING_METADATA_CROSSREF_V1.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# RULE_CODING_COMPLIANCE_V4

## Estilo
- Sigue PEP8 y PEP257.
- Indenta con cuatro espacios y evita tabuladores.
- Máximo 88 caracteres por línea y una línea en blanco al final del archivo.

## Naming
- Funciones y variables: `snake_case`.
- Clases y excepciones: `PascalCase`.
- Constantes y flags: `UPPER_SNAKE_CASE`.
- Archivos: `lower_snake_case` y extensión acorde (`.py`, `.md`).

### Ejemplo
```python
# Conformidad
def calculate_offset(value: int) -> int:
    """Devuelve el offset."""
    return value + 1

# Incumplimiento
def CalculateOffset( value ):
return value+1  # sin indentación y estilo incorrecto
```

## Metadatos YAML
- Todo documento debe iniciar con un bloque YAML con claves `CODE`, `ID`, `VERSION`,
  `ROUTE`, `CROSSREF`, `AUTHOR` y `DATE`.
- `CROSSREF` lista rutas relativas existentes al _Blueprint_, _Master Plan_,
  _Prompt Codex_ y reglas relacionadas.
- Valida metadatos con `python ops/validate_metadata.py <ruta>`.

### Ejemplo
```yaml
# Conformidad
CODE: DOC
ID: example_v1
VERSION: v1.0-2025-08-10
ROUTE: path/to/doc.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10

# Incumplimiento (faltan claves y rutas inválidas)
CODE: DOC
CROSSREF:
  - missing/path.md
```

## Crossrefs
- Toda ruta en `CROSSREF` debe existir y actualizarse al mover archivos.
- Utiliza `python ops/update_crossrefs.py` para regenerar referencias cuando sea necesario.

### Ejemplo
```yaml
# Conformidad
CROSSREF:
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md

# Incumplimiento
CROSSREF:
  - lifecycle/temp/inexistente.md  # archivo no encontrado
```

## OutputTemplate
```yaml
CODE:
ID:
VERSION:
ROUTE:
CROSSREF:
AUTHOR:
DATE:
```

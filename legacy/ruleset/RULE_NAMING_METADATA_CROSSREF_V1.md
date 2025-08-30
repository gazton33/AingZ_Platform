---
CODE: DOC
ID: RULE_NAMING_METADATA_CROSSREF_V1
VERSION: v1.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/legacy/ruleset/RULE_NAMING_METADATA_CROSSREF_V1.md
CROSSREF:
  - legacy/ruleset/RULE_CODING_COMPLIANCE_V4.md
  - README.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# RULE_NAMING_METADATA_CROSSREF_V1

Políticas globales para convenciones de naming, metadatos YAML y mantenimiento de referencias cruzadas.

## 1. Naming
- Idioma: inglés o español claro.
- Formato recomendado: *snake_case* (`[a-z0-9_]+`).
- Usar `_` como separador y mayúsculas solo para acrónimos clave (`RULE`, `README`).
- Prohibidos espacios, caracteres especiales o nombres genéricos (`final.md`, `temp.txt`).
- Incluir sufijo de versión al final (`_v1`, `_v2_20250810`).

**Conforme**
- `core/data/readme_core_data_rw_b_v_3_2.md`
- `ops/scripts/deploy_pipeline_v1.sh`

**No Conforme**
- `core/data/ReadMeCoreData.md`
- `ops/scripts/deploy pipeline.sh`

## 2. Metadatos YAML
- Todo archivo de documentación inicia con bloque YAML con campos obligatorios:
  `CODE`, `ID`, `VERSION`, `ROUTE`, `CROSSREF`, `AUTHOR`, `DATE`.
- `ROUTE` debe ser absoluta; `CROSSREF` una lista de rutas relativas existentes.
- `DATE` en formato ISO (`YYYY-MM-DD`).

**Conforme**
```yaml
---
CODE: READM
ID: ejemplo_readme
VERSION: v1.0-2025-08-10
ROUTE: /abs/path/ejemplo_readme.md
CROSSREF:
  - ruleset/legacy/RULE_NAMING_METADATA_CROSSREF_V1.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
```

**No Conforme**
```yaml
CODE: ejemplo
VERSION: 1.0
ROUTE: relative/path.md
---
```

## 3. Crossref
- Al mover o renombrar archivos citados, actualizar rutas en `CROSSREF` y en el cuerpo del documento.
- Las rutas deben ser relativas al repo y resolver a archivos existentes.
- Evitar URLs externas o rutas rotas.

**Conforme**
- `CROSSREF: [README.md, legacy/ruleset/RULE_CODING_COMPLIANCE_V4.md]`

**No Conforme**
- `CROSSREF: [docs/old_readme.md, http://externo.com/doc.md]`

---
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

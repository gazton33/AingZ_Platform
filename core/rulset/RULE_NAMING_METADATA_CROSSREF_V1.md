---
CODE: DOC
ID: RULE_NAMING_METADATA_CROSSREF_V1
VERSION: v1.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/core/rulset/RULE_NAMING_METADATA_CROSSREF_V1.md
CROSSREF:
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
  - README.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# RULE_NAMING_METADATA_CROSSREF_V1

Políticas globales para convenciones de naming, metadatos YAML y mantenimiento de referencias cruzadas.

## 1. Naming
- Archivos y directorios en inglés o español claro.
- Usar `_` como separador y mayúsculas para acrónimos clave (`RULE`, `README`).
- Incluir sufijo de versión al final (`_v1`, `_v2_20250810`).

**Conforme**
- `core/data/readme_core_data_rw_b_v_3_2.md`

**No Conforme**
- `core/data/ReadMeCoreData.md`

## 2. Metadatos YAML
- Todos los archivos de documentación deben iniciar con bloque YAML con campos: `CODE`, `ID`, `VERSION`, `ROUTE`, `CROSSREF`, `AUTHOR`, `DATE`.
- Mantener rutas absolutas en `ROUTE` y listas reales en `CROSSREF`.

**Conforme**
```yaml
---
CODE: READM
ID: ejemplo_readme
VERSION: v1.0-2025-08-10
ROUTE: /abs/path/ejemplo_readme.md
CROSSREF:
  - core/rulset/RULE_NAMING_METADATA_CROSSREF_V1.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
```

**No Conforme**
```yaml
CODE: ejemplo
VERSION: 1.0
---
```

## 3. Crossref
- Al mover o renombrar archivos citados, actualizar todas las rutas en `CROSSREF` y en el cuerpo del documento.
- Las listas `CROSSREF` deben apuntar a rutas relativas válidas dentro del repo.

**Conforme**
- `CROSSREF: [README.md, core/rulset/RULE_CODING_COMPLIANCE_V4.md]`

**No Conforme**
- `CROSSREF: [http://externo.com/doc.md]`

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

---

## asset: id: md\_full\_test\_harness\_v0 name: MD\_Full\_Test\_Harness kind: DOC version: 0.1.0-draft owner: AingZ\_Platform · ArchOps status: working schema: {id: md.master.v0, version: 0.1.0} context: dom: Templates\_MD summary: "Harness integral para validar Master MD v0 en Obsidian y Canvas" compat: {platforms: [OBSIDIAN, GPT5]} logs: {created\_at: 2025-09-24T00:05:00-03:00, updated\_at: 2025-09-24T00:05:00-03:00}

# 0) Objetivo

Probar end‑to‑end el **Master MD v0**:front‑matter, catálogos, enlaces, Templater, Dataview, Buttons, Modal Forms y Tasks. Resultado: checklist de QA y reporte Dataview.

# 1) Preparación

- Plugins requeridos: **Dataview**, **Templater**, **Buttons**, **Modal Forms**, **Tasks**, **Tracker** (opcional).
- Carpeta de pruebas: `sandbox/master_md_v0/`.

# 2) Caso base — crear documento válido

1. Crear una nueva nota con el siguiente FM mínimo.
2. Guardar en `sandbox/master_md_v0/ExampleMasterDoc.md`.
---
asset:
  id: md_example_001
  name: ExampleMasterDoc
  kind: DOC
  version: 0.1.0-draft
  owner: AingZ_Platform · ArchOps
  status: working
schema: {id: md.master.v0, version: 0.1.0}
context:
  dom: Templates_MD
  summary: "Documento de ejemplo que cumple Master MD v0"
compat: {platforms: [GPT5, OBSIDIAN]}
refs: []
tags: [aingz, md]
logs: {created_at: 2025-09-24T00:05:00-03:00, updated_at: 2025-09-24T00:05:00-03:00}
---
```

# 3) Validaciones Dataview

## 3.1 Requeridos faltantes

```dataview
TABLE file.link AS Nota, asset.kind, asset.status, context.dom, asset.version
FROM "sandbox/master_md_v0"
WHERE !asset OR !asset.kind OR !asset.status OR !context.dom OR !asset.version
SORT file.mtime DESC
```

## 3.2 Catálogos inválidos

```dataview
TABLE file.link AS Nota, asset.kind, context.dom, compat.platforms
FROM "sandbox/master_md_v0"
WHERE (asset.kind AND !contains(["RULE","SPEC","ENV","PRC","WK","CHK","VALD","AUDT","RPT","DOC","TPL"], asset.kind))
   OR (context.dom AND !contains(["Templates_MD","Rulesets","Workflows","Ops","Knowledge","Reports"], context.dom))
```

## 3.3 SemVer y status

```dataview
TABLE file.link, asset.version, asset.status
FROM "sandbox/master_md_v0"
WHERE !regexmatch("^\\d+\\.\\d+\\.\\d+(-[A-Za-z0-9]+)?$", asset.version)
OR !contains(["draft","working","final"], asset.status)
```

## 3.4 Rutas duras

```dataview
TABLE file.link
FROM "sandbox/master_md_v0"
WHERE contains(string(this.file.contents), ":\\\\") OR contains(string(this.file.contents), "/Users/") OR contains(string(this.file.contents), "/home/")
```

# 4) Macros Templater

## 4.1 Actualizar `updated_at`

```tpl
<%*
await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
  fm.logs = fm.logs || {};
  fm.logs.updated_at = tp.date.now('YYYY-MM-DDTHH:mm:ssZ');
});
-%>
```

## 4.2 Bump SemVer (PATCH)

```tpl
<%*
function bumpPatch(v){
  const m = (v||'0.0.0').match(/(\d+)\.(\d+)\.(\d+)(-.+)?/);
  if(!m){return '0.1.0-draft'}
  return `${m[1]}.${m[2]}.${parseInt(m[3])+1}${m[4]||''}`
}
await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
  fm.asset = fm.asset || {};
  fm.asset.version = bumpPatch(fm.asset.version)
});
-%>
```

# 5) Buttons

```button
name Update timestamp
type command
action Templater: Replace templates in the active file
```

# 6) Modal Forms (mínimo)

```yaml
# forms/master_md_min.yaml
fields:
  - key: asset.name
    label: Nombre (PascalCase)
    type: text
    required: true
  - key: asset.kind
    type: select
    options: [RULE, SPEC, ENV, PRC, WK, CHK, VALD, AUDT, RPT, DOC, TPL]
  - key: context.dom
    type: select
    options: [Templates_MD, Rulesets, Workflows, Ops, Knowledge, Reports]
  - key: asset.status
    type: select
    options: [draft, working, final]
```

# 7) Tasks de QA

-

# 8) Panel de reporte

```dataview
TABLE WITHOUT ID
  length(rows) AS Total,
  length(rows WHERE !asset OR !asset.kind OR !asset.status OR !context.dom OR !asset.version) AS Faltantes,
  length(rows WHERE !regexmatch("^\\d+\\.\\d+\\.\\d+(-[A-Za-z0-9]+)?$", asset.version)) AS VersionInvalida
FROM "sandbox/master_md_v0"
```

# 9) Canvas vs Obsidian

- Canvas: edición del MD. Probar copiado/pegado de FM y cuerpo.
- Obsidian: ejecutar consultas y macros.

# 10) Resultado esperado

Cero filas en 3.1–3.4 y panel con `Faltantes = 0` y `VersionInvalida = 0`. Si aparece error, anotar nota y causa para corrección del **Master MD v0**.


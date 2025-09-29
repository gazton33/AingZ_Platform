---

## asset: id: master\_md\_format\_v0 name: Master\_MD\_Format version: 0.1.0-draft owner: AingZ\_Platform · ArchOps status: draft schema: id: md.master.v0 version: 0.1.0 context: dom: Templates\_MD goals: ["Definir contrato maestro para todos los .md", "Alinear Canvas/Obsidian bajo Clean Architecture"] risks: ["Deriva de claves YAML", "Plugins no disponibles en Canvas", "Rutas absolutas"] compat: platforms: [GPT5, OBSIDIAN, VSC] connectors: [GitHub] notes: "Diseño plugin-agnóstico. Validación avanzada se hace en Obsidian." logs: created\_at: 2025-09-24T00:00:00-03:00 updated\_at: 2025-09-24T00:00:00-03:00

# 0) Propósito

Contrato unificado de **front‑matter + convenciones** para cualquier Markdown del ecosistema AingZ. Usable en **ChatGPT Canvas** sin plugins y validable en **Obsidian** con stack de plugins.

# 1) Clean Architecture aplicada a MD

 **Domain (qué)**: contenido semántico, glosario, entidades y relaciones.
- **Application (cómo)**: workflows, checklists, validaciones, procesos.
- **Interface (UI)**: Canvas/Obsidian como vistas y formularios.
- **Infrastructure**: plugins (Dataview, Templater, Modal Forms, Tasks, Tracker). Separación: el **front‑matter** es la API del Domain; los plugins son adapters.

# 2) Master Front‑Matter Schema (v0)

## 2.1 Requeridos

```yaml
asset:
  id: <uid/slug>
  name: <PascalCase>
  kind: RULE|SPEC|ENV|PRC|WK|CHK|VALD|AUDT|RPT|DOC|TPL
  version: <SemVer>
  owner: AingZ_Platform · <Equipo>
  status: draft|working|final
context:
  dom: <DomainCatalog>
  summary: <Descripción breve 1–2 líneas>
compat:
  platforms: [GPT5, OBSIDIAN]
logs:
  created_at: <iso8601>
  updated_at: <iso8601>
```

## 2.2 Opcionales (recomendados)

```yaml
schema: {id: md.master.v0, version: 0.1.0}
refs: [<wikilink|mdlink>]
tags: [aingz, md]
security: {class: public|internal|restricted, retention_days: 3650}
audit: {created_by: <who>, reviewed_by: <who?>, review_at: <iso8601?>}
VALM:
  criteria:
    - {id: citations_web, metric: coverage_pct, target: ">= 0.9"}
    - {id: tests_green, metric: pass_rate, target: 1.0}
integrity: {hash: <sha256-of-body>}
i18n: {lang: es, alt_langs: [en]}
ui: {layout: default, forms: modal|inline, controls: [buttons, tasks]}
```

## 2.3 Catálogos (controlados)

```yaml
CATALOGS:
  DomainCatalog: [Templates_MD, Rulesets, Workflows, Ops, Knowledge, Reports]
  KindCatalog:   [RULE, SPEC, ENV, PRC, WK, CHK, VALD, AUDT, RPT, DOC, TPL]
  Platforms:     [GPT5, OBSIDIAN, VSC, OPENAI_API, GH_BOT, PY]
  Status:        [draft, working, final]
  Security:      [public, internal, restricted]
```

# 3) Convenciones de archivos y enlaces

- **Nombre de archivo**: `YYYYMMDD__<kind>__<slug>.md` o `<kind>__<PascalCase>.md`.
- **Wikilinks** `[[...]]` preferidos para navegación; **mdlinks** relativos permitidos.
- **Prohibido**: rutas absolutas; anchors a IDs volátiles.
- **Cross‑refs**: declarar en `refs[]` y referenciar en cuerpo.
- **Tags**: taxonomía corta y estable.

# 4) Reglas de formato YAML

- Orden recomendado: `asset > schema > context > compat > refs > tags > security > audit > VALM > integrity > ui > logs`.
- Strings cortos inline; listas en multilínea.
- Sin tabs; 2 espacios; claves en `snake_case` salvo `PascalCase` para `asset.name`.
- SemVer `MAJOR.MINOR.PATCH[-label]`.

# 5) Lint/Validación (Canvas/Obsidian)

## 5.1 Dataview — faltantes críticos

```dataview
TABLE file.link AS Nota, asset.kind, asset.status, context.dom, asset.version
WHERE !asset OR !asset.kind OR !asset.status OR !context.dom OR !asset.version
SORT file.mtime DESC
```

## 5.2 Dataview — catálogos inválidos

```dataview
TABLE file.link AS Nota, asset.kind, context.dom, compat.platforms
WHERE asset.kind AND !contains(["RULE","SPEC","ENV","PRC","WK","CHK","VALD","AUDT","RPT","DOC","TPL"], asset.kind)
OR   context.dom AND !contains(["Templates_MD","Rulesets","Workflows","Ops","Knowledge","Reports"], context.dom)
```

## 5.3 Templater — auto‑update `updated`

```tpl
<%*
await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
  fm.logs = fm.logs || {};
  fm.logs.updated_at = tp.date.now('YYYY-MM-DDTHH:mm:ssZ');
});
-%>
```

## 5.4 Buttons — crear nota desde master

```button
name Nueva nota (Master MD)
type command
action Templater: Create new note from template
```

## 5.5 Modal Forms — schema mínimo

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
    required: true
  - key: context.dom
    type: select
    options: [Templates_MD, Rulesets, Workflows, Ops, Knowledge, Reports]
    required: true
  - key: asset.status
    type: select
    options: [draft, working, final]
    required: true
```

# 6) Reglaset Obsidian — plataforma AingZ (v0)

1. **Templater** obligatorio para escritura de `logs.updated_at` y SemVer bump.
2. **Dataview** como única fuente de consultas; prohibido usar rutas absolutas.
3. **Modal Forms** para alta/edición de FM contra catálogos.
4. **Buttons** para acciones estándar: nueva nota, bump de versión, publicar.
5. **Tasks** para QA y revisiones con `#qa`.
6. **Tracker** opcional para métricas VALM por vault.
7. **Convención de directorios**: `templates/`, `rules/`, `workflows/`, `knowledge/`, `reports/`.

# 7) Ejemplo mínimo válido (copiable)

```yaml
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
refs: [[RULESET_MAX]], [[GLOS::Code_Semantics]]
tags: [aingz, md]
security: {class: internal, retention_days: 3650}
audit: {created_by: ai, reviewed_by: null, review_at: null}
VALM:
  criteria:
    - {id: citations_web, metric: coverage_pct, target: ">= 0.9"}
    - {id: tests_green, metric: pass_rate, target: 1.0}
integrity: {hash: null}
ui: {layout: default, forms: modal, controls: [buttons, tasks]}
logs: {created_at: 2025-09-24T00:00:00-03:00, updated_at: 2025-09-24T00:00:00-03:00}
---
```

# 8) Mapeo desde legacy → master

| Legacy                           | Master                                  |
| -------------------------------- | --------------------------------------- |
| `asset.status` duplicado         | Mantener solo bajo `asset.status`       |
| `compat.notes` rutas duras       | Remover; usar mdlinks o wikilinks       |
| `owner` libre                    | Normalizar `AingZ_Platform · <Equipo>`  |
| Falta `kind`                     | Introducir `asset.kind` según catálogo  |
| `context.goals`/`risks` disperso | Mantener, pero `summary` es obligatorio |

# 9) QA Checklist (VALM aplicado)

-

# 10) Roadmap a v1.0.0

- v0.2: JSON Schema opcional y validador Templater.
- v0.3: Macros de bump SemVer y publicación.
- v0.4: Panel Dataview de auditoría completa.
- v1.0: Congelar schema, publicar RULE + SPEC de Master MD.


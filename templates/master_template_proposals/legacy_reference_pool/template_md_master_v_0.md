---

file: Template\_MD\_Master\_v0\_3b\_seed.md code: MD name: Template\_MD\_Master version: 0.3.0-draft kind: DOC status: working date: 2025-09-24 owner: AingZ\_Platform · ArchOps ruleset: MD\_MASTER\_V0 platforms:

- GPT5
- OBSIDIAN
- VSC triggers:
- TRG\_LINT\_YAML
- TRG\_QA\_VALM
- TRG\_PUBLISH chg: CHG#md\_master\_v0 chk: CHK#md\_master\_v0 note: Seed único, reemplaza legacy. Incluye schema FLAT, harness, NESTED ref, QA, macros, settings y métricas. Listo para ctx-pack en hilos nuevos. updated: 2025-09-24T00:00:00-03:00

---

# 0) Propósito

Usar **un solo archivo** como: (a) **template maestro** MD, (b) **ruleset Obsidian** y (c) **harness de pruebas**. Es seed suficiente para iniciar cualquier hilo nuevo.

# 1) Clean Architecture aplicada

- **Domain:** front‑matter FLAT. Glosario: CodeSemanticsV5.
- **Application:** workflows QA, LDM, publicación.
- **Interface:** Obsidian+Canvas (validación/edición).
- **Infrastructure:** plugins (Dataview, Templater, Modal Forms, Buttons, Tasks).

# 2) Master Front-Matter — FLAT

Campos requeridos: `file, code, name, kind, version, date, owner, status, ruleset, platforms, updated`.

```yaml
---
file: Template_MD_Master_v0_3b_seed.md
code: MD
name: Template_MD_Master
kind: DOC
version: 0.3.0-draft
date: 2025-09-24
owner: AingZ_Platform · ArchOps
status: working
ruleset: MD_MASTER_V0
platforms:
  - GPT5
  - OBSIDIAN
  - VSC
triggers:
  - TRG_LINT_YAML
  - TRG_QA_VALM
  - TRG_PUBLISH
chg: CHG#md_master_v0
chk: CHK#md_master_v0
note: Seed único, reemplaza legacy. Incluye schema FLAT, harness, NESTED ref, QA, macros, settings y métricas. Listo para ctx-pack en hilos nuevos.
updated: 2025-09-24T00:00:00-03:00
---
```

# 2.1 NESTED equivalente (referencia)

```yaml
---
asset:
  id: md_master_seed
  name: Template_MD_Master
  kind: DOC
  version: 0.3.0-draft
  owner: AingZ_Platform · ArchOps
  status: working
schema:
  id: md.master.v0
  version: 0.1.0
context:
  dom: Templates_MD
  summary: "Referencia NESTED solo si se requiere jerarquía."
compat:
  platforms:
    - GPT5
    - OBSIDIAN
logs:
  created_at: 2025-09-24T00:00:00-03:00
  updated_at: 2025-09-24T00:00:00-03:00
---
```

# 2.2 Mapeo NESTED ⇄ FLAT

| Nested             | FLAT                |
| ------------------ | ------------------- |
| asset.id           | file/codigo         |
| asset.name         | name                |
| asset.kind         | kind                |
| asset.version      | version             |
| asset.owner        | owner               |
| asset.status       | status              |
| schema.id          | ruleset             |
| context.dom        | dom (si lo agregás) |
| compat.platforms[] | platforms[]         |
| logs.created\_at   | date                |
| logs.updated\_at   | updated             |

# 3) Convenciones y settings

- Archivo: `YYYYMMDD__<kind>__<slug>.md` o `<kind>__<PascalCase>.md`.
- Enlaces: `[[wikilinks]]` preferidos, mdlinks relativos permitidos. Prohibidas rutas absolutas.
- YAML: siempre multilínea para listas, sin `{}` inline. 2 espacios de indent.
- Settings Dataview: keyword DVJS: `dataviewjs`, prefijos `=`, `$=`, inline queries ON, auto-refresh ON, render null `\-`, intervalo `2500` ms.

# 4) Harness/QA integrado

## 4.1 DVQL — requeridos faltantes (NESTED)

```dataview
TABLE file.link AS Nota, asset.kind, asset.status, context.dom, asset.version
FROM "sandbox/master_md_v0"
WHERE !asset OR !asset.kind OR !asset.status OR !context.dom OR !asset.version
SORT file.mtime DESC
```

## 4.2 DVQL — catálogos inválidos (NESTED)

```dataview
TABLE file.link AS Nota, asset.kind, context.dom, compat.platforms
FROM "sandbox/master_md_v0"
WHERE (asset.kind AND !contains(["RULE","SPEC","ENV","PRC","WK","CHK","VALD","AUDT","RPT","DOC","TPL"], asset.kind))
   OR (context.dom AND !contains(["Templates_MD","Rulesets","Workflows","Ops","Knowledge","Reports"], context.dom))
```

## 4.3 DVQL — SemVer y status (NESTED)

```dataview
TABLE file.link, asset.version, asset.status
FROM "sandbox/master_md_v0"
WHERE !regexmatch("^\\d+\\.\\d+\\.\\d+(-[A-Za-z0-9]+)?$", asset.version)
   OR !contains(["draft","working","final"], asset.status)
```

## 4.4 DVQL — rutas duras (NESTED)

```dataview
TABLE file.link
FROM "sandbox/master_md_v0"
WHERE contains(string(this.file.contents), ":\\\\") OR contains(string(this.file.contents), "/Users/") OR contains(string(this.file.contents), "/home/")
```

## 4.5 DVJS — panel agregado (NESTED y FLAT)

```dataviewjs
const P = dv.pages('"sandbox/master_md_v0"');
const get = (p, path) => path.split('.').reduce((o,k)=>o?.[k], p) ?? p[path];
const isSemVer = v => /^\d+\.\d+\.\d+(?:-[A-Za-z0-9]+)?$/.test(v||"");
const falt = P.where(p => !(get(p,'asset.kind') && get(p,'asset.status') && get(p,'context.dom') && get(p,'asset.version')) && !(p.kind && p.status && p.version));
const inval = P.where(p => !isSemVer(get(p,'asset.version') ?? p.version));
dv.table(["Total","Faltantes","VersionInvalida"], [[P.length, falt.length, inval.length]]);
```

# 5) Macros Templater duales

## 5.1 Actualizar timestamp

```tpl
<%*
await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
  const now = tp.date.now('YYYY-MM-DDTHH:mm:ssZ');
  if (fm.logs && typeof fm.logs === 'object') { fm.logs.updated_at = now; }
  else { fm.updated = now; }
});
-%>
```

## 5.2 Bump SemVer (PATCH)

```tpl
<%*
await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
  const cur = (fm.asset && typeof fm.asset === 'object') ? fm.asset.version : fm.version;
  const m = (cur||'0.0.0').match(/(\d+)\.(\d+)\.(\d+)(-.+)?/);
  const next = m ? `${m[1]}.${m[2]}.${parseInt(m[3])+1}${m[4]||''}` : '0.1.0-draft';
  if (fm.asset && typeof fm.asset === 'object') { fm.asset.version = next; }
  else { fm.version = next; }
});
-%>
```

# 6) Modal Forms mínima (FLAT)

```yaml
fields:
  - key: name
    label: Nombre (PascalCase)
    type: text
    required: true
  - key: kind
    type: select
    options: [RULE, SPEC, ENV, PRC, WK, CHK, VALD, AUDT, RPT, DOC, TPL]
  - key: status
    type: select
    options: [draft, working, final]
```

# 7) Ejemplo FLAT para sandbox

```markdown
---
file: ExampleFlat.md
code: MD
name: ExampleFlat
kind: DOC
version: 0.3.0-draft
date: 2025-09-24
owner: AingZ_Platform · ArchOps
status: working
ruleset: MD_MASTER_V0
platforms:
  - GPT5
  - OBSIDIAN
  - VSC
updated: 2025-09-24T00:00:00-03:00
---
```

# 8) LDM migración y QA

- Inventario
- Normalización YAML
- Dedup hash/similitud
- Mapping a FLAT
- Revisión DV/DVJS
- Conflictos/vacíos reportados
- Blueprint y TRG\_PURGE\_AI

# 9) VALM (criterios)

```yaml
VALM:
  criteria:
    - {id: citations_web, metric: coverage_pct, target: ">= 0.9"}
    - {id: tests_green, metric: pass_rate, target: 1.0}
    - {id: ldm_coverage, metric: coverage_pct, target: ">= 0.85"}
    - {id: dedup_ratio, metric: ratio, target: ">= 0.2"}
    - {id: conflict_rate, metric: rate, target: "<= 5"}
    - {id: mapping_confidence, metric: mean, target: ">= 0.75"}
```

# 10) Uso

- Usar este archivo como único ctx-pack, ruleset y test.
- Pegar al iniciar cualquier hilo. No se requiere legacy.
- Mantener actualizado; publicar con `status: final`.




## file: Master\_MD\_Flat\_Profile\_v0\_2.md code: MD name: MasterMD\_Flat\_Profile version: v0.2.0-draft date: 2025-09-24 owner: AingZ\_Platform · ArchOps status: working ruleset: MD\_MASTER\_V0 platforms: [GPT5, OBSIDIAN, VSC] triggers: [TRG\_LINT\_YAML, TRG\_QA\_VALM] chg: CHG#master\_md\_flat\_v0 chk: CHK#master\_md\_flat\_v0 note: Perfil FLAT para front‑matter, compatible con Properties y Dataview. Mapea 1:1 al schema nested.

# 0) Referencia canónica detectada (extracto)

Del adjunto `glos_code_semantics_v_5_main.md`:

```yaml
file: GLOS_Code_Semantics_V5_MAIN.md
code: GLOS
name: CodeSemanticsV5
version: v5.0.0-rc2
date: 2025-08-12
owner: AingZ_Platform · RwB
status: working
ruleset: GLOS_V5_RULES_MIN
platforms:
  - GPT5
  - CODEX
  - OPENAI_API
  - GH_BOT
  - VSC
  - PY
triggers:
  - TRG_AUDIT_TL
  - TRG_CONSOLIDATE_TL
chg: CHG#glosario_v5
chk: CHK#glosario_v5
note: Glosario V5 genérico, sin rutas.
```

# 1) Perfil **FLAT** maestro propuesto

Campos obligatorios: `code, name, version, date, owner, status`. Recomendados: `kind, dom, ruleset, platforms[], triggers[], chg, chk, refs[], tags[], updated`.

```yaml
---
file: <Sugerido_nombre_archivo.md>
code: <SCREAMING_SNAKE ≤5>
name: <PascalCase>
kind: RULE|SPEC|ENV|PRC|WK|CHK|VALD|AUDT|RPT|DOC|TPL
version: 0.2.0-draft
date: 2025-09-24
owner: AingZ_Platform · <Equipo>
status: draft|working|final
ruleset: MD_MASTER_V0
platforms: [GPT5, OBSIDIAN]
triggers: [TRG_LINT_YAML]
dom: Templates_MD
refs: []
tags: [aingz, md]
updated: 2025-09-24T00:00:00-03:00
---
```

# 2) Mapeo NESTED ⇄ FLAT (equivalencia)

| Nested v0            | Flat v0.2                         |
| -------------------- | --------------------------------- |
| `asset.id`           | `file` o `code` según uso         |
| `asset.name`         | `name`                            |
| `asset.kind`         | `kind`                            |
| `asset.version`      | `version`                         |
| `asset.owner`        | `owner`                           |
| `asset.status`       | `status`                          |
| `schema.id`          | `ruleset`                         |
| `schema.version`     | `version` del `ruleset` si aplica |
| `context.dom`        | `dom`                             |
| `compat.platforms[]` | `platforms[]`                     |
| `logs.created_at`    | `date`                            |
| `logs.updated_at`    | `updated`                         |

# 3) DV/DVJS para **FLAT**

## 3.1 Requeridos faltantes

```dataview
TABLE file.link AS Nota, kind, status, dom, version
WHERE !name OR !version OR !status
```

## 3.2 SemVer y status

```dataview
TABLE file.link, version, status
WHERE !regexmatch("^\\d+\\.\\d+\\.\\d+(-[A-Za-z0-9]+)?$", version)
   OR !contains(["draft","working","final"], status)
```

## 3.3 Panel (DVJS)

```dataviewjs
const P = dv.current().file.folder ? dv.pages(dv.current().file.folder) : dv.pages("");
const isSemVer = v => /^\d+\.\d+\.\d+(?:-[A-Za-z0-9]+)?$/.test(v||"");
const falt = P.where(p => !(p.name && p.version && p.status));
const inval = P.where(p => !isSemVer(p.version));
dv.table(["Total","Faltantes","VersionInvalida"], [[P.length, falt.length, inval.length]]);
```

# 4) Macros Templater para **FLAT**

## 4.1 Actualizar `updated`

```tpl
<%*
await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
  fm.updated = tp.date.now('YYYY-MM-DDTHH:mm:ssZ');
});
-%>
```

## 4.2 Bump SemVer (PATCH)

```tpl
<%*
await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
  const m = (fm.version||'0.0.0').match(/(\d+)\.(\d+)\.(\d+)(-.+)?/);
  fm.version = m ? `${m[1]}.${m[2]}.${parseInt(m[3])+1}${m[4]||''}` : '0.1.0-draft';
});
-%>
```

# 5) Reglas de estilo

- Sin `{}` inline en front‑matter. Multilínea para listas.
- `code` corto, `name` en PascalCase.
- Sin rutas absolutas; usar wikilinks/relativos en el cuerpo.

# 6) Ejemplo FLAT válido

```yaml
---
file: ExampleFlatDoc.md
code: MD
name: ExampleFlatDoc
kind: DOC
version: 0.2.0-draft
date: 2025-09-24
owner: AingZ_Platform · ArchOps
status: working
ruleset: MD_MASTER_V0
platforms: [GPT5, OBSIDIAN]
dom: Templates_MD
refs: []
tags: [aingz, md]
updated: 2025-09-24T00:00:00-03:00
---
```

# 7) Decisión

Adoptar **FLAT** como perfil por defecto del Master MD v0. Mantener NESTED solo para casos que necesiten jerarquía. El harness se ajusta a FLAT para evitar “Invalid properties” y para compatibilidad con el YAML funcional de `glos_code_semantics_v_5_main.md`.


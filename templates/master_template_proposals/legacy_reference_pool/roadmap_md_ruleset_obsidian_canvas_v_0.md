---

## file: 20250925\_\_RPT\_\_Roadmap\_MD\_Ruleset\_Obsidian\_Canvas\_v0.md code: PLAN name: Roadmap\_MDRuleset\_ObsidianCanvas kind: RPT version: 0.1.0-draft date: 2025-09-25 owner: AingZ\_Platform · ArchOps status: working ruleset: MD\_MASTER\_V0 platforms: [GPT5, OBSIDIAN] triggers: [TRG\_LINT\_YAML, TRG\_QA\_VALM] updated: 2025-09-25T00:00:00-03:00

# 0) Objetivo

Bloquear un **ruleset de configuración MD** interoperable entre **ChatGPT Canvas** y **Obsidian**. Luego generar y validar los **templates maestros**: RULESET, README, PLAYBOOK y PIPELINE. Cerrar con test de aceptación y publicar baseline `final`.

---

# 1) Alcance y referencias internas

- Perfil **FLAT** maestro y mapeo NESTED⇄FLAT.
- Template maestro único y harness integrado.
- Settings validados de Dataview.
- Test suites para el stack de Obsidian.

> Refs internas: Master\_MD\_Flat\_Profile\_v0, Template\_MD\_Master\_v0\_3b\_seed, Harness\_Dataview\_Settings\_v0, Master\_MD\_Format\_v0, Test\_Suite\_Obsidian\_Plugins\_v1, Obsidian\_Stack\_Validator\_v1, BrainstormingTemplatesMD\_v0.

---

# 2) Fases, entregables y criterios de aceptación

## Fase A — Configuración base (Canvas ↔ Obsidian)

**Entregables**

- A1. RULE: `MD_MASTER_V0` actualizado (perfil **FLAT** como default; NESTED solo de referencia).
- A2. Carpeta sandbox `sandbox/master_md_v0/` con ejemplo **válido** FLAT.
- A3. Settings Dataview aplicados en vault.

**Criterios de aceptación**

- CA-1: Sin “Invalid properties” en notas FLAT.
- CA-2: DV panel muestra `Faltantes = 0` y `VersionInvalida = 0`.

## Fase B — Templates maestros

**Entregables**

- B1. `tpl_ruleset.md` (RULE).
- B2. `tpl_readme.md` (DOC).
- B3. `tpl_playbook.md` (PRC/WK según caso).
- B4. `tpl_pipeline.md` (PRC/OPS).
- B5. Formulario mínimo `forms/master_md_min.yaml` y macros Templater (`updated`, bump SemVer PATCH).

**Criterios de aceptación**

- CB-1: Creación desde template sin edición manual de YAML.
- CB-2: SemVer bump automático funcional.

## Fase C — QA en Obsidian (stack y harness)

**Entregables**

- C1. **Full Test Harness** ejecutado en `sandbox/master_md_v0`.
- C2. **Test Suite — Obsidian Plugins (Core+Community)** ejecutada. Pass rate ≥ 95%.
- C3. **Stack Validator v1.1** ejecutado.

**Criterios de aceptación**

- CC-1: Pass rate global ≥ 95% sin bloqueos críticos.
- CC-2: DV consultas de catálogo sin errores; Tasks y Buttons operativos.

## Fase D — Publicación y bloqueo

**Entregables**

- D1. RULE `MD_MASTER_V0` con `status: final` y changelog.
- D2. Anuncio interno + checklist de adopción.

**Criterios de aceptación**

- CD-1: Todos los templates maestros compilados, enlazados y probados.
- CD-2: Zero regresiones en DV/DVJS con sample set de 10+ notas.

---

# 3) Checklist global (marca para avanzar)

-

---

# 4) Bloques operativos para QA

## 4.1 DVQL — faltantes críticos (FLAT o NESTED)

```dataview
TABLE file.link AS Nota, asset.kind, asset.status, context.dom, asset.version
FROM "sandbox/master_md_v0"
WHERE !asset OR !asset.kind OR !asset.status OR !context.dom OR !asset.version
SORT file.mtime DESC
```

## 4.2 DVQL — catálogos inválidos

```dataview
TABLE file.link AS Nota, asset.kind, context.dom, compat.platforms
FROM "sandbox/master_md_v0"
WHERE (asset.kind AND !contains(["RULE","SPEC","ENV","PRC","WK","CHK","VALD","AUDT","RPT","DOC","TPL"], asset.kind))
   OR (context.dom AND !contains(["Templates_MD","Rulesets","Workflows","Ops","Knowledge","Reports"], context.dom))
```

## 4.3 DVQL — SemVer y status

```dataview
TABLE file.link, asset.version, asset.status
FROM "sandbox/master_md_v0"
WHERE !regexmatch("^\\d+\\.\\d+\\.\\d+(-[A-Za-z0-9]+)?$", asset.version)
   OR !contains(["draft","working","final"], asset.status)
```

## 4.4 DVQL — rutas duras

```dataview
TABLE file.link
FROM "sandbox/master_md_v0"
WHERE contains(string(this.file.contents), ":\\\\") OR contains(string(this.file.contents), "/Users/") OR contains(string(this.file.contents), "/home/")
```

## 4.5 DVJS — panel resumen

```dataviewjs
const P = dv.pages('"sandbox/master_md_v0"');
const get = (p, path) => path.split('.').reduce((o,k)=>o?.[k], p) ?? p[path];
const isSemVer = v => /^\d+\.\d+\.\d+(?:-[A-Za-z0-9]+)?$/.test(v||"");
const falt = P.where(p => !(get(p,'asset.kind') && get(p,'asset.status') && get(p,'context.dom') && get(p,'asset.version')) && !(p.kind && p.status && p.version));
const inval = P.where(p => !isSemVer(get(p,'asset.version') ?? p.version));
dv.table(["Total","Faltantes","VersionInvalida"], [[P.length, falt.length, inval.length]]);
```

---

# 5) Plugins y settings mínimos

- **Dataview**: inline `=`, `$=`; auto‑refresh 2500 ms; render null `-`.
- **Templater**: macros `updated` y `bump PATCH` activas.
- **Buttons**: comando “Templater: Replace templates in the active file”.
- **Modal Forms**: `forms/master_md_min.yaml` para alta FM.
- **Tasks**: seguimiento de QA con `#qa`.

---

# 6) Canvas vs Obsidian (criterios prácticos)

| Criterio           | Canvas | Obsidian              |
| ------------------ | ------ | --------------------- |
| Render MD estándar | Sí     | Sí                    |
| Plugins/JS         | No     | Sí                    |
| Tablas dinámicas   | Manual | Dataview              |
| Formularios        | Manual | Modal Forms/Meta Bind |
| Botones            | Manual | Buttons               |
| Métricas           | Manual | Tracker               |

---

# 7) Registro de resultados

- Casos totales:
- Casos OK:
- **Pass rate**:
- Bloqueos:

---

# 8) Cierre y publicación

- Changelog breve por fase.
- Marcar RULE `MD_MASTER_V0` como `final`.
- Archivar sandbox en `snapshots_ctx/` y etiquetar baseline.


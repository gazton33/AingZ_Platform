---

file:20250925\_\_TPL\_\_Template\_MD\_Master\_v1.md code:TPL name:Template\_MD\_Master kind:TPL version:1.0.0-draft date: 2025-09-25 owner: "AingZ\_Platform · ArchOps" status: draft ruleset: MD\_MASTER\_V1 platforms:

- OBSIDIAN
- CANVAS dom: Templates\_MD tags: [tpl, master, md] created: "<% tp.date.now('YYYY-MM-DDTHH\:mm\:ssZ') %>" updated: "<% tp.date.now('YYYY-MM-DDTHH\:mm\:ssZ') %>" bump\_on\_save: false semver\_lineage: ["1.0.0-draft"] acceptance: "Pass≥95%"

---

# 0) Guía rápida

1. Duplicar esta nota para cada nuevo artefacto.
2. Editar **name, kind, status, dom** y **tags**.
3. Ejecutar **Buttons → Templater** para sellar `updated`.
4. Para subir **PATCH**, poner `bump_on_save: true`, ejecutar Templater y volver a `false`.

---

# 1) Metadatos mínimos (perfil FLAT)

- `name` · identificador humano legible.
- `kind` ∈ {RULE, SPEC, ENV, PRC, WK, CHK, VALD, AUDT, RPT, DOC, TPL}.
- `status` ∈ {draft, working, final}.
- `version` · SemVer `MAJOR.MINOR.PATCH[-tag]`.
- `dom` ∈ {Templates\_MD, Rulesets, Workflows, Ops, Knowledge, Reports}.
- `platforms` · lista.

---

# 2) Bloques listos para usar

## 2.1 Buttons → Templater

```button
name Ejecutar Templater (sellar updated / bump opcional)
type command
action Templater: Replace templates in the active file
```

## 2.2 DV inline sanity

`Nombre ⇒` `= this.name`  |  `Versión ⇒` `= this.version`  |  `Estado ⇒` `= this.status`

## 2.3 DVQL — control rápido en `sandbox/master_md_v0`

```dataview
TABLE file.link AS Nota, name, kind, status, version, dom
FROM "sandbox/master_md_v0"
WHERE !name OR !version OR !status OR !kind OR !dom
SORT file.mtime DESC
```

```dataview
TABLE file.link, version, status
FROM "sandbox/master_md_v0"
WHERE !regexmatch("^\\d+\\.\\d+\\.\\d+(-[A-Za-z0-9]+)?$", version)
   OR !contains(["draft","working","final"], status)
```

---

# 3) Macros Templater

## 3.1 Sellar `updated` (siempre)

```tpl
<%*
await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
  const now = tp.date.now('YYYY-MM-DDTHH:mm:ssZ');
  fm.updated = now;
});
-%>
```

## 3.2 Bump SemVer PATCH (según `bump_on_save`)

```tpl
<%*
const shouldBump = tp.frontmatter?.bump_on_save === true;
if (!shouldBump) { tR += ''; return; }
await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
  const cur = fm.version || '0.0.0';
  const m = (cur||'').match(/(\d+)\.(\d+)\.(\d+)(-.+)?/);
  const next = m ? `${m[1]}.${m[2]}.${parseInt(m[3])+1}${m[4]||''}` : '0.1.0-draft';
  fm.version = next;
  fm.semver_lineage = Array.isArray(fm.semver_lineage) ? [...fm.semver_lineage, next] : [next];
});
-%>
```

---

# 4) Secciones maestras (para iterar y perfilar)

## 4.1 RULESET (estructura base)

- Propósito
- Alcance
- Catálogos controlados (kind, dom, status, platforms)
- Normas de FM (FLAT), ejemplos válidos e inválidos
- DVQL de validación
- Criterios de aceptación

## 4.2 README (estructura base)

- Introducción
- Requisitos
- Instalación
- Uso rápido
- Troubleshooting
- Licencia

## 4.3 PLAYBOOK (estructura base)

- Objetivo
- Prerrequisitos
- Pasos operativos
- Validación / Métricas
- Rollback

## 4.4 PIPELINE (estructura base)

- Descripción
- Entradas/Salidas
- Jobs/Stages
- Artefactos
- Notificaciones

---

# 5) Checklist de control del artefacto

-

---

# 6) Notas

- Este template evita propiedades anidadas para compatibilidad con **Properties view**.
- Los DVQL incluidos asumen perfil **FLAT**.
- Para compatibilidad legacy, mantener los queries con fallback en reportes.


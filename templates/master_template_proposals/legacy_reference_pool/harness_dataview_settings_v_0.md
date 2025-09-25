---

## file: Harness\_Dataview\_Settings\_v0.md code: MD name: Harness\_Dataview\_Settings version: v0.1.0-draft date: 2025-09-24 owner: AingZ\_Platform · ArchOps status: working ruleset: MD\_MASTER\_V0 platforms: [OBSIDIAN] updated: 2025-09-24T00:00:00-03:00

# 0) Objetivo

Fijar configuración comprobada de **Dataview** para ejecutar el harness y validar Master MD v0.

# 1) Configuración Dataview verificada

- **Codeblocks → DataviewJS keyword**: `dataviewjs`
- **Inline query prefix**: `=`
- **JavaScript inline query prefix**: `$=`
- **Code block inline queries**: habilitado
- **View → Display result count**: habilitado
- **View → Warn on empty result**: habilitado
- **View → Automatic view refreshing**: habilitado
- **View → Refresh interval**: `2500` ms
- **View → Render null as**: `\-`
- **Date format**: `MMMM dd, yyyy`
- **Date + time format**: `h:mm a - MMMMM dd, yyyy`
- **Tasks**:
  - **Automatic task completion tracking**: habilitado
  - **Use emoji shorthand for completion**: habilitado
  - **Recursive sub-task completion**: habilitado

# 2) Pruebas rápidas (inline)

- **DV inline**: `= this.name`
- **Fecha actualizada**: `= dateformat(this.updated, "yyyy-MM-dd'T'HH:mm:ss")`
- **DVJS inline**: `$= dv.span(dv.current().frontmatter.version)`

# 3) Pruebas en bloque

**DVQL**

```dataview
TABLE file.link, kind, status, version
FROM "sandbox/master_md_v0"
```

**DVJS**

```dataviewjs
const pages = dv.pages('"sandbox/master_md_v0"');
dv.table(["Nota","Versión"], pages.map(p => [p.file.link, p.version ?? p.asset?.version]));
```

# 4) Troubleshooting

- Si un inline no rinde, verificar prefijos `=` y `$=`.
- Si ves *Invalid properties*, usa perfil **FLAT** del Master MD.
- Si una tabla sale vacía, forzar **Refresh** o subir `Refresh interval` temporalmente.

# 5) Referencia

- Harness principal: [[MD — Full Test Harness v0.1 (strict-flat)]]


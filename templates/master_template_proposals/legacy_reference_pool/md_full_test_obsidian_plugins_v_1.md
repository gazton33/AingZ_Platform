---

## file: 20250925\_\_VALD\_\_MD\_Full\_Test\_Obsidian\_Plugins\_v1.md code: VALD name: MD\_Full\_Test\_Obsidian\_Plugins kind: VALD version: 1.0.0-draft date: 2025-09-25 owner: AingZ\_Platform · ArchOps status: working ruleset: MD\_MASTER\_V0 platforms: [OBSIDIAN] updated: 2025-09-25T00:00:00-03:00

# 0) Propósito

Validar la configuración Obsidian (Core + Community) y el **RULESET MD\_MASTER\_V0**. Aceptación ≥ 95% casos OK. Registrar pass rate y bloquear configuración.

---

# 1) Pre‑flight

- Carpeta sandbox: `sandbox/master_md_v0/`
- Crear `sessions/_seed.md` con una tarea demo `- [ ] Tarea demo 📅 2025-09-30`
- **DV inline**: `= this.name` debería rendir.
- **Templater** activo.

---

# 2) Lista de plugins a validar

## 2.1 Core

- Audio recorder
- Backlinks / Outgoing links
- Bases (DB core)
- Bookmarks
- Canvas
- Command palette / Quick switcher / Search / Slash commands
- Daily notes
- Files / File recovery
- Footnotes view
- Format converter
- Graph view
- Note composer
- Outline / Page preview
- Properties view

## 2.2 Community

- Dataview
- Tasks
- Buttons
- Templater
- Modal Forms
- Meta Bind
- Excalidraw
- Linter
- Tracker
- QuickAdd (opcional)

---

# 3) Casuística de prueba

## 3.1 Core — pruebas funcionales

1. **Audio recorder**: Ribbon → micrófono → grabar 5s → stop → insertar `.m4a`.
2. **Backlinks/Outgoing**: crear nota `A` → enlazar `[[B]]` → abrir `B` → verificar backlinks.
3. **Bases**: crear Base `AI_HUM_SESIONES` → columnas `file,objective,horizon,status,due,coverage_pct,latency_budget,stakeholders,tags` → vista `open` con filtro `status != locked`.
4. **Bookmarks**: marcar esta nota y la Base.
5. **Canvas**: `boards/stack_overview.canvas` con 2 tarjetas unidas por flecha.
6. **Command palette/Quick switcher/Search**: ejecutar `Ctrl/Cmd+P`, `Ctrl/Cmd+O`, `Ctrl/Cmd+Shift+F` y `/`.
7. **Daily notes**: abrir `YYYY‑MM‑DD.md`.
8. **Files/File recovery**: crear `sessions/test_core.md` → editar → restaurar snapshot.
9. **Footnotes view**: `Texto[^1]` y `[^1]: nota al pie`.
10. **Format converter**: migrar propiedades antiguas.
11. **Graph view**: grafo global → filtrar tag `#stack/test`.
12. **Note composer**: extraer párrafo a nueva nota.
13. **Outline/Page preview**: navegar encabezados y hovers.
14. **Properties view**: cambiar `status` a `review` desde *File properties*.

## 3.2 Community — pruebas funcionales

1. **Dataview**
   - Debug
     ```dataview
     LIST FROM "sessions"
     ```
   - Tabla
     ```dataview
     TABLE file.link AS Nota, objective, horizon, status, due
     FROM "sessions"
     WHERE status != "locked"
     SORT due ASC
     ```
2. **Tasks**
   ```tasks
   not done
   path includes sessions
   sort by due
   ```
3. **Buttons → Templater**
   ```button
   name Nueva sesión IA
   type command
   action Templater: Create new note from template
   ```
4. **Templater**
   - Actualizar timestamp (FLAT/NESTED compatible)
     ```tpl
     <%*
     await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
       const now = tp.date.now('YYYY-MM-DDTHH:mm:ssZ');
       if (fm.logs && typeof fm.logs === 'object') { fm.logs.updated_at = now; }
       else { fm.updated = now; }
     });
     -%>
     ```
   - Bump SemVer (PATCH)
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
5. **Modal Forms**
   - Schema mínimo `forms/master_md_min.yaml`
     ```yaml
     fields:
       - key: name
         label: Nombre (PascalCase)
         type: text
         required: true
       - key: kind
         type: select
         options: [RULE, SPEC, ENV, PRC, WK, CHK, VALD, AUDT, RPT, DOC, TPL]
         required: true
       - key: status
         type: select
         options: [draft, working, final]
         required: true
     ```
6. **Meta Bind**
   ```meta-bind-input
   frontmatterKey: status
   type: select
   options: [draft, active, review, locked]
   ```
7. **Excalidraw**
   ```markdown
   ![[diagrams/00_INDEX.excalidraw|900]]
   ```
8. **Linter**: ejecutar según reglas del vault y confirmar no rompe FM.
9. **Tracker**
   ````markdown
   ```tracker
   searchType: frontmatter
   searchTarget: coverage_pct
   folder: sessions
   output: line
   ```
   ````
10. **QuickAdd** (opcional): flujo de alta desde template maestro.

---

# 4) Lint/QA sobre sandbox (perfil FLAT)

## 4.1 Requeridos faltantes

```dataview
TABLE file.link AS Nota, kind, status, dom, version
FROM "sandbox/master_md_v0"
WHERE !name OR !version OR !status
```

## 4.2 SemVer y status

```dataview
TABLE file.link, version, status
FROM "sandbox/master_md_v0"
WHERE !regexmatch("^\\d+\\.\\d+\\.\\d+(-[A-Za-z0-9]+)?$", version)
   OR !contains(["draft","working","final"], status)
```

## 4.3 Catálogos inválidos

```dataview
TABLE file.link AS Nota, kind, dom, platforms
FROM "sandbox/master_md_v0"
WHERE (kind AND !contains(["RULE","SPEC","ENV","PRC","WK","CHK","VALD","AUDT","RPT","DOC","TPL"], kind))
   OR (dom AND !contains(["Templates_MD","Rulesets","Workflows","Ops","Knowledge","Reports"], dom))
```

## 4.4 Rutas duras

```dataview
TABLE file.link
FROM "sandbox/master_md_v0"
WHERE contains(string(this.file.contents), ":\\\\") OR contains(string(this.file.contents), "/Users/") OR contains(string(this.file.contents), "/home/")
```

## 4.5 Panel resumen (DVJS)

```dataviewjs
const P = dv.pages('"sandbox/master_md_v0"');
const isSemVer = v => /^\d+\.\d+\.\d+(?:-[A-Za-z0-9]+)?$/.test(v||"");
const falt = P.where(p => !(p.name && p.version && p.status));
const inval = P.where(p => !isSemVer(p.version));
dv.table(["Total","Faltantes","VersionInvalida"], [[P.length, falt.length, inval.length]]);
```

---

# 5) Registro y aceptación

- Casos totales:
- Casos OK:
- **Pass rate**:
- Bloqueos:
- Observaciones:

**Criterio de aceptación**: Pass rate ≥ 95% sin bloqueos críticos. Si falla, iterar configuración y repetir.

---

# 6) Cierre

- Exportar capturas del panel DVJS y listado de casos.
- Publicar `ENV__Obsidian_Config_v1.md` con los plugins habilitados.
- Actualizar `RULE MD_MASTER_V0` a `status: final` cuando el pass rate sea estable.


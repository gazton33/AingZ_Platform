---

## asset: id: tmpl\_md\_brainstorm\_v0 name: BrainstormingTemplatesMD version: 0.1.0 owner: AingZ\_Platform · ArchOps status: draft context: dom: Templates\_MD goals: ["Diseñar set de plantillas Markdown dinámicas", "Compatibles con ChatGPT Canvas y Obsidian"] risks: ["Desalineación semántica con RULESET\_MAX", "Limitaciones de runtime en Canvas"] compat: platforms: [GPT5, OBSIDIAN] notes: "Canvas no ejecuta plugins; Obsidian sí. Integrar por patrones MD neutros." updated: 2025-09-23

# 0) Objetivo y alcance (Fase 1 — MD)

- Entregar **pack de plantillas MD** estandarizadas y reusables.
- Foco: **texto + front‑matter YAML** + bloques interactivos compatibles con Obsidian.
- Validación cruzada en **ChatGPT Canvas** y **Obsidian**.

# 1) Fuentes base

- **Internas**: RULESET\_MAX v1.0, FORM\_LDM Intake, Glosario CODE V5, Inventario Obsidian plugins.
- **Plataforma**: ChatGPT Canvas, Projects + Project‑only memory, Deep Research.
- **Obsidian**: Templater, Dataview, Modal Forms, Meta Bind, Buttons, Tasks, Tracker.

# 2) Principios de diseño (alineados a RULESET\_MAX)

1. **Semántica única**: un término = un concepto (GLOS V5).
2. **Contrato antes que implementación**: front‑matter como API de nota.
3. **Interoperabilidad**: sin rutas duras; crossref semántico.
4. **Evidencia**: cada plantilla define `logs`/`VALM` mínimos.
5. **Evolución controlada**: SemVer + `Deprecated/ReplacedBy`.

# 3) Taxonomía de plantillas MD (mínimo inicial)

- **RULE** · Ruleset universal → `ruleset_*.md`
- **SPEC** · Overrides acotados → `spec_*.md`
- **ENV** · Ajustes por plataforma → `env_*.md`
- **PRC** · Procedimientos → `prc_*.md`
- **WK** · Knowledge/logs → `wk_*.md`
- **CHK** · Checklists → `chk_*.md`
- **VALD** · Validaciones/tests → `vald_*.md`
- **AUDT** · Auditoría → `audt_*.md`
- **RPT** · Reportes → `rpt_*.md`
- **DOC/TMP** · Documentos y plantillas base → `doc_*.md`, `tpl_*.md`

# 4) Front‑matter base (plantilla)

```yaml
asset: {id: <uid>, name: <PascalCase>, version: <SemVer>, owner: AingZ_Platform, status: draft|working|final}
context: {dom: <Domain>, goals: [<g1>,<g2>], risks: [<r1>,<r2>]}
compat: {platforms: [GPT5, OBSIDIAN], connectors: [GitHub, GoogleDrive], notes: "Sin rutas duras"}
VALM: {citations_web: ">=0.9", tests_green: 1.0}
logs: {created_at: <iso8601>, updated_at: <iso8601>}
```

# 5) Patrones MD interactivos para **Obsidian**

- **Dataview**: tablas/listas sobre `front‑matter` e inline fields.
- **Templater**: variables y JS para generar secciones y escribir properties.
- **Modal Forms**: alta/edición guiada de `front‑matter`.
- **Meta Bind**: inputs y vistas atadas a properties.
- **Buttons**: atajos de flujo (crear nota desde template, ejecutar Templater).
- **Tasks**: tareas con recurrencia; tablero con consultas.
- **Tracker**: métricas/series a partir de properties.

### Snippets operativos (mini‑catálogo)

**Dataview → tabla de artefactos**

```dataview
TABLE file.link AS Nota, asset.version, status, dom
FROM "templates"
WHERE status != "final"
SORT file.mtime DESC
```

**Templater → set de properties**

```tpl
<%*
await app.fileManager.processFrontMatter(tp.config.target_file, fm => {
  fm.status = fm.status ?? 'draft';
  fm.updated = tp.date.now('YYYY-MM-DD');
});
-%>
```

**Buttons → nueva nota desde template**

```button
name Nueva plantilla RULE
type command
action Templater: Create new note from template
```

# 6) Patrones **compatibles con Canvas** (sin plugins)

- Edición colaborativa de MD y **front‑matter**.
- Vista/edición de **checklists** y tablas simples.
- Previsualización de **code/html** o **code/react** para prototipos UI de templates.
- Estrategia: diseñar MD **plugin‑agnóstico** y validar en Obsidian.

# 7) Matriz "versus" — Canvas vs Obsidian (v0)

| Criterio           | Canvas        | Obsidian              |
| ------------------ | ------------- | --------------------- |
| Render MD estándar | Sí            | Sí                    |
| Plugins/JS         | No            | Sí                    |
| Tablas dinámicas   | Manual        | Dataview              |
| Formularios        | Manual        | Modal Forms/Meta Bind |
| Botones            | Manual        | Buttons               |
| Métricas/gráficos  | Manual        | Tracker               |
| Vista lienzo       | Canvas nativo | Canvas plugin         |

# 8) Artefactos a generar (backlog v0)

- `tpl_ruleset.md`, `tpl_spec.md`, `tpl_env.md`, `tpl_prc.md`, `tpl_chk.md`, `tpl_vald.md`, `tpl_audt.md`, `tpl_rpt.md`, `tpl_doc_baseline.md`, `tpl_brainstorm.md`, `tpl_decision.md`, `tpl_datasheet.md`.
- `form_modal.yaml` (Modal Forms) + `templater_macros/`.
- `dataview_blocks.md` de referencia.

# 9) Criterios VALM (mínimos)

- `ldm_coverage >= 0.85`, `dedup_ratio >= 0.20`, `mapping_confidence >= 0.75`.
- `%citations_web >= 0.9` para afirmaciones no triviales.

# 10) Preguntas abiertas

- ¿Añadir `SCHEMA` para contratos JSON/YAML por plantilla?
- ¿Estandarizar `IDs` con prefijos por CODE?
- ¿Generar UI mínima en `code/react` para validar front‑matter en Canvas?

# 11) Próximos pasos (iteración inmediata)

1. Escaffold de `tpl_*` con front‑matter base.
2. Prototipos `dataview_blocks.md` y `templater_macros/`.
3. Validación cruzada en Canvas/Obsidian + registro `WK`.
4. Ajustes por feedback y **Blueprint v0**.


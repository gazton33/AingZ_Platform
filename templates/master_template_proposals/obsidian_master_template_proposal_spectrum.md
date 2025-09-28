---
asset:
  id: obsidian_master_template_spectrum_2025_09
  name: ObsidianMasterTemplateSpectrum
  version: 0.1.1
  owner: AingZ_Platform
  status: draft
context:
  dom: KnowledgeSystems
  goals:
    - curate_multidisciplinary_knowledge
    - maintain_traceable_evidence
  risks:
    - reference_drift
    - knowledge_fragmentation
compat:
  platforms: [Obsidian, GPT5, CODEX]
  connectors: [GitHub, Zotero, GoogleDrive]
  notes: "Diseñado para vaults con fuerte componente de investigación."
obsidian:
  cssclass: layout-widescreen
  required_plugins: [Dataview, Excalidraw, Canvas, Buttons, DataviewJS, Linter, StyleSettings, Admonition]
  recommended_dataview_version: ">=0.5.68"
---

# {{VALUE:entry_title?Ficha de conocimiento}}

> [!abstract] Snapshot
> **Tema**: `<topic>` · **Dominios**: `<dominios>` · **Nivel de confianza**: `<confidence>%`
>
> - Última revisión: {{DATE:YYYY-MM-DD}}
> - Estado: `<status>`
> - Guardián: `@guardian`

---

## 1. Front-matter extendido (Properties)

```yaml
aliases: [<alias1>, <alias2>]
source_primary: <fuente principal>
source_type: [paper|repo|nota]
relevance_score: <0-100>
confidence: <0-100>
impact_axes: [ambiental, social, económico]
related_canvas: {{VALUE:entry_title?Ficha de conocimiento}}.canvas
related_excalidraw: {{VALUE:entry_title?Ficha de conocimiento}}.excalidraw
```

---

## 2. Mapa cognitivo

> [!map]- Visualizaciones clave
> - Canvas :: `![[{{VALUE:entry_title?Ficha de conocimiento}}.canvas]]`
> - Excalidraw :: `![[{{VALUE:entry_title?Ficha de conocimiento}}.excalidraw]]`
> - Grafo local :: `[[=this.file.path]]`

```dataviewjs
const neighbors = dv.current().file.outlinks.concat(dv.current().file.inlinks);
const counts = {};
neighbors.forEach(link => {
  const path = link.path;
  counts[path] = (counts[path] ?? 0) + 1;
});
const rows = Object.entries(counts).map(([path, weight]) => ({
  note: dv.fileLink(path),
  weight
})).sort((a, b) => b.weight - a.weight);
dv.table(["Nota relacionada", "Peso"], rows.slice(0, 10));
```

---

## 3. Contenido nuclear

> [!summary]- TL;DR
> - Insight 1 :: <texto>
> - Insight 2 :: <texto>
> - Insight 3 :: <texto>

### Contexto ampliado

```ad-note
title: Origen del conocimiento
type: bookmark
collapse: closed
```
> - Fuente primaria: <cita>
> - Fecha de publicación: <año>
> - Licencia: <tipo>

### Detalle técnico (RAW)

```ad-example
title: Evidencia clave
collapse: open
```
> - Punto de datos A: <detalle>
> - Punto de datos B: <detalle>
> - Modelos asociados: <modelo>

```ad-info
title: Riesgos y límites
collapse: open
```
> - Riesgo 1: <detalle>
> - Riesgo 2: <detalle>
> - Gap: <detalle>

---

## 4. DO / DON'T operacional

> [!check]- DO
> - Aplicar en proyectos con <condición>
> - Mantener trazas en `WK.log`
> - Validar métricas de impacto antes de escalar

> [!failure]- DON'T
> - Usar sin validación de contexto
> - Compartir sin limpiar datos sensibles
> - Desalinear nomenclatura del glosario V5

---

## 5. Evidencias y bibliografía

```dataview
TABLE source as "Fuente", type as "Tipo", year, access, reliability
FROM ""
WHERE type = "reference" and topic = this.file.name
SORT reliability desc
```

> [!tip]- Sincronización Zotero
> ```button
> name Importar desde Zotero
> type command
> action MetaEdit: Zotero Import
> ```

```dataviewjs
const bib = dv.pages().where(p => p.collection == "bibliography" && p.topics && p.topics.includes(dv.current().file.name));
dv.list(bib.map(b => `${b.file.link} — ${b.authors ?? "s.d."} (${b.year ?? "s.f."})`));
```

---

## 6. Aprendizajes y próximos pasos

> [!note]- WK.log
> ```yaml
> wk_entry:
>   when: {{DATE:YYYY-MM-DDTHH:mm}}
>   actor: ai|human
>   connector: <GitHub/Zotero>
>   findings:
>     - <aprendizaje>
>   next:
>     - <acción>
> ```

```tasks
not done
path includes {{VALUE:entry_title?Ficha de conocimiento}}
tag includes #knowledge/todo
```

> [!todo]- Próximos pasos sugeridos
> - [ ] Validar con experto dominio `@persona`
> - [ ] Actualizar indicadores de impacto
> - [ ] Subir resumen a repositorio público

---

## 7. OutputTemplate

```yaml
OutputTemplate:
  deliverable: KnowledgeMasterRecord
  exports:
    - format: markdown
    - format: json
    - format: opml
  validation:
    - command: Dataview: Force refresh current view
    - command: Linter: Lint current file
  review:
    owner: {{VALUE:guardian?"@pending"}}
    cadence: P30D
```

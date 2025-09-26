---
asset:
  id: obsidian_master_template_kpi_dashboard
  name: OrbitSpectrumKPIDashboard
  type: dataview_dashboard
  version: 1.0.0
  owner: AingZ_Platform
  status: draft
  tags:
    - obsidian/master
    - analytics/kpi
kpi_scope: "\"\""
kpi_window_days: 14
kpi_template_tag: obsidian/master
kpi_feedback_field: first_feedback_at
---

# Orbit·Spectrum · KPI Dashboard

> [!summary] Propósito
> Consolidar las métricas clave de adopción del master template validado usando las fórmulas recomendadas en [[assets_landscape_analysis.md#7-kpi-propuestos-para-evaluar-adopción]]. Ajusta los parámetros en el frontmatter (`kpi_scope`, `kpi_window_days`, `kpi_template_tag`, `kpi_feedback_field`) según la estructura de tu vault.

---

## KPI Snapshot (últimos <%* tp.frontmatter.kpi_window_days %> días) ^kpi-dashboard-snapshot

- Ventana analizada: `<%* moment().subtract(tp.frontmatter.kpi_window_days, 'days').format('YYYY-MM-DD') %> → <%* moment().format('YYYY-MM-DD') %>`
- Alcance Dataview: `<%* tp.frontmatter.kpi_scope %>`
- Tag / identificador de instancia del template: `<%* tp.frontmatter.kpi_template_tag %>`
- Campo con el primer feedback registrado: `<%* tp.frontmatter.kpi_feedback_field %>`

---

## TemplateCoverage

> Fórmula: `#NotasTemplate / #NotasNuevas` dentro del alcance y ventana definidos.

```dataviewjs
const params = dv.current();
const windowDays = params.kpi_window_days ?? 14;
const scope = params.kpi_scope ?? "\"\"";
const templateTag = params.kpi_template_tag ?? "obsidian/master";
const now = window.moment();
const since = windowDays ? now.clone().subtract(windowDays, 'days') : null;
const sinceTs = since ? since.valueOf() : null;
const pages = dv.pages(scope);
const newNotes = pages.where(p => !sinceTs || (p.file && p.file.cday && p.file.cday.ts >= sinceTs));
const templateNotes = newNotes.where(p => {
  const tags = (p.tags ?? []).map(t => t.toString());
  const assetType = p?.asset?.type ?? "";
  const templateId = (p?.asset?.id ?? "").toString();
  return tags.includes(templateTag) || assetType === "master_template_instance" || templateId === templateTag;
});
const coverage = newNotes.length ? (templateNotes.length / newNotes.length) * 100 : null;
dv.table([
  "Notas nuevas (ventana)",
  `Notas con ${templateTag}`,
  "TemplateCoverage"
], [[
  newNotes.length,
  templateNotes.length,
  coverage !== null ? `${coverage.toFixed(1)}%` : "N/A"
]]);
```

---

## InteractionDepth

> Fórmula: `Promedio(callouts + tasks + embeds por nota)`.

```dataviewjs
const paramsID = dv.current();
const windowDaysID = paramsID.kpi_window_days ?? 14;
const scopeID = paramsID.kpi_scope ?? "\"\"";
const nowID = window.moment();
const sinceID = windowDaysID ? nowID.clone().subtract(windowDaysID, 'days') : null;
const sinceTsID = sinceID ? sinceID.valueOf() : null;
const pagesID = dv.pages(scopeID).where(p => !sinceTsID || (p.file && p.file.cday && p.file.cday.ts >= sinceTsID));
(async () => {
  const rows = [];
  for (const note of pagesID) {
    const contents = await dv.io.load(note.file.path);
    const callouts = (contents.match(/^>\s*\[!/gm) || []).length;
    const embeds = (contents.match(/!\[[^\]]*\]\([^\)]+\)|!\[\[[^\]]+\]\]/g) || []).length;
    const tasks = (note.file.tasks ?? []).length;
    const total = callouts + tasks + embeds;
    rows.push({
      note: note.file.link,
      callouts,
      tasks,
      embeds,
      total
    });
  }
  const average = rows.length ? (rows.reduce((acc, item) => acc + item.total, 0) / rows.length) : 0;
  dv.table([
    "Nota",
    "Callouts",
    "Tasks",
    "Embeds",
    "Total componentes"
  ], rows.map(r => [r.note, r.callouts, r.tasks, r.embeds, r.total]));
  dv.paragraph(`**InteractionDepth promedio:** ${average.toFixed(2)} componentes por nota.`);
})();
```

---

## SustainabilityTrace

> Fórmula: `Notas con propiedades de impacto ambiental completadas / Notas nuevas`.

```dataviewjs
const paramsST = dv.current();
const windowDaysST = paramsST.kpi_window_days ?? 14;
const scopeST = paramsST.kpi_scope ?? "\"\"";
const nowST = window.moment();
const sinceST = windowDaysST ? nowST.clone().subtract(windowDaysST, 'days') : null;
const sinceTsST = sinceST ? sinceST.valueOf() : null;
const pagesST = dv.pages(scopeST);
const newNotesST = pagesST.where(p => !sinceTsST || (p.file && p.file.cday && p.file.cday.ts >= sinceTsST));
const withImpact = newNotesST.where(p => p.impact_carbon || p.impact_water || p.impact_social || p.impact_energy);
const sustainabilityTrace = newNotesST.length ? (withImpact.length / newNotesST.length) * 100 : null;
dv.table([
  "Notas nuevas (ventana)",
  "Notas con métricas de impacto",
  "SustainabilityTrace"
], [[
  newNotesST.length,
  withImpact.length,
  sustainabilityTrace !== null ? `${sustainabilityTrace.toFixed(1)}%` : "N/A"
]]);
```

---

## FeedbackLoopTime

> Fórmula: `Promedio(date(first_feedback) - date(created))` expresado en horas. Se espera un campo ISO8601 (por defecto `first_feedback_at`).

```dataviewjs
const paramsFLT = dv.current();
const windowDaysFLT = paramsFLT.kpi_window_days ?? 14;
const scopeFLT = paramsFLT.kpi_scope ?? "\"\"";
const feedbackField = paramsFLT.kpi_feedback_field ?? "first_feedback_at";
const nowFLT = window.moment();
const sinceFLT = windowDaysFLT ? nowFLT.clone().subtract(windowDaysFLT, 'days') : null;
const sinceTsFLT = sinceFLT ? sinceFLT.valueOf() : null;
const pagesFLT = dv.pages(scopeFLT).where(p => !sinceTsFLT || (p.file && p.file.cday && p.file.cday.ts >= sinceTsFLT));
const notesWithFeedback = pagesFLT.where(p => p[feedbackField]);
const rowsFLT = [];
let totalHours = 0;
let counted = 0;
for (const note of notesWithFeedback) {
  const created = window.moment(note.file.cday ? note.file.cday.toISO() : note.file.ctime.toISO());
  const firstFeedback = window.moment(note[feedbackField]);
  if (!firstFeedback.isValid() || !created.isValid()) continue;
  const hours = firstFeedback.diff(created, 'hours', true);
  totalHours += hours;
  counted += 1;
  rowsFLT.push([note.file.link, created.format('YYYY-MM-DD HH:mm'), firstFeedback.format('YYYY-MM-DD HH:mm'), `${hours.toFixed(1)} h`]);
}
const averageHours = counted ? (totalHours / counted) : null;
dv.table([
  "Nota",
  "Creación",
  "Primer feedback",
  "Tiempo transcurrido"
], rowsFLT);
dv.paragraph(`**FeedbackLoopTime promedio:** ${averageHours !== null ? averageHours.toFixed(1) + ' h' : 'Sin registros'} (basado en ${counted} notas).`);
```

---

> [!tip] Mantén sincronizado este dashboard con el WK.log de [[obsidian_master_template_aingz_master#50 · Feedback y WK.log]] para que las métricas reflejen los ciclos de mejora continua.

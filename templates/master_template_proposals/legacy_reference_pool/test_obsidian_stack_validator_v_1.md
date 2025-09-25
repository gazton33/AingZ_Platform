---

## id: obsidian\_stack\_validator\_v1\_1 version: 1.1 created\_at: 2025-09-09T00:00:00Z scope: Desktop — Core: Bases/Canvas/Properties; Community: Buttons/Dataview/Excalidraw/Tasks/Templater/Tracker/Meta‑Bind/Modal‑Forms/QuickAdd/Linter status: test

# TEST — Obsidian Stack Validator v1.1

 objetivo: validar rápido todo el stack. Pasa si **≥95%** checks en OK.

## 0) Pre‑flight (obligatorio)




---
id: ai_sess_20250902_0000
objective: "prueba stack"
horizon: MVP
status: draft
due: 2025-09-10
coverage_pct: 10
latency_budget: 0
stakeholders: [GZ]
tags: [stack/test]
---
- [ ] Tarea demo 📅 2025-09-10
```

-

---

## 1) CORE — pruebas

### 1.1 Properties view

-

### 1.2 Bases (DB core)

-

### 1.3 Canvas

-

### 1.4 Daily notes / Search / Command palette / Quick switcher

-

### 1.5 File recovery

-

---

## 2) COMMUNITY — pruebas

### 2.1 Dataview

**Debug**

```dataview
LIST FROM "sessions"
```

-

**Tabla**

```dataview
TABLE file.link AS Nota, objective, horizon, status, due
FROM "sessions"
WHERE status != "locked"
SORT due ASC
```

-

### 2.2 Tasks

```tasks
not done
path includes sessions
sort by due
```

-

### 2.3 Buttons → Templater

```button
name Nueva sesión IA
type command
action Templater: Create new note from template
```

-

### 2.4 QuickAdd (opcional)

-

### 2.5 Meta Bind

```meta-bind-input
frontmatterKey: status
type: select
options: [draft, active, review, locked]
```

-

### 2.6 Modal Forms

```tpl
<%*
const mf = app.plugins.plugins.modalforms?.api;
if (mf) {
  const data = await mf.openForm('alta_sesion');
  if (data) await app.fileManager.processFrontMatter(tp.config.target_file, fm => Object.assign(fm, data.getData()));
}
-%>
```

-

### 2.7 Excalidraw

-

```
![[diagrams/00_INDEX.excalidraw|900]]
```

-

### 2.8 Linter

-

### 2.9 Templater

-

### 2.10 Tracker

````markdown
```tracker
searchType: frontmatter
searchTarget: coverage_pct
folder: sessions
output: line
```
````

-

---

## 3) Cross‑checks

-

## 4) Registro

- Casos totales:
- Casos OK:
- **Pass rate**:
- Bloqueos:

## 5) Cierre

-


---

file: templates/readme/README\_Universal\_Template\_v1.md code: RUTPL name: README\_Universal\_TemplateV1 version: v1.0.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: template referencias: [DTT11, BAT11, GTPL11, RST11, PIPLT, PCTRL, RMBL] triggers: [TRG\_README\_UNIVERSAL] cambios:

- 2025-08-18: Primera versión del README universal por carpeta/bucket. checks:
- Sin rutas a archivos ni anclas (#...)
- Sólo namespaces aprobados
- `links.parent` y `links.children` coherentes

---

# README Universal de Carpeta/Bucket — Plantilla

**Uso**: colocar una copia en cada carpeta del árbol. Completar metadatos, enlaces a buckets, funciones, interfaces y control de calidad. No incluir pasos operativos específicos ni rutas a archivos.

## 1) Identidad del nodo

```yaml
---
title: <Nombre del bucket>
code: <DIR_CODE>               # p.ej. ROOT, DATA, SEM
path: <ruta_relativa_logica>   # p.ej. /main/data_base/semantics
type: dir_node
level: <0..N>
aliases: [<Nombre corto>]
tags: [dir, node, baseline]
links:
  parent: DIR::<PADRE>
  children: [DIR::<H1>, DIR::<H2>]
  related: []
policies:
  no_file_refs: true
---
```

## 2) Propósito y alcance

Breve descripción (≤ 30 palabras) de la función del bucket y sus límites.

## 3) Funciones operativas

- Lista concisa de capacidades del bucket.
- Evitar detalles de implementación.

## 4) Interfaces (contratos)

- **Entradas (DIR::)**: [[DIR::]], [[DIR::]]
- **Salidas (DIR::)**: [[DIR::]], [[DIR::]]
- **Triggers (WF::)**: [[WF::]]
- **Reglas aplicables (RULESET::)**: [[RULESET::]]
- **Términos clave (GLOS::)**: [[GLOS::]]

## 5) Pipelines asociados

| PIPE\_CODE | Trigger (WF::) | Propósito | Entradas (DIR::) | Salidas (DIR::) | R/A       |
| ---------- | -------------- | --------- | ---------------- | --------------- | --------- |
| Pxx        | [[WF::]]       |           | [[DIR::]]        | [[DIR::]]       | R:  · A:  |

## 6) Métricas SLO/SLI

| Métrica    | Objetivo | Cómo se mide | Fuente       |     |         |
| ---------- | -------- | ------------ | ------------ | --- | ------- |
| \<métrica> |          | \<método>    | [[DIR::\<LOG | QMS | DATA>]] |

## 7) Gobierno y calidad (QMS)

- Validaciones: `VALD/VALG` requeridas
- Cambios: registrar en [[CHG::]]
- Excepciones aprobadas: referencia QMS

## 8) Notas y riesgos

- Riesgos conocidos y mitigaciones propuestas.

## 9) Wikilinks y crossref — reglas

- Sólo `DIR::, GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::`.
- Prohibido enlazar archivos (`*.md`, `*.py`, `*.yml`) o anclas.
- Mantener `parent`↔`children` sin ciclos.

## 10) Checklist local

-

## OutputTemplate

```yaml
output_example:
  status: README_UNIVERSAL_READY
  created_at: 2025-08-18T00:00:00-03:00
  params:
    - namespaces: [DIR::, GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::]
  result:
    - node_defined: true
    - links_consistent: true
  log:
    - step1: author
    - step2: link_dirs
    - step3: validate
```


---

file: templates/\_baselines/dir\_tree/DirTree\_Template\_Baseline\_v1\_1\_locked.md code: DTTBL name: DirTreeTemplateBaselineV1\_1 version: v1.1.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: locked referencias: [DTTPL, DTT11, BL-2025-08-18-DirTree-v1.4.2, PCTRL] triggers: [TRG\_BASELINE\_LOCK, TRG\_NEW\_TREE] cambios:

- 2025-08-18: Congelada la plantilla de árbol enlazada (wikilinks + export cobertura). checks:
- ASCII tree correcto y columnas 52/54/60
- `CODE` ≤5, únicos
- `no_file_refs: true`
- Índice de códigos completo y sin duplicados

---

# Template — Árbol de Directorios (Baseline v1.1 bloqueado)

**Objetivo**: proveer estructura mínima y estable para definir jerarquía de buckets con códigos `DIR::<CODE>`, sin enlazar archivos.

**Notas**: mantener independencia tecnológica; usar verbos funcionales; derivar cobertura a Buckets.

## Namespaces y políticas

```yaml
namespaces: { dir: "DIR::", glos: "GLOS::", ruleset: "RULESET::", wf: "WF::", tpl: "TPL::", qms: "QMS::", chg: "CHG::" }
reserved_codes: [ROOT, MAIN, RULE, PIPE]
policies: { no_file_refs: true }
```

## Árbol (plantilla)

```text
<RepositoryName>                                     [ROOT]  — <breve descripción raíz>
├── <module_or_area>                                 [M001]  — <breve descripción>
│   ├── <subarea_a>                                   [A001]  — <breve>
│   │   ├── <sub_a1>                                  [A1]    — <breve>
│   │   └── <sub_a2>                                  [A2]    — <breve>
│   └── <subarea_b>                                   [B001]  — <breve>
├── <module_or_area_2>                               [M002]  — <breve>
└── <ops_or_common>                                  [OPS]   — <scripts/ci/cd/etc>
```

> Alineación: nombre→col 52 · `[CODE]`→col 54 · descripción→col 60.

## Índice de códigos

| CODE | Ruta base relativa                 | Función breve        |
| ---- | ---------------------------------- | -------------------- |
| ROOT | /                                  | Raíz del repositorio |
| M001 | /\<module\_or\_area>               | \<función>           |
| A001 | /\<module\_or\_area>/\<subarea\_a> | \<función>           |
| A1   | ...                                | \<función>           |
| A2   | ...                                | \<función>           |
| B001 | /\<module\_or\_area>/\<subarea\_b> | \<función>           |
| M002 | /\<module\_or\_area\_2>            | \<función>           |
| OPS  | /\<ops\_or\_common>                | \<función>           |

## Wikilinks y crossref

- Página por nodo: `DIR::<CODE>`.
- Wikilink: `[[DIR::<CODE>|Nombre]]`.
- Crossref permitidos: `GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::`.

## Export para cobertura aguas abajo

```yaml
tree_export:
  codes: [ROOT, MAIN, RULE, PIPE, DB, CACT, DOCS, DATA, SEM, AILE, DEVP, OTPL, GUID, WF, KCTX, CDEV, CARC, LOG, GIT, PKG, SCRIP]
  contract: "Cada CODE debe existir en Buckets/Assets/Entidades"
```

## Checklist

-

## OutputTemplate

```yaml
output_example:
  status: TREE_TEMPLATE_BASELINE_LOCKED
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - export_codes: 20
    - codes_policy: { max_len: 5, unique: true }
  log:
    - step1: author
    - step2: align
    - step3: validate
    - step4: freeze
```


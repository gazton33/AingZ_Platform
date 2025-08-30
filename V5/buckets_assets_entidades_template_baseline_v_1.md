---

file: templates/\_baselines/buckets/Buckets\_Assets\_Entidades\_Template\_Baseline\_v1\_1\_locked.md code: BATBL name: BucketsAssetsEntidadesTemplateBaselineV1\_1 version: v1.1.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: locked referencias: [BATPL, BAT11, DTT11, BL-2025-08-18-DirTree-v1.4.2, PCTRL] triggers: [TRG\_BASELINE\_LOCK, TRG\_NEW\_BUCKETS\_MAP] cambios:

- 2025-08-18: Congelada la plantilla con cobertura, router y catálogo de roles. checks:
- coverage\_pct == 100
- `file_links_detected == 0`
- tipos ∈ {bucket, asset, entity}

---

# Template — Buckets / Assets / Entidades (Baseline v1.1 bloqueado)

**Objetivo**: mapear 100% de `tree_export.codes` a funciones operativas, entradas/salidas y R/A, sin enlazar archivos.

**Notas**: usar sólo `DIR::` en wikilinks; roles desde catálogo; crossref a `GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::`.

## Cobertura del Dir Tree

```yaml
coverage:
  source: tree_export.codes   # exportado por DirTree
  required: 100
```

## Catálogo de roles R/A

```yaml
roles_catalog:
  architect: Arch
  core_dev_lead: Core Dev Lead
  devops: DevOps
  qms: QMS
  platform_ops: Platform-Ops
  ontology_lead: Ontology Lead
```

## 1) Tabla maestra (rellenar)

| CODE | Nodo (wikilink) | Tipo | Función operativa | Entradas | Salidas | R (owner) / A (aprob) | Calidad/QMS |   |                                                     |           |
| ---- | --------------- | ---- | ----------------- | -------- | ------- | --------------------- | ----------- | - | --------------------------------------------------- | --------- |
|      | [[DIR::         | ]]   | \<bucket          | asset    | entity> | \<función>            |             |   | R: \<roles\_catalog.key> · A: \<roles\_catalog.key> | [[QMS::]] |

## 2) RULESET — Router declarativo (plantilla)

```yaml
ruleset_router:
  targets:
    platform: [[DIR::RULE]]
    app:      [[DIR::RULE]]
    api:      [[DIR::RULE]]
  routes: []
```

## 3) PIPE — Registro de orquestación (plantilla)

| PIPE\_CODE | Nodo DIR      | Propósito    | Triggers (WF::) | Inputs (DIR::) | Outputs (DIR::) | R/A       |
| ---------- | ------------- | ------------ | --------------- | -------------- | --------------- | --------- |
| P01        | [[DIR::PIPE]] | \<propósito> | [[WF::]]        | [[DIR::]]      | [[DIR::]]       | R:  · A:  |

## Reglas

1. Sólo `DIR::<CODE>` en enlaces.
2. `coverage_pct` debe ser 100.
3. R/A desde `roles_catalog`.

## Checklist

-

## OutputTemplate

```yaml
output_example:
  status: BUCKETS_TEMPLATE_BASELINE_LOCKED
  created_at: 2025-08-18T00:00:00-03:00
  params:
    - coverage_required: 100
  result:
    - sections: [master, ruleset_router, pipe_registry]
  log:
    - step1: author
    - step2: xref_wire
    - step3: validate
    - step4: freeze
```


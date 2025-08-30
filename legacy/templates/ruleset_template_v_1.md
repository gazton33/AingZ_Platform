---

file: templates/ruleset/Ruleset\_Template\_v1\_1\_router.md code: RST11 name: RulesetTemplateV1\_1Router version: v1.1.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: template referencias: [DTT11, BAT11, GTPL11, PIPLT] triggers: [TRG\_RULESET\_ROUTER] cambios:

- 2025-08-18: Versión refinada con políticas anti‑archivo y router vacío. checks:
- goto sólo `DIR::`
- Sin rutas de archivo ni anclas
- `routes` cubre {global, platform, app, api} cuando se complete

---

# Ruleset — Plantilla v1.1 (router)

**Rol**: router normativo. Sin instrucciones operativas. Sólo deriva a buckets.

## Políticas

```yaml
policies: { no_file_refs: true }
namespaces: { dir: "DIR::", ruleset: "RULESET::", wf: "WF::", qms: "QMS::" }
```

## Router (completar)

```yaml
ruleset_router:
  targets:
    global:   [[DIR::RULE]]
    platform: [[DIR::RULE]]
    app:      [[DIR::RULE]]
    api:      [[DIR::RULE]]
  routes: []   # agregar items {match: {kind, name}, goto: [[DIR::RULE]], section: <hint>}
```

## Secciones sugeridas

- Global · Platform · App · API (todas bajo [[DIR::RULE]]).

## Checklist

-

## OutputTemplate

```yaml
output_example:
  status: RULESET_TEMPLATE_READY
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - targets: [global, platform, app, api]
    - routes_defined: <n>
  log:
    - step1: author
    - step2: define_routes
    - step3: validate
```


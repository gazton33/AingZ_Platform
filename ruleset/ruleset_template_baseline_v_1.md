---

file: ruleset/ruleset_template_baseline_v_1.md code: RSTBL name: RulesetTemplateBaselineV1_1 version: v1.1.0 date: 2025-08-18 owner: AingZ_Platform · RwB status: locked referencias: [RST11, DTT11, BAT11, PIPLT, PCTRL] triggers: [TRG_BASELINE_LOCK, TRG_RULESET_ROUTER] cambios:

- 2025-08-18: Congelada la plantilla de router de Ruleset. checks:
- goto sólo `DIR::`
- Sin rutas de archivo ni anclas
- Namespaces válidos

---

# Ruleset — Plantilla (Baseline v1.1 bloqueado)

**Objetivo**: centralizar reglas y enrutar a secciones bajo `[[DIR::RULE]]`.

**Notas**: Ruleset no ejecuta. Sólo define políticas y rutas.

## Políticas

```yaml
policies: { no_file_refs: true }
namespaces: { dir: "DIR::", ruleset: "RULESET::", wf: "WF::", qms: "QMS::" }
```

## Router (plantilla)

```yaml
ruleset_router:
  targets: { global: [[DIR::RULE]], platform: [[DIR::RULE]], app: [[DIR::RULE]], api: [[DIR::RULE]] }
  routes: []
```

## Secciones sugeridas

- Global · Platform · App · API (todas bajo [[DIR::RULE]]).

## Checklist

-

## OutputTemplate

```yaml
output_example:
  status: RULESET_TEMPLATE_BASELINE_LOCKED
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - targets: [global, platform, app, api]
  log:
    - step1: author
    - step2: validate
    - step3: freeze
```


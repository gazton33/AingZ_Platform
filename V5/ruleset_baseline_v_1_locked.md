---

file: core/doc/workbench/AINGZ\_V5\_Ruleset\_Baseline\_v1\_locked.md code: RBL name: RulesetBaselineV1 version: v1.0.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: locked referencias:

- RREAL (RulesetRealV1)
- RSTBL (Ruleset\_Template\_Baseline\_v1.1\_Locked)
- DTTBL (DirTree\_Template\_Baseline\_v1.1\_Locked)
- PIPLT (Pipelines\_Template\_v1)
- PCTRL (PlatformControlPrinciplesV1) triggers: [TRG\_BASELINE\_LOCK, TRG\_RULESET\_ROUTER] cambios:
- 2025-08-18: Baseline real del ruleset bloqueado según template. checks:
- goto sólo `DIR::`
- Sin rutas de archivo ni anclas
- Namespaces válidos

---

# Baseline Lock — Ruleset v1.0.0

**Baseline-ID**: BL-2025-08-18-Ruleset-v1.0.0\
**Árbol**: BL-2025-08-18-DirTree-v1.4.2\
**Snapshot**: `AINGZ_V5_Ruleset_Real_v1.md` validado 2025-08-18

> Estado congelado. Ediciones futuras en *working copy* de Ruleset y nuevo lock.

## Router (snapshot)

```yaml
ruleset_router:
  targets:
    global:   [[DIR::RULE]]
    platform: [[DIR::RULE]]
    app:      [[DIR::RULE]]
    api:      [[DIR::RULE]]
  routes:
    - match: { kind: platform, name: aws }
      goto: [[DIR::RULE]]
      section: platform/aws
    - match: { kind: platform, name: gcp }
      goto: [[DIR::RULE]]
      section: platform/gcp
    - match: { kind: platform, name: azure }
      goto: [[DIR::RULE]]
      section: platform/azure
    - match: { kind: platform, name: local }
      goto: [[DIR::RULE]]
      section: platform/local
    - match: { kind: app, name: console }
      goto: [[DIR::RULE]]
      section: app/console
    - match: { kind: app, name: etl }
      goto: [[DIR::RULE]]
      section: app/etl
    - match: { kind: app, name: ui }
      goto: [[DIR::RULE]]
      section: app/ui
    - match: { kind: api, name: rest }
      goto: [[DIR::RULE]]
      section: api/rest
    - match: { kind: api, name: graphql }
      goto: [[DIR::RULE]]
      section: api/graphql
    - match: { kind: api, name: sdk }
      goto: [[DIR::RULE]]
      section: api/sdk
```

## Normas globales (snapshot)

- Anti‑archivo activa.
- Namespaces aprobados.
- Roles R/A desde QMS.
- ADR para cambios con impacto.

## Integración PIPE

- Rutas válidas habilitan ejecución en [[DIR::PIPE]].

## Checklist

-

## OutputTemplate

```yaml
output_example:
  status: RULESET_BASELINE_LOCKED
  baseline_id: BL-2025-08-18-Ruleset-v1.0.0
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - files_frozen: [core/doc/workbench/AINGZ_V5_Ruleset_Baseline_v1_locked.md]
  log:
    - step1: qa_pass
    - step2: checkpoint
    - step3: freeze
```


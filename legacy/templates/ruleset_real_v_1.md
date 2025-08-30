---

file: core/doc/workbench/AINGZ\_V5\_Ruleset\_Real\_v1.md code: RREAL name: RulesetRealV1 version: v1.0.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: draft (real) referencias:

- BL-2025-08-18-DirTree-v1.4.2
- BL-2025-08-18-BucketsMap-v1.0.0
- DTT11 (DirTreeGenericTemplateV1\_1Linked)
- BAT11 (BucketsAssetsEntidadesTemplateV1\_1Router)
- RSTPL (Ruleset\_Router\_Template\_v1)
- PCTRL (PlatformControlPrinciplesV1)
- GTPL11 (Glossary\_Template\_v1\_1\_linked)
- PIPLT (Pipelines\_Template\_v1) triggers: [TRG\_RULESET\_REAL, TRG\_ROUTER] cambios:
- 2025-08-18: Primera versión real con router y secciones global/platform/app/api. checks:
- goto sólo a `DIR::` (sin rutas a archivos)
- política `no_file_refs: true`
- rutas cubren plataformas/apps/apis declaradas

---

# Ruleset — Real v1

**Rol**: router normativo. Centraliza reglas y deriva a secciones aplicables. Enlaces sólo a buckets `DIR::`. Sin archivos.

## 1) Entrypoint

- **README main** → delega a **Ruleset**: [[DIR::RULE|Ruleset]]
- **Ruleset** → deriva a sección aplicable bajo [[DIR::RULE]].
- **PIPE** [[DIR::PIPE]] ejecuta orquestaciones según reglas activas.

## 2) Router declarativo (real)

```yaml
ruleset_router:
  targets:
    global:   [[DIR::RULE]]   # políticas transversales
    platform: [[DIR::RULE]]   # reglas por plataforma
    app:      [[DIR::RULE]]   # reglas por aplicación
    api:      [[DIR::RULE]]   # contratos de API
  routes:
    # Plataformas soportadas
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

    # Aplicaciones internas
    - match: { kind: app, name: console }
      goto: [[DIR::RULE]]
      section: app/console
    - match: { kind: app, name: etl }
      goto: [[DIR::RULE]]
      section: app/etl
    - match: { kind: app, name: ui }
      goto: [[DIR::RULE]]
      section: app/ui

    # Tipos de API
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

> `section` es informativa y no es un link a archivo. Indica sub‑sección lógica dentro del bucket [[DIR::RULE]].

## 3) Sección Global (normas transversales)

- **Anti‑archivo**: prohibido enlazar `*.md`, `*.py`, `*.yml`, anclas `#...`.
- **Namespaces válidos**: `DIR::, GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::`.
- **Roles R/A**: usar catálogo de QMS. Registrar excepciones en `CHG::`.
- **ADR**: cambios con impacto → ADR‑0001+ en [[DIR::CARC]].

## 4) Sección Platform (ejemplos de reglas)

- **aws**: cifrado en reposo y tránsito, tagging obligatorio, límites de costo.
- **gcp**: VPC Service Controls para datos sensibles, CMEK requerido.
- **azure**: Azure Policy para conformidad, RBAC mínimo necesario.
- **local**: secretos fuera del repo, backups verificados.

## 5) Sección App (ejemplos de reglas)

- **console**: autenticación SSO, auditoría de comandos.
- **etl**: idempotencia en jobs, catálogos en [[DIR::DATA]].
- **ui**: accesibilidad AA, telemetría sin PII.

## 6) Sección API (contratos)

- **rest**: versionado semántico, límites y *retry‑after* definidos.
- **graphql**: esquemas *typed*, *persisted queries* para producción.
- **sdk**: soporte mínimo para 3 runtimes, *deprecation policy* clara.

## 7) Integración con Pipelines

- Las reglas activas habilitan rutas de ejecución en [[DIR::PIPE]].
- Triggers `WF::` definidos en PIPLT disparan pipelines con entradas/salidas `DIR::`.

## 8) Validación y QMS

- `VALD` valida conformidad de reglas declaradas.
- `VALG` valida su aplicación en ejecuciones.
- `CHG` registra excepciones y desvíos aprobados.

## 9) Checklist

-

## OutputTemplate

```yaml
output_example:
  status: RULESET_REAL_READY
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - router_defined: true
    - kinds: [global, platform, app, api]
    - file_refs_detected: 0
  log:
    - step1: author
    - step2: routes_fill
    - step3: validate
```


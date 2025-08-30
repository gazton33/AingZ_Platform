---

file: core/doc/workbench/AINGZ\_V5\_Platform\_Control\_Principles\_v1.md code: PCTRL name: PlatformControlPrinciplesV1 version: v1.0.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: draft referencias:

- BL-2025-08-18-DirTree-v1.4.2
- BL-2025-08-18-BucketsMap-v1.0.0
- DTTPL (DirTree\_Generic\_Template\_v1)
- DTT11 (DirTree\_Generic\_Template\_v1\_1\_linked)
- BATPL (Buckets\_Assets\_Entidades\_Template\_v1)
- BAT11 (Buckets\_Assets\_Entidades\_Template\_v1\_1\_router)
- RMTPL (README\_Main\_Template\_v1)
- RSTPL (Ruleset\_Router\_Template\_v1)
- GTPL (Glossary\_Template\_v1)
- PIPLT (Pipelines\_Template\_v1) triggers: [TRG\_PLATFORM\_CTRL] cambios:
- 2025-08-18: Creación del marco de control y operación. checks:
- Sin referencias a archivos concretos
- Sólo namespaces aprobados

---

# Principios de control de la plataforma

## 1) Flujo de control (router)

- **README main** `[[DIR::MAIN]]` → delega a **Ruleset** `[[DIR::RULE]]`.
- **Ruleset (router)** resuelve destino por `kind/name` y redirige a la sección aplicable (bucket bajo `DIR::RULE`).
- **PIPE** `[[DIR::PIPE]]` orquesta la ejecución con triggers `WF::` y entradas/salidas en buckets `DIR::`.

## 2) Política anti‑archivo

- Prohibido enlazar a `*.md`, `*.py`, `*.yml` o anclas `#...`.
- Sólo `[[DIR::<CODE>|Alias]]` y prefijos: `DIR::, GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::`.

## 3) Namespaces

```yaml
namespaces: { dir: "DIR::", glos: "GLOS::", ruleset: "RULESET::", wf: "WF::", tpl: "TPL::", qms: "QMS::", chg: "CHG::" }
```

## 4) Jerarquía y cobertura

- Fuente de verdad de códigos: **DirTree Template** (`tree_export.codes`).
- **Buckets Template** debe cubrir 100% de `codes` (coverage=100).
- Cambios estructurales requieren versión nueva y ADR.

## 5) Gobierno de cambios

- **Baselines** quedan `locked`. Ediciones sólo vía *working copy* + `VersionReview` + `BaselineLock`.
- **ADR‑0001+** registra decisiones y efectos.
- **QMS** valida: `VALD/VALG` y registra `CHG`.

## 6) Pipelines (hub)

- Registro en `PIPLT`. Campos mínimos: `PIPE_CODE`, `Trigger WF::`, `Entradas DIR::`, `Salidas DIR::`, `R/A`.
- `PIPE` no guarda lógica de negocio; sólo orquesta buckets.

## 7) KPIs iniciales

- **Coverage** Buckets vs DirTree ≥ 100%.
- **Broken links** (wikilinks/crossref) = 0.
- **Tiempo de lock** ≤ 1 día hábil por cambio mayor.

## OutputTemplate

```yaml
output_example:
  status: PLATFORM_CTRL_READY
  created_at: 2025-08-18T00:00:00-03:00
  params:
    - namespaces: [DIR::, GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::]
    - coverage_required: 100
  result:
    - router_chain: [README->RULESET->PIPE]
    - anti_file_refs: true
  log:
    - step1: author
    - step2: validate
```


---
file: core/doc/workbench/AINGZ_V5_Context_Package_NewThread_v1.md
code: CTXPKG
name: ContextPackageNewThreadV1
version: v1.0.0
date: 2025-08-18
owner: AingZ_Platform · RwB
status: handoff
referencias:
  - ARBBL (DirTreeV14BaselineLocked)
  - BAMBL (BucketsAssetsEntidadesBaselineV1)
  - GBL (GlossaryBaselineV1)
  - RBL (RulesetBaselineV1)
  - RMBL2 (README_Main_BaselineV1)
  - DTTBL (DirTreeTemplateBaselineV1_1)
  - BATBL (BucketsAssetsEntidadesTemplateBaselineV1_1)
  - GTBL (GlossaryTemplateBaselineV1_1)
  - RSTBL (RulesetTemplateBaselineV1_1)
  - RMBL (README_Main_Template_BaselineV1)
  - RUTPL (README_Universal_TemplateV1)
  - PCTRL (PlatformControlPrinciplesV1)
triggers: [TRG_CONTEXT_PACKAGE]
cambios:
  - 2025-08-18: Paquete de contexto para continuar en hilo nuevo.
checks:
  - Sin enlaces a archivos en el cuerpo
  - Sólo namespaces aprobados cuando se usen wikilinks
---

# Context Package — Nuevo hilo

**Objetivo**: transportar el estado mínimo completo para reanudar trabajo en un hilo nuevo y mantener coherencia de referencias.

## 0) Resumen
- **Cadena router**: README → RULESET → PIPE (ver PCTRL).
- **Política**: anti‑archivo activa; sólo `DIR::, GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::`.
- **Fuente de verdad de códigos**: DirTree baseline (ARBBL). Cobertura en Buckets baseline (BAMBL).

## 1) Artefactos congelados (baselines reales)
| Alias | Artefacto | Código | Versión | Estado |
|---|---|---|---|---|
| 1 | Árbol de Directorios | ARBBL | v1.4.2 | locked |
| 2 | Buckets/Assets/Entidades | BAMBL | v1.0.0 | locked |
| 3 | Glosario | GBL | v1.0.0 | locked |
| 4 | Ruleset | RBL | v1.0.0 | locked |
| 5 | README Main | RMBL2 | v1.0.0 | locked |

## 2) Plantillas baseline (bloqueadas)
| Alias | Plantilla | Código | Versión | Estado |
|---|---|---|---|---|
| A | DirTree Template | DTTBL | v1.1.0 | locked |
| B | Buckets/Assets Template | BATBL | v1.1.0 | locked |
| C | Glossary Template | GTBL | v1.1.0 | locked |
| D | Ruleset Template | RSTBL | v1.1.0 | locked |
| E | README Main Template | RMBL | v1.0.0 | locked |

> Nota: README Universal Template (RUTPL) listo para replicación por carpeta.

## 3) Namespaces
```yaml
namespaces: { dir: "DIR::", glos: "GLOS::", ruleset: "RULESET::", wf: "WF::", tpl: "TPL::", qms: "QMS::", chg: "CHG::" }
```

## 4) Contratos clave
- `ARBBL.tree_export.codes` define el universo de `DIR::<CODE>`.
- `BATBL.coverage.required = 100` obliga mapeo total en BAMBL.
- `RSTBL.ruleset_router` centraliza derivación a [[DIR::RULE]].
- `RMBL` asegura que README delega y no tiene pasos operativos.

## 5) Próximos pasos sugeridos al reanudar
1. Verificar **coverage** Buckets vs DirTree = 100%.
2. Replicar **README Universal** (RUTPL) en buckets críticos.
3. Completar rutas en **Ruleset Real** y registrar ADR si impacta.
4. Completar **Pipelines** y triggers `WF::` con entradas/salidas `DIR::`.
5. Ejecutar **Checklist** en cada baseline y registrar `CHG` si aplica.

## 6) Indicadores
- Broken links = 0; coverage = 100; tiempo de lock ≤ 1 día hábil.

## 7) Cómo reanudar
- Abrir hilo nuevo e iniciar con el **Seed Prompt** de `SEED1`.

## OutputTemplate
```yaml
output_example:
  status: CONTEXT_PACKAGE_READY
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - baselines: [ARBBL, BAMBL, GBL, RBL, RMBL2]
    - templates: [DTTBL, BATBL, GTBL, RSTBL, RMBL]
    - seed: SEED1
  log:
    - step1: author
    - step2: consolidate
    - step3: validate
```


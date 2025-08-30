---
file: README.md
code: RDMN
name: ReadmeMain
version: v5.0.0
date: 2025-08-24
owner: AingZ_Platform · RwB
status: locked
referencias: [RMTPL, DTT11, RST11, PIPLT, PCTRL]
triggers: [TRG_BASELINE_LOCK, TRG_README_ENTRY]
cambios:
- 2025-08-24: Alineación con plantilla bloqueada.
checks:
- Sin instrucciones operativas
- Enlaces sólo a `DIR::`
---

# README — Entrypoint (Template Baseline v1 bloqueado)

**Objetivo**: actuar como landing y derivar a Ruleset y Pipelines.

**Notas**: documento minimalista; no describe pasos; garantiza cadena router.

## Navegación

- Reglas y políticas → [[DIR::RULE|Ruleset]]
- Orquestación y ejecución → [[DIR::PIPE|Pipelines]]
- Árbol del monorepo → [[DIR::ROOT|Monorepo]]

## Garantías

```yaml
no_instructions_here: true
links_only_to_buckets: true
router_chain: [README->RULESET->PIPE]
```

## Checklist

-

## OutputTemplate

```yaml
output_example:
  status: README_TEMPLATE_BASELINE_LOCKED
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - delegates_to: [DIR::RULE, DIR::PIPE]
  log:
    - step1: author
    - step2: validate
    - step3: freeze
```

---

file: templates/\_baselines/readme/README\_Main\_Template\_Baseline\_v1\_locked.md code: RMBL name: README\_Main\_Template\_BaselineV1 version: v1.0.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: locked referencias: [RMTPL, DTT11, RST11, PIPLT, PCTRL] triggers: [TRG\_BASELINE\_LOCK, TRG\_README\_ENTRY] cambios:

- 2025-08-18: Congelada la plantilla de README de entrada. checks:
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


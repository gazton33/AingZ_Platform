---

file: core/doc/workbench/AINGZ\_V5\_README\_Main\_Real\_v1.md code: RMREAL name: README\_Main\_Real\_V1 version: v1.0.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: draft (real) referencias: [BL-2025-08-18-DirTree-v1.4.2, RMTPL, RST11, PIPLT, PCTRL] triggers: [TRG\_README\_ENTRY] cambios:

- 2025-08-18: Entrypoint real declarativo hacia Ruleset y Pipelines. checks:
- No contiene instrucciones operativas
- Enlaces sólo a buckets `DIR::`

---

# README — Entrypoint de la Plataforma (real v1)

**Rol**: landing único. Deriva a `Ruleset` y `Pipelines`. Sin pasos operativos.

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

## OutputTemplate

```yaml
output_example:
  status: README_REAL_READY
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - delegates_to: [DIR::RULE, DIR::PIPE]
  log:
    - step1: author
    - step2: validate_links
```


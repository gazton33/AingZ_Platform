---

file: core/doc/workbench/AINGZ\_V5\_README\_Main\_Baseline\_v1\_locked.md code: RMBL2 name: README\_Main\_BaselineV1 version: v1.0.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: locked referencias:

- RMREAL (README\_Main\_Real\_V1)
- RMBL (README\_Main\_Template\_Baseline\_v1\_Locked)
- DTTBL (DirTree\_Template\_Baseline\_v1.1\_Locked)
- RSTBL (Ruleset\_Template\_Baseline\_v1.1\_Locked)
- PIPLT (Pipelines\_Template\_v1)
- PCTRL (PlatformControlPrinciplesV1) triggers: [TRG\_BASELINE\_LOCK, TRG\_README\_ENTRY] cambios:
- 2025-08-18: Baseline real del README principal bloqueado según template. checks:
- Sin instrucciones operativas
- Enlaces sólo a `DIR::`

---

# Baseline Lock — README Main v1.0.0

**Baseline-ID**: BL-2025-08-18-README-v1.0.0\
**Árbol**: BL-2025-08-18-DirTree-v1.4.2\
**Snapshot**: `AINGZ_V5_README_Main_Real_v1.md` validado 2025-08-18

> Estado congelado. Ediciones futuras en *working copy* del README y nuevo lock.

## Navegación (snapshot)

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
  status: README_BASELINE_LOCKED
  baseline_id: BL-2025-08-18-README-v1.0.0
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - files_frozen: [core/doc/workbench/AINGZ_V5_README_Main_Baseline_v1_locked.md]
  log:
    - step1: qa_pass
    - step2: checkpoint
    - step3: freeze
```


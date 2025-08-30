---
file: core/doc/workbench/AINGZ_V5_Baselines_Unificados_v1_4_1_locked.md
code: A5BUBL
name: AINGZ_V5_Baselines_Unificados
version: v1.4.1
date: 2025-08-19
owner: AingZ_Platform · RwB
status: locked
referencias:
  - DirTreeV14BaselineLocked
  - GlossaryBaselineV1
  - RulesetBaselineV1
triggers: [TRG_BASELINE_LOCK]
cambios:
  - 2025-08-19: Unificación de baselines congelados.
checks:
  - Rutas apuntan a main/data_base
---

# Baselines Unificados — v1.4.1

**Baseline-ID**: BL-2025-08-19-Baselines-v1.4.1  
**DirTree**: `main/data_base/dir_tree_v_1_4_baseline_locked.md`  
**Glosario**: `main/data_base/glossary_baseline_v_1_locked.md`  
**Ruleset**: `ruleset/ruleset_baseline_v_1_locked.md`

> Artefacto congelado que referencia los baselines finales del repositorio. Cualquier modificación requiere nueva revisión y lock.

## Referencias

- [DirTree v1.4.2](../../../main/data_base/dir_tree_v_1_4_baseline_locked.md)
- [Glosario v1.0.0](../../../main/data_base/glossary_baseline_v_1_locked.md)
- [Ruleset v1.0.0](../../../ruleset/ruleset_baseline_v_1_locked.md)

## OutputTemplate

```yaml
output_example:
  status: BASELINES_UNIFIED_LOCKED
  baseline_id: BL-2025-08-19-Baselines-v1.4.1
  created_at: 2025-08-19T00:00:00-03:00
  result:
    dir_tree: main/data_base/dir_tree_v_1_4_baseline_locked.md
    glossary: main/data_base/glossary_baseline_v_1_locked.md
    ruleset: ruleset/ruleset_baseline_v_1_locked.md
  log:
    - step1: qa_pass
    - step2: checkpoint
    - step3: freeze
```

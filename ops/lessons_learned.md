---
CODE: DOC
ID: lessons_learned_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/ops/lessons_learned.md
CROSSREF:
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# Lessons Learned

Example entry format:
- 2024-01-01 | path/to/file.md | Brief description of lesson

---

- Updated crossref in README.md: rw_b_blueprint_v_4_extendido_2025_08_06.md -> lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
- Updated crossref in README.md: rw_b_master_plan_v_4_extendido_2025_08_06.md -> lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
- Updated crossref in ops/ops_readme_v_3_1.md: rw_b_blueprint_v_4_extendido_2025_08_06.md -> lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
- Updated crossref in ops/ops_readme_v_3_1.md: rw_b_master_plan_v_4_extendido_2025_08_06.md -> lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
- Updated crossref in ops/scripts/ops_scripts_readme_v_3_1.md: rw_b_blueprint_v_4_extendido_2025_08_06.md -> lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
- Updated crossref in ops/scripts/ops_scripts_readme_v_3_1.md: rw_b_master_plan_v_4_extendido_2025_08_06.md -> lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
- Updated crossref in ops/log/ops_log_readme_v_3_1.md: rw_b_blueprint_v_4_extendido_2025_08_06.md -> lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
- Updated crossref in ops/log/ops_log_readme_v_3_1.md: rw_b_master_plan_v_4_extendido_2025_08_06.md -> lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
- Updated crossref in README.md: RULE_CODING_COMPLIANCE_V4.md -> core/rulset/RULE_CODING_COMPLIANCE_V4.md
- 2025-08-08 | README.md | TRG_AUDIT_TL failed: [Errno 2] No such file or directory: 'TRG_AUDIT_TL'
- 2025-08-08 | README.md | TRG_CONSOLIDATE_TL failed: [Errno 2] No such file or directory: 'TRG_CONSOLIDATE_TL'
- 2025-08-08 | README.md | TRG_LSWP failed: [Errno 2] No such file or directory: 'TRG_LSWP'
- 2025-08-08 | README.md | TRG_AUDIT_TL failed: [Errno 2] No such file or directory: 'TRG_AUDIT_TL'
- 2025-08-08 | README.md | TRG_CONSOLIDATE_TL failed: [Errno 2] No such file or directory: 'TRG_CONSOLIDATE_TL'
- 2025-08-08 | README.md | TRG_LSWP failed: [Errno 2] No such file or directory: 'TRG_LSWP'
- 2025-08-08 | README.md | Updated crossref: crossref_blueprint: (DETECTAR Y ACTUALIZAR RUTA REAL) -> crossref_blueprint: lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
- 2025-08-08 | README.md | Updated crossref: crossref_masterplan: (DETECTAR Y ACTUALIZAR RUTA REAL) -> crossref_masterplan: lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
- 2025-08-08 | README.md | Updated crossref: crossref_prompt_codex: (DETECTAR Y ACTUALIZAR RUTA REAL) -> crossref_prompt_codex: null
- 2025-08-08 | README.md | TRG_AUDIT_TL failed: [Errno 2] No such file or directory: 'TRG_AUDIT_TL'
- 2025-08-08 | README.md | TRG_CONSOLIDATE_TL failed: [Errno 2] No such file or directory: 'TRG_CONSOLIDATE_TL'
- 2025-08-08 | README.md | TRG_LSWP failed: [Errno 2] No such file or directory: 'TRG_LSWP'
- 2025-08-08 | README.md | Updated crossref: Prompt_Codex_Baseline_V4_Check.md -> lifecycle/temp/prompt_codex_baseline_v_4_check.md
- 2025-08-08 | README.md | Updated crossref: crossref_prompt_codex: null -> crossref_prompt_codex: lifecycle/temp/prompt_codex_baseline_v_4_check.md
- 2025-08-08 | ops/scripts/litw_sweep.py | Handling missing blueprint files prevents sweep failure
- 2025-08-08 | ops/validate_metadata.py | Repository READMEs lack required metadata and OutputTemplate sections

- 2025-08-08 | .github/workflows/* | All workflows require GH_TOKEN_RW_B_CI for authenticated checkout and scripts
- 2025-08-08 | ops/__init__.py | Missing __init__ files prevent package imports
- 2025-08-08 | core/platform_v_4_0.py | Simple stubs unblock platform tests
- 2025-08-08 | ops/scripts/diagnose_baseline.py | Baseline path fallback ensures report generation
- 2025-08-08 | ops/baseline.csv | Include config files to exercise all categories
- 2025-08-08 | ops/paths_cache.json | Cache must include core V4 documents for crossref scripts
- 2025-08-08 | pln_primeros_pasos_codex_crossref_update_v_4_20250807.md | Always start plans with YAML front matter and OutputTemplate
- 2025-08-08 | ops/scripts/diagnose_baseline.py | Added json config support and default category sections to satisfy tests
- 2025-08-08 | ops/scripts/litw_sweep.py | Regular sweeps confirm cache completeness
- 2025-08-08 | ops/validate_metadata.py | Valid metadata blocks prevent crossref drift

- 2025-08-08 | pln_primeros_pasos_codex_crossref_update_v_4_20250807.md | Temporary plan removed after crossref validation
- 2025-08-08 | repo | Centralizing changelog and lessons_learned under ops simplifies maintenance of dynamic crossrefs
- 2025-08-10 | library/intg/readme_library_intg_rw_b_v_3_1.md | Documentar integraciones asegura trazabilidad y metadatos uniformes

- 2025-08-10 | ops/log/purge/readme_ops_log_purge_v_4.md | Documented retention policy and workflow linkage

## OutputTemplate
```yaml
CODE:
ID:
VERSION:
ROUTE:
CROSSREF:
AUTHOR:
DATE:
```
- 2025-08-10 | README.md | TRG_AUDIT_TL failed: [Errno 2] No such file or directory: 'TRG_AUDIT_TL'
- 2025-08-10 | README.md | TRG_CONSOLIDATE_TL failed: [Errno 2] No such file or directory: 'TRG_CONSOLIDATE_TL'
- 2025-08-10 | README.md | TRG_LSWP failed: [Errno 2] No such file or directory: 'TRG_LSWP'
- 2025-08-10 | README.md | Updated crossref: crossref_prompt_codex: lifecycle/temp/prompt_codex_baseline_v_4_check.md -> crossref_prompt_codex: null

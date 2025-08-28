---
CODE: OPS
ID: readme_ops_log_purge_v_4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/ops/log/purge/readme_ops_log_purge_v_4.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
  - .github/workflows/aingz_purge_fixes_v2.yml
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# Purge Logs Subbucket

## Objetivo
Repositorio específico para los registros de purga automática y manual dentro de `ops/log`. Sirve como bitácora de las tareas de limpieza ejecutadas sobre los buckets de logs.

## Política de Retención
Los registros se conservan por un máximo de 30 días. Pasado ese período se eliminan automáticamente mediante el workflow `aingz_purge_fixes_v2.yml`.

## Workflows Relacionados
- Workflow de purga: [`.github/workflows/aingz_purge_fixes_v2.yml`](../../../.github/workflows/aingz_purge_fixes_v2.yml)

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

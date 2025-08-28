---
CODE: OPS
ID: bootstrap_v_4_readme_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/ops/bootstrap_v_4_readme.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# Bootstrap V4 — Instrucciones rápidas

## Copiar archivos
Coloca estos archivos en la **raíz** del repo local, respetando las rutas:
- .github/workflows/aingz_agent_pr.yml
- .github/workflows/ci_audit.yml
- core/rulset/RULE_CODING_COMPLIANCE_V4.md
- ops/templates/template_readme_rw_b_v_4.md
- ops/hooks/pre-commit
- ops/paths_cache.json

## Commit con GitHub Desktop
1) Verás los cambios en la lista.
2) Rama: **main** (como acordamos).
3) Mensaje: `Bootstrap V4: workflows, ruleset, hooks, template`.
4) Pulsa **Commit to main** y luego **Push origin**.

## Ejecutar el workflow del Agent
En GitHub (web) → **Actions → AingZ Agent PR → Run workflow**. Razón sugerida: `bootstrap`.

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

# Bootstrap V4 — Instrucciones rápidas

## Copiar archivos
Coloca estos archivos en la **raíz** del repo local, respetando las rutas:
- .github/workflows/aingz_agent_pr.yml
- .github/workflows/ci_audit.yml
- core/rulset/RULE_CODING_COMPLIANCE_V4.md
- ops/templates/template_readme_rw_b_v_4.md
- ops/hooks/pre-commit
- ops/hooks/pre-push
- ops/paths_cache.json

## Commit con GitHub Desktop
1) Verás los cambios en la lista.
2) Rama: **main** (como acordamos).
3) Mensaje: `Bootstrap V4: workflows, ruleset, hooks, template`.
4) Pulsa **Commit to main** y luego **Push origin**.

## Ejecutar el workflow del Agent
En GitHub (web) → **Actions → AingZ Agent PR → Run workflow**. Razón sugerida: `bootstrap`. 


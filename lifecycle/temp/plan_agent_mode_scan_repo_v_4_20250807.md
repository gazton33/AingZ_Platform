# Plan de Ejecución · AgentMode para Escaneo y Migración V4 (2025‑08‑07 · versión FINAL)

> **Contexto actualizado:** El usuario dispone de \~30 mensajes mensuales y máximo **3 ejecuciones Agent Mode**. El repo público a migrar es [**https://github.com/gazton33/AingZ\_Platform.git**](https://github.com/gazton33/AingZ_Platform.git).

---

## 1. Evaluación de Herramientas

| Opción                      | Pros                                                   | Contras                                 | Adecuación                |
| --------------------------- | ------------------------------------------------------ | --------------------------------------- | ------------------------- |
| **Deep Research**           | Rápido para docs externas                              | No mantiene estado; sin git push        | Media                     |
| **Agent Mode (Multi‑turn)** | Clona, testea, commitea, re‑escanea; mantiene contexto | Requiere prompt detallado; tokens altos | **Óptima (seleccionada)** |

---

## 2. Requisitos Previos

1. **Repo URL**: `https://github.com/gazton33/AingZ_Platform.git`
2. **Branch destino**: `migration/v4-baseline`
3. **GitHub Secret**: `GH_TOKEN_RW_B_CI` (`repo`, `workflow` scopes).  Añadir en *Settings → Secrets → Actions*.
4. **Runner**: Container/VM con Python 3.11, Git, Bash, y CLI GitHub (`gh`).  Timeout ≥ 60 min.
5. **Archivos clave ya en raíz**:
   - `Prompt_Codex_Baseline_V4_Check.md`
   - `rw_b_blueprint_v_4_extendido_2025_08_06.md`
   - `rw_b_master_plan_v_4_extendido_2025_08_06.md`
6. **Hooks locales opcionales**: Copiar a `ops/hooks/`.
7. **Límite runs**: 3 ejecuciones Agent Mode → Diseñar prompt idempotente.

---

## 3. Prompt Agent Mode (🔧 listo para copiar)

```agent
# == SETUP ==
SET VAR REPO_URL="https://github.com/gazton33/AingZ_Platform.git"
SET VAR BRANCH="migration/v4-baseline"
SET VAR PROMPT="Prompt_Codex_Baseline_V4_Check.md"
SET VAR BLUEPRINT="rw_b_blueprint_v_4_extendido_2025_08_06.md"
SET VAR MPLAN="rw_b_master_plan_v_4_extendido_2025_08_06.md"
SET VAR RULESET="core/rulset/RULE_CODING_COMPLIANCE_V4.md"
SET VAR GH_TOKEN="$GH_TOKEN_RW_B_CI"

# == OBJECTIVE ==
"""
Migrar la plataforma de estándar V3.x a V4 siguiendo Blueprint y MasterPlan.
Debe:
1. Clonar repo públicamente (`git clone --depth 1 ${REPO_URL}`).
2. Crear rama `${BRANCH}`.
3. Ejecutar `${PROMPT}` en modo baseline ➜ genera baseline.csv y diagnosis.md.
4. Corregir MISSING/RENAME/LEGACY vía scripts (scaffold_readme.py, mover a lifecycle/legacy, etc.).
5. Crear `${RULESET}` + hooks git + workflow CI `.github/workflows/ci_audit.yml`.
6. Re‑ejecutar `${PROMPT}` en modo scan y verificar **0 discrepancias**.
7. Commit & push a `${BRANCH}`.
8. Crear PR automático contra `main`.
"""

# == STEPS ==
1. `git clone ${REPO_URL}` && `cd AingZ_Platform`
2. `git switch -c ${BRANCH}`
3. `python ops/scripts/codex_runner.py --prompt ${PROMPT} --mode baseline`
4. Process `diagnosis.md` ⇒ apply fixes.
5. Generate `${RULESET}` (mandates + triggers).
6. Add git hooks invoking Codex scan + pytest.
7. Create `.github/workflows/ci_audit.yml` (Python 3.11 matrix).
8. `python ops/scripts/codex_runner.py --prompt ${PROMPT} --mode scan` (expect 0 errors).
9. Update root `README.md` (⚠️ Validación Automática + crossrefs reforzados).
10. `git add -A && git commit -m "feat(v4): baseline compliance & CI"`
11. `git push -u origin ${BRANCH}`
12. `gh pr create --fill --base main --head ${BRANCH}`

# == GUARDRAILS ==
- Abort if >10% new discrepancies after step 8.
- Backup legacy files before move.
- Use semantic commits (`feat`, `fix`, `docs`).
- Log to `ops/logs/valog.log`.
- Hard timeout 50 min; auto‑sleep allowed.

# == END ==
```

---

## 4. Estrategia para 3 ejecuciones

| Run | Objetivo                                    | Resultado esperado                                               |
| --- | ------------------------------------------- | ---------------------------------------------------------------- |
| 1   | Baseline + diagnóstico                      | `baseline.csv`, `diagnosis.md` completos. Sin cambios en repo.   |
| 2   | Correcciones & generación de assets V4 + CI | README actualizados, ruleset, hooks, workflow añadidos; scan=OK. |
| 3   | Re‑scan final tras revisión QA              | 0 discrepancias, PR merge‑ready.                                 |

---

## 5. Checklist de Inputs aún necesarios

-

---

## 6. Referencias & Enlaces

- **Repo accesible** y verificado ✔️ ([github.com](https://github.com/gazton33/AingZ_Platform))
- **README actual** muestra estado V3.x auditado ✔️ ([github.com](https://github.com/gazton33/AingZ_Platform))

---

## NEXT\_ACTIONS

1. **Usuario**: crear token y configurar secret.
2. **ChatGPT/Codex**: generar `codex_runner.py` + plantilla RuleSet.
3. **Ejecutar Agent Mode** Run #1 (baseline).

---

**FIN — Plan AgentMode FINAL (repo gazton33/AingZ\_Platform)**


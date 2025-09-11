---
file: new_repo_pack/ruleset_full_v2/ruleset_master_v2.md
code: RSMSTR2
name: RulesetMaster
version: v2.0.0
date: 2025-09-30
owner: "AingZ_Platform · RwB"
status: draft
refs:
  - new_repo_pack/ruleset_full_v2/ruleset_baseline_v2.md
  - new_repo_pack/ruleset_full_v2/develop/ruleset_chatgpt_v2.md
  - new_repo_pack/ruleset_full_v2/develop/ruleset_codex_v2.md
  - new_repo_pack/ruleset_full_v2/context_pack_index.md
---

# Ruleset Maestro — v2

## 1. Alcance
- Aplica a ChatGPT, Codex, VSCode, GitHub, Obsidian, Excalidraw.
- Este archivo prevalece sobre reglas locales.

## 2. Principios globales
- Naming y metadatos coherentes (snake_case / PascalCase según plataforma).
- Crossref y changelog obligatorio.
- OutputTemplate con `status`, `created_at` y `log`.

## 3. Reglas por plataforma
### ChatGPT
- Aplica `ruleset_chatgpt_v2.md`.
- Interacciones ≤120 caracteres, literalidad estricta.
### Codex
- Aplica `ruleset_codex_v2.md`.
- Naming PascalCase, trazabilidad en repos.

## 4. Flujo de evolución
1. Proponer → 2. Validar → 3. Lock (snapshots).

## 5. Router
```yaml
ruleset_master_router:
  global: [[DIR::RULE]]
  platforms:
    chatgpt: [[DIR::RULE]]
    codex: [[DIR::RULE]]
```

## Checklist
- [ ] Cumple naming.
- [ ] Crossref actualizado.
- [ ] OutputTemplate válido.

## OutputTemplate
```yaml
ruleset_master_v2:
  status: draft
  id: RSMSTR2-2025-09-30
  created_at: 2025-09-30T00:00:00Z
  log:
    - step1: authoring
    - step2: review
```

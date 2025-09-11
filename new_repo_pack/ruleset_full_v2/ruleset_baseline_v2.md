---
file: new_repo_pack/ruleset_full_v2/ruleset_baseline_v2.md
code: RBL2
name: RulesetBaseline
version: v2.0.0
date: 2025-09-30
owner: "AingZ_Platform · RwB"
status: draft
---

# Baseline — Ruleset v2

## Router
```yaml
ruleset_router:
  targets:
    global: [[DIR::RULE]]
    platform: [[DIR::RULE]]
  routes:
    - match: {kind: platform, name: chatgpt}
      goto: [[DIR::RULE]]
      section: platform/chatgpt
    - match: {kind: platform, name: codex}
      goto: [[DIR::RULE]]
      section: platform/codex
```

## Normas globales
- Namespaces aprobados.
- ADR para cambios relevantes.

## OutputTemplate
```yaml
baseline_v2:
  status: draft
  created_at: 2025-09-30T00:00:00Z
  log:
    - step1: authoring
```

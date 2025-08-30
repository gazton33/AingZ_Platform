---
file: ruleset/ruleset_master_v_1.md
code: RSMSTR
name: RulesetMaster
version: v1.0.0
date: 2025-08-31
owner: "AingZ_Platform · RwB"
status: draft
refs:
  - ruleset/ruleset_baseline_v_1_locked.md
  - ruleset/develop/ruleset_chatgpt_v_1.md
  - ruleset/develop/ruleset_codex_v_1.md
  - legacy/ruleset/RULE_CODING_COMPLIANCE_V4.md
  - legacy/ruleset/RULE_NAMING_METADATA_CROSSREF_V1.md
  - legacy/ruleset/readme_core_data_ruleset_rw_b_v_3_2.md
  - ruleset/context_pack_index.md
triggers: [TRG_RULESET_MASTER]
---

# Ruleset Maestro — AingZ_Platform

> Documento de máxima jerarquía para todas las apps, conectores y plataformas. Evolutivo y validable con participación del usuario.

## 1. Alcance

 - Aplica a ChatGPT (incluidos modelos como ChatGPT-5 y AgentMode), Codex, VSCode, GitHub, Obsidian, Excalidraw y cualquier conector futuro.
- Este archivo prevalece ante reglas locales; los rulesets específicos se heredan desde aquí.
- Baseline y referencias: RBL, RSCGP, RSCDX y reglas legacy.

## 2. Principios globales

- **Naming y Metadatos**: seguir `RULE_NAMING_METADATA_CROSSREF_V1`.
- **Coding Compliance**: cumplir `RULE_CODING_COMPLIANCE_V4`.
- **Crossref**: toda modificación actualiza referencias y changelog.
- **OutputTemplate**: bloque YAML con `status`, `created_at` ISO8601 y `log`.
- **Context Packs**: utilizar índice en `context_pack_index.md` para seleccionar paquetes.

## 3. Reglas por plataforma

### ChatGPT / ChatGPT-5 / AgentMode
- Aplicar `ruleset_chatgpt_v_1.md`.
- Registrar ruta exacta y OutputTemplate en cada interacción.
- Contratos ≤120 caracteres y literalidad (LSWP).

### Codex
- Aplicar `ruleset_codex_v_1.md`.
- Naming PascalCase con `CODE` ≤5.
- Acciones reproducibles y alineadas con templates `V5/`.

### VSCode
- Sincronizar con Git; commits claros y trazables.
- Respetar naming y metadatos; linting activo.
- Integrar con GitHub para validar antes del push.

### GitHub
- Pull requests directas desde `main`, sin ramas extra.
- Ejecutar checks locales antes de `git push`.
- Mantener cadena `README→RULESET→PIPE` y crossref en cada PR.

### Obsidian
- Notas en Markdown con YAML front‑matter completo.
- Naming `snake_case` y vínculo con ruleset mediante context packs.

### Excalidraw
- Diagramas versionados (`*_vN.excalidraw`).
- Referenciar en crossref y documentar cambios relevantes.

## 4. Flujo de interacción y evolución

1. **Proponer** — El usuario agrega o modifica reglas en la sección pendiente.
2. **Validar** — Se revisan los cambios y se actualiza `status`.
3. **Lock** — Cuando se estabiliza, se genera snapshot según `ruleset_baseline_v_1_locked.md`.

### Sección Pendiente / Feedback del usuario

```markdown
- [ ] Propuesta:
- [ ] Autor:
- [ ] Fecha:
- [ ] Discusión:
- [ ] Resultado:
```

## 5. Router

```yaml
ruleset_master_router:
  global: [[DIR::RULE]]
  platforms:
    chatgpt: [[DIR::RULE]]
    codex: [[DIR::RULE]]
    vscode: [[DIR::RULE]]
    github: [[DIR::RULE]]
    obsidian: [[DIR::RULE]]
    excalidraw: [[DIR::RULE]]
```

## 6. Checklist

- [ ] Cumple naming y metadatos.
- [ ] Crossref actualizado.
- [ ] OutputTemplate válido.
- [ ] Reglas por plataforma revisadas.

## OutputTemplate

```yaml
ruleset_master_v1:
  status: draft
  id: RSMSTR-2025-08-31
  created_at: 2025-08-31T00:00:00Z
  approvals:
    - user:
    - maintainer:
  log:
    - step1: authoring
    - step2: review
```

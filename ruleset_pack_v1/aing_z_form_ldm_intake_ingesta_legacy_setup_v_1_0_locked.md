---
id: aingz_form_ldm_intake
name: FORM_LDM_Intake
version: 1.0.0
status: final
locked: true
owner: AingZ_Platform · ArchOps
scope: Legacy Discovery & Migration · Setup
updated: 2025-08-31
links:
  targets: [RULESET_MAX v1.0.0]
  inherits_from: [InstructionPrompt_RULESET_Dev_LDM v1.0.0]
---

# FORM_LDM — Ingesta inicial de data legacy (Setup)

Propósito: capturar parámetros mínimos para ejecutar **relevamiento LDM** y producir inventario, mapeo y blueprint v0, sin tocar Assets Activos.

---

## 0) Cómo usar

1. Completar el YAML y checklists.
2. Adjuntar rutas/repos o conceder acceso por conectores.
3. Enviar este formulario al proyecto de ChatGPT junto con las **instrucciones**.

---

## 1) Formulario (YAML)

```yaml
form:
  submitter: {name: <string>, email: <string>, area: <string>}
  project: {code: <≤5 SCREAMING_SNAKE>, name: <PascalCase>, dom: <domain>, work_type: <V0|Migracion>, objective: <1 frase>, horizon: <MVP|6-12m|>12m>}
  weights: {evolvability: 0.28, reliability: 0.20, performance: 0.20, simplicity: 0.12, cost: 0.10, auditability: 0.10}
  legacy_inputs:
    locations: [<rutas/repos/carpetas>]
    types: [md, pdf, yaml, py, diagrams, wiki, tickets]
    triage: {A: "crítico", B: "útil", C: "descartable"}
    purge_rules: [pii, secrets, tokens, keys]
    dedup: {strategy: [hash, title+sim], threshold: 0.90}
    mapping_targets: [RULE, SPEC, ENV, PRC, WK, CHK, VALD, AUDT, RPT]
  connectors:
    allowed: [GitHub, GoogleDrive]
    scopes: {github: [<org/repo#branch:path|*>], drive: [<folder paths>]}
    notes: "sin secretos en links públicos"
  access: {reviewers: [<nombres>], approvals_required: [security, data_owner], privacy_class: <public|internal|restricted>}
  outputs: {assets_active: [<docs a impactar tras validación>], canvas_docs: true, obsidian_vault_path: </AingZ/Decisions>, gh_repo_target: <org/repo#branch>}
  review: {sla_days: 3, acceptance_criteria: [ldm_coverage, dedup_ratio, conflict_rate, mapping_confidence]}
  compliance: {pii_expected: <true|false>, secrets_expected: <true|false>, retention_policy: <string>, consent_statement: "Autorizo uso de la data para LDM y consolidación"}
  logs: {wk_batch_id: <uid>}
```

**Checklist de envío**
- [ ] Accesos validados (repos y carpetas)
- [ ] `purge_rules` revisadas por Seguridad
- [ ] `dedup.threshold` confirmado
- [ ] `mapping_targets` acordados
- [ ] `reviewers` asignados

---

## 2) Salidas esperadas

- `legacy_inventory.md`
- `mapping_matrix.md|csv`
- `extraction_pack/`
- `conflicts_report.md`
- `gaps_list.md`
- `migration_plan.md`
- `blueprint_v0.md`

---

## 3) Instrucciones para ChatGPT‑5

```md
Actúa en **modo LDM**. Objetivo: relevar legacy y generar los 7 artefactos de §2 **sin modificar Assets Activos**.
Reglas: respuesta primero; español técnico; fechas absolutas; entrega parcial si falta acceso; usar Archivos/Python/Canvas/VS Code/GitHub/Obsidian según `form.*`; citar web sólo si impacta decisiones; sin PII/secretos en salidas.
Procedimiento: 1) Inventario 2) Normalizar 3) Dedup 4) Mapear 5) Purgar 6) Extraction Pack 7) Conflictos/Vacíos 8) Plan de Migración 9) Blueprint v0 10) Métricas VALM.
Entregables: crear/actualizar 7 archivos en Canvas con front‑matter y OutputTemplate.
```

---

## 4) Plantillas de artefactos

- `legacy_inventory.md`, `mapping_matrix.md`, `conflicts_report.md`, `gaps_list.md`, `migration_plan.md`, `blueprint_v0.md` (esqueletos incluidos en versión de trabajo).

---

## 5) JSON Schema (opcional)

```json
{"$schema":"https://json-schema.org/draft/2020-12/schema","title":"FORM_LDM_Intake","type":"object","properties":{"form":{"type":"object"}},"required":["form"]}
```

---

## 6) Criterios de aceptación (VALM)

```yaml
VALM:
  ldm_coverage: ">= 0.85"
  dedup_ratio: ">= 0.20"
  conflict_rate: "<= 5/100"
  mapping_confidence: ">= 0.75"
```


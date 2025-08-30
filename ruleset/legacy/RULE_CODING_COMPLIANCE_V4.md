---
file: ruleset/legacy/RULE_CODING_COMPLIANCE_V4.md
code: RULE
name: RuleCodingComplianceV4
version: v4.0
date: 2025-08-11
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL, TRG_AUDIT_TL]
chg: CHG_main.md#2025-08-11-rule-coding-v4
chk: CHK_root.md#2025-08-11-rule-coding-v4
---

# Rule — Coding Compliance V4

## PreCheck (obligatorio)
- CODE: `^[A-Z]{1,5}$` y definido en Glosario.
- Ruta válida en Blueprint; `file:` coincide con ruta real.
- `xrf` completo (blueprint/mplan/glossary/dictionary).
- `triggers` incluye `TRG_CONSOLIDATE_TL`.
- **OutputTemplate** integrado.

## PostCheck
- `status: OK` en OutputTemplate.
- Registro `CHG/CHK/CHKP` actualizado (fecha ISO)
- Evidencias publicadas (artefacto/commit/Notion).

## Gates de error
- `BAD_CODE_FORMAT`, `UNKNOWN_CODE`, `ROUTE_OUT_OF_BLUEPRINT`, `MISSING_XRF`, `MISSING_TRIGGERS`, `NO_OUTPUTTEMPLATE`.

---
# OutputTemplate (obligatorio)
rule_coding_compliance_v4:
  status: OK
  id_asset: RULE_CODING_V4_2025-08-11T00:00:00Z
  generated_by: ai
  created_at: 2025-08-11T00:00:00Z
  checks:
    precheck: required
    postcheck: required
  log:
    - step1: declare_rules
    - step2: enforce_pre
    - step3: enforce_post
---
file: core/rulset/RULE_CODING_COMPLIANCE_V4.md
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

> **Propósito**: estandarizar el contrato de cumplimiento para todo asset V4 (naming, ruta, WF, OutputTemplate, crossref) y habilitar su verificación **Pre**/**Post** en cualquier plataforma (Chat/Actions/Bot/Notion).

## 1) Alcance
- Aplica a **todos** los archivos versionados (MD, YAML, scripts) que formen parte del árbol V4.
- Compatible con CI (GitHub Actions) y orquestación Notion.

## 2) PreCheck (obligatorio)
- **CODE**: coincide con `^[A-Z]{1,5}$` y existe en **Glosario** (CODE_Glossary_v2).
- **Ruta**: válida según **Blueprint V4**; el campo `file:` del front‑matter **coincide** con la ruta real.
- **Metadatos**: front‑matter completo (`file, code, name, version, date, owner, status, xrf, triggers, chg, chk`).
- **XRF**: referencias presentes a `blueprint`, `mplan`, `glossary`, `dictionary`.
- **Triggers**: lista contiene al menos `TRG_CONSOLIDATE_TL` (y los que correspondan por ciclo).
- **WF**: pasos explícitos o referencia clara a WF aplicable.
- **OutputTemplate**: bloque YAML integrado (estructura mínima validable).

## 3) PostCheck (obligatorio)
- `OutputTemplate.status == OK` y `created_at` en ISO8601.
- `CHG/CHK/CHKP/LESSONS` actualizados (fecha actual) y enlazados.
- Evidencias publicadas: artefacto CI / commit en ruta / snapshot Notion.

## 4) Gates de error
- `BAD_CODE_FORMAT` → `code:` no cumple regex o no existe en Glosario.
- `UNKNOWN_CODE` → CODE no registrado en Glosario.
- `ROUTE_OUT_OF_BLUEPRINT` → ruta fuera del árbol permitido.
- `MISMATCH_FILE_ROUTE` → `file:` no coincide con la ruta efectiva.
- `MISSING_XRF` → faltan refs a blueprint/mplan/glossary/dictionary.
- `MISSING_TRIGGERS` → no declara triggers mínimos.
- `NO_OUTPUTTEMPLATE` → falta bloque OutputTemplate.

## 5) Notas de precedencia
- En conflicto de semántica o triggers, **prevalecen** `CODE_Glossary_v2` y `CODE_Triggers_v2` (máxima jerarquía).

## 6) Checklist rápido
- [ ] CODE ≤5 (`SCREAMING_SNAKE`) y válido en Glosario.
- [ ] `file:` = ruta real; ubicación válida (Blueprint).
- [ ] XRF completo a Blueprint/MPlan/Glosario/Diccionario.
- [ ] Triggers declarados (`TRG_CONSOLIDATE_TL` mínimo).
- [ ] WF explícito y **OutputTemplate** integrado.
- [ ] CHG/CHK/CHKP/LESSONS actualizados.

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


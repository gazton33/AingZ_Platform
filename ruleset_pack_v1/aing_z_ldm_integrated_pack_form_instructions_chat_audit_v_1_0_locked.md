---
id: aingz_ldm_integrated_pack
name: LDM_Integrated_Pack
version: 1.0.0
status: final
locked: true
owner: AingZ_Platform · ArchOps
scope: Legacy Discovery & Migration · Chats Audit
updated: 2025-09-01
links:
  imports: [RULESET_MAX v1.0.0, InstructionPrompt_RULESET_Dev_LDM v1.0.0, FORM_LDM_Intake v1.0.0]
---

# LDM Pack integral — Form + Template + Instrucciones de auditoría de hilos
Propósito: auditar hilos nuevos o antiguos, **extraer notas/feedback/aprendizajes** relevantes al RULESET, **completar el FORM** y dejar artefactos listos para consolidar y migrar a Assets Activos.

---

## 0) Cómo ejecutar en hilos NUEVOS o ANTIGUOS
**Modo A — Hilo nuevo (recomendado):** pega el bloque de §3 “Instrucciones para ChatGPT‑5” + completa el **FORM** (§2).  
**Modo B — Hilo antiguo:** trae el transcript como texto/MD o archivo (Drive/GitHub). Si no hay exportación, copia y pega manualmente en Canvas.

**Reglas globales**
- Respuesta primero. Español técnico. Fechas absolutas.
- Sin PII/secretos en salidas; enmascarar.
- Entrega parcial si faltan insumos. No asíncrono.
- Hereda principios de `RULESET_MAX`. Excepciones solo vía `SPEC.*`.

---

## 1) Plantilla mínima de RULESET para mapeo
Usar esta ficha para **cada item extraído** del chat.

```yaml
mapped_item:
  legacy_id: <uid|msg_id>
  source: <chat_title|url|file>
  when: <YYYY-MM-DDThh:mm:ssZ>
  author: <human|ai|user@org>
  snippet: "<texto breve>"
  target:
    code: <RULE|SPEC|ENV|PRC|WK|CHK|VALD|AUDT|RPT>
    name: <PascalCase sugerido>
  confidence: <0.0-1.0>
  pii_or_secret: <true|false>
  notes: <observaciones>
```

**Heurística de relevancia (chat → RULESET)**
- **Reglas/instrucciones**: frases con “regla”, “instrucción”, “debe/shall”, checklist.
- **Decisiones**: “decidimos”, “aprobado/rechazado”, ADR implícito.
- **Aprendizajes**: “aprendimos”, “retro”, “insight”.
- **Feedback**: “mejorar”, “dolor”, “riesgo”.
- Ignorar charla social; marcar dudas como `open_question` en `notes`.

---

## 2) FORM embebido (v1.0)
> **Clonar y completar**. Fuente: `FORM_LDM_Intake v1.0.0`.

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
  chat_inputs:
    threads: [<títulos o urls de hilos>]
    timeframe: {from: <YYYY-MM-DD>, to: <YYYY-MM-DD|today>}
    transcript_provider: <manual_paste|export_md|drive_file>
    message_filters: [#decision, #rule, #instruction, #risk, #retro]
  connectors:
    allowed: [GitHub, GoogleDrive]
    scopes: {github: [<org/repo#branch:path|*>], drive: [<folder paths>]}
  outputs: {assets_active: [<docs a impactar tras validación>], canvas_docs: true, obsidian_vault_path: </AingZ/Decisions>, gh_repo_target: <org/repo#branch>}
  review: {sla_days: 3, acceptance_criteria: [ldm_coverage, dedup_ratio, conflict_rate, mapping_confidence]}
  compliance: {pii_expected: <true|false>, secrets_expected: <true|false>, retention_policy: <string>}
  logs: {wk_batch_id: <uid>}
```

**Checklist de envío**
- [ ] Accesos validados (repos/carpeta y hilos)
- [ ] `purge_rules` revisadas por Seguridad
- [ ] `dedup.threshold` confirmado
- [ ] `mapping_targets` acordados
- [ ] `reviewers` asignados

---

## 3) Instrucciones para ChatGPT‑5 — Auditoría de hilos (pegar en el chat)
```md
Actúa en **modo LDM**. Objetivo: auditar hilos nuevos/antiguos, extraer notas/feedback/aprendizajes y **mapear a RULESET_MAX**, generando artefactos sin modificar Assets Activos.

Procedimiento:
1) **Confirmación de alcance** con `form.*` y `chat_inputs.*`.
2) **Ingesta**: recibir transcript como texto/MD o archivo; si falta acceso, continúa con entrega parcial.
3) **Normalizar**: convertir a tabla (msg_id, fecha, autor, rol, texto).
4) **Extracción**: detectar candidatos por heurística (reglas/decisiones/instrucciones/feedback/aprendizajes).
5) **Dedup**: aplicar `dedup.strategy` y `threshold`; conservar versión más rica.
6) **Purgar**: aplicar `purge_rules`; enmascarar PII/secretos.
7) **Mapeo**: emitir `mapped_item` por candidato a [RULE|SPEC|ENV|PRC|WK|CHK|VALD|AUDT|RPT] con `confidence`.
8) **Pack de extracción**: compilar textos limpios por target y fuente.
9) **Reporte de auditoría**: síntesis por hilo, decisiones, riesgos, vacíos y recomendaciones.
10) **Métricas**: `ldm_coverage`, `dedup_ratio`, `conflict_rate`, `mapping_confidence`.

Entregables (Canvas):
- `chat_audit_report.md`
- `legacy_inventory.md`
- `mapping_matrix.md|csv`
- `extraction_pack/`
- `conflicts_report.md`
- `gaps_list.md`
- `migration_plan.md`
- `blueprint_v0.md`
- `form_filled.yaml`
```

---

## 4) Procedimiento de auditoría detallado
**Estructura tabular (recomendada):**
```yaml
chat_row: {msg_id: <id>, date: <iso>, author: <name|ai>, role: <system|user|assistant|tool>, text: "..."}
```
**Patrones útiles:** `^#`, `\bdecid(imos|ir)\b`, `\bregla\b`, `\binstrucci[oó]n\b`, `\bpr[oó]ximo paso\b`, `\baprend(imos|izaje|imos)\b`, `\briesgo\b`.

**Scoring de relevancia (0..1):**
```yaml
score:
  match_terms: 0.5
  section_format: 0.2
  author_weight: 0.2
  recency: 0.1
threshold_keep: 0.6
```

**Resolución de conflictos:** preferir mensajes más recientes y confirmados en ADR/decisión; registrar el conflicto en `conflicts_report.md`.

---

## 5) Plantillas de artefactos (chat)
### 5.1 `chat_audit_report.md`
```md
---
file: chat_audit_report
code: CAR
version: 0.1.0
date: <YYYY-MM-DD>
status: working
refs: [RULESET_MAX v1.0.0]
---
# Resumen ejecutivo
- Hilos analizados: N
- Ítems mapeados: N (confianza media: X)
- Conflictos: N  · Vacíos: N  · Duplicados removidos: N

## Hallazgos por categoría
- RULE: …
- SPEC: …
- ENV: …
- PRC: …
- WK/CHK/VALD/AUDT/RPT: …

## Decisiones y riesgos
- …

## Recomendaciones
- …

## Métricas (VALM)
- ldm_coverage: … · dedup_ratio: … · conflict_rate: … · mapping_confidence: …
```

### 5.2 `mapping_matrix.md`
```md
| legacy_id | hilo | msg_id | tipo | target_CODE | target_name | snippet | confianza |
| --------- | ---- | ------ | ---- | ----------- | ----------- | ------- | --------- |
```

### 5.3 `form_filled.yaml`
```yaml
# Copia del §2 con valores reales utilizados
```

---

## 6) OutputTemplate (general)
```yaml
output_example:
  status: OK
  generated_by: ai
  created_at: <YYYY-MM-DDThh:mm:ssZ>
  params:
    - mode: LDM_chat_audit
    - thresholds: {dedup: 0.90, keep: 0.60}
  result:
    - ready_to_use: true
    - files: [chat_audit_report.md, legacy_inventory.md, mapping_matrix.md, extraction_pack/, conflicts_report.md, gaps_list.md, migration_plan.md, blueprint_v0.md, form_filled.yaml]
  log:
    - step1: ingest_transcripts
    - step2: normalize_extract
    - step3: dedup_map_purge
    - step4: reporting_metrics
```

---

## 7) Checklists
- [ ] FORM completo y validado
- [ ] Transcripts cargados y normalizados
- [ ] Dedupe aplicado y documentado
- [ ] Mapeo a RULESET_MAX con `confidence`
- [ ] Purgas de PII/secretos aplicadas
- [ ] Artefactos generados en Canvas
- [ ] Métricas VALM reportadas


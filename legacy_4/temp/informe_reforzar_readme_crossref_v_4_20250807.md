---
CODE: DOC
ID: informe_reforzar_readme_crossref_v_4_20250807_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/lifecycle/temp/informe_reforzar_readme_crossref_v_4_20250807.md
CROSSREF:
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# Informe · Refuerzo README & Ruleset — Transición V3.x ➜ V4 (2025‑08‑07)

---

## 1. Panorama de problemas detectados
| Nº | Categoría | Descripción del problema | Impacto |
|----|-----------|--------------------------|---------|
| 1 | **Interpretación Codex** | El modelo ejecutó acciones sin respetar siempre el prompt `Prompt_Codex_Baseline_V4_Check.md` ni las reglas del *Blueprint* y *Master Plan* V4. | Riesgo de naming/ruta incorrectos y divergencia de estándar. |
| 2 | **Crossref insuficiente** | README raíz y secundarios no obligan a validar `CROSSREF` ni a ejecutar triggers tras cada cambio. | Falta de trazabilidad, mayor probabilidad de errores. |
| 3 | **Ruleset débil**      | No existe un documento RULE formal que encapsule las validaciones mínimas para GitHub + Codex + CI. | Dificulta enforcement automático y revisiones PR. |
| 4 | **Compatibilidad CI/CD** | Falta script/hook que ejecute prompt Codex + tests antes de *merge*. | Riesgo de integrar cambios no conformes. |

---

## 2. Requerimientos de refuerzo (según solicitud)
1. **README main** debe:
   - Incluir sección *“⚠️ Validación Automática”* con pasos explícitos para Codex (ejecutar prompt, validar rutas, naming, crossref y triggers).  
   - Enumerar archivos de referencia obligatorios: `Prompt_Codex_Baseline_V4_Check.md`, `rw_b_blueprint_v_4_extendido_2025_08_06.md`, `rw_b_master_plan_v_4_extendido_2025_08_06.md`.
   - Instruir a Codex a *reanálisis completo* (`LITW //sweep`) antes de cada serie de commits.
2. **Crossref & Naming Check**: Añadir mandato de ejecutar script `TRG_AUDIT_TL` al cerrar cualquier PR.
3. **Ruleset sólido**: Crear archivo `core/rulset/RULE_CODING_COMPLIANCE_V4.md` que contenga:
   - Checklist de validación (naming, ruta, metadatos YAML, OutputTemplate, crossref).
   - Hooks Git (`pre-commit`, `pre-push`) que llamen al prompt Codex + pruebas unitarias.
4. **Compatibilidad GitHub & Codex**:
   - Definir *Workflow GitHub Actions* que instale Python 3.11, ejecute prompt Codex en modo *dry‑run*, compare árbol vs baseline y falle si hay discrepancias.
   - Configurar *CI* para correr unit tests en `ops/tests/` y triggers de auditoría.
5. **Procedimiento iterativo V4**:
   - Ciclo PDCA sobre README como *asset de prueba* antes de migrar resto de carpetas.
   - Actualización incremental de README secundarios siguiendo estandarización.

---

## 3. Propuesta de Ruleset → `RULE_CODING_COMPLIANCE_V4`
```yaml
ID: RULE_CODING_COMPLIANCE_V4
VERSION: 0.1‑draft
SCOPE: Naming · Ruta · Crossref · OutputTemplate · CI/CD
MANDATES:
  - Todo archivo/README debe incluir metadatos YAML y bloque OutputTemplate.
  - Crossrefs obligatorios a Blueprint, MasterPlan, Prompt Codex.
  - Ningún cambio se puede *mergear* si `TRG_AUDIT_TL` ≥ 1 fallo.
  - GitHub Action `ci_audit.yml` debe ejecutarse y aprobar.
  - Hooks locales (`pre‑commit`, `pre‑push`) ejecutan prompt Codex en modo *scan*.
TRIGGERS_REQUIRED:
  - TRG_CONSOLIDATE_TL
  - TRG_AUDIT_TL
  - TRG_LSWP
```

---

## 4. Procedimiento iterativo (First Steps V4)
1. **Baseline & Diagnóstico** (ya generado)  
2. **Crear `RULE_CODING_COMPLIANCE_V4.md`** en `core/rulset/`  
3. **Actualizar README main** con secciones reforzadas (⚠️ Validación Automática, Crossref obligatorio).  
4. **Configurar hooks Git** (`ops/hooks/`).  
5. **Adicionar GitHub Action** `ci_audit.yml`.  
6. **Regenerar README secundarios** (`core/`, `core/data/…`) con estándar V4 + crossref.  
7. Ejecutar prompt Codex → validar **0 discrepancias**.  
8. Documentar resultado en `CHANGELOG` y `LESSONS_LEARNED`.  

---

## 5. Configuración & compatibilidad multi‑plataforma
| Plataforma | Requisito clave | Archivo/Script |
|------------|----------------|----------------|
| **GitHub** | Workflow CI con Python 3.11 + prompt Codex *dry‑run* + UnitTests | `.github/workflows/ci_audit.yml` |
| **Codex**  | Prompt obligatorio (`Prompt_Codex_Baseline_V4_Check.md`) + re‑scan tree | (en README main) |
| **Python** | Versión mínima 3.11, `requirements.txt` actualizado, virtualenv reproducible | `ops/requirements/` |
| **Local hooks** | `pre‑commit`, `pre‑push` que invocan prompt Codex + `pytest` | `ops/hooks/` |

---

## 6. Roadmap inmediato (bloque
Kanban simplificado)
- **TO DO**: RULE_CODING_COMPLIANCE_V4 · Hooks · Workflow CI  
- **IN PROGRESS**: Reescritura README main con refuerzo  
- **BLOCKED**: Ninguno  
- **DONE**: Baseline V3.x, Identificación problemas Codex  

---

## 7. Próximos pasos para el equipo
1. Validar este informe en reunión corta.  
2. Aprobar creación del Ruleset y CI.  
3. Proceder a reforzar README main + bootstrap hooks.  
4. Revisar Codex interpretando prompt actualizado.  
5. Continuar con migración iterativa del árbol.  

---

**FIN — Informe de refuerzo README & Ruleset V4**

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

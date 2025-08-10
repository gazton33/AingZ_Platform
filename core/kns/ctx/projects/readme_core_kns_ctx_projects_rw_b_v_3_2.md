---
CODE: CORE
ID: readme_core_kns_ctx_projects_rw_b_v_3_2_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/core/kns/ctx/projects/readme_core_kns_ctx_projects_rw_b_v_3_2.md
CROSSREF:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
# 🗂️ core/kns/ctx/projects/ — Contexto Extendido por Proyecto/Rama (v3.2)

## 1. Descripción, función, objetivos y contexto

La carpeta `core/kns/ctx/projects/` almacena **contextos extendidos, configuraciones y preferencias** de cada proyecto/rama de la plataforma AingZ/RwB, asegurando personalización, onboarding y explotación de contexto vivo a nivel micro.

### Funciones principales:

- Registrar configuraciones, contexto operativo y glosario ampliado de cada proyecto/rama.
- Facilitar onboarding incremental, personalización y reporting de contexto vivo específico.
- Servir de input para IA/humano en recuperación y análisis de contexto histórico/actual por proyecto/rama.

### Integraciones y sistemas relacionados:

- Crossref con onboarding, lessons y checkpoints de proyecto (`doc/`, `kns/`, `chkp/`).
- Contexto de proyecto nutre personalización, recuperación de contexto y mejora de experiencia a nivel de rama.

## 2. Estructura interna

| Archivo/Subcarpeta | Propósito                                    | Estado |
| ------------------ | -------------------------------------------- | ------ |
| preferencias\_X/   | Preferencias y configuraciones de proyecto X | Activo |
| glosario\_X.md     | Glosario ampliado de proyecto/rama X         | Activo |
| ...                | Otros contextos específicos                  | Activo |

## 3. Metadatos y compliance

- **Versión:** v3.2 — 2025-08-06
- **Owner/Responsable:** AingZ\_Platform · RwB
- **Crossref obligatoria:** Blueprint, master plan, checklist, template universal README (ops/templates/)
- **Naming/Versionado:** Cumplimiento estricto de políticas RwB v3.2
- **Estado:** Activo

## 4. Ciclo de vida y flujos

```mermaid
graph TD;
  A[Ingreso/update de contexto proyecto/rama] --> B[Validación compliance y naming]
  B --> C[Crossref en README, onboarding y checklist]
  C --> D[Recuperación y explotación por IA/humano]
  D --> E[Lessons learned y cierre de ciclo]
```

## 5. Changelog local

- 2025-08-06: Versión v3.2, compliance contexto extendido proyecto/rama.

## 6. Observaciones / Lessons learned

- Todo cambio de contexto/preferencia de proyecto debe estar versionado y referenciado.
- Mantener onboarding y recuperación de contexto de proyecto/rama sincronizados con lessons y releases de rama.

---

**FIN README core/kns/ctx/projects/ v3.2**

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

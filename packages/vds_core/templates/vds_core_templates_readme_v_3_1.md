---
CODE: DOC
ID: vds_core_templates_readme_v_3_1_v4
VERSION: v4.0-2025-08-10
ROUTE: /home/runner/work/AingZ_Platform/AingZ_Platform/packages/vds_core/templates/vds_core_templates_readme_v_3_1.md
CROSSREF:
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
AUTHOR: AingZ_Platform
DATE: 2025-08-10
---
## Índice

1. [Descripción General](#1-descripción-general)
2. [Estructura Interna](#2-estructura-interna)
3. [Cross‑References](#3-cross-references)
4. [Uso y Buenas Prácticas](#4-uso-y-buenas-practicas)
5. [Quick Start / Ejemplo](#5-quick-start--ejemplo)
6. [Lecciones y Recomendaciones](#6-lecciones-y-recomendaciones)
7. [Compliance & Governance](#7-compliance--governance)
8. [Changelog](#8-changelog)
9. [Metadatos IA](#9-metadatos-ia)

---

## 1. Descripción General

Repositorio de plantillas parametrizables (Jinja, Bash, Markdown, YAML, Python) empleadas como base para nuevos scripts, tests, docs y scaffolds de core/plugins. Permiten acelerar el desarrollo y garantizar naming/compliance. Cada template debe estar bien documentado y versionado.

---

## 2. Estructura Interna

| Path   | Rol        | Descripción breve                                   |
| ------ | ---------- | --------------------------------------------------- |
| ./     | Contenedor | README + metadatos                                  |
| \*.tpl | Template   | Plantillas parametrizables para scripts, docs, etc. |
| \*.md  | Docs       | Plantillas rápidas de documentación                 |

---

## 3. Cross‑References

- **Blueprint v3** → [`../../../lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md`](../../../lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md)
- **Master Plan v3** → [`../../../lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md`](../../../lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md)
- **Checklist Root v3** → [`../../../checklist_root_rw_b_v_3_20250803.md`](../../../checklist_root_rw_b_v_3_20250803.md)
- **Core README** → [`../README.md`](../README.md)

---

## 4. Uso y Buenas Prácticas

- Cada template debe contener cabecera con descripción, autor, fecha y uso esperado.
- Actualizar/changeloguear cualquier cambio de estructura, naming o lógica.
- Adaptar templates al contexto del plugin/core, evitando hardcoding.

---

## 5. Quick Start / Ejemplo

```bash
# Listar plantillas disponibles
$ ls *.tpl *.md

# Copiar y adaptar plantilla
$ cp script_base.tpl nuevo_script.sh
```

---

## 6. Lecciones y Recomendaciones

- Versionar todo template significativo; mantener histórico.
- Documentar limitaciones y recomendaciones de uso en cada archivo.

---

## 7. Compliance & Governance

| Área     | Regla                  | Fuente         |
| -------- | ---------------------- | -------------- |
| Naming   | `naming_universal_v3`  | Blueprint §2.2 |
| Template | Formato parametrizable | Master Plan §3 |

---

## 8. Changelog

| Fecha      | Versión | Autor       | Cambios                            |
| ---------- | ------- | ----------- | ---------------------------------- |
| 2025-08-05 | v3.1    | ChatGPT 4.1 | README inicial enriched templates/ |

---

## 9. Metadatos IA

```yaml
bucket: packages/vds_core/templates
version: v3.1
updated: 2025-08-05
blueprint_ref: ../../../lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
master_plan_ref: ../../../lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
triggers:
  - TRG_AUDIT_LEGACY
  - TRG_CONSOLIDATE_TL
  - TRG_PURGE_AI
```

---

**FIN README packages/vds\_core/templates/ v3.1**

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

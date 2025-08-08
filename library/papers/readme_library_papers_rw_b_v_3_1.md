---
file: readme_library_papers_rw_b_v_3_1.md
version: v3.1-2025-08-05
status: active
role: readme
owner: AingZ_Platform · RwB
crossref:
  - lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md
  - lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md
  - lifecycle/temp/prompt_codex_baseline_v_4_check.md
  - core/rulset/RULE_CODING_COMPLIANCE_V4.md
  - core/kns/glossary/rw_b_glosario_code_v_2_20250729.md
  - core/data/dicts/rw_b_diccionario_code_triggers_v_2_20250729.md
  - ops/templates/template_readme_rw_b_v_4.md
---

# 📄 README — Subcarpeta `papers/` (RwB v3.1)

## 1. Rol y propósito
Subcarpeta para gestión, referencia y trazabilidad de **papers científicos, artículos y publicaciones técnicas** relevantes para los workflows y dominios RwB.

## 2. Estructura y criterios
- Ingresar solo papers completos, preferentemente con DOI o fuente de origen clara.
- Metadatos mínimos: título, autores, revista/congreso, año, DOI, licencia.
- Formatos preferidos: PDF (principal), TXT (backup, solo si es legal).

## 3. Naming y versionado
- `paper_{titulo}_autor_año_revista_rw_b_v_3_1.pdf`
- Documentar en README todas las referencias y versiones.

## 4. Crossref obligatoria
- [README library/](../readme_library_rw_b_v_3_1.md)
- [Blueprint v3](../../../blueprint_rw_b_platform_v_3_20250803.md)
- [Checklist Root](../../../checklist_root_rw_b_v_3_20250805.md)

## 5. Buenas prácticas y lessons learned
- Verificar acceso y uso permitido (open access o licencia adecuada).
- Mantener tabla de papers actualizada y trazable en README.
- Registrar excepciones, erratas o papers retirados.

## 6. Tabla de papers (ejemplo)

| Título                  | Autor(es)      | Año | Revista/Congreso | DOI                | Licencia      | Estado |
|------------------------|----------------|-----|------------------|--------------------|--------------|--------|
| AI for Engineers       | Smith et al.   | 2022| AI Journal       | 10.1234/ai.eng.22  | Open Access  | ✅     |
| Energy Efficient Design| Zhang & Lee    | 2021| Eng. Conf. 2021  | 10.4321/eed.21     | Academic Use | ✅     |

---
**FIN README — papers/**


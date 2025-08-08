---
file: readme_library_rw_b_v_3_1.md
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

# 📚 README — Bucket `library/` (RwB v3.1)

## 1. Rol y propósito

Bucket para almacenamiento, consulta y versionado de **recursos de referencia**: libros, papers, normas, manuales, datasets y licencias. Estructura compatible con ciclo PDCA, crossref y onboarding humano/IA.

## 2. Estructura y subniveles

| Subcarpeta   | Contenido principal                 | Estado   |
|--------------|-------------------------------------|----------|
| books/       | Libros y obras de referencia        | ✅       |
| papers/      | Artículos, papers y publicaciones   | ✅       |
| normas/      | Normas técnicas y estándares        | ✅       |
| manuals/     | Manuales y guías prácticas          | ✅       |
| datasets/    | Datasets de entrenamiento/uso       | ✅       |
| licencias/   | Licencias y permisos de uso         | ✅       |

## 3. Naming y versionado
- Archivos principales: `readme_library_{subnivel}_rw_b_v_3_1.md`
- Versionado semántico y metadatos YAML obligatorios.

## 4. Crossref obligatoria
- [Blueprint v4](../lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md)
- [Master Plan v4](../lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md)
- [Prompt Codex Baseline v4](../lifecycle/temp/prompt_codex_baseline_v_4_check.md)
- [Ruleset Coding Compliance v4](../core/rulset/RULE_CODING_COMPLIANCE_V4.md)
- [Checklist Root](../checklist_root_rw_b_v_3_20250805.md)
- [Workflow Naming/Creación](../wf_pipeline_creacion_archivos_rw_b_v_3_20250805.md)

## 5. Flujo y ciclo de vida (PDCA)

```mermaid
flowchart TD
  start([Input recurso])
  start --> c1[Verificar subcarpeta destino]
  c1 --> c2[Nombrar y versionar asset]
  c2 --> c3[Registrar metadatos y crossref]
  c3 --> c4[Guardar y actualizar README local]
  c4 --> c5[Registrar en checklist y changelog]
  c5 --> end([Recurso drop-in listo para consulta])
```

## 6. Buenas prácticas y lessons learned
- Mantener metadatos y naming alineados a blueprint/master plan.
- Documentar cualquier excepción, workaround o integración externa.
- No agregar ni migrar recursos sin actualizar crossref y checklist.
- Verificar compatibilidad y trazabilidad documental en onboarding.

---
**FIN README — Bucket `library/` (RwB v3.1)**


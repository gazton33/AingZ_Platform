---
asset:
  id: audit_baselines_20250926
  name: Audit · Baselines & Ruleset Alignment
  type: audit
  version: 0.1.0
  status: working
context:
  scope: obsidian_master_template_aingz_master
  reviewers: ["AI Codex", "GPT5", "AingZ_Platform · RwB"]
  sources:
    - core/doc/workbench/AINGZ_V5_Baselines_Unificados_v1_4_1_locked.md
    - core/doc/workbench/dir_tree_v_1_4_baseline_locked.md
    - core/doc/workbench/glossary_baseline_v_1_locked.md
    - core/doc/workbench/ruleset_baseline_v_1_locked.md
    - ruleset/ruleset_master_v_1.md
logs:
  created_at: 2025-09-26T00:00:00Z
  updated_at: 2025-09-26T00:00:00Z
---

# Auditoría de alineación con baselines (2025-09-26)

## Objetivo

Documentar requisitos presentes en los baselines/ruleset maestros que todavía no están reflejados en `obsidian_master_template_aingz_master.md` y definir acciones de actualización.

## Brechas detectadas

| Origen | Requisito base | Observación en plantilla actual | Riesgo |
| ------ | -------------- | -------------------------------- | ------ |
| Baselines Unificados v1.4.1 | OutputTemplate exige `baseline_id`, `result.dir_tree/glossary/ruleset` y bitácora `qa_pass → checkpoint → freeze`. | La plantilla no expone campos YAML ni sección para reportar estado de baselines congelados o bitácora de freeze. | Pérdida de trazabilidad frente a locks oficiales. |
| DirTree v1.4.2 (lock) | Checklists para ASCII tree con códigos `[CODE]` y OutputTemplate con `files_frozen`. | No existe callout/sección que solicite incrustar la vista ASCII ni validar códigos `DIR::`. | Desalineación con nomenclatura y navegación oficial. |
| Glosario v1.0.0 (lock) | IDs deben comenzar con `GLOS::` y referencias limitarse a `DIR::` sin rutas físicas. | En la plantilla no hay validación o recordatorio para usar `GLOS::` ni restricción de rutas en referencias semánticas. | Riesgo de introducir términos fuera del vocabulario controlado. |
| Ruleset v1.0.0 (lock) | `ruleset_router` obliga `goto: [[DIR::...]]` y checklist de namespaces válidos. | La sección de gobernanza no menciona restricciones de router ni namespaces. | Romper el router maestro y pipelines dependientes. |
| Ruleset Maestro v1.0.0 | Requiere bloque `Sección Pendiente / Feedback`, OutputTemplate con `approvals.user/maintainer`, selección de `context packs`, y contratos específicos por plataforma (ej. `≤120` caracteres en ChatGPT, `CODE ≤5` en Codex). | La plantilla carece de bloque pendiente, no pide `approvals`, no menciona `context_pack_index`, ni hace cumplir límites por plataforma. | Falta de readiness para auditorías y cooperación multi-plataforma. |

## Recomendaciones de actualización

1. **Frontmatter**: agregar bloque `baselines:` con `id`, `dir_tree`, `glossary`, `ruleset` y `approvals` (`user`, `maintainer`) más campo `context_pack` enlazado a `ruleset/context_pack_index.md`.
2. **Sección 02 · Contratos y Metadata**: incorporar callout `todo` que liste verificaciones de locks (`DIR::`, `GLOS::`, router) y un sub-bloque para registrar el `OutputTemplate` actual de baselines.
3. **Nueva subsección en 20·30**: embed/placeholder para ASCII tree (`![[...dir_tree...]]`) y recordatorio de validar códigos `[CODE]` antes de publicar.
4. **Sección 50 · Feedback y WK.log**: añadir bloque plegable `Sección Pendiente / Feedback` replicando el contrato del ruleset maestro y relacionarlo con KPIs.
5. **Guías por plataforma**: insertar callouts específicos (ChatGPT, Codex, GitHub) que recuerden límites operativos (contratos ≤120 caracteres, `CODE` ≤5, PR directo a `main`) para mantener compliance cruzado.

## Próximos pasos sugeridos

- Validar propuestas con guardianes de ruleset antes de versionar la plantilla.
- Priorizar incorporación en la próxima iteración del master template y actualizar KPIs de adopción tras el cambio.
- Registrar el merge resultante en WK.log y generar snapshot si los nuevos campos afectan contratos existentes.

> [!todo]- Seguimiento
> - [ ] Validar bloque YAML extendido.
> - [ ] Diseñar callouts y secciones propuestas.
> - [ ] Actualizar README catálogo tras aprobación.

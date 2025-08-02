# Auditoría RAW — AingZ_Repo-main.zip (Legacy)

## 1. Mapeo completo de estructura y archivos

## Árbol de carpetas y archivos — AingZ_Repo-main.zip

- `AingZ_Repo-main/`
    - `AingZ_Repo-main/`
        - `.gitattributes`
        - `.gitignore`
        - `README.md`
        - `changelog.md`
        - `convencion_nombrado_versionado_full_custom_infraestructura.md`
        - `master_plan_aingz_infrastructure.md`
        - `readme_base_aingz_t_3_infra.md`
        - `readme_integracion_t_2_memorias_historiales.md`
        - `readme_master_plan.md`
        - `readme_matriz_memorias_historiales.md`
        - `t_3_roadmap_integrado_conectores_ia_full_custom.md`
        - `Cierre_integracion_1/`
            - `plantilla_readme_cierre_hilo_raw_gold.md`
            - `prompt_cierre_auditoria_hilos.md`
            - `readme_cierre_t_0_raw_gold.md`
            - `readme_cierre_t_1_raw_gold.md`
            - `readme_cierre_t_3_raw_gold.md`
            - `t_2_raw_gold_matriz_historiales.md`
        - `doc/`
            - `ChatGPT Image 13 jul 2025, 22_35_55.png`
            - `ChatGPT Image 14 jul 2025, 10_08_00.png`
            - `croquis_mapeo_features_prompts.md`
            - `faq_avanzada_gestion_de_adjuntos_knowledge_y_workflows_fuera_de_proyectos_aing_z_repo.md`
            - `mapa_jerarquia_instrucciones_aing_z_repo_borrador_raw.md`
            - `mapa_jerarquia_instrucciones_aing_z_repo_visual_markdown.md`
            - `welcome_onboarding_gz.md`
            - `Gem_Digitales/`
                - `gem_dig_gz_gpt_raw.md`
                - `gem_dig_gz_gpt_raw_v_1.md`

## 2. Matching vs. Matriz RAW GOLD

| **Componente RAW GOLD** | **¿Presente?** | **Ubicación/Archivo Legacy**         | **Notas y gaps**                                   |
|------------------------|:--------------:|--------------------------------------|----------------------------------------------------|
../knowledges/            |                |                                      |                                                    |
| /matrices/             |                |                                      |                                                    |
| /WF/            |                |                                      |                                                    |
| /scripts/              |                |                                      |                                                    |
| /logs/                 |                |                                      |                                                    |
| /doc/                 |     ✔️         | doc/                                | Croquis, diagramas, onboarding presentes.           |
| / (README raíz)        |     ✔️         | README.md                            | Existe, falta README por subcarpeta.                |
| /config/ (.env, .json) |                |                                      |                                                    |
| /backups/              |                |                                      |                                                    |
| /notebooks/            |                |                                      |                                                    |

## 3. Coverage y gaps detectados
- **Ejemplos reales:** Faltan carpetas tipo../knowledges/`, `/matrices/`, `/WF/`, `/scripts/`, `/logs/`, `/config/`, `/backups/`, `/notebooks/` (no están como carpetas, aunque hay archivos relacionados distribuidos en raíz y `doc/`).
- **Plantillas base:** Solo parcial, plantillas de cierre (`plantilla_readme_cierre_hilo_raw_gold.md`).
- **Documentación y naming:** Documentación central sólida, faltan convenciones y README por carpeta.
- **Automatización y scripts:** No se detectan scripts de automatización, sync o backup en carpetas dedicadas.
- **Logs y seguimiento:** Sin carpeta/logs automáticos, registro manual en changelog.

## 4. Recomendaciones para migración
- **Qué reutilizar directamente:** Documentos de master plan, convenciones, changelog, README central, docs visuales.
- **Qué crear/adaptar:** Crear estructura modular según RAW GOLD; mover/renombrar archivos existentes a las carpetas objetivo; generar README y templates base por carpeta; iniciar logging y automatización.
- **Automatización/coverage inmediato:** Implementar scripts de sync/backup; definir naming y versionado por carpeta; establecer coverage checklists en onboarding.
- **Prioridades para onboarding y pruebas:** Testing de workflows locales, simulación de flujos completos (alta, rollback, logs, backups), documentación de casos y lessons learned en knowledge base.

---

> Este documento se irá completando tras el análisis RAW del .zip. El output final servirá de base para el roadmap de migración a la arquitectura RAW GOLD.


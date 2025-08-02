# KNS_CTX_O3_41_ANALISIS_INTEGRACION.md

> **Instrucciones esenciales para modelos o3 y 4.1 — análisis e integración de conceptos avanzados de arquitectura en DIR_ARCH_PLAN y workflows RwB**

---

## 1. Límite de contexto vivo (o3 y 4.1)

- **o3:** 200,000 tokens (~150,000 palabras), salida máxima 100,000 tokens.
- **4.1:** 1,000,000 tokens (~750,000 palabras), salida máxima 65,536 tokens.
- El contexto debe incluir solo archivos, insights y chunkings estrictamente necesarios.
- **Nunca** adjuntar archivos “full” ni listas masivas; siempre generar slices/insights, con coverage, fecha y tokens usados.

---

## 2. Instrucciones dirigidas a modelos (o3/4.1) para análisis e integración

1. **Leer, comparar y consolidar:**
   - Analizar todos los archivos core relevantes (README, DirArchPlan, Matrix, glosario, workflows, learn, logs) usando solo los slices/insights optimizados para tokens.
   - Identificar y documentar gaps, duplicidades, inconsistencias y propuestas de mejora.
2. **Integrar conceptos nuevos:**
   - Fusionar literal y semánticamente los conceptos de “LEGACY”, “DESARROLLO/STAGING”, eliminación del purgatorio y snapshots de contexto vivo, en el blueprint del DIR_ARCH_PLAN.
   - Proponer el árbol de directorio y reglas resultantes, listos para la matriz y el glosario.
3. **Mantener trazabilidad:**
   - Registrar cada cambio, consolidación o ajuste en los logs y changelog principales.
   - Actualizar README y matrices según toda integración realizada.
4. **Respetar límites de contexto:**
   - Antes de agregar nuevos insights/archivos, medir y auditar los tokens consumidos respecto al modelo objetivo (o3/4.1) usando la matriz.
   - Si se supera el límite, priorizar: blueprint, matriz, glosario, workflows y logs activos; dejar extras en slices/insights secundarios.
5. **Preparar para siguiente ciclo (Workflows):**
   - Una vez consolidada la infraestructura y naming, analizar y definir los workflows y scripts de transición, integración, migración y QA alineados a la nueva arquitectura.
   - Registrar lessons, feedback, triggers y checklists en LEARN y en los README.

---

## 3. Ejemplo de checklist para análisis/integración

- [ ] ¿Están todos los conceptos y reglas nuevos reflejados en DIR_ARCH_PLAN y blueprint?
- [ ] ¿Se integraron/actualizaron los flujos de LEGACY y DESARROLLO?
- [ ] ¿Fue eliminada toda referencia al purgatorio y ajustado el backup?
- [ ] ¿Están claros los triggers y outputs para workflows futuros?
- [ ] ¿Se registró y versionó cada cambio en los logs/changelog/README?
- [ ] ¿La matriz de límites de contexto está referenciada y alineada?

---

## 4. Notas para modelos o3 y 4.1

- Priorizar siempre la literalidad, la trazabilidad, el coverage y la exhaustividad alineada al estándar RwB Universal.
- Toda propuesta de integración debe estar documentada y ser reproducible paso a paso.
- Si se detecta conflicto entre glosario, matriz y blueprint, listar explícitamente la discrepancia y sugerir resolución.
- El output debe ser siempre auditable y modular.

---

## 5. Archivos y referencias obligatorias para adjuntar con este KNS_CTX

### a. Blueprint, matriz y guía de referencia
- `rw_b_dir_arch_plan_v_4_20250729.md`  
  _Blueprint arquitectónico definitivo del repositorio (DIR_ARCH_PLAN v4)._
- `rw_b_assets_classification_matrix_v_1_20250729.md`  
  _Matriz de clasificación de assets (origen × etapa × rol) y procedimientos asociados._
- `mpln_master_plan_aingz_rw_b_v_20250729_v_3.md`  
  _Master Plan arquitectónico, hoja de ruta y dependencias clave._
- `rw_b_checklist_avances_v_1_20250730.md`  
  _Checklist incremental de tareas ejecutadas y cobertura._

### b. Glosario, diccionario y triggers
- `rw_b_diccionario_code_triggers_v_2_20250729.md`  
  _Diccionario de triggers y lookup de prompts/scripts._
- (Glosario CODE v2: si el archivo está presente, incluirlo como fuente principal de naming y semántica)

### c. Workflows principales de operación
- `wf_cons_actv_transcripcion_raw_v_4_20250730_draft.md`  
  _Workflow de consolidación y actualización de activos en desarrollo._
- `rw_b_wf_auditoria_legacy_v_3_20250725.md`  
  _Workflow optimizado para auditoría, mapeo y consolidación de legacy._
- `wf_migracion_final_legacy_rw_b_v_1_20250725.md`  
  _Workflow para migración final de legacy._
- `rw_b_wf_dictado_v_1.md`  
  _Workflow para interacción y procesamiento por dictado (voz/texto)._
- `rw_b_wf_relevamiento_ideas_actv_v_1_20250725.md`  
  _Workflow de relevamiento de ideas y baseline._
- `wk_feedtrn_eval_actv_raw_v_2_20250725.md`  
  _Workflow de feedback, learning, training, evals y tuning._

### d. Control de trazabilidad y mapping
- `registro_trazabilidad_total.md`  
  _Mapeo automático legacy → RwB, estados de migración, checklist de integración._

### e. Límites de contexto IA y auditoría tokens
- `matriz_limites_contexto_chatgpt_v_1.md`  
  _Tabla de límites de contexto vivo (tokens) para modelos IA, ejemplos de chunking/auditoría._

---

### f. Archivos de referencia y logs
- `readme.md`  
  _README principal del repo (estructura, reglas y referencias)._
- `chglog_main_rwb_v_4_20250729.md`  
  _Changelog maestro de cambios y versión._

---

### g. Criterios de adjunción
- Todos estos archivos deben ser incluidos como adjuntos (o como slices/insights si el contexto lo requiere).
- Se deben priorizar archivos en este orden para evitar duplicidades y asegurar coverage.
- Si la ventana de tokens es insuficiente para todos, priorizar blueprint, matriz, glosario, workflows activos y mapping.

---

**FIN — KNS_CTX_O3_41_ANALISIS_INTEGRACION.md**


---
file: informe_tareas_pendientes_v4.md
version: v4.0-2025-08-07
status: record
role: report
owner: AingZ_Platform · RwB
---

### 1. `Prompt_Codex_Baseline_V4_Check.md` no está referenciado  
`ops/paths_cache.json` define `Prompt_Codex_Baseline_V4_Check.md` como `null`, dejando el campo `crossref_prompt_codex` vacío en `README.md`.  

:::task-stub{title="Registrar ruta real de Prompt Codex"}
1. Abrir `ops/paths_cache.json` y sustituir `null` por la ruta real `lifecycle/temp/prompt_codex_baseline_v_4_check.md`.
2. Ejecutar `python ops/update_crossrefs.py` para propagar el nuevo `crossref_prompt_codex` en todos los README.
3. Confirmar los cambios en `changelog.md` y `lessons_learned.md`.
:::

---

### 2. Crossref obsoletos en README secundarios  
Archivos como `core/readme_core_rw_b_v_3_2.md` mantienen referencias a blueprint y master plan de la serie v3.x, sin reflejar las rutas actuales de los documentos V4.  

:::task-stub{title="Actualizar crossref en README secundarios a V4"}
1. Localizar los README desactualizados (`core/`, `library/`, `packages/`, etc.).
2. Sustituir referencias v3.x por:
   - `lifecycle/temp/rw_b_blueprint_v_4_extendido_2025_08_06.md`
   - `lifecycle/temp/rw_b_master_plan_v_4_extendido_2025_08_06.md`
   - `lifecycle/temp/prompt_codex_baseline_v_4_check.md`
   - `core/rulset/RULE_CODING_COMPLIANCE_V4.md`
3. Verificar metadatos y registrar cambios en `changelog.md`.
:::

---

### 3. Falta de barrido y validación de metadatos  
El plan exige un barrido “LITW //sweep” y la verificación de metadatos/OutputTemplate en cada README, pero no se ha documentado su ejecución.  

:::task-stub{title="Automatizar barrido y validación de metadatos"}
1. Ejecutar `python ops/scripts/litw_sweep.py` para generar el listado completo de rutas.
2. Alimentar `ops/paths_cache.json` con las rutas resultantes.
3. Validar metadatos con `python ops/validate_metadata.py <lista_de_readme>`.
4. Documentar los resultados en `changelog.md` y `lessons_learned.md`.
:::

---

### 4. Script `update_crossrefs.py` depende de nombres rígidos  
`ops/update_crossrefs.py` usa un mapeo fijo (`CROSSREF_FIELDS`) que no contempla cambios de nombre o mayúsculas/minúsculas (caso `Prompt_Codex`).  

:::task-stub{title="Hacer dinámico el mapeo de crossref"}
1. En `ops/update_crossrefs.py`, reemplazar `CROSSREF_FIELDS` por una lectura dinámica de `ops/paths_cache.json` para obtener los nombres reales de los archivos clave.
2. Normalizar la comparación de rutas con `lower()` para evitar problemas de capitalización.
3. Añadir pruebas unitarias que cubran cambios de nombre y ausencias de archivos.
:::

---

### 5. Checks de GitHub dependen de secreto ausente  
Los workflows (`baseline_check.yml`, `tests.yml`, `validation.yml`) requieren `GH_TOKEN_RW_B_CI`; si no está configurado, los jobs fallan durante `actions/checkout`.  

:::task-stub{title="Configurar secreto y validar workflows"}
1. Crear el secreto `GH_TOKEN_RW_B_CI` en GitHub con scope `repo, workflow`.
2. Verificar que `baseline_check.yml`, `tests.yml` y `validation.yml` leen el secreto mediante `${{ secrets.GH_TOKEN_RW_B_CI }}`.
3. Lanzar un push/pr de prueba para confirmar que los tres workflows completan `checkout`, instalación de dependencias y scripts.
:::

---

### 6. `run_codex_baseline_v4_check.py` es solo placeholder  
El workflow `codex-baseline-check` ejecuta un script sin validaciones reales, lo que impide detectar incoherencias de crossref o metadatos.  

:::task-stub{title="Implementar verificación real en Codex baseline check"}
1. En `ops/scripts/run_codex_baseline_v4_check.py`, agregar lógica que invoque `ops/validate_metadata.py` y `ops/update_crossrefs.py` en modo dry-run.
2. Retornar código de salida distinto de cero ante cualquier error de metadatos o crossref.
3. Ajustar `baseline_check.yml` para fallar el job si el script retorna error.
:::

---

Estas tareas priorizan la trazabilidad y la sostenibilidad operativa del repositorio, alineadas con la arquitectura V4 y garantizando que los checks de GitHub se ejecuten de manera confiable y transparente.

### Notas para modelos o3 y gpt-4.1
- Mantener seguimiento de referencias dinámicas permite **in-context learning** estable y evita drift semántico.
- La estandarización de metadatos facilita el fine-tuning responsable y mejora la capacidad de auditoría.
- Recomendación: validar este listado con pruebas automáticas en cada commit para sostener calidad y reproducibilidad.

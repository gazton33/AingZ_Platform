# PLN · Primeros pasos Codex — Update Crossref y Compliance V4 (2025-08-07)

---

## Objetivo
Automatizar la actualización dinámica de crossref, metadatos y validación compliance en TODO el árbol del repo, tras cualquier movimiento de archivos clave o cambios en la estructura.

---

## Pasos detallados para Codex

### 1. **Barrido literal completo del repo**
- Ejecutar barrido 100% (`LITW //sweep` o script Python) para listar TODAS las rutas y archivos presentes, sin omitir ninguna carpeta/subcarpeta.

### 2. **Detectar archivos clave y rutas reales**
- Localizar la ruta actual de:
  - `Prompt_Codex_Baseline_V4_Check.md`
  - `rw_b_blueprint_v_4_extendido_2025_08_06.md`
  - `rw_b_master_plan_v_4_extendido_2025_08_06.md`
  - `core/rulset/RULE_CODING_COMPLIANCE_V4.md` (si existe)
- Registrar cualquier cambio respecto a la ubicación esperada o documentada.

### 3. **Actualizar crossref dinámico**
- En cada README (raíz y secundarios), actualizar referencias y rutas a los archivos clave, según su ubicación real detectada.
- Si un crossref es ambiguo, duplicado o apunta a ruta vieja, corregirlo y documentar el fix en changelog.

### 4. **Validar y estandarizar metadatos y OutputTemplate**
- Verificar que todos los README incluyan:
  - Metadatos YAML mínimos (CODE, ID, VERSION, ROUTE, CROSSREF, AUTHOR, DATE)
  - Descripción y objetivos actualizados (no legacy)
  - Crossref con rutas reales
  - Bloque OutputTemplate al final

### 5. **Ejecutar triggers y registrar en logs**
- Lanzar triggers QA (`TRG_AUDIT_TL`, `TRG_CONSOLIDATE_TL`, `TRG_LSWP`) tras la actualización.
- Registrar cada acción en `changelog.md` y `lessons_learned.md`, incluyendo detalles de archivos movidos, crossref corregidos, excepciones detectadas, etc.

### 6. **Configurar y testear CI/token si aplica**
- Si el repo usará CI/CD automático:
  - Verificar la existencia/configuración del secret `GH_TOKEN_RW_B_CI` (scopes: `repo`, `workflow`).
  - Actualizar `requirements.txt` con `openai`, `pyyaml`, `pytest`, y otras dependencias si falta.
  - Validar que workflows y hooks apunten a rutas reales, no fijas.
- Si sólo trabajo local/manual: dejar como opcional, no requerido.

### 7. **Ciclo iterativo y compliance**
- Tras cada ciclo, revalidar que el crossref y metadatos de TODOS los README coinciden con la ubicación y estado real del repo.
- Documentar lessons learned, changelog y checklist incremental.

---

## Criterios de éxito
- Crossref actualizado y coherente en el 100% de README y assets.
- Ningún README referencia rutas o archivos movidos/legacy.
- Todo fix y hallazgo documentado en changelog y lessons learned.
- Compliance y triggers QA activos en cada ciclo.

---

**Fin PLN primeros pasos Codex para compliance V4**


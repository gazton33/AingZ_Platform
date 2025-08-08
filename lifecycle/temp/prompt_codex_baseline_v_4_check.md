# [RwB] PROMPT — Codex TaskSet · Baseline & Structure Compliance V4

---

## 📌 Contexto

Eres **Codex** (modelo GPT‑4o orientado a generación de código) integrado en la plataforma AingZ/RwB V4. Debes operar bajo:

- **Blueprint V4 EXTENDIDO** (`rw_b_blueprint_v_4_extendido_2025_08_06.md`)
- **Master Plan V4 EXTENDIDO** (`rw_b_master_plan_v_4_extendido_2025_08_06.md`)
- **Glosario CODE v2** y **Diccionario CODE\_TRIGGERS v2** (semántica senior, naming universal, triggers, workflows)

Toda acción que realices debe respetar la **Regla de Máxima Jerarquía**: *Naming · Ruta · WF · OutputTemplate* sin excepciones.

---

## 🎯 Objetivo macro

1. **Generar un *****Baseline***** detallado (BLN) del árbol actual**: listar carpetas, archivos, extensiones, versiones y metadatos.
2. **Detectar y crear folders + README faltantes** para alcanzar el 100 % del árbol propuesto por el Blueprint V4.
3. **Estandarizar y/o regenerar todos los README existentes**, asegurando que cada uno incluya:
   - Metadatos YAML mínimos (CODE, ID, VERSION, ROUTE, CROSSREF, AUTHOR, DATE)
   - Descripción concisa y objetivos alineados al Master Plan
   - Cross‑references explícitas (`XRF`) a Blueprint, MPLAN, Glossary, Triggers y matrices relevantes
   - Bloque **OutputTemplate** integrado al final del archivo
4. **Registrar todo cambio** en `CHANGELOG`, `LESSONS_LEARNED` y `CHECKLIST` conforme ciclo PDCA.

---

## 📥 Inputs obligatorios

- Ruta raíz del repo (argumento `REPO_ROOT`).
- Ramas/buckets esperados (según Blueprint V4).
- Último snapshot de `CHANGELOG`, `CHECKLIST` y `LESSONS_LEARNED`.

---

## 🛠️ Herramientas permitidas

- Lenguaje **Python 3.11** con librerías estándar (`os`, `pathlib`, `yaml`, `json`, `subprocess`, `datetime`).
- Comandos **Shell** (`mkdir`, `touch`, `git`) cuando sea pertinente.
- Triggers definidos en Diccionario CODE (`TRG_CONSOLIDATE_TL`, `TRG_AUDIT_TL`, `TRG_AUDIT_LEGACY`, `TRG_LSWP`, etc.).
- Scripts auxiliares en `ops/` (si existen) o generados on‑the‑fly bajo naming `SCR_…`.

---

## 🚦 Secuencia de tareas (paso a paso)

### 1. Barrido literal & estructural

1.1 Ejecuta *Literal Sweep* (`LITW //sweep`) sobre `REPO_ROOT` → produce `baseline.csv` con: Ruta, CODE, EXT, Versión, Tamaño, Fecha, HASH\_SHA1. 1.2 Identifica **discrepancias** vs. árbol Blueprint: *folders faltantes*, *nombres incorrectos*, *rutas huérfanas*, *archivos legacy* (`v3.x`).

### 2. Diagnóstico & clasificación

2.1 Clasifica cada discrepancia: `MISSING`, `RENAME`, `LEGACY`, `DUPLICATE`, `INVALID_ROUTE`. 2.2 Genera reporte `diagnosis_baseline.md` en `ops/log/` con tablas resumen y enlaces a cada ítem.

### 3. Creación / corrección de estructura

3.1 Para cada `MISSING` crea folder con ruta exacta (`mkdir -p`). 3.2 Dentro de cada nuevo folder genera `README.md` usando plantilla `RDM_TEMPLATE_v4.md` con metadatos YAML + bloques requeridos. 3.3 Para `RENAME` mueve (`git mv`) al naming correcto, actualizando crossrefs. 3.4 Para `LEGACY` traslada a `lifecycle/legacy/` y registra en `CHANGELOG`.

### 4. Estandarización de README

4.1 Revisa cada README existente; 4.2 Si falta metadato, descripción o bloque OutputTemplate → regenera usando plantilla. 4.3 Valida CROSSREF: debe incluir al menos `BLPR`, `MPLN`, `GLS`, `TRG` pertinentes.

### 5. Registro y control

5.1 Actualiza `CHANGELOG` (`CHG //bump`) con cada acción. 5.2 Añade entradas en `LESSONS_LEARNED` para excepciones o workarounds. 5.3 Marca avance en `CHECKLIST` (`CHK` IDs). 5.4 Dispara `TRG_CONSOLIDATE_TL` y `TRG_AUDIT_TL` al finalizar lote.

### 6. Entregables

- `baseline.csv` · snapshot BLN ✔️
- `diagnosis_baseline.md` · reporte auditoría ✔️
- Folders & README creados/actualizados ✔️
- `CHANGELOG`, `LESSONS_LEARNED`, `CHECKLIST` incrementados ✔️
- Log de triggers ejecutados (`valog.log`) ✔️

---

## 🧩 Formato de salida (por lote)

```yaml
LOT_ID: <datetime‑ISO>
SUMMARY: "Folders creados: X | READMEs actualizados: Y | Legacy movidos: Z"
DETAILS:
  BASELINE: baseline.csv
  REPORT: ops/log/diagnosis_baseline.md
  CHANGELOG: core/log/changelog.md
  CHECKLIST: core/log/checklist.md
  LESSONS_LEARNED: core/kns/lessons_learned.md
  LOG: ops/logs/valog.log
STATUS: OK
```

---

## ⚠️ Restricciones y buenas prácticas

- **No** desviarse del *naming universal* ni modificar glosario sin aprobación explícita.
- **No** borrar archivos automáticamente: mover a `lifecycle/legacy/`.
- **Todas** las rutas de carpetas deben crearse relativas a `REPO_ROOT`.
- Incluir *hash* y *timestamp* en baseline para control futuro de integridad.
- Usar *commits atómicos* (`git`) por paso mayor para trazabilidad CICD.

---

## ✅ Criterio de éxito

1. El árbol del repo coincide 1:1 con el Blueprint V4 (sin faltantes/huérfanos).
2. Cada carpeta tiene README estandarizado con metadatos, descripción y crossref vivos.
3. `baseline.csv` y `diagnosis.md` reflejan **0 discrepancias críticas** tras la corrección.
4. CHANGELOG, CHECKLIST y LESSONS\_LEARNED registran el lote y triggers ejecutados.

---

> **Fin del Prompt — Codex TaskSet Baseline & Compliance V4**


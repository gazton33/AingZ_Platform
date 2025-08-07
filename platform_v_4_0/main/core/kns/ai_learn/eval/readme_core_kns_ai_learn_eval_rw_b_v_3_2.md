---

file: readme\_core\_kns\_ai\_learn\_eval\_rw\_b\_v3\_2.md version: v3.2-2025-08-06 status: active role: readme owner: AingZ\_Platform · RwB crossref:

- blueprint\_rw\_b\_platform\_v\_3\_20250803.md
- mpln\_master\_plan\_rw\_b\_v\_3\_20250803.md
- checklist\_root\_rw\_b\_v\_3\_20250805.md
- wf\_pipeline\_creacion\_archivos\_rw\_b\_v\_3\_20250805.md
- ops/templates/template\_readme\_rw\_b\_v3\_1.md changelog:
- 2025-08-06: Consolidación README eval/ ai\_learn v3.2, compliance y estructura métricas IA/humano.

---

# 📊 core/kns/ai\_learn/eval/ — Evaluaciones y Métricas de Aprendizaje (v3.2)

## 1. Descripción, función, objetivos y contexto

La carpeta `core/kns/ai_learn/eval/` centraliza **todas las evaluaciones, métricas y análisis de performance** asociados al aprendizaje IA/humano en la plataforma AingZ/RwB.

### Funciones principales:

- Almacenar reportes, análisis, métricas y validaciones de modelos, prompts y tuning.
- Facilitar el control de calidad, benchmarking y tracking de progresos o regresiones.
- Permitir auditoría y mejora continua sobre procesos de aprendizaje y ajuste IA/humano.

### Integraciones y sistemas relacionados:

- Conexión directa con lessons, tuning y feedback (`ai_learn/`), y assets de métricas globales (`metrics/`).
- Datos de evaluaciones alimentan procesos de onboarding, reporting y ajustes de workflows (`wf/`).

## 2. Estructura interna

| Archivo/Subcarpeta  | Propósito                            | Estado |
| ------------------- | ------------------------------------ | ------ |
| metricas\_X.md      | Métricas de aprendizaje/test X       | Activo |
| benchmark\_modelos/ | Resultados y comparativas de modelos | Activo |
| ...                 | Otros análisis y reportes            | Activo |

## 3. Metadatos y compliance

- **Versión:** v3.2 — 2025-08-06
- **Owner/Responsable:** AingZ\_Platform · RwB
- **Crossref obligatoria:** Blueprint, master plan, checklist, template universal README (ops/templates/)
- **Naming/Versionado:** Cumplimiento estricto de políticas RwB v3.2
- **Estado:** Activo

## 4. Ciclo de vida y flujos

```mermaid
graph TD;
  A[Ingreso/update de métrica/evaluación] --> B[Validación compliance y naming]
  B --> C[Crossref en README, metrics y checklist]
  C --> D[Uso en feedback, tuning y lessons]
  D --> E[Lessons learned y cierre de ciclo]
```

## 5. Changelog local

- 2025-08-06: Versión v3.2, compliance métricas y evaluaciones IA/humano.

## 6. Observaciones / Lessons learned

- Todas las métricas y evaluaciones deben tener referencia cruzada con lessons, tuning y assets de reporting.
- Mantener histórico y trazabilidad para auditoría y mejora continua.

---

**FIN README core/kns/ai\_learn/eval/ v3.2**


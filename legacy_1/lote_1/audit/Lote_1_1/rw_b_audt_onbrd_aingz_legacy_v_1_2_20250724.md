# RwB_AUDT_ONBRD_AINGZ_LEGACY_v1.2_20250724.md — Auditoría legacy bajo workflow v1.2 (Draft)

---

## 1. Propósito/contexto
Auditar el archivo de onboarding y reglas de contexto vivo para el proyecto AingZ_Repo, asegurando trazabilidad, integración y adaptación a la infraestructura RwB.

---

## 2. Barrido literal selectivo y mapeo estructural
- **Bloques críticos:**
  - Instrucciones iniciales: leer siempre el MASTER_PLAN_AINGZ_INFRASTRUCTURE.md antes de avanzar en cualquier hilo.
  - Registro de ideas/errores/cambios importantes en la knowledge base (insights, fecha, contexto).
  - Auditoría: revisar y actualizar matrices de control de fuentes/cobertura.
  - Buenas prácticas: uso de naming/estructura sugeridos, anotar dependencias y relación con master plan en cada deliverable, registrar fecha/motivo en migraciones, documentar todo para no perder cobertura.
  - Referencias clave: MASTER_PLAN_AINGZ_INFRASTRUCTURE.md, knowledge_gz_project_insights.md, croquis-mapeo-features-prompts.md, matriz_extendida_features_chatgpt_workflow.md, control_trazabilidad_fuentes_chatgpt_workflow.md, control-cruce-matriz-raw-vs-extendida.md
- **Mapeo glosario/estructura:**
  - Este archivo cumple función de onboarding, control de contexto y gobernanza del flujo de trabajo: Categoría “core/infraestructura”, clase “ONBRD/README”.
  - Directamente vinculado a los templates y triggers de cambios en el stack principal.

---

## 3. Análisis de integración y mejoras
- Estructura secuencial, bloques claros, referencias cruzadas y triggers bien definidos.
- **Propuesta:** Mantener un template universal de onboarding para cada nuevo repo/proyecto. Incluir checklist de actualización (¿se revisaron las matrices? ¿se loggearon cambios?).
- No requiere nueva clase de archivo, pero sí consolidar los templates ONBRD y README como clase explícita en la arquitectura.

---

## 4. Checklist de cobertura y reproducibilidad (versión visual-friendly)

Cobertura mínima:
- Bloques críticos extraídos y mapeados: OK
- Referenciado al glosario y estructura core: OK
- Checklist ONBRD/README sugerido: OK
- Feedback registrado en memoria viva: OK
- Legacy original referenciado (Legacy_onboarding_gz.md): OK
- Propuestas de mejora estructural: OK
- Auto-reproducible con legacy accesible: OK

---

## 5. Feedback, lessons learned, riesgos
- Estructura robusta pero dependiente de actualización disciplinada.
- Recomendación: automatizar triggers de actualización y checks periódicos en futuros workflows.

---


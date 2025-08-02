# RwB_AUDT_TEMPLATE_CASOS_USO_PRECEDENCIA_INFRA_FULL_CUSTOM_LOTE2_20250725.md — Auditoría estructural legacy (Draft)

---

## 1. Propósito/contexto
Auditoría de los templates legacy para casos de uso: precedencia, infraestructura full custom y segmentación multi-entorno (AingZ_Repo). Proveen la base para customización global, proyectos y asistentes IA.

---

## 2. Barrido literal selectivo y mapeo estructural
- **Bloques críticos:**
  - Templates para personalización global, proyectos/workspaces y asistentes custom (GPTs).
  - Detalle de propósito, template base (en MD), inputs permitidos, outputs, logging, criterios para elegir cada entorno.
  - Regla universal: “aplica workflow universal salvo override por capa inferior”.
  - Referencias cruzadas: workflows, matrices, README y logs.
- **Mapeo glosario/estructura:**
  - Clase “TEMPLATE/CASOS_USO”; función “infraestructura/template base”, bloque “customización/control”.
  - Puente entre onboarding, customización y governance de IA multi-entorno.

---

## 3. Análisis de integración y mejoras
- Propuesta: Mantener los templates versionados y documentar upgrades en cada release; agregar ejemplos de integración y logging en workflows.
- Sumar triggers de exportación/logging y recomendaciones para QA/onboarding automatizado.

---

## 4. Checklist de cobertura y reproducibilidad (visual-friendly)
- Templates global, proyecto y asistente extraídos: OK
- Inputs/outputs, logging y reglas de precedencia: OK
- Referencias cruzadas a workflows, matrices y README: OK
- Legacy original referenciado (templates_casos_uso_precedencia_infraestructura_full_custom.md): OK
- Auto-reproducible con legacy accesible: OK

---

## 5. Feedback, lessons learned, riesgos
- Si los templates no se actualizan en releases y upgrades, se pierde control y trazabilidad de customizaciones.
- Propuesta: Versionar cada template, registrar upgrades en changelog y documentar mejores prácticas de integración.

---


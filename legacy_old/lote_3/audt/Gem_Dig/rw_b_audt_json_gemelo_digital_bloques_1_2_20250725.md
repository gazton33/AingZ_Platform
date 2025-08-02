# RwB_AUDT_JSON_GEMELO_DIGITAL_BLOQUES_1_2_20250725.md — Auditoría estructural bloques JSON (1 y 2)

---

## 1. Propósito/contexto
Auditoría de los bloques de entrevista para perfil Gemelo Digital GZ: identidad, perfil profesional, formación y certificaciones. Sirven como input para onboarding IA, memoria viva y tuning de sistemas personalizados.

---

## 2. Barrido literal selectivo y mapeo estructural
### Bloque 1: Identidad y perfil profesional
- Datos personales, historia breve, auto-presentación, motivación principal, valores clave, visión de futuro.
- Campos para validación: coherencia entre identidad percibida y trayectoria, alineación de valores con ética/objetivos del sistema IA.
- Mapeo: clase “PERFIL/IDENTIDAD”, función “onboarding/entrypoint”, referencia a blueprint de skills y valores.

### Bloque 2: Formación académica y certificaciones
- Estudios formales, títulos, certificaciones, cursos clave, logros destacados.
- Campos de validación: mapeo con legacy (CV, Gemelo Digital MD), profundidad de skills certificados, actualización de competencias.
- Mapeo: clase “FORMACION/CERTIFICACION”, función “skills/core”, referencia cruzada a memoria viva y templates de onboarding.

---

## 3. Checklist de cobertura y reproducibilidad (visual-friendly)
- Identidad y valores extraídos: OK
- Formación y certificaciones mapeadas: OK
- Referencias a legacy y skills: OK
- Auto-reproducible con acceso a bloques/legacy: OK

---

## 4. Feedback, lessons learned, riesgos
- Sin integración viva de identidad y skills, el onboarding IA puede perder fidelidad o reproducir datos desactualizados.
- Propuesta: cruzar todos los cambios de perfil con memoria viva y consolidar logs de upgrades/cambios significativos.

---


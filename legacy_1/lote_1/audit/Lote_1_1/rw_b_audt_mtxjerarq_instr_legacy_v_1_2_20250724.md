# RwB_AUDT_MTXJERARQ_INSTR_LEGACY_v1.2_20250724.md — Auditoría legacy bajo workflow v1.2 (Draft)

---

## 1. Propósito/contexto
Auditoría del diagrama visual y reglas de jerarquía de instrucciones para el stack AingZ_Repo.

---

## 2. Barrido literal selectivo y mapeo estructural
- **Bloques críticos:**
  - Diagrama Mermaid de jerarquía (ética, global, proyecto, gpt, sesión, prompt) y reglas de precedencia.
  - Leyenda de capas y niveles, explicación de anulación/herencia, zonas de compliance.
  - Observaciones clave: precedencia (prompt > resto), excepción de límites no anulables, conflicto y persistencia.
- **Mapeo glosario/estructura:**
  - Clase “MTX/JERARQ/INSTR”; función “documentación arquitectónica”, bloque “diagramas/reglas core”.
  - Referencia a matrices extendidas y docs de control de flujos.

---

## 3. Análisis de integración y mejoras
- Diagrama modular y portable; leyenda clara, alineada a workflows y features RwB.
- **Propuesta:** Unificar todos los diagramas Mermaid en un subdirectorio “diagramas/core” con versión controlada.
- Sumar a los templates una sección de “reglas de precedencia/anulación”.

---

## 4. Checklist de cobertura y reproducibilidad (versión visual-friendly)

Cobertura mínima:
- Bloques críticos extraídos y mapeados: OK
- Referenciado al glosario y arquitectura “documentación/diagramas”: OK
- Propuesta de subdirectorio para diagramas Mermaid: OK
- Feedback registrado: OK
- Legacy original referenciado (Legacy_MTX_jerarquia_instrucciones.md): OK
- Auto-reproducible con legacy accesible: OK

---

## 5. Feedback, lessons learned, riesgos
- Riesgo de obsolescencia si no se actualiza tras cambios en flujos/compliance.
- Recomendación: documentar triggers para actualización automatizada en futuros ciclos.

---


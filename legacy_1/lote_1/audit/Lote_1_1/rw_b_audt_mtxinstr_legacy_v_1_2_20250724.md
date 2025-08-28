# RwB_AUDT_MTXINSTR_LEGACY_v1.2_20250724.md — Auditoría legacy bajo workflow v1.2 (Draft)

---

## 1. Propósito/contexto
Auditoría del esquema de capas y reglas de precedencia/herencia para instrucciones y workflows en AingZ_Repo.

---

## 2. Barrido literal selectivo y mapeo estructural
- **Bloques críticos:**
  - Desglose de niveles/capas: Global, Proyecto, GPT, Sesión, Prompt.
  - Reglas de precedencia, herencia, anulación, persistencia y conflicto.
  - Elementos visuales: nodos/cajas por capa, flechas de herencia, zonas de límites, colores por función.
- **Mapeo glosario/estructura:**
  - Clase “MTX/INSTR”; función “documentación funcional”, bloque “jerarquía/workflows”.
  - Vinculado a templates de tablas de precedencia y diagramas visuales.

---

## 3. Análisis de integración y mejoras
- Propuesta: Consolidar una plantilla tipo “jerarquía de instrucciones” con variantes para usuarios, admins y devs.
- Sumar tabla de precedencia y registro de casos límite a los outputs futuros.
- Proponer subdirectorio “workflows/jerarquía” dentro de la arquitectura.

---

## 4. Checklist de cobertura y reproducibilidad (versión visual-friendly)

Cobertura mínima:
- Bloques críticos extraídos y mapeados: OK
- Referenciado al glosario y arquitectura “workflows/documentación”: OK
- Propuesta de plantilla y subdirectorio jerarquía: OK
- Feedback registrado: OK
- Legacy original referenciado (Legacy_MTX_instrucciones.md): OK
- Auto-reproducible con legacy accesible: OK

---

## 5. Feedback, lessons learned, riesgos
- Riesgo de ambigüedad si no se mantiene la tabla de precedencia y las reglas actualizadas en cada cambio del stack.
- Sugerencia: Versionar tabla/jerarquía en cada entrega relevante.

---


# [RwB] Master Plan — Plataforma AingZ/RwB V4 (EXTENDIDO 2025-08-06)

---

## 1. Objetivo, misión y contexto V4
La etapa V4 marca el cierre de toda la legacy y la apertura de una plataforma auditable, robusta y modular que maximiza la automatización, compliance y escalabilidad IA/humano. El objetivo es consolidar el árbol de directorios como línea de base única y documentar en vivo cada ciclo operativo, migración y test, asegurando que cada activo sea drop-in-ready, auto-documentado y fácil de auditar. El contexto incluye lessons learned, feedback de usuarios, resultados de test y todo el conocimiento acumulado durante el ciclo V3.x y su migración total a V4.

---

## 2. Premisas, reglas y principios activos
- Naming, ruta, WF y OutputTemplate son requisitos **innegociables** para todo asset, workflow o procedimiento. Su omisión invalida el asset o integración.
- Todo ciclo de migración, integración, onboarding o cierre debe ejecutar triggers, registrar lessons learned y dejar changelog vivo.
- Los documentos lookup (glosario, diccionario) son la fuente de verdad para naming, triggers y semántica en toda rama/bucket/procedimiento.
- Lessons learned y checklist incremental activos en cada etapa, documentando feedback humano/IA y evolución de la arquitectura.

---

## 3. Procedimiento detallado de implementación y validación V4
### 3.1 Post-import y línea de base
- La importación del árbol de directorios (`platform.zip`) define la línea de base: todo lo que no esté alineado a blueprint/mplan, naming y ruta, debe migrarse o depurarse antes de release.
- Se realiza un barrido literal del árbol, checklist de rutas, assets y triggers activos.

### 3.2 Migración, onboarding y workflows
- Por cada rama, asset o README legacy detectado:
  - Validar naming, ruta y estructura vs blueprint/MPLAN.
  - Regenerar el asset vía workflow actual, integrando OutputTemplate, metadatos YAML, changelog y crossref vivo.
  - Versionar correctamente (sufijo _rw_b_v_4_0.md o nomenclatura establecida).
  - Dejar registro en lessons learned, changelog y checklist incremental.
- Completar onboarding y documentación de workflows en cada bucket (core, ops, packages, library, etc.)

### 3.3 Validación de compliance y testeo
- Ejecutar triggers (`TRG_CONSOLIDATE_TL`, `TRG_AUDIT_LEGACY`, `TRG_AUDIT_TL`, etc.) en cada ciclo, asegurando compliance naming/ruta/WF/OutputTemplate/crossref.
- Automatizar barrido y validación con modelo Codex o IA, registrar lessons learned/feedback tras cada lote.

### 3.4 Cierre, release note y documentación
- Solo se libera la plataforma tras auditar 100% del árbol, migrar todo legacy y consolidar compliance.
- Checklist incremental, changelog, snapshot y release note publicados como documentación final de la V4.
- Blueprint y mplan quedan bloqueados y como fuentes únicas de referencia y compliance para toda operación futura.

---

## 4. Integración IA, aceleradores y feedback vivo
- Utilizar scripts batch y prompts Codex para generación/migración/update masivo de assets, onboarding y reporting.
- Integrar feedback humano/IA tras cada ciclo, documentando lessons learned, gaps, excepciones y oportunidades de mejora.
- Establecer triggers automáticos de validación, registro y reporting por lote de migración o test.

---

## 5. Post-release y ciclo operativo V4
- Solo se permite creación/migración de nuevos assets si cumplen las reglas supremas y pasan auditoría de compliance.
- Todo cambio, excepción o workaround debe quedar registrado y justificado.
- El ciclo PDCA (plan-do-check-act) es mandatorio: feedback y lessons learned alimentan cada iteración.

---

**FIN — Master Plan RwB V4 EXTENDIDO**


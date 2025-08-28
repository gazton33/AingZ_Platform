# [RwB] NAMING TEMPLATE — v1 (Jerarquía Avanzada, Modular, Abreviada)

> Plantilla universal y jerárquica para nombrar cualquier archivo, template, knowledge, log, readme, workflow, backup, glosario, etc. Admite estructura extendida (máxima trazabilidad) y versión abreviada (ID mínima única). Optimizada para RwB, integración CI/CD, y automatización avanzada.

---

## Sintaxis JERÁRQUICA (completa)

```
<RULESET>_<LAYER>_<DOMAIN>_<USERSCOPE>_<MODULE>_<CATEGORY>_<TASK>_<NAME>_<STATE>_<VERSION>_<DATE>.<EXT>
```

- `<RULESET>`: Sistema o estándar principal (`RwB`, `Org`, etc)
- `<LAYER>`: Layer/capa (ej: `INFRA`, `APP`, `DATA`, `CFG`, etc)
- `<DOMAIN>`: Dominio/disciplina (`KNW`, `ENG`, `AI`, etc)
- `<USERSCOPE>`: Privacidad/colaboración (`PR`, `CO`, `CL`)
- `<MODULE>`: Módulo/subsistema (nombre corto)
- `<CATEGORY>`: Macrogrupo funcional/técnico (del glosario)
- `<TASK>`: Tarea, flujo, workflow o tipo (del glosario)
- `<NAME>`: Nombre clave, propósito o descriptor
- `<STATE>`: Estado (`WIP`, `FINAL`, `ARCH`, etc)
- `<VERSION>`: Versión explícita (`vN`, `vN.N`, `YYYYMMDD`, etc)
- `<DATE>`: Fecha o timestamp, opcional para releases (`YYYYMMDD`)
- `<EXT>`: Extensión nativa/estándar (`.md`, `.json`, etc)

---

## Sintaxis ABREVIADA / ID UNICA

- Puedes omitir campos no relevantes/contextuales y dejar solo los necesarios para unicidad y trazabilidad.
- Sugerencia mínima: `<RULESET>_<CATEGORY>_<NAME>_<VER>.<EXT>`

---

## Ejemplos prácticos (completa/abreviada)

- `RwB_APP_KNW_PR_KNS_GLOSARIO_CODE_CORE_WIP_v1_20250722.md` — Glosario code, layer app, knowledge, privado, estado WIP, versión 1, fecha.
- `RwB_DATA_AI_CL_GLOSARIO_TEMPLATE_FINAL_v0.md` — Template de glosario AI en datos colaborativo, final.
- `RwB_DOC_README_PRINCIPAL_v1.md` — README principal de documentación, versión 1.
- `RwB_TMPL_README_HUMAN_ONBOARD_v0.md` — Template de readme humano para onboarding.
- `RwB_TMPL_README_AI_RULESET_v0.md` — Template de readme AI para ruleset.
- `RwB_KNS_CTX_LSWP_v0_20250722.md` — Contexto knowledge, LSWP, versión 0.
 - `rw_b_glosario_code_v_0_core.md` — Glosario abreviado, versión 0, core.
- `RwB_TMPL_WF_MATRIX_VERSUS_v1.md` — Template de matriz versus de workflow.
- `RwB_BK_GLOSARIO_CODE_v0.json` — Backup de glosario code, versión 0.

---

## Reglas y recomendaciones

- Mantener siempre el orden de jerarquía si aplica, pero omitir sin ambigüedad.
- Para templates: siempre anteponer `TMPL` o `TMP` según glosario, seguido de destino (`README`, `DOC`, `WF`, etc).
- Evitar repeticiones de palabras, usar nombres cortos pero descriptivos.
- La convención puede abreviarse si hay unicidad y contexto, pero nunca eliminar versión ni tipo.
- Validar naming con el glosario y registrar cambios importantes en changelog.

---

**FIN NAMING TEMPLATE v1**


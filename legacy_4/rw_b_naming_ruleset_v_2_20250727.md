# [RwB] NAMING RULESET — v2 (2025-07-27)

> Actualización de las reglas de nombrado para todo el repositorio.
> Se basa en los códigos del glosario core (`../kns/glossary/`) y sustituye la versión v1.

---

## 1. Premisas generales
- Emplear siempre los códigos de `rw_b_glosario_code_v_0_core.md` para prefijos y categorías.
- Incluir versión (`vN`) y fecha (`YYYYMMDD`) cuando aplique.
- Nombres cortos y descriptivos; evitar repeticiones.
- Ante dudas, revisar el glosario antes de nombrar un archivo nuevo.

---

## 2. Sintaxis recomendada (jerárquica)

```
<RULESET>_<CATEGORY>_<TASK>_<NAME>_<STATE>_<VERSION>_<DATE>.<EXT>
```

- `RULESET`: código principal (ej. `RWB`, `RULE`).
- `CATEGORY` y `TASK`: según las tablas "Workflow", "Knowledge" o "Documentation".
- `STATE`: `WIP`, `FINAL`, `ARCH`, etc.

Ejemplo:
```
rwb_wf_auditoria_legacy_v_3_20250727.md
```

---

## 3. Alias abreviado

Formato reducido permitido si existe contexto suficiente:
```
<RULESET>_<NAME>_<VER>.<EXT>
```

---

## 4. Validación
- Verificar en el glosario que los códigos utilizados sean válidos.
- Registrar en `Learn/chglog` cualquier modificación o excepción.

---

**FIN NAMING RULESET v2**

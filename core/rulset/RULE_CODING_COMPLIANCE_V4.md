# RULE_CODING_COMPLIANCE_V4 (draft)

## 1. Lineamientos de estilo
- Adoptar convenciones PEP8 para Python.
- Incluir docstrings claros en funciones y módulos.
- Favorecer estructuras modulares y reutilizables.
- Nombrar commits y ramas siguiendo un formato descriptivo.

## 2. Lineamientos de pruebas
- Toda nueva funcionalidad debe acompañarse de pruebas `pytest`.
- Ejecutar `pytest` localmente antes de cada commit.
- Validar casos edge y comportamiento esperado ante errores.

## 3. Validación dinámica de crossrefs
- Mantener referencias vivas a archivos críticos en todos los README.
- Después de mover o crear archivos, correr `python ops/update_crossrefs.py`.
- Verificar los cambios generados en `README.md`, `ops/changelog.md` y `ops/lessons_learned.md`.


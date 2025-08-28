# rw_b_naming_convention — v1

> **STATUS:** `ACTUALIZADO`
> **Última actualización:** 2025-08-02 | Autor: ChatGPT

---

## 1. Convención general
- Usa `snake_case` para nombres de archivos y carpetas.
- Reserva `UPPER_CASE` únicamente para etapas del pipeline:
  `LEGACY`, `TMP`, `MIG`, `CORE`, `bk_temp`.

## 2. Ejemplos
| Tipo      | Correcto          | Incorrecto        |
|-----------|-------------------|-------------------|
| Script    | `my_script.py`    | `MyScript.py`     |
| Carpeta   | `data_files/`     | `DataFiles/`      |
| Etapa     | `bk_temp/`         | `backup/`         |

Esta guía aplica a nuevas incorporaciones y ayuda a mantener
coherencia en el repositorio. Las rutas heredadas se ajustarán
progresivamente conforme se actualicen.

# MTX — README v1

> **STATUS:** `ACTUALIZADO`
> **Última actualización:** 2025-08-02 | Autor: ChatGPT

---

## 1. Resumen
Descripción pendiente.

## 2. Snapshots / Contexto
- Carpeta de snapshots relacionada: [../../../bk_temp/](../../../bk_temp/)
- Enlaces a versiones relevantes o backups IA: [../../../backup/](../../../backup/)

## 3. Crossref y Mapping
- **Referencia ascendente:** `[../]`
- **Referencias laterales:** [../mplan/], [../rulset/], [../template/]
- **Buckets destino típicos:** `[../DESTINO/]`
- **Crossref central:** [Mapa Global](../../../core/data/crossref_mapping_buckets_aingz_platform_v_1_20250731.md)
- **Flujos/Pipelines relevantes:** [../../../infra/pipelines/README.md](../../../infra/pipelines/README.md)

## 4. Precedencia en el Árbol de Directorios
```text
AingZ_Platform_main/
└── mig/
    └── data/
        └── mtx/
```

## 4.1 Procedencia en el Árbol de Directorios
```text
mtx/
└── (sin subdirectorios)
```

## 5. Pipeline y Workflows (Ciclo de Vida)
Describe los pasos clave del ciclo de vida para los archivos de este bucket:
1. **Ingreso / LEGACY o TMP:** [../../../legacy/](../../../legacy/) o [../../../tmp_staging/](../../../tmp_staging/)
2. **Staging / MIG:** [../../](../../)
3. **Consolidación / CORE:** [../../../core/](../../../core/)
4. **bk_temp / Eliminación:** [../../../backup/](../../../backup/) y/o [../../../bk_temp/](../../../bk_temp/)

## 6. Siguiente etapa
Ruta correspondiente en la siguiente etapa del ciclo de vida: [../../../core/data/mtx/](../../../core/data/mtx/)

Ajustar enlaces de acuerdo al pipeline oficial y etapas de `LEGACY→TMP→MIG→CORE→bk_temp`.

---

Completar todos los campos con links activos una vez creada la estructura real.


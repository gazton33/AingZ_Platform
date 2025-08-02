# LEGACY — README v1

> **STATUS:** `PENDIENTE`
> **Última actualización:** 2025-08-02 | Autor: Gastón Zelechower

---

## 1. Resumen
Fuentes legadas pendientes de migración.

## 2. Snapshots / Contexto
- Carpeta de snapshots relacionada: `[./SNAPSHOTS/]` (ajustar si aplica)
- Enlaces a versiones relevantes o backups IA: `[./SNAPSHOTS_CTX/]` (opcional)

## 3. Crossref y Mapping
- **Referencia ascendente:** `[../]`
- **Referencias laterales:** [../BACKUP/], [../apps/], [../backup/], [../conectors/], [../core/], [../infra/], [../log/], [../mig/], [../packages/], [../scripts/], [../tmp_staging/]
- **Buckets destino típicos:** `[../DESTINO/]`
- **Crossref central:** `[Mapa Global](../DOC/MPLN/crossref_global.md)`
- **Flujos/Pipelines relevantes:** `[../WF/pipeline_legacy.md]`, `[../PIPELINES/pipeline_legacy.md]`

## 4. Precedencia en el Árbol de Directorios
```text
AingZ_Platform_main/
└── legacy/
```

## 4.1 Procedencia en el Árbol de Directorios
```text
legacy/
├── data/
├── doc/
├── kns/
├── log/
├── scr/
└── wf/
```

## 5. Pipeline y Workflows (Ciclo de Vida)
Describe los pasos clave del ciclo de vida para los archivos de este bucket:
1. **Ingreso / [LEGACY](./) o [TMP](../tmp_staging/):** `[../WF/wf_ingreso_legacy.md]`
2. **Staging / [MIG](../mig/):** `[../WF/wf_staging_legacy.md]`
3. **Consolidación / [CORE](../core/):** `[../WF/wf_consolidacion_legacy.md]`
4. **Backup / Eliminación / [BACKUP](../backup/) o [BACKUP final](../BACKUP/):** `[../WF/wf_backup_legacy.md]`

Ajustar enlaces de acuerdo al pipeline oficial y etapas de `LEGACY→TMP→MIG→CORE→BACKUP`.

---

Completar todos los campos con links activos una vez creada la estructura real.


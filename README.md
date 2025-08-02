# AingZ_Platform_main — README v1

> **STATUS:** `PENDIENTE`
> **Última actualización:** 2025-08-02 | Autor: Gastón Zelechower

---

## 1. Resumen
Bucket raíz que organiza los módulos principales de la plataforma.

## 2. Snapshots / Contexto
- Carpeta de snapshots relacionada: `[./SNAPSHOTS/]` (ajustar si aplica)
- Enlaces a versiones relevantes o backups IA: `[./SNAPSHOTS_CTX/]` (opcional)

## 3. Crossref y Mapping
- **Referencia ascendente:** `[../]`
- **Referencias laterales:** [./BACKUP/], [./apps/], [./backup/], [./conectors/], [./core/], [./infra/], [./legacy/], [./log/], [./mig/], [./packages/], [./scripts/], [./tmp_staging/]
- **Buckets destino típicos:** `[../DESTINO/]`
- **Crossref central:** `[Mapa Global](../DOC/MPLN/crossref_global.md)`
- **Flujos/Pipelines relevantes:** `[../WF/pipeline_AingZ_Platform_main.md]`, `[../PIPELINES/pipeline_AingZ_Platform_main.md]`

## 4. Precedencia en el Árbol de Directorios
```text
AingZ_Platform_main/
```

## 4.1 Procedencia en el Árbol de Directorios
```text
AingZ_Platform_main/
├── BACKUP/
├── apps/
├── backup/
├── conectors/
├── core/
├── infra/
├── legacy/
├── log/
├── mig/
├── packages/
├── scripts/
└── tmp_staging/
```

## 5. Pipeline y Workflows (Ciclo de Vida)
Describe los pasos clave del ciclo de vida para los archivos de este bucket:
1. **Ingreso** — [LEGACY](./legacy/) o [TMP](./tmp_staging/) `[../WF/wf_ingreso_AingZ_Platform_main.md]`
2. **Staging** — [MIG](./mig/) `[../WF/wf_staging_AingZ_Platform_main.md]`
3. **Consolidación** — [CORE](./core/) `[../WF/wf_consolidacion_AingZ_Platform_main.md]`
4. **Backup / Eliminación** — [BACKUP](./backup/) y/o [BACKUP final](./BACKUP/) `[../WF/wf_backup_AingZ_Platform_main.md]`

Ajustar enlaces de acuerdo al pipeline oficial y etapas de `LEGACY→TMP→MIG→CORE→BACKUP`.

---

Completar todos los campos con links activos una vez creada la estructura real.


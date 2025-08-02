# LOG — README v1

> **STATUS:** `PENDIENTE`
> **Última actualización:** 2025-08-02 | Autor: Gastón Zelechower

---

## 1. Resumen
Registros y bitácoras operativas.

## 2. Snapshots / Contexto
- Carpeta de snapshots relacionada: `[./SNAPSHOTS/]` (ajustar si aplica)
- Enlaces a versiones relevantes o backups IA: `[./SNAPSHOTS_CTX/]` (opcional)

## 3. Crossref y Mapping
- **Referencia ascendente:** `[../]`
- **Referencias laterales:** [../BACKUP/], [../apps/], [../backup/], [../conectors/], [../core/], [../infra/], [../legacy/], [../mig/], [../packages/], [../scripts/], [../tmp_staging/]
- **Buckets destino típicos:** `[../DESTINO/]`
- **Crossref central:** `[Mapa Global](../DOC/MPLN/crossref_global.md)`
- **Flujos/Pipelines relevantes:** `[../WF/pipeline_log.md]`, `[../PIPELINES/pipeline_log.md]`

## 4. Precedencia en el Árbol de Directorios
```text
AingZ_Platform_main/
└── log/
```

## 4.1 Procedencia en el Árbol de Directorios
```text
log/
├── bitacoras/
├── changlog/
└── trazabilidad total/
```

## 5. Pipeline y Workflows (Ciclo de Vida)
Describe los pasos clave del ciclo de vida para los archivos de este bucket:
1. **Ingreso / LEGACY o TMP:** `[../WF/wf_ingreso_log.md]`
2. **Staging / MIG:** `[../WF/wf_staging_log.md]`
3. **Consolidación / CORE:** `[../WF/wf_consolidacion_log.md]`
4. **Backup / Eliminación:** `[../WF/wf_backup_log.md]`

Ajustar enlaces de acuerdo al pipeline oficial y etapas de `LEGACY→TMP→MIG→CORE→BACKUP`.

---

Completar todos los campos con links activos una vez creada la estructura real.


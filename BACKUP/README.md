# BACKUP — README v1

> **STATUS:** `PENDIENTE`
> **Última actualización:** 2025-08-02 | Autor: Gastón Zelechower

---

## 1. Resumen
Almacén de respaldo final y archivo definitivo de la plataforma.

## 2. Snapshots / Contexto
- Carpeta de snapshots relacionada: `[./SNAPSHOTS/]` (ajustar si aplica)
- Enlaces a versiones relevantes o backups IA: `[./SNAPSHOTS_CTX/]` (opcional)

## 3. Crossref y Mapping
- **Referencia ascendente:** `[../]`
- **Referencias laterales:** [../backup/], [../apps/], [../connectors/], [../core/], [../infra/], [../legacy/], [../log/], [../mig/], [../packages/], [../scripts/], [../tmp_staging/]
- **Buckets destino típicos:** `[../DESTINO/]`
- **Crossref central:** `[Mapa Global](../DOC/MPLN/crossref_global.md)`
- **Flujos/Pipelines relevantes:** `[../WF/pipeline_BACKUP_final.md]`, `[../PIPELINES/pipeline_BACKUP_final.md]`

## 4. Precedencia en el Árbol de Directorios
```text
AingZ_Platform_main/
└── BACKUP/
```

## 4.1 Procedencia en el Árbol de Directorios
```text
BACKUP/
├── AI/
├── EXT/
└── INT/
```

## 5. Pipeline y Workflows (Ciclo de Vida)
Describe los pasos clave del ciclo de vida para los archivos de este bucket:
1. **Backup final / Eliminación:** `[../WF/wf_backup_final.md]`

---
Completar todos los campos con links activos una vez creada la estructura real.

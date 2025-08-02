# CORE — README v1

> **STATUS:** `PENDIENTE`
> **Última actualización:** 2025-08-02 | Autor: Gastón Zelechower

---

## 1. Resumen
Almacén consolidado de datos y recursos centrales.

## 2. Snapshots / Contexto
- Carpeta de snapshots relacionada: `[./SNAPSHOTS/]` (ajustar si aplica)
- Enlaces a versiones relevantes o backups IA: `[./SNAPSHOTS_CTX/]` (opcional)

## 3. Crossref y Mapping
- **Referencia ascendente:** `[../]`
- **Referencias laterales:** [../BACKUP/], [../apps/], [../backup/], [../conectors/], [../infra/], [../legacy/], [../log/], [../mig/], [../packages/], [../scripts/], [../tmp_staging/]
- **Buckets destino típicos:** `[../DESTINO/]`
- **Crossref central:** `[Mapa Global](../DOC/MPLN/crossref_global.md)`
- **Flujos/Pipelines relevantes:** `[../WF/pipeline_core.md]`, `[../PIPELINES/pipeline_core.md]`

## 4. Precedencia en el Árbol de Directorios
```text
AingZ_Platform_main/
└── core/
```

## 4.1 Procedencia en el Árbol de Directorios
```text
core/
├── data/
├── doc/
├── kns/
├── log/
├── scr/
└── wf/
```

## 5. Pipeline y Workflows (Ciclo de Vida)
Describe los pasos clave del ciclo de vida para los archivos de este bucket:
1. **Ingreso / LEGACY o TMP:** `[../WF/wf_ingreso_core.md]`
2. **Staging / MIG:** `[../WF/wf_staging_core.md]`
3. **Consolidación / CORE:** `[../WF/wf_consolidacion_core.md]`
4. **Backup / Eliminación:** `[../WF/wf_backup_core.md]`

Ajustar enlaces de acuerdo al pipeline oficial y etapas de `LEGACY→TMP→MIG→CORE→BACKUP`.

### Enlaces directos a cada etapa del ciclo

- [LEGACY](../legacy/)
- [TMP_STAGING](../tmp_staging/)
- [MIG](../mig/)
- [CORE](./)
- [BACKUP](../backup/) / [BACKUP final](../BACKUP/)

---

Completar todos los campos con links activos una vez creada la estructura real.


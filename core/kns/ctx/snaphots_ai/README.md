# [NOMBRE_BUCKET] — README Template v1

> **STATUS:** `PENDIENTE`
> **Última actualización:** YYYY-MM-DD | Autor: <Autor>

---

## 1. Resumen
Breve descripción del propósito y alcance de este bucket/carpeta. Completar según corresponda.

## 2. Snapshots / Contexto
- Carpeta de snapshots relacionada: `[./SNAPSHOTS/]` (ajustar si aplica)
- Enlaces a versiones relevantes o backups IA: `[./SNAPSHOTS_CTX/]` (opcional)

## 3. Crossref y Mapping
- **Referencia ascendente:** `[../]`
- **Referencias laterales:** `[./BUCKET_LATERAL1/]`, `[./BUCKET_LATERAL2/]`
- **Buckets destino típicos:** `[../DESTINO/]`
- **Crossref central:** `[Mapa Global](../DOC/MPLN/crossref_global.md)`
- **Flujos/Pipelines relevantes:** `[../WF/pipeline_BUCKET.md]`, `[../PIPELINES/pipeline_BUCKET.md]`

## 4. Precedencia en el Árbol de Directorios
Indicar la ubicación exacta dentro de `AingZ_Platform_main/` usando un esquema tipo:

```text
AingZ_Platform_main/
└── RUTA/AL/B UCKET/
```

## 5. Pipeline y Workflows (Ciclo de Vida)
Describe los pasos clave del ciclo de vida para los archivos de este bucket:
1. **Ingreso / LEGACY o TMP:** `[../WF/wf_ingreso_BUCKET.md]`
2. **Staging / MIG:** `[../WF/wf_staging_BUCKET.md]`
3. **Consolidación / CORE:** `[../WF/wf_consolidacion_BUCKET.md]`
4. **Backup / Eliminación:** `[../WF/wf_backup_BUCKET.md]`

Ajustar enlaces de acuerdo al pipeline oficial y etapas de `LEGACY→TMP→MIG→CORE→BACKUP`.

---

Completar todos los campos con links activos una vez creada la estructura real.


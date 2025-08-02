# 🗂️ DIR\_ARCH\_PLAN — v5 (Integración Matrix RwB, 2025-07-31)

> **Blueprint extendido con integración explícita de todos los conceptos de la Matrix de Clasificación de Activos (SRC·STG·ROLE)**
>
> **Cambios respecto a v4 marcados en *****color***** (🟩 agregado, 🟦 cambiado, 🟥 eliminado).**

---

## 1. Blueprint raíz (v5)

```text
Repo Root /
├── WF/                    # Workflows activos (D01)
│   └── PURG/              # Workflows legacy
├── DOC/                   # Documentación, blueprints, onboarding
│   ├── MPLN/              # MasterPlan & Blueprints (D03)
│   └── ONBRD/             # Onboarding y welcome
├── KNS/                   # Knowledge base modular (I01)
│   └── LEARN/             # Lessons learned, training, drafts
│   └── TL/                # Entrenamiento/feedback (ROLE=TL)
│   └── 🟩 EXT_COM/         # 🟩 Training/learning de comunidad externa (nuevo bucket Matrix)
│   └── 🟩 EXT_OFF/         # 🟩 Training/learning externo oficial (nuevo bucket Matrix)
├── AUDIT_LIGHT/           # Informes ligeros de auditoría y referencias rápidas
├── SCR/                   # Scripts globales (G01)
├── DATA/                  # Matrices, datasets, CSV/Parquet
├── LOG/                   # Logs, changelogs, bitácoras (E01)
│   └── AUDT/              # Audit logs pesados (E06)
├── BACKUP/                # Snapshots y BLN (B13)
│   └── 🟩 INT/             # 🟩 Backups internos (Matrix)
│   └── 🟩 EXT_OFF/         # 🟩 Backups externos oficiales
│   └── 🟩 EXT_COM/         # 🟩 Backups comunidad externa
│   └── 🟩 AI/              # 🟩 Backups IA
├── PURGATORIO/            # Obsoletos/legacy (B15)
│   └── LEGACY/            # Activos antiguos/externos para migración
│   └── 🟩 AI/              # 🟩 Purgatorio IA (Matrix)
├── TMP/                   # Temp files, scratchpads, procesamiento previo consolidación
│   └── 🟩 AI/              # 🟩 Drafts y outputs temporales IA
├── MIG/                   # Outputs de migración literal, staging previo a activos finales
├── 🟩 CORE/                # 🟩 Consolidado principal (ej: INT_LEG·AC·CORE)
│   └── 🟩 INT_LEG/         # 🟩 Consolidado de legacy interno
```

---

## 2. Tabla extendida de buckets y alineación Matrix

| ID    | Dir                  | SRC     | STG   | ROLE | Propósito/Procedimiento Matrix      | Cambios v5      |
| ----- | -------------------- | ------- | ----- | ---- | ----------------------------------- | --------------- |
| R01   | `/WF`                | INT     | AC    | CORE | Workflows activos                   | -               |
| R02   | `/DOC`               | INT/EXT | AC    | BLUE | Documentación y blueprints          | -               |
| R03   | `/KNS/LEARN`         | INT     | DR    | TL   | Lessons, drafts, feedback           | -               |
| R04   | `/KNS/TL`            | INT/AI  | TL    | TL   | Training interno y outputs IA       | -               |
| 🟩R05 | `/KNS/EXT_COM`       | EXT-COM | AC/TL | TL   | Training comunidad externa (Matrix) | 🟩 nuevo        |
| 🟩R06 | `/KNS/EXT_OFF`       | EXT-OFF | AC/TL | TL   | Training externo oficial (Matrix)   | 🟩 nuevo        |
| R07   | `/AUDIT_LIGHT`       | INT/EXT | AU    | REF  | Auditoría liviana                   | -               |
| R08   | `/SCR`               | INT     | AC    | CORE | Scripts globales                    | -               |
| R09   | `/DATA`              | INT/EXT | AC    | REF  | Datasets, matrices, etc.            | -               |
| R10   | `/LOG`               | INT     | AC    | LOG  | Logs generales                      | -               |
| R11   | `/LOG/AUDT`          | INT     | AU    | LOG  | Logs de auditoría pesada            | -               |
| R12   | `/BACKUP/INT`        | INT     | BK    | CORE | Snapshots internos                  | 🟩 split Matrix |
| 🟩R13 | `/BACKUP/EXT_OFF`    | EXT-OFF | BK    | CORE | Snapshots externos oficiales        | 🟩 nuevo        |
| 🟩R14 | `/BACKUP/EXT_COM`    | EXT-COM | BK    | REF  | Snapshots comunidad externa         | 🟩 nuevo        |
| 🟩R15 | `/BACKUP/AI`         | AI      | BK    | TL   | Snapshots/backup outputs IA         | 🟩 nuevo        |
| R16   | `/PURGATORIO/LEGACY` | INT-LEG | PG    | CORE | Purgatorio legacy interno           | -               |
| 🟩R17 | `/PURGATORIO/AI`     | AI      | PG    | TL   | Purgatorio IA                       | 🟩 nuevo        |
| R18   | `/TMP`               | INT/AI  | DR    | TL   | Archivos temporales y drafts        | -               |
| 🟩R19 | `/TMP/AI`            | AI      | DR    | TL   | Drafts IA                           | 🟩 nuevo        |
| 🟩R20 | `/CORE/INT_LEG`      | INT-LEG | AC    | CORE | Consolidado legacy interno          | 🟩 nuevo        |

---

## 3. Reglas adicionales y recomendaciones (v5)

- Todo asset debe tener su código `SRC·STG·ROLE` y vivir en el bucket según Matrix.
- README de cada bucket debe mostrar tabla versus Matrix y triggers asociados.
- Triggers y flujos entre buckets ahora referencian directamente procedimiento Matrix.
- Naming/metadata reforzado: todo archivo incluye código Matrix como prefijo/sufijo.
- Workflows actualizados: agregados triggers para training comunitario, outputs IA y purgatorio IA.

---

## 4. Diferencias clave v5 vs v4

- 🟩 Buckets nuevos: `/KNS/EXT_COM`, `/KNS/EXT_OFF`, `/BACKUP/EXT_COM`, `/BACKUP/EXT_OFF`, `/BACKUP/AI`, `/PURGATORIO/AI`, `/TMP/AI`, `/CORE/INT_LEG`.
- 🟩 Tabla de buckets ahora referencia explícita a combinaciones Matrix y procedimiento.
- 🟩 Flujos de integración IA y training comunitario referenciados en triggers y workflows.
- 🟩 Naming reforzado y obligatorio con código Matrix en toda la infraestructura.

---

**FIN — DIR\_ARCH\_PLAN v5 Integración Matrix**


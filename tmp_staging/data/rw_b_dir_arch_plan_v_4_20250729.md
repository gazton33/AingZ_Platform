# 🗂️ [RwB] DIR\_ARCH\_PLAN — v4 (CORE, 2025-07-29)

> **Blueprint definitivo — integra la matriz de clasificación de assets y los nuevos flujos de procedimientos por voz.**\
> **Referencia cruzada:** Este plan debe usarse junto al *Assets Classification Matrix v1*, *WF\_RELEV\_HILO\_ASSETS v1*, *Glosario CODE v2*, y *CONCEPTOS CICLO DE VIDA v1*.\
> **Alineado a modelos OpenAI 4.1+ para máxima capacidad de contexto, dictado y workflows iterativos.**

---

## 🔝 Instrucciones actualizadas

1. Antes de crear, mover o auditar un archivo, revisa el mapping y las rutas en esta arquitectura.
2. El código de cada asset debe seguir el formato `SRC·STG·ROLE` según la matriz, y ubicarse en el bucket correcto.
3. Todos los procedimientos de dictado por voz, relevamiento, auditoría, consolidado y migración deben trazar outputs aquí.
4. Cambios relevantes exigen update en README, CHGLOG, y crossref con Glosario v2.
5. Repositorio de trabajo soporta análisis por IA (OpenAI 4.1+) para dictado, feedback, entrenamiento y auditoría iterativa.

---

## 📦 Árbol de directorios (unificado y ampliado)

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
├── AUDIT_LIGHT/           # Informes ligeros de auditoría y referencias rápidas
├── SCR/                   # Scripts globales (G01)
├── DATA/                  # Matrices, datasets, CSV/Parquet
├── LOG/                   # Logs, changelogs, bitácoras (E01)
│   └── AUDT/              # Audit logs pesados (E06)
├── BACKUP/                # Snapshots y BLN (B13)
├── PURGATORIO/            # Obsoletos/legacy (B15)
│   └── LEGACY/            # Activos antiguos/externos para migración
├── TMP/                   # Temp files, scratchpads, procesamiento previo consolidación
└── MIG/                   # Outputs de migración literal, staging previo a activos finales
```

---

## A. Root Directories Mapping (extendido)

| ID  | Dir                  | ROLE      | CODE Área | Propósito/Ejemplo                                                           | Referencia      |
| --- | -------------------- | --------- | --------- | --------------------------------------------------------------------------- | --------------- |
| R01 | `/WF`                | CORE      | WF        | Workflows activos, scripts `.md` + `SCR`.                                   | D01             |
| R02 | `/DOC`               | CORE/BLUE | DOC       | Documentación, blueprints, onboarding, master plans.                        | F01/F02/D03/D19 |
| R03 | `/KNS`               | CORE/REF  | KNS       | Núcleo conocimientos modulares, registros auditados, insights.              | I01/I05/I08     |
| R04 | `/KNS/LEARN`         | TL        | LEARN     | Lessons learned, feedback, draft de aprendizajes.                           | I07/TL          |
| R05 | `/KNS/TL`            | TL        | TL        | Training/feedback intermedio (outputs de workflows, tuning, voice dictado). | TL/AI/INT       |
| R06 | `/AUDIT_LIGHT`       | REF/AU    | AUDT-L    | Auditorías livianas, informes rápidos, referencias.                         | AU/REF          |
| R07 | `/SCR`               | CORE      | SCR       | Scripts globales Python/Shell.                                              | G01             |
| R08 | `/DATA`              | CORE      | MTR       | Matrices, datasets, CSV/Parquet.                                            | H01             |
| R09 | `/LOG`               | CORE      | LOG       | Logs, changelogs, bitácoras.                                                | E01             |
| R10 | `/LOG/AUDT`          | AU        | ADT       | Audit logs detallados (pesados).                                            | E06             |
| R11 | `/BACKUP`            | BK        | BK        | Snapshots BLN y backups comprimidos.                                        | B13             |
| R12 | `/PURGATORIO`        | PG        | PURG      | Stage de obsoletos antes de eliminación o migración legacy.                 | B15             |
| R13 | `/PURGATORIO/LEGACY` | LG        | LEGACY    | Activos antiguos/externos para migración.                                   | LEGACY          |
| R14 | `/TMP`               | TEMP      | TMP       | Archivos temporales y scratchpad de dictado/auditoría.                      | TMP             |
| R15 | `/MIG`               | MIG       | MIG       | Outputs de migración literal, staging previo a activos finales.             | MIG             |

---

## B. Convenciones y patrones (procedimientos voz y feedback)

| Carpeta              | Uso típico/procedimiento por voz                        | Ejemplo output                 |
| -------------------- | ------------------------------------------------------- | ------------------------------ |
| `/KNS/TL`            | Dictado, resultados tuning, training AI, logs feedback. | `INT·TL·DR_ai_tuning_draft.md` |
| `/AUDIT_LIGHT`       | Auditoría por voz, revisión express, insights, links.   | `EXT-OFF·AU·REF_audit_ISO.md`  |
| `/TMP`               | Scratchpad mientras dictas, resultados intermedios.     | `tmp_interview202507.md`       |
| `/MIG`               | Migración literal desde consolidado, inputs validados.  | `mig_DOC_v1_202507.md`         |
| `/PURGATORIO/LEGACY` | Import legacy, fuentes para análisis, migrar a ACTV.    | `legacy_PROC_manuales/`        |

---

## C. Integración con flujos iterativos y dictado

- Workflows de relevamiento, auditoría y migración usan rutas específicas y separan roles de carpeta para outputs intermedios vs activos finales.
- El dictado por voz, feedback tuning y entrenamiento IA deben guardar outputs siempre en `/KNS/TL` o `/TMP` (según si es training o solo scratchpad).
- Auditorías express guardan outputs livianos en `/AUDIT_LIGHT` para posterior consolidado o migración.
- Migraciones literales (copias 100% textuales y auditadas) viven en `/MIG` antes de pasar a carpetas ACTV.
- Purgatorio/Legacy se reserva para activos sin uso activo, esperando auditoría o migración posterior.

---

## D. Ejemplo de ciclo iterativo (workflow dictado+IA+consolidado)

1. Dictado, tuning o feedback → `/KNS/TL` o `/TMP`
2. Auditoría rápida → `/AUDIT_LIGHT`
3. Consolidado/manual mapping → `/DOC` o `/KNS`
4. Migración literal → `/MIG`
5. Auditoría final → `/LOG/AUDT`
6. Si se archiva, pasa a `/PURGATORIO` o `/BACKUP`

---

## 📑 Changelog

- 2025-07-29 · **v4** · Blueprint extendido para soportar dictado por voz, matriz de assets, entrenamiento IA y nuevos buckets.

## ℹ️ Metadatos

| Campo        | Valor                           |
| ------------ | ------------------------------- |
| Versión      | v4                              |
| Fecha        | 2025-07-29                      |
| Matrix ref   | Assets Classification Matrix v1 |
| Glosario ref | v2                              |

---

### Firma

> Gastón Zelechower · OpenAI o3 — Ruleset RWB Universal

---

**FIN — DIR\_ARCH\_PLAN v4**


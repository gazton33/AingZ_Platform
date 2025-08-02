# 🌐 CTX\_O3\_RwB\_Total\_20250731 (Optimizado para modelo o3)

> **Contexto máximo condensado, literal y referenciado para el setup y operaciones IA RwB bajo arquitectura Monorepo Modular v5, blueprint, Matrix, workflows y naming universal.** **Target:** modelo o3, límite 200K tokens (ventana contexto vivo), idioma nativo IA, chunking y naming RwB. **Fuente:** Barrido literal y síntesis de todos los adjuntos clave del proyecto (2025-07-31).

---

## 1. PROPÓSITO Y SCOPE

- Unificar el contexto necesario para auditoría, setup, integración y desarrollo de activos en el repositorio RwB.
- Asegurar alineación entre blueprint, Matrix, glosario, workflows y snapshots optimizados según límite de tokens del modelo objetivo (o3).
- Servir como input universal para onboarding, análisis, consolidación y auditoría incremental por IA.

---

## 2. PRINCIPIOS Y REGLAS BASE

- Arquitectura Monorepo Modular: cada package independiente, buckets y recursos compartidos (`WF/`, `DOC/`, `KNS/`, `SCR/`, `DATA/`, `LOG/`, `BACKUP/`, `TMP/`, `MIG/`).
- Naming obligatorio `SRC·STG·ROLE` (ver Matrix y glosario).
- Flujos: LEGACY→STAGING→ACTIVO/CORE→BACKUP/ELIMINACIÓN.
- Prohibido citar legacy en activos, consolidar y eliminar residuos tras merge.
- Workflows y scripts siempre alineados a arquitectura y límites de tokens IA.

---

## 3. BLUEPRINT ARQUITECTÓNICO (DIR\_ARCH\_PLAN v5)

```text
Repo Root /
├── packages/                  # Paquetes independientes (src/tests/docs)
├── WF/                       # Workflows globales
├── DOC/                      # Documentación, blueprints, onboarding
│   ├── MPLN/                 # MasterPlan & Blueprints
│   └── ONBRD/                # Onboarding
├── KNS/                      # Knowledge base modular
│   ├── LEARN/                # Lessons learned, training
│   ├── TL/                   # Outputs training IA, dictado, tuning
│   ├── EXT_COM/              # Training comunidad externa
│   └── EXT_OFF/              # Training externo oficial
├── AUDIT_LIGHT/              # Auditorías ligeras
├── SCR/                      # Scripts globales
├── DATA/                     # Matrices y datasets
├── LOG/                      # Logs y changelogs
│   └── AUDT/                 # Audit logs pesados
├── BACKUP/                   # Snapshots/Backups (INT/EXT_COM/EXT_OFF/AI)
├── PURGATORIO/               # Staging de legacy, obsoletos
│   ├── LEGACY/               # Zona exclusiva de activos antiguos/externos
│   └── AI/                   # Purgatorio IA (Matrix)
├── TMP/                      # Archivos temporales, drafts
│   └── AI/                   # Drafts IA
├── MIG/                      # Outputs de migración literal
├── CORE/                     # Consolidado principal (ej. INT_LEG·AC·CORE)
│   └── INT_LEG/              # Consolidado legacy interno
└── SNAPSHOTS_CTX/            # Snapshots optimizados por modelo IA
    └── o3/                   # Slices y contextos preparados p/modelo o3
```

- **Convención:** cada asset/bucket mapea a la Matrix (SRC·STG·ROLE) y al glosario CODE v2.
- README de cada bucket incluye tabla versus Matrix, triggers, y naming de referencia.

---

## 4. CICLO DE VIDA DE ASSET (RESUMEN)

1. **Ingreso:** LEGACY o creación en TMP/STAGING.
2. **Auditoría y procesamiento:** En STAGING/TMP según workflow, naming provisional.
3. **Validación QA:** Checklist, feedback, triggers (ver diccionario y glosario).
4. **Consolidación:** Movimiento a CORE/ASSETS/KNS/ según naturaleza y rol.
5. **Backup/Eliminación:** Snapshots en BACKUP si aplica, eliminación física tras merge.

- **LEGACY:** zona cuarentena, todo archivo pendiente, sólo usable tras migración y QA.
- **STAGING:** todo asset en revisión, testing o feedback, prohibido mover a activos sin cumplir QA y naming RwB.
- **CORE/ASSETS/KNS:** solo activos validados, versionados y referenciados.
- **BACKUP:** compresión solo para externos o por requerimiento legal.

---

## 5. REGLAS DE NAMING Y MATRIZ SRC·STG·ROLE

- Cada archivo, script, doc, dataset, workflow, snapshot: prefijo/sufijo Matrix (`SRC·STG·ROLE_Nombre[_VER].ext`).
- Ejemplo: `INT·AC·CORE_blueprint_infra_v2.md`, `EXT-OFF·AU·REF_audit_ISO.md`.
- Naming y metadata reforzados (fecha, fuente, coverage, tokens usados en snapshots IA).

---

## 6. LÍMITES DE CONTEXTO Y OPTIMIZACIÓN IA

- **o3:** Máx. 200,000 tokens en contexto vivo (\~150K palabras, salida máx. 100K tokens).
- Todo input IA: usar sólo insights/slices/snapshots curados, nunca full files ni bulk data.
- Cada snapshot debe registrar modelo, tokens, coverage y fecha.
- Carpeta `/SNAPSHOTS_CTX/o3/` centraliza contextos optimizados para este modelo.

---

## 7. WORKFLOWS Y CHECKLISTS OBLIGATORIOS

- **Checklists activos** (QA, migración, feedback, naming): todos versionados y referenciados en LOG/CHG.
- **Workflows activos:** consolidación, migración legacy, dictado IA, onboarding, training/feedback iterativo, auditoría.
- Todos los outputs de workflows deben seguir el naming y rutas Matrix; todo cambio o integración se registra en logs y changelog principal.

---

## 8. INTEGRACIÓN CONECTORES Y APPS EXTERNAS

- Conectores de plataforma (`AingZ_Platform`): Draw\.io, Mermaid, Obsidian, Notion API, LangChain, n8n, Airbyte, Zapier, Slack-GitHub, etc.
- Naming y registro estandarizado: `CNX.<LAYER>.<ROLE>.<tool>[.<qualifier>]`.
- Matriz comparativa en `/DATA/` y checklist para onboarding/configuración.

---

## 9. GLOSARIO Y DICCIONARIO CODE/TRIGGERS

- Referenciar siempre el Glosario CODE v2 y Diccionario Code\_Triggers v2 como fuente primaria para naming, semántica, triggers y prompts estructurados.
- Códigos críticos: RULE, LITW, RWB, CFG, PKG, BLN, CTX, WF, MPLN, CHK, AUDT, LOG, TL, KNS, LEARN, MIG, TMP, ACTV, PURG, LEGACY, etc.

---

## 10. FEEDBACK, LEARN Y CONTEXTO VIVO

- Infraestructura lista para feedback iterativo IA/humano: cada learning/feedback/draft versionado en KNS/LEARN/TL.
- Snapshots y feedback listos para reinyectar contexto y aprendizaje incremental, conforme ciclos de mejora y actualización del repo.
- Cada snapshot de contexto vivo debe cubrir: blueprint, matriz, glosario, workflows activos, checklist, logs, triggers, naming y notas de feedback.

---

## 11. NOTAS Y CHECKLIST DE COBERTURA (BARRIDO\_LITERAL)

- ¿Blueprint, Matrix y Glosario referenciados y actualizados?
- ¿Flujo de LEGACY→STAGING→ACTIVO/CORE→BACKUP/ELIMINACIÓN operativo y sin residuos?
- ¿Naming universal y triggers integrados?
- ¿Snapshots y contextos curados bajo límite tokens?
- ¿Workflows y logs actualizados y trazables?
- ¿Integración conectores externos documentada?
- ¿Notas y feedback registrados en KNS/LEARN/TL?
- ¿README y CHGLOG reflejan cambios y cobertura?

---

> **FIN CTX\_O3\_RwB\_Total\_20250731.md** [Auto-generado por IA, chunking y literalidad según estándar RwB v5, 2025-07-31.]


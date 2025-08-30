---

file: core/doc/workbench/glossary_baseline_v_1_locked.md code: GBL name: GlossaryBaselineV1 version: v1.0.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: locked referencias:

- GREAL (GlossaryRealV1)
- GTBL (Glossary\_Template\_Baseline\_v1.1\_Locked)
- DTTBL (DirTree\_Template\_Baseline\_v1.1\_Locked)
- PCTRL (PlatformControlPrinciplesV1) triggers: [TRG\_BASELINE\_LOCK, TRG\_GLOSSARY] cambios:
- 2025-08-18: Baseline real del glosario bloqueado según template. checks:
- IDs únicos prefijo GLOS::
- Refs sólo a buckets DIR::
- Sin rutas de archivos ni anclas

---

# Baseline Lock — Glosario v1.0.0

**Baseline-ID**: BL-2025-08-18-Glossary-v1.0.0\
**Árbol**: BL-2025-08-18-DirTree-v1.4.2\
**Snapshot**: `AINGZ_V5_Glossary_Real_v1.md` validado 2025-08-18

> Estado congelado. Ediciones futuras en *working copy* del glosario y nuevo lock.

## Tabla (snapshot)

| ID (GLOS::)    | Término             | Definición breve                                          | Refs (DIR::)                                 | Sinónimos           | Tags            |
| -------------- | ------------------- | --------------------------------------------------------- | -------------------------------------------- | ------------------- | --------------- |
| GLOS::MAIN     | Glosario principal  | Conjunto de términos canónicos del monorepo.              | [[DIR::SEM]], [[DIR::ROOT]]                  | vocabulario         | #glosario       |
| GLOS::BUCKET   | Bucket              | Agrupador lógico de carpetas y assets para un dominio.    | [[DIR::ROOT]], [[DIR::DB]]                   | carpeta lógica      | #estructura     |
| GLOS::ASSET    | Asset               | Artefacto tangible y versionable bajo control QMS.        | [[DIR::DOCS]], [[DIR::OTPL]], [[DIR::SCRIP]] | artefacto           | #artefacto      |
| GLOS::ENTITY   | Entidad             | Contrato semántico aplicable a datos o procesos.          | [[DIR::SEM]]                                 | concepto            | #semantica      |
| GLOS::RULESET  | Ruleset             | Conjunto de reglas con router por plataforma/app/api.     | [[DIR::RULE]]                                | políticas           | #gobierno       |
| GLOS::PIPE     | Pipeline            | Orquestación declarativa disparada por triggers.          | [[DIR::PIPE]], [[DIR::WF]]                   | flujo               | #orquestacion   |
| GLOS::WFTRIG   | Trigger de workflow | Evento que inicia una ejecución o cambio de estado.       | [[DIR::WF]]                                  | disparador          | #workflow       |
| GLOS::BASELOCK | Baseline lock       | Estado congelado e inmutable de un artefacto.             | [[DIR::LOG]]                                 | freeze              | #qms            |
| GLOS::VREVIEW  | Version review      | Evaluación de deltas, riesgos y recomendación de versión. | [[DIR::OTPD]]                                | revisión de versión | #qms            |
| GLOS::QMS      | QMS                 | Sistema de gestión de calidad, validaciones y normas.     | [[DIR::QMS]]                                 | calidad             | #qms            |
| GLOS::KCTX     | Contexto vivo       | Estado operativo actual para continuidad de procesos.     | [[DIR::KCTX]]                                | estado activo       | #operacion      |
| GLOS::AILE     | AI Learn            | Área de aprendizaje, evaluación y feedback de IA.         | [[DIR::AILE]]                                | mlops               | #ia             |
| GLOS::DEVP     | Develop             | Configuración, conectores y orquestación desacoplada.     | [[DIR::DEVP]]                                | devops              | #plataforma     |
| GLOS::OTPL     | Out Templates       | Plantillas de salida estandarizadas para entregables.     | [[DIR::OTPL]]                                | templates           | #documentacion  |
| GLOS::GUID     | Guides              | Guías operativas y SOPs de la plataforma.                 | [[DIR::GUID]]                                | manuales            | #procedimientos |

## Reglas y Checklist

- Namespaces aprobados.
- Sin enlaces a archivos ni anclas.

## OutputTemplate

```yaml
output_example:
  status: GLOSSARY_BASELINE_LOCKED
  baseline_id: BL-2025-08-18-Glossary-v1.0.0
  created_at: 2025-08-18T00:00:00-03:00
  result:
    - files_frozen: [core/doc/workbench/glossary_baseline_v_1_locked.md]
  log:
    - step1: qa_pass
    - step2: checkpoint
    - step3: freeze
```


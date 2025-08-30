---

file: core/doc/workbench/AINGZ\_V5\_Glossary\_Real\_v1.md code: GREAL name: GlossaryRealV1 version: v1.0.0 date: 2025-08-18 owner: AingZ\_Platform · RwB status: draft (real) referencias:

- BL-2025-08-18-DirTree-v1.4.2
- BL-2025-08-18-BucketsMap-v1.0.0
- PCTRL (PlatformControlPrinciplesV1)
- GTPL (Glossary\_Template\_v1) triggers: [TRG\_GLOSSARY\_REAL, TRG\_XREF\_GRAPH] cambios:
- 2025-08-18: Primera versión real del glosario con refs a DIR::. checks:
- IDs únicos prefijo GLOS::
- Refs sólo a buckets DIR::
- Sin rutas de archivos ni anclas

---

# Glosario — Real v1

**Contrato**: Término → Definición breve → Referencias a buckets `DIR::`. Sin enlaces a archivos.

## Tabla

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

---

## Reglas mínimas

- Mantener sólo namespaces aprobados: `DIR::, GLOS::, RULESET::, WF::, TPL::, QMS::, CHG::`.
- El alias visible de un nodo puede cambiar; el `DIR::<CODE>` es estable.
- Añadir términos nuevos con impacto → crear ADR.

## OutputTemplate

```yaml
output_example:
  status: GLOSSARY_REAL_READY
  created_at: 2025-08-18T00:00:00-03:00
  params:
    - namespaces: [DIR::, GLOS::]
  result:
    - terms_defined: 15
    - file_refs_detected: 0
  log:
    - step1: author
    - step2: link_dirs
    - step3: validate
```


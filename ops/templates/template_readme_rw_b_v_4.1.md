---
file: templates/README_TEMPLATE_v4_1.md
code: TPL
name: ReadmeTemplateV4_1
version: v4.1
date: 2025-08-11
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#2025-08-11-readme-template-v4_1
chk: CHK_root.md#2025-08-11-readme-template-v4_1
---

# <NombreDelBucket>

> Plantilla universal **V4.1** para READMEs de buckets/activos. Cumple **Regla de Máxima Jerarquía** (Naming · Ruta · WF · OutputTemplate) y **precedencia** Glosario/Diccionario.

## 1) Propósito
Describir objetivo del bucket/activo, su alcance y criterios de éxito.

## 2) Alcance
- Ramas/paths incluidos del árbol V4.
- Plataformas involucradas: Chat, Actions, Bot/API, Notion.

## 3) Estructura mínima (árbol)
```text
<ruta/>
  ├─ readme.md (este)
  ├─ wf/...
  ├─ templates/...
  ├─ log/...
  └─ ...
```

## 4) Naming & Ruta (obligatorio)
- **CODE** ≤5, `SCREAMING_SNAKE` (ver Glosario).
- **Ruta válida** según Blueprint; el campo `file:` del front‑matter debe **coincidir** con la ruta real del archivo.

## 5) Metadatos (front‑matter)
Incluir: `file, code, name, version, date, owner, status, xrf{blueprint,mplan,glossary,dictionary}, triggers[], chg, chk`.

## 6) Crossref (XRF)
Enlazar Blueprint, Master Plan, Glosario CODE v2 y Diccionario CODE_TRIGGERS v2 (máxima jerarquía).

## 7) Triggers (mínimos por ciclo)
`TRG_CONSOLIDATE_TL` obligatorio; agregar `TRG_AUDIT_TL`, `TRG_AUDIT_LEGACY`, `TRG_PURGE_AI` según el caso.

## 8) Workflow del bucket
Objetivo → Inputs → Pasos → Validaciones → Salidas. Referenciar WFs específicos si están en otro archivo.

## 9) Validación (Pre/PostCheck)
- **PreCheck**: CODE regex, ruta válida, XRF completo, triggers mínimos, OutputTemplate presente.
- **PostCheck**: `status: OK`, evidencias publicadas (artefacto/commit/Notion), `CHG/CHK/CHKP/LESSONS` actualizados.

## 10) Entregables
Listar archivos/artefactos que produce el bucket (logs, plantillas, datasets, WFs, etc.).

## 11) Matriz VERSUS (Plataforma × I/O × Evidencias)
| Plataforma | I/O permitido | Evidencias |
|---|---|---|
| Chat | Markdown/MD, tablas, Mermaid | OutputTemplate en canvas + CHG/CHK |
| Actions | Archivos/Artefactos | Artefacto OutputTemplate + commit |
| Bot/API | Comentarios/labels, archivos | Comment con OutputTemplate + log |
| Notion | Propiedades/páginas/DB | Página con snapshot del OutputTemplate |

## 12) Checklist rápido
- [ ] CODE ≤5 (`SCREAMING_SNAKE`), válido en Glosario.
- [ ] `file:` = ruta real; ruta válida en Blueprint.
- [ ] XRF completo (blueprint/mplan/glossary/dictionary).
- [ ] Triggers mínimos declarados.
- [ ] WF explícito del bucket.
- [ ] **OutputTemplate** integrado.
- [ ] PDCA (CHG/CHK/CHKP/LESSONS) actualizado.

---
# OutputTemplate (obligatorio)
readme_template_v4_1:
  status: OK
  id_asset: README_TPL_V4_1_2025-08-11T00:00:00Z
  generated_by: ai
  created_at: 2025-08-11T00:00:00Z
  params:
    bucket: <core|ops|packages|lifecycle|library|snapshots_ctx>
    owner: <equipo>
  result:
    files: [<ejemplos>]
    checks:
      precheck: required
      postcheck: required
  log:
    - step1: draft
    - step2: review
    - step3: publish


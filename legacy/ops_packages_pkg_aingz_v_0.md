---

## file: ops/packages/PKG\_AINGZ\_V0.md code: PKGAZ name: AingzArchPackage version: v0.1 date: 2025-08-12 owner: AingZ\_Platform · RwB status: active xrf: blueprint: RwB\_Blueprint\_V4 mplan: RwB\_MasterPlan\_V4 glossary: CODE\_Glossary\_v2 dictionary: CODE\_Triggers\_v2 triggers: [TRG\_CONSOLIDATE\_TL, TRG\_AUDIT\_TL] chg: CHG\_main.md#pkg\_aingz\_v0 chk: CHK\_root.md#pkg\_aingz\_v0

# Paquete de Arquitectura — **AINGZ** (V0 / MVP)

> **Manifiesto** del paquete de salida ajustado a **nueva arquitectura** (naming sin "V4"). Incluye **árbol mínimo propuesto**, rutas provisoriamente definitivas y **10 archivos** (8 artefactos núcleo + README del paquete + plantilla de READMEs).

---

## 0) Árbol de directorios mínimo (propuesto)

```text
AingZ_Platform/
├─ core/
│  ├─ doc/
│  │  ├─ blueprint/BLP_AINGZ_V0.md
│  │  ├─ mplan/MPLN_AINGZ_V0.md
│  │  ├─ roadmap/RDM_AINGZ_V0.md
│  │  └─ adr/ADR_0001_AINGZ_V0.md
│  ├─ rules/RULES_AINGZ_V0.md
│  ├─ checklists/CHK_AINGZ_V0.md
│  └─ kns/
│     ├─ glossary/
│     └─ triggers/
├─ ops/
│  ├─ configs/CFG_AINGZ_V0.yaml
│  ├─ scripts/
│  │  └─ setup/SETUP_AINGZ_V0.md
│  ├─ packages/PKG_AINGZ_V0.md
│  └─ templates/
│     └─ README_TEMPLATE_V0.md
├─ src/
│  └─ aingz/
│     ├─ domain/
│     ├─ adapters/
│     ├─ orchestration/
│     ├─ memory/
│     ├─ eval/
│     └─ telemetry/
├─ storage/
└─ data/
```

> Este árbol es **mínimo viable** y alinea módulos del **Blueprint** con código (`src/aingz/...`).

---

## 1) `core/doc/blueprint/BLP_AINGZ_V0.md`

```markdown
---
file: core/doc/blueprint/BLP_AINGZ_V0.md
code: BLP
name: AingzBlueprint
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: MPLN_AINGZ_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#blp_aingz_v0
chk: CHK_root.md#blp_aingz_v0
---
# Blueprint — AINGZ (V0)

## Patrones & topología
- **Base**: Monolito Modular + **Hexagonal** (Puertos/Adaptadores)
- **Flujo**: **Orquestación en grafo** en proceso (nodos = agente/herramientas)
- **Memoria**: Híbrida (episódica, semántica, factual) con **purga por objetivos**
- **Asíncrono**: **EDA ligero** (cola in‑process → Redis opcional)

## Boundaries (módulos)
- **domain/** núcleo de casos de uso (sin dependencias a infra)  
- **adapters/** I/O (DB, FS, queue, HTTP, APIs)
- **orchestration/** grafo de tareas; reintentos; timeouts
- **memory/** episodic/semantic/factual + políticas de retención
- **eval/** evaluación de prompts/outputs; métricas IA
- **telemetry/** tracing, logs, métricas

## Dependencias externas
- BD: **SQLite** (dev) → **PostgreSQL** (escala)
- Cache: **in‑memory** (TTL)
- Mensajería: **in‑process** (→ Redis opcional)
- Storage: **FS local** + adaptador **nube/drive**
- LLM/IA: proveedor vía **Puerto** (OpenAI como primer adaptador)

## Contratos
- **Puertos** (Protocol/ABC) para LLM, Tools, Storage, Queue, DB
- **Eventos** versionados; **Outbox**; **DLQ**; **idempotencia**
- **Prompt/Tool registry** con trazabilidad (alta para IA)

## Riesgos & mitigaciones
- Erosión modular → **tests de arquitectura**; reglas de dependencia
- Pérdida de eventos → **Outbox** + **DLQ** + reintentos idempotentes
- Lock‑in proveedor → **DIP** por puertos; adaptadores neutrales

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: blp_aingz_v0
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
  params:
    - patterns: [monolith_modular, hexagonal, eda_lite, graph_orchestration, hybrid_memory]
  result:
    - modules: [domain, adapters, orchestration, memory, eval, telemetry]
```

---

## 2) `core/doc/mplan/MPLN_AINGZ_V0.md`

```markdown
---
file: core/doc/mplan/MPLN_AINGZ_V0.md
code: MPLN
name: AingzMasterPlan
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V0
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#mplan_aingz_v0
chk: CHK_root.md#mplan_aingz_v0
---
# Master Plan — AINGZ (V0)

## Fases
- **F0 Baseline (0–1 mes)**: Modular+Hex; memoria híbrida mínima; tool/prompt registry; telemetría básica; .env
- **F1 Eventos (1–3 meses)**: EDA ligero; outbox; DLQ; idempotencia; proyecciones de lectura
- **F2 Escala (3–6 meses)**: Redis opcional; migración selectiva a PostgreSQL; endurecer contratos
- **F3 API (6–9 meses)**: exponer endpoints (FastAPI opcional); autenticación básica; rate‑limit
- **F4 Serverless táctico (9–12 meses)**: funciones para picos/batch

## KPIs (objetivos)
- Interacción p95 **<3s**; Batch sin restricción dura  
- **MTTR < 1h**  
- **DLQ = 0** sostenido  
- **Cobertura tests 50%→70%** (F1)  
- **Costo** acorde a necesidad (flexible)

## Riesgos & planes
- Complejidad creciente → limitar deps; plantillas; revisiones ADR
- Debt de observabilidad → OTel básico en F0; ampliar en F1

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: mplan_aingz_v0
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
```

---

## 3) `core/doc/roadmap/RDM_AINGZ_V0.md`

```markdown
---
file: core/doc/roadmap/RDM_AINGZ_V0.md
code: RDM
name: AingzRoadmap
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V0
  mplan: MPLN_AINGZ_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#rdm_aingz_v0
chk: CHK_root.md#rdm_aingz_v0
---
# Roadmap — AINGZ (V0)

## Hitos (MVP → F1)
- **M0** Repo & entorno; linters/type‑checks/tests base
- **M1** Memoria híbrida v1 (episódica/semántica/factual) + políticas por objetivo
- **M2** Prompt/Tool registry + trazabilidad IA
- **M3** Orquestación en grafo + reintentos/timeout
- **M4** EDA ligero + outbox/DLQ/idempotencia
- **M5** Observabilidad (tracing/logs/métricas)
- **M6** Redis opcional + vistas lectura
- **M7** PostgreSQL (si aplica)

## Criterios de done
- Código y docs cumplen **rutas V0** + front‑matter  
- **SOLID‑Gate** verde  
- KPIs mínimos de Fase alcanzados

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: rdm_aingz_v0
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
```

---

## 4) `core/rules/RULES_AINGZ_V0.md`

```markdown
---
file: core/rules/RULES_AINGZ_V0.md
code: RULES
name: AingzRuleSet
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V0
  mplan: MPLN_AINGZ_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_AUDIT_TL]
chg: CHG_main.md#rules_aingz_v0
chk: CHK_root.md#rules_aingz_v0
---
# RuleSet — AINGZ (V0)

## SOLID (obligatorio)
- **DIP**: dominio no importa adaptadores/SDKs; todo I/O tras **Puertos**
- **ISP**: interfaces pequeñas (<5 métodos); una por caso de uso
- **SRP**: módulos con una sola razón de cambio
- **OCP**: extensión por registro/config (sin tocar core)
- **LSP**: tests de sustitución para cada adaptador

## Eventos
- Contratos versionados; **Outbox**; **DLQ**; idempotencia; **sagas** si aplica

## Persistencia & memoria
- ACID para estado fuerte; **TTL** en cache  
- Capas de memoria (episódica/semántica/factual) con **purga por objetivos**

## Naming & rutas
- **CODE ≤ 5**; nombre en PascalCase en `name:`; rutas según **árbol V0**

## Calidad & gates
- import‑linter (arquitectura), mypy (tipos), pytest (tests), ruff/pylint (lint)
- cobertura mínima 50% (F0) → 70% (F1)

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: rules_aingz_v0
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
```

---

## 5) `core/checklists/CHK_AINGZ_V0.md`

```markdown
---
file: core/checklists/CHK_AINGZ_V0.md
code: CHK
name: AingzChecklist
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V0
  mplan: MPLN_AINGZ_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_AUDIT_TL]
chg: CHG_main.md#chk_aingz_v0
chk: CHK_root.md#chk_aingz_v0
---
# Checklist — AINGZ (V0)

- [ ] DIP: dominio no importa adaptadores/SDK
- [ ] ISP: interfaces pequeñas (<5 métodos)
- [ ] SRP: una responsabilidad por módulo
- [ ] OCP: registro/plug‑in para herramientas/LLM
- [ ] LSP: tests de sustitución para cada adaptador
- [ ] Eventos: outbox + DLQ + idempotencia
- [ ] Memoria: políticas por objetivo implementadas
- [ ] Observabilidad: tracing/logs/métricas activos
- [ ] KPIs: p95<3s, MTTR<1h, DLQ=0
- [ ] Docs: front‑matter + rutas V0 + OutputTemplate

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: chk_aingz_v0
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
```

---

## 6) `ops/configs/CFG_AINGZ_V0.yaml`

```yaml
---
file: ops/configs/CFG_AINGZ_V0.yaml
code: CFG
name: AingzConfig
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V0
  mplan: MPLN_AINGZ_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#cfg_aingz_v0
chk: CHK_root.md#cfg_aingz_v0
---
arch:
  alias: AINGZ
  patterns: [monolith_modular, hexagonal, eda_lite, graph_orchestration, hybrid_memory]
modules:
  - id: domain
    purpose: casos_de_uso
  - id: adapters
    purpose: io_externo
  - id: orchestration
    purpose: grafo_tareas
  - id: memory
    purpose: memorias_y_politicas
  - id: eval
    purpose: evaluaciones_ia
  - id: telemetry
    purpose: observabilidad
ports:
  db:
    driver: sqlite
    dsn: sqlite:///./data/aingz.db
    prod:
      driver: postgres
      dsn: postgresql://<user>:<pass>@<host>/<db>
  cache:
    driver: in_memory
    ttl_seconds: 300
  queue:
    driver: in_process   # redis opcional
    redis_url: "redis://localhost:6379/0"
  storage:
    local_root: ./storage
    cloud_driver: none   # drive/cloud opcional via adaptador
llm:
  provider: openai
  model: <set_by_env>
  timeout_s: 60
  retry:
    max: 3
    backoff_s: 2
memory:
  episodic:
    enabled: true
    retention: by_objective
  semantic:
    enabled: true
    index_path: ./data/embeddings
  factual:
    enabled: true
    store: ./data/facts
telemetry:
  tracing: basic
  metrics: basic
  logs: info
secrets:
  source: env
  required:
    - OPENAI_API_KEY
    - GITHUB_TOKEN
ci_cd:
  containers: true
  pipelines: [build, test, lint]
```

---

## 7) `ops/scripts/setup/SETUP_AINGZ_V0.md`

```markdown
---
file: ops/scripts/setup/SETUP_AINGZ_V0.md
code: SETUP
name: AingzSetup
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V0
  mplan: MPLN_AINGZ_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#setup_aingz_v0
chk: CHK_root.md#setup_aingz_v0
---
# Setup — AINGZ (V0)

1) **Entorno**
   - Python 3.12 (o 3.11)
   - `python -m venv .venv && source .venv/bin/activate`
   - `pip install -U pip wheel`
2) **Dependencias base**
   - `pip install ruff mypy pytest import-linter`
3) **Configuración**
   - Copiar `ops/configs/CFG_AINGZ_V0.yaml` y ajustar DSNs
   - Crear `.env` con `OPENAI_API_KEY` y `GITHUB_TOKEN`
4) **Calidad**
   - `ruff .` · `mypy .` · `pytest`
   - `import-linter -c arch_contracts.toml` (cuando lo agreguemos)
5) **Contenedores (opcional)**
   - Dockerfile simple + `docker compose up` para servicio base
```

---

## 8) `core/doc/adr/ADR_0001_AINGZ_V0.md`

```markdown
---
file: core/doc/adr/ADR_0001_AINGZ_V0.md
code: ADR
name: ADR0001_AingzArchitecture
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: proposed
xrf:
  blueprint: BLP_AINGZ_V0
  mplan: MPLN_AINGZ_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#adr_0001_aingz_v0
chk: CHK_root.md#adr_0001_aingz_v0
---
# ADR-0001: Arquitectura AINGZ (V0)

## Contexto
Proyecto personal (1 dev) con agentes/IA, foco en **evolutividad**, **escalabilidad** y **confiabilidad**; memoria no‑loss y trazabilidad IA altas; volumen bajo; integraciones OpenAI/GitHub; despliegue local/contenedor con opción nube.

## Decisión
Adoptar **Monolito Modular + Hexagonal**, **orquestación en grafo** en proceso, **memoria híbrida**, **EDA ligero** con outbox/DLQ/idempotencia, **prompt/tool registry**, y telemetría abierta. SQLite (dev) → Postgres (escala); cache in‑memory; queue in‑process → Redis opcional.

## Consecuencias
- + Simplicidad, costo bajo, testabilidad (SOLID)
- − Escalado por proceso; disciplina en límites requerida

## KPIs
- p95 <3s; MTTR <1h; DLQ=0; cobertura 50%→70% (F1)

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: adr_0001_aingz_v0
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
```

---

## 9) `ops/packages/README_PKG_AINGZ_V0.md`

```markdown
---
file: ops/packages/README_PKG_AINGZ_V0.md
code: RDPKG
name: AingzPackageReadme
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V0
  mplan: MPLN_AINGZ_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#readme_pkg_aingz_v0
chk: CHK_root.md#readme_pkg_aingz_v0
---
# README — Paquete AINGZ (V0)

## Propósito
Este paquete define la **arquitectura base** de AINGZ (V0), lista para versionar y evolucionar.

## Contenido
- Blueprint, Master Plan, Roadmap, RuleSet, Checklist
- Configuración (YAML), Setup, ADR inicial
- Plantilla de README para replicar en nuevos módulos

## Árbol
(Ver sección 0 del manifiesto o el repositorio).

## Cómo usar
1) Completar `CFG_AINGZ_V0.yaml`.
2) Seguir `SETUP_AINGZ_V0.md`.
3) Validar **Checklist** y **RuleSet** (SOLID‑Gate).
4) Registrar cambios en **ADR**.

## Crossref
Mantener XRF con Blueprint/MasterPlan/Glosario/Diccionario.
```

---

## 10) `ops/templates/README_TEMPLATE_V0.md`

```markdown
---
file: ops/templates/README_TEMPLATE_V0.md
code: RDTPL
name: ReadmeTemplate
version: v0.1
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#readme_template_v0
chk: CHK_root.md#readme_template_v0
---
# <Title> — README (V0)

## Propósito
<descripción breve>

## Estructura
```

<árbol de carpetas/archivos>

```

## Configuración
- Requisitos/variables/env

## Uso
- Pasos clave / comandos

## Calidad
- Lints/tests/tipos obligatorios

## Crossref
- Blueprint/MasterPlan/Glosario/Diccionario/ADR
```

---

## OutputTemplate (obligatorio)

output\_example: status: OK id\_asset: pkg\_aingz\_v0 generated\_by: ai created\_at: 2025-08-12T00:00:00-03:00 params: - alias: AINGZ - files: - core/doc/blueprint/BLP\_AINGZ\_V0.md - core/doc/mplan/MPLN\_AINGZ\_V0.md - core/doc/roadmap/RDM\_AINGZ\_V0.md - core/rules/RULES\_AINGZ\_V0.md - core/checklists/CHK\_AINGZ\_V0.md - ops/configs/CFG\_AINGZ\_V0.yaml - ops/scripts/setup/SETUP\_AINGZ\_V0.md - core/doc/adr/ADR\_0001\_AINGZ\_V0.md - ops/packages/README\_PKG\_AINGZ\_V0.md - ops/templates/README\_TEMPLATE\_V0.md result: - status: package\_ready log: - step1: generate - step2: assemble - step3: validate\_meta


---
file: ops/packages/PKG_AINGZ_V4.md
code: PKGAZ
name: AingzArchPackage
version: v4.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL, TRG_AUDIT_TL]
chg: CHG_main.md#pkg_aingz_v4
chk: CHK_root.md#pkg_aingz_v4
---

# Paquete de Arquitectura — **AINGZ** (MVP)

> **Este manifiesto agrupa los 8 archivos del paquete**. Cada sección contiene el **contenido completo** del archivo final (drop‑in‑ready) con **front‑matter** y, cuando aplica, **OutputTemplate**.

---

## 1) `core/doc/blueprint/BLP_AINGZ_V4.md`
```markdown
---
file: core/doc/blueprint/BLP_AINGZ_V4.md
code: BLP
name: AingzBlueprint
version: v4.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: MPLN_AINGZ_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#blp_aingz
chk: CHK_root.md#blp_aingz
---
# Blueprint — AINGZ

## Patrones & topología
- **Base**: Monolito Modular + **Hexagonal** (Puertos/Adaptadores)
- **Flujo**: **Orquestación en grafo** en proceso (nodos = agente/herramientas)
- **Memoria**: Híbrida (episódica, semántica, factual) con **purga por objetivos**
- **Asíncrono**: **EDA ligero** (cola in‑process → Redis opcional)

## Boundaries (módulos)
- **domain/** núcleo de casos de uso (sin dependencias a infra)  
- **adapters/** I/O (DB, FS, queue, HTTP, APIs proveedores)
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
- **Eventos** con versión y semántica clara; **Outbox** e **idempotencia**
- **Prompt/Tool registry** con trazabilidad (alta para IA)

## Riesgos & mitigaciones
- Erosión modular → **tests de arquitectura**; reglas de dependencia
- Pérdida de eventos → **Outbox** + **DLQ** + reintentos idempotentes
- Lock‑in proveedor → **DIP** por puertos; adaptadores neutrales

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: blp_aingz_v4
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
  params:
    - patterns: [monolith_modular, hexagonal, eda_lite, graph_orchestration, hybrid_memory]
  result:
    - modules: [domain, adapters, orchestration, memory, eval, telemetry]
```

---

## 2) `core/doc/mplan/MPLN_AINGZ_V4.md`
```markdown
---
file: core/doc/mplan/MPLN_AINGZ_V4.md
code: MPLN
name: AingzMasterPlan
version: v4.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V4
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#mplan_aingz
chk: CHK_root.md#mplan_aingz
---
# Master Plan — AINGZ

## Fases
- **F0 Baseline (0–1 mes)**: Modular+Hex; memoria híbrida mínima; tool/prompt registry; telemetría básica; .env
- **F1 Eventos (1–3 meses)**: EDA ligero; outbox; DLQ; idempotencia; proyecciones de lectura
- **F2 Escala (3–6 meses)**: Redis opcional; migración selectiva a PostgreSQL; endurecer contratos
- **F3 API (6–9 meses)**: exponer endpoints (FastAPI opcional); autenticación básica; políticas de rate‑limit
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
  id_asset: mplan_aingz_v4
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
```

---

## 3) `core/doc/roadmap/RDM_AINGZ_V4.md`
```markdown
---
file: core/doc/roadmap/RDM_AINGZ_V4.md
code: RDM
name: AingzRoadmap
version: v4.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V4
  mplan: MPLN_AINGZ_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#rdm_aingz
chk: CHK_root.md#rdm_aingz
---
# Roadmap — AINGZ

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
- Código y docs cumplen **rutas V4** + front‑matter  
- **SOLID‑Gate** verde  
- KPIs mínimos de Fase alcanzados

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: rdm_aingz_v4
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
```

---

## 4) `core/rules/RULES_AINGZ_V4.md`
```markdown
---
file: core/rules/RULES_AINGZ_V4.md
code: RULES
name: AingzRuleSet
version: v4.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V4
  mplan: MPLN_AINGZ_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_AUDIT_TL]
chg: CHG_main.md#rules_aingz
chk: CHK_root.md#rules_aingz
---
# RuleSet — AINGZ

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
- **CODE ≤ 5** (SCREAMING_SNAKE para códigos); nombre en PascalCase en `name:`; rutas según **Blueprint V4**

## Calidad & gates
- import‑linter (arquitectura), mypy (tipos), pytest (tests), ruff/pylint (lint)
- cobertura mínima 50% (F0) → 70% (F1)

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: rules_aingz_v4
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
```

---

## 5) `core/checklists/CHK_AINGZ_V4.md`
```markdown
---
file: core/checklists/CHK_AINGZ_V4.md
code: CHK
name: AingzChecklist
version: v4.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V4
  mplan: MPLN_AINGZ_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_AUDIT_TL]
chg: CHG_main.md#chk_aingz
chk: CHK_root.md#chk_aingz
---
# Checklist — AINGZ

- [ ] DIP: dominio no importa adaptadores/SDK
- [ ] ISP: interfaces pequeñas (<5 métodos)
- [ ] SRP: una responsabilidad por módulo
- [ ] OCP: registro/plug‑in para herramientas/LLM
- [ ] LSP: tests de sustitución para cada adaptador
- [ ] Eventos: outbox + DLQ + idempotencia
- [ ] Memoria: políticas por objetivo implementadas
- [ ] Observabilidad: tracing/logs/métricas activos
- [ ] KPIs: p95<3s, MTTR<1h, DLQ=0
- [ ] Docs: front‑matter + rutas V4 + OutputTemplate

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: chk_aingz_v4
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
```

---

## 6) `ops/configs/CFG_AINGZ_V4.yaml`
```yaml
---
file: ops/configs/CFG_AINGZ_V4.yaml
code: CFG
name: AingzConfig
version: v4.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V4
  mplan: MPLN_AINGZ_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#cfg_aingz
chk: CHK_root.md#cfg_aingz
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

## 7) `ops/scripts/setup/SETUP_AINGZ_V4.md`
```markdown
---
file: ops/scripts/setup/SETUP_AINGZ_V4.md
code: SETUP
name: AingzSetup
version: v4.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: BLP_AINGZ_V4
  mplan: MPLN_AINGZ_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#setup_aingz
chk: CHK_root.md#setup_aingz
---
# Setup — AINGZ

1) **Entorno**
   - Python 3.12 (o 3.11)
   - `python -m venv .venv && source .venv/bin/activate`
   - `pip install -U pip wheel`
2) **Dependencias base**
   - `pip install ruff mypy pytest import-linter`
3) **Configuración**
   - Copiar `ops/configs/CFG_AINGZ_V4.yaml` y ajustar DSNs
   - Crear `.env` con `OPENAI_API_KEY` y `GITHUB_TOKEN`
4) **Calidad**
   - `ruff .` · `mypy .` · `pytest`
   - `import-linter -c arch_contracts.toml` (cuando lo agreguemos)
5) **Contenedores (opcional)**
   - Dockerfile simple + `docker compose up` para servicio base
```

---

## 8) `core/doc/adr/ADR_0001_AINGZ_V4.md`
```markdown
---
file: core/doc/adr/ADR_0001_AINGZ_V4.md
code: ADR
name: ADR0001_AingzArchitecture
version: v4.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: proposed
xrf:
  blueprint: BLP_AINGZ_V4
  mplan: MPLN_AINGZ_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#adr_0001_aingz
chk: CHK_root.md#adr_0001_aingz
---
# ADR-0001: Arquitectura AINGZ

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
  id_asset: adr_0001_aingz_v4
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
```

---

## OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: pkg_aingz_v4
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
  params:
    - alias: AINGZ
    - files:
      - core/doc/blueprint/BLP_AINGZ_V4.md
      - core/doc/mplan/MPLN_AINGZ_V4.md
      - core/doc/roadmap/RDM_AINGZ_V4.md
      - core/rules/RULES_AINGZ_V4.md
      - core/checklists/CHK_AINGZ_V4.md
      - ops/configs/CFG_AINGZ_V4.yaml
      - ops/scripts/setup/SETUP_AINGZ_V4.md
      - core/doc/adr/ADR_0001_AINGZ_V4.md
  result:
    - status: package_ready
  log:
    - step1: generate
    - step2: assemble
    - step3: validate_meta


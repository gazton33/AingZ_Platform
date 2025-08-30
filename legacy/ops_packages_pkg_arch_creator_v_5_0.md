---

## file: ops/packages/PKG\_ARCH\_CREATOR\_V5\_0.md code: PKGAC name: ArchCreatorPackage version: v5.0 date: 2025-08-12 owner: AingZ\_Platform · RwB status: active xrf: blueprint: RwB\_Blueprint\_V4 mplan: RwB\_MasterPlan\_V4 glossary: CODE\_Glossary\_v2 dictionary: CODE\_Triggers\_v2 triggers: [TRG\_CONSOLIDATE\_TL, TRG\_AUDIT\_TL] chg: CHG\_main.md#pkg\_arch\_creator\_v5\_0 chk: CHK\_root.md#pkg\_arch\_creator\_v5\_0

# Paquete **Arch\_Creator** — V5.0 (MTX + WF + Plantillas)

> **Objetivo**: que con **este paquete** puedas **diseñar, crear e implementar** una arquitectura nueva de forma repetible. Incluye: **MTX (V5.0)**, **WF de creación (V5.0)**, plantillas completas (blueprint/mplan/roadmap/rules/checklist/config/setup/adr), contratos de arquitectura y tests mínimos.

---

## 0) Árbol de directorios del paquete (propuesto)

```text
Arch_Creator/
├─ core/
│  ├─ data/mtx/MTX_ARCH_PATTERNS_V5_0.md
│  └─ wf/WF_ARCH_CREATE_V5_0.md
├─ ops/
│  ├─ packages/README_ARCH_CREATOR_V5_0.md
│  ├─ templates/
│  │  ├─ blueprint/BLP_<ARCH>_V0.md
│  │  ├─ mplan/MPLN_<ARCH>_V0.md
│  │  ├─ roadmap/RDM_<ARCH>_V0.md
│  │  ├─ rules/RULES_<ARCH>_V0.md
│  │  ├─ checklists/CHK_<ARCH>_V0.md
│  │  ├─ configs/CFG_<ARCH>_V0.yaml
│  │  ├─ setup/SETUP_<ARCH>_V0.md
│  │  ├─ adr/ADR_0001_<ARCH>_V0.md
│  │  ├─ readme/README_TEMPLATE_V0.md
│  │  ├─ contracts/arch_contracts.toml
│  │  └─ tests/test_substitution_contract.py
│  └─ scripts/
│     └─ GENERATOR_NOTES.md
└─ .
```

> **Nota**: Las plantillas usan **V0** para nuevos trabajos. Si es migración legacy, el **WF** te pide versionar a **V5\_0**.

---

## 1) `core/data/mtx/MTX_ARCH_PATTERNS_V5_0.md`

```markdown
---
file: core/data/mtx/MTX_ARCH_PATTERNS_V5_0.md
code: MTRAP
name: ArchPatternsAssessment
version: v5.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL, TRG_AUDIT_TL, TRG_AUDIT_LEGACY, TRG_PURGE_AI]
chg: CHG_main.md#arch_patterns_v5_0
chk: CHK_root.md#arch_patterns_v5_0
---
# Patrones de Arquitectura de Software — Snapshots + Matrices (V5.0)

> **Propósito**: documento **genérico**, sin naming de terceros, para evaluar y seleccionar patrones en **agentes/IA** con uno o pocos devs. Incorpora **SOLID‑first**, memoria del agente (episódica/semántica/factual), **orquestación en grafo**, EDA ligero y criterios V5.

## 1) Alcance y supuestos
- 1 dev (extensible a 2–3), repositorio único, contenedores, CI/CD repo‑based.
- Objetivos: **evolutividad**, **escalabilidad táctica**, **confiabilidad**, **trazabilidad IA**.
- No objetivos: tiempo real estricto, multi‑equipo, SLA 24x7 crítico.

### 1.1 Escenarios típicos (Agentes/IA)
- Agente único con **tool registry** y **puertos/adaptadores**.
- **Orquestación en grafo** (reintentos/timeout por nodo).
- **Memoria híbrida** con **purga por objetivos** (no por tiempo fijo).
- Trazabilidad de prompts/decisiones/evaluaciones (alta para IA, baja para humano general).

## 1.2 Principios SOLID (guía práctica)
- **SRP**: módulos con una razón de cambio; separar tooling del dominio.
- **OCP**: extensión por registro/config; evitar tocar el core.
- **LSP**: adaptadores deben pasar **tests de sustitución** comunes.
- **ISP**: **interfaces pequeñas** por caso de uso (<5 métodos).
- **DIP**: dominio depende de **abstracciones** (Puertos), no SDKs.

**Reglas ejecutables**: import‑linter (dependencias), mypy (contratos), pytest (sustitución), ruff/pylint (complejidad/estilo).

## 2) Snapshots de patrones (1‑pagers)
- **Monolito Modular** (base recomendada).
- **Hexagonal** (Puertos/Adaptadores) sobre el monolito.
- **Layered**, **Microservicios**, **EDA**, **CQRS**, **Event Sourcing**, **Serverless**.
- **Orquestación en Grafo**, **Agente con Tool Registry**, **Memoria Híbrida**.

> Cada snapshot: **Contexto → Fuerzas → Trade‑offs → Antipatrones → Indicadores** (idénticos a V4, revisados para V5).

## 3) Matrices comparativas (VRS)
- **Patrón × Criterios** (complejidad, escalabilidad, cohesión, acoplamiento, consistencia, latencia, despliegue, observabilidad, coste, fit equipo).
- **Requisitos × Adecuación** (para agentes/IA 1 dev), con escala 1–5.
- **Riesgos × Mitigaciones** (erosión modular, complejidad operativa, pérdida de eventos, lock‑in) con KPIs.
- **Stack de agentes × Integración** (grafo, tools, memoria, persistencia, mensajería, evaluación, observabilidad).
- **Matriz SOLID × Patrones** (ajustada a V5; Hexagonal sobresale en OCP/DIP/ISP).

## 4) Roadmap genérico (1 dev)
- **F0** Baseline: Monolito Modular + Hexagonal; memoria híbrida mínima; tool/prompt registry; telemetría básica.
- **F1** Eventos: EDA ligero (outbox/DLQ/idempotencia), proyecciones de lectura.
- **F2** Escala: Redis opcional; migración selectiva a Postgres; contratos endurecidos.
- **F3** API: FastAPI opcional; auth básica; rate‑limit.
- **F4** Serverless táctico: picos/batch.

## 5) WF — Selección y evaluación (APSEL)
**Pasos**: 0) **SOLID‑Gate** → 1) INGEST → 2) SCORING (VRS) → 3) RIESGOS → 4) DECISIÓN (ADR) → 5) KPIs → 6) CHECK (tests) → 7) CLOSE (CHG/LESSONS/Triggers).

## 6) KPIs mínimos
- p95 lat <3s; MTTR <1h; DLQ=0; cobertura 50%→70%; hit rate memoria; % decisiones explicadas; alucinaciones detectadas.

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: mtx_arch_patterns_v5_0
  generated_by: ai
  created_at: 2025-08-12T00:00:00-03:00
  params:
    - principles: [SOLID]
    - patterns: [monolith_modular, hexagonal, layered, microservices, eda, cqrs, event_sourcing, serverless, graph_orchestration, agent_tools_registry, hybrid_memory]
  result:
    - decision_matrix_path: core/data/mtx/MTX_ARCH_PATTERNS_V5_0.md
    - recommended_strategy: ModularMonolith+Hexagonal→EDA→CQRS(selectivo)
```

---

## 2) `core/wf/WF_ARCH_CREATE_V5_0.md`

````markdown
---
file: core/wf/WF_ARCH_CREATE_V5_0.md
code: WFARC
name: ArchCreateWorkflow
version: v5.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL, TRG_AUDIT_TL, TRG_AUDIT_LEGACY, TRG_PURGE_AI]
chg: CHG_main.md#wf_arch_create_v5_0
chk: CHK_root.md#wf_arch_create_v5_0
---
# WF_ARCH_CREATE_V5_0 — Crear Arquitectura Base (agentes/IA, 1 dev)

> **Propósito**: instanciar una arquitectura desde la **MTX V5.0** y el **ruleset** del paquete, generando **todos los artefactos** (blueprint/mplan/roadmap/rules/checklist/configs/setup/adr) con rutas correctas y metadatos.

## 1) Gates y entradas
- **VERSION‑GATE (0‑fail)**: ¿Trabajo nuevo o migración?
  - **Nuevo** → usar plantillas **V0** (naming `*_V0.*`).
  - **Migración** → usar sufijo **V5_0** (naming `*_V5_0.*`).
- **Inputs**: requisitos, prioridades/pesos, restricciones, **MTX V5.0**.

## 2) Flujo
```mermaid
flowchart TD
  A[Kickoff] --> B[VERSION-GATE]
  B --> C[Ingest requisitos]
  C --> D[SOLID-Gate]
  D --> E[Scoring MTX (VRS)]
  E --> F[ADR decisión]
  F --> G[Generar paquete artefactos]
  G --> H[Config & Setup]
  H --> I[QA (tests + checklist)]
  I --> J[Commit + Triggers]
````

## 3) Pasos

1. **Ingest**: completar plantilla de requisitos + pesos (defaults sugeridos: evolvability 0.28, reliability 0.20, performance 0.20, simplicity 0.12, cost 0.10, auditability 0.10).
2. **SOLID‑Gate**: DIP (dominio no importa infra), ISP (<5 métodos por puerto), SRP (módulos), OCP (extender por registro), LSP (tests de sustitución en adaptadores).
3. **Scoring**: aplicar matriz de la MTX (VRS) y seleccionar patrón/es.
4. **ADR**: registrar contexto, decisión, consecuencias, KPIs.
5. **Generación**: copiar plantillas desde `ops/templates` al destino del proyecto usando alias `<ARCH>` y versión (**V0** o **V5\_0**).
6. **Config & Setup**: rellenar `CFG_<ARCH>_<VER>.yaml` (puertos, storage, cola, secrets).
7. **QA**: ejecutar import‑linter, mypy, pytest (incluye test de sustitución), ruff/pylint.
8. **Commit**: registrar CHG/CHK/LESSONS; disparar triggers.

## 4) Salidas

- Paquete de 8 artefactos instanciado.
- ADR principal creado y aceptado.
- Checklist inicial en verde (o con gaps explícitos).

---

# OutputTemplate (obligatorio)

output\_example: status: OK id\_asset: wf\_arch\_create\_v5\_0 generated\_by: ai created\_at: 2025-08-12T00:00:00-03:00 params: - source\_mtx: core/data/mtx/MTX\_ARCH\_PATTERNS\_V5\_0.md - deliverables: [blueprint, masterplan, roadmap, ruleset, checklist, configs, setups, adr] result: - files\_template\_root: ops/templates - generated\_paths\_example: - core/doc/blueprint/BLP\_*V0.md - core/doc/mplan/MPLN**V0.md - core/doc/roadmap/RDM**V0.md - core/rules/RULES**V0.md - core/checklists/CHK**V0.md - ops/configs/CFG**V0.yaml - ops/scripts/setup/SETUP**V0.md - core/doc/adr/ADR\_0001*\_V0.md log: - step1: ingest - step2: solid\_gate - step3: scoring - step4: adr - step5: package - step6: qa - step7: commit

````

---

## 3) `ops/packages/README_ARCH_CREATOR_V5_0.md`
```markdown
---
file: ops/packages/README_ARCH_CREATOR_V5_0.md
code: RDACR
name: ArchCreatorReadme
version: v5.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#readme_arch_creator_v5_0
chk: CHK_root.md#readme_arch_creator_v5_0
---
# README — Arch_Creator (V5.0)

## Propósito
Paquete para **crear arquitecturas** de forma estandarizada. Incluye **MTX V5.0**, **WF V5.0** y **plantillas**.

## Uso rápido
1) Abrí `core/wf/WF_ARCH_CREATE_V5_0.md` y corré el **VERSION‑GATE** (¿nuevo **V0** o migración **V5_0**?).
2) Completá **INGEST** (requisitos) y **pesos**.
3) Pasá **SOLID‑Gate**. Si falla, corregí límites.
4) Hacé **Scoring** con la **MTX V5.0** y cerrá el **ADR**.
5) **Generá** los 8 artefactos copiando desde `ops/templates/` (ajustá `<ARCH>` y `<VER>`).
6) Completá `CFG_<ARCH>_<VER>.yaml` y `SETUP_<ARCH>_<VER>.md`.
7) Ejecutá QA (linters, tipos, tests, contratos) y registrá **CHG/CHK/LESSONS**.

## Árbol del paquete
(Ver sección 0 del manifiesto o el repositorio.)
````

---

## 4) Plantillas clave (listas para copiar)

### 4.1 `ops/templates/blueprint/BLP_<ARCH>_V0.md`

```markdown
---
file: core/doc/blueprint/BLP_<ARCH>_V0.md
code: BLP
name: <PascalCaseBlueprint>
version: v0.1
date: <YYYY-MM-DD>
owner: <Owner>
status: draft
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: MPLN_<ARCH>_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#blp_<arch>_v0
chk: CHK_root.md#blp_<arch>_v0
---
# Blueprint <ARCH> (V0)
- **Patrones**: <Monolito Modular + Hexagonal + EDA ligero + Orquestación en Grafo + Memoria Híbrida>
- **Boundaries**: <módulos/contextos>
- **Dependencias externas**: <DB, cola, storage, API>
- **Contratos**: <puertos/interface + eventos>
- **Riesgos** & **mitigaciones**: <tabla>

---
# OutputTemplate (obligatorio)
output_example:
  status: DRAFT
  id_asset: blp_<arch>_v0
  generated_by: user
  created_at: <ISO8601>
```

### 4.2 `ops/templates/mplan/MPLN_<ARCH>_V0.md`

```markdown
---
file: core/doc/mplan/MPLN_<ARCH>_V0.md
code: MPLN
name: <PascalCaseMasterPlan>
version: v0.1
date: <YYYY-MM-DD>
owner: <Owner>
status: draft
xrf:
  blueprint: BLP_<ARCH>_V0
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#mplan_<arch>_v0
chk: CHK_root.md#mplan_<arch>_v0
---
# Master Plan <ARCH> (V0)
- Fases/KPIs/Riesgos

---
# OutputTemplate (obligatorio)
output_example:
  status: DRAFT
  id_asset: mplan_<arch>_v0
  generated_by: user
  created_at: <ISO8601>
```

### 4.3 `ops/templates/roadmap/RDM_<ARCH>_V0.md`

```markdown
---
file: core/doc/roadmap/RDM_<ARCH>_V0.md
code: RDM
name: <PascalCaseRoadmap>
version: v0.1
date: <YYYY-MM-DD>
owner: <Owner>
status: draft
xrf:
  blueprint: BLP_<ARCH>_V0
  mplan: MPLN_<ARCH>_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#rdm_<arch>_v0
chk: CHK_root.md#rdm_<arch>_v0
---
# Roadmap <ARCH> (V0)
- Hitos / Entregables / Done

---
# OutputTemplate (obligatorio)
output_example:
  status: DRAFT
  id_asset: rdm_<arch>_v0
  generated_by: user
  created_at: <ISO8601>
```

### 4.4 `ops/templates/rules/RULES_<ARCH>_V0.md`

```markdown
---
file: core/rules/RULES_<ARCH>_V0.md
code: RULES
name: <PascalCaseRuleset>
version: v0.1
date: <YYYY-MM-DD>
owner: <Owner>
status: draft
xrf:
  blueprint: BLP_<ARCH>_V0
  mplan: MPLN_<ARCH>_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_AUDIT_TL]
chg: CHG_main.md#rules_<arch>_v0
chk: CHK_root.md#rules_<arch>_v0
---
# RuleSet <ARCH> (V0)
- **SOLID** obligatorio; Puertos/Adaptadores; Eventos (Outbox/DLQ/idempotencia);
- Persistencia ACID; Cache TTL; Naming CODE≤5 y rutas V0.

---
# OutputTemplate (obligatorio)
output_example:
  status: DRAFT
  id_asset: rules_<arch>_v0
  generated_by: user
  created_at: <ISO8601>
```

### 4.5 `ops/templates/checklists/CHK_<ARCH>_V0.md`

```markdown
---
file: core/checklists/CHK_<ARCH>_V0.md
code: CHK
name: <PascalCaseChecklist>
version: v0.1
date: <YYYY-MM-DD>
owner: <Owner>
status: draft
xrf:
  blueprint: BLP_<ARCH>_V0
  mplan: MPLN_<ARCH>_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_AUDIT_TL]
chg: CHG_main.md#chk_<arch>_v0
chk: CHK_root.md#chk_<arch>_v0
---
# Checklist <ARCH> (V0)
- [ ] DIP/ISP/SRP/OCP/LSP
- [ ] Outbox/DLQ/Idempotencia
- [ ] Memoria por objetivos
- [ ] Telemetría básica
- [ ] KPIs definidos

---
# OutputTemplate (obligatorio)
output_example:
  status: DRAFT
  id_asset: chk_<arch>_v0
  generated_by: user
  created_at: <ISO8601>
```

### 4.6 `ops/templates/configs/CFG_<ARCH>_V0.yaml`

```yaml
---
file: ops/configs/CFG_<ARCH>_V0.yaml
code: CFG
name: <PascalCaseConfig>
version: v0.1
date: <YYYY-MM-DD>
owner: <Owner>
status: draft
xrf:
  blueprint: BLP_<ARCH>_V0
  mplan: MPLN_<ARCH>_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#cfg_<arch>_v0
chk: CHK_root.md#cfg_<arch>_v0
---
arch:
  alias: <ARCH>
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
    dsn: sqlite:///./data/<arch>.db
    prod:
      driver: postgres
      dsn: postgresql://<user>:<pass>@<host>/<db>
  cache:
    driver: in_memory
    ttl_seconds: 300
  queue:
    driver: in_process
    redis_url: "redis://localhost:6379/0"
  storage:
    local_root: ./storage
    cloud_driver: none
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
  required: [OPENAI_API_KEY]
ci_cd:
  containers: true
  pipelines: [build, test, lint]
```

### 4.7 `ops/templates/setup/SETUP_<ARCH>_V0.md`

```markdown
---
file: ops/scripts/setup/SETUP_<ARCH>_V0.md
code: SETUP
name: <PascalCaseSetup>
version: v0.1
date: <YYYY-MM-DD>
owner: <Owner>
status: draft
xrf:
  blueprint: BLP_<ARCH>_V0
  mplan: MPLN_<ARCH>_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#setup_<arch>_v0
chk: CHK_root.md#setup_<arch>_v0
---
# Setup <ARCH> (V0)
1) Crear venv e instalar dependencias base (ruff/mypy/pytest/import-linter).
2) Copiar y ajustar `CFG_<ARCH>_V0.yaml` y `.env`.
3) Ejecutar QA: `ruff .`, `mypy .`, `pytest`, `import-linter -c arch_contracts.toml`.
```

### 4.8 `ops/templates/adr/ADR_0001_<ARCH>_V0.md`

```markdown
---
file: core/doc/adr/ADR_0001_<ARCH>_V0.md
code: ADR
name: ADR0001_<PascalCaseArch>
version: v0.1
date: <YYYY-MM-DD>
owner: <Owner>
status: proposed
xrf:
  blueprint: BLP_<ARCH>_V0
  mplan: MPLN_<ARCH>_V0
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#adr_0001_<arch>_v0
chk: CHK_root.md#adr_0001_<arch>_v0
---
# ADR-0001: Arquitectura <ARCH> (V0)

## Contexto
<resumen>

## Decisión
<patrones elegidos y justificación>

## Consecuencias
<trade-offs>

## KPIs
<p95/MTTR/DLQ/cobertura>

---
# OutputTemplate (obligatorio)
output_example:
  status: OK
  id_asset: adr_0001_<arch>_v0
  generated_by: user
  created_at: <ISO8601>
```

### 4.9 `ops/templates/readme/README_TEMPLATE_V0.md`

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

### 4.10 `ops/templates/contracts/arch_contracts.toml`

```toml
[linter]
contract = "layers"

[python]
source = "src/<arch>"

[rules.layered]
# Dominio no puede importar adaptadores/infra
layers = ["domain", "orchestration", "adapters"]
depend_on_lower = true
forbidden_dependencies = [
  "domain -> adapters",
]
```

### 4.11 `ops/templates/tests/test_substitution_contract.py`

```python
import importlib
import inspect
from typing import Protocol

class LLMPort(Protocol):
    def complete(self, prompt: str, **kw) -> str: ...

# Cada adaptador debe implementar LLMPort sin romper contrato

def test_llm_adapters_substitution():
    adapters = [
        "src.<arch>.adapters.openai_adapter",
        # agregar otros aquí
    ]
    for mod in adapters:
        m = importlib.import_module(mod)
        cls = getattr(m, "Adapter")
        assert issubclass(cls, object)
        sig = inspect.signature(getattr(cls(), "complete"))
        assert "prompt" in sig.parameters
```

### 4.12 `ops/scripts/GENERATOR_NOTES.md`

```markdown
---
file: ops/scripts/GENERATOR_NOTES.md
code: GENNO
name: GeneratorNotes
version: v5.0
date: 2025-08-12
owner: AingZ_Platform · RwB
status: active
xrf:
  blueprint: RwB_Blueprint_V4
  mplan: RwB_MasterPlan_V4
  glossary: CODE_Glossary_v2
  dictionary: CODE_Triggers_v2
triggers: [TRG_CONSOLIDATE_TL]
chg: CHG_main.md#generator_notes_v5_0
chk: CHK_root.md#generator_notes_v5_0
---
# Notas para generadores (manual)
- Copiar plantillas desde `ops/templates` al repo del proyecto.
- Reemplazar `<ARCH>` y `<VER>` (V0 o V5_0) en rutas y metadatos.
- Completar ADR y CFG.
- Ejecutar QA y registrar CHG/CHK/LESSONS.
```

---

## OutputTemplate (obligatorio)

output\_example: status: OK id\_asset: pkg\_arch\_creator\_v5\_0 generated\_by: ai created\_at: 2025-08-12T00:00:00-03:00 params: - files: - core/data/mtx/MTX\_ARCH\_PATTERNS\_V5\_0.md - core/wf/WF\_ARCH\_CREATE\_V5\_0.md - ops/packages/README\_ARCH\_CREATOR\_V5\_0.md - ops/templates/blueprint/BLP\_*V0.md - ops/templates/mplan/MPLN**V0.md - ops/templates/roadmap/RDM**V0.md - ops/templates/rules/RULES**V0.md - ops/templates/checklists/CHK**V0.md - ops/templates/configs/CFG**V0.yaml - ops/templates/setup/SETUP**V0.md - ops/templates/adr/ADR\_0001*\_V0.md - ops/templates/readme/README\_TEMPLATE\_V0.md - ops/templates/contracts/arch\_contracts.toml - ops/templates/tests/test\_substitution\_contract.py - ops/scripts/GENERATOR\_NOTES.md result: - status: package\_ready log: - step1: generate - step2: assemble - step3: validate\_meta


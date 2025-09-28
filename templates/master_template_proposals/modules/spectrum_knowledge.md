---
asset:
  id: "<% tp.date.now('YYYYMMDDHHmm') %>_SPECTRUM_MODULE_<% tp.file.title.replace(/\\s+/g, '_').toUpperCase() %>"
  name: "<% tp.file.title %>"
  type: module_template
  parent: obsidian_master_template_aingz_master
  version: "0.1.0"
  owner: "AingZ_Platform"
  status: "draft"
  tags:
    - obsidian/module
    - spectrum/knowledge
  created: "<% tp.date.now('YYYY-MM-DD') %>"
  updated: "<% tp.date.now('YYYY-MM-DD') %>"
context:
  knowledge_domain: "AI_Sustainability"
  evidence_maturity: "hypothesis"
  retention_policy: "permanent"
compat:
  platforms: ["Obsidian", "Notion"]
  plugins:
    required: ["Templater", "Dataview", "Buttons", "QuickAdd"]
    optional: ["DataviewJS", "Canvas", "BRAT"]
ai_handshake:
  codex:
    mode: "structured_markdown"
    output_contract: "Mantener tablas y callouts de evidencias intactos; actualizar referencias cruzadas."
    prompts:
      - "Etiquetar cada evidencia con metadata mínima"
      - "Sugerir next steps en formato checklist"
  gpt5:
    mode: "reasoning_markdown"
    output_contract: "Documentar inferencias y supuestos en secciones 30 y 40."
    prompts:
      - "Evaluar madurez de conocimiento y brechas"
      - "Proponer enlaces a repositorios externos"
---

# {{VALUE:knowledge_asset?Knowledge Spectrum}}

> [!summary] Módulo Spectrum · Conocimiento
> Para consolidar aprendizajes con `context.knowledge_domain = <tema>`.
>
> - Dominio: `<% tp.frontmatter()["context"].knowledge_domain %>`
> - Madurez de evidencia: `<% tp.frontmatter()["context"].evidence_maturity %>`
> - Política de retención: `<% tp.frontmatter()["context"].retention_policy %>`

---

## 10 · Contexto Estratégico

> [!quote] Marco conceptual
> Explica por qué este conocimiento es crítico para el dominio seleccionado.

> [!example]- Highlights
> - Evidencia clave: _...
> - Origen de datos: _...
> - KPI de adopción: _...

> [!faq]- Preguntas abiertas
> - ¿Qué supuestos deben validarse?
> - ¿Qué equipos consumen este conocimiento?
> - ¿Qué dependencias externas existen?

---

## 20 · Flujo Operativo

> [!todo]+ Cadena de curación
> 1. **Capturar** → incorporar fuentes en bruto.
> 2. **Analizar** → extraer hallazgos y clasificarlos.
> 3. **Sintetizar** → generar resúmenes y KPIs.
> 4. **Difundir** → actualizar repositorios y notificar a stakeholders.

### 20.1 · Lista de acciones

- [ ] Normalizar taxonomía `knowledge_domain` (owner: )
- [ ] Validar credibilidad de fuentes (owner: )
- [ ] Publicar síntesis en plataforma objetivo (owner: )
- [ ] Registrar feedback de usuarios (owner: )

```tasks
not done
path includes <% tp.file.title %>
short mode
```

> [!tip] Usa QuickAdd `Spectrum · Nueva Evidencia` para capturar notas rápidas vinculadas.

---

## 30 · Data & Inteligencia

> [!info] Dataview de evidencias
> Filtra notas por `context.knowledge_domain` y estado de madurez.

```dataview
TABLE file.mtime as "Última edición", evidence_type, confidence, next_step
FROM ""
WHERE knowledge_domain = "<% tp.frontmatter()["context"].knowledge_domain %>" AND evidence_maturity = "<% tp.frontmatter()["context"].evidence_maturity %>"
SORT confidence DESC
```

> [!hint]- Extensiones
> - Embebe visualizaciones (`![[data/spectrum/<domain>.svg]]`).
> - Usa `dataviewjs` para calcular coverage por categoría.

---

## 40 · Impacto & Sostenibilidad

> [!todo]+ Indicadores de conocimiento
> - `knowledge_reuse_rate` (% equipos reutilizando el asset)
> - `evidence_refresh_cadence` (días)
> - `sustainability_alignment_score` (0-100)

```tracker
searchType: frontmatter
searchTarget: sustainability_alignment_score
datasetName: "Alineación"
line:
  title: "Score"
  color: "#1F6FEB"
```

> [!warning] Si `evidence_refresh_cadence` supera el umbral pactado, activar revisión colaborativa con AI↔humano.


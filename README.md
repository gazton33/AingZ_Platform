---
file: README.md code: RDMN name: ReadmeMain version: v5.0.0 date: 2025-08-24 owner: "AingZ_Platform · RwB" status: wip
---

# AingZ Platform – Arquitectura V5

Repositorio base para la implementación de la arquitectura V5. Mantiene los baselines bloqueados y las plantillas operativas para el desarrollo sostenible.

## Estructura principal
- `main/` – contiene la base de datos operativa (glosario, ruleset, dir tree) y artefactos core.
- `V5/` – plantillas y minipacks oficiales para generar artefactos.
- `legacy/` – material heredado pendiente de migración o archivado.
- `ruleset/` – bucket central con el ruleset maestro y sus referencias.
- `templates/` – punto de entrada para los formularios maestros (documentación operativa y arquitectura).

## Ruta de contexto para nuevas sesiones

> [!summary] Inicio rápido para IA (Codex/GPT5) y humanos
> 1. **Reglas y contratos** → lee el [Ruleset maestro](ruleset/ruleset_master_v_1.md) para alinear modos de colaboración.
> 2. **Master template validado** → sigue `templates/master_template_proposals/README.md` y aplica [[templates/master_template_proposals/obsidian_master_template_aingz_master.md|A·Master Template · Orbit-Spectrum V1]].
> 3. **Context pack operativo** → carga [[templates/master_template_proposals/context_packages/orbit_spectrum_master_template_context_pack_v1.md]] para recuperar acuerdos y dependencias previas.
> 4. **Arquitectura** → usa `templates/architecture_interactive_forms/README.md` para seleccionar el formulario adecuado.
> 5. **Dir Tree + Excalidraw** → trabaja con [[templates/architecture_interactive_forms/dir_tree_creator_form.md]] como baseline sincronizado Mermaid/Excalidraw.
> 6. **Legacy de soporte** → consulta `templates/master_template_proposals/legacy_reference_pool/README.md` y `templates/architecture_interactive_forms/legacy_reference_pool/README.md` para evitar releer el repositorio completo.

## Reglas generales
1. Los baselines bloqueados residen en `core/doc/workbench` y son la fuente de verdad.
2. Toda nueva documentación debe incluir front‑matter válido y un OutputTemplate explícito.
3. `wf_playbooks` reemplaza a `wf_template` en la estructura V5.
4. Respetar los bloques interactivos protegidos de las plantillas (Buttons, Dataview, Tasks, Tracker) para mantener la colaboración IA↔humana.

## Formularios clave y recursos

| Ruta | Propósito | Notas |
| ---- | --------- | ----- |
| `templates/master_template_proposals/README.md` | Índice del master template validado y propuestas Next Gen. | Mantiene contratos Codex/GPT5 y lineamientos de adopción. |
| `templates/architecture_interactive_forms/README.md` | Guía de formularios de arquitectura. | Incluye integración con Excalidraw y KPIs de arquitectura. |
| `templates/architecture_interactive_forms/obsidian_architecture_master_form.md` | Formulario maestro para diseñar y auditar arquitectura. | Usa Tabs, Buttons, Dataview y WK.log. |
| `templates/architecture_interactive_forms/dir_tree_creator_form.md` | Blueprint de árboles de directorios con Mermaid + Excalidraw. | Baseline oficial para evolucionar el dir tree. |
| `templates/architecture_interactive_forms/architecture_assets_inventory.md` | Inventario de assets y árboles actuales. | Referencia rápida para auditorías y asignación de owners. |
| `templates/master_template_proposals/legacy_reference_pool/README.md` | Pool de decisiones y reglas históricas del master template. | Registra experimentos y acuerdos previos. |
| `templates/architecture_interactive_forms/legacy_reference_pool/README.md` | Legacy para formularios de arquitectura. | Adjunta snapshots, evidencias y feedback. |

## Output Template
```markdown
# Título
Contenido...
```

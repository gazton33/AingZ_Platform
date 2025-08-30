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

## Reglas generales
1. Los baselines bloqueados residen en `core/doc/workbench` y son la fuente de verdad.
2. Toda nueva documentación debe incluir front‑matter válido y un OutputTemplate explícito.
3. `wf_playbooks` reemplaza a `wf_template` en la estructura V5.

Para obtener lineamientos unificados de todas las plataformas (ChatGPT, Codex, VSCode, GitHub, Obsidian, Excalidraw), consultar el [Ruleset maestro](ruleset/ruleset_master_v_1.md).

## Output Template
```markdown
# Título
Contenido...
```

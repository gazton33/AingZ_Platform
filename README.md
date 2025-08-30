---
file: README.md code: RDMN name: ReadmeMain version: v5.0.0 date: 2025-08-24 owner: "AingZ_Platform · RwB" status: wip
---

# AingZ Platform – Arquitectura V5

Repositorio base para la implementación de la arquitectura V5. Mantiene los baselines bloqueados y las plantillas operativas para el desarrollo sostenible.

## Estructura principal
- `main/` – contiene la base de datos operativa (glosario, ruleset, dir tree) y artefactos core.
- `V5/` – plantillas y minipacks oficiales para generar artefactos.
- `legacy/` – material heredado pendiente de migración o archivado.

## Reglas generales
1. Los baselines bloqueados residen en `core/doc/workbench` y son la fuente de verdad.
2. Toda nueva documentación debe incluir front‑matter válido y un OutputTemplate explícito.
3. `wf_playbooks` reemplaza a `wf_template` en la estructura V5.

## Output Template
```markdown
# Título
Contenido...
```

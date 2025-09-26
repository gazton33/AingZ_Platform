---
asset:
  id: "inventory_architecture_assets_v1"
  type: knowledge_base
  version: "1.0.0"
  owner: "AingZ_Platform"
  status: "active"
tags:
  - architecture
  - inventory
  - obsidian/reference
updated: "2024-09-30"
---

# Inventario de Assets · Arquitectura Plataforma AingZ

> [!info] Propósito
> Proporcionar un mapa rápido de carpetas, plantillas y artefactos clave para orquestar la arquitectura de plataforma dentro del repositorio `AingZ_Platform`.

## Directorios raíz relevantes

| Carpeta | Enfoque | Notas clave |
| ------- | ------- | ----------- |
| `core/` | Documentación y workbench operativos | Contiene cuadernos de trabajo en `doc/workbench` y artefactos bloqueados para baseline V5. |
| `legacy/` | Historial y versiones previas | Útil para rastrear evoluciones de reglas y plantillas. |
| `main/` | Activos funcionales actuales | Incluye implementaciones y configuraciones en curso. |
| `new_repo_pack/` | Paquetes de arranque | Base para generar nuevos repositorios alineados a la metodología AingZ. |
| `ruleset/` & `ruleset_pack_v1/` | Normativas vigentes | Reglas y contratos maestros que gobiernan plantillas y operaciones. |
| `templates/master_template_proposals/` | Plantillas maestras validadas | Aloja el Orbit·Spectrum V1 y el Legacy Reference Pool asociado. |
| `V5/` | Material específico de la versión 5 | Incluye planes (`TREE_PLAN`, `SWEEP_PLAN`) y artefactos estratégicos. |
| `scripts/` | Automatizaciones y utilidades | Scripts de soporte para workflows técnicos. |

## Artefactos destacados

- `platform_arch_v5.excalidraw` · Mapa visual de arquitectura actual, ideal para enlazar desde formularios interactivos.
- `codex_chatgpt5_config.md` · Configuración de colaboración entre modelos Codex/GPT5.
- `aing_z_ruleset_max_universal_v_1_0_template.md` · Referencia extendida de reglas universales.
- `templates/master_template_proposals/obsidian_master_template_aingz_master.md` · Master template validado Orbit·Spectrum V1.
- `templates/master_template_proposals/legacy_reference_pool/README.md` · Índice de referencias históricas para iteraciones futuras.

## Vínculos sugeridos

- `[[ruleset/ruleset_master_v_1]]`
- `[[templates/master_template_proposals/obsidian_master_template_aingz_master|Orbit·Spectrum V1]]`
- `[[templates/master_template_proposals/legacy_reference_pool/README|Legacy Reference Pool]]`
- `![[platform_arch_v5.excalidraw]]`

## Próximos pasos

- [ ] Actualizar este inventario al incorporar nuevos repositorios satélite.
- [ ] Añadir referencias a dashboards o monitoreo externo (Grafana/Prometheus) cuando estén disponibles.
- [ ] Enlazar decisiones registradas en `obsidian_architecture_master_form` una vez activado.

> [!tip] Dataview
> Convierte esta nota en panel navegable con `TABLE file.link, asset.status WHERE contains(tags, "architecture")` para listar rápidamente todos los formularios activos.


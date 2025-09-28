---
asset_id: orbit_spectrum_master_template_context_pack
asset_name: OrbitSpectrumMasterTemplateContextPack
asset_version: 1.0.0
asset_owner: AingZ_Platform
last_update: 2025-09-02
compat_agents:
  - Codex
  - GPT5
compat_platforms:
  - Obsidian
  - VSCode
  - GitHub
  - CodexCLI
status: active
---

# Orbit·Spectrum Master Template · Context Pack v1.0

> Paquete de contexto para iniciar nuevas iteraciones del [[obsidian_master_template_aingz_master|A·Master Template · Orbit-Spectrum V1]] sin releer el repositorio completo.

---

## 1. Propósito y alcance
- Centralizar instrucciones operativas, contratos IA↔humano y enlaces críticos del master template validado.
- Servir como punto de partida para nuevos hilos de trabajo con Codex o GPT5 en ausencia de historial previo.
- Registrar avances confirmados y experimentos fallidos para evitar retrabajo.

---

## 2. Navegación esencial
| Recurso | Descripción | Uso inmediato |
|---------|-------------|----------------|
| [[obsidian_master_template_aingz_master]] | Plantilla validada Orbit·Spectrum V1 | Insertar en notas nuevas (QuickAdd/Templater). |
| [[next_gen_master_templates/README]] | Catálogo Nexus · Orbit Continuum · Spectrum | Referencia comparativa para futuras mejoras. |
| [[legacy_reference_pool/README]] | Índice de legados y experimentos previos | Consultar decisiones históricas y anexos. |
| [[assets_landscape_analysis.md]] | Análisis integral de assets Markdown | Validar KPIs y requisitos técnicos. |
| [[context_packages/orbit_spectrum_master_template_context_pack_v1|Este context pack]] | Punto de partida para nuevas sesiones | Revisar antes de ejecutar cambios. |

---

## 3. Flujo recomendado según plataforma
### 3.1 Obsidian
1. Cargar plugins mínimos: Dataview, Templater, QuickAdd, Buttons, Tracker, Excalidraw, Tasks, Admonition.
2. Ejecutar `QuickAdd → MT · Nueva Nota` o `Templater → Insert template → A·Master Template · Orbit-Spectrum V1`.
3. Completar frontmatter y seguir la sección `[[obsidian_master_template_aingz_master#00 · Setup Rápido]]`.
4. Documentar feedback en `## 50 · Feedback y WK.log` y anexar evidencias al `[[legacy_reference_pool/README]]`.

### 3.2 VSCode / GitHub
- Utilizar Markdown Preview para validar estructura y callouts.
- Mantener la jerarquía `templates/master_template_proposals/` y actualizar README tras cada cambio.
- Confirmar que los bloques de código y botones se conservan; no convertir wikilinks a enlaces planos.

### 3.3 Codex / GPT5
- Inyectar este context pack + plantilla objetivo en el prompt inicial.
- Recordar que los bloques protegidos (`Buttons`, `Dataview`, `Tracker`) son obligatorios.
- Registrar decisiones en `## 40 · Impacto` y escalar hallazgos al legacy pool cuando corresponda.

---

## 4. Contratos IA↔humano
- **Handshake inicial**: respetar campos `ai_role`, `human_role`, `ruleset_anchor` definidos en el frontmatter.
- **Tareas iterativas**: usar `## 20 · Flujo de trabajo` para coordinar entregas Codex/GPT5 ↔ humano.
- **Feedback continuo**: consolidar aprendizajes en `## 50 · Feedback y WK.log` y etiquetar con fecha ISO.

---

## 5. Registro de avances y pruebas
| Fecha | Acción | Resultado |
|-------|--------|-----------|
| 2025-09-02 | Validación del [[obsidian_master_template_aingz_master]] como base obligatoria. | ✅ Adoptado en README principal. |
| 2025-09-02 | Creación del `legacy_reference_pool` dedicado a plantillas y ruleset. | ✅ Disponible para consultas rápidas. |
| 2025-09-02 | Diseño Orbit·Spectrum Prime y propuestas Nexus/Orbit Continuum/Spectrum. | ✅ Listas para evaluación comparativa. |
| 2025-09-02 | Automatización/Tests sobre bloques interactivos. | ⚠️ Pendiente: no se han ejecutado pruebas automatizadas; requiere validación manual en Obsidian. |

> [!note] Pruebas negativas registradas
> - No se ejecutaron tests automatizados; documentado para evitar suposiciones de cobertura.
> - Falta validar botones y trackers en un vault limpio (tarea abierta).

---

## 6. Próximos pasos sugeridos
1. Auditar alineación con `ruleset/` y `core/doc/workbench` para incorporar requisitos faltantes.
2. Desarrollar módulos derivados (Orbit proyectos, Spectrum conocimiento) en `[[next_gen_master_templates/README]]`.
3. Configurar dashboard de KPIs (`TemplateCoverage`, `InteractionDepth`, `SustainabilityTrace`, `FeedbackLoopTime`).
4. Registrar quincenalmente ajustes y aprendizajes en `legacy_reference_pool` siguiendo convención `YYYYMMDD_change_log.md`.

---

## 7. Historial de revisiones
- **v1.0.0 (2025-09-02):** Primera publicación del context pack para el Master Template Orbit·Spectrum V1. Resume lineamientos operativos, recursos clave y pruebas pendientes.

> Mantener este documento sincronizado con GitHub/Obsidian. Cualquier cambio debe ir acompañado de una anotación en `[[legacy_reference_pool/README]]` y actualización del índice principal.

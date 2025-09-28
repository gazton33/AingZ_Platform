# Dir Tree Draft · Alignment Plan

## 1. Alcance y objetivos inmediatos
- Confirmar la capacidad para leer y versionar el recurso `dir_tree_draft.excalidraw` como insumo maestro del árbol de directorios.
- Extraer y documentar los nodos principales para sincronizar el borrador con implementaciones en curso de plantillas y formularios.
- Establecer un flujo híbrido Excalidraw ⇄ Markdown/Mermaid que permita mantener la arquitectura viva y auditable.

## 2. Capacidad de lectura del `.excalidraw`
- El archivo es JSON con compresión interna. Podemos inspeccionarlo directamente (`sed`, `jq`) o utilizar la variante `dir_tree.excalidraw.md`, que ya expone los *Text Elements* relevantes (por ejemplo: `/data_base`, `/rulesets`, `/brainstorm`, `/planin`).
- Para obtener la versión editable desde la terminal:
  1. Copiar el bloque `compressed-json` y descomprimirlo con el comando del plugin (`palette: Decompress current Excalidraw file`) o con un script Node/Python que implemente `lz-string`.
  2. Convertir el JSON resultante en un arreglo de nodos (id, texto, posición) que podemos reutilizar para generar estructuras auxiliares (YAML, Markdown, Mermaid).
- Con esta metodología garantizamos trazabilidad: cualquier modificación en Excalidraw puede auditarse en Git y sincronizarse con representaciones textuales.

## 3. Inventario del borrador actual
Relevamiento inicial de nodos (extraídos de `dir_tree.excalidraw.md`):
- **Capas base**: `/data_base`, `/rulesets`, `/packages`, `/scripts`, `/log`, `/qms`, `/core_actv`, `/core_dev`, `/core_arch_platform`.
- **Árboles funcionales**: `/rlst_arch` (platform_arch, dir_tree, life_cicle, dict_apps), `/rlst_human`, `/rlst_llm`, `/rlst_api`, `/rlst_platform`, `/rlst_apps` (chat_gpt, openai_api, codex, git_hub, obsidian, excalidraw).
- **Repositorios multimedia**: `/docs`, `/audio`, `/image`, `/video`, `/library` tanto en raíz como en carpetas específicas (`/projects`, `/ai_llm`, `/semantics`).
- **Workflows y outputs**: `/wf_template` (creator, relev, auditoria, migracion, update, validation, report, clone), `/workflows`, `/playbooks`, `/pipeline`, `/forms_in`, `/templ_out`.
- **Planificación y exploración**: `/planin` (master_plan, blueprint, baseline, roadmap, plans, task/checklist, feedback), `/brainstorm` (insights, ideas, snapshots, research, diver/conver).
- **Diccionarios y semántica**: `/semantics` (glossary, dict_code, dict_trigger, dict_prompt, dict_api, dict_apps, vocabulary, naming).
- **Ámbitos de datos/aprendizaje**: `/ai_llm` (data, learn, kns_ctx), `/kns_ctx_vivo`, `/ctx`, `/mem_viva`.

Estos elementos constituyen el *baseline* más actualizado y servirán como referencia para nuevas plantillas y formularios iterativos.

## 4. Estrategia Excalidraw ⇄ Mermaid
1. **Normalización de nodos**: exportar los elementos de texto a una estructura `YAML` (`type`, `path`, `descripcion`).
2. **Generación Mermaid**: a partir del YAML producir diagramas `mindmap` o `graph TD` que reflejen jerarquías. Esto permite incrustar la arquitectura en documentación Markdown y mantener sincronización automática.
3. **Ciclo de actualización**:
   - Editar en Excalidraw cuando se requiera trabajo visual colaborativo.
   - Registrar cambios en `dir_tree.excalidraw.md` (modo texto) para auditorías rápidas.
   - Re-generar el YAML y los gráficos Mermaid (scripts en `scripts/diagram_sync/` — a crear).
4. **Control de versiones**: cada commit debe incluir la versión `.excalidraw`, su `.md` asociado y los derivados Mermaid para evitar divergencias.

## 5. Próximos pasos operativos
- **P1 – Sincronización de baseline**: traducir el inventario de nodos a un `dir_tree_baseline.yaml` que sirva de fuente única para formularios y plantillas.
- **P2 – Scripts de sincronización**: preparar utilidades (Python/Node) que permitan descomprimir, parsear y exportar el árbol automáticamente.
- **P3 – Diagramas Mermaid**: generar al menos un `graph TD` y un `mindmap` documentando la arquitectura actual para revisión.
- **P4 – Integración con formularios**: enlazar `dir_tree_creator_form.md` con el YAML baseline para alimentar campos dinámicos y validar cobertura.
- **P5 – Métricas y gobernanza**: definir KPIs (`TemplateCoverage`, `InteractionDepth`, `SustainabilityTrace`) que se calculen contra el baseline para auditar evoluciones.

Con esta hoja de ruta confirmamos la lectura del borrador y establecemos un flujo sólido para consolidar la arquitectura mediante Excalidraw y Mermaid.

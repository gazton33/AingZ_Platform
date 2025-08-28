# AingZ\_Platform · Matriz de Conectores Gratuitos (v2 ‑ jul‑2025)

[BARRIDO\_LITERAL]

> **Propósito**: ampliar la versión v1 con nuevos conectores solicitados (Notion, LangChain, etc.) y mantener nomenclatura estándar para trazabilidad.

## 1 · Tabla comparativa “versus” (ampliada)

| #  | Conector / App                     | Categoría                | Función general                                | Aplicación AingZ\_Platform                     | Punto de integración†                               | Naming sugerido          |
| -- | ---------------------------------- | ------------------------ | ---------------------------------------------- | ---------------------------------------------- | --------------------------------------------------- | ------------------------ |
| 1  | Draw\.io GitHub App / VS Code ext. | Diagramas WYSIWYG        | Editar `.drawio`, exportar SVG, diff visual PR | Diagramas infra y flujos                       | Carpeta `/diagrams` + PR                            | CNX.DI.drawio            |
| 2  | Mermaid (nativo GitHub)            | Diagramas como código    | Render Markdown→SVG                            | Docs técnicas                                  | Cualquier `.md`                                     | CNX.DI.mermaid           |
| 3  | PlantUML Action                    | UML texto                | CI `.puml`→SVG                                 | Modelado UML                                   | Action `render-plantuml`                            | CNX.DI.plantuml          |
| 4  | D2 Action                          | DSL moderno diagramas    | CI `.d2`→SVG                                   | Infra‑as‑code visual                           | Action `terrastruct/d2-action`                      | CNX.DI.d2                |
| 5  | Obsidian‑Git                       | Sync notas ↔ Git         | Push automático vault                          | Knowledge base en repo                         | Vault `obsidian/` rama `knowledge`                  | CNX.SYNC.obs\_git        |
| 6  | Obsidian‑GDrive‑Sync               | Backup vault ↔ Drive     | Redundancia & trabajo móvil                    | Backup en Google Drive                         | Google Drive folder                                 | CNX.SYNC.obs\_gdrive     |
| 7  | Dropbox‑folder sync / Action       | Backup artefactos        | Copia fría de releases                         | Resguardo SVG/PDF                              | `/backups/dropbox` + secret TOKEN                   | CNX.SYNC.dropbox         |
| 8  | GDrive‑upload Action               | Distribución builds      | Sube datasets/release                          | Compartir externos                             | Action `gdrive-upload`                              | CNX.SYNC.gdrive          |
| 9  | GitLens (VS Code)                  | IDE / Git UX             | Blame, history, PR in‑editor                   | Auditoría y trazabilidad de código             | Extensión VS Code                                   | CNX.IDE.gitlens          |
| 10 | Draw\.io‑for‑Obsidian              | Diagramas en notas       | Edita `.drawio` in‑vault                       | Diagramas + texto juntos                       | Plugin Obsidian                                     | CNX.DI.obs\_drawio       |
| 11 | Mermaid Preview (VS Code)          | IDE render               | Preview en vivo Mermaid                        | Refactor rápido                                | Extensión VS Code                                   | CNX.IDE.mermaid\_preview |
| 12 | tldraw (self‑host/SDK)             | Pizarra colaborativa     | Canvas realtime, export SVG                    | Ideación visual remota                         | GH Pages / React app                                | CNX.CANVAS.tldraw        |
| 13 | **Notion API + GitHub Action**     | Knowledge / Docs         | Sincronizar bases Notion ↔ Issues/PR           | Documentación ejecutiva, tareas OKR            | Action `notion-sync-action` + secret TOKEN          | CNX.KN.not\_git          |
| 14 | **LangChain (Python)**             | AI / Orquestación LLM    | Framework pipelines LLM, embeddings, agents    | Orquestar GPT‑4, llamada a embeddings propios  | Carpeta `/ai/langchain` + requirements.txt          | CNX.AI.langchain         |
| 15 | **n8n (open‑source iPaaS)**        | Automatización workflows | Low‑code flows: GitHub → Slack → Notion        | Alertas CI/CD, hooks de PR, backups            | Self‑host Docker `infra/n8n/` + Webhook URLs        | CNX.AUTO.n8n             |
| 16 | **Airbyte (open‑source ELT)**      | Integración de datos     | Conectores ETL 300+, sync JSON/DB → S3/GDrive  | Ingesta datasets externos para IA              | Self‑host Docker `infra/airbyte/` + dumps           | CNX.DATA.airbyte         |
| 17 | **Zapier (Free tier)**             | Automatización SaaS      | Triggers GitHub ↔ G Drive/Dropbox/Notion       | Flujos rápidos sin código (máx 100 tareas/mes) | Zap templates referenciados en `automation/zapier/` | CNX.AUTO.zapier          |
| 18 | **Slack‑GitHub Integration**       | Comunicación             | Notificaciones PR / CI en Slack                | Feedback instantáneo en equipo                 | Slack app + webhook GitHub                          | CNX.COMM.slack\_github   |

†*Punto de integración* = carpeta, acción CI, ruta Docker o extensión.

---

## 2 · Nomenclatura estandarizada (sin cambios)

```
<AingZ_Platform>.<LAYER>.<ROLE>.<tool>[.<qualifier>]
```

- **LAYER** → DI, SYNC, IDE, CANVAS, KN (knowledge), AI, AUTO, DATA, COMM.
- **ROLE** → descrito en la tabla.
- **Qualifier** opcional.

---

## 3 · Prioridades de adopción Q3‑2025

1. **Notion API sync** para documentar OKR y key decisions (alta visibilidad).
2. **LangChain skeleton** en módulo `/ai/` para pipelines (prototipo POC).
3. **n8n docker‑compose** integrando GitHub → Slack → Notion hooks.
4. Onboard **Slack‑GitHub** bot en canal `#rwb-dev`.
5. PoC **Airbyte** para ingestión de CSV históricos de proyectos.
6. Configurar **Zapier** flujos ligeros mientras se madura n8n.

---

## 4 · Checklist RwB (BARRIDO\_LITERAL)

-

---

> **Fin Matriz v2 – lista para merge en rama **``**.**


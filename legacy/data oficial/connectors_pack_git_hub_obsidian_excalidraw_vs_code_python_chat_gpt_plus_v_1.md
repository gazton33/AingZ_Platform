# Connectors Pack — GitHub, Obsidian, Excalidraw, VS Code, Python (ChatGPT Plus)

**Fecha:** 27‑Ago‑2025  
**Plan:** ChatGPT **Plus**  
**Objetivo:** unificar instalación, límites y *playbooks* para usar **Conectores** y flujos equivalentes con tu stack: **GitHub, Obsidian, Excalidraw, VS Code y Python**.

---

## 0) Visión rápida
- **Conectores nativos**: GitHub, Google Drive, SharePoint/OneDrive, Teams, Box, Dropbox, Notion, HubSpot, Canva, Gmail/Calendar/Contacts (según plan y región).  
- **Synced connectors**: **Google Drive** y **GitHub** con indexado previo para respuestas más rápidas.  
- **Deep Research** y **Chat** pueden usar conectores; **Projects** hoy no soporta conectores.  
- **VS Code**: integración “Work with Apps” vía extensión para que ChatGPT lea/edite archivos abiertos.  
- **Python/Data Analysis**: ejecución sandbox para análisis; complementa conectores (no los reemplaza).

---

## 1) GitHub
### 1.1 Qué permite
- Buscar y citar código, PRs, issues y docs en chat o en Deep Research.  
- Filtrar por repositorios autorizados; control de acceso repo‑a‑repo.

### 1.2 Instalación
1) **Settings → Connectors → GitHub**.  
2) Autorizar en GitHub y elegir repos a exponer.  
3) Opcional: habilitar como **Synced connector** para indexado.

### 1.3 Uso
- En **Deep Research**: seleccionar **GitHub** en “Sources”.  
- En **Chat**: menciona “buscar en GitHub” o pega URLs de repos; el conector se activa cuando es relevante.  
- En **Agent**: pedir plan de pasos, revisión de un módulo, lista de PRs abiertos y análisis de impacto.

### 1.4 Límites y notas
- Acceso **sólo de lectura**.  
- Respeta permisos de la cuenta GitHub conectada.  
- Indexado *synced* acelera pero no es instantáneo tras cada commit.

### 1.5 Prompts
- *“Usa el conector GitHub y analiza los PRs abiertos en [org/repo] sobre [tema]; devuelve riesgos y cambios sugeridos.”*  
- *“Deep research + GitHub: resume el diseño de [ruta/archivo] y compara con [archivo2]. Cita commits y PRs.”*

---

## 2) Obsidian
> No hay conector nativo. Estrategias equivalentes:

### 2.1 Vía GitHub
- Sincroniza tu **vault** con un repo privado.  
- Conecta ese repo por el conector GitHub y consulta notas con rutas o etiquetas.

### 2.2 Vía Drive/SharePoint
- Sincroniza la carpeta del vault con **Google Drive** o **OneDrive/SharePoint** y habilita el conector.  
- Usa búsquedas por título y contenido; apoya con metadatos en el nombre del archivo.

### 2.3 Plugins locales (opcional)
- Plugins comunitarios de Obsidian para ChatGPT/AI. Úsalos sólo para edición local. No exponen contenido a ChatGPT vía conectores.

### 2.4 Prompts
- *“Busca en mi vault (conector GitHub) las notas con tag #roadmap del último trimestre y arma un resumen con enlaces a cada MD.”*  
- *“Desde Drive (conector), trae las notas de ‘/Research/LLMs/’ y genera tabla con título, fecha y 3 hallazgos.”*

---

## 3) Excalidraw
> No hay conector nativo. Vías de trabajo:

### 3.1 Mermaid → Excalidraw
- Pide a ChatGPT diagramas en **Mermaid**; exporta el código y conviértelo en Excalidraw desde herramientas compatibles.  
- Variante: generar **JSON .excalidraw** básico y abrirlo en la app.

### 3.2 Con Obsidian
- Usa el plugin **Excalidraw** en Obsidian y sincroniza el vault vía GitHub/Drive para que ChatGPT pueda referenciar el contexto textual de las notas asociadas.

### 3.3 Prompts
- *“Crea un diagrama de arquitectura en Mermaid con [nodos], orientado a importarlo en Excalidraw; incluye estilos y comentarios.”*  
- *“Explícale al agente cómo actualizar el diagrama: qué formas y conexiones cambiar para reflejar [cambio].”*

---

## 4) VS Code
### 4.1 Qué permite
- **Work with Apps**: ChatGPT **lee/edita** archivos abiertos en VS Code; sugiere cambios y puede aplicar parches locales.

### 4.2 Instalación
1) Instalar la **extensión oficial** (VSIX o Marketplace).  
2) Abrir el chat de ChatGPT desktop y autorizar VS Code.  
3) Verifica que el IDE muestre el estado “conectado”.

### 4.3 Playbooks
- Revisión por carpeta activa, búsqueda de *code smells*, generación de tests.  
- ¿Refactor masivo? Pide *dry‑run* y diff antes de aplicar.

### 4.4 Prompts
- *“Con VS Code conectado: revisa todos los archivos abiertos y propone un plan de refactor con diffs.”*  
- *“Genera pruebas unitarias para [archivo] usando [framework]; aplica cambios si confirmo.”*

---

## 5) Python / Data Analysis
### 5.1 Qué permite
- Ejecutar **Python** en entorno seguro para análisis, gráficos, validaciones y transformaciones; carga archivos locales o desde conectores.

### 5.2 Patrones
- **ETL ligero**: CSV/Parquet → limpieza → reporte.  
- **Auditoría**: duplicados, nulos, outliers, reglas de negocio.  
- **Visualización**: tablas y gráficos con explicación.

### 5.3 Prompts
- *“Desde Drive (conector), carga ‘/datasets/sales_2025.csv’, limpia y genera dashboard con 6 KPIs; adjunta notebook y CSV final.”*  
- *“Valida este dataset del repo [ruta] con reglas [X]; devuelve un HTML de hallazgos.”*

---

## 6) Seguridad y privacidad
- Revisa **Data Controls** en ChatGPT.  
- Conectores heredan permisos del servicio origen; sé explícito al limitar repos/carpetas.  
- Evita datos sensibles en **Shared Links**.  
- En Plus, los datos pueden entrenar modelos salvo *opt‑out*.

---

## 7) Problemas frecuentes
- **No veo conectores**: revisar plan, región, versión de app y permisos.  
- **Indexado lento**: espera a que el *synced* refresque o fuerza búsqueda directa.  
- **Projects**: hoy no soportan conectores; usa chats generales.  
- **VS Code no conecta**: reinstalar extensión y reautorizar en desktop.

---

## 8) Checklists
**GitHub**: habilitar conector → seleccionar repos → probar búsqueda en chat y Deep Research → configurar synced.  
**Obsidian**: decidir ruta (GitHub o Drive) → configurar sync → probar consultas sobre rutas/tags.  
**Excalidraw**: definir formato (Mermaid/JSON) → establecer pipeline de importación → versionar artefactos en repo.  
**VS Code**: instalar extensión → autorizar → ensayar refactor con diff.  
**Python**: preparar plantillas de notebooks y políticas de salida.

---

## 9) Plantillas de prompt (rápidas)
- **Deep Research + GitHub**: *“Analiza el diseño de [carpeta] y las decisiones en PRs recientes; cita fuentes y riesgos.”*  
- **Chat + Drive**: *“Busca en ‘/Obsidian/Research/AI/’ y resume 5 puntos por nota con fecha y enlace.”*  
- **Agent**: *“/agent Usa navegador y GitHub para listar issues ‘perf’ y proponer fixes; pausa antes de abrir enlaces externos.”*  
- **Python**: *“Audita [dataset] de [conector]; produce reporte HTML, CSV limpio y notebook adjunto.”*

---

## 10) Mapa de límites (Plus)
- Conectores: disponibilidad y cupos varían por plan/región.  
- GitHub en Deep Research: acceso beta en algunos despliegues.  
- Synced: Google Drive y GitHub.  
- Projects: sin conectores por ahora.

---

## 11) Roadmap interno (sugerido)
- Definir repos/carpetas “fuente única de verdad”.  
- Estandarizar nombres y metadatos en notas Markdown.  
- Versionar diagramas y assets de Excalidraw.  
- Mantener prompts y *playbooks* en un repo público/privado.


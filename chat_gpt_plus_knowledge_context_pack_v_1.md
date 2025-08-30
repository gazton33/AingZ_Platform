# ChatGPT Plus — Knowledge & Context Pack v1.0

**Fecha:** 27‑Ago‑2025  
**Ámbito:** Uso en **ChatGPT Plus** (web, Windows, Android). Enfoque en Deep Research, Agent Mode, Projects, Connectors, Data Analysis, Canvas, GPTs, Sora, Codex, Personalización y Controles de datos.

---

## 1) Resumen ejecutivo
- ChatGPT Plus ofrece acceso prioritario a nuevas funciones y modelos, con límites de uso variables por región y carga del sistema.
- Capacidades clave: **Deep Research**, **Agent Mode**, **Projects** con **Project‑only memory**, **Connectors**, **Data Analysis** (Python), **Canvas**, **Voice**, **Images** (crear/editar), **Tasks**, **Shared Links** y apps de escritorio/móvil.
- Modelos recientes: familia **GPT‑5** disponible en ChatGPT; la disponibilidad concreta por plan y región puede variar.

---

## 2) Plataformas
### 2.1 Web (chatgpt.com)
- Acceso a todas las herramientas según plan y región.
- Gestión de **Settings → Personalization**: Custom Instructions, Personalities, Memory, Data Controls.

### 2.2 Windows app
- Atajo **Alt + Space** para abrir el **Companion Window**.
- Subir archivos, tomar capturas, usar navegación y herramientas desde el escritorio.

### 2.3 Android app
- App oficial en **Google Play**. Soporta historial, voz, imágenes y carga de archivos; paridad de herramientas puede diferir por región.

> Nota: **Record mode** está hoy soportado en macOS app; se documenta por completitud (ver §8.5).

---

## 3) Modelos y selección
- Selector de modelo dentro del chat o proyecto.
- **GPT‑5** es el predeterminado en ChatGPT. Opciones en el selector: **Auto**, **Fast** y **Thinking**.
- **Thinking** aplica razonamiento ampliado en tareas complejas. Límites y contexto pueden variar; referencia reciente: hasta ~196k tokens de contexto y cupos semanales visibles en la UI.
- Para latencia baja usa **Fast**. Cambia a modelos anteriores sólo si lo necesitas.

---

## 4) Herramientas principales en Plus
### 4.1 Deep Research
- Investigación multi‑paso con citación automática; puede combinar web + archivos del proyecto + conectores permitidos.
- Arranque desde **Tools → Deep research** o desde **Agent Mode** con visual browser.
- Límites de uso mensuales existen; visibles en la UI y sujetos a plan/región.

**Entregables esperados**: Resumen ejecutivo, hallazgos con citas, metodología y anexos de fuentes.

### 4.2 ChatGPT agent
- Agente que **razona, navega y actúa** en tu nombre con control humano en el bucle.
- Herramientas: **navegador visual**, **Data Analysis (Python)**, **conectores** y **terminal** en comandos soportados.
- Flujo: muestra un **plan de pasos**, ejecuta, pausa ante acciones sensibles y registra enlaces.
- Uso típico: formularios, scraping light, hojas de cálculo, flujos repetibles.

### 4.3 Projects
- Espacios de trabajo con chats, archivos y **Project Instructions**.
- **Project‑only memory**: la memoria sólo se usa dentro del proyecto y no contamina otros chats. Requiere Memory activada.
- Herramientas disponibles dentro del proyecto: Deep Research, Voice, Canvas, Data Analysis.
- Nota: hoy los **conectores** aún no están soportados dentro de Projects (se usan en chats generales).

### 4.4 Connectors
- Conecta fuentes externas de forma segura (Drive, OneDrive/SharePoint, Box, Dropbox, GitHub, Gmail/Calendar/Contacts, Teams, Notion, Canva, HubSpot, etc., según plan y región).
- **Synced connectors**: hoy **Google Drive** y **GitHub**. Inyectan contenido relevante automáticamente en respuestas.
- **Chat search / Deep research connectors**: exponen búsqueda en conectores dentro del chat o deep research. Algunas integraciones están limitadas fuera de EEA/CH/UK.
- Revisa **permisos** y políticas en cada conector; puedes incluir o excluir un conector desde el prompt.

### 4.5 Data Analysis (Python)
- Cargar CSV/Excel/Parquet, crear tablas interactivas y gráficos, ejecutar notebooks y auditorías de datos.

### 4.6 Canvas
- Interfaz lateral para **co‑edición** de documentos y código.
- Disponible en **Web, Windows y macOS**. Próximamente en móviles.
- Atajos: abrir como canvas desde el compositor; compartir canvases.

### 4.7 Images (crear/editar)
- Crear y **editar** imágenes dentro del chat. Biblioteca de imágenes centralizada.
- Respeta política de contenidos; no uses material con copyright sin permiso.

### 4.8 Voice
- Modo voz unificado en web, desktop y móvil con mayor expresividad.
- Conversaciones interrumpibles y respuesta en tiempo real.

### 4.9 Tasks
- **Tareas programadas** desde el chat para recordatorios y automatizaciones.

### 4.10 Shared Links
- Genera enlaces públicos de chats específicos. Evita información sensible.
- La opción **“continuar conversación”** desde enlaces compartidos fue retirada.

---

## 5) GPTs personalizados ("GPTs")
- Creación en **Create GPT** con *Create* y *Configure* (Instructions, Capabilities, Knowledge, Actions).
- **Knowledge**: hasta **20 archivos**, **512 MB** por archivo, **2.0M tokens** por archivo. Solo se procesa el **texto**.
- Privacidad: ajusta **Data Controls** si no quieres que tus chats entrenen modelos en Plus. En planes de negocio, no se usan para entrenamiento por defecto.
- Diferencia con **Projects**: GPT = comportamiento reutilizable; Project = contexto operativo por trabajo.

---

## 6) Codex (agente de ingeniería de software)
- Agente cloud para repositorios: **bug‑fixing, features, tests**, documentación y propuestas de **PR** en sandboxes.
- Acceso desde ChatGPT y **Codex CLI** con inicio de sesión vía cuenta ChatGPT.
- Buenas prácticas: límites de permisos, políticas de ramas y revisión humana de PRs.

---

## 7) Sora (texto‑a‑video)
- Generación de video desde texto/imagen/video. Disponibilidad por país y plan.
- En **Plus**, acceso básico integrado en ChatGPT con salidas **hasta 720p y ~10 s** por clip; límites sujetos a cambios.

---

## 8) Personalización, Memoria y Datos
### 8.1 Custom Instructions y Personalities
- Configurar en **Settings → Personalization**. Define rol, idioma, formato y tono.

### 8.2 Memory
- Control on/off, consultar y olvidar elementos.
- **Project‑only memory** para aislamiento contextual dentro de Projects.

### 8.3 Data Controls
- Desactivar entrenamiento sobre tus chats, exportar datos, borrar cuenta, o usar **Temporary Chat**.

### 8.4 Connectors y privacidad
- Revisa retención y borrado de cada conector. El contenido conectado se elimina al borrar el chat.

### 8.5 Record mode (macOS)
- Disponible para **Plus** en la app de **macOS**. Graba, transcribe y resume reuniones o notas a **canvas**; requiere consentimientos legales.

---

## 9) Prompts operativos (listos para pegar)
### 9.1 Deep Research — estándar
```
Activa Deep research.
Objetivo: [qué necesitas] para [audiencia/decisión].
Alcance: [país/fechas]; profundidad: [breve/medio/exhaustivo].
Fuentes: web + archivos del proyecto + conectores [lista].
Políticas: cita todo lo no trivial; deduplica; marca incertidumbres.
Entregable: resumen ejecutivo, hallazgos con citas, contrastes, riesgos, anexos.
Si falta algo crítico, muestra plan de pasos antes de ejecutar.
```

### 9.2 Deep Research — comparativa estructurada
```
Deep research con tabla por criterios [C1..Cn].
Incluye: feature parity, TCO, riesgos regulatorios por país, señales de adopción.
Anexa metodología y queries usadas.
```

### 9.3 ChatGPT agent — ejecución segura
```
/agent
Tarea: [outcome].
Herramientas: navegador visual, data analysis, conectores [lista], terminal.
Restricciones: sin compras ni formularios sin confirmación; pausa ante logins.
Éxito = [criterio]. Registra pasos y enlaces; propone 2 alternativas si falla algo.
```

### 9.4 Projects — instrucciones de proyecto (plantilla)
```
Contexto: <negocio y dominio>
Fuentes: <archivos, carpetas de Drive/SharePoint, repos>
Tareas prioritarias: <bullets>
Estilo: <guía de tono>
Salida: <JSON schema o plantilla textual>
Criterios de calidad: <tests y métricas>
```

---

## 10) Checklists
**Arranque de proyecto**: (1) crear Project, (2) activar **Project‑only memory** si aplica, (3) cargar archivos, (4) habilitar conectores en Chat si se usarán, (5) fijar Instructions, (6) preparar prompts de Deep Research/Agent, (7) definir esquema de salida y tests.

**Seguridad y privacidad**: (1) ajustar **Data Controls**, (2) revisar permisos y residencia de datos de conectores, (3) usar **Temporary Chat** para pruebas sensibles, (4) evitar datos confidenciales en Shared Links.

**Operación**: (1) monitorear límites de uso y modos de GPT‑5 (Auto/Fast/Thinking), (2) versionar Instructions, (3) mantener Knowledge y fuentes al día.

---

## 11) Glosario mínimo
- **Agent Mode**: ejecución autónoma con herramientas y navegador visual.
- **Deep Research**: investigación guiada multi‑paso con citas.
- **Project‑only memory**: memoria aislada a un proyecto.
- **Synced connectors**: inyección de contenido relevante desde conectores.
- **Canvas**: editor lateral de documentos/código.

---

## 12) Fuentes clave (índice)
- **Help Center**: GPT‑5 in ChatGPT; ChatGPT — Release Notes; Deep Research; ChatGPT agent; Projects; Data analysis; Canvas; Windows app; Shared Links FAQ; Tasks; Voice; Knowledge in GPTs; Connectors + Synced connectors; Admin controls de Connectors; Google Drive Synced Connector.
- **OpenAI Blog/News**: Introducing GPT‑5; GPT‑5 System Card; Introducing ChatGPT agent; Improvements to Data Analysis; Introducing Canvas; Sora.
- **Páginas de producto**: ChatGPT Overview; ChatGPT en desktop.
- **Codex**: Codex in ChatGPT; Codex Changelog; Codex CLI.
- **Sora**: landing y system card.

> Revisa artículos por región/plan, ya que disponibilidad y límites cambian en el tiempo.


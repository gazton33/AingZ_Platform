# FAQ Avanzada — Gestión de Adjuntos, Knowledge y Workflows fuera de Proyectos

> Respuestas a dudas comunes sobre integración de archivos, workflows y conocimiento en chats generales (fuera de proyectos).

---

## 1. ¿Cómo adjunto o referencio archivos de conocimiento, workflows, templates, etc. en un chat fuera de proyectos?

### a. **Adjuntos directos**
- Puedes cargar archivos **manualmente** (PDFs, docs, imágenes, CSV, templates, etc.) usando la función de adjuntos de la plataforma/chat (feature ATT, CORE-06).
- Una vez adjuntos, puedes **pedir resúmenes, análisis, extracción de datos** o integración a memoria durante esa sesión.
- Por defecto, estos adjuntos solo viven en el contexto de ese chat o sesión, **no impactan la knowledge base ni settings globales** salvo acción explícita.

### b. **Referencia a repositorios (Repo de conocimiento)**
- Si ya existe un **repo o carpeta estructurada** (por ejemplo, en GitHub, Notion, Google Drive), puedes **referenciar links directos a los archivos o README**.
- Se recomienda mantener un README de índice de recursos clave (workflows, plantillas, datasets) y compartir el enlace al mismo.
- Puedes instruir al asistente para trabajar “según los lineamientos del repo” o “usar como referencia el archivo X del repositorio”.
- Si la plataforma lo permite, puedes cargar archivos masivamente desde el repo, o bien copiar su contenido relevante al chat.

### c. **Workflows/plantillas universales**
- Puedes **adjuntar workflows en formato markdown, JSON, tablas** o simplemente pegar el contenido en el chat.
- El asistente puede seguir esos pasos, adaptar outputs o reutilizar fragmentos en base a la plantilla enviada, pero solo durante la sesión.
- Si quieres que una plantilla/flujo pase a ser parte del knowledge base global, debes solicitarlo explícitamente ("guarda este workflow como template universal").

---

## 2. ¿Qué limitaciones existen fuera de proyectos?
- **No hay memoria persistente** más allá de la sesión, salvo integración manual con knowledge base.
- Las instrucciones **globales** siguen aplicando (idioma, tono, ética, límites), pero los adjuntos, workflows y outputs no se guardan automáticamente.
- Todo lo que se desea conservar debe ser **registrado a mano** en la knowledge base o repo.

---

## 3. ¿Qué buenas prácticas aplicar?
- Llevar un README/index que centralice todos los recursos y referencias para fácil acceso.
- Si se trabaja con muchos archivos, organizar una carpeta “adjuntos”, otra “plantillas” y otra “workflows” en el repo.
- Para colaboraciones, siempre vincular outputs/insights importantes al archivo de knowledge base para trazabilidad.
- Al terminar el chat, documentar o exportar los outputs relevantes para no perderlos.

---

## 4. **Ejemplo operativo básico**

1. Nuevo chat (no proyecto).
2. Adjunto un workflow.md y un dataset.csv.
3. Solicito: “Analizá el dataset según el flujo de trabajo adjunto. Documenta todo en español y explica los pasos usando mi plantilla”.
4. Al finalizar, exporto el resumen y lo guardo en mi knowledge base para futuras sesiones.

---

¿Quieres un ejemplo paso a paso de integración entre adjuntos y repo, o te gustaría que modele la lógica de versionado y memoria fuera de proyectos?


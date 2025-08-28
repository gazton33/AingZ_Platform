# Capacidades y Limitaciones del Agente (AgentMode)

## Entradas (Inputs)
- **Texto estructurado**: comandos, prompts, archivos `.md`, `.csv`, `.json`.
- **Parámetros de API**: consultas avanzadas sobre GitHub y Google Drive (búsqueda, fetch, listado, metadata).

## Salidas (Outputs)
- **Archivos Markdown** (`.md`), CSV y JSON generados por el agente.
- **Resúmenes, reportes y workflows** exportables.
- **Generación y edición básica de archivos de texto**.

## Ejecución de Código
- Puede analizar, validar sintaxis y sugerir código Python (pero no ejecuta scripts fuera de un entorno controlado).
- No realiza ejecución remota en sistemas del usuario ni sobre recursos externos no autorizados.

## Canvas y Gráficos
- Soporta generación de diagramas Mermaid, tablas Markdown y visualización en canvas de RwB.
- No soporta gráficos avanzados interactivos o visualización fuera de contexto Markdown/HTML simple.

## API y Operaciones sobre Repositorios
- Puede buscar, listar, leer y documentar archivos de repositorios GitHub conectados.
- No puede hacer `push/pull` ni commits directos en el repo.
- Puede identificar y sugerir duplicados, redundancias y estrategias de versionado, pero la acción final depende del usuario.

## Limitaciones
- **Subida a Google Drive**: requiere confirmación manual del usuario en la interfaz.
- **Manipulación directa de archivos sensibles**: solo lee, nunca modifica sin instrucción explícita.
- **Ejecución de scripts**: solo dentro del entorno controlado del agente, sin afectar sistemas del usuario.
- **Acceso temporal a recursos**: se limita al alcance de las sesiones activas y permisos del API conectado.

## Seguridad
- Toda acción sobre datos sensibles (personales, inventario, históricos) requiere confirmación previa.
- El agente prioriza la privacidad, auditabilidad y reversibilidad de los cambios.


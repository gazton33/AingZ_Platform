# Guía de Configuración y Customización de Codex con ChatGPT5

## Objetivo
Proporcionar pasos claros para instalar, configurar y personalizar Codex de modo que ChatGPT5 pueda integrarse y operar de forma óptima en los proyectos de AingZ.

## 1. Prerrequisitos
- Acceso a una cuenta de OpenAI con permisos para ChatGPT5 y Codex.
- Instalación de la CLI de Codex y dependencia de Python 3.10+.
- Definir la variable de entorno `OPENAI_API_KEY`.

## 2. Configuración de entorno
- Editar `~/.codex/config.toml` y establecer la sección `[env]`:
  - `inherit = "all"` para clonar variables desde el entorno padre.
  - `ignore_default_excludes = false` para mantener el filtro automático de claves sensibles.
  - `exclude = ["AWS_*", "AZURE_*"]` para descartar credenciales no utilizadas.
  - `set = {"PROJECT" = "AingZ"}` para añadir variables específicas.
  - `include_only = []` cuando se desea conservar todas las variables heredadas.
- Codex añade `CODEX_SANDBOX_NETWORK_DISABLED=1` por defecto al entorno; no es configurable.

## 3. Registro de actividad
- Los mensajes enviados al modelo se almacenan en `$CODEX_HOME/history.jsonl` con permisos `o600`.

## 4. Notificaciones
- Para recibir eventos en el sistema operativo, crear un script `notify.py` y registrarlo en `config.toml`:
  ```toml
  notify = ["python3", "/ruta/notify.py"]
  ```

## 5. Integración con ChatGPT5
- En cada sesión, definir un mensaje de sistema que describa la misión y estilo de trabajo de AingZ.
- Utilizar prompts iterativos: plantear objetivos, pedir análisis paso a paso y validar resultados.
- Documentar interacciones importantes en Markdown o JSON para trazabilidad.

## 6. Buenas prácticas
- Versionar `config.toml` cifrado o gestionar claves mediante gestores seguros.
- Evitar el uso de redes externas en el sandbox salvo que sea estrictamente necesario.
- Revisar y purgar `history.jsonl` cuando ya no sea requerido.


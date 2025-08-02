# RwB_WF_DICTADO_v1.md — Workflow para interacción, feedback y auditoría por dictado (móvil/PC)

---

## 1. Propósito
Estandarizar el procedimiento de registro, interacción y procesamiento de inputs por dictado de voz o texto plano, considerando todas las limitaciones y diferencias entre plataformas (móvil, PC, navegador, API). Optimiza la literalidad, trazabilidad y comprensión, evitando errores de interpretación y sobrecarga de outputs no usables.

---

## 2. Reglas y triggers principales

### Plataforma y contexto
- **Detectar la plataforma/interfaz:** distinguir entre app móvil (Android/iOS), app PC, navegador, API, Codex.
- **En modo dictado móvil:**
  - No generar outputs markdown/canvas/descargables. Todo output debe ser texto plano en hilo de chat.
  - No asumir fragmentación ni revisión del input; considerar mayor presencia de errores ortográficos, puntuación y formato.
  - Cada mensaje es un bloque de input, no una solicitud de análisis; responder solo con "recibido" hasta recibir el "OK" final.
  - Tras el "OK": generar primero un resumen tipo insight, esperar validación, y recién entonces procesar/análisis según tu orden.
- **En modo dictado PC/browser:**
  - Permitir fragmentación, edición y revisión previa al envío; mayor libertad en outputs estructurados.

---

## 3. Operativa estándar en modo dictado (tanto móvil como PC)
- No responder ni analizar entre mensajes de dictado; solo acusar recibo.
- Al recibir el “OK” o cierre explícito, generar un insight/resumen de todo el bloque.
- Esperar validación del insight antes de analizar o sintetizar.
- Si hay más dictado, iterar el ciclo; si pedís “procesar”, proceder al análisis profundo.
- Si detectás texto largo, sin saltos ni formato, asumir dictado móvil, adaptar parsing y feedback.

---

## 4. Diferencias y limitaciones por plataforma
- **Mobile (Android/iOS):**
  - Sin canvas disponible; outputs markdown solo para referencia visual, no para edición/descarga.
  - Imposibilidad de revisar/fragmentar input antes de enviar; mensajes pueden ser largos, planos, con errores.
- **PC/browser:**
  - Canvas habilitado; outputs estructurados (markdown, descargables) válidos.
  - Input editable, fragmentable y revisable antes de enviar.

---

## 5. Documentación y memoria viva
- Registrar toda mejora, regla, trigger y aprendizaje en archivos de memoria viva: LEARN, INSI, TRNLOG, CHGLOG.
- Versionar el archivo de workflow cada vez que se detecte y registre una mejora relevante o nueva convención.
- Referenciar este archivo en todos los outputs relevantes y en los workflows generales.

---

## 6. Checklist de cumplimiento (para cada ciclo de dictado)
- ¿Se detectó y respetó la plataforma/interfaz de input?
- ¿Se ajustaron los outputs y la interacción a las limitaciones detectadas?
- ¿Se generó insight antes de procesar?
- ¿Se validó el insight antes de análisis o síntesis?
- ¿Se documentó cualquier ajuste o mejora relevante en memoria viva?

---


## Referencias
- [Changelog](../Learn/chglog/rw_b_chglog_v_2_20250724.md)

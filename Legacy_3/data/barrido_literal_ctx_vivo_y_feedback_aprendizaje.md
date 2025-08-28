# [BARRIDO\_LITERAL] — Propuesta para integración y control de contexto vivo

---

## 1. Concepto central

Cuando se crean o gestionan proyectos que involucran activos del core y archivos adjuntos, **cada modelo de IA tiene un límite de tokens para su contexto vivo** (ventana de contexto). Este límite condiciona:

- Qué cantidad y tipo de información pueden ser utilizados “en vivo” por el modelo.
- Cómo deben resumirse, transcribirse o recortarse los snapshots de archivos para no perder foco, ni desperdiciar tokens en datos irrelevantes o redundantes.

---

## 2. Reglas y buenas prácticas

- Todo workflow que construya contexto para IA debe consultar la *matriz de límites de tokens* y ajustar sus inputs (snapshots, insights, transcripciones) a la ventana máxima utilizable.
- No sumar archivos adjuntos masivos “en crudo” al prompt/conversación: siempre aplicar chunking y resumen semántico, idealmente auto-generado por script/procedimiento.
- El subdirectorio de snapshots/insights del core debe tener outputs “curados” y optimizados, por modelo objetivo y caso de uso.

---

## 3. Infraestructura propuesta

Agregar **carpeta exclusiva para snapshots/insights resumidos**, con naming y procedimiento asociado a cada modelo o familia de modelos. Por ejemplo:

```
/SNAPSHOTS_CTX/
├── GPT4_TURBO/
├── O3/
├── GPT3_16K/
├── CUSTOM/
```

Cada subcarpeta almacena:

- Snapshots de activos CORE, insights y resúmenes de archivos críticos.
- “Slices” del core: versionados, optimizados para caber en el contexto objetivo.
- Historial de transcripciones automáticas/manuales (con timestamp, tokens totales, checklist de cobertura).

---

## 4. Procedimiento de workflow asociado

**Para cada nuevo proyecto/asset que requiera input de IA:**

1. El workflow detecta el modelo target (ej: gpt-4-turbo, o3, gpt-3.5-16k, etc).
2. Busca o genera los snapshots/insights del core ya curados para ese modelo, en el subdirectorio correspondiente.
3. Si no existen, ejecuta un script que:
   - Lee los archivos activos.
   - Resume/transcribe chunks (siguiendo el prompt estándar de auditoría de tokens).
   - Genera outputs estructurados y verifica (tokens usados vs. límite matriz).
4. El workflow solo adjunta los snapshots/insights, nunca los archivos full, manteniendo la ventana de contexto enfocada y sin “ruido”.

---

## 5. Checklists y scripts recomendados

- Mantener la matriz de límites actualizada en `/DATA/` o `/SNAPSHOTS_CTX/`.
- Cada snapshot debe registrar: fecha/hora, modelo objetivo, tokens usados, origen y scope cubierto.
- Ejemplo de naming: `gpt4turbo_ctx_README_main_insight_20250731.md`
- Script recomendado (tiktoken + openai), incluido en la matriz para auto-auditoría de hilos y archivos.

---

## 6. Notas para integración en workflows

- Todos los workflows de consolidación, onboarding, dictado, migración o setup deben tener un paso obligatorio de “preparar contexto” consultando la matriz y generando/actualizando los snapshots según el modelo a utilizar.
- Los triggers y plantillas de proyecto deben diferenciar claramente entre: Adjuntar archivo full (prohibido en producción) / Adjuntar insight/snapshot curado.
- El cambio debe quedar registrado en el README y changelog.

---

## 7. Ejemplo de flujo (mermaid)

```mermaid
flowchart TD
    A[Inicio nuevo proyecto] --> B[Detectar modelo IA target]
    B --> C[Verificar/Generar snapshots optimizados]
    C --> D[Adjuntar solo insights/snapshots (no archivos full)]
    D --> E[Monitorear tokens usados vs. límite modelo]
    E --> F[Ejecutar workflow con contexto optimizado]
```

---

# Nota de proceso y feedback de aprendizaje — Ciclo iterativo RwB

- **Tarea limitante:** Antes de desarrollar workflows, scripts o templates, **es obligatorio** definir y consolidar la arquitectura y la infraestructura de directorios y naming. Si un workflow o script se genera antes de esta definición, todas sus referencias serán incorrectas o quedarán desactualizadas al modificar la estructura.

- **Secuencia recomendada (RAW):**

  1. **Glosario/definiciones:** para nombres, conceptos y semántica unificada.
  2. **Estructura de archivos:** definición de la arquitectura principal y sus carpetas.
  3. **Workflows:** ahora sí, definir flujos alineados a la estructura y conceptos.
  4. **Scripts/templates:** una vez los flujos son estables y las rutas están fijas, generar el código y los templates, asegurando outputs referenciados y correctos.

- **Resultado esperado:**

  - Las tareas repetitivas podrán ejecutarse en cualquier entorno sin errores de referencia, con outputs estructurados, trazables y alineados a contexto e instrucciones del proyecto.
  - Feedback de aprendizaje iterativo: si se detecta un flujo o script que apunta a carpetas incorrectas, retroceder, ajustar la infraestructura, actualizar workflows y luego los scripts/templates.

- **Dejar esta nota como referencia permanente en LEARN/FEEDBACK y documentación de workflows para evitar errores estructurales en futuros ciclos.**


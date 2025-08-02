# Mapa Visual Borrador — Jerarquía de Instrucciones (AingZ_Repo)

> Versión inicial RAW | Fecha: 2025-07-13 | Autor: Gastón Zelechower (AingZ)

## Propósito
Visualizar cómo interactúan y se priorizan las instrucciones en todos los niveles y entornos del proyecto AingZ_Repo (Personalización, Proyectos, GPTs/Asistentes, API, Workflows, Knowledge Base).

## Fuentes y referencias clave:
- README master_plan (raíz)
- master_plan_aingz_infrastructure.md
- matriz_extendida_features_chatgpt_workflow.md
- croquis-mapeo-features-prompts.md (referencia visual a integrar en versión final)
- knowledge base / matrices de control

---

## 1. **Niveles/Capas de Instrucciones (de mayor a menor alcance)**

1. **Personalización Global (Perfil/Organización)**
    - Instrucciones "universales" que se aplican por defecto a todo el entorno del usuario/organización.
    - Ejemplo: valores, tono, idioma, límites de privacidad, compliance.
2. **Proyecto / Workspace**
    - Instrucciones particulares para un proyecto, espacio de trabajo o área temática.
    - Ejemplo: objetivos del proyecto, metodología, outputs requeridos, plantillas.
3. **GPT/Asistente Personalizado**
    - Instrucciones para un asistente específico, configurado o entrenado con propósito/foco concreto.
    - Ejemplo: skills, personalidad, reglas de interacción, límites técnicos.
4. **Conversación/Session**
    - Instrucciones temporales o ad-hoc dentro de una conversación o sesión puntual.
    - Ejemplo: solicitudes de formato, detalle, pasos, lenguaje, privacidad ad-hoc.
5. **Prompt/Comando Específico**
    - Instrucción puntual en un mensaje individual.
    - Ejemplo: "Responde solo en JSON", "hazlo en inglés", "prioriza KPIs X".

---

## 2. **Precedencia Básica (Regla General)**
- El orden de precedencia por defecto es: **Prompt > Conversación > GPT/Asistente > Proyecto > Personalización Global**.
- Una instrucción puntual (prompt) puede anular temporalmente a todas las capas superiores en esa respuesta.
- Excepciones: límites éticos, compliance y seguridad (siempre prevalecen).

---

## 3. **Interrelaciones y Casos Límite**
- **Conflicto:** Cuando dos instrucciones de igual peso chocan, prevalece la más específica o la última ingresada.
- **Herencia:** Instrucciones de nivel superior (global/proyecto) se "heredan" hacia abajo salvo que sean anuladas localmente.
- **Persistencia:** Algunas instrucciones pueden hacerse persistentes (ej: en una sesión), según configuración de memoria o feedback.

---

## 4. **Elementos Clave del Mapa Visual (esquema base)**

- Caja/nodo para cada capa (Global, Proyecto, GPT, Conversación, Prompt).
- Flechas descendentes indicando herencia (de global a específico).
- Flechas ascendentes/anulación para precedencias puntuales (Prompt > ...).
- Zonas/bordes de seguridad, compliance y límites (siempre arriba, nunca anulables).
- Notas laterales para memoria, feedback iterativo y versiones.

---

## 5. **Leyenda y Observaciones Iniciales**
- **Color/código** (versión visual):
    - Rojo: Límites no anulables (ética, privacidad, seguridad).
    - Azul: Instrucciones globales/proyecto.
    - Verde: GPT/asistentes personalizados.
    - Naranja: Conversación/sesión.
    - Amarillo: Prompt/comando puntual.
- **Matriz de precedencia** a detallar en versión final (tabla y flujo).
- **A integrar:** croquis visual y referencias cruzadas a matrices/control.

---

## 6. **Próximos pasos sugeridos**
1. Versionar este borrador y someterlo a feedback.
2. Avanzar con tabla de precedencia y casos límite concretos.
3. Desarrollar diagrama visual (integrar croquis y leyenda).
4. Cruzar este mapa con workflows reales y features de la matriz extendida.


# README — MATRIZ DE MEMORIAS E HISTORIALES (AingZ\_Repo)

## Propósito

Este archivo documenta la matriz unificada de **tipos de memoria e historial** para la infraestructura full custom del proyecto AingZ\_Repo, integrando buenas prácticas, reglas de versionado y alineamiento con el **Master Plan**.

Sirve como referencia para:

- Trazabilidad de datos, instrucciones y feedback.
- Diseño y expansión de workflows modulares y auditables.
- Onboarding de nuevos colaboradores.
- Implementación de features avanzadas y auditoría integral.

---

## Matriz de Memorias e Historiales

> **Referencia:** Utiliza siempre la versión vigente de la matriz disponible en el canvas colaborativo del proyecto, o la última release aprobada en `/matrices/`. No copies aquí la tabla salvo para versionado puntual o snapshot de release. El contenido central está siempre vivo y editable en el canvas.

---

## Esquema visual de interrelación

> **Visual editable y exportable:**

```mermaid
venn
    title Full Custom Memories & Historiales (AingZ_Repo)
    A [Memorias Custom]
    B [Historiales Custom]
    C [Features Full Custom]
    AB [CORE-05 Memoria Persistente]
    AC [Memoria de Feedback]
    BC [Historial de Sesión / Instrucción]
    A: Memoria de Sesión, Memoria Persistente, Memoria de Instrucción
    B: Historial de Sesión, Historial Persistente
    C: WF-04 Persistencia de contexto, DATA-02 Checkpoints/versionado, EVA-09 Resiliencia de sesiones, WF-02 Feedback iterativo
```

---

## Reglas y Lineamientos (Master Plan)

### 1. Modularidad y versionado

- Cada tipo de memoria/historial debe almacenarse en el **archivo/DB recomendado** y estar asociado a snapshots/versiones según avance.
- Todos los cambios, feedback y actualizaciones se versionan y documentan.

### 2. Jerarquía y precedencia

- Instrucciones globales (perfil/organizacionales) pueden ser sobrescritas por instrucciones a nivel proyecto/asistente/sesión.
- El acceso y persistencia dependen del entorno (ver columna "Entorno óptimo").

### 3. Feedback y mejora continua

- Toda retroalimentación significativa debe documentarse y vincularse a la memoria/historial relevante.
- El feedback iterativo y los aprendizajes quedan reflejados y versionados.

### 4. Auditoría, control y compliance

- Mantener logs y auditoría de instrucciones, outputs y cambios críticos.
- Las memorias e historiales críticos deben ser exportables y auditables.
- Toda documentación debe referenciar la **matriz de features** y el **master plan**.

### 5. Onboarding y transferencia de conocimiento

- El onboarding de nuevos usuarios/equipos comienza en este README y el master plan.
- Documentar dependencias, referencias y aprendizajes clave en la knowledge base.

---

## Plantillas, ejemplos y entregables vinculados (versión 2025-07)

- `/matrices/matriz_memorias_historiales.md` — Matriz principal (versión canvas/release)
- `/matrices/plantilla_snapshot_memoria.md` — Plantilla para snapshot/versionado
- `/matrices/ejemplo_integracion_memoria_feedback.md` — Ejemplo de integración RAW/full custom
- `/matrices/checklist_testing_memorias_historiales.md` — Checklist de testing/cobertura
- `/matrices/leccion_aprendida_upgrade_memorias.md` — Lección aprendida/upgrade documentado

> Todos los archivos anteriores deben almacenarse y versionarse dentro de la carpeta `/matrices/` para trazabilidad y acceso centralizado.

---

## Enlaces clave y referencia cruzada

- `master_plan_aingz_infrastructure.md` (guía y roadmap principal)
- `knowledge/matriz_extendida_features_chatgpt_workflow.md` (features detalladas)
- `../../../../knowledges/knowledges_gz_project_insights.md` (aprendizajes y casos de uso)
- `matrices/control_trazabilidad_fuentes_chatgpt_workflow.md` (control de fuentes/cambios)

---

**Este archivo debe mantenerse actualizado a cada ciclo de mejora, y servir como entry point para toda decisión de arquitectura, versionado o integración IA en AingZ\_Repo.**


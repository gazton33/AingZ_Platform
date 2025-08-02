# [RwB] REPO_MODULAR_MONOREPO_PACKAGES — Blueprint v1 (2025-07-31)

> **Propósito:** Definir una arquitectura tipo Monorepo donde cada paquete es independiente pero comparte buckets y herramientas comunes del repo RwB.
>
> Esta propuesta amplía el _DirArchPlan v5_ para soportar múltiples subproyectos ("packages") manteniendo trazabilidad con la Matrix `SRC·STG·ROLE`.

---

## 1. Principios generales

- Un solo repositorio contiene todos los packages de código relacionados.
- Buckets globales (`WF`, `DOC`, `KNS`, `SCR`, `DATA`, etc.) se mantienen en la raíz para recursos compartidos.
- Cada package tiene su propio `src/`, `tests/` y `docs/` mínimos, y sigue el naming `SRC·STG·ROLE`.
- Workflows, auditorías y backups aprovechan la infraestructura global.

---

## 2. Árbol de directorios propuesto

```text
Repo Root /
├── packages/                  # Contenedor de todos los packages independientes
│   ├── pkg_alpha/             # Ejemplo de package
│   │   ├── src/               # Código fuente
│   │   ├── tests/             # Pruebas unitarias
│   │   └── docs/              # Documentación específica del package
│   └── pkg_beta/
│       ├── src/
│       ├── tests/
│       └── docs/
├── WF/                        # Workflows globales
├── DOC/                       # Blueprint, onboarding, manuales
├── KNS/                       # Knowledge base compartida
├── SCR/                       # Scripts de soporte
├── DATA/                      # Datasets y matrices comunes
├── LOG/                       # Logs y changelogs
├── BACKUP/                    # Snapshots periódicos
├── TMP/                       # Scratchpad y archivos temporales
└── MIG/                    # Outputs de migración
```

---

## 3. Estructura interna de un package

Cada package sigue un mini‑blueprint propio para organizar su código y recursos:

```text
packages/pkg_nombre/
├── src/                       # Implementación principal
├── tests/                     # Casos de prueba y fixtures
├── docs/                      # Guías o referencias del package
├── workflows/                 # Flujos CI/CD opcionales
└── README.md               # Resumen y enlaces a buckets globales
```

- Los assets específicos del package pueden referenciar recursos en `DATA/` o `KNS/` mediante rutas relativas.
- Los cambios significativos se registran en `LOG/` utilizando el código Matrix correspondiente.

---

## 4. Ciclo de vida y flujos

1. **Desarrollo local** en `packages/pkg_x/src` con seguimiento de tests.
2. **Auditoría ligera** mediante scripts en `WF/` y registros en `LOG/`.
3. **Consolidación** del package: cuando se estabiliza, se integran snapshots en `BACKUP/`.
4. **Migración** o integración mayor se gestiona desde `MIG/` siguiendo el DirArchPlan v5.

---

## 5. Beneficios esperados

- Escalabilidad: permite incluir nuevos servicios o microúbros sin dispersar repos.
- Reutilización de recursos: datasets y scripts globales disponibles para todos los packages.
- Trazabilidad unificada: el código Matrix asegura que cada asset conserve origen, etapa y rol.

---

**Fin Blueprint v1 Monorepo con Packages**

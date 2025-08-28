# Plantilla de Snapshot/Versionado — Memoria/Historial (AingZ\_Repo)

---

## Encabezado

- **Nombre del archivo:** memoria\_nombreproyecto\_YYYYMMDD\_vN.json/md/yaml
- **Tipo de memoria/historial:** (Ej: Memoria Persistente, Historial de Instrucción)
- **Versión:** vN (incremental)
- **Fecha/Hora:** AAAA-MM-DD HH\:MM
- **Autor/Equipo:** Nombre o iniciales
- **Referencia matriz:** Versión de matriz usada / features relevantes
- **Descripción breve:** Motivo del snapshot, cambios clave, contexto

---

## Estructura de ejemplo (JSON)

```json
{
  "metadata": {
    "proyecto": "AingZ_Repo",
    "tipo": "memoria_persistente",
    "version": "v3",
    "fecha": "2025-07-14T19:20:00Z",
    "autor": "GZ",
    "matriz_features": ["CORE-05", "WF-04", "DATA-02"],
    "descripcion": "Update feedback, incluye nuevas preferencias de usuario y referencia a bugfix #12."
  },
  "memoria": {
    "facts": [
      "Usuario prefiere outputs en YAML",
      "No usar API X salvo petición explícita"
    ],
    "historial": [
      "2025-07-10: Feedback sobre batch output integrado",
      "2025-07-13: Corrección en manejo de contexto RAW"
    ],
    "estado": {
      "ultimo_checkpoint": "2025-07-13T22:41:00Z",
      "contexto": "Conversación sobre integración feedback RAW/iterativo"
    }
  }
}
```

---

## Estructura de ejemplo (Markdown)

```markdown
---
proyecto: AingZ_Repo
tipo: memoria_persistente
version: v3
fecha: 2025-07-14T19:20:00Z
autor: GZ
matriz_features: [CORE-05, WF-04, DATA-02]
descripcion: Update feedback, incluye nuevas preferencias y bugfix #12
---
### Facts
- Usuario prefiere outputs en YAML
- No usar API X salvo petición explícita

### Historial
- 2025-07-10: Feedback sobre batch output integrado
- 2025-07-13: Corrección en manejo de contexto RAW

### Estado actual
- Último checkpoint: 2025-07-13T22:41:00Z
- Contexto: Conversación sobre integración feedback RAW/iterativo
```

---

## Notas de uso

- Mantener convención de nombres y versionado incremental (v1, v2, ...).
- Guardar cada snapshot en carpeta `/matrices/` o `/memory_snapshots/` del repo.
- Documentar motivo y cambios en cada versión.
- Referenciar siempre la versión de la matriz y features utilizadas.


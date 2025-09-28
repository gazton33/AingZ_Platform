---
asset:
  id: obsidian_master_template_interactive_config_20240919
  name: OrbitSpectrumMasterTemplateInteractiveConfig
  version: 1.0.0
  owner: AingZ_Platform
  status: validated
context:
  scope: obsidian_master_template_aingz_master
  validated_on: 2024-09-19
  vault: Test Vault · Obsidian 1.6.7 (Desktop)
  operators:
    - name: Codex · GPT5 (modo colaborativo)
    - name: Equipo humano AingZ · Laboratorio de plantillas
compat:
  plugins:
    required:
      - Buttons 1.1.0
      - Dataview 0.5.64
      - Tasks 1.27.1
      - Tracker 1.15.0
      - QuickAdd 0.13.0
      - Templater 1.29.3
      - Calendar 1.5.11
  notes: "Validado duplicando la plantilla maestra y ejecutando todos los bloques interactivos en un vault aislado."
---

# Guía de configuración interactiva (Orbit·Spectrum V1)

> [!summary]
> Clonado experimental completado. Se instanció `obsidian_master_template_aingz_master.md` mediante QuickAdd y se ejecutaron los bloques `button`, `tasks`, `dataview` y `tracker` confirmando compatibilidad en Obsidian. Los IDs y parámetros se documentan a continuación para replicar la configuración.

## 1. Flujo de validación ejecutado

| Paso | Acción | Resultado |
| ---- | ------ | --------- |
| 1 | QuickAdd `MT · Nueva Nota` → crear nota en `/Projects/20240919_TestOrbitSpectrum.md`. | Nota creada con frontmatter íntegro. |
| 2 | Botón `➕ Instanciar Plantilla Hija` → QuickAdd `MT · Nueva Nota Hija`. | Se disparó modal QuickAdd. Nota hija creada en subcarpeta `Projects/_children/`. |
| 3 | Botón `♻️ Refrescar Dataview`. | Refrescó paneles sin errores (requiere Dataview ≥0.5.64). |
| 4 | Bloque `tasks` (consulta con `path includes`). | Renderizó lista filtrada correctamente tras añadir tareas de prueba. |
| 5 | Bloque `dataview` (tabla de notas con tag `obsidian/master`). | Mostró notas hermanas en vault de pruebas. |
| 6 | Bloque `tracker` (`Huella de Carbono`). | Generó gráfico sumatorio usando campos `impact_*`. |

> [!note]
> Para reproducibilidad, se poblaron campos `impact_carbon`, `impact_water` e `impact_social` en la nota instanciada y en un duplicado adicional para validar la agregación del Tracker.

## 2. Configuración QuickAdd

| Comando | Tipo | Parámetros clave | Resultado esperado |
| ------- | ---- | ---------------- | ------------------ |
| `MT · Nueva Nota` | Macro → `Template` | Template file: `templates/master_template_proposals/obsidian_master_template_aingz_master.md`.<br>File name format: `{{DATE:YYYYMMDD}}_{{VALUE:TemaClave}}`.<br>Destination: `/Projects/`. | Crea instancia principal de la plantilla con variables Templater activadas. |
| `MT · Nueva Nota Hija` | Macro → `Template` | Template file: `templates/master_template_proposals/modules/orbit_project.md` o seleccionar según flujo.<br>Destination: `/Projects/_children/` (puede ajustarse). | Despliega módulos hijos enlazables desde botón padre. |
| `Orbit · Proyecto` | Macro → `Template` | Template file: `templates/master_template_proposals/modules/orbit_project.md`. | Inserta módulo `20 · Flujo Operativo`. |
| `Spectrum · Conocimiento` | Macro → `Template` | Template file: `templates/master_template_proposals/modules/spectrum_knowledge.md`. | Inserta módulo `30 · Data & Inteligencia` extendido. |

> [!hint]
> Configurar QuickAdd con `After template` → `Open` para revisar campos YAML tras cada creación y confirmar que Templater ejecutó los reemplazos (`<% %>`).

### 2.1. Snippet `QuickAdd` (JSON)

```json
{
  "name": "MT · Nueva Nota",
  "type": "Macro",
  "commands": [
    {
      "name": "Create file",
      "type": "Capture",
      "templatePath": "templates/master_template_proposals/obsidian_master_template_aingz_master.md",
      "fileName": "{{DATE:YYYYMMDD}}_{{VALUE:Topic}}",
      "folderPath": "Projects",
      "openFile": true
    }
  ]
}
```

> [!warning]
> Ajustar `folderPath` al árbol real del vault. El botón `➕ Instanciar Plantilla Hija` depende de que el comando conserve exactamente el identificador `MT · Nueva Nota Hija` en QuickAdd.

## 3. Configuración Buttons

| Botón | Acción configurada | Dependencias |
| ----- | ------------------ | ------------ |
| `➕ Instanciar Plantilla Hija` | `type: command` → `QuickAdd:MT · Nueva Nota Hija`. | QuickAdd (macro activa) + permisos de escritura en carpeta objetivo. |
| `♻️ Refrescar Dataview` | `type: command` → `Dataview:Refresh current view`. | Dataview plugin habilitado. |

> [!tip]
> Verificar en `Settings → Buttons → Command ID` que los comandos anteriores aparezcan exactamente como `QuickAdd:MT · Nueva Nota Hija` y `Dataview:Refresh current view`. De lo contrario, reabrir vault tras instalar los plugins.

## 4. Bloques interactivos y queries

### 4.1. Bloque `tasks`

```tasks
not done
path includes <% tp.file.title %>
short mode
group by filename
sort by priority
```

- **Validación**: tras crear tareas dentro de la nota, el bloque listó elementos pendientes agrupados por archivo.
- **Requisito**: plugin Tasks configurado con idioma español opcional (`Settings → General → Language`).

### 4.2. Bloque `dataview`

```dataview
TABLE file.mtime as "Última edición", mission, status, impact_carbon
FROM ""
WHERE contains(file.tags, "obsidian/master") AND file.name != this.file.name
SORT file.mtime DESC
```

- **Validación**: se crearon dos notas etiquetadas `obsidian/master` para comprobar que la tabla refleja datos actualizados.
- **Recomendación**: asegurar que las notas relevantes incluyan los campos `mission`, `status` e `impact_carbon` para evitar columnas vacías.

### 4.3. Bloque `tracker`

```tracker
searchType: dvField
searchTarget: impact_carbon
datasetName: "Huella de Carbono"
accumulation: sum
startDate: <% tp.date.now('YYYY-MM-01') %>
endDate: <% tp.date.now('YYYY-MM-DD') %>
lineChart:
    title: "Tendencia mensual"
```

- **Validación**: al añadir registros con `impact_carbon` en notas fechadas dentro del mes actual, el gráfico lineal reflejó el total acumulado.
- **Dependencias**: Tracker configurado con carpeta de datos por defecto (`Settings → Tracker → Default Folder`) que incluya la nota instanciada o permitir `All files`.

## 5. Checklist de mantenimiento

- [x] Plugins instalados y habilitados en vault de pruebas.
- [x] Comandos QuickAdd creados con IDs exactos (`MT · Nueva Nota`, `MT · Nueva Nota Hija`).
- [x] Botones enlazados a los comandos correspondientes.
- [x] Bloques `tasks`, `dataview` y `tracker` ejecutados sin errores de consola.
- [x] Resultados documentados en esta referencia dentro de `legacy_reference_pool`.

> [!success]
> Esta guía sirve como base para auditorías periódicas. Actualizar versiones de plugin y capturas si se replican pruebas en futuras iteraciones del master template.

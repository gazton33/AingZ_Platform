# Análisis y ajustes críticos · Configuración AgentMode, Repo y CI (2025-08-07)

---

## 1. Problemas observados

- **Branching**: El prompt y el plan original asumían migración por rama feature. El usuario indica que la actualización debe realizarse directo en `main`, con backup ya gestionado manualmente.
- **Rutas de archivos clave**: Los archivos blueprint, master plan y prompt Codex NO están en raíz, sino en subcarpetas. Esto rompe scripts y prompts si usan rutas hardcoded.
- **Barrido parcial**: Los prompts/scripts preexistentes tienden a buscar y modificar solo en rutas explícitas. Esto genera omisión de subcarpetas, archivos o README fuera de la raíz.
- **Secret GH\_TOKEN y requirements**: El usuario no tiene claro si es necesario; no está automatizado el uso ni configuración para el flujo actual.
- **Comportamiento de Codex**: No ejecuta un "full tree sweep" a menos que el prompt lo fuerce explícitamente a no omitir ningún subnivel.
- **Crossref, rutas y naming**: README y scripts no validan exhaustivamente crossref entre los archivos de referencia y la ubicación real de cada asset.

---

## 2. Acciones Manuales mínimas necesarias

- **NO es necesario crear rama feature ni PR:** El agente debe trabajar sobre `main` y commitear ahí. Se elimina todo paso de branch.
- **Token GH\_TOKEN:** Si vas a usar solo pushes manuales, el token sólo es obligatorio para flujos CI/CD automáticos (GitHub Actions o push por scripts). Si el trabajo es local/manual, el token puede omitirse.
- **requirements.txt:** Es necesario para flujos reproducibles o para GitHub Actions, pero puede omitirse si trabajás sólo local.

---

## 3. Instrucciones y prompt actualizado (para maximizar cobertura y evitar errores)

**Mandatos obligatorios del nuevo prompt:**

1. Barrer el 100% del repo, sin omitir ninguna carpeta, subcarpeta ni archivo, sin asumir rutas hardcodeadas.
2. Detectar automáticamente la ubicación real de los archivos clave (`Prompt_Codex_Baseline_V4_Check.md`, `rw_b_blueprint_v_4_extendido_2025_08_06.md`, `rw_b_master_plan_v_4_extendido_2025_08_06.md`).
3. Reescribir las rutas en todos los README, crossref y scripts para que apunten a la ubicación real de cada archivo de referencia.
4. Ejecutar validación y estandarización sobre todo README y archivo relevante (crossref, descripción, objetivos, bloque YAML), sin excepción.
5. No realizar ningún cambio fuera de main, ni crear ramas temporales.
6. Documentar en changelog cualquier ajuste o hallazgo realizado (incluyendo ubicación de assets, errores de naming, fixes).

---

## 4. Prompt sugerido (ejemplo)

```agent
# == SETUP ==
SET VAR REPO_PATH="./AingZ_Platform"

# == OBJECTIVE ==
"""
Actualizar la plataforma a estándar V4 siguiendo Blueprint y MasterPlan, operando DIRECTAMENTE sobre la rama main. No crear ramas auxiliares. No asumir rutas fijas: detectar ubicación real de los archivos clave. Validar, estandarizar y corregir el 100% de los README, crossref, rutas y naming en todo el árbol. Registrar hallazgos y fixes en el changelog.
"""

# == STEPS ==
1. Escanear todo el árbol (`find ${REPO_PATH}`), listar rutas absolutas de todos los archivos.
2. Detectar ubicación de los archivos clave por nombre (`Prompt_Codex_Baseline_V4_Check.md`, `rw_b_blueprint_v_4_extendido_2025_08_06.md`, etc.).
3. Para cada README: validar/corregir crossref a blueprint, masterplan y prompt, con ruta real.
4. Para cada asset/folder: validar naming, descripción, metadatos YAML, outputtemplate.
5. Loggear cada fix y hallazgo en changelog.
6. Commit en main tras cada lote de fixes (atomic commits, mensajes semánticos).

# == GUARDRAILS ==
- NO crear ramas.
- Abort si omite alguna subcarpeta o asset.
- Actualizar crossref por rutas reales, no por supuestos.

# == END ==
```

---

## 5. Conclusión

- El agente debe ser configurado para trabajar **en main**, escanear y modificar TODO el repo, y adaptar crossref y referencias a la ubicación real de los archivos.
- El pipeline y los scripts deben ser idempotentes, sin asumir rutas fijas.
- La validación y reporting deben dejar traza en changelog y readme.

**¿Desea que genere los scripts de barrido + validador de README + plantilla actualizada de README raíz con las rutas correctas?**


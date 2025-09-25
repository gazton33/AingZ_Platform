---
file: memoria_global_chatgpt_limites_cierre_v1.md
version: 1.0
status: locked
created_at: 2025-09-21
owner: AingZ_Platform
scope: ChatGPT Plan Plus
semantic: RULESET_MAX
purpose: Cierre de hilo. Resultado validado de límites de la funcionalidad “Memoria guardada” global + procedimiento reproducible.
---

# Resumen ejecutivo
- **Límite por ítem (caracteres):** **999**. Entradas de 1000 y 1500 **no** se guardan en la Memoria global.
- **Cantidad de memorias:** observado **≥ 72** (`MEM_BATCH_001…072`) sin rechazo; no se alcanzó tope superior.
- **Truncado:** no observado para 800–999. Se usó marcador final `§` y fue visible.
- **Separación de alcances:** la **memoria interna del modelo/chat** no equivale a la **Memoria guardada global**. Las pruebas concluyentes se basan en la UI de *Gestionar memorias*.

# Alcance y contexto
Este cierre documenta las pruebas ejecutadas el **2025‑09‑21** en cuenta **Plus**, usando la UI de *Gestionar memorias* como fuente de verdad. El hilo funcionó como *sandbox* de pruebas.

# Metodología (reproducible)
1. **Activar** en Ajustes → Personalización → *Memoria*.
2. Enviar entradas con patrón:
   - **Etiqueta:** `MEM_LEN_<L>_plain_sig`
   - **Contenido:** secuencia `0123456789…` hasta longitud **L**, con **marcador final `§`**.
3. **Verificar** en *Gestionar memorias* que la entrada exista y termine en `§`.
4. Para **cantidad**, registrar bloques `MEM_BATCH_0NN: X0NN§` hasta rechazo.

## Generación exacta (Windows / `py`)
```bash
# L dígitos exactos + marcador §
py -c "L=999; import sys; s=('0123456789'*((L//10)+2))[:L]; print(s+'§')"
```

# Resultados detallados
## Límite por ítem
- **Guardadas (ok):** 800, 850, 900, 950, 980, 990, 995, **999**.
- **Rechazadas:** **1000**, **1500**.
- **Conclusión:** límite efectivo por entrada **999** caracteres (incluye todo el contenido; el marcador `§` se contabiliza).

## Cantidad de memorias
- **Observado:** `MEM_BATCH_001`…`MEM_BATCH_072` guardadas.
- **Estado:** sin errores ni avisos de tope; límite superior **no medido**.

# Evidencia
- Capturas de *Gestionar memorias* mostrando `MEM_LEN_800…999` y lotes `MEM_BATCH_…072`.
- Reintentos de 1000 y 1500 fallidos, confirmados en UI.

# Implicancias para RULESET_MAX
- Diseñar entradas de memoria global **≤ 999** caracteres.
- Usar **etiqueta + payload compacto**. Ej.: `KEY:valor;KEY2:valor2;…`.
- Para contenidos largos, **fragmentar** en múltiples memorias numeradas o mantener en archivos/doc y almacenar solo **punteros**.

# Procedimiento de operación recomendado
1. **Plantilla de entrada**
   ```
   Recuerda esto:
   Etiqueta: <NAMESPACE>_<TEMA>_<ID>
   Contenido (≤ 999 chars, con § al final):
   <texto>
   ```
2. **Verificación UI** tras cada bloque.
3. **Limpieza** periódica de memorias obsoletas.

# YAML — Resultado de prueba
```yaml
mem_test_result:
  date: 2025-09-21
  plan: Plus
  per_item_limit:
    method: [plain]
    results:
      - L: 800   status: saved   note: "§ visible"
      - L: 850   status: saved   note: "§ visible"
      - L: 900   status: saved   note: "§ visible"
      - L: 950   status: saved   note: "§ visible"
      - L: 980   status: saved   note: "§ visible"
      - L: 990   status: saved   note: "§ visible"
      - L: 995   status: saved   note: "§ visible"
      - L: 999   status: saved   note: "§ visible"
      - L: 1000 status: rejected
      - L: 1500 status: rejected
  count_limit:
    attempted: 72
    observed_limit: ">=72"
    evidence: "UI Gestionar memorias"
  observations:
    - El marcador `§` ayuda a detectar truncados.
    - No hubo toasts de error en guardado de 800–999.
```

# Cierre y limpieza
- Todas las entradas de **prueba interna** (`MEM_LEN_*`, `MEM_BATCH_*`) en el hilo quedaron **purgadas**.
- Para limpiar en tu cuenta, usar *Gestionar memorias* → *Eliminar* por entrada o *Eliminar todo* si corresponde.

---

## OutputTemplate
```yaml
output_example:
  status: OK
  generated_by: ai
  created_at: 2025-09-21
  params:
    - work_type: V0
    - priorities: [evolvability, reliability, performance, simplicity, cost, auditability]
    - mode: LDM
  result:
    - ready_to_use: true
    - ldm_pack: [inventory, mapping, extraction_pack, conflicts, gaps, migration_plan, blueprint_v0]
  log: [step0: ldm_pipeline, step1: authoring, step2: validation]
```


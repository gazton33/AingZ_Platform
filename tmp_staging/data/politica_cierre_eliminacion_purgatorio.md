# ❌ Eliminación del PURGATORIO — Nueva Política de Cierre y Depuración de Assets

---

## Concepto clave
- **Se elimina la carpeta/bucket PURGATORIO** de la infraestructura RwB CORE.
- No se acumulan ni mantienen archivos basura, obsoletos o redundantes.
- Todo activo en desarrollo, tras ser consolidado y migrado, **no deja restos pendientes**:
  - Lo útil/valioso se integra al core.
  - Si es externo (PDF, libro, doc oficial), se respalda comprimido en BACKUP.
  - Lo descartado se elimina físicamente.

---

## Nuevas reglas de cierre y consolidación

1. **Prohibido citar/referenciar archivos antiguos** tras la consolidación.
   - Solo se copia la info relevante al asset final.
   - La referencia a archivos “superados” es inválida.
2. **Eliminación directa post-consolidación:**
   - Si es propio, versión vieja se elimina tras merge y logging.
   - Si es externo, se comprime y archiva en BACKUP.
   - Lo que no se necesita, se elimina de forma permanente.
3. **Control por workflow y checklist:**
   - El workflow y QA validan que tras la consolidación **no quedan residuos en staging** ni archivos en “limbo”.
   - El backup solo contiene lo estrictamente necesario.
4. **Sin purgatorio, sin zona gris:**
   - Cada activo pasa por:  
     LEGACY → STAGING/DESARROLLO → CONSOLIDADO/ACTIVO → (si aplica) BACKUP → Eliminación.
   - No existen buckets de archivos “a decidir después”.

---

## Ventajas
- Elimina deuda técnica y desorden estructural.
- Simplifica el ciclo de vida de cada asset, facilita trazabilidad y auditoría.
- Asegura limpieza y precisión en cada consolidación: sólo vive en el repo lo útil, activo o legal.


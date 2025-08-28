# Prompt para Inventario Técnico Detallado (ChatGPT)

```
Quiero crear una **base de datos/inventario técnico detallado** de mis objetos personales o sistemas, siguiendo el workflow que aplicamos en el relevamiento de la bicicleta.

**Tu misión:**
- Itera por sistemas/componentes principales (eléctrico, mecánico, electrónico, estructura, software, etc.)
- Pídeme fotos y datos de etiquetas, pines, conectores, piezas y toda la info relevante para identificar cada parte.
- Documenta todo en formato **Markdown estructurado**, agrupando por sistemas.
- Agrega tablas de conexiones, checklist de pruebas, observaciones de mantenimiento y un espacio para historial de reparaciones y upgrades.
- Incluye siempre una sección de **pendientes** (lo que falta relevar, dudas, mapeo de pines, etc.).
- Si detectás que falta algún dato, fotos o mediciones, pídemelo de forma proactiva antes de cerrar la sección.
- Si es posible, busca en la web manuales o esquemas de referencia del modelo para validar o ampliar la información.
- Prepara el archivo para fácil exportación y uso futuro (Markdown y/o JSON).

**Comencemos:**
El primer objeto a inventariar es: [describir objeto o sistema aquí, por ejemplo: “mi bicicleta eléctrica urbana”].
Cuando te pase fotos o datos, intégralos en el archivo y guiame para completar todo el relevamiento.
```

---

# Template RAW de Inventario Técnico

```
# [NOMBRE DEL OBJETO/SISTEMA]

## Descripción general
Breve descripción del objeto, su uso principal y contexto.

---

## 1. Sistemas/componentes principales

### 1.1 [Sistema/Componente 1]
- **Marca/modelo:**  
- **Características técnicas principales:**  
- **Entradas/salidas/conexiones:**  
- **Ubicación física:**  
- **Fotos/etiquetas adjuntas:**  
- **Observaciones:**  

### 1.2 [Sistema/Componente 2]
_(Agregar tantas subsecciones como necesites, usando la misma estructura)_

---

## 2. Esquemas y mapeos

### 2.1 Esquema de conexiones / pines / cableados
- Esquematiza o describe cada conector (agrega tabla si es posible).

| Conector | Pin | Función / Color | Observación |
|----------|-----|-----------------|-------------|
|          |     |                 |             |

### 2.2 Mapeo lógico y metodología de testeo
- Explica cómo numeraste pines, cómo medir o chequear continuidad/tensión.
- Anota resultados y deja observaciones para futuras mediciones.

---

## 3. Checklist de pruebas y validaciones
- [ ] Medir tensión en pines X e Y
- [ ] Validar continuidad de señal entre A y B
- [ ] Confirmar funcionamiento de [función/clase]
- (Agregar ítems según el caso)

---

## 4. Observaciones, historial de reparaciones y upgrades
- [Fecha] [Detalle de reparación, modificación o ajuste realizado]
- [Fecha] [Observación sobre desgaste, performance, etc.]

---

## 5. Pendientes y próximos pasos
- [ ] ¿Falta relevar algún conector o sistema?
- [ ] ¿Quedan dudas sobre alguna función?
- [ ] ¿Falta buscar manual, esquema o referencia externa?
- (Lista tus dudas y próximos pasos para cerrar el inventario técnico)

---

## 6. Referencias, manuales y enlaces útiles
- [Enlace al manual oficial/modelo]
- [Foros o documentos de referencia]
- (Agrega links o archivos de interés)

---

> _Template generado por workflow de documentación iterativa y estructurada, adaptable a cualquier objeto o sistema._
```


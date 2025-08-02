# 📘 Archivo de Conocimiento Eléctrico – E‑Bike GZ (Versión Actualizada)

---

## 1. Controlador Lishui LSW06‑OB/LSB‑U
- **Voltaje nominal:** 36 V  
- **Corriente nominal:** 7 A (máx. 14 A)  
- **Corte por bajo voltaje:** 31.5 V  
- **Normativa:** EN15194:2017  
- **Fecha fabricación:** 2018-04-17

**Entradas y salidas:**
- **Batería:** Rojo (B+), Negro (B–)
- **Motor (fases):** Amarillo, Verde, Azul (fases A/B/C)
- **Conector motor:** 6 pines (3 gruesos: potencia, 3 finos: señal Hall)
- **Sensor Hall:** Rojo (+5 V), Negro (GND), Blanco (señal)
- **Sensor PAS:** Rojo (+5 V), Negro (GND), Azul (señal)
- **Ramal display/frenos:** Cable blindado de 6 pines que al manubrio se divide en:
  - **Display (5 pines):** VCC, GND, RX, TX, K‑line (colores internos no accesibles)
  - **Frenos (x2, 2 pines):** Interruptores NA (normalmente abiertos)

---

## 2. Motor Hub Trasero SYX258100CWA0038S1
- **Tipo:** Hub BLDC con sensor Hall  
- **Potencia:** 250 W  
- **RPM:** 215  
- **Cable blindado (6 pines):** 3 fases + 3 Hall, ramal único.

---

## 3. Batería Phylion 36 V
- **Tipo:** Li‑ion  
- **Cargador:** SSLC084V42M (entrada 100–240 V AC, salida 42 V / 2 A)  
- **Recomendaciones:** cargador original, evitar cortos, no exponer a calor.

---

## 4. Frenos
- **Interruptores:** 2× NA, abren al frenar y cortan señal al controlador.

---

## 5. Display King Meter T319
- **Voltaje:** 36 V (IPX6)  
- **Conector:** 5 pines, cable blindado  
- **Botones:** POWER, +, –, AUTO  
- **Indicadores:** LEDs de batería y asistencia (0–3)
- **Funciones:**
  - Encendido/apagado (POWER)
  - Niveles de asistencia (+/–)
  - **Walk assist:** mantener “–” → ~6 km/h
  - **Auto‑brillo:** modo AUTO
- **Menú de configuración (“ciego”):**
  1. Mantener + y – (~2 s) para entrar
  2. Parámetros (LED titila):
     1. Tamaño rueda (16"–700C/28")
     2. Límite velocidad (12–40 km/h, def. 25)
     3. Brillo (niveles 1–3)
     4. Unidad (km/h o mph)
  3. Ajustar con +/–, confirmar con POWER o avance automático
  4. Salir: mantener POWER (~3 s) o esperar auto-salida

---

## 6. Ramales y Mapeo de Pines
**Estrategia de numeración:** mira el conector lado cable, numera pines de izquierda a derecha.

| Conector        | Pines | Función esperada                     | Método comprobación             |
|-----------------|-------|--------------------------------------|---------------------------------|
| **Display (5)** | 1     | VCC (+36 V)                          | Medir tensión                   |
|                 | 2     | GND                                  | Contin. con batería             |
|                 | 3     | RX (o K‑line)                        | Tensiones pulsatiles            |
|                 | 4     | TX (o K‑line)                        | Pulsos UART                     |
|                 | 5     | A definir (datos/freno?)            | Test continuidad                |
| **Freno L** (2) | 1     | VCC o señal                         | Contin. en reposo               |
|                 | 2     | GND o señal                         | Cambio al frenar                |
| **Freno R** (2) | 1     | VCC o señal                         | Contin. en reposo               |
|                 | 2     | GND o señal                         | Cambio al frenar                |

---

## 7. Pendientes
- Numerar pines reales en conectores 5 y 2 pines siguiendo guía visual.
- Medir y documentar:
  - Tensiones VCC/GND
  - Identificar RX, TX, K‑line
  - Continuidad de frenos en reposo y al accionar
- Completar la tabla de mapeo con valores reales.
- Actualizar esquema final en archivo.

---

*Documento preparado con historial y fotos adjuntas revisadas para asegurar integridad de la información.*


# GZ E-Bike Knowledge

Este documento recopila de manera estructurada toda la información técnica de la e-bike de Gastón Zelechower, agrupada por sistemas:

- **Sistema Eléctrico**
- **Sistema Mecánico**
- **Sistema de Transmisión**
- **Sistema de Frenos**
- **Sistema de Suspensión y Chasis**

---

## 1. Sistema Eléctrico

### 1.1 Controlador Lishui LSW06-OB/LSB-U
- **Voltaje nominal:** 36 V  
- **Corriente nominal:** 7 A (máx. 14 A)  
- **Corte por bajo voltaje:** 31.5 V  
- **Normativa:** EN15194:2017  
- **Fecha fabricación:** 2018-04-17
- **Entradas y salidas:**
  - **Batería:** Rojo (B+), Negro (B–)
  - **Motor (fases):** Amarillo, Verde, Azul
  - **Conector motor:** 6 pines (3 gruesos: potencia; 3 finos: señal Hall)
  - **Sensor Hall:** Rojo (+5 V), Negro (GND), Blanco (señal)
  - **Sensor PAS:** Rojo (+5 V), Negro (GND), Azul (señal)
  - **Ramal display/frenos:** Cable blindado de 6 pines que se divide en:
    - **Display (5 pines):** VCC, GND, RX, TX, K-line
    - **Frenos (2×2 pines):** interruptores NA

### 1.2 Motor Hub Trasero SYX258100CWA0038S1
- **Tipo:** BLDC con sensor Hall  
- **Potencia:** 250 W  
- **RPM:** 215  
- **Cable blindado (6 pines):** 3 fases + 3 Hall

### 1.3 Batería Phylion EBG370-140H1S24
- **Voltaje nominal:** 37.0 V (10S)  
- **Capacidad:** 14.0 Ah  
- **Energía:** 518 Wh  
- **Modelo cargador:** SSLC084V42M (entrada 100–240 V AC, salida 42 V / 2 A)  
- **Recomendaciones:** usar cargador original, evitar cortocircuitos, no exponer a calor extremo

#### 1.3.1 Conector BMS / Balance y Regulador interno
- Pack incluye un conector múltiple para BMS:
  - **Sólo dos hilos extremos:** rojo = +37 V, negro = GND → regulador principal
  - **Otros hilos:** amarillo, naranja, rojo intermedio → conector no usado (BMS/balance)
  - **Hilo marrón:** conector no usado (posible sensor temperatura)
- **Pendiente:** mapear función de cada pin si es necesario diagnóstico interno

### 1.4 Frenos Eléctricos (Señales)
- **Interruptores:** 2× NA, abren al frenar y cortan señal al controlador

### 1.5 Display King Meter T319
- **Voltaje:** 36 V (IPX6)  
- **Conector:** 5 pines, cable blindado  
- **Funciones:** POWER, +, –, AUTO; LEDs de batería/asistencia  
- **Walk assist:** mantener “–” (~6 km/h)  
- **Menú ciego de configuración:**
  1. Mantener + y – (~2 s)
  2. Ajustar con +/– (LED titila) parámetros:
     1. Tamaño rueda (16"–700C)
     2. Límite velocidad (12–40 km/h; def. 25)
     3. Brillo backlight (1–3)
     4. Unidad (km/h o mph)
  3. Confirmar con POWER o esperar avance
  4. Salir: mantener POWER (~3 s)

### 1.6 Ramales y Mapeo de Pines
**Metodología:** numerar pines mirando el conector lado cable de izquierda a derecha.

| Conector        | Pines | Función esperada         | Método              |
|-----------------|-------|--------------------------|---------------------|
| Display (5)     | 1     | VCC (+36 V)              | medir tensión       |
|                 | 2     | GND                      | continuidad         |
|                 | 3     | RX o K-line              | pulsos/tensión      |
|                 | 4     | TX o K-line              | UART/osciloscopio   |
|                 | 5     | A definir                | continuidad         |
| Frenos (2×2)    | 1,2   | señal/freno (NA)         | cambio al frenar    |

**Pendientes:** numerar pines y medir VCC/GND/RX/TX; documentar resultados.

---

## 2. Sistema Mecánico
> **Pendiente:** fotos y datos de cuadro, horquilla, suspensión, dirección

---

## 3. Sistema de Transmisión
> **Pendiente:** tipo de cadena, platos, cambios, eje central, pedales

---

## 4. Sistema de Frenos (Mecánico)
> **Pendiente:** modelo de discos, pinzas, pastillas, adaptadores

---

## 5. Sistema de Suspensión y Chasis
> **Pendiente:** tipo de suspensión (si aplica), materiales del cuadro, geometría

---


# 🏥 Reto 01 — Gestión de Hospital

**Nivel:** 💀 Desafío Final | **Dificultad:** 💀 Extremo

---

## 🎯 Historia

El **Hospital General de Algoritmia** tiene su sala de urgencias al borde del caos. El Dr. **Urgencia Pérez** necesita un sistema de triaje y gestión de colas para manejar a los pacientes de manera eficiente y justa.

El sistema debe gestionar múltiples aspectos simultáneamente y tomar decisiones complejas en tiempo real.

---

## 📋 El Sistema

### Categorías de Triaje (Manchester)
| Código | Color | Prioridad | Tiempo máximo espera | Descripción |
|--------|-------|-----------|---------------------|-------------|
| 1 | 🔴 Rojo | Inmediata | 0 min | Riesgo vital (paro cardíaco, etc.) |
| 2 | 🟠 Naranja | Muy urgente | 10 min | Dolor severo, riesgo alto |
| 3 | 🟡 Amarillo | Urgente | 60 min | Condición moderada |
| 4 | 🟢 Verde | Poco urgente | 120 min | Condición leve |
| 5 | ⚪ Blanco | No urgente | 240 min | Visita ambulatoria |

### Los Módulos del Sistema

#### Módulo 1: Registro de Pacientes
- Cada paciente tiene: ID, nombre, edad, síntomas, hora de llegada, categoría de triaje
- Si llega un categoría 1 (Rojo): **interrumpe** todo y va directo

#### Módulo 2: Cola de Prioridad
- Pacientes ordenados por categoría (1 primero) y luego por hora de llegada
- Si hay empate de categoría: el que llegó antes va primero

#### Módulo 3: Asignación de Médicos
- El hospital tiene **3 médicos** disponibles
- Cada médico atiende UN paciente a la vez
- Tiempo de atención estimado: 15 min por categoría (cat 1→15min, cat 2→30min, cat 3→45min, cat 4→15min, cat 5→10min)

#### Módulo 4: Alertas de Espera
- Si un paciente lleva más tiempo del máximo permitido sin ser atendido: alerta roja
- Si todos los médicos están ocupados y hay un cat 1 en espera: EMERGENCIA CRÍTICA

#### Módulo 5: Estadísticas
- Tiempo promedio de espera por categoría
- Médico más eficiente (menor tiempo promedio de atención)
- Pico de ocupación (momento con más pacientes simultáneos)

---

## 🔢 Entradas

- Configuración inicial: número de médicos disponibles
- Lista de llegadas de pacientes (en orden cronológico): (hora, nombre, edad, categoría)
- Lista de altas (paciente termina de ser atendido): (hora, id_paciente, id_medico)

## 📤 Salidas

- Estado de la cola en tiempo real (cada vez que llega alguien o hay un alta)
- Alertas de espera excesiva
- Estadísticas finales del turno

---

## 🧪 Caso de Prueba

### Llegadas:
```
08:00 - Juan García,    45 años, Categoría 3 (Amarillo)
08:05 - María López,   32 años, Categoría 1 (Rojo) ← INTERRUMPE
08:10 - Pedro Ramírez, 67 años, Categoría 2 (Naranja)
08:15 - Ana Torres,    28 años, Categoría 4 (Verde)
08:20 - ALTA: María López (atendida en 15 min, Médico 1)
08:20 - Luis Mendoza,  55 años, Categoría 2 (Naranja)
```

### Estado esperado a las 08:05:
```
🚨 EMERGENCIA — Categoría 1: María López (08:05)
Cola de prioridad:
  1. [🔴] María López   - Categoría 1 - Esperando: 0 min
  2. [🟡] Juan García   - Categoría 3 - Esperando: 5 min
  
Médico 1: LIBRE → Asignando María López
Médico 2: LIBRE
Médico 3: LIBRE
```

### Estado esperado a las 08:20 (después del alta y nueva llegada):
```
✅ ALTA: María López (Médico 1 libre en 08:20)

Cola de prioridad actualizada:
  1. [🟠] Pedro Ramírez - Categoría 2 - Esperando: 10 min ⚠️ (al límite)
  2. [🟠] Luis Mendoza  - Categoría 2 - Esperando: 0 min
  3. [🟡] Juan García   - Categoría 3 - Esperando: 20 min

Médico 1: LIBRE → Asignando Pedro Ramírez
Médico 2: LIBRE
Médico 3: LIBRE
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Este es el reto más complejo del repositorio. PLANIFICA antes de dibujar.**
>
> Guarda con `reto_01_diagrama_arquitectura.png` (arquitectura general) y archivos separados para cada módulo.

### Arquitectura Sugerida

```
[Evento Llegada Paciente]     [Evento Alta Médico]
        ↓                             ↓
  [Módulo 1: Registro]      [Liberar Médico]
        ↓                             ↓
  [Módulo 2: Cola]  ←─────────────────┘
        ↓
  [Módulo 3: Asignación]
        ↓
  [Módulo 4: Alertas]
        ↓
  [Módulo 5: Estadísticas] (al final del turno)
```

**Diagrama de cada módulo:**

**Módulo 2 (Cola):**
- Recibe un nuevo paciente
- Inserta en la posición correcta según categoría y hora de llegada
- Muestra el estado actual de la cola

**Módulo 3 (Asignación):**
- Verifica si hay médicos libres
- Si hay médico libre Y hay pacientes en cola: asigna el primero de la cola
- Si el primer paciente es Cat 1 y todos los médicos están ocupados: EMERGENCIA CRÍTICA

**Lista de verificación:**
- [ ] Estructura de datos para la cola de pacientes (ordenada por prioridad)
- [ ] Estructura de datos para el estado de cada médico (libre/ocupado/paciente asignado)
- [ ] Función de inserción en cola con ordenamiento por prioridad y luego por hora
- [ ] Función de asignación de médico
- [ ] Función de gestión de alertas por tiempo máximo
- [ ] Función de estadísticas al cierre
- [ ] Programa principal que procesa eventos en orden cronológico

---

## 💻 Fase 2 — Tu Código

> ⚠️ **Solo completa esta sección DESPUÉS de validar tu diagrama.**

**Lenguaje elegido:** `________________`

```
// Escribe tu código aquí
```

---

## 💡 Pistas

<details>
<summary>Pista 1 — La cola de prioridad</summary>

Una cola de prioridad es como una lista ordenada donde insertar un nuevo elemento significa encontrar la posición correcta según su prioridad. Para insertar: recorre la lista existente y encuentra el primer elemento con menor prioridad (mayor número de categoría) o con la misma prioridad pero que llegó después.

</details>

<details>
<summary>Pista 2 — Representar el tiempo</summary>

Convierte todas las horas a minutos desde el inicio para hacer comparaciones más fáciles. Por ejemplo, 08:05 = (8 × 60) + 5 = 485 minutos. La diferencia entre dos tiempos es simplemente la resta.

</details>

<details>
<summary>Pista 3 — El criterio de alerta de espera</summary>

Después de cada evento (llegada o alta), recorre la cola y verifica si algún paciente lleva más tiempo esperando del permitido por su categoría. El tiempo de espera = `tiempo_actual - hora_llegada`.

</details>

---

## ⭐ Reto Extra

El hospital quiere predecir la carga de trabajo. Dado el historial de un mes de llegadas (día y hora de cada paciente), identifica las **3 horas pico** (franjas de 1 hora con más llegadas) y los **días de menor demanda**. Diseña el análisis estadístico para esta "inteligencia operacional".

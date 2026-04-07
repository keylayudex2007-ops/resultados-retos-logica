# 🏆 Reto 02 — Sistema de Torneos

**Nivel:** 💀 Desafío Final | **Dificultad:** 💀 Extremo

---

## 🎯 Historia

La **Liga de Videojuegos de Algoritmia** organiza torneos de eliminación directa (brackets). El coordinador **Don Bracket** necesita un sistema completo que gestione el torneo desde la inscripción hasta la ceremonia de premiación.

El torneo tiene reglas especiales que lo hacen único — y particularmente retador de programar.

---

## 📋 Las Reglas del Torneo

### Estructura
- El número de jugadores debe ser **potencia de 2** (4, 8, 16, 32...)
- Si hay más jugadores de los que caben, los excedentes quedan en **lista de espera**
- Si hay menos, se agregan **"Bye"** (pases automáticos a la siguiente ronda)

### Sistema de Puntuación de Partidas
Cada partida se juega con 3 sets. Para ganar un set, necesitas mínimo 11 puntos con diferencia de al least 2.
- Gana la partida quien gane 2 sets primero
- La puntuación de cada set es ingresada manualmente

### Reglas de Seeding (Cabezas de Serie)
- Los 4 mejores clasificados del ranking anterior son "cabezas de serie"
- Las cabezas de serie 1 y 2 están en brackets opuestos (no pueden verse hasta la final)
- Las cabezas de serie 3 y 4 también en brackets distintos

### Sistema de Puntos ELO (simplificado)
Tras cada partida, los puntos ELO se actualizan:
- Ganador recibe: `+50 - (diferencia_de_elo / 40)` puntos (mínimo +10)
- Perdedor pierde: `+30 + (diferencia_de_elo / 40)` puntos (mínimo +5)
- Si el ganador tenía ELO menor: el ganador recibe puntos extra (+20 bonus)

### Desempate Especial
Si hay empate en el match (1-1 en sets), se juega un **"Super Tiebreak"** a 15 puntos.

---

## 📋 Los Módulos del Sistema

### Módulo 1: Registro e Inicialización
- Registra jugadores con nombre, ELO inicial, país
- Determina el tamaño del bracket (próxima potencia de 2)
- Coloca a los jugadores según el seeding

### Módulo 2: Generador de Bracket
- Crea el árbol de eliminación: ronda 1, cuartos, semifinales, final
- Asigna partidas: ¿quién juega contra quién?
- Muestra el bracket visualmente (con formato)

### Módulo 3: Procesador de Partidas
- Recibe los puntajes de una partida
- Valida que los puntajes sean correctos (mínimo 11, diferencia ≥ 2)
- Determina el ganador del set y de la partida
- Actualiza el ELO de ambos jugadores

### Módulo 4: Progresión del Bracket
- Avanza al ganador a la siguiente ronda
- Si la lista de espera tiene jugadores y hubo un "Bye", incorpora al primero en lista de espera
- Muestra el estado del bracket actualizado

### Módulo 5: Estadísticas y Premiación
- Top 4 del torneo (ganador, finalista, dos semifinalistas)
- Mayor ganancia de ELO en el torneo
- Partida más reñida (mayor cantidad de puntos totales)
- "Upset" del torneo: victoria de ELO más bajo contra más alto

---

## 🧪 Caso de Prueba

### Jugadores (8 plazas):
```
1. Arístides  ELO: 1800  (cabeza de serie 1)
2. Bertha     ELO: 1750  (cabeza de serie 2)
3. Carmelo    ELO: 1700  (cabeza de serie 3)
4. Diana      ELO: 1650  (cabeza de serie 4)
5. Eduardo    ELO: 1400
6. Fernanda   ELO: 1350
7. Gerardo    ELO: 1300
8. Helena     ELO: 1250
```

### Bracket generado (Ronda 1):
```
Bloque A:               Bloque B:
Arístides vs. Helena     Bertha vs. Gerardo
Carmelo vs. Fernanda     Diana vs. Eduardo
```

### Resultado Ronda 1:
```
Partida 1: Arístides vs. Helena
  Set 1: 11-7   → Arístides ✅
  Set 2: 8-11   → Helena ✅
  Set 3: 11-9   → Arístides ✅
  Ganador: Arístides (2-1)

Partida 2: Carmelo vs. Fernanda
  Set 1: 11-4   → Carmelo ✅
  Set 2: 11-6   → Carmelo ✅
  Ganador: Carmelo (2-0)

[...continúa con las partidas del Bloque B]
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Planifica la arquitectura completa antes de dibujar los diagramas.**
>
> Guarda con múltiples archivos: `reto_02_arquitectura.png`, `reto_02_modulo_N.png`

### Diagramas Requeridos

1. **Arquitectura General**: cómo interactúan los 5 módulos
2. **Módulo 1**: registro y seeding
3. **Módulo 2**: generación del bracket (árbol binario)
4. **Módulo 3**: procesamiento de una partida con validación de sets
5. **Módulo 4**: progresión y actualización del bracket
6. **Módulo 5**: cálculo de estadísticas

### Lista de Verificación

**Módulo 1:**
- [ ] Calcula la próxima potencia de 2 para el número de jugadores
- [ ] Ordena por ELO descendente para el seeding
- [ ] Si hay < N jugadores: rellena con "Bye" en las últimas posiciones

**Módulo 2:**
- [ ] El bracket es un árbol binario completo
- [ ] Cabeza 1 y 2 en lados opuestos; 3 y 4 en lados distintos
- [ ] Muestra el bracket en formato texto (árbol hacia la derecha)

**Módulo 3:**
- [ ] Valida cada puntaje de set (≥11, diferencia ≥2)
- [ ] Cuenta los sets ganados por cada jugador
- [ ] Si hay 1-1: solicitar el super tiebreak (a 15)
- [ ] Actualiza ELO según la fórmula

**Módulo 4:**
- [ ] Avanza al ganador en el árbol del bracket
- [ ] Si el contrincante fue "Bye": el jugador avanza automáticamente
- [ ] Muestra visualmente el estado actualizado del bracket

---

## 💻 Fase 2 — Tu Código

> ⚠️ **Solo completa esta sección DESPUÉS de validar todos los diagramas.**

**Lenguaje elegido:** `________________`

```
// Estructura del árbol del bracket:
// Un nodo del bracket contiene:
// - jugador_izquierdo
// - jugador_derecho
// - ganador (null hasta que se juegue)
// - ronda (1=octavos, 2=cuartos, 3=semi, 4=final)

// Escribe tu código aquí
```

---

## 💡 Pistas

<details>
<summary>Pista 1 — Calcular la próxima potencia de 2</summary>

Empieza con N=1 y multiplica por 2 hasta que N >= número de jugadores. Ejemplo: 6 jugadores → 1, 2, 4, 8 → bracket de 8.

</details>

<details>
<summary>Pista 2 — El árbol del bracket como arreglo</summary>

Puedes representar el bracket como un arreglo plano donde los índices representan posiciones. Si la final es el índice 1, las semifinales son 2 y 3, los cuartos son 4, 5, 6, 7, etc. El ganador del índice `i` avanza al índice `i/2` (división entera).

</details>

<details>
<summary>Pista 3 — Validar un set de ping pong</summary>

Un set es válido si: `(puntaje >= 11 Y diferencia >= 2)` O `(puntaje > 11 Y diferencia == 2)`. Esto cubre el caso normal (11-x con diferencia 2) y el caso extendido (12-10, 13-11, etc.).

</details>

---

## ⭐ Reto Extra

Implementa un **sistema de predicción probabilística**: basado solo en los ELO iniciales, calcula la probabilidad de que cada jugador llegue a la final y de que gane el torneo. La probabilidad de que A gane a B es: `P(A gana) = 1 / (1 + 10^((ELO_B - ELO_A)/400))`. Muestra el "favorito teórico" del torneo.

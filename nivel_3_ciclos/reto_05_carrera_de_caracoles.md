# 🐌 Reto 05 — La Carrera de Caracoles

**Nivel:** ⭐⭐⭐ Ciclos | **Dificultad:** 🔴 Muy Difícil

---

## 🎯 Historia

En la **Gran Pista de Barro de Caracol City**, se celebra el evento más lento y emocionante del año: **La Carrera de los Caracoles**. Hay **N caracoles** compitiendo en una pista de **L centímetros**.

Cada caracol tiene sus propias características:
- **Velocidad base** (cm por turno)
- **Suerte**: en cada turno, hay una probabilidad de eventos especiales

Los **eventos especiales** ocurren según el número del turno (no son aleatorios — siguen una lista de eventos predefinida):

| Turno | Evento | Efecto |
|-------|--------|--------|
| Múltiplo de 3 | Lluvia | Todos los caracoles se mueven 1 cm extra |
| Múltiplo de 5 | Barro | El caracol más lento pierde 2 cm (no puede ir negativo) |
| Múltiplo de 7 | Viento | El caracol en primer lugar se mueve 3 cm extra |
| Múltiplo de 11 | Trampa | El caracol en último lugar salta al promedio de posiciones |

La carrera termina cuando **algún caracol** llega o supera los L centímetros.

---

## 📋 El Problema

Simula la carrera turno por turno. Muestra el estado de cada turno y anuncia al ganador.

---

## 🔢 Entradas

- **N**: número de caracoles (2 a 5)
- **L**: longitud de la pista (en centímetros)
- **velocidades**: lista de N velocidades base (una por caracol)

## 📤 Salidas

- Estado de la carrera cada turno (posición de cada caracol)
- Los eventos que ocurrieron en cada turno
- El caracol ganador y en cuántos turnos ganó

---

## 🧪 Casos de Prueba

### Caso 1 — 3 caracoles, pista de 30 cm
```
Entrada:
N = 3
L = 30
Velocidades: [5, 3, 4]  (Caracol A: 5, Caracol B: 3, Caracol C: 4)

Turno 1: A=5, B=3, C=4
  (sin eventos)

Turno 2: A=10, B=6, C=8
  (sin eventos)

Turno 3: A=15, B=9, C=12  [LLUVIA: +1 a todos]
  → A=16, B=10, C=13

Turno 4: A=21, B=13, C=17
  (sin eventos)

Turno 5: A=26, B=16, C=21  [BARRO: el más lento (B=16) pierde 2cm]
  → A=26, B=14, C=21

Turno 6: A=31 ← LLEGÓ A LA META!
  → B=17, C=25  (pero A ya ganó)

🏆 Ganador: Caracol A en el turno 6.
```

**Verificar que los eventos encadenen correctamente:**
- Turno 6: ¿es múltiplo de 2? No. ¿de 3? No. ¿de 5? No. ¿de 7? No. → Sin evento.
  - A: 26 + 5 = 31 ≥ 30 → ¡Gana!

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Este es un diagrama complejo. Considera dividirlo en **sub-diagramas**:
> 1. Diagrama principal (ciclo de turnos)
> 2. Sub-diagrama: "Aplicar eventos del turno"
> 3. Sub-diagrama: "Verificar si hay ganador"

**Variables importantes:**
- `posiciones[]` ← arreglo con la posición de cada caracol
- `turno` ← contador de turnos
- `ganador` ← índice del caracol ganador (-1 si no hay)
- Variables auxiliares para el caracol más lento y más rápido

**Lista de verificación del diagrama:**
- [ ] Lee N, L y las velocidades
- [ ] Inicializa todas las posiciones en 0
- [ ] El ciclo principal continúa mientras no haya ganador
- [ ] En cada turno: mueve todos los caracoles (posicion[i] += velocidad[i])
- [ ] Verifica eventos (múltiplos de 3, 5, 7, 11) y los aplica
- [ ] Tras los eventos: verifica si algún caracol llegó a L
- [ ] Si hay ganador: guarda cuál es y sale del ciclo
- [ ] Muestra el resumen final

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
<summary>Pista 1 — Múltiples eventos por turno</summary>

Un turno puede activar VARIOS eventos simultáneamente. Por ejemplo, el turno 15 es múltiplo de 3 (lluvia) Y de 5 (barro) al mismo tiempo. Verifica cada condición por separado (no uses else entre ellas).

</details>

<details>
<summary>Pista 2 — Encontrar el más lento y el más rápido</summary>

Para aplicar el evento de "barro" o "viento", necesitas encontrar el caracol con menor/mayor posición. Recorre el arreglo de posiciones buscando el mínimo/máximo y guarda su índice.

</details>

<details>
<summary>Pista 3 — El promedio para el evento de trampa</summary>

Para el evento del turno múltiplo de 11:
`promedio = (suma de todas las posiciones) / N`
Luego el caracol en último lugar sube a `promedio` (puedes redondear al entero más cercano).

</details>

---

## ⭐ Reto Extra

Agrega un evento de **turno múltiplo de 13**: todos los caracoles intercambian posiciones de manera rotatoria (el primero pasa al lugar del segundo, el segundo al tercero, ..., el último al lugar del primero). ¿Cambia quién gana?

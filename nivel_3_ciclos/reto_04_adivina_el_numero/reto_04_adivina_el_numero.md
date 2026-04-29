# 🎯 Reto 04 — Adivina el Número

**Nivel:** ⭐⭐⭐ Ciclos | **Dificultad:** 🟠 Difícil

---

## 🎯 Historia

El profesor **Cornelio** tiene el pasatiempo más estresante del mundo: adivinar números. En su versión del juego, la máquina **escoge un número secreto** (dado por el sistema o por otro jugador) y el jugador tiene **intentos limitados** para adivinarlo.

Pero la máquina de Cornelio es especialmente cruel:
- El número secreto está entre **1 y 100**
- El jugador tiene máximo **7 intentos**
- En cada intento, la máquina solo dice: `"Más alto"`, `"Más bajo"` o `"¡Correcto!"`
- Si el jugador **no adivina en 7 intentos**: pierde y la máquina se mofa: `"¡Perdiste! El número era X. Con búsqueda binaria habrías adivinado en máximo 7 intentos."`
- El juego lleva un **registro de los intentos** (qué número dijo el jugador y qué respondió la máquina)
- **Bonus de eficiencia**: si el jugador adivina en 3 intentos o menos, recibe un mensaje de `"¡Genio! Usaste búsqueda binaria perfecta."`

---

## 📋 El Problema

Simula el juego completo: el número secreto está dado, el jugador ingresa sus intentos uno por uno. El sistema responde y al final reporta el resultado.

---

## 🔢 Entradas

- **secreto**: el número que hay que adivinar (1-100)
- En cada intento: **intento** (número que ingresa el jugador, 1-100)

## 📤 Salidas

- Respuesta de la máquina en cada intento
- Al terminar: resumen con el historial de intentos y el resultado final

---

## 🧪 Casos de Prueba

### Caso 1 — El jugador adivina en el 4to intento
```
Secreto = 42

Intento 1: jugador dice 50 → Más bajo
Intento 2: jugador dice 25 → Más alto
Intento 3: jugador dice 37 → Más alto
Intento 4: jugador dice 42 → ¡Correcto! Adivinaste en 4 intentos.

Historial:
[50: Más bajo] [25: Más alto] [37: Más alto] [42: ¡Correcto!]
```

### Caso 2 — El jugador pierde
```
Secreto = 73

Intento 1: 10 → Más alto
Intento 2: 90 → Más bajo
Intento 3: 80 → Más bajo
Intento 4: 75 → Más bajo
Intento 5: 74 → Más bajo
Intento 6: 60 → Más alto
Intento 7: 70 → Más alto

¡Perdiste! El número era 73.
Con búsqueda binaria habrías adivinado en máximo 7 intentos.
```

### Caso 3 — Adivinanza genial (búsqueda binaria perfecta)
```
Secreto = 64

Intento 1: 50 → Más alto
Intento 2: 75 → Más bajo
Intento 3: 63 → Más alto
... (continúa hasta encontrar 64 en ≤ 7 intentos)
```

*(Nota: si adivinas en 3 o menos, se activa el bonus de genio)*

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_04_diagrama.[png|pdf]` en esta carpeta.

**Variables importantes:**
- `secreto` ← el número a adivinar
- `intentos` ← contador de intentos (empieza en 0)
- `adivinado` ← booleano (empieza en falso)
- `historial` ← lista de pares (intento, respuesta)

**Lista de verificación del diagrama:**
- [ ] Lee el número secreto
- [ ] El ciclo continúa mientras `intentos < 7` Y `adivinado == falso`
- [ ] En cada iteración: lee el intento del jugador, incrementa el contador
- [ ] Compara el intento con el secreto (3 casos: ==, <, >)
- [ ] Registra en el historial
- [ ] Si adivinó: activa la bandera `adivinado = verdadero`
- [ ] Al salir del ciclo: verifica si ganó o perdió
- [ ] Si ganó en ≤ 3 intentos: mensaje de genio
- [ ] Muestra el historial al final

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
<summary>Pista 1 — La condición del ciclo</summary>

El ciclo tiene DOS condiciones para continuar: que no se hayan agotado los intentos Y que no se haya adivinado. Si cualquiera de las dos falla, el ciclo termina. Usa AND: `intentos < 7 AND NOT adivinado`.

</details>

<details>
<summary>Pista 2 — ¿Ganó o perdió al salir del ciclo?</summary>

Cuando el ciclo termina, hay dos posibilidades:
1. Termina porque `adivinado == verdadero` → el jugador ganó
2. Termina porque `intentos == 7` y `adivinado == falso` → el jugador perdió

La variable `adivinado` te dice cuál fue.

</details>

---

## ⭐ Reto Extra

Implementa la **inteligencia artificial** que juega sola usando búsqueda binaria: la IA mantiene dos variables `bajo = 1` y `alto = 100`, y en cada turno prueba el punto medio `(bajo + alto) / 2`. Diagrama el algoritmo de la IA y demuestra que siempre adivina en 7 o menos intentos.

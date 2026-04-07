# 🗺️ Reto 01 — El Laberinto del Tesoro

**Nivel:** 🔥 Lógica Avanzada | **Dificultad:** 🟠 Difícil

---

## 🎯 Historia

El explorador **Indiana Algoritmos** está atrapado en un laberinto en forma de cuadrícula. El laberinto es una matriz de N×N celdas, donde cada celda puede ser:
- `0` → Camino libre
- `1` → Pared (no se puede pasar)
- `T` → Tesoro (la meta)
- `S` → El inicio (donde está Indiana)

Indiana solo puede moverse en 4 direcciones: **Arriba, Abajo, Izquierda, Derecha**. No puede salir de los límites de la cuadrícula.

Indiana usa el siguiente **algoritmo de exploración**:
1. Va hacia **Arriba** si puede
2. Si no puede, va hacia la **Derecha**
3. Si no puede, va hacia **Abajo**
4. Si no puede, va hacia la **Izquierda**
5. Si no puede ir a ningún lado: retrocede al paso anterior (backtracking)
6. Si ya recorrió todas las opciones sin encontrar el tesoro: declara "¡Sin salida!"

El algoritmo marca las celdas visitadas para no repetirlas.

---

## 📋 El Problema

Dado el laberinto como matriz, simula el recorrido de Indiana paso a paso y determina si puede encontrar el tesoro, mostrando el camino recorrido.

---

## 🔢 Entradas

- **N**: tamaño de la cuadrícula (N×N)
- **La matriz** del laberinto (N filas × N columnas con valores 0, 1, T, S)

## 📤 Salidas

- El recorrido paso a paso (posición actual en cada paso)
- Si encontró el tesoro: el camino óptimo seguido
- Si no lo encontró: "¡Sin salida! El tesoro es inalcanzable."
- La cantidad de pasos dados

---

## 🧪 Casos de Prueba

### Caso 1 — Laberinto 4×4 con solución
```
Laberinto:
S 0 1 0
1 0 1 0
1 0 0 0
1 1 0 T

Posición inicial: (0,0) = S
Posición del tesoro: (3,3) = T

Salida esperada:
Paso 1:  (0,0)→(0,1)  [Derecha]
Paso 2:  (0,1)→(1,1)  [Abajo]
Paso 3:  (1,1)→(2,1)  [Abajo]
Paso 4:  (2,1)→(2,2)  [Derecha]
Paso 5:  (2,2)→(3,2)  [Abajo]
Paso 6:  (3,2)→(3,3)  [Derecha] ← TESORO ENCONTRADO!

Camino: (0,0)→(0,1)→(1,1)→(2,1)→(2,2)→(3,2)→(3,3)
Total de pasos: 6
```

### Caso 2 — Sin solución
```
Laberinto:
S 1 0
1 1 0
0 0 T

Salida esperada:
No se puede llegar al tesoro desde la posición inicial.
¡Sin salida! El tesoro es inalcanzable.
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Este es un problema de **backtracking**. El diagrama tendrá una estructura recursiva o usará una pila (stack).
>
> Guarda con `reto_01_diagrama.[png|pdf]`.

**Variables importantes:**
- `laberinto[N][N]` ← la cuadrícula
- `visitado[N][N]` ← booleanos, marcan si esa celda ya fue explorada
- `camino[]` ← lista de posiciones del camino actual
- `pos_actual` ← (fila, columna) de Indiana

**Lista de verificación:**
- [ ] Lee el laberinto y encuentra la posición de S y T
- [ ] Inicializa `visitado` en todo falso
- [ ] Función de exploración: intenta las 4 direcciones en orden (Arriba, Derecha, Abajo, Izquierda)
- [ ] Para cada dirección: verifica si está dentro de la cuadrícula, si no es pared, si no fue visitada
- [ ] Si la celda es T → ¡éxito! Muestra el camino
- [ ] Marca la celda actual como visitada antes de avanzar
- [ ] Si ninguna dirección funciona → retrocede (backtrack: desmarca la celda y regresa)
- [ ] Si regresaste al inicio sin encontrar T → sin salida

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
<summary>Pista 1 — El concepto de backtracking</summary>

El backtracking es como explorar un laberinto en la vida real: vas por un camino, y si llegas a un callejón sin salida, retrocedes y pruebas otra dirección. En el diagrama, esto se representa como una función que se llama a sí misma (recursión) o como una pila (stack) que guarda los pasos dados.

</details>

<details>
<summary>Pista 2 — Verificar límites de la cuadrícula</summary>

Antes de moverte a (fila, columna), verifica:
- `fila >= 0 AND fila < N` (no te salgas por arriba o abajo)
- `columna >= 0 AND columna < N` (no te salgas por izquierda o derecha)
- `laberinto[fila][columna] != 1` (no es pared)
- `visitado[fila][columna] == falso` (no la has visitado)

</details>

---

## ⭐ Reto Extra

Indiana quiere encontrar el **camino más corto** al tesoro (menor número de pasos). El algoritmo actual encuentra un camino, pero no necesariamente el más corto. Modifica el diagrama para explorar TODOS los caminos posibles y quedarte con el más corto.

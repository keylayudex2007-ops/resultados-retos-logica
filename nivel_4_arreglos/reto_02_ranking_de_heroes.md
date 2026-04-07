# 🦸 Reto 02 — El Ranking de Héroes

**Nivel:** ⭐⭐⭐⭐ Arreglos | **Dificultad:** 🟠 Difícil

---

## 🎯 Historia

La **Liga de Héroes Improbables** tiene una base de datos de sus miembros con sus puntuaciones de batalla. El director de la Liga necesita generar el **ranking oficial** para el anuario.

El ranking funciona así:
1. Los héroes se ordenan por **puntuación** de mayor a menor
2. Si dos héroes tienen la misma puntuación, se ordenan **alfabéticamente por nombre** (A primero)
3. Los primeros 3 lugares reciben medallas: 🥇 🥈 🥉
4. Cualquier héroe con apodo que termine en **"Man"** o **"Woman"** recibe el título **"Clásico"**
5. El ranking muestra el **cambio de posición** respecto al ranking anterior (si se proporciona)

---

## 📋 El Problema

Dado el listado de héroes con sus puntuaciones, genera el ranking ordenado con medallas y títulos.

---

## 🔢 Entradas

- **N**: número de héroes
- **N pares** de (nombre, puntuación)
- Opcionalmente: el ranking anterior (lista de nombres en orden)

## 📤 Salidas

- El ranking ordenado con posición, nombre, puntuación, medalla y título (si aplica)
- El cambio de posición respecto al ranking anterior (↑ subió, ↓ bajó, = igual, ★ nuevo)

---

## 🧪 Casos de Prueba

### Caso 1 — Ranking simple
```
Entrada:
N = 5
SpiderMan     850
IronWoman     920
Hulk          850
Thor          910
AntMan        780

Salida esperada (ranking):
1. 🥇 IronWoman   920  [Clásico]
2. 🥈 Thor        910
3. 🥉 Hulk        850
4.    SpiderMan   850  [Clásico]
5.    AntMan      780  [Clásico]

(Nota: Hulk y SpiderMan tienen 850 puntos → ordenados alfabéticamente: Hulk < SpiderMan)
```

### Caso 2 — Con ranking anterior
```
Ranking anterior: [Thor, IronWoman, SpiderMan, Hulk, AntMan]
Ranking nuevo:    [IronWoman, Thor, Hulk, SpiderMan, AntMan]

Salida:
1. 🥇 IronWoman   920  [Clásico]  ↑1 (era 2do)
2. 🥈 Thor        910             ↓1 (era 1ro)
3. 🥉 Hulk        850             ↑1 (era 4to)
4.    SpiderMan   850  [Clásico]  ↓1 (era 3ro)
5.    AntMan      780  [Clásico]  = (era 5to)
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda con el nombre `reto_02_diagrama.[png|pdf]`.

**Sub-diagramas:**
1. Ordenamiento por puntuación y nombre (Bubble Sort o similar)
2. Asignación de medallas y títulos
3. Cálculo de cambios respecto al ranking anterior

**Lista de verificación:**
- [ ] Lee N pares de nombre/puntuación en dos listas paralelas
- [ ] Implementa el ordenamiento (mayor puntuación primero, empate → alfabético)
- [ ] Asigna medallas a los 3 primeros
- [ ] Verifica si cada nombre termina en "Man" o "Woman"
- [ ] Si hay ranking anterior: busca la posición anterior de cada héroe y calcula el cambio
- [ ] Muestra el resultado formateado

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
<summary>Pista 1 — Ordenamiento burbuja (Bubble Sort)</summary>

Compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Repite esto hasta que no ocurra ningún intercambio. El criterio de comparación: primero por puntuación (desc), luego por nombre (asc).

</details>

<details>
<summary>Pista 2 — Detectar "Man" o "Woman" al final</summary>

Verifica si el nombre termina con "Man" o "Woman" revisando los últimos 3 o 5 caracteres. Muchos lenguajes tienen funciones como `endsWith()` o `substr()`.

</details>

<details>
<summary>Pista 3 — Cambio de posición</summary>

Para cada héroe en el nuevo ranking (posición `i`), busca su posición en el ranking anterior (`j`). Si `i < j`, subió (`↑ j-i`). Si `i > j`, bajó (`↓ i-j`). Si `i == j`, igual (`=`).

</details>

---

## ⭐ Reto Extra

La Liga quiere un sistema de **"rachas"**: si un héroe aparece en el Top 3 por 3 torneos seguidos, recibe la insignia **"Leyenda Viviente"**. Diseña el diagrama para rastrear el historial de 5 torneos consecutivos.

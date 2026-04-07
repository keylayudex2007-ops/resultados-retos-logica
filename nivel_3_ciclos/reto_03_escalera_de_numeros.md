# 🔢 Reto 03 — La Escalera de Números

**Nivel:** ⭐⭐⭐ Ciclos | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

La profesora **Dora Escalante** (sí, su apellido es apropiado) enseña programación en la secundaria. Para enseñar ciclos anidados, dibuja "escaleras numéricas" en el pizarrón. Los estudiantes deben recrearlas con código.

Este reto tiene **tres escaleras** que debes dibujar. Cada una demuestra un patrón distinto. La dificultad está en entender cómo los ciclos externos e internos se relacionan.

---

## 📋 El Problema

Dado un número **N** (altura de la escalera), dibuja los tres patrones siguientes:

---

### Patrón A — Triángulo de números crecientes

Para N=5:
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

### Patrón B — Triángulo invertido de asteriscos con números de fila

Para N=5:
```
Fila 1: * * * * *
Fila 2: * * * *
Fila 3: * * *
Fila 4: * *
Fila 5: *
```

---

### Patrón C — Diamante de números

Para N=4:
```
   1
  1 2
 1 2 3
1 2 3 4
 1 2 3
  1 2
   1
```
*(Los espacios crean la forma de diamante)*

---

## 🔢 Entradas

- **N**: número que define la altura del patrón (entero positivo, 1 ≤ N ≤ 10)

## 📤 Salidas

- Los tres patrones dibujados correctamente

---

## 🧪 Casos de Prueba

### Caso 1 — N=3
**Patrón A:**
```
1
1 2
1 2 3
```

**Patrón B:**
```
Fila 1: * * *
Fila 2: * *
Fila 3: *
```

**Patrón C:**
```
  1
 1 2
1 2 3
 1 2
  1
```

### Caso 2 — N=1
**Patrón A:**
```
1
```
**Patrón B:**
```
Fila 1: *
```
**Patrón C:**
```
1
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Dibuja **3 diagramas separados**, uno por patrón.  
> Guarda las imágenes con nombres `reto_03_patron_a.png`, `reto_03_patron_b.png`, `reto_03_patron_c.png`.

**Lista de verificación para Patrón A:**
- [ ] Ciclo externo de `fila = 1` hasta N
- [ ] Ciclo interno de `j = 1` hasta `fila`
- [ ] Imprime j (con espacio, sin salto de línea)
- [ ] Al terminar el ciclo interno: salto de línea

**Lista de verificación para Patrón B:**
- [ ] Ciclo externo de `fila = 1` hasta N
- [ ] Imprime "Fila X: " donde X es el número de fila
- [ ] Ciclo interno de `j = 1` hasta `N - fila + 1`
- [ ] Imprime "*" (con espacio)
- [ ] Salto de línea al final

**Lista de verificación para Patrón C (el más difícil):**
- [ ] Primera mitad: fila sube de 1 a N (ciclo externo ascendente)
  - [ ] Imprimir `N - fila` espacios
  - [ ] Imprimir números del 1 al fila
- [ ] Segunda mitad: fila baja de N-1 a 1 (ciclo externo descendente)
  - [ ] Imprimir `N - fila` espacios
  - [ ] Imprimir números del 1 al fila

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
<summary>Pista 1 — Ciclos anidados</summary>

Un ciclo anidado tiene esta estructura:
```
Para fila = 1 hasta N:
    Para j = 1 hasta fila:
        Imprimir j
    Imprimir salto de línea
```
El ciclo interno se ejecuta completamente en CADA iteración del ciclo externo.

</details>

<details>
<summary>Pista 2 — Los espacios en el Patrón C</summary>

En el diamante, los espacios antes de los números siguen este patrón:
- Fila 1: N-1 espacios
- Fila 2: N-2 espacios
- Fila N: 0 espacios

Es decir, los espacios previos = `N - fila`.

</details>

<details>
<summary>Pista 3 — La segunda mitad del diamante</summary>

La segunda mitad es el mismo patrón que la primera, pero de N-1 bajando a 1 (invierte el ciclo externo).

</details>

---

## ⭐ Reto Extra

Diseña un **Patrón D** propio: un patrón numérico original que requiera ciclos anidados. Dibuja el resultado esperado para N=4 y luego crea el diagrama. Compártelo con tus compañeros para que lo reproduzcan.

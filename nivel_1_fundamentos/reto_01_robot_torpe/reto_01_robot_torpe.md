# 🤖 Reto 01 — El Robot Torpe

**Nivel:** ⭐ Fundamentos | **Dificultad:** 🟢 Fácil

---

## 🎯 Historia

En el año 2087, en la fábrica de galletas más grande de Marte, trabaja **BOLT-3**, un robot de entrega que tiene un problema: no puede improvisar. BOLT-3 solo sigue instrucciones exactas, una por una. Si le dices *"avanza 3 pasos"*, avanza exactamente 3 pasos. Si le dices *"gira a la derecha"*, gira 90° exactamente.

El ingeniero de la fábrica necesita calcular, **antes de programar al robot**, cuántos **pasos totales** camina BOLT-3 en un día de trabajo, y cuántas veces **gira a la izquierda o derecha** para saber si las ruedas necesitan mantenimiento.

---

## 📋 El Problema

Dado un listado de instrucciones de BOLT-3 en un día, calcula:
1. El **total de pasos** que caminó
2. El **total de giros** que realizó (izquierda + derecha por separado)

Cada instrucción es de la forma: `AVANZA X` o `GIRA IZQUIERDA` o `GIRA DERECHA`.

---

## 🔢 Entradas

- **N**: número de instrucciones del día (entero positivo)
- **Lista de N instrucciones**, cada una es:
  - `AVANZA X` → X es un número entero positivo de pasos
  - `GIRA IZQUIERDA`
  - `GIRA DERECHA`

## 📤 Salidas

- Total de pasos caminados
- Total de giros a la izquierda
- Total de giros a la derecha

---

## 🧪 Casos de Prueba

### Caso 1
```
Entrada:
N = 5
AVANZA 10
GIRA DERECHA
AVANZA 5
GIRA IZQUIERDA
AVANZA 3

Salida esperada:
Pasos totales: 18
Giros izquierda: 1
Giros derecha: 1
```

### Caso 2
```
Entrada:
N = 3
GIRA DERECHA
GIRA DERECHA
GIRA DERECHA

Salida esperada:
Pasos totales: 0
Giros izquierda: 0
Giros derecha: 3
```

### Caso 3
```
Entrada:
N = 1
AVANZA 100

Salida esperada:
Pasos totales: 100
Giros izquierda: 0
Giros derecha: 0
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Herramientas sugeridas: [draw.io](https://draw.io), [Flowgorithm](http://flowgorithm.org), papel y lápiz.
>
> Cuando termines, guarda la imagen o PDF con el nombre `reto_01_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Tiene símbolo de INICIO y FIN
- [ ] Lee el valor de N
- [ ] Tiene un ciclo que se repite N veces
- [ ] Dentro del ciclo, distingue entre los 3 tipos de instrucción
- [ ] Acumula correctamente los contadores
- [ ] Muestra los 3 resultados al final
- [ ] Funciona con los 3 casos de prueba (ejecuta el diagrama a mano)

---

## 💻 Fase 2 — Tu Código

> ⚠️ **Solo completa esta sección DESPUÉS de validar tu diagrama con los casos de prueba.**

**Lenguaje elegido:** `________________`

```
// Escribe tu código aquí
```

---

## 💡 Pistas

<details>
<summary>Pista 1 — Estructura general</summary>

El diagrama tiene esta estructura básica:
1. Leer N
2. Inicializar contadores en 0 (pasos, girosIzq, girosDer)
3. Ciclo que se repite N veces
4. Dentro del ciclo: ¿qué tipo de instrucción es? → actualizar el contador correspondiente
5. Mostrar los 3 contadores

</details>

<details>
<summary>Pista 2 — La instrucción AVANZA</summary>

Cuando la instrucción es `AVANZA X`, debes extraer el número X y sumarlo al acumulador de pasos. El tipo de instrucción tiene dos partes: el comando y el valor.

</details>

<details>
<summary>Pista 3 — La condición del ciclo</summary>

Usa un contador `i` que empieza en 1 y termina cuando llega a N. Con cada instrucción procesada, aumenta `i` en 1.

</details>

---

## ⭐ Reto Extra

BOLT-3 ahora tiene un sensor de dirección. Además de contar pasos y giros, calcula la **posición final** del robot en una cuadrícula 2D, asumiendo que empieza en (0,0) mirando al Norte.

- AVANZA X en dirección Norte → Y aumenta X
- AVANZA X en dirección Este → X aumenta X
- etc.

¿En qué coordenada (X, Y) termina BOLT-3?
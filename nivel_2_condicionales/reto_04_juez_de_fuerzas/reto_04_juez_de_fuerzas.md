# 🏋️ Reto 04 — El Juez de Fuerzas

**Nivel:** ⭐⭐ Condicionales | **Dificultad:** 🟠 Difícil

---

## 🎯 Historia

El **Torneo InterGaláctico de Fuerzas** es la competencia más rara del universo: dos contrincantes se miden en **tres pruebas** (Fuerza bruta, Resistencia, Velocidad). El sistema de puntuación es el siguiente:

- En cada prueba, el que obtenga el puntaje más alto **gana esa prueba** y recibe **1 punto**
- Si empatan en una prueba, **ninguno** recibe el punto (es un empate y el punto se pierde)
- Al final, el que tenga **más puntos gana el torneo**
- Si ambos tienen el mismo número de puntos al final: **gana el que tuvo mayor puntaje total** (suma de las 3 pruebas)
- Si incluso el puntaje total es igual: **¡EMPATE GALÁCTICO!** (esto es rarísimo)

Adicionalmente, si un competidor gana las **3 pruebas** (barrida total), recibe el título de **"Campeón Absoluto"** aunque el otro competidor no reciba nada.

---

## 📋 El Problema

Dados los puntajes de los dos competidores en las tres pruebas, determina quién gana el torneo y con qué resultado.

---

## 🔢 Entradas

- **a1, a2, a3**: puntajes del Competidor A en las 3 pruebas
- **b1, b2, b3**: puntajes del Competidor B en las 3 pruebas

## 📤 Salidas

- Resultado de cada prueba
- Puntos finales de cada competidor
- Ganador del torneo (y el motivo si hubo desempate)
- Mención de "Campeón Absoluto" si aplica

---

## 🧪 Casos de Prueba

### Caso 1 — Ganador claro
```
Entrada: A=[80, 60, 75]  B=[70, 50, 90]

Salida esperada:
Prueba 1: A gana (80 vs 70)
Prueba 2: A gana (60 vs 50)
Prueba 3: B gana (75 vs 90)
Puntos: A=2, B=1
🏆 Ganador: Competidor A
```

### Caso 2 — Desempate por puntaje total
```
Entrada: A=[100, 50, 70]  B=[90, 60, 80]

Salida esperada:
Prueba 1: A gana (100 vs 90)
Prueba 2: B gana (50 vs 60)
Prueba 3: B gana (70 vs 80)
Puntos: A=1, B=2
🏆 Ganador: Competidor B
```

### Caso 3 — Empate en puntos, desempate por total
```
Entrada: A=[100, 50, 60]  B=[90, 80, 40]

Salida esperada:
Prueba 1: A gana (100 vs 90)
Prueba 2: B gana (50 vs 80)
Prueba 3: A gana (60 vs 40)
Puntos: A=2, B=1
🏆 Ganador: Competidor A
```

### Caso 4 — Campeón Absoluto
```
Entrada: A=[95, 88, 91]  B=[80, 70, 85]

Salida esperada:
Prueba 1: A gana (95 vs 80)
Prueba 2: A gana (88 vs 70)
Prueba 3: A gana (91 vs 85)
Puntos: A=3, B=0
🏆🥇 ¡CAMPEÓN ABSOLUTO! Competidor A ganó las 3 pruebas.
```

### Caso 5 — Empate galáctico
```
Entrada: A=[90, 80, 70]  B=[90, 80, 70]

Salida esperada:
Prueba 1: Empate (90 vs 90)
Prueba 2: Empate (80 vs 80)
Prueba 3: Empate (70 vs 70)
Puntos: A=0, B=0
Total: A=240, B=240
🌌 ¡EMPATE GALÁCTICO!
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_04_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Lee los 6 puntajes
- [ ] Para cada prueba: compara y asigna puntos (o no, si empatan)
- [ ] Suma los puntajes totales de A y B
- [ ] Compara puntos finales de A y B
- [ ] Si hay empate en puntos: compara puntaje total
- [ ] Si hay empate en total: declara empate galáctico
- [ ] Verifica si alguno ganó las 3 pruebas (Campeón Absoluto)
- [ ] Funciona con los 5 casos de prueba

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
<summary>Pista 1 — Variables de puntos</summary>

Usa variables `puntosA` y `puntosB` que empiezan en 0. Para cada prueba, si A gana, `puntosA++`. Si B gana, `puntosB++`. Si empatan, ninguno recibe nada.

</details>

<details>
<summary>Pista 2 — La condición de Campeón Absoluto</summary>

Un competidor es Campeón Absoluto si su puntaje de puntos es 3 (ganó las 3 pruebas). Puedes verificar esto después de contar los puntos.

</details>

<details>
<summary>Pista 3 — El puntaje total para desempate</summary>

`totalA = a1 + a2 + a3` y `totalB = b1 + b2 + b3`. Solo necesitas esta comparación si los puntos de A y B son iguales.

</details>

---

## ⭐ Reto Extra

El torneo ahora tiene **5 pruebas**, y los jueces quieren introducir un **multiplicador de dificultad** por prueba (un número del 1 al 3 que multiplica el puntaje de esa prueba para el ranking final). Reorganiza el diagrama para manejar los puntajes ponderados.
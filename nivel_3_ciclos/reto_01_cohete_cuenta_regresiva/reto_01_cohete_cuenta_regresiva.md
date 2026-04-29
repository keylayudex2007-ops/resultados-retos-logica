# 🚀 Reto 01 — La Cuenta Regresiva del Cohete

**Nivel:** ⭐⭐⭐ Ciclos | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

La **Agencia Espacial de Bolsillo** está lista para lanzar su cohete más pequeño del mundo. El sistema de cuenta regresiva funciona normalmente del 10 al 0, pero tiene **reglas especiales**:

- En el número **7**: el sistema grita `"¡Revisión de sistemas!"` y **pausa 2 segundos** (en el diagrama: muestra un mensaje especial adicional)
- En el número **5**: el sistema grita `"¡Punto de no retorno!"`
- En el número **3**: el sistema grita `"¡Ignición encendida!"`
- Si se detecta una **racha de 3 números pares consecutivos**, el lanzamiento se **aborta** automáticamente (rarísimo, pero el sistema debe contemplarlo)

Al llegar al **0**: `"🚀 ¡DESPEGUE!"`

---

## 📋 El Problema

Simula la cuenta regresiva desde 10 hasta 0, mostrando cada número y los mensajes especiales en los momentos indicados. Detecta si se activa el abort por 3 pares consecutivos.

---

## 🔢 Entradas

- Sin entradas externas. La cuenta empieza siempre en 10.

## 📤 Salidas

- Cada número de la cuenta regresiva
- Los mensajes especiales en los números correspondientes
- El mensaje de despegue o de abort

---

## 🧪 Casos de Prueba

### Caso 1 — Cuenta normal (sin abort)
```
Salida esperada:
10
9
8
7 — ¡Revisión de sistemas!
6
5 — ¡Punto de no retorno!
4
3 — ¡Ignición encendida!
2
1
0 — 🚀 ¡DESPEGUE!
```
*(Nota: los pares son 10, 8, 6, 4, 2 — hay consecutivos pero la lógica de abort no aplica aquí porque están separados por impares; la racha se reinicia cada vez que aparece un impar)*

---

## 🤔 Sobre la condición de abort

La racha de 3 pares **consecutivos** significa: tres números pares **uno detrás del otro** sin interrupciones de impares. En la secuencia del 10 al 0, esto no ocurre naturalmente. Pero imagina que el sistema puede **empezar desde cualquier número par alto**:

### Caso 2 — Con abort (cuenta desde 20)
```
Si la cuenta empieza en 20 y va de 2 en 2 (solo pares), el abort ocurre en el tercer número.
20, 18, 16 → ¡ABORT! Racha de 3 pares consecutivos.
```

Implementa el diagrama que puede manejar ambos casos.

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_01_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Tiene una variable `contador` que empieza en 10
- [ ] El ciclo va mientras `contador >= 0`
- [ ] Muestra el número actual en cada iteración
- [ ] Verifica si el número es 7, 5 o 3 para mensajes especiales
- [ ] Lleva un contador de pares consecutivos (se resetea si el número es impar)
- [ ] Verifica si la racha de pares llegó a 3 → abort y sale del ciclo
- [ ] Al final del ciclo normal (llega a 0): muestra DESPEGUE
- [ ] En cada iteración: `contador--`

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
<summary>Pista 1 — Racha de pares consecutivos</summary>

Usa una variable `racha_pares = 0`. Si el número actual es par, `racha_pares++`. Si es impar, `racha_pares = 0`. Si `racha_pares == 3`, activa el abort.

</details>

<details>
<summary>Pista 2 — Salir del ciclo anticipadamente</summary>

Necesitas una forma de **salir del ciclo antes de tiempo** si ocurre el abort. Muchos lenguajes tienen `break`. En el diagrama, una flecha que salta directamente al FIN del ciclo (o al bloque de abort).

</details>

---

## ⭐ Reto Extra

El ingeniero quiere que la cuenta regresiva sea **configurable**: el usuario ingresa el número inicial y el **paso** (puede contar de 1 en 1, de 2 en 2, etc.). Los mensajes especiales siguen siendo en los números 7, 5 y 3 (si la cuenta los toca). Adapta el diagrama.
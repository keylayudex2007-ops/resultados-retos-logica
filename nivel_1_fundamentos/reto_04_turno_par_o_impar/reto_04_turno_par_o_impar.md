# 🎫 Reto 04 — Turno Par o Impar

**Nivel:** ⭐ Fundamentos | **Dificultad:** 🟢 Fácil

---

## 🎯 Historia

El banco **"Sin Filas S.A."** tiene un nuevo sistema de turnos que supuestamente reduce el tiempo de espera. El sistema funciona así:

- Los turnos **pares** van a la **Ventanilla A**
- Los turnos **impares** van a la **Ventanilla B**
- Los múltiplos de 10 son turnos **VIP** y van directo a la **Ventanilla Especial**, sin importar si son pares o impares

Sin embargo, el sistema se cayó y el gerente necesita que un empleado clasifique manualmente a los clientes según su número de turno.

Además, al final del día, el gerente quiere saber cuántos clientes fueron a cada ventanilla.

---

## 📋 El Problema

Dado una serie de números de turno, determina para cada uno a qué ventanilla corresponde. Al final, muestra el conteo total de clientes por ventanilla.

---

## 🔢 Entradas

- **N**: cantidad de turnos a clasificar
- **N números de turno** (enteros positivos)

## 📤 Salidas

Para cada turno: el número y la ventanilla asignada.
Al final: totales por ventanilla (A, B, Especial).

---

## 🧪 Casos de Prueba

### Caso 1
```
Entrada:
N = 6
Turnos: 10, 3, 8, 20, 15, 7

Salida esperada:
Turno 10  → Ventanilla Especial (VIP)
Turno 3   → Ventanilla B
Turno 8   → Ventanilla A
Turno 20  → Ventanilla Especial (VIP)
Turno 15  → Ventanilla B
Turno 7   → Ventanilla B

Totales:
Ventanilla A: 1 cliente
Ventanilla B: 3 clientes
Ventanilla Especial: 2 clientes
```

### Caso 2
```
Entrada:
N = 3
Turnos: 100, 200, 300

Salida esperada:
Turno 100 → Ventanilla Especial (VIP)
Turno 200 → Ventanilla Especial (VIP)
Turno 300 → Ventanilla Especial (VIP)

Totales:
Ventanilla A: 0 clientes
Ventanilla B: 0 clientes
Ventanilla Especial: 3 clientes
```

### Caso 3
```
Entrada:
N = 4
Turnos: 1, 2, 3, 4

Salida esperada:
Turno 1 → Ventanilla B
Turno 2 → Ventanilla A
Turno 3 → Ventanilla B
Turno 4 → Ventanilla A

Totales:
Ventanilla A: 2 clientes
Ventanilla B: 2 clientes
Ventanilla Especial: 0 clientes
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_04_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Tiene símbolo de INICIO y FIN
- [ ] Lee N
- [ ] Inicializa contadores (contA, contB, contEspecial) en 0
- [ ] Tiene un ciclo que se repite N veces
- [ ] Dentro del ciclo: lee el turno y lo clasifica
- [ ] La clasificación VIP va ANTES de la clasificación par/impar
- [ ] Acumula los contadores correctamente
- [ ] Al final, muestra los totales
- [ ] Funciona con los 3 casos de prueba

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
<summary>Pista 1 — Orden de los condicionales</summary>

¡El orden importa! Si revisas primero si es par o impar, nunca llegarás a revisar si es múltiplo de 10. El múltiplo de 10 debe ser la **primera** condición que verificas (ya que es el caso más prioritario).

</details>

<details>
<summary>Pista 2 — Múltiplo de 10</summary>

Un número es múltiplo de 10 cuando `turno % 10 == 0`.

</details>

---

## ⭐ Reto Extra

El banco quiere agregar una regla nueva: si un cliente lleva **más de 30 minutos esperando** (el sistema registra el tiempo de espera en minutos junto al número de turno), se le asciende automáticamente a **Ventanilla Especial**, sin importar su turno.

Modifica el diagrama para aceptar pares `(turno, minutos_espera)` y aplicar esta regla adicional.
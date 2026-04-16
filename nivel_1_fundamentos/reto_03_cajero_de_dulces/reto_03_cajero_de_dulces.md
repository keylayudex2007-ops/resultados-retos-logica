# 🍬 Reto 03 — El Cajero de Dulces

**Nivel:** ⭐ Fundamentos | **Dificultad:** 🟢 Fácil

---

## 🎯 Historia

La señora **Guadalupe** tiene la tienda de dulces más antigua del barrio. Su caja registradora se descompuso y ahora tiene que calcular el **cambio** a mano. Pero Guadalupe tiene una regla especial: **siempre devuelve el cambio con la menor cantidad de monedas y billetes posible**.

Las denominaciones disponibles son (en pesos): **500, 200, 100, 50, 20, 10, 5, 1**.

Guadalupe necesita un algoritmo que le diga exactamente cuántos billetes y monedas de cada denominación debe dar de cambio.

---

## 📋 El Problema

Dado el precio de lo que compró el cliente y el monto que entregó, calcula el **cambio exacto en denominaciones**, usando la menor cantidad de billetes/monedas.

---

## 🔢 Entradas

- **precio**: precio del producto (en pesos, entero positivo)
- **pago**: cantidad que entregó el cliente (en pesos, entero positivo ≥ precio)

## 📤 Salidas

Para cada denominación usada (de mayor a menor), mostrar:
- Cuántos billetes/monedas de esa denominación se usan

Si el cambio es 0, mostrar "No hay cambio".

---

## 🧪 Casos de Prueba

### Caso 1
```
Entrada:
precio = 37
pago = 500

Salida esperada:
Cambio total: 463
- Billetes de 200: 2
- Billetes de 50: 1
- Monedas de 10: 1
- Monedas de 1: 3
```

### Caso 2
```
Entrada:
precio = 100
pago = 100

Salida esperada:
No hay cambio.
```

### Caso 3
```
Entrada:
precio = 7
pago = 20

Salida esperada:
Cambio total: 13
- Monedas de 10: 1
- Monedas de 1: 3
```

### Caso 4
```
Entrada:
precio = 1
pago = 501

Salida esperada:
Cambio total: 500
- Billetes de 500: 1
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_03_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Tiene símbolo de INICIO y FIN
- [ ] Lee precio y pago
- [ ] Calcula el cambio (pago - precio)
- [ ] Verifica si el cambio es 0
- [ ] Para cada denominación (en orden descendente): calcula cuántas piezas caben y resta el monto
- [ ] Solo muestra las denominaciones que se usaron (cantidad > 0)
- [ ] Funciona con los 4 casos de prueba

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
<summary>Pista 1 — El algoritmo del cambio</summary>

Este problema usa el **algoritmo codicioso (greedy)**:
1. Siempre toma la denominación más grande posible
2. Calcula cuántas piezas de esa denominación caben: `piezas = cambio ÷ denominación`
3. Resta lo que cubre: `cambio = cambio - (piezas × denominación)`
4. Pasa a la siguiente denominación y repite

</details>

<details>
<summary>Pista 2 — Estructurar las denominaciones</summary>

Puedes guardar las denominaciones en una lista ordenada de mayor a menor: [500, 200, 100, 50, 20, 10, 5, 1], y luego recorrerla con un ciclo.

</details>

---

## ⭐ Reto Extra

El hijo de Guadalupe, **Miguelito**, quiere saber: ¿cuál es el monto de cambio más difícil de dar? Es decir, ¿qué monto entre 1 y 999 requiere la **mayor cantidad total de piezas** (billetes + monedas)?

Diseña el diagrama para encontrarlo automáticamente.
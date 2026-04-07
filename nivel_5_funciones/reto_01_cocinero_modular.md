# 👨‍🍳 Reto 01 — El Cocinero Modular

**Nivel:** ⭐⭐⭐⭐⭐ Funciones | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

El chef **Módulo Ramírez** es famoso por su método de cocina: nunca repite instrucciones. Si algo se hace más de una vez en la cocina, lo convierte en un "módulo" que puede reutilizarse.

Para preparar su **Paella Galáctica**, el proceso tiene muchos sub-pasos que se repiten (como "saltear", "hervir", "sazonar"). El chef quiere documentar su receta como un conjunto de **funciones reutilizables** que se llaman entre sí.

---

## 📋 El Problema

Diseña el algoritmo de la Paella Galáctica usando **funciones**. Cada operación de cocina es una función separada. El programa principal solo "llama" a estas funciones en el orden correcto.

### Las Operaciones (Funciones a Diseñar):

| Función | Parámetros | Retorna | Descripción |
|---------|-----------|---------|-------------|
| `calentar_aceite(temp)` | temperatura deseada | tiempo_calentamiento | Sube la temperatura hasta el nivel indicado |
| `saltear(ingrediente, minutos)` | nombre, tiempo | `listo`/`quemado` | Saltea un ingrediente; si minutos > 8 → quemado |
| `hervir(liquido, litros)` | nombre, cantidad | tiempo_ebullicion | Calcula el tiempo para hervir (2 min por litro) |
| `sazonar(plato, sal, pimenta)` | nombre del plato, gramos de sal, gramos de pimienta | descripcion_sabor | Si sal > 5g → "salado"; si < 1g → "insípido"; si no → "perfecto" |
| `reposar(tiempo)` | minutos de reposo | `listo` | El plato reposa ese tiempo |
| `servir(plato, porciones)` | nombre y porciones | descripcion_presentacion | Genera el texto final de presentación |

### La Receta (Programa Principal):
```
1. calentar_aceite(180)
2. saltear("cebolla", 5)
3. saltear("ajo", 2)
4. saltear("tomate", 4)
5. hervir("caldo_de_mariscos", 3)
6. Agregar arroz y sazonar("paella_base", 4, 2)
7. reposar(10)
8. servir("Paella Galáctica", 4)
```

---

## 🔢 Entradas

- Los parámetros de cada llamada a función (definidos en la receta)

## 📤 Salidas

- El resultado de cada función conforme se ejecuta la receta
- Al final: un resumen del platillo terminado

---

## 🧪 Caso de Prueba

```
Salida esperada al ejecutar la receta:

🔥 Calentando aceite a 180°C... [3 minutos]
🥘 Salteando cebolla (5 min)... → ✅ Listo
🥘 Salteando ajo (2 min)... → ✅ Listo
🥘 Salteando tomate (4 min)... → ✅ Listo
💧 Hirviendo caldo_de_mariscos (3 litros)... [6 minutos]
🧂 Sazonando paella_base: 4g sal, 2g pimienta → 👌 Sabor perfecto
😴 Reposando 10 minutos...
🍽️ Sirviendo Paella Galáctica para 4 porciones.

=== RESUMEN ===
Tiempo total de cocción: 30 minutos
Sabor: perfecto
Estado: listo para servir
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Dibuja **un sub-diagrama por cada función** + el diagrama principal.  
> Guarda con `reto_01_diagramas.[png|pdf]`.

**Lista de verificación:**
- [ ] Diagrama del programa principal (muestra las llamadas a funciones como rectángulos con bordes dobles)
- [ ] Sub-diagrama de `calentar_aceite` (recibe temp, calcula tiempo, retorna tiempo)
- [ ] Sub-diagrama de `saltear` (recibe ingrediente y minutos, decide si quemado o listo)
- [ ] Sub-diagrama de `hervir` (calcula tiempo = litros × 2)
- [ ] Sub-diagrama de `sazonar` (decide el sabor según la sal)
- [ ] Sub-diagrama de `servir` (genera texto de presentación)
- [ ] Cada sub-diagrama tiene INICIO y FIN y muestra el valor de retorno

---

## 💻 Fase 2 — Tu Código

> ⚠️ **Solo completa esta sección DESPUÉS de validar tu diagrama.**

**Lenguaje elegido:** `________________`

```
// Escribe tu código aquí
// Define cada función primero, luego el programa principal
```

---

## 💡 Pistas

<details>
<summary>Pista 1 — Estructura de una función en diagrama</summary>

En un diagrama de flujo, una función se representa como un sub-diagrama con:
- Un INICIO que muestra los parámetros que recibe
- El proceso interno
- Un símbolo de RETORNO con el valor que devuelve
En el diagrama principal, la llamada a la función es un rectángulo con líneas dobles en los bordes verticales.

</details>

<details>
<summary>Pista 2 — El tiempo total</summary>

El programa principal debe acumular el tiempo de cada función en una variable `tiempo_total`. Las funciones que toman tiempo lo retornan; el programa principal lo suma.

</details>

---

## ⭐ Reto Extra

El chef quiere hacer una **versión vegana** de la paella. Crea una función `adaptar_a_vegano(ingrediente)` que, dado un ingrediente, devuelva su sustituto vegano (mariscos → tofu, caldo de pollo → caldo de verduras, etc.). Modifica el programa principal para usar esta función antes de saltear.

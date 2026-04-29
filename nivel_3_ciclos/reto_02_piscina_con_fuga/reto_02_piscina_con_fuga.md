# 🏊 Reto 02 — La Piscina con Fuga

**Nivel:** ⭐⭐⭐ Ciclos | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

En el hotel **"Agua No Llega"**, la piscina olímpica tiene un serio problema: **tiene una fuga**. El encargado, don **Heliodoro**, llena la piscina con una manguera pero el agua se escapa por un hoyo.

Los datos del problema:
- La piscina tiene capacidad de **50,000 litros**
- La manguera vierte **500 litros por minuto**
- La fuga pierde **80 litros por minuto**
- La piscina empieza **vacía** (0 litros)
- ¡Pero hay más! Cada **10 minutos**, Heliodoro revisa y si el nivel bajó respecto al minuto anterior, sube el flujo de la manguera en **50 litros extra por minuto** (acumulativo)

Don Heliodoro quiere saber:
1. ¿Cuántos **minutos** tardará en llenarse la piscina?
2. ¿Cuántos litros tiene la piscina cada 10 minutos?
3. ¿Cuántas veces tuvo que **aumentar el flujo** de la manguera?

---

## 📋 El Problema

Simula minuto a minuto el llenado de la piscina con la fuga y los aumentos de flujo periódicos. Para cuando llegue a 50,000 litros.

---

## 🔢 Entradas

- Sin entradas (los valores son fijos en el enunciado)
- *Opcional/Reto: hacer los valores configurables*

## 📤 Salidas

- Cada 10 minutos: el nivel de agua actual
- Al finalizar: minutos totales, nivel final, cantidad de aumentos de flujo

---

## 🧪 Caso de Prueba

```
Salida esperada (fragmento):
Minuto  0: 0 litros
Minuto 10: 4,200 litros  (flujo neto: 420 L/min)
Minuto 20: 8,400 litros
...
Minuto X: 50,000+ litros

Resumen:
- Tardó N minutos en llenarse
- Flujo final de la manguera: Y litros/min
- Aumentos de flujo realizados: Z veces
```

*(Nota: calcula manualmente los primeros pasos con el diagrama para verificar)*

**Verificación manual:**
- Flujo inicial = 500 - 80 = 420 L/min netos
- Minuto 10: 420 × 10 = 4,200 litros ✓
- En el minuto 10, Heliodoro revisa: ¿bajó el nivel? No (está subiendo). No aumenta flujo.
- Minuto 20: 420 × 20 = 8,400 litros ✓

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_02_diagrama.[png|pdf]` en esta carpeta.

**Variables a usar:**
- `litros` ← nivel actual de agua (empieza en 0)
- `minutos` ← contador de tiempo
- `flujo_manguera` ← litros por minuto que entra (empieza en 500)
- `fuga` ← litros por minuto que sale (constante: 80)
- `litros_anterior` ← nivel del minuto anterior (para comparar en revisión)
- `aumentos` ← conteo de veces que aumentó el flujo

**Lista de verificación del diagrama:**
- [ ] Inicializa todas las variables correctamente
- [ ] El ciclo continúa mientras `litros < 50000`
- [ ] En cada iteración: calcula los litros ganados y perdidos
- [ ] Actualiza el nivel de litros
- [ ] Incrementa el contador de minutos
- [ ] Cada 10 minutos: verifica si subir el flujo y muestra el nivel
- [ ] Al final: muestra el resumen
- [ ] Verifica manualmente los primeros 20 minutos con el diagrama

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
<summary>Pista 1 — Flujo neto</summary>

En cada minuto, los litros que entran a la piscina son:
`litros += flujo_manguera - fuga`

</details>

<details>
<summary>Pista 2 — La revisión de Heliodoro</summary>

La revisión ocurre cuando `minutos % 10 == 0`. En ese momento, guarda `litros_anterior` antes de la iteración para comparar si subió o bajó. Si bajó (`litros < litros_anterior`), suma 50 al `flujo_manguera`.

</details>

<details>
<summary>Pista 3 — Condición de parada</summary>

El ciclo debe parar cuando `litros >= 50000`. Ten cuidado de no pasarte: ajusta el nivel al exactamente 50,000 si lo superas.

</details>

---

## ⭐ Reto Extra

El hotel tiene **3 piscinas** con capacidades distintas (25,000 / 50,000 / 100,000 litros) y las tres se llenan simultáneamente con la misma manguera que **reparte el flujo equitativamente**. ¿Cuánto tarda en llenarse cada una? Simúlalas en paralelo (en el mismo ciclo).

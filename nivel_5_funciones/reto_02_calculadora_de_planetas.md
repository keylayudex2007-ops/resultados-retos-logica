# 🪐 Reto 02 — La Calculadora de Planetas

**Nivel:** ⭐⭐⭐⭐⭐ Funciones | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

La astronauta **Valentina Cosmo** está preparando su viaje interplanetario. Antes de partir, quiere saber cuánto pesaría en cada planeta del sistema solar. Pero no solo eso: también quiere saber cuántos **"saltos"** podría dar (cada salto en la Tierra = 1 metro de altura) y cuánto tardaría en **caer desde 10 metros de altura** en cada planeta.

La gravedad de cada planeta (en m/s²):
| Planeta | Gravedad |
|---------|----------|
| Mercurio | 3.7 |
| Venus | 8.87 |
| Tierra | 9.81 |
| Marte | 3.72 |
| Júpiter | 24.79 |
| Saturno | 10.44 |
| Urano | 8.87 |
| Neptuno | 11.15 |
| Luna | 1.62 |

---

## 📋 El Problema

Diseña un sistema de funciones que, dado el peso en la Tierra de la astronauta, calcule para cualquier planeta:
1. **Peso** en ese planeta
2. **Altura del salto** (proporcional: si en Tierra saltas 1m, en Marte saltas más)
3. **Tiempo de caída** desde 10 metros: `t = √(2h/g)` donde h=10

---

## 🔢 Funciones a Diseñar

| Función | Parámetros | Retorna |
|---------|-----------|---------|
| `obtener_gravedad(planeta)` | nombre del planeta | gravedad en m/s² |
| `calcular_peso(masa_kg, gravedad)` | masa y gravedad | peso en Newtons |
| `calcular_salto(gravedad_planeta)` | gravedad del planeta | altura del salto en metros |
| `calcular_caida(gravedad)` | gravedad | tiempo de caída desde 10m (segundos) |
| `reporte_planeta(nombre, masa_kg)` | nombre, masa | imprime el reporte completo del planeta |

**Nota:** La masa en kg se calcula como `masa = peso_tierra / 9.81`

---

## 🧪 Caso de Prueba

```
Entrada:
Peso en la Tierra: 70 kg-fuerza (686.7 N)
Masa: 70 kg

reporte_planeta("Marte", 70):

=== INFORME PLANETA: MARTE ===
Gravedad: 3.72 m/s²
Peso en Marte: 260.4 N (26.5 kg-fuerza)
Altura de salto: 2.64 m (vs 1m en Tierra)
Tiempo de caída 10m: 2.32 segundos
```

```
reporte_planeta("Júpiter", 70):

=== INFORME PLANETA: JÚPITER ===
Gravedad: 24.79 m/s²
Peso en Júpiter: 1735.3 N (176.9 kg-fuerza)
Altura de salto: 0.40 m (vs 1m en Tierra)
Tiempo de caída 10m: 0.90 segundos
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Dibuja un sub-diagrama por cada función y el programa principal.  
> Guarda con `reto_02_diagramas.[png|pdf]`.

**Lista de verificación:**
- [ ] Sub-diagrama de `obtener_gravedad`: usa comparaciones para devolver el valor según el nombre del planeta
- [ ] Sub-diagrama de `calcular_peso`: fórmula simple (masa × gravedad)
- [ ] Sub-diagrama de `calcular_salto`: `salto = gravedad_tierra / gravedad_planeta` (proporción inversa)
- [ ] Sub-diagrama de `calcular_caida`: `t = raiz(2 × 10 / gravedad)`
- [ ] Sub-diagrama de `reporte_planeta`: llama a las otras 4 funciones y muestra el informe
- [ ] Programa principal: lee el peso, calcula la masa, y llama a `reporte_planeta` para cada planeta

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
<summary>Pista 1 — La altura del salto</summary>

Si en la Tierra con gravedad 9.81 saltas 1 metro, en un planeta con gravedad G saltas:
`salto = 1 × (9.81 / G)`
Menor gravedad → mayor salto. Mayor gravedad → menor salto.

</details>

<details>
<summary>Pista 2 — La raíz cuadrada</summary>

Para `√(2h/g)`, necesitas la función de raíz cuadrada de tu lenguaje: `sqrt()` en Python/JS/C, `Math.sqrt()` en Java, etc. En el diagrama, puedes escribirlo como `[t = √(20/g)]`.

</details>

---

## ⭐ Reto Extra

Valentina quiere saber en qué planeta podría **correr más rápido**. Crea una función `velocidad_maxima(gravedad)` que modele que a menor gravedad, el coeficiente de rozamiento con el suelo es menor, permitiendo más velocidad (fórmula simplificada: `v_max = 40 × (9.81/g)` km/h donde 40 km/h es la máxima humana en Tierra). ¿Dónde corre más rápido?

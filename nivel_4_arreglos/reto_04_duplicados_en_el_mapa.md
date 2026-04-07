# 🗺️ Reto 04 — Duplicados en el Mapa

**Nivel:** ⭐⭐⭐⭐ Arreglos | **Dificultad:** 🟠 Difícil

---

## 🎯 Historia

El cartógrafo **Rodrigo Puntos** dibujó un mapa del tesoro con coordenadas de lugares importantes. Por un error de su pluma de tinta de pulpo, **algunas coordenadas aparecen repetidas** en el mapa. El problema: si el marinero sigue cada coordenada sin verificar duplicados, dedicará el doble o triple de tiempo buscando en el mismo lugar.

Rodrigo necesita un algoritmo que:
1. **Identifique** todas las coordenadas duplicadas
2. **Limpie** el mapa quitando los duplicados
3. **Encuentre** las coordenadas que forman una **línea recta** (horizontal o vertical)
4. **Calcule** la distancia total del recorrido si se visitan todas las coordenadas únicas en orden de aparición

La distancia entre dos puntos (x1,y1) y (x2,y2) es: `|x2-x1| + |y2-y1|` (distancia Manhattan).

---

## 📋 El Problema

Dado un listado de coordenadas (pares x,y), limpia duplicados, identifica patrones y calcula distancias.

---

## 🔢 Entradas

- **N**: número de coordenadas en el mapa (pueden haber duplicados)
- **N pares (x, y)**: coordenadas de los puntos

## 📤 Salidas

1. Lista de coordenadas duplicadas (las que aparecen más de una vez)
2. Lista limpia (sin duplicados, en orden de primera aparición)
3. Grupos de coordenadas en línea recta
4. Distancia total del recorrido de la lista limpia

---

## 🧪 Casos de Prueba

### Caso 1
```
Entrada:
N = 8
(2,3) (5,1) (2,3) (8,4) (5,1) (5,7) (1,3) (5,4)

Salida esperada:
Duplicados encontrados:
- (2,3) aparece 2 veces
- (5,1) aparece 2 veces

Mapa limpio (6 coordenadas únicas):
(2,3) → (5,1) → (8,4) → (5,7) → (1,3) → (5,4)

Coordenadas en línea vertical (misma X=5):
(5,1), (5,7), (5,4)

Coordenadas en línea horizontal (misma Y=3):
(2,3), (1,3)

Distancia total del recorrido:
(2,3)→(5,1): |5-2|+|1-3| = 3+2 = 5
(5,1)→(8,4): |8-5|+|4-1| = 3+3 = 6
... [continúa]
Distancia total: XX km
```

### Caso 2 — Sin duplicados
```
Entrada:
N = 3
(1,1) (2,2) (3,3)

Salida:
No hay duplicados.
Mapa limpio: (1,1) → (2,2) → (3,3)
Sin alineaciones horizontal/vertical.
Distancia total: |2-1|+|2-1| + |3-2|+|3-2| = 2 + 2 = 4
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda con el nombre `reto_04_diagrama.[png|pdf]`.

**Sub-diagramas:**
1. "Detectar y contar duplicados"
2. "Construir lista limpia manteniendo orden"
3. "Encontrar alineaciones"
4. "Calcular distancia total"

**Lista de verificación:**
- [ ] Lee N coordenadas en dos arreglos: xs[] y ys[]
- [ ] Para detectar duplicados: para cada coordenada, busca si aparece en el resto
- [ ] Construye la lista limpia: solo agrega si no ha aparecido antes
- [ ] Para las alineaciones: agrupa coordenadas con el mismo x (vertical) o el mismo y (horizontal)
- [ ] Calcula la distancia acumulada entre coordenadas consecutivas de la lista limpia
- [ ] Muestra todo el reporte

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
<summary>Pista 1 — Comparar coordenadas</summary>

Dos coordenadas son iguales si tienen el mismo x Y el mismo y. En el diagrama, el rombo de comparación debe verificar ambas condiciones con AND.

</details>

<details>
<summary>Pista 2 — Lista limpia manteniendo orden</summary>

Crea una segunda lista vacía. Para cada coordenada original, revisa si ya está en la segunda lista. Si NO está → agrégala. Si SÍ está → ignórala.

</details>

<details>
<summary>Pista 3 — Alineaciones</summary>

Para encontrar alineaciones, recorre las coordenadas y agrupa las que tienen la misma X (o la misma Y). Si un grupo tiene 3 o más puntos, es una "línea relevante".

</details>

---

## ⭐ Reto Extra

El cartógrafo quiere ordenar el recorrido para **minimizar la distancia total**: en lugar de visitar las coordenadas en orden de aparición, encuentra el orden que resulte en el recorrido más corto (empieza siempre desde (0,0)). Diseña el diagrama del algoritmo greedy (siempre ve al punto más cercano).

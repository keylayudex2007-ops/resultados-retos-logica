# 🌍 Reto 03 — El Simulador de Ecosistema

**Nivel:** 💀 Desafío Final | **Dificultad:** 💀 Extremo

---

## 🎯 Historia

El biólogo **Dr. Chaos Darwin** necesita simular la dinámica de un ecosistema con **depredadores y presas** durante **N ciclos** (generaciones). Este modelo simplificado (basado en el modelo Lotka-Volterra) permite estudiar cómo las poblaciones se afectan mutuamente.

El ecosistema tiene **3 tipos de seres** en un mapa de cuadrícula:
- 🐇 **Conejos** (presas): se reproducen rápidamente, mueren si un lobo los alcanza o si no hay hierba
- 🐺 **Lobos** (depredadores): comen conejos, mueren de hambre si no comen en K ciclos
- 🌿 **Hierba** (recurso): crece en celdas vacías, los conejos la consumen

---

## 📋 Las Reglas del Ecosistema

### Reglas de la Hierba 🌿
- En cada ciclo, cada celda **vacía** tiene 30% de probabilidad de crecer hierba
- La hierba no se mueve
- Una celda con hierba puede ser consumida por un conejo

### Reglas de los Conejos 🐇
- En cada ciclo, cada conejo se **mueve** a una celda adyacente aleatoria
  - Prefiere las celdas con hierba (si hay, va a una con hierba)
  - Si no hay hierba adyacente, va a una celda vacía (si hay)
  - Si todas las celdas adyacentes tienen lobos o no hay espacio: **no se mueve**
- Si el conejo llega a una celda con hierba: **come** (gana 2 puntos de energía)
- Si un conejo tiene **≥ 4 puntos de energía**, se **reproduce**: crea un nuevo conejo en una celda adyacente vacía y gasta 2 puntos de energía
- Si un conejo tiene **0 puntos de energía**: **muere** (la celda queda vacía)
- Cada ciclo un conejo pierde 1 punto de energía
- Los conejos inician con **3 puntos de energía**

### Reglas de los Lobos 🐺
- En cada ciclo, cada lobo se **mueve** hacia el conejo más cercano (si hay uno en un radio de 2 celdas)
  - Si no hay conejo cercano: se mueve aleatoriamente
- Si el lobo cae en una celda con un conejo: **caza** (el conejo muere, el lobo gana 5 puntos de energía)
- Si un lobo tiene **≥ 8 puntos de energía**, se **reproduce**: crea un nuevo lobo en celda adyacente vacía y gasta 4 puntos
- Si un lobo lleva **5 ciclos sin comer** (0 puntos de energía): **muere**
- Cada ciclo un lobo pierde 1 punto de energía
- Los lobos inician con **5 puntos de energía**

### Fin de la Simulación
La simulación termina cuando:
- Se completan los N ciclos
- Los lobos se extinguen (solo quedan conejos)
- Los conejos se extinguen (solo quedan lobos que eventualmente mueren)
- Todo el ecosistema colapsa (todo muerto)

---

## 📋 Los Módulos del Sistema

### Módulo 1: Inicialización
- Crea el mapa de cuadrícula M×M
- Coloca aleatoriamente (o en posiciones dadas) los conejos, lobos y hierba iniciales
- Muestra el estado inicial

### Módulo 2: Ciclo de Hierba
- Para cada celda vacía: con probabilidad 30%, coloca hierba
- (En simulaciones deterministas: usa un patrón fijo en lugar de aleatoriedad)

### Módulo 3: Ciclo de Conejos
- Para cada conejo (en orden): ejecuta su turno siguiendo las reglas
- Después de mover: verifica reproducción y muerte

### Módulo 4: Ciclo de Lobos
- Para cada lobo (en orden): ejecuta su turno siguiendo las reglas
- Después de mover: verifica reproducción y muerte

### Módulo 5: Visualización y Estadísticas
- Muestra el mapa del ecosistema cada ciclo (o cada N ciclos)
- Gráfica de población: conejos y lobos por ciclo
- Estadísticas al final: máxima población de cada especie, ciclo del colapso (si hubo)

---

## 🧪 Caso de Prueba

### Configuración inicial:
```
Mapa: 6×6
Conejos: 5 (en posiciones aleatorias con energía 3)
Lobos: 2 (en posiciones aleatorias con energía 5)
Hierba: 8 celdas con hierba aleatoriamente
N ciclos: 20
```

### Estado inicial (ejemplo):
```
Mapa 6×6:
. 🌿 . 🐇 . .
. . 🐺 . 🌿 .
🐇 . . . . 🐇
. 🌿 . . 🌿 .
. . 🐇 🐺 . .
. 🌿 . . 🐇 .

Conejos: 5 | Lobos: 2 | Hierba: 6 celdas
```

### Después del Ciclo 1:
```
[Ciclo 1 — Hierba]:
  3 celdas vacías nuevas con hierba (30% de ~20 vacías ≈ 6, pero se usan condiciones deterministas)

[Ciclo 1 — Conejos]:
  Conejo en (0,3): hay hierba en (0,1) adyacente? No. Se mueve a (1,3). No come. Energía: 3→2
  Conejo en (2,0): busca hierba... (3,1) está a distancia 2, no adyacente. Se mueve a (3,0). No come. E: 3→2
  [...]

[Ciclo 1 — Lobos]:
  Lobo en (1,2): conejo más cercano en (2,0) a distancia 2 (radio OK). Se mueve hacia (2,0)... llega a (2,1). No caza. E: 5→4
  [...]

Mapa después del Ciclo 1:
[mapa actualizado]
Conejos: 5 | Lobos: 2
```

### Gráfica de Población (al final de 20 ciclos):
```
Ciclo  | Conejos | Lobos
-------|---------|------
0      |    5    |   2
1      |    5    |   2
2      |    6    |   2   ← reproducción de un conejo
3      |    6    |   3   ← reproducción de un lobo
...
10     |    3    |   4   ← conejos disminuyen
15     |    8    |   2   ← conejos se recuperan, lobos mueren de hambre
20     |   12    |   1   ← boom de conejos sin depredadores
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Este es el reto más complejo del repositorio entero. Empieza por la arquitectura.**
>
> Guarda con: `reto_03_arquitectura.png`, `reto_03_ciclo_conejo.png`, `reto_03_ciclo_lobo.png`, `reto_03_main.png`

### Arquitectura General

```
INICIO
  ↓
[Módulo 1: Inicializar mapa, entidades y estadísticas]
  ↓
[Mostrar estado inicial]
  ↓
ciclo = 1
  ↓
◇ ciclo ≤ N Y hay_conejos Y hay_lobos?
  |                |
  Sí               No → [Módulo 5: Reporte Final]
  ↓
[Módulo 2: Ciclo de Hierba]
  ↓
[Módulo 3: Ciclo de Conejos]
  ↓
[Módulo 4: Ciclo de Lobos]
  ↓
[Registrar estadísticas del ciclo]
  ↓
[Mostrar mapa cada 5 ciclos]
  ↓
ciclo = ciclo + 1 → (regresa a ◇)
```

### Diagrama del Turno de un Conejo

```
[Conejo en posición (r,c)]
  ↓
[Buscar celdas adyacentes disponibles (Arriba, Abajo, Izq, Der)]
  ↓
◇ ¿Hay celda con hierba adyacente?
  |                |
  Sí               No
  ↓                ↓
[Mover a celda  ◇ ¿Hay celda vacía adyacente?
  con hierba]     |           |
[Consumir         Sí          No
 hierba]          ↓           ↓
[Energía += 2]  [Mover a   [No se mueve]
  ↓              celda vacía]   ↓
[Energía -= 1]     ↓         [Energía -= 1]
  ↓             [Energía -= 1]
◇ Energía >= 4?
  |       |
  Sí      No
  ↓       ↓
[Reproducir]  ◇ Energía == 0?
[Energía -= 2]   |       |
                 Sí      No → (siguiente conejo)
                 ↓
              [Conejo muere - eliminar del mapa]
```

**Lista de verificación completa:**
- [ ] Estructura de datos para el mapa (qué hay en cada celda)
- [ ] Listas separadas de todos los conejos y todos los lobos (con sus posiciones y energías)
- [ ] Módulo de hierba: recorre celdas vacías y aplica la probabilidad (o regla determinista)
- [ ] Turno de cada conejo: busca hierba adyacente, mueve, come, verifica reproducción y muerte
- [ ] Turno de cada lobo: busca conejo a radio ≤2, se mueve hacia él (un paso), come si puede, verifica reproducción y muerte
- [ ] Al mover: verifica que la celda destino existe y está disponible
- [ ] Estadísticas: lleva la cuenta de población cada ciclo
- [ ] Condición de terminación: sin conejos O sin lobos O ciclos completos

---

## 💻 Fase 2 — Tu Código

> ⚠️ **Solo completa esta sección DESPUÉS de validar todos los diagramas.**

**Lenguaje elegido:** `________________`

```
// Estructura de datos sugerida:
// mapa[M][M] = 0 (vacío) | 1 (hierba) | 2 (conejo) | 3 (lobo)
// conejos[] = lista de objetos {fila, col, energia}
// lobos[] = lista de objetos {fila, col, energia, ciclos_sin_comer}

// Escribe tu código aquí
```

---

## 💡 Pistas

<details>
<summary>Pista 1 — Ordenar el turno sin conflictos</summary>

Cuando múltiples conejos se mueven hacia la misma celda, puede haber conflictos. Una solución simple: procesa los conejos uno por uno. Cuando un conejo se mueve, actualiza el mapa inmediatamente. Los conejos que se procesarán después "ven" el mapa ya actualizado.

</details>

<details>
<summary>Pista 2 — El lobo busca el conejo más cercano</summary>

Para encontrar el conejo más cercano dentro de un radio de 2: calcula la distancia Manhattan (|Δfila| + |Δcol|) a cada conejo. El lobo se mueve hacia el más cercano (distancia menor) un solo paso en la dirección correcta (primero intenta reducir la diferencia de fila, luego de columna).

</details>

<details>
<summary>Pista 3 — Probabilidad determinista</summary>

Si no tienes función de números aleatorios, simula la "aleatoriedad" con un patrón: el ciclo 1 activa hierbas en posiciones con índice par, el ciclo 2 en posiciones con índice impar, etc. Esto hace la simulación **reproducible** y más fácil de depurar.

</details>

<details>
<summary>Pista 4 — Cuidado al eliminar entidades</summary>

Cuando un conejo o lobo muere, NO lo elimines inmediatamente de la lista mientras estás iterando. Márcalo como "muerto" y elimina todos los marcados al final del ciclo. Esto evita errores de índices al recorrer las listas.

</details>

---

## ⭐ Reto Extra — El Tercer Nivel Trófico

Agrega una tercera especie: **🦁 Leones** que cazan lobos (pero no conejos). Los leones tienen sus propias reglas análogas pero con mayor energía (10 inicial, pierden 1/ciclo, necesitan cazar cada 8 ciclos o mueren). ¿Cómo cambia la dinámica del ecosistema con una cadena alimenticia de 3 niveles?

---

## 🏁 Has Completado el Repositorio

Si llegaste hasta aquí y resolviste el Simulador de Ecosistema, has demostrado dominar:

- ✅ Pensamiento secuencial y algorítmico
- ✅ Toma de decisiones complejas con múltiples condiciones
- ✅ Ciclos e iteraciones de todo tipo
- ✅ Gestión de estructuras de datos (listas, matrices)
- ✅ Diseño modular con funciones
- ✅ Algoritmos avanzados (backtracking, búsqueda, simulación)
- ✅ Diseño de sistemas completos e integrados
- ✅ **Diagramas de flujo** para todo lo anterior

**El siguiente paso**: Aprende estructuras de datos avanzadas (árboles, grafos, pilas, colas), algoritmos de ordenamiento y búsqueda, y comienza a estudiar complejidad algorítmica (Big O).

*🎓 Bienvenido al mundo real del desarrollo de software.*

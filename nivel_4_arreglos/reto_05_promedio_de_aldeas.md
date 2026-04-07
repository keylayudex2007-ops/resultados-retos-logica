# 🌡️ Reto 05 — El Promedio de las Aldeas

**Nivel:** ⭐⭐⭐⭐ Arreglos | **Dificultad:** 🔴 Muy Difícil

---

## 🎯 Historia

El **Sistema Climático de las Montañas Nebulosas** monitorea la temperatura de **K aldeas** durante **7 días** (una semana completa). El meteorólogo jefe, **don Meteo**, necesita un análisis completo para emitir alertas de calor o frío a tiempo.

El sistema debe calcular:
1. **Temperatura promedio** de cada aldea (7 días)
2. **Temperatura promedio** de toda la región (todos los días, todas las aldeas)
3. La aldea con **temperatura más extrema** (mayor diferencia entre su max y su min)
4. **Días de alerta**: días donde el promedio de TODAS las aldeas supere 35°C (alerta calor) o baje de 5°C (alerta frío)
5. La **tendencia** de cada aldea: ¿las temperaturas van subiendo, bajando o son variables?

Una aldea tiene tendencia **"subiendo"** si cada día es mayor o igual al anterior.  
Tiene tendencia **"bajando"** si cada día es menor o igual al anterior.  
Si no, es **"variable"**.

---

## 📋 El Problema

Dado un arreglo 2D de temperaturas (K aldeas × 7 días), calcular todas las métricas.

---

## 🔢 Entradas

- **K**: número de aldeas
- **K × 7 temperaturas** en grados Celsius (pueden ser decimales)

## 📤 Salidas

- Tabla con promedios por aldea
- Promedio regional
- Aldea más extrema (con max y min)
- Lista de días de alerta
- Tendencia de cada aldea

---

## 🧪 Caso de Prueba

### Entrada (3 aldeas, 7 días):
```
Aldea Aurora:     [20, 22, 24, 26, 28, 30, 32]
Aldea Bruma:      [38, 39, 37, 40, 38, 36, 41]
Aldea Cumbre:     [4, 6, 3, 5, 2, 8, 1]
```

### Salida esperada:
```
=== ANÁLISIS CLIMÁTICO SEMANA 1 ===

Promedios por aldea:
- Aldea Aurora:   25.1°C  | Tendencia: Subiendo ↑
- Aldea Bruma:    38.4°C  | Tendencia: Variable ~
- Aldea Cumbre:   4.1°C   | Tendencia: Variable ~

Promedio regional: 22.6°C

Aldea más extrema: Aldea Cumbre
  Max: 8°C (día 6) | Min: 1°C (día 7) | Rango: 7°C

⚠️ ALERTAS:
- Días 1, 2, 3, 4, 5, 6, 7: ALERTA CALOR (Bruma supera 35°C individualmente)

(Nota: el promedio regional no supera 35°C, pero considera si quieres alertar por aldea individual)

❄️ Días cercanos a alerta de frío (por aldea Cumbre):
- Día 5: Cumbre registra 2°C
- Día 7: Cumbre registra 1°C
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Este problema usa una **matriz 2D**. Guarda con `reto_05_diagrama.[png|pdf]`.

**Estructura de datos:**
```
temperaturas[K][7]  ← matriz K filas (aldeas) × 7 columnas (días)
```

**Sub-diagramas:**
1. "Calcular promedio de una aldea" (recorre la fila i)
2. "Calcular promedio regional" (recorre toda la matriz)
3. "Encontrar max y min de una aldea"
4. "Determinar tendencia de una aldea"
5. "Verificar alertas por día" (recorre columna j)

**Lista de verificación:**
- [ ] Lee K y la matriz de temperaturas con doble ciclo
- [ ] Para cada aldea (ciclo externo): calcula promedio, max, min, tendencia
- [ ] Calcula el promedio regional (promedio de todos los valores)
- [ ] Identifica la aldea más extrema (mayor rango max-min)
- [ ] Para cada día (ciclo externo sobre los 7 días): calcula promedio diario y verifica alertas
- [ ] Muestra el reporte completo

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
<summary>Pista 1 — La matriz 2D</summary>

Piensa en la matriz como una "tabla": filas son aldeas, columnas son días. Para recorrer una aldea específica: `para j = 0 hasta 6: accede a temperaturas[aldea][j]`. Para recorrer un día específico: `para i = 0 hasta K-1: accede a temperaturas[i][dia]`.

</details>

<details>
<summary>Pista 2 — Tendencia "subiendo"</summary>

Una aldea va "subiendo" si `t[1] >= t[0] AND t[2] >= t[1] AND ... AND t[6] >= t[5]`. En el diagrama: un ciclo que verifica cada par consecutivo; si encuentra algún par donde baja, la tendencia es "variable" y puede salir del ciclo.

</details>

---

## ⭐ Reto Extra

Agrega un sistema de **predicción simple**: para cada aldea, calcula la **temperatura promedio de la segunda mitad de la semana** (días 4-7) vs la primera mitad (días 1-3). Si la segunda es mayor, predice que la semana siguiente también subirá. Si es menor, predice bajada. Muestra las predicciones en el reporte.

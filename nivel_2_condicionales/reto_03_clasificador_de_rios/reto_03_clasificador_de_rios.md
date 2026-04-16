# 🏞️ Reto 03 — El Clasificador de Ríos

**Nivel:** ⭐⭐ Condicionales | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

La **Secretaría Nacional de Hidrología** ha encargado un sistema de clasificación automática de ríos. Los ríos deben clasificarse según dos características: su **caudal** (litros por segundo) y su **longitud** (kilómetros). 

La clasificación es la siguiente:

**Por caudal:**
- Caudal < 10 L/s → Arroyo
- 10 ≤ Caudal < 100 L/s → Río pequeño
- 100 ≤ Caudal < 1000 L/s → Río mediano
- Caudal ≥ 1000 L/s → Río grande

**Por longitud:**
- Longitud < 50 km → Corto
- 50 ≤ Longitud < 500 km → Mediano
- Longitud ≥ 500 km → Largo

**Clasificación de importancia ecológica** (combinación de ambos):
- Río grande + Largo → **Ecosistema Crítico** 🔴
- Río grande + Mediano → **Alta importancia** 🟠
- Río mediano + Largo → **Alta importancia** 🟠
- Cualquier otra combinación con río grande o mediano → **Importancia media** 🟡
- Arroyo o río pequeño → **Importancia baja** 🟢

---

## 📋 El Problema

Dados el caudal y la longitud de un río, determina:
1. Su **categoría de caudal**
2. Su **categoría de longitud**
3. Su **importancia ecológica**

---

## 🔢 Entradas

- **caudal**: en litros por segundo (número real positivo)
- **longitud**: en kilómetros (número real positivo)

## 📤 Salidas

- Categoría de caudal
- Categoría de longitud
- Importancia ecológica (con ícono)

---

## 🧪 Casos de Prueba

### Caso 1
```
Entrada: caudal=5000, longitud=800

Salida esperada:
Caudal: Río grande
Longitud: Largo
Importancia ecológica: 🔴 Ecosistema Crítico
```

### Caso 2
```
Entrada: caudal=500, longitud=700

Salida esperada:
Caudal: Río mediano
Longitud: Largo
Importancia ecológica: 🟠 Alta importancia
```

### Caso 3
```
Entrada: caudal=3, longitud=5

Salida esperada:
Caudal: Arroyo
Longitud: Corto
Importancia ecológica: 🟢 Importancia baja
```

### Caso 4
```
Entrada: caudal=1500, longitud=200

Salida esperada:
Caudal: Río grande
Longitud: Mediano
Importancia ecológica: 🟠 Alta importancia
```

### Caso 5
```
Entrada: caudal=50, longitud=600

Salida esperada:
Caudal: Río pequeño
Longitud: Largo
Importancia ecológica: 🟢 Importancia baja
```

### Caso 6
```
Entrada: caudal=200, longitud=30

Salida esperada:
Caudal: Río mediano
Longitud: Corto
Importancia ecológica: 🟡 Importancia media
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_03_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Lee caudal y longitud
- [ ] Tiene una rama de decisión para clasificar el caudal (4 categorías)
- [ ] Tiene una rama de decisión para clasificar la longitud (3 categorías)
- [ ] Determina la importancia ecológica según la combinación de categorías
- [ ] Muestra las 3 salidas
- [ ] Funciona con los 6 casos de prueba

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
<summary>Pista 1 — Separar las clasificaciones</summary>

Puedes resolver el problema en **dos bloques independientes**: primero clasifica el caudal (guarda el resultado), luego clasifica la longitud (guarda el resultado). Luego usa ambos resultados para determinar la importancia ecológica. Esto hace el diagrama más claro.

</details>

<details>
<summary>Pista 2 — Condicionales anidados para la ecología</summary>

La importancia ecológica requiere comparar **dos variables a la vez** (categoría de caudal Y categoría de longitud). Usa un rombo dentro del otro o usa operadores AND.

</details>

---

## ⭐ Reto Extra

La Secretaría quiere agregar una tercera característica: la **temperatura del agua** (fría < 15°C, templada 15-25°C, cálida > 25°C). Los Ecosistemas Críticos con agua fría reciben la categoría especial **"Glaciar de importancia mundial"**. Actualiza el diagrama.
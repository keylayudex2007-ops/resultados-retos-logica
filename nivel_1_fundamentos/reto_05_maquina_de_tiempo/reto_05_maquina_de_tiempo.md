# ⏳ Reto 05 — La Máquina del Tiempo

**Nivel:** ⭐ Fundamentos | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

El profesor **Erasmo Quijano** construyó en su garaje una máquina del tiempo que, lamentablemente, solo puede hacer cálculos — no puede viajar físicamente al pasado ni al futuro (qué decepción). 

La máquina hace tres cosas:
1. Dado el año de nacimiento de una persona y el año actual, calcula su **edad actual**
2. Dado un año futuro, calcula **cuántos años tendrá** en ese año
3. Dado un año pasado, calcula **qué edad tenía** en ese año (o si todavía no había nacido)

El profesor quiere que los estudiantes diseñen el algoritmo de la máquina.

---

## 📋 El Problema

Dado el año de nacimiento de una persona, el año actual, y un año consulta (pasado o futuro):

1. Calcula la **edad actual** de la persona
2. Si el año consulta es **mayor** que el año actual: calcula la edad en ese año futuro
3. Si el año consulta es **igual** al año actual: muestra la edad actual
4. Si el año consulta es **menor** que el año actual:
   - Si el año consulta es **mayor o igual** al año de nacimiento: calcula la edad que tenía
   - Si el año consulta es **menor** que el año de nacimiento: informa que "aún no había nacido"

---

## 🔢 Entradas

- **anio_nacimiento**: año en que nació la persona (ej: 1995)
- **anio_actual**: el año presente (ej: 2025)
- **anio_consulta**: el año que se quiere consultar (ej: 2050 o 1980)

## 📤 Salidas

- Edad actual de la persona
- Resultado de la consulta (edad en el año consulta, o mensaje especial)

---

## 🧪 Casos de Prueba

### Caso 1 — Consulta futura
```
Entrada:
anio_nacimiento = 2000
anio_actual = 2025
anio_consulta = 2060

Salida esperada:
Edad actual: 25 años
En el año 2060 tendrá: 60 años
```

### Caso 2 — Consulta pasada (ya había nacido)
```
Entrada:
anio_nacimiento = 1990
anio_actual = 2025
anio_consulta = 2005

Salida esperada:
Edad actual: 35 años
En el año 2005 tenía: 15 años
```

### Caso 3 — Aún no había nacido
```
Entrada:
anio_nacimiento = 2010
anio_actual = 2025
anio_consulta = 2008

Salida esperada:
Edad actual: 15 años
En el año 2008 aún no habías nacido.
```

### Caso 4 — Consulta es el año actual
```
Entrada:
anio_nacimiento = 1985
anio_actual = 2025
anio_consulta = 2025

Salida esperada:
Edad actual: 40 años
El año consultado es el año actual: 40 años.
```

### Caso 5 — Consulta es el año de nacimiento
```
Entrada:
anio_nacimiento = 2000
anio_actual = 2025
anio_consulta = 2000

Salida esperada:
Edad actual: 25 años
En el año 2000 acababas de nacer: 0 años.
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_05_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Tiene símbolo de INICIO y FIN
- [ ] Lee las 3 entradas
- [ ] Calcula la edad actual (anio_actual - anio_nacimiento)
- [ ] Muestra la edad actual
- [ ] Compara anio_consulta con anio_actual (3 casos: mayor, igual, menor)
- [ ] En el caso "menor", tiene otro condicional: ¿ya había nacido?
- [ ] Funciona con los 5 casos de prueba

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
<summary>Pista 1 — La fórmula básica</summary>

La edad en cualquier año es: `año - año_de_nacimiento`

Esto funciona para el pasado y el futuro. Solo hay que verificar que el resultado no sea negativo (que significa "no había nacido").

</details>

<details>
<summary>Pista 2 — Estructura de decisiones</summary>

El problema tiene **dos niveles de decisión**:
1. **Primer nivel**: ¿el año consulta es mayor, igual o menor que el año actual?
2. **Segundo nivel** (solo si el año consulta es menor): ¿el año consulta es >= al año de nacimiento?

Dibuja el primer rombo, y dentro de la rama "menor" dibuja un segundo rombo.

</details>

---

## ⭐ Reto Extra

El profesor Erasmo quiere agregar una función: dado un **rango de años** (año inicio y año fin), la máquina debe mostrar la edad de la persona en **cada año del rango**. ¿Eras mayor de edad (18+) en alguno de esos años? Indícalo con un asterisco (*).

Ejemplo: Si nació en 2000 y el rango es 2015-2022, mostrar una tabla año por año.
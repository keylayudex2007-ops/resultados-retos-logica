# 🍦 Reto 03 — El Filtro de Sabores

**Nivel:** ⭐⭐⭐⭐ Arreglos | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

La heladería **"Sabores Imposibles"** tiene una carta con 20 sabores exóticos. Cada helado tiene una lista de **ingredientes** y el cliente puede ingresar sus **alergias** para filtrar automáticamente qué helados puede comer de forma segura.

Además, el cliente puede indicar sus **preferencias** (chocolate, frutal, sin azúcar, vegano) y el sistema mostrará los helados compatibles ordenados de mayor a menor compatibilidad.

---

## 📋 El Problema

Dado el catálogo de helados (nombre + ingredientes) y el perfil del cliente (alergias + preferencias), determina:
1. Qué helados están **prohibidos** por alergias
2. Qué helados son **seguros** para el cliente
3. De los seguros, cuáles **coinciden** con las preferencias del cliente (y cuántas coincidencias)
4. Ordena los seguros de más a menos compatible

---

## 🔢 Entradas

- **Catálogo**: lista de helados, cada uno con nombre y lista de ingredientes
- **Alergias del cliente**: lista de ingredientes a evitar
- **Preferencias**: lista de categorías que le gustan al cliente

## 📤 Salidas

- Lista de helados prohibidos (y qué ingrediente los descartó)
- Lista de helados seguros ordenados por compatibilidad

---

## 🧪 Caso de Prueba

### Catálogo de helados:
```
1. Vainilla Cósmica      → [leche, vainilla, azúcar]
2. Choco Trueno          → [leche, cacao, nueces, azúcar]
3. Mango Tsunami         → [mango, azúcar, limón]        [frutal]
4. Menta Radical         → [leche, menta, azúcar]
5. Vegano de Fresas      → [fresas, agua, stevia]        [frutal, vegano, sin_azúcar]
6. Pistache de las Nubes → [leche, pistache, nueces]
```

### Perfil del cliente:
```
Alergias: [nueces, leche]
Preferencias: [frutal, vegano]
```

### Salida esperada:
```
❌ Helados PROHIBIDOS (contienen alérgenos):
- Vainilla Cósmica      → contiene: leche
- Choco Trueno          → contiene: leche, nueces
- Menta Radical         → contiene: leche
- Pistache de las Nubes → contiene: leche, nueces

✅ Helados SEGUROS:
1. Vegano de Fresas      [frutal ✓, vegano ✓] →  2/2 coincidencias ⭐⭐
2. Mango Tsunami         [frutal ✓]            →  1/2 coincidencias ⭐
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda con el nombre `reto_03_diagrama.[png|pdf]`.

**Sub-diagramas recomendados:**
1. "Verificar si un helado contiene alérgenos" (sub-diagrama reutilizable)
2. "Calcular compatibilidad de preferencias"
3. Diagrama principal: iterar heladod y clasificarlos

**Lista de verificación:**
- [ ] Lee el catálogo, las alergias y las preferencias
- [ ] Para cada helado: verifica si contiene algún alérgeno (doble ciclo)
- [ ] Si contiene alérgeno → descártalo y registra qué ingrediente
- [ ] Si es seguro → calcula cuántas preferencias coinciden
- [ ] Ordena los helados seguros por número de coincidencias (de mayor a menor)
- [ ] Muestra el resultado

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
<summary>Pista 1 — Ciclos anidados para verificar alérgenos</summary>

Para cada helado, recorre los ingredientes del helado. Para cada ingrediente, recorre las alergias del cliente. Si hay coincidencia → helado descartado.

Es un doble ciclo: `para cada helado → para cada ingrediente → para cada alergia`.

</details>

<details>
<summary>Pista 2 — Las categorías como metadatos</summary>

Las preferencias del cliente (frutal, vegano, etc.) son categorías que los helados tienen como etiquetas. La compatibilidad es simplemente cuántas etiquetas del helado coinciden con las preferencias del cliente.

</details>

---

## ⭐ Reto Extra

La heladería quiere agregar una función de **"combinaciones"**: el cliente puede pedir un helado doble copa (2 sabores). El sistema debe mostrar todas las combinaciones posibles de 2 sabores seguros, ordenadas por compatibilidad total (suma de coincidencias de ambos sabores). ¡Solo muestra las 3 mejores combinaciones!

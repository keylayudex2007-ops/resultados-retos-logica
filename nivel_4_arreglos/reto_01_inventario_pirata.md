# 🏴‍☠️ Reto 01 — El Inventario Pirata

**Nivel:** ⭐⭐⭐⭐ Arreglos | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

El temido **Capitán Lógica** acaba de saquear un galeón español y su bodega está llena de tesoros. El problema: el capitán tiene la memoria de un pez dorado y necesita un **sistema de inventario** para gestionar el botín.

El inventario funciona con tres operaciones:
1. **AGREGAR**: añade un item al inventario
2. **BUSCAR**: busca si un item está en el inventario
3. **ELIMINAR**: quita un item del inventario (si existe)

Además, al final el capitán quiere:
- Ver **todos los items** del inventario actual
- Saber cuántos items tiene en total
- Encontrar cuál es el item que **más se repite** (hay items duplicados)
- Ver los items en **orden alfabético** (para impresionar a su tripulación)

---

## 📋 El Problema

Dado una lista de operaciones sobre el inventario, ejecuta cada una y al final muestra el estado del inventario con las estadísticas.

---

## 🔢 Entradas

- **N**: número de operaciones
- **N operaciones**, cada una es:
  - `AGREGAR [item]`
  - `BUSCAR [item]`
  - `ELIMINAR [item]`
- Luego una línea `REPORTE` para mostrar las estadísticas finales

## 📤 Salidas

- Para BUSCAR: si está o no está en el inventario
- Para ELIMINAR: confirmación o "no encontrado"
- Al REPORTE: lista ordenada, total de items, item más repetido

---

## 🧪 Casos de Prueba

### Caso 1
```
Entrada:
N = 8
AGREGAR moneda_de_oro
AGREGAR esmeralda
AGREGAR moneda_de_oro
AGREGAR mapa_del_tesoro
BUSCAR esmeralda
BUSCAR diamante
ELIMINAR esmeralda
REPORTE

Salida esperada:
BUSCAR esmeralda → ✅ Encontrado en el inventario.
BUSCAR diamante → ❌ No está en el inventario.
ELIMINAR esmeralda → 🗑️ Eliminado correctamente.

=== REPORTE DEL CAPITÁN LÓGICA ===
Items en inventario (3 total):
1. mapa_del_tesoro
2. moneda_de_oro
3. moneda_de_oro
Item más repetido: moneda_de_oro (aparece 2 veces)
```

### Caso 2 — Eliminar item inexistente
```
Entrada:
N = 2
AGREGAR rubí
ELIMINAR diamante
REPORTE

Salida:
ELIMINAR diamante → ⚠️ Item no encontrado en el inventario.

=== REPORTE ===
Items: [rubí]
Total: 1 item
Sin repetidos.
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_01_diagrama.[png|pdf]` en esta carpeta.

**Sub-diagramas recomendados:**
1. Diagrama principal (ciclo de N operaciones)
2. Sub-diagrama: operación BUSCAR
3. Sub-diagrama: operación ELIMINAR
4. Sub-diagrama: generar REPORTE

**Lista de verificación:**
- [ ] Inicializa la lista `inventario` vacía
- [ ] Ciclo de N operaciones
- [ ] Dentro del ciclo: identifica qué operación es y la dirige al sub-diagrama correcto
- [ ] AGREGAR: añade el item al final de la lista
- [ ] BUSCAR: recorre la lista buscando el item, muestra resultado
- [ ] ELIMINAR: busca el item y lo quita si existe
- [ ] REPORTE: ordena la lista, muestra todo, encuentra el más repetido

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
<summary>Pista 1 — Búsqueda lineal</summary>

Para BUSCAR o ELIMINAR, recorre la lista con un ciclo. Para cada elemento, compara con el item buscado. Si los encuentras, sale del ciclo con el índice.

</details>

<details>
<summary>Pista 2 — Encontrar el más repetido</summary>

Para el item más repetido: recorre la lista. Para cada item único, cuenta cuántas veces aparece (con un segundo ciclo interno). Guarda el que tenga mayor conteo.

</details>

---

## ⭐ Reto Extra

El capitán quiere dividir el botín en **partes iguales** entre su tripulación de M piratas. ¿Cuántos items le tocan a cada uno? ¿Cuántos quedan sin repartir? Muestra también qué items específicos le tocan a cada pirata (distribución en orden alfabético).

# 📊 Reto 05 — El Generador de Reportes

**Nivel:** ⭐⭐⭐⭐⭐ Funciones | **Dificultad:** 🔴 Muy Difícil

---

## 🎯 Historia

La **Escuela de Talentos Raros** tiene un sistema de calificaciones muy elaborado. Al final del semestre, el director (don **Reporte Guzmán**) necesita generar automáticamente el boletín de cada estudiante.

El boletín incluye:
- Promedio general
- Mejor y peor materia
- Clasificación del desempeño
- Comparación con el promedio del grupo
- Comentario personalizado según el perfil del estudiante

El sistema usa **múltiples funciones** que trabajan en conjunto.

---

## 📋 Las Funciones

### `calcular_promedio(calificaciones[])` → número
Suma todas las calificaciones y las divide entre la cantidad.

### `encontrar_extremos(calificaciones[], nombres[])` → (mejor_nombre, mejor_nota, peor_nombre, peor_nota)
Encuentra la materia con la nota más alta y la más baja.

### `clasificar_desempeno(promedio)` → string
- promedio ≥ 90 → "Excelente"
- promedio ≥ 80 → "Muy Bueno"
- promedio ≥ 70 → "Bueno"
- promedio ≥ 60 → "Suficiente"
- promedio < 60 → "Insuficiente"

### `comparar_con_grupo(promedio_estudiante, promedio_grupo)` → string
- Si está 10+ puntos arriba → "Muy por encima del promedio del grupo"
- Si está 5-10 puntos arriba → "Por encima del promedio del grupo"
- Si está entre -5 y 5 → "En el promedio del grupo"
- Si está 5-10 debajo → "Por debajo del promedio del grupo"
- Si está 10+ debajo → "Muy por debajo del promedio del grupo"

### `generar_comentario(nombre, clasificacion, mejor_materia, peor_materia)` → string
Genera un comentario personalizado. Ejemplos:
- Excelente + mejor=Matemáticas → "¡{nombre} tiene un talento excepcional, especialmente en {mejor_materia}!"
- Insuficiente + peor=Historia → "{nombre} necesita dedicar más esfuerzo, sobre todo en {peor_materia}."
- (Diseña al menos 5 comentarios distintos según las combinaciones)

### `generar_boletin(nombre, calificaciones[], materias[], promedio_grupo)` → void
Función principal que llama todas las anteriores y muestra el boletín completo.

### `generar_reporte_grupo(estudiantes[], todas_calificaciones[][], materias[])` → void
Llama a `generar_boletin` para cada estudiante, y al final muestra un resumen del grupo.

---

## 🧪 Caso de Prueba

### Entrada:
```
Materias: [Matemáticas, Historia, Ciencias, Español, Arte]

Estudiante 1: Ana Torres
Calificaciones: [95, 72, 88, 91, 85]

Estudiante 2: Bruno Reyes
Calificaciones: [58, 63, 55, 70, 62]

Promedio del grupo a calcular automáticamente.
```

### Salida esperada (boletín de Ana):
```
╔══════════════════════════════════════╗
║  BOLETÍN DE CALIFICACIONES           ║
║  Alumna: Ana Torres                  ║
╠══════════════════════════════════════╣
║  Matemáticas:  95                    ║
║  Historia:     72                    ║
║  Ciencias:     88                    ║
║  Español:      91                    ║
║  Arte:         85                    ║
╠══════════════════════════════════════╣
║  Promedio: 86.2       Desempeño: Muy Bueno  ║
║  🏆 Mejor materia:  Matemáticas (95) ║
║  📉 Área de mejora: Historia (72)    ║
║  Posición grupal: Por encima del promedio   ║
╠══════════════════════════════════════╣
║  Comentario:                         ║
║  "¡Ana tiene un talento excepcional, ║
║  especialmente en Matemáticas!"      ║
╚══════════════════════════════════════╝
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Un sub-diagrama por función. El más complejo es `generar_reporte_grupo`.  
> Guarda con `reto_05_diagramas.[png|pdf]`.

**Lista de verificación:**
- [ ] `calcular_promedio`: ciclo de suma + división
- [ ] `encontrar_extremos`: recorre con un ciclo guardando el mayor y menor vistos
- [ ] `clasificar_desempeno`: cadena de condicionales con el promedio
- [ ] `comparar_con_grupo`: calcula la diferencia y usa condicionales
- [ ] `generar_comentario`: múltiples condicionales anidados
- [ ] `generar_boletin`: orquesta todas las funciones anteriores
- [ ] `generar_reporte_grupo`: ciclo sobre estudiantes + calcula promedio del grupo primero

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
<summary>Pista 1 — El promedio del grupo</summary>

Para el promedio del grupo necesitas el promedio de TODOS los estudiantes. En `generar_reporte_grupo`, primero calcula todos los promedios individuales y luego promédialos. Solo entonces puedes llamar a `generar_boletin` para cada uno con el promedio del grupo correcto.

</details>

<details>
<summary>Pista 2 — Composición de funciones</summary>

`generar_boletin` debe llamar a `calcular_promedio`, luego a `encontrar_extremos`, luego a `clasificar_desempeno`, luego a `comparar_con_grupo`, y finalmente a `generar_comentario`. El resultado de cada función alimenta a las siguientes.

</details>

---

## ⭐ Reto Extra

El director quiere un **resumen ejecutivo** del semestre: para cada materia, ¿qué porcentaje del grupo la aprobó (≥60)? ¿Cuál es la materia con mayor promedio y cuál con menor? Crea la función `resumen_ejecutivo(todas_calificaciones[][], materias[])` que genere este análisis.

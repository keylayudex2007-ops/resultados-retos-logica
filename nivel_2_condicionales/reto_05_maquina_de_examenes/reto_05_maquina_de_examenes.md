# 📝 Reto 05 — La Máquina de Exámenes

**Nivel:** ⭐⭐ Condicionales | **Dificultad:** 🟠 Difícil

---

## 🎯 Historia

La **Universidad de las Decisiones Difíciles** tiene un sistema de evaluación muy peculiar. Para aprobar una materia, un estudiante debe cumplir **todas** las siguientes condiciones:

1. La **nota del examen final** debe ser ≥ 60
2. El **promedio de parciales** (hay 3 parciales) debe ser ≥ 55
3. La **asistencia** debe ser ≥ 80% (de 100 clases posibles)
4. El proyecto final debe estar **entregado** (SI / NO)

**Calificaciones finales:**
- Si **reprueba** por cualquier razón: `"REPROBADO"` + motivo(s)
- Si cumple todo:
  - Promedio final = (examen_final × 0.4) + (promedio_parciales × 0.4) + (asistencia_puntos × 0.2)
    - donde `asistencia_puntos = (asistencia / 100) × 100`
  - Promedio final ≥ 90 → `"APROBADO CON DISTINCIÓN"`
  - Promedio final ≥ 70 → `"APROBADO"`
  - Promedio final ≥ 60 → `"APROBADO CON CONDICIÓN"`

---

## 📋 El Problema

Dados los datos académicos de un estudiante, determina si aprobó o reprobó y su calificación final.

---

## 🔢 Entradas

- **parcial1, parcial2, parcial3**: notas de los 3 parciales (0-100)
- **examen_final**: nota del examen final (0-100)
- **asistencia**: número de clases asistidas (0-100)
- **proyecto_entregado**: SI o NO

## 📤 Salidas

- Decisión: APROBADO / REPROBADO (con clasificación o motivo)
- Promedio de parciales y promedio final (si aprobó)

---

## 🧪 Casos de Prueba

### Caso 1 — Aprobado con distinción
```
Entrada:
Parciales: 95, 90, 85  |  Final: 92  |  Asistencia: 98  |  Proyecto: SI

Salida esperada:
Promedio parciales: 90.0
Promedio final: 91.2
✅ APROBADO CON DISTINCIÓN
```

### Caso 2 — Reprobado por múltiples razones
```
Entrada:
Parciales: 40, 50, 45  |  Final: 55  |  Asistencia: 70  |  Proyecto: NO

Salida esperada:
❌ REPROBADO
Motivos:
- Examen final insuficiente (55 < 60)
- Promedio de parciales insuficiente (45 < 55)
- Asistencia insuficiente (70% < 80%)
- Proyecto no entregado
```

### Caso 3 — Solo reprobado por asistencia
```
Entrada:
Parciales: 80, 75, 85  |  Final: 70  |  Asistencia: 75  |  Proyecto: SI

Salida esperada:
❌ REPROBADO
Motivos:
- Asistencia insuficiente (75% < 80%)
```

### Caso 4 — Aprobado con condición
```
Entrada:
Parciales: 60, 65, 58  |  Final: 62  |  Asistencia: 82  |  Proyecto: SI

Salida esperada:
Promedio parciales: 61.0
Promedio final: 62.2
⚠️ APROBADO CON CONDICIÓN
```

### Caso 5 — Aprobado normal
```
Entrada:
Parciales: 75, 80, 70  |  Final: 78  |  Asistencia: 90  |  Proyecto: SI

Salida esperada:
Promedio parciales: 75.0
Promedio final: 77.0
✅ APROBADO
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_05_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Lee todas las entradas
- [ ] Calcula el promedio de parciales
- [ ] Verifica las 4 condiciones de aprobación y registra los motivos de falla
- [ ] Si hay motivos de falla → imprime REPROBADO con todos los motivos
- [ ] Si no hay fallas → calcula el promedio final y lo clasifica
- [ ] Funciona con los 5 casos de prueba

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
<summary>Pista 1 — Recolectar motivos</summary>

En lugar de usar if/else gigantes, usa una **lista de motivos de falla**. Revisa cada condición por separado y si falla, agrega el motivo a la lista. Al final, si la lista tiene elementos → REPROBADO; si está vacía → APROBADO.

</details>

<details>
<summary>Pista 2 — La fórmula del promedio final</summary>

```
promedio_final = (examen_final × 0.4) + (promedio_parciales × 0.4) + (asistencia × 0.2)
```

La asistencia ya es un porcentaje de 100, así que se usa directamente.

</details>

---

## ⭐ Reto Extra

El decano quiere agregar una **"segunda oportunidad"**: si el estudiante reprobó solo por el examen final (y cumple todo lo demás), puede presentar un **examen de recuperación**. Si saca ≥ 70 en recuperación, aprueba con el mínimo (calificación fija de 60). Modifica el diagrama para incluir esta posibilidad.
# 🤥 Reto 01 — El Detector de Mentiras

**Nivel:** ⭐⭐ Condicionales | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

La detective **Valentina Ríos** usa un polígrafo digital para sus interrogatorios. El polígrafo detecta inconsistencias entre las respuestas del sospechoso.

El sistema funciona con **tres preguntas de control** cuyas respuestas "correctas" son conocidas de antemano. El polígrafo compara las respuestas del sospechoso y emite un veredicto:

- Si las **3 respuestas son correctas** → **"Sin inconsistencias"**
- Si **exactamente 1 respuesta es incorrecta** → **"Posible estrés"**
- Si **exactamente 2 respuestas son incorrectas** → **"Alta probabilidad de engaño"**
- Si las **3 respuestas son incorrectas** → **"Sospechoso confirma mentira"**

Además, si la **primera pregunta** (que es la más importante) es incorrecta, siempre se agrega la nota: **"⚠️ ALERTA: Inconsistencia en pregunta clave"**.

---

## 📋 El Problema

Dados los valores correctos de las 3 preguntas y las respuestas del sospechoso, emite el veredicto del polígrafo con la nota de alerta si aplica.

---

## 🔢 Entradas

- **correcta1, correcta2, correcta3**: las respuestas correctas (pueden ser "SI" o "NO")
- **respuesta1, respuesta2, respuesta3**: las respuestas del sospechoso

## 📤 Salidas

- El veredicto del polígrafo
- La nota de alerta (si aplica)

---

## 🧪 Casos de Prueba

### Caso 1 — Sin mentiras
```
Entrada:
Correctas:   SI, NO, SI
Respuestas:  SI, NO, SI

Salida esperada:
Veredicto: Sin inconsistencias.
```

### Caso 2 — Una mentira (en pregunta clave)
```
Entrada:
Correctas:   SI, NO, SI
Respuestas:  NO, NO, SI

Salida esperada:
Veredicto: Posible estrés.
⚠️ ALERTA: Inconsistencia en pregunta clave.
```

### Caso 3 — Dos mentiras
```
Entrada:
Correctas:   NO, NO, SI
Respuestas:  SI, SI, SI

Salida esperada:
Veredicto: Alta probabilidad de engaño.
⚠️ ALERTA: Inconsistencia en pregunta clave.
```

### Caso 4 — Tres mentiras
```
Entrada:
Correctas:   SI, SI, NO
Respuestas:  NO, NO, SI

Salida esperada:
Veredicto: Sospechoso confirma mentira.
⚠️ ALERTA: Inconsistencia en pregunta clave.
```

### Caso 5 — Dos mentiras, sin alerta
```
Entrada:
Correctas:   SI, NO, SI
Respuestas:  SI, SI, NO

Salida esperada:
Veredicto: Alta probabilidad de engaño.
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_01_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Lee las 6 entradas (3 correctas + 3 respuestas)
- [ ] Compara cada par y cuenta el número de incorrectas (0, 1, 2 o 3)
- [ ] Usa el contador para determinar el veredicto
- [ ] Adicionalmente verifica si respuesta1 ≠ correcta1 para la alerta
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
<summary>Pista 1 — Contar incorrectas</summary>

En lugar de hacer un árbol de if/else enorme, considera usar un **contador de errores**. Por cada respuesta incorrecta, suma 1 al contador. Al final, el contador te dice directamente el veredicto.

</details>

<details>
<summary>Pista 2 — La alerta es independiente</summary>

La alerta de la pregunta clave es una verificación **separada** del veredicto. Después de determinar el veredicto, verifica el caso de la alerta con un condicional adicional.

</details>

---

## ⭐ Reto Extra

La detective Valentina quiere extender el sistema a **N preguntas** (no solo 3). Define un **umbral**: si el porcentaje de respuestas incorrectas supera el 50%, el veredicto es "Alta sospecha"; si supera el 70%, es "Confirmado: mentiroso". Diseña el diagrama para N preguntas con umbrales porcentuales.
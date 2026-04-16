# 🚦 Reto 02 — El Semáforo Roto

**Nivel:** ⭐ Fundamentos | **Dificultad:** 🟢 Fácil

---

## 🎯 Historia

En la ciudad más caótica del mundo, **Villa Trampa**, el único semáforo de la avenida principal se ha desconfigurado. El técnico municipal descubrió que el semáforo ya no sigue el ciclo estándar (verde, amarillo, rojo) sino que tiene **tiempos variables** que el operador puede configurar cada día.

El jefe de tránsito necesita saber, **dado el tiempo en verde, el tiempo en amarillo y el tiempo en rojo**, cuántos **ciclos completos** puede hacer el semáforo en un turno de trabajo de **8 horas** (480 minutos), y cuántos **minutos sobrantes** quedan sin completar un ciclo.

---

## 📋 El Problema

Dados los tiempos en segundos de cada fase del semáforo, calcula:
1. La **duración total de un ciclo** (en segundos)
2. Cuántos **ciclos completos** caben en 8 horas (28800 segundos)
3. Cuántos **segundos sobran** después del último ciclo completo

---

## 🔢 Entradas

- **verde**: tiempo en verde (en segundos), entero positivo
- **amarillo**: tiempo en amarillo (en segundos), entero positivo
- **rojo**: tiempo en rojo (en segundos), entero positivo

## 📤 Salidas

- Duración del ciclo completo (en segundos)
- Número de ciclos completos en 8 horas
- Segundos sobrantes

---

## 🧪 Casos de Prueba

### Caso 1 — Ciclo estándar
```
Entrada:
verde = 30
amarillo = 5
rojo = 25

Salida esperada:
Ciclo completo: 60 segundos
Ciclos en 8 horas: 480
Segundos sobrantes: 0
```

### Caso 2 — Ciclo irregular
```
Entrada:
verde = 45
amarillo = 7
rojo = 33

Salida esperada:
Ciclo completo: 85 segundos
Ciclos en 8 horas: 338
Segundos sobrantes: 50
```

### Caso 3 — Ciclo muy largo
```
Entrada:
verde = 300
amarillo = 30
rojo = 270

Salida esperada:
Ciclo completo: 600 segundos
Ciclos en 8 horas: 48
Segundos sobrantes: 0
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_02_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Tiene símbolo de INICIO y FIN
- [ ] Lee las 3 entradas (verde, amarillo, rojo)
- [ ] Calcula el ciclo completo sumando los 3 valores
- [ ] Calcula los ciclos completos usando división entera
- [ ] Calcula los segundos sobrantes usando el módulo (%)
- [ ] Muestra las 3 salidas
- [ ] Funciona con los 3 casos de prueba

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
<summary>Pista 1 — Operación clave</summary>

Hay dos operaciones matemáticas fundamentales en este problema:
- **División entera** (sin decimales): para saber cuántos ciclos completos caben
- **Módulo** (`%`): para saber cuánto sobra

</details>

<details>
<summary>Pista 2 — La fórmula</summary>

- `ciclo = verde + amarillo + rojo`
- `ciclos_completos = 28800 ÷ ciclo` (división entera)
- `sobrantes = 28800 % ciclo`

</details>

---

## ⭐ Reto Extra

El municipio quiere saber además:
- A los **45 minutos** de empezar el turno, ¿en qué **fase del semáforo** está? (verde, amarillo o rojo) y ¿cuántos segundos lleva en esa fase?
- ¿En qué **minuto exacto** del turno arranca el ciclo número 100?
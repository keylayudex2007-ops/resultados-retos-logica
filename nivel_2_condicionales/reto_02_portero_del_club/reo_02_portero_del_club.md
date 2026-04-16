# 🕺 Reto 02 — El Portero del Club

**Nivel:** ⭐⭐ Condicionales | **Dificultad:** 🟡 Medio

---

## 🎯 Historia

**El Club del Algoritmo** es el lugar más exclusivo de la ciudad. **Don Serafín**, el portero, tiene una lista de reglas que debe seguir al pie de la letra antes de dejar entrar a alguien:

1. La persona debe tener **18 años o más**
2. Debe traer una **identificación válida** (pasaporte o credencial)
3. Debe estar en la **lista de invitados** O haber pagado la **entrada de $500 pesos**
4. Si viene con un **acompañante que no cumple las reglas**, ambos son rechazados
5. Excepción: los **miembros VIP** entran sin importar nada (excepto la edad mínima)

Don Serafín tarda mucho verificando todo esto manualmente. Necesita un algoritmo que le diga inmediatamente: **"ENTRA"** o **"NO ENTRA"** y **por qué**.

---

## 📋 El Problema

Dado el perfil de una persona, determina si puede entrar al club y el motivo de la decisión.

---

## 🔢 Entradas

- **edad**: edad de la persona (entero)
- **tiene_id**: si trae identificación válida (SI / NO)
- **en_lista**: si está en la lista de invitados (SI / NO)
- **pago_entrada**: si pagó los $500 (SI / NO)
- **es_vip**: si es miembro VIP (SI / NO)
- **acompañante_ok**: si su acompañante cumple todas las reglas (SI / NO / NINGUNO)

## 📤 Salidas

- Decisión: `ENTRA` o `NO ENTRA`
- Motivo de la decisión

---

## 🧪 Casos de Prueba

### Caso 1 — VIP menor de edad
```
Entrada: edad=16, tiene_id=SI, en_lista=SI, pago=SI, es_vip=SI, acompañante=NINGUNO

Salida: NO ENTRA — Es menor de edad (incluso los VIP deben ser mayores de edad).
```

### Caso 2 — VIP adulto sin nada más
```
Entrada: edad=25, tiene_id=NO, en_lista=NO, pago=NO, es_vip=SI, acompañante=NINGUNO

Salida: ENTRA — Miembro VIP con edad válida.
```

### Caso 3 — Cumple todo correctamente
```
Entrada: edad=22, tiene_id=SI, en_lista=SI, pago=NO, es_vip=NO, acompañante=SI

Salida: ENTRA — Cumple todos los requisitos.
```

### Caso 4 — Sin identificación
```
Entrada: edad=30, tiene_id=NO, en_lista=SI, pago=SI, es_vip=NO, acompañante=NINGUNO

Salida: NO ENTRA — No presenta identificación válida.
```

### Caso 5 — Acompañante problemático
```
Entrada: edad=28, tiene_id=SI, en_lista=SI, pago=NO, es_vip=NO, acompañante=NO

Salida: NO ENTRA — Su acompañante no cumple los requisitos.
```

### Caso 6 — Sin lista y sin pago
```
Entrada: edad=19, tiene_id=SI, en_lista=NO, pago=NO, es_vip=NO, acompañante=NINGUNO

Salida: NO ENTRA — No está en la lista de invitados y no pagó la entrada.
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda la imagen con el nombre `reto_02_diagrama.[png|pdf]` en esta carpeta.

**Lista de verificación del diagrama:**
- [ ] Lee las 6 entradas
- [ ] Verifica la edad PRIMERO (aplica a todos, incluso VIP)
- [ ] Verifica si es VIP (cambia el flujo)
- [ ] Para no-VIP: verifica identificación, luego (lista OR pago), luego acompañante
- [ ] Cada rama de rechazo tiene su propio mensaje de motivo
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
<summary>Pista 1 — El orden importa</summary>

Verifica las condiciones **en orden de prioridad**:
1. Edad (aplica a todos)
2. ¿Es VIP? (si sí, saltarse las demás verificaciones)
3. Identificación
4. Lista O pago
5. Acompañante

</details>

<details>
<summary>Pista 2 — El operador OR</summary>

La condición "en lista O pagó entrada" usa el operador lógico **OR**. En el diagrama, un rombo con OR puede representarse como dos rombos consecutivos donde si alguno dice Sí, avanzas.

</details>

---

## ⭐ Reto Extra

El club tiene **4 zonas**: Entrada General, Sala VIP, Terraza y Cabina del DJ. Cada zona tiene sus propias restricciones. Diseña el diagrama que, dado el perfil de la persona, determina a cuáles zonas puede acceder (puede ser a ninguna, una o varias).
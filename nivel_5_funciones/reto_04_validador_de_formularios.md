# 📋 Reto 04 — El Validador de Formularios

**Nivel:** ⭐⭐⭐⭐⭐ Funciones | **Dificultad:** 🟠 Difícil

---

## 🎯 Historia

La startup **"FormaFácil"** desarrolla formularios web. Su sistema de validación del lado del servidor necesita verificar que los datos del usuario son correctos antes de guardarlos en la base de datos.

Cada campo tiene sus propias reglas de validación. El sistema usa **funciones especializadas** para cada tipo de campo.

---

## 📋 Las Funciones de Validación

### `validar_nombre(nombre)` → (valido, mensaje)
- No puede estar vacío
- Solo letras y espacios (no números ni caracteres especiales)
- Longitud entre 2 y 50 caracteres
- No puede empezar ni terminar con espacio

### `validar_email(email)` → (valido, mensaje)
- Debe contener exactamente UN símbolo `@`
- Antes del `@` debe haber al menos 1 carácter
- Después del `@` debe haber un punto (`.`)
- Después del último punto debe haber entre 2 y 4 caracteres (extensión)

### `validar_telefono(telefono)` → (valido, mensaje)
- Solo dígitos (puede tener un `+` al inicio para código de país)
- Longitud entre 10 y 15 dígitos (sin contar el `+`)
- No puede empezar con 0 si no tiene código de país

### `validar_fecha_nacimiento(fecha)` → (valido, mensaje, edad)
- Formato: `DD/MM/AAAA`
- La persona debe tener entre 13 y 120 años
- La fecha no puede ser en el futuro
- Verifica que el día sea válido para el mes (considera meses con 28/29/30/31 días)

### `validar_formulario(nombre, email, tel, fecha)` → reporte_completo
Llama a las 4 funciones anteriores y genera un reporte de validación completo.

---

## 🧪 Casos de Prueba

### Caso 1 — Todo inválido
```
Entrada:
nombre = "J"
email = "noesunmail"
telefono = "123"
fecha = "45/13/2000"

Salida:
=== REPORTE DE VALIDACIÓN ===
❌ nombre:    "J" → Muy corto (mínimo 2 caracteres)
❌ email:     "noesunmail" → No contiene '@'
❌ teléfono: "123" → Muy corto (mínimo 10 dígitos)
❌ fecha:     "45/13/2000" → Día inválido (45) y mes inválido (13)

Estado: FORMULARIO RECHAZADO (4 errores)
```

### Caso 2 — Todo válido
```
Entrada:
nombre = "María López"
email = "maria@ejemplo.com"
telefono = "+5215551234567"
fecha = "15/08/1995"

Salida:
=== REPORTE DE VALIDACIÓN ===
✅ nombre:    "María López" → Válido
✅ email:     "maria@ejemplo.com" → Válido
✅ teléfono: "+5215551234567" → Válido
✅ fecha:     "15/08/1995" → Válido | Edad: 29 años

Estado: FORMULARIO ACEPTADO ✅
```

### Caso 3 — Emails inválidos varios
```
"usuario@"           → falta dominio
"@dominio.com"       → falta usuario
"usuario.dominio.com"→ falta @
"a@b.c"              → extensión muy corta (1 char)
"a@b.comcomcom"      → extensión muy larga
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Un sub-diagrama por función.  
> Guarda con `reto_04_diagramas.[png|pdf]`.

**Lista de verificación:**
- [ ] `validar_nombre`: ciclo para verificar que cada carácter sea letra o espacio
- [ ] `validar_email`: buscar el `@`, dividir en dos partes, verificar el punto en la derecha
- [ ] `validar_telefono`: verificar el `+` opcional, luego que todos sean dígitos y el largo
- [ ] `validar_fecha`: parsear DD/MM/AAAA, validar rangos de cada parte, calcular edad
- [ ] `validar_formulario`: llama las 4, acumula errores, muestra reporte

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
<summary>Pista 1 — Validar el email</summary>

Para encontrar el `@`, recorre el string carácter a carácter y guarda su posición. Si encuentras más de uno (o ninguno) → inválido. Luego divide en `[antes_del_@]` y `[después_del_@]` y valida cada parte.

</details>

<details>
<summary>Pista 2 — Días válidos por mes</summary>

Crea una lista con los días máximos por mes: `[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`. Para febrero, si el año es bisiesto, usa 29. Año bisiesto: divisible entre 4 Y (no divisible entre 100 O divisible entre 400).

</details>

---

## ⭐ Reto Extra

Agrega una función `validar_contrasena_match(pass1, pass2)` que verifique que dos contraseñas ingresadas son idénticas, y una función `validar_codigo_postal(cp, pais)` que valide formatos distintos por país (México: 5 dígitos, USA: 5 dígitos o ZIP+4, España: 5 dígitos empezando por 01-52).

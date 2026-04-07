# 🔐 Reto 03 — La Fábrica de Contraseñas

**Nivel:** ⭐⭐⭐⭐⭐ Funciones | **Dificultad:** 🟠 Difícil

---

## 🎯 Historia

La empresa **"CiberSeguro S.A."** ofrece un servicio de generación y validación de contraseñas. El sistema tiene tres modos:

1. **Generar**: crea una contraseña segura a partir de una frase del usuario
2. **Validar**: verifica si una contraseña cumple los requisitos de seguridad
3. **Evaluar**: calcula la **fuerza** de una contraseña (Débil / Media / Fuerte / Inquebrantable)

---

## 📋 Las Funciones

### `tiene_mayusculas(password)` → booleano
Retorna `verdadero` si la contraseña tiene al menos UNA letra mayúscula.

### `tiene_minusculas(password)` → booleano
Retorna `verdadero` si tiene al menos UNA letra minúscula.

### `tiene_numeros(password)` → booleano
Retorna `verdadero` si tiene al menos UN número.

### `tiene_especiales(password)` → booleano
Retorna `verdadero` si tiene al menos UN carácter especial (`!@#$%^&*`).

### `longitud_ok(password, minimo)` → booleano
Retorna `verdadero` si la longitud es ≥ minimo.

### `validar_password(password)` → (es_valida, lista_de_problemas)
Retorna si la contraseña es válida (cumple TODOS los requisitos: largo ≥ 8, mayúsculas, minúsculas, números, especiales) y la lista de problemas si falla.

### `evaluar_fuerza(password)` → string
- Solo letras minúsculas → "Débil"
- Letras + números (sin espaciales ni mayúsculas) → "Media"
- Cumple 3 de 5 criterios → "Fuerte"
- Cumple los 5 criterios Y largo ≥ 12 → "Inquebrantable"

### `generar_desde_frase(frase)` → password
- Toma la primera letra de cada palabra de la frase
- Convierte vocales a números (a→4, e→3, i→1, o→0, u→9)
- Las palabras en posición par (0, 2, 4...) van en MAYÚSCULA
- Al final añade `"!2024"`

---

## 🧪 Casos de Prueba

### Caso 1 — Validar contraseña
```
validar_password("hola123")

Resultado:
❌ Contraseña inválida.
Problemas:
- Falta al menos una mayúscula
- Falta al menos un carácter especial
- Longitud insuficiente (7 < 8 caracteres)
```

### Caso 2 — Validar contraseña válida
```
validar_password("ProgramAción#99")

Resultado:
✅ Contraseña válida.
Fuerza: Inquebrantable (largo=15, todos los criterios)
```

### Caso 3 — Generar desde frase
```
generar_desde_frase("me gusta programar con logica")

Palabras: me, gusta, programar, con, logica
Primeras letras: m, g, p, c, l
Aplicar mayúsculas en posición par (0,2,4): M, g, P, c, L
Convertir vocales: (no hay vocales sueltas en las iniciales aquí)
Añadir "!2024"

Resultado: "MgPcL!2024"

Evaluación: Fuerte (tiene mayúsculas, minúsculas, números, especiales; largo=10)
```

### Caso 4 — Generar desde frase con vocales
```
generar_desde_frase("el universo es infinito")

Palabras: el, universo, es, infinito
Primeras letras: e, u, e, i
Posiciones pares (0,2): E, u, E, i → mayúsculas
Convertir vocales: E→3, u→9, E→3, i→1
Añadir "!2024"

Resultado: "3931!2024"

Evaluación: Media (tiene números y especiales, pero no mayúsculas/minúsculas textuales)
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Crea un sub-diagrama por cada una de las 8 funciones.  
> Guarda con `reto_03_diagramas.[png|pdf]`.

**Lista de verificación:**
- [ ] `tiene_mayusculas`: ciclo que recorre cada carácter, verifica si es mayúscula
- [ ] `tiene_minusculas`: similar al anterior
- [ ] `tiene_numeros`: similar, verifica si es dígito
- [ ] `tiene_especiales`: verifica si el carácter está en el conjunto `!@#$%^&*`
- [ ] `longitud_ok`: comparación única (len >= minimo)
- [ ] `validar_password`: llama a las 5 funciones anteriores, recoge problemas
- [ ] `evaluar_fuerza`: cuenta criterios cumplidos y devuelve categoría
- [ ] `generar_desde_frase`: divide frase en palabras, aplica transformaciones

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
<summary>Pista 1 — Recorrer caracteres de un string</summary>

Para verificar si una cadena tiene mayúsculas, minúsculas, etc., recorre cada carácter con un ciclo. Usa las funciones del lenguaje para verificar el tipo: `isupper()`, `islower()`, `isdigit()` (Python), o comparaciones con rangos ASCII.

</details>

<details>
<summary>Pista 2 — Dividir frase en palabras</summary>

Muchos lenguajes tienen `split(" ")` para dividir un string por espacios. Si no está disponible, recorre el string carácter a carácter y acumula en una palabra hasta encontrar un espacio.

</details>

---

## ⭐ Reto Extra

Implementa una función `descifrar(password)` que **revierta** el proceso de `generar_desde_frase`, pero solo para la parte de sustitución de vocales (no puede recuperar las palabras originales, pero sí puede "descodificar" los números: 4→a, 3→e, 1→i, 0→o, 9→u). Úsala para verificar que el proceso es reversible.

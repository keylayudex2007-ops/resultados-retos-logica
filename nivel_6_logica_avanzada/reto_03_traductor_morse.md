# 📡 Reto 03 — El Traductor Morse

**Nivel:** 🔥 Lógica Avanzada | **Dificultad:** 🟠 Difícil

---

## 🎯 Historia

El agente secreto **Señal Pérez** trabaja para la **Agencia de Comunicaciones Anacrónicas**, un grupo que por razones de seguridad sigue usando el **código Morse** para sus mensajes. Señal Pérez necesita un traductor bidireccional: texto → Morse y Morse → texto.

Pero hay un giro: la agencia tiene sus propias reglas de codificación adicionales para mayor seguridad.

---

## 📋 El Código Morse Estándar

```
A=.-    B=-...  C=-.-.  D=-..   E=.     F=..-.
G=--.   H=....  I=..    J=.---  K=-.-   L=.-..
M=--    N=-.    O=---   P=.--.  Q=--.-  R=.-.
S=...   T=-     U=..-   V=...-  W=.--   X=-..-
Y=-.--  Z=--..

0=-----  1=.----  2=..---  3=...--  4=....-
5=.....  6==....  7=--...  8=---..  9=----.
```

**Reglas de formato Morse:**
- Cada letra/número está separada por un **espacio** (`-.- .- ... .-`)
- Cada palabra está separada por **tres espacios** o por `/` (`.-   -... /   -.-.`)

---

## 📋 Las Funciones

### `letra_a_morse(letra)` → string
Dado una letra o dígito, retorna su código Morse.

### `morse_a_letra(codigo)` → string
Dado un código Morse, retorna la letra o dígito correspondiente.

### `texto_a_morse(texto)` → string
Convierte un texto completo a Morse (maneja espacios entre palabras).

### `morse_a_texto(morse)` → string
Convierte una cadena Morse completa a texto.

### `verificar_palíndromo_morse(texto)` → booleano
Verifica si la representación Morse del texto es un palíndromo (igual de izquierda a derecha que de derecha a izquierda, ignorando espacios).

### `encriptar_agencia(morse)` → string
**Regla especial de la agencia**: invierte cada símbolo individualmente (`.` → `-` y `-` → `.`), manteniendo los grupos.

### `desencriptar_agencia(morse_encriptado)` → string
El proceso inverso de `encriptar_agencia`.

---

## 🧪 Casos de Prueba

### Caso 1 — Texto a Morse
```
texto_a_morse("SOS")

S = ...
O = ---
S = ...

Resultado: "... --- ..."
```

### Caso 2 — Texto con espacios
```
texto_a_morse("HOLA MUNDO")

H=....  O=---  L=.-..  A=.-      M=--  U=..-  N=-.  D=-..  O=---

Resultado: ".... --- .-.. .- / -- ..- -. -.. ---"
```

### Caso 3 — Morse a texto
```
morse_a_texto("-- --- .-. ... .")
Resultado: "MORSE"
```

### Caso 4 — Encriptado de la agencia
```
encriptar_agencia("... --- ...")

Invierte cada símbolo: . → -  y  - → .

"... " → "---"
"---"  → "..."
"..."  → "---"

Resultado: "--- ... ---"

(que en Morse estándar sería "OSO")
```

### Caso 5 — Palíndromo Morse
```
verificar_palindromo_morse("AMA")
A=.-  M=--  A=.-

Morse: ".- -- .-"
Sin espacios: ".--..-" 
¿Es palíndromo? → ".--..—" vs "--..-." → ¿Es igual al revés? NO

verificar_palindromo_morse("ETE")
E=.  T=-  E=.

Morse: ". - ."
Sin espacios: ".-."
Revés: ".-."
→ SÍ es palíndromo ✅
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda con `reto_03_diagramas.[png|pdf]`.

**El diccionario Morse:** Necesitas una estructura que almacene la asociación letra↔código. En el diagrama puedes representarla como una "tabla de búsqueda".

**Lista de verificación:**
- [ ] `letra_a_morse`: busca la letra en el diccionario y retorna el código
- [ ] `morse_a_letra`: busca el código en el diccionario y retorna la letra
- [ ] `texto_a_morse`: ciclo sobre cada carácter; si es espacio → agrega `/`; si no → convierte con `letra_a_morse`
- [ ] `morse_a_texto`: divide por `/` para obtener palabras; divide cada palabra por espacio para obtener letras; convierte cada una con `morse_a_letra`
- [ ] `encriptar_agencia`: ciclo sobre el morse, invierte cada `.` por `-` y viceversa, preserva espacios
- [ ] `verificar_palindromo_morse`: convierte a morse, quita espacios, verifica si el string es igual al revés

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
<summary>Pista 1 — El diccionario Morse como arreglo paralelo</summary>

Si tu lenguaje no tiene diccionarios/mapas, puedes usar dos arreglos paralelos: uno con las letras y otro con los códigos. Para buscar, recorre el arreglo de letras hasta encontrar la que buscas y devuelve el elemento en la misma posición del arreglo de códigos.

</details>

<details>
<summary>Pista 2 — Dividir la cadena Morse</summary>

Para `morse_a_texto`, necesitas dividir el string por `/` primero (obtienes palabras), y luego cada palabra por espacios simples (obtienes códigos individuales). Si tu lenguaje no tiene `split`, recorre carácter a carácter y acumula en buffers.

</details>

---

## ⭐ Reto Extra

La agencia quiere una función `frecuencia_en_morse(texto)` que analice el texto dado y reporte: ¿cuántos puntos (`.`) y cuántos guiones (`-`) tiene su versión Morse? ¿Cuál es el carácter más "costoso" en transmisión (el que genera más símbolos)? Esto era importante en la era del telégrafo para optimizar el tiempo de transmisión.

# 🧬 Reto 05 — El Clasificador de ADN

**Nivel:** 🔥 Lógica Avanzada | **Dificultad:** 🔴 Muy Difícil

---

## 🎯 Historia

La **Doctora Genética Quiroga** trabaja en un laboratorio que analiza secuencias de ADN. El ADN está compuesto de 4 bases nitrogenadas: **A** (adenina), **T** (timina), **G** (guanina) y **C** (citosina).

El laboratorio necesita un sistema automatizado que analice secuencias de ADN y:
1. **Valide** que la secuencia solo contenga los caracteres A, T, G, C
2. **Cuente** la frecuencia de cada base
3. **Encuentre** el par complementario (A↔T, G↔C)
4. **Detecte** secuencias palindrómicas de ADN (importantes biológicamente)
5. **Identifique** patrones repetidos
6. **Clasifique** la secuencia por su contenido GC (porcentaje de G+C)

---

## 📋 Las Reglas del ADN

**Complemento de bases:** A es complemento de T, G es complemento de C
- La cadena complementaria invierte la secuencia Y cambia cada base por su complemento
- Ejemplo: `ATCG` → complemento → `CGAT` (primero complementa: TAGC, luego invierte: CGAT)

**Palíndromo de ADN:** Una secuencia es palíndroma si es igual a su cadena complementaria
- Ejemplo: `GAATTC` → complementaria: `GAATTC` → ¡EsTa es palíndroma!

**Contenido GC:**
- < 40% → "Bajo contenido GC"
- 40-60% → "Contenido normal"
- > 60% → "Alto contenido GC"

**Patrón repetido:** Una subcadena de longitud M que aparece 3 o más veces consecutivamente

---

## 📋 Las Funciones

| Función | Retorna |
|---------|---------|
| `validar_secuencia(adn)` | (valida, posicion_error) |
| `contar_bases(adn)` | (cant_A, cant_T, cant_G, cant_C) |
| `complemento(adn)` | string con la cadena complementaria |
| `es_palindromo_adn(adn)` | booleano |
| `contenido_gc(adn)` | porcentaje y clasificación |
| `buscar_patron(adn, patron)` | lista de posiciones donde aparece el patrón |
| `encontrar_repetidos(adn, longitud_m)` | lista de subcadenas que se repiten 3+ veces |
| `reporte_adn(adn)` | genera el análisis completo |

---

## 🧪 Casos de Prueba

### Caso 1 — Secuencia válida y análisis completo
```
adn = "GAATTCGAATTC"

validar_secuencia("GAATTCGAATTC") → (válida, sin error)

contar_bases:
A=4, T=4, G=2, C=2

complemento("GAATTCGAATTC"):
Paso 1 - complementar: CTTAAGCTTAAG
Paso 2 - invertir: GAATTCGAATTC  ← ¡igual a la original!

es_palindromo_adn → ✅ VERDADERO (GAATTC es un sitio de restricción EcoRI)

contenido_gc: (2+2)/12 = 33.3% → Bajo contenido GC

buscar_patron("GAATTCGAATTC", "GAATTC"):
- Aparece en posición 0 y posición 6

encontrar_repetidos("GAATTCGAATTC", 3):
- "GAA" aparece en pos 0 y 6 (no 3 veces seguidas)
- "AAT" aparece en pos 1 y 7 (no 3 veces seguidas)
```

### Caso 2 — Secuencia inválida
```
adn = "ATCGXATC"

validar_secuencia → ❌ INVÁLIDA: carácter 'X' en posición 4
```

### Caso 3 — Repetidos
```
adn = "ATAATAATA"

buscar_patron("ATAATAATA", "ATA"):
- Posiciones: 0, 3, 6

encontrar_repetidos("ATAATAATA", 3):
- "ATA" se repite 3 veces en posiciones [0, 3, 6] ← REPETICIÓN DETECTADA
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda con `reto_05_diagramas.[png|pdf]`.

**Lista de verificación:**
- [ ] `validar_secuencia`: ciclo que verifica que cada carácter esté en {A,T,G,C}
- [ ] `contar_bases`: ciclo que incrementa el conteo según el carácter
- [ ] `complemento`: ciclo que reemplaza cada base por su complemento, luego invierte
- [ ] `es_palindromo_adn`: llama a `complemento` y compara con el original
- [ ] `contenido_gc`: cuenta G+C, calcula porcentaje, clasifica
- [ ] `buscar_patron`: ciclo que compara subcadenas de longitud igual al patrón
- [ ] `encontrar_repetidos`: para cada longitud M, busca subcadenas que aparezcan 3+ veces
- [ ] `reporte_adn`: orquesta todas las funciones

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
<summary>Pista 1 — La cadena complementaria</summary>

Para complementar: recorre la cadena carácter a carácter y reemplaza: A→T, T→A, G→C, C→G. Para invertir: recorre de atrás hacia adelante (del último carácter al primero).

</details>

<details>
<summary>Pista 2 — Buscar un patrón</summary>

Usa una "ventana deslizante": recorre el ADN con un índice `i`. En cada posición, verifica si los próximos `len(patron)` caracteres coinciden con el patrón. Si sí → guarda la posición.

</details>

<details>
<summary>Pista 3 — Los palíndromos de ADN</summary>

Recuerda que en biología, el palíndromo de ADN no es el mismo concepto que el palíndromo matemático. El ADN es palíndromo si la cadena es igual a su **complemento invertido** (no a su propia inversa). Ejemplo: GAATTC → complemento: CTTAAG → invertido: GAATTC ✅

</details>

---

## ⭐ Reto Extra

La Dra. Quiroga quiere identificar **sitios de restricción** conocidos. Un sitio de restricción es una secuencia específica que las enzimas de restricción cortan. Agrega una lista de sitios conocidos (ej: GAATTC→EcoRI, AAGCTT→HindIII, GGATCC→BamHI) y busca cuáles aparecen en la secuencia analizada y en qué posiciones.

# 🗳️ Reto 02 — El Sistema de Votación

**Nivel:** 🔥 Lógica Avanzada | **Dificultad:** 🟠 Difícil

---

## 🎯 Historia

El pueblo de **Algoritmia** celebra elecciones para elegir su próximo alcalde. El sistema de votación tiene reglas muy específicas para garantizar la transparencia:

1. Cada votante tiene un **ID único** y puede votar exactamente **una vez**
2. El voto es por el nombre del candidato
3. Un voto es **inválido** si:
   - El votante ya votó antes (voto duplicado)
   - El candidato no está en la lista oficial
   - El ID del votante es inválido (no está en el padrón)
4. Al cerrar la votación, si ningún candidato tiene **más del 50%** de los votos válidos, hay **segunda vuelta** entre los 2 más votados
5. El sistema debe generar un **acta de escrutinio** detallada

---

## 📋 El Problema

Dado el padrón electoral, la lista de candidatos y los votos emitidos (en orden), simula el proceso completo y genera el acta.

---

## 🔢 Entradas

- **Padrón**: lista de IDs de votantes habilitados
- **Candidatos**: lista de nombres de candidatos
- **votos**: lista de pares (id_votante, candidato_votado)

## 📤 Salidas

- Conteo de votos por candidato
- Votos inválidos (con motivo)
- Porcentaje de participación
- Ganador (o anuncio de segunda vuelta)
- Acta de escrutinio completo

---

## 🧪 Caso de Prueba

### Configuración:
```
Padrón (10 votantes): [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
Candidatos: [Arístides, Bertha, Carmelo]
```

### Votos emitidos:
```
(101, Arístides)
(102, Bertha)
(103, Arístides)
(104, Carmelo)
(105, Arístides)
(102, Bertha)      ← INVÁLIDO: 102 ya votó
(106, Bertha)
(107, Arístides)
(999, Carmelo)     ← INVÁLIDO: ID 999 no está en el padrón
(108, Dionisio)    ← INVÁLIDO: Dionisio no es candidato
(109, Bertha)
(110, Carmelo)
```

### Salida esperada:
```
=== ACTA DE ESCRUTINIO — ELECCIONES DE ALGORITMIA ===

Votos válidos emitidos: 9

Resultados:
- Arístides: 4 votos (44.4%)  ██████████████
- Bertha:    3 votos (33.3%)  ██████████
- Carmelo:   2 votos (22.2%)  ███████

Participación: 10/10 votantes (100%)

Votos inválidos (3):
- Voto de 102 (Bertha): DUPLICADO — Ya había votado
- Voto de 999 (Carmelo): ID NO EN PADRÓN
- Voto de 108 (Dionisio): CANDIDATO NO REGISTRADO

⚠️ NINGÚN CANDIDATO SUPERA EL 50%
→ Segunda vuelta entre: ARÍSTIDES (44.4%) y BERTHA (33.3%)
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda con `reto_02_diagrama.[png|pdf]`.

**Sub-diagramas:**
1. `validar_voto(id, candidato, padron, candidatos, ya_votaron)` → (valido, motivo)
2. `contar_votos(votos_validos[], candidatos[])` → conteos[]
3. `determinar_ganador(conteos[], total_validos)` → ganador o segunda_vuelta
4. Diagrama principal: procesa cada voto, luego genera el acta

**Lista de verificación:**
- [ ] Lee el padrón, candidatos y votos
- [ ] Para cada voto: valida los 3 tipos de error posibles
- [ ] Lleva registro de quién ya votó (lista de IDs que ya votaron)
- [ ] Cuenta votos por candidato
- [ ] Calcula porcentajes
- [ ] Verifica si alguien supera el 50%
- [ ] Si no: identifica los 2 más votados para segunda vuelta
- [ ] Genera el acta completa

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
<summary>Pista 1 — Rastrear quién ya votó</summary>

Necesitas una lista `ya_votaron[]` que empieza vacía. Cuando un voto es válido, agrega el ID a esta lista. Antes de procesar cada voto, busca si el ID ya está en `ya_votaron`.

</details>

<details>
<summary>Pista 2 — Los dos más votados para segunda vuelta</summary>

Necesitas encontrar el primero y el segundo lugar. Recorre los conteos: guarda el máximo (primero) y el segundo máximo por separado. Si hay empate en el segundo lugar, todos los empatados van a segunda vuelta.

</details>

---

## ⭐ Reto Extra

Implementa la **segunda vuelta** como un proceso completo: los mismos votantes pueden volver a votar, pero ahora solo entre los 2 finalistas. Diseña el diagrama completo del proceso de segunda vuelta con sus propias validaciones.

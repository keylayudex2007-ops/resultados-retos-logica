# 🏦 Reto 04 — El Simulador de Banco

**Nivel:** 🔥 Lógica Avanzada | **Dificultad:** 🔴 Muy Difícil

---

## 🎯 Historia

El **Banco de los Algoritmos** necesita un sistema de gestión de cuentas. El banco tiene varios tipos de cuentas y un conjunto de reglas estrictas para las transacciones.

**Tipos de cuenta:**
- **Básica**: sin costo mensual, límite de retiro diario de $5,000, sin interés
- **Ahorro**: $50/mes de costo, no tiene límite de retiro diario, genera 0.5% de interés mensual sobre el saldo mínimo del mes
- **Negocio**: $200/mes, sin límite de retiro, genera 1% de interés mensual, permite sobregiro de hasta $10,000

**Reglas de transacciones:**
1. Depósito: siempre válido si el monto > 0
2. Retiro: válido si hay saldo suficiente (o dentro del sobregiro para cuentas Negocio)
3. Transferencia: retiro de origen + depósito en destino (atomico: si el retiro falla, no se hace el depósito)
4. Cierre de mes: aplica costo mensual y calcula intereses

---

## 📋 El Problema

Simula una secuencia de operaciones bancarias y genera el estado de todas las cuentas al final.

---

## 🔢 Entradas

- Lista de cuentas iniciales (número, tipo, saldo inicial, propietario)
- Lista de operaciones:
  - `DEPOSITO [cuenta] [monto]`
  - `RETIRO [cuenta] [monto]`
  - `TRANSFERENCIA [cuenta_origen] [cuenta_destino] [monto]`
  - `CIERRE_MES`

## 📤 Salidas

- Resultado de cada operación (éxito o falla con motivo)
- Estado final de cada cuenta (saldo y historial del mes)

---

## 🧪 Caso de Prueba

### Cuentas iniciales:
```
001 - Básica   - $10,000 - Ana Torres
002 - Ahorro   - $50,000 - Bruno Reyes
003 - Negocio  - $5,000  - Carmela Inc.
```

### Operaciones:
```
DEPOSITO 001 2000
RETIRO 001 6000          ← excede límite diario de $5,000 básica
RETIRO 001 4000          ← OK (dentro del límite de básica)
TRANSFERENCIA 002 001 20000
RETIRO 003 12000         ← OK (sobregiro de Negocio cubre)
CIERRE_MES
```

### Salida esperada:
```
✅ DEPOSITO 001 $2,000   → Saldo: $12,000
❌ RETIRO 001 $6,000     → RECHAZADO: supera límite diario (básica: max $5,000/día)
✅ RETIRO 001 $4,000     → Saldo: $8,000
✅ TRANSFERENCIA 002→001 $20,000
   Ana Torres recibe $20,000 → Saldo: $28,000
   Bruno Reyes retira $20,000 → Saldo: $30,000
✅ RETIRO 003 $12,000    → Saldo: -$7,000 (sobregiro activo)

=== CIERRE DE MES ===
001 (Básica):   $28,000 → $28,000     (sin costo, sin interés)
002 (Ahorro):   $30,000 → $29,650     (−$50 costo + interés $0.5%)
    Saldo mínimo del mes: $30,000 → interés: $150
    Nuevo saldo: $30,000 - $50 + $150 = $30,100 ... [recalcular]
003 (Negocio):  -$7,000 → -$7,230     (−$200 costo + 1% interés sobre saldo positive si hay)
```

---

## 📐 Fase 1 — Tu Diagrama de Flujo

> ✏️ **Dibuja aquí tu diagrama de flujo antes de escribir código.**
>
> Guarda con `reto_04_diagrama.[png|pdf]`.

**Sub-diagramas:**
1. `procesar_deposito(cuenta, monto)`
2. `procesar_retiro(cuenta, monto, fecha)` — considera límites por tipo
3. `procesar_transferencia(origen, destino, monto)`
4. `cierre_de_mes(cuentas[])` — aplica costos e intereses a todas las cuentas
5. Diagrama principal: ciclo de operaciones

**Lista de verificación:**
- [ ] Cada cuenta tiene: número, tipo, saldo, propietario, retiro_hoy, saldo_minimo_mes
- [ ] Deposito: valida monto > 0, agrega al saldo, registra en historial
- [ ] Retiro: verifica tipo → aplica reglas del tipo, verifica saldo, descuenta
- [ ] Transferencia: intenta el retiro primero → si OK, hace el depósito; si falla → nada
- [ ] Cierre de mes: para cada cuenta aplica costo mensual y calcula interés
- [ ] Resetea el `retiro_hoy` a 0 en el cierre de mes
- [ ] Actualiza el `saldo_minimo_mes`

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
<summary>Pista 1 — El límite de retiro diario</summary>

Para la cuenta Básica, necesitas rastrear cuánto se ha retirado HOY. Usa una variable `retirado_hoy` por cuenta. Si un retiro haría que `retirado_hoy > 5000`, recházalo. Al cierre de mes, resetea `retirado_hoy = 0`.

</details>

<details>
<summary>Pista 2 — El saldo mínimo del mes (para interés de ahorro)</summary>

El saldo mínimo del mes es el menor saldo que tuvo la cuenta en algún momento durante el mes. Después de cada operación, verifica si el saldo actual es menor que el `saldo_minimo_mes` y actualízalo si es así.

</details>

---

## ⭐ Reto Extra

El banco quiere implementar un sistema de **alertas automáticas**: si una cuenta de ahorro tiene menos de $1,000 al cierre del mes, envía alerta "SALDO BAJO". Si una cuenta de negocio lleva más de $5,000 en sobregiro, envía alerta "SOBREGIRO CRÍTICO". Agrega estas verificaciones al cierre de mes.

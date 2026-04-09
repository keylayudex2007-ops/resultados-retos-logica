# calculo_descuentos.py

def calcular_precio_final(monto_compra, es_vip):
    """
    Calcula el descuento aplicable y el precio final de una compra.
    """
    porcentaje_descuento = 0

    # --- VALIDACIÓN DE MONTO ---
    if monto_compra > 500000:
        # Evaluar categoría VIP (Nivel Alto)
        if es_vip:
            porcentaje_descuento = 0.30  # 30%
        else:
            porcentaje_descuento = 0.20  # 20%
    else:
        # Evaluar categoría VIP (Nivel Base)
        if es_vip:
            porcentaje_descuento = 0.10  # 10%
        else:
            porcentaje_descuento = 0.00  # Sin Descuento

    # --- PROCESO DE CIERRE ---
    descuento_total = monto_compra * porcentaje_descuento
    precio_final = monto_compra - descuento_total

    return {
        "monto_original": monto_compra,
        "porcentaje": f"{int(porcentaje_descuento * 100)}%",
        "ahorro": descuento_total,
        "precio_final": precio_final
    }

# --- PRUEBA DEL SISTEMA ---
if __name__ == "__main__":
    compras = [
        {"monto": 600000, "vip": True,  "desc": "Compra Alta + VIP"},
        {"monto": 600000, "vip": False, "desc": "Compra Alta No VIP"},
        {"monto": 300000, "vip": True,  "desc": "Compra Base + VIP"},
        {"monto": 300000, "vip": False, "desc": "Compra Base No VIP"}
    ]

    print("=== RECIBO DE COMPRA ===")
    for c in compras:
        res = calcular_precio_final(c["monto"], c["vip"])
        print(f"Escenario: {c['desc']}")
        print(f" - Monto: ${res['monto_original']:,}")
        print(f" - Descuento: {res['porcentaje']} (-${res['ahorro']:,})")
        print(f" - TOTAL A PAGAR: ${res['precio_final']:,}")
        print("-" * 30)

    print("Fin del proceso.")
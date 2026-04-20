def calcular_cambio():
    precio = int(input("Precio del producto: "))
    pago = int(input("Monto pagado: "))
    
    cambio = pago - precio
    
    if cambio == 0:
        print("No hay cambio, el pago es exacto.")
    elif cambio < 0:
        print("Falta dinero para completar el pago.")
    else:
        print(f"Cambio total: ${cambio}")
        denominaciones = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        resultado = []

        for d in denominaciones:
            piezas = cambio // d
            if piezas > 0:
                resultado.append(f"{piezas} de ${d}")
                cambio -= piezas * d

        print("\nEntregar:")
        for item in resultado:
            print(item)

calcular_cambio()
     
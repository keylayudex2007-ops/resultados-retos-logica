import random
def juego_adivinanza():
    # 1. INICIO E INICIALIZACIÓN
    secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    historial = [] # Lista vacía para el historial
    
    print("--- Bienvenido al Juego de Adivinanza ---")
    print("He pensado un número entre 1 y 100. Tienes 7 intentos.")

    # 2. CICLO DE JUEGO (Máx 7 intentos)
    while intentos < 7 and adivinado == False:
        try:
            intento_jugador = int(input(f"\nIntento {intentos + 1} - Ingresa tu número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
            
        intentos += 1
        
        # Comparación
        if intento_jugador == secreto:
            adivinado = True
            historial.append(f"Intento {intentos}: {intento_jugador} - ¡Correcto!")
        elif intento_jugador < secreto:
            print("Más alto")
            historial.append(f"Intento {intentos}: {intento_jugador} - Más alto")
        else:
            print("Más bajo")
            historial.append(f"Intento {intentos}: {intento_jugador} - Más bajo")

    # 3. SALIDA DEL CICLO Y RESULTADOS
    if adivinado:
        print(f"\n¡Correcto! Adivinaste en {intentos} intentos.")
        if intentos <= 3:
            print("¡Genio! Usaste búsqueda binaria perfecta.")
    else:
        print(f"\n¡Perdiste! El número era {secreto}.")
        print("Mensaje de búsqueda binaria: Con 7 intentos siempre deberías poder ganar si usas la estrategia correcta.")

    # 4. FINAL: Imprimir Historial
    print("\n--- Historial de Intentos ---")
    for registro in historial:
        print(registro)

# Ejecutar el juego
juego_adivinanza()
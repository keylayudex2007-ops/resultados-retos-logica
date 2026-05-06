# --- Prepracion ---
secreto = random.randint(1, 100)
intentos_realizados = 0
adivinado = False
historial = "" # Usaremos un texto simple para el historial

print("Adivina el número (1-100). Tienes 7 intentos.")

# --- Ciclo (Límite de 7 intentos) ---
for i in range(1, 8):
    if adivinado == False:
        usuario = int(input(f"Intento {i}: "))
        intentos_realizados = i
        
        # --- Comparar ---
        if usuario < secreto:
            respuesta = "Más alto"
            print(respuesta)
            historial += f"Intento {i}: {usuario} -> {respuesta}\n"
            
        elif usuario > secreto:
            respuesta = "Más bajo"
            print(respuesta)
            historial += f"Intento {i}: {usuario} -> {respuesta}\n"
            
        else:
            respuesta = "¡Correcto!"
            print(respuesta)
            adivinado = True
            historial += f"Intento {i}: {usuario} -> {respuesta}\n"

# --- Resultado final (Fuera del ciclo) ---
if adivinado == True:
    if intentos_realizados <= 3:
        print("¡MENSAJE DE GENIO!")
    else:
        print("Mensaje de éxito normal.")
else:
    print(f"¡PERDISTE! El número era {secreto}. Mi abuela adivina mejor...")

# --- Mostrar Historial ---
print("\n--- HISTORIAL ---")
print(historial)
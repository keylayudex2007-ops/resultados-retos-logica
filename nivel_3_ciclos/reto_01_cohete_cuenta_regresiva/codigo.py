# --- Preparar: Inicialización de variables ---
racha = 0
abortado = False

# Usamos range(inicio, fin, paso) para ir de 10 a 0
for contador in range(10, -1, -1):
    
    # --- EsPar: ¿Es par? ---
    if contador % 2 == 0:
        racha += 1
        
        # --- pruebaAborto: ¿Racha igual a 3? ---
        if racha == 3:
            print(f"[{contador}] ¡ABORTAR LANZAMIENTO!")
            abortado = True
            break  
    else:
        # --- ReiniciarRacha ---
        racha = 0

    # --- MirarMensajes: Mensajes especiales según el número ---
    mensajes = {
        7: "Revision de sistemas + pausa",
        5: "punto de no retorno",
        3: "Ignición encendida"
    }

    if contador in mensajes:
        print(f"[{contador}] {mensajes[contador]}")
    else:
        print(f"[{contador}]")

# --- Despegue ---
if not abortado:
    print("\n🚀 ¡DESPEGUE!")
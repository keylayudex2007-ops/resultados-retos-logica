# --- Variables ---
nivel = 0
manguera = 500
fuga = 80
CAPACIDAD_MAXIMA = 5000
nivel_anterior = 0

# Ponemos un límite de tiempo razonable para evitar errores
for minuto in range(1, 101):
    
    # Llenado por minuto: lo que entra menos lo que se escapa
    nivel += (manguera - fuga)
    
    # Cada 10 minutos hacemos el chequeo
    if minuto % 10 == 0:
        print(f"Minuto {minuto}: {nivel} litros")
        
        # Si el nivel es menor que hace 10 minutos, abrimos más el grifo
        if nivel < nivel_anterior:
            manguera += 50
            print(f"Aumentando manguera a {manguera} L/min")
       
     # Si el nivel es mayor o igual, mantenemos el mismo caudal
        nivel_anterior = nivel
     
    # Si ya se llenó el tanque, paramos el proceso
    if nivel >= CAPACIDAD_MAXIMA:
        tiempo_total = minuto
        break

# --- Resultados ---
print("\n--- OPERACIÓN TERMINADA ---")
print(f"Tiempo total: {tiempo_total} minutos")
print(f"Nivel final: {nivel} litros")
print(f"Caudal final: {manguera} L/min")
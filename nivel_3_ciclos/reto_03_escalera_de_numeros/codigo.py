# --- Entrada de datos ---
n = int(input("Introduce la altura (N): "))

# --- Dibujar la pirámide invertida ---
for fila in range(n, 0, -1):
    
    # Creamos la hilera de estrellas multiplicando el símbolo por el número de fila
    estrellas = "* " * fila
    
    # Calculamos el número de fila actual para el texto (de 1 hasta N)
    numero_fila = n - fila + 1
    
    print(f"Fila {numero_fila}: {estrellas}")

# --- Fin ---
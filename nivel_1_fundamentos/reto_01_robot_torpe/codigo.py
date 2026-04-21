# Robot torpe
n = int(input("cuantas intrucciones se van a ingresar: "))

# Inicializamos los contadores
pasos_totales = 0
giros_derecha = 0
giros_izquierda = 0

for i in range(n):
    instruccion = input(f"ingrese la instruccion {i+1}: ").lower()
    if instruccion == "paso":
        pasos_totales += 1
    elif instruccion == "giro derecha":
        giros_derecha += 1
    elif instruccion == "giro izquierda":
        giros_izquierda += 1
    else:
        print("instruccion no valida")

# Imprimimos los resultados
print("pasos totales:", pasos_totales)
print("giros a la derecha:", giros_derecha)
print("giros a la izquierda:", giros_izquierda)


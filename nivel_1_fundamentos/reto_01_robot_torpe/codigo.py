# Robot torpe
n = int(input("cuantas intrucciones se van a ingresar: "))

# Inicializamos los contadores
pasos_totales = 0
giros_derecha = 0
giros_izquierda = 0
i = 1

while i <= n:
    instruccion = input("ingrese la instruccion: ").lower()
    if instruccion == "paso":
        pasos_totales += 1
    elif instruccion == "giro derecha":
        giros_derecha += 1
    elif instruccion == "giro izquierda":
        giros_izquierda += 1
    else:
        print("instruccion no valida")
    i += 1

# Imprimimos los resultados
print("pasos totales:", pasos_totales)
print("giros a la derecha:", giros_derecha)
print("giros a la izquierda:", giros_izquierda)


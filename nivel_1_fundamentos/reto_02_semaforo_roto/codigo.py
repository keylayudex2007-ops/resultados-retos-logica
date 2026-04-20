# semaforo roto
def semaforo_roto( ):
    # leer valores
    verde = int(input("tiempo en verde: "))
    amarillo = int(input("tiempo en amarillo: "))
    rojo = int(input("tiempo en rojo: "))
    # calcular ciclo y vueltas
    ciclo = verde + amarillo + rojo
    vueltas = 28800 // ciclo
    sobras = 28800 % ciclo

    print(f"vueltas: {vueltas} sobras: {sobras}")
    # determinar posicion del semaforo
    posicion = 2700 % ciclo
    fase = "VERDE"
    if posicion < verde:
        fase = "VERDE"
    elif posicion < verde + amarillo:
        fase = "AMARILLO"
    else:
        fase = "ROJO"
    
    #Imprimer resultado final
    print(f"El semáforo se encuentra en la fase: {fase}")
    
    semaforo_roto()
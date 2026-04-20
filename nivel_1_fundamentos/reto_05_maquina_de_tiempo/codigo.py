def maquina_del_tiempo():
    # 1. INICIO E INICIALIZACIÓN
    print("--- Bienvenido a la Máquina del Tiempo ---")
    
    # Leer datos básicos
    anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
    anio_actual = int(input("Ingresa el año actual: "))
    
    # Calcular y mostrar edad actual
    edad_actual = anio_actual - anio_nacimiento
    print(f"Tu edad actual es: {edad_actual} años")
    
    # 2. LÓGICA DE CONSULTA
    anio_consulta = int(input("\n¿A qué año quieres viajar?: "))
    
    # CASO 1: El año de consulta es en el PASADO (MENOR al actual)
    if anio_consulta < anio_actual:
        # ¿Ya habías nacido?
        if anio_consulta >= anio_nacimiento:
            edad_pasada = anio_consulta - anio_nacimiento
            print(f"En el año {anio_consulta} tenías {edad_pasada} años.")
        else:
            print(f"En el año {anio_consulta} aún no habías nacido.")
            
    # CASO 2: El año de consulta es el PRESENTE o FUTURO
    else:
        # Subcaso 2.1: El año es el PRESENTE
        if anio_consulta == anio_actual:
            print(f"El año consultado es el presente: tienes {edad_actual} años.")
            
        # Subcaso 2.2: El año es el FUTURO
        else:
            edad_futura = anio_consulta - anio_nacimiento
            print(f"En el año {anio_consulta} tendrás {edad_futura} años.")

maquina_del_tiempo()
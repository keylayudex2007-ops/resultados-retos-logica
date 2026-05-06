# --- Configuración inicial ---
n = int(input("Número de caracoles: "))
meta = int(input("Distancia de la meta (cm): "))

velocidades = []
for i in range(n):
    v = int(input(f"Velocidad caracol {i}: "))
    velocidades.append(v)

# Empezamos todos en posición 0
posiciones = [0] * n
ganador = None

# --- Simulación de la carrera ---
for turno in range(1, 501):  # Límite de 500 turnos por seguridad
    
    # Movimiento normal
    for i in range(n):
        posiciones[i] += velocidades[i]

    # Eventos especiales (Lluvia, Barro, Viento, Trampa)
    if turno % 3 == 0:
        posiciones = [p + 1 for p in posiciones]
        print(f"Turno {turno}: ¡Lluvia! (+1 a todos)")

    if turno % 5 == 0:
        lento = velocidades.index(min(velocidades))
        posiciones[lento] -= 2
        print(f"Turno {turno}: ¡Barro! (El más lento retrocede)")

    if turno % 7 == 0:
        lider = posiciones.index(max(posiciones))
        posiciones[lider] += 3
        print(f"Turno {turno}: ¡Viento! (El líder avanza +3)")

    if turno % 11 == 0:
        colero = posiciones.index(min(posiciones))
        promedio = sum(posiciones) // n
        posiciones[colero] = promedio
        print(f"Turno {turno}: ¡Trampa! (El último salta al promedio)")

    # Verificación de ganador
    for i in range(n):
        if posiciones[i] >= meta:
            ganador = i
            break
    
    if ganador is not None:
        break

# --- Resultado final ---
print(f"\n🏆 GANADOR: Caracol {ganador} en el turno {turno}")
print(f"Posiciones finales: {posiciones}")
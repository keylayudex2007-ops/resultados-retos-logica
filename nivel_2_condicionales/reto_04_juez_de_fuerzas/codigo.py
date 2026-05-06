# --- INICIO DEL TORNEO ---

# 1. Leer puntajes totales (Fuerza/Desempeño total acumulado)
total_fuerza_a = float(input("Escribe el total acumulado de A: "))
total_fuerza_b = float(input("Escribe el total acumulado de B: "))

# 2. Inicializar marcadores de rondas
puntos_a = 0
puntos_b = 0

# --- PRUEBAS (Simulando 3 rondas) ---
for i in range(1, 4):
    print(f"\n--- Prueba {i} ---")
    ganador = input(f"¿Quién ganó la Prueba {i}? (A/B/EMPATE): ").strip().upper()
    
    if ganador == "A":
        puntos_a += 1
    elif ganador == "B":
        puntos_b += 1
    else:
        print("Empate en ronda: nadie suma puntos.")

# --- VEREDICTO FINAL ---
print("\n" + "Resultados:".center(30, "="))
print(f"Marcador final -> A: {puntos_a} | B: {puntos_b}")

# 1. Verificación de Campeón Absoluto
if puntos_a == 3 or puntos_b == 3:
    ganador_nombre = "A" if puntos_a == 3 else "B"
    print(f"🏆 CAMPEON ABSOLUTO: {ganador_nombre}")

# 2. Comparación de puntos (si no hubo absoluto)
elif puntos_a != puntos_b:
    ganador_nombre = "A" if puntos_a > puntos_b else "B"
    print(f"VEREDICTO: Gana {ganador_nombre} por mayoría de puntos.")

# 3. El Desempate (Si los puntos son iguales)
else:
    print("Empate en puntos... consultando fuerza total acumulada.")
    if total_fuerza_a != total_fuerza_b:
        ganador_nombre = "A" if total_fuerza_a > total_fuerza_b else "B"
        print(f"VEREDICTO: Gana {ganador_nombre} por suma de fuerza total.")
    else:
        print("🌌 EMPATE GALÁCTICO: ¡Son exactamente iguales!")

print("="*30)
# gestion_compuertas.py

def gestionar_compuertas(nivel, velocidad):
    """
    Controla el estado de las compuertas y alarmas según el nivel y velocidad.
    Variables:
    - nivel (int/float): Metros.
    - velocidad (str): "Alta", "Media" o "Baja".
    """
    estado_compuerta_a = "Cerrada"
    estado_compuerta_b = "Cerrada"
    alarma_general = "Apagada"

    # --- VALIDACIÓN DE EMERGENCIA (NIVEL CRÍTICO) ---
    if nivel > 120:
        estado_compuerta_a = "Abierta"
        estado_compuerta_b = "Abierta"
        alarma_general = "ACTIVA"
        mensaje = "EMERGENCIA: Nivel crítico superado."

    # --- VALIDACIÓN PREVENTIVA ---
    elif nivel > 100:
        alarma_general = "Apagada"
        
        if velocidad == "Alta":
            estado_compuerta_a = "Abierta"
            mensaje = "PREVENTIVO: Nivel alto, velocidad alta."
        elif velocidad == "Media":
            estado_compuerta_b = "Abierta"
            mensaje = "PREVENTIVO: Nivel alto, velocidad media."
        else:
            mensaje = "PREVENTIVO: Nivel alto, velocidad baja. Sin apertura."
            
    # --- NIVEL NORMAL ---
    else:
        mensaje = "ESTADO NORMAL: Niveles bajo control."

    return {
        "Compuerta A": estado_compuerta_a,
        "Compuerta B": estado_compuerta_b,
        "Alarma": alarma_general,
        "Reporte": mensaje
    }

# --- SIMULACIÓN DE OPERACIONES ---
if __name__ == "__main__":
    escenarios = [
        (125, "Baja"),   # Emergencia (ignora velocidad)
        (110, "Alta"),   # Preventivo A
        (105, "Media"),  # Preventivo B
        (102, "Baja"),   # Preventivo sin apertura
        (80,  "Alta")    # Normal
    ]

    print(f"{'NIVEL':<8} | {'VELOC.':<8} | {'COMP. A':<10} | {'COMP. B':<10} | {'ALARMA':<8}")
    print("-" * 55)

    for n, v in escenarios:
        res = gestionar_compuertas(n, v)
        print(f"{n:<8} | {v:<8} | {res['Compuerta A']:<10} | {res['Compuerta B']:<10} | {res['Alarma']:<8}")

    print("\nResultado: Fin del proceso.")
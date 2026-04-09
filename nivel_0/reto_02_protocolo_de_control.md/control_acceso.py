# control_acceso.py

def control_acceso(fuga_gas, id_valida, traje_puesto):
    """
    Evalúa el protocolo de seguridad y acceso industrial.
    Retorna el estado de acceso y el motivo.
    """
    
    # --- VALIDACIÓN DE SEGURIDAD ---
    if fuga_gas:
        return "ACCESO DENEGADO - Motivo: Seguridad (Fuga de gas detectada)"

    # --- EVALUACIÓN DE CREDENCIALES Y EQUIPO ---
    if id_valida and traje_puesto:
        return "ACCESO AUTORIZADO - Bienvenido al área protegida"
    
    # --- ANÁLISIS DE FALLO (Si llega aquí es porque algo faltó) ---
    else:
        if id_valida:
            return "ACCESO DENEGADO - Motivo: Equipo Incompleto (Falta traje)"
        else:
            return "ACCESO DENEGADO - Motivo: Sin ID válida"

# --- SIMULACIÓN DE ESCENARIOS ---
if __name__ == "__main__":
    print("=== SISTEMA DE CONTROL DE ACCESO ===")
    
    escenarios = [
        # (FugaGas, ID_Valida, Traje)
        {"gas": True,  "id": True,  "traje": True,  "desc": "Emergencia total"},
        {"gas": False, "id": True,  "traje": True,  "desc": "Cumple todo"},
        {"gas": False, "id": True,  "traje": False, "desc": "Sin EPP"},
        {"gas": False, "id": False, "traje": True,  "desc": "Desconocido con traje"}
    ]

    for e in escenarios:
        resultado = control_acceso(e['gas'], e['id'], e['traje'])
        print(f"Escenario: {e['desc']}")
        print(f"Resultado: {resultado}")
        print("-" * 40)
    
    print("Estado Final: Fin del proceso.")
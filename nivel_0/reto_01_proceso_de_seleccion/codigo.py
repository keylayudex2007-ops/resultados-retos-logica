# codigo.py

def evaluar_candidato(datos):
    """
    Función que aplica la lógica de selección:
    1. Filtro de integridad.
    2. Evaluación por rutas técnicas y académicas.
    """
    
    # --- FILTRO DE INTEGRIDAD (OBLIGATORIO) ---
    if datos.get("faltas_eticas"):
        return "DESCARTADO: Faltas éticas"

    # --- EVALUACIÓN DE PERFILES ---
    
    # Ruta 1: Experiencia (> 5 años) Y Lenguaje (Python)
    cumple_ruta_1 = (datos.get("experiencia", 0) > 5 and 
                     "Python" in datos.get("lenguajes", []))
    
    # Ruta 2: Educación (Maestría) Y Idioma (Inglés)
    cumple_ruta_2 = (datos.get("educacion") == "Maestría" and 
                     datos.get("ingles") == True)

    # --- RESULTADO FINAL ---
    if cumple_ruta_1:
        return "PRE-SELECCIONADO: Ruta 1 (Experiencia/Python)"
    elif cumple_ruta_2:
        return "PRE-SELECCIONADO: Ruta 2 (Educación/Inglés)"
    else:
        return "NO SELECCIONADO: No cumple criterios de ruta"


# --- BLOQUE PRINCIPAL PARA EJECUCIÓN ---
if __name__ == "__main__":
    # Base de datos de ejemplo
    candidatos = [
        {
            "nombre": "Andrés",
            "faltas_eticas": False,
            "experiencia": 7,
            "lenguajes": ["Python", "JavaScript"],
            "educacion": "Grado",
            "ingles": False
        },
        {
            "nombre": "Beatriz",
            "faltas_eticas": False,
            "experiencia": 2,
            "lenguajes": ["Java"],
            "educacion": "Maestría",
            "ingles": True
        },
        {
            "nombre": "Claudio",
            "faltas_eticas": True,  # Candidato descartado automáticamente
            "experiencia": 10,
            "lenguajes": ["Python"],
            "educacion": "Maestría",
            "ingles": True
        },
        {
            "nombre": "Diana",
            "faltas_eticas": False,
            "experiencia": 3,
            "lenguajes": ["Python"],
            "educacion": "Grado",
            "ingles": True
        }
    ]

    print("=== RESULTADOS DEL PROCESO DE SELECCIÓN ===")
    for c in candidatos:
        resultado = evaluar_candidato(c)
        print(f"Candidato: {c['nombre']} -> {resultado}")
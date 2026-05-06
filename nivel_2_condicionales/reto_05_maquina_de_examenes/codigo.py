# --- INICIO ---

# 1. Entrada de datos
print("--- Sistema de Calificación Académica ---")
p1 = float(input("Promedio Parcial 1: "))
p2 = float(input("Promedio Parcial 2: "))
p3 = float(input("Promedio Parcial 3: "))
nota_final = float(input("Nota Examen Final: "))
asistencia = float(input("Porcentaje de Asistencia: "))
proyecto = input("¿Entregó el Proyecto? (SI/NO): ").strip().upper()

# 2. Calcular Promedio de Parciales
promedio_parciales = (p1 + p2 + p3) / 3
motivos_fallo = []

# --- VERIFICACIÓN DE CONDICIONES EN SECUENCIA ---

# Validamos cada requisito y guardamos los fallos si existen
if promedio_parciales < 55:
    motivos_fallo.append("Promedio de parciales insuficiente (< 55)")

if asistencia < 80:
    motivos_fallo.append("Asistencia insuficiente (< 80%)")

if proyecto != "SI":
    motivos_fallo.append("No entregó el proyecto")

# --- LÓGICA DE DECISIÓN ---

# Si ya hay fallos en los requisitos básicos (Parciales, Asistencia o Proyecto)
if motivos_fallo:
    print("\nRESULTADO: REPROBADO")
    print(f"Motivos: {', '.join(motivos_fallo)}")

else:
    # Si los básicos están OK, revisamos el Examen Final
    if nota_final >= 60:
        # APROBACIÓN NORMAL
        promedio_total = (promedio_parciales * 0.6) + (nota_final * 0.4) # Ejemplo de peso
        
        if promedio_total >= 90:
            print(f"\nRESULTADO: APROBADO CON DISTINCIÓN (Nota: {promedio_total:.1f})")
        elif promedio_total >= 70:
            print(f"\nRESULTADO: APROBADO (Nota: {promedio_total:.1f})")
        else:
            print(f"\nRESULTADO: APROBADO CON CONDICIÓN (Nota: 60)")
            
    else:
        # LÓGICA ESPECIAL: RECUPERACIÓN (El único fallo es el final)
        print("\nNota final insuficiente. Accediendo a recuperación...")
        nota_recup = float(input("Introduce Nota de Recuperación: "))
        
        if nota_recup >= 70:
            print("\nRESULTADO: APROBADO CON CONDICIÓN")
            print("Nota fija registrada: 60")
        else:
            print("\nRESULTADO: REPROBADO")
            print("Motivo: Falló examen final y recuperación.")

# --- FIN ---
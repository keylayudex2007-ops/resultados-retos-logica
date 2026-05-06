# 🤥 DETECTOR DE MENTIRAS - RETO 01

# --- INICIO DEL INTERROGATORIO ---
# 1. Definir respuestas correctas (puedes cambiarlas para pruebas)
correcta1 = "SI"
correcta2 = "NO"
correcta3 = "SI"

# 2. Obtener respuestas del sospechoso (Entrada)
print("--- Detector de Mentiras ---")
respuesta1 = input("Respuesta 1 (SI/NO): ").strip().upper()
respuesta2 = input("Respuesta 2 (SI/NO): ").strip().upper()
respuesta3 = input("Respuesta 3 (SI/NO): ").strip().upper()

# 3. Contador de errores
errores = 0

# --- ZONA DE CONTEO ---
if respuesta1 != correcta1:
    errores = errores + 1

if respuesta2 != correcta2:
    errores = errores + 1

if respuesta3 != correcta3:
    errores = errores + 1

# --- ZONA DE VEREDICTO (La Tabla de la verdad) ---
if errores == 0:
    resultado = "Sin inconsistencias."
elif errores == 1:
    resultado = "Posible estrés."
elif errores == 2:
    resultado = "Alta probabilidad de engaño."
else:
    resultado = "Sospechoso confirma mentira."

# --- SALIDA FINAL ---
print(f"\nVeredicto: {resultado}")

# --- ZONA DE ALERTA FINAL ---
if respuesta1 != correcta1:
    print("⚠️ ALERTA: Inconsistencia en pregunta clave.")
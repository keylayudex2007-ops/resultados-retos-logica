# --- INICIO ---

#  Inicialización de variables
caudal = 0
longitud = 0
c_caudal = ""
c_longitud = ""
imp_ecologica = ""

# Entrada de datos
print("--- Clasificación de Ecosistemas Acuáticos ---")
caudal = float(input("Escribe la velocidad del Caudal (m³/s): "))
longitud = float(input("Escribe la Longitud (km): "))

# --- CLASIFICACIÓN DEL CAUDAL (D, E, F, G) ---
if caudal < 10:
    c_caudal = "Arroyo"
elif 10 <= caudal < 100:
    c_caudal = "Río pequeño"
elif 100 <= caudal < 1000:
    c_caudal = "Río mediano"
elif caudal >= 1000:
    c_caudal = "Río grande"

# --- CLASIFICACIÓN DE LA LONGITUD (H, I, J) ---
if longitud < 50:
    c_longitud = "Corto"
elif 50 <= longitud < 500:
    c_longitud = "Mediano"
elif longitud >= 500:
    c_longitud = "Largo"

# --- DETERMINAR IMPORTANCIA ECOLÓGICA (K, L, M, N, O) ---
if c_caudal == "Río grande" and c_longitud == "Largo":
    imp_cologica = "Ecosistema Crítico 🔴"

elif c_caudal == "Río grande" and c_longitud == "Mediano":
    imp_cologica = "Alta importancia 🟠"

elif c_caudal == "Río mediano" and c_longitud == "Largo":
    imp_cologica = "Alta importancia 🟠"

elif c_caudal == "Río grande" or c_caudal == "Río mediano":
    imp_cologica = "Importancia media 🟡"

elif c_caudal == "Arroyo" or c_caudal == "Río pequeño":
    imp_cologica = "Importancia baja 🟢"

# --- P. SALIDA DE RESULTADOS ---
print("\n" + "="*40)
print(f"Clasificación Caudal: {c_caudal}")
print(f"Clasificación Longitud: {c_longitud}")
print(f"Importancia ecológica: {imp_cologica}")
print("="*40)
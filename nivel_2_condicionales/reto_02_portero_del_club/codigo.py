# --- INICIO VERIFICACIÓN ---

print("--- Control de Acceso ---")

# Entradas (Leemos los datos)
# Nota: Para los "Si/No" usamos comparaciones booleanas (True/False)
edad = int(input("Introduce la edad: "))
es_vip = input("¿Es Miembro VIP? (SI/NO): ").strip().upper() == "SI"
tiene_id = input("¿Tiene ID física? (SI/NO): ").strip().upper() == "SI"
en_lista_o_pago = input("¿Está en lista o ya pagó? (SI/NO): ").strip().upper() == "SI"
acompanante_ok = input("¿Acompañante cumple las reglas? (SI/NO): ").strip().upper() == "SI"

# --- LÓGICA DE VALIDACIÓN (Siguiendo el Diagrama) ---

if edad < 18:
    print("RESULTADO: NO ENTRA - Menor de edad")
else:
    # Si llegó aquí, es mayor de edad (Edad >= 18)
    if es_vip:
        print("RESULTADO: ENTRA - Miembro VIP con edad válida")
    else:
        # No es VIP, seguimos validando
        if not tiene_id:
            print("RESULTADO: NO ENTRA - Sin identificación")
        else:
            # Tiene ID, revisamos acceso
            if not en_lista_o_pago:
                print("RESULTADO: NO ENTRA - Sin lista ni pago")
            else:
                # Revisamos acompañante
                if not acompanante_ok:
                    print("RESULTADO: NO ENTRA - Acompañante problemático")
                else:
                    print("RESULTADO: ENTRA - Cumple todo")

# --- FIN --- VERIFICACIÓN ---
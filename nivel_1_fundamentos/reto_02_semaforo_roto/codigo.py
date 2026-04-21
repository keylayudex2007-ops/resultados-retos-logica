# semaforo roto
# leer valores
verde = int(input("tiempo en verde: "))
amarillo = int(input("tiempo en amarillo: "))
rojo = int(input("tiempo en rojo: "))

ciclo = verde + amarillo + rojo
vueltas = 28800 // ciclo
sobras = 28800 % ciclo

print(f"vueltas: {vueltas} sobras: {sobras}")

posicion = 2700 % ciclo

if posicion < verde:
    fase = "VERDE"
elif posicion < (verde + amarillo):
    fase = "AMARILLO"
else:
    fase = "ROJO"

print(f"El semáforo se encuentra en la fase: {fase}")
```mermaid
flowchart TD
    Inicio([Inicio]) --> Leer[/Leer: v, a, r/]
    Leer --> Suma[ciclo = v + a + r]
    Suma --> Calc[vueltas = 28800 / ciclo]
    Calc --> Sobra[sobra = 28800 % ciclo]
    
    Sobra --> Mostrar[/Mostrar: vueltas, sobra/]
    
    # La posición actual depende del residuo (sobra)
    Mostrar --> PuntoControl[posicion = 2700 % ciclo]
    
    PuntoControl --> EsVerde{¿posicion < v?}
    
    EsVerde -- Sí --> Verde[Fase: VERDE]
    EsVerde -- No --> CalcLimite[Limite_Amarillo = v + a]
    
    CalcLimite --> EsAmarillo{¿posicion < Limite_Amarillo?}
    
    EsAmarillo -- Sí --> Amarillo[Fase: AMARILLO]
    EsAmarillo -- No --> Rojo[Fase: ROJO]
    
    Verde --> Fin([Fin])
    Amarillo --> Fin
    Rojo --> Fin
``` 
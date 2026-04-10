```mermaid
graph TD
    A([INICIO]) --> B[Inicializar Contadores:<br/>pasosTotales = 0<br/>girosIzquierda = 0<br/>girosDerecha = 0]
    B --> C[/Leer N<br/>total instrucciones/]
    C --> D{¿i <= N?}
    
    D -- Sí --> E[/Leer Instrucción i/]
    
    E --> F{¿Contiene<br/>'AVANZA'? }
    
    F -- Sí --> G[Extraer valor X<br/>pasosTotales += X]
    F -- No --> H{¿Es<br/>'GIRA DERECHA'?}
    
    H -- Sí --> I[girosDerecha += 1]
    H -- No --> J[girosIzquierda += 1]
    
    G & I & J --> K[i = i + 1]
    K --> D
    
    D -- No --> L[/Mostrar:<br/>pasosTotales<br/>girosIzquierda<br/>girosDerecha/]
    L --> M([FIN])
```
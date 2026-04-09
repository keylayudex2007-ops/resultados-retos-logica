```mermaid
graph TD
    A([Inicio]) --> B{¿Nivel > 120m?}
    B -- Sí --> C[Abrir Comuerta A + B y Alarma General]
    B -- No --> D{¿Nivel > 100m?}
    D -- Sí --> E{¿Velocidad?}
    E -- Alta --> F[Abrir Comuerta A]
    E -- Media --> G[Abrir Comuerta B]
    E -- Baja --> H[Comuertas Cerradas]
    D -- No --> H
    C --> I([Fin])
    F --> I
    G --> I
    H --> I
```
```mermaid
graph TD
    %% --- Estilos para claridad ---
    classDef inicioFin fill:#f9f,stroke:#333,stroke-width:2px,color:black;
    classDef proceso fill:#e1f5fe,stroke:#0277bd,stroke-width:1px,color:black;
    classDef decision fill:#fff9c4,stroke:#fbc02d,stroke-width:1px,color:black;
    classDef entradaSalida fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px,color:black;

    %% --- 1. INICIO E INICIALIZACIÓN ---
    Start((INICIO)):::inicioFin --> ReadInputs[/"Leer anio_nacimiento\nLeer anio_actual\nLeer anio_consulta"/]:::entradaSalida
    ReadInputs --> CalcEdadActual[/"edad_actual =\nanio_actual - anio_nacimiento"/]:::proceso
    CalcEdadActual --> PrintEdadActual[/"Imprimir 'Edad actual: X años'"/]:::entradaSalida

    %% --- 2. LOGICA DE CONSULTA ---
    PrintEdadActual --> CompareQuery{"¿anio_consulta < anio_actual?"}:::decision

    %% CASO 1: Año consulta es en el PASADO (MENOR que el año actual)
    CompareQuery -- Sí (<) --> CheckBorn{"¿anio_consulta >= anio_nacimiento?"}:::decision
    
    CheckBorn -- Sí (>=) --> CalcEdadPast[/"edad_pasada =\nanio_consulta - anio_nacimiento"/]:::proceso
    CalcEdadPast --> PrintPast[/"Imprimir 'En el año X tenía Y años.'"/]:::entradaSalida
    PrintPast --> End

    CheckBorn -- No (<) --> PrintNotBorn[/"Imprimir 'En el año X aún no habías nacido.'"/]:::entradaSalida
    PrintNotBorn --> End

    %% CASO 2: Año consulta es el PRESENTE o FUTURO
    CompareQuery -- No (>=) --> CompareQueryFuture{"¿anio_consulta == anio_actual?"}:::decision

    %% Subcaso 2.1: Año consulta es el PRESENTE (IGUAL al año actual)
    CompareQueryFuture -- Sí (==) --> PrintPresent[/"Imprimir 'El año consultado es el año actual: X años.'"/]:::entradaSalida
    PrintPresent --> End

    %% Subcaso 2.2: Año consulta es el FUTURO (MAYOR que el año actual)
    CompareQueryFuture -- No (>) --> CalcEdadFuture[/"edad_futura =\nanio_consulta - anio_nacimiento"/]:::proceso
    CalcEdadFuture --> PrintFuture[/"Imprimir 'En el año X tendrá Y años.'"/]:::entradaSalida
    PrintFuture --> End

    %% --- 3. FINAL ---
    End((FIN)):::inicioFin
 ```
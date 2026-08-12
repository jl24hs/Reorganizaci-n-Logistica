# Ejemplo de diagrama por capas (datos genéricos de logística)

Este ejemplo usa datos ficticios solo para mostrar la técnica. Reemplazalo
por tus procesos reales una vez que tengas la planilla de inventario
completa.

## 1. Mapa macro de procesos (nivel Proceso)

Un solo diagrama, cajas grandes, sin detalle interno.

```mermaid
flowchart LR
    A[Recepción de Mercadería] --> B[Gestión de Inventario]
    B --> C[Gestión de Pedidos]
    C --> D[Distribución de Mercadería]
    D --> E[Devoluciones]
    E --> B
```

## 2. Diagrama de un procedimiento, con carriles por persona

Ejemplo del procedimiento "Carga de camión" (dentro del proceso
Distribución de Mercadería). Colores: 🟩 se hace / 🟥 debería hacerse
(falta) / 🟦 mejora futura.

```mermaid
flowchart TD
    subgraph Supervisor
        S1[Asignar camión a hoja de ruta]:::hace
    end
    subgraph Operario
        O1[Verificar bultos contra remito]:::hace
        O2[Escanear código de barras de cada bulto]:::falta
        O3[Cargar bultos al camión]:::hace
    end
    subgraph Chofer
        C1[Firmar remito de conformidad]:::hace
        C2[Registrar hora de salida]:::hace
    end
    subgraph "Sin responsable asignado"
        M1[Optimizar orden de entregas por zona]:::mejora
    end

    S1 --> O1 --> O2 --> O3 --> C1 --> C2
    S1 -.-> M1
    M1 -.-> O3

    classDef hace fill:#c6f6c9,stroke:#2f7a33,color:#000
    classDef falta fill:#f7c6c6,stroke:#a32f2f,color:#000
    classDef mejora fill:#c6d9f7,stroke:#2f4f7a,color:#000
```

### Lectura de este diagrama (lo que le mostrás a tu jefe/gerencia)

- El carril **Operario** tiene 3 tareas, una de ellas (🟥 escanear código
  de barras) no se hace hoy por falta de tiempo — y es la causa de
  diferencias de stock, un problema que sí se nota "río abajo".
- La caja 🟦 (optimizar rutas) no tiene carril propio porque **no hay
  nadie asignado** — ese es literalmente el hueco de un puesto nuevo
  (ej: un planificador de rutas o un rol de mejora continua).
- Con la planilla de inventario, esas dos cajas (🟥 y 🟦) tienen una
  cantidad de horas-persona/mes calculada, que es el número que sostiene
  el pedido de personal.

## Cómo replicarlo con tus datos

1. Completá `plantilla-inventario-tareas.csv` con tus procesos reales
   (aunque sea incompleto al principio, no importa — se va sumando).
2. Agrupá las filas por Proceso → armá el mapa macro (paso 1).
3. Agrupá por Procedimiento → armá un diagrama como el del paso 2 por
   cada uno, con un carril por persona/rol real de tu equipo.
4. Pintá cada caja según la columna "Estado" de la planilla.

# Organigrama de nivel 1 — Área LOG

Primer nivel del diagrama de flujo del área: Julián López conduce el
proceso macro de **Gestión de Tareas de LOG**, delegado en AB y RM, cada
uno a cargo de 5 bloques diarios (sus "macrotareas"). Este es el punto de
partida para seguir abriendo cada bloque en Procedimientos y Tareas.

Versión visual (con estado de relevamiento por bloque, coloreado):
ver el artifact publicado, o el diagrama Mermaid equivalente abajo.

```mermaid
flowchart TD
    JL[Julián López<br/>Jefe de Área] --> LOG[Gestión de Tareas de LOG<br/>proceso macro del área]
    JL --> AB[AB<br/>Ariel Bazán]
    JL --> RM[RM<br/>Rubén Moreyra]

    AB --> AB1[Lunes<br/>Falla de Tests]
    AB --> AB2[Martes<br/>Offline]
    AB --> AB3[Miércoles<br/>Redes]
    AB --> AB4[Jueves<br/>Chips]
    AB --> AB5[Viernes<br/>Stock]

    RM --> RM1[Lunes<br/>TOP10]
    RM --> RM2[Martes<br/>OS]
    RM --> RM3[Miércoles<br/>REE]
    RM --> RM4[Jueves<br/>Configuración]
    RM --> RM5[Viernes<br/>Red + Eventos]

    classDef doc fill:#c6d9f7,stroke:#1F5C8B,color:#000
    classDef parcial fill:#f3e3c2,stroke:#A96A1E,color:#000
    classDef vacio fill:#ffffff,stroke:#9AA7B0,stroke-dasharray: 4 3,color:#000

    class AB5,RM1 doc
    class AB1,AB2,AB4,RM2,RM3 parcial
    class AB3,RM4,RM5 vacio
```

## Estado de relevamiento por bloque (12/08/2026)

| Persona | Día | Bloque | Estado | Detalle |
|---|---|---|---|---|
| AB | Lunes | Falla de Tests | Parcial | 3 tareas relevadas |
| AB | Martes | Offline | Parcial | 2 tareas relevadas |
| AB | Miércoles | Redes | **Sin datos** | 5 procedimientos identificados (ISP, Telefonía IP, Red NCS, Cámaras, Impresoras), 0 tareas con detalle |
| AB | Jueves | Chips | Parcial | 4 tareas relevadas (aparecen como "Bloqueo/Desbloqueo de equipos" en el catálogo — confirmar si es lo mismo que "Chips") |
| AB | Viernes | Stock | Documentado | 16 tareas relevadas |
| RM | Lunes | TOP10 | Documentado | 11 pasos relevados (instructivo completo) |
| RM | Martes | OS (Órdenes de Servicio) | Parcial | 6 tareas relevadas |
| RM | Miércoles | REE (Remoto de Equipos) | Parcial | 6 tareas relevadas |
| RM | Jueves | Configuración | **Sin datos** | No aparece con ese nombre en el catálogo; candidatos a confirmar: Gestión de Chips (administrativo), Directivas técnicas |
| RM | Viernes | Red + Revisión de Eventos | **Sin datos** | 0 tareas relevadas |

Ninguno de estos números incluye tiempos ni objetivos confirmados — eso
es la siguiente capa a completar dentro de cada bloque (ver
`resumen-carga-horaria.md` y `plantilla-inventario-tareas.csv`).

## Próximo paso

Elegir uno de los 10 bloques y abrirlo en el siguiente nivel del
diagrama (sus Procedimientos y Tareas, con descripción, objetivo y
tiempo real). Prioridad sugerida: los 3 bloques "Sin datos" — Redes
(AB, miércoles), Configuración y Red + Eventos (RM, jueves y viernes).

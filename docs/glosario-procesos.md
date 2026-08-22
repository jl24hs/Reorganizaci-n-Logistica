# Glosario: Proceso, Procedimiento y Tarea

Confundir estos tres niveles es la causa más común de que un diagrama de flujo
termine siendo inmanejable. Cada uno responde una pregunta distinta y vive en
un nivel distinto de detalle.

## Proceso (nivel macro — "el QUÉ")

Conjunto de actividades relacionadas que transforman una entrada en una
salida con valor para alguien (un cliente interno o externo). Responde:
**¿qué hace el área?**

- Suele tener nombre de sustantivo + verbo: "Gestión de Pedidos",
  "Distribución de Mercadería", "Gestión de Inventario", "Devoluciones".
- Un área de logística típicamente tiene entre 5 y 10 procesos. Si tenés
  más de 12, probablemente estás mezclando procedimientos con procesos.
- El mapa de procesos es UN solo diagrama, con cajas grandes, sin detalle
  interno. Ese es el único diagrama que puede ser "de toda el área".

## Procedimiento (nivel medio — "el CÓMO")

La secuencia específica de pasos para ejecutar una parte de un proceso.
Responde: **¿cómo se hace esto, en qué orden, y quién interviene en cada
paso?**

- Ejemplos dentro del proceso "Distribución de Mercadería": "Procedimiento
  de armado de hojas de ruta", "Procedimiento de carga de camión",
  "Procedimiento de entrega y rendición".
- Cada procedimiento es UN diagrama de flujo aparte, con carriles
  (swimlanes) por persona o rol, para que se vea quién hace cada paso.
- Un proceso puede tener entre 2 y 8 procedimientos.

## Tarea (nivel micro — "la ACCIÓN")

La acción concreta y atómica que ejecuta una persona en un paso del
procedimiento. Responde: **¿qué hace la persona con sus manos/con el
sistema en ese momento?**

- Ejemplos dentro de "Procedimiento de carga de camión": "verificar bultos
  contra remito", "escanear código de barras", "firmar remito", "cargar
  novedad en el sistema".
- Las tareas NO llevan diagrama propio: van como texto dentro de cada caja
  del diagrama de procedimiento, o como filas en la planilla de inventario
  (ver `plantilla-inventario-tareas.csv`).

## Regla práctica para no confundirte

Preguntate: *"¿esto es algo que puedo medir en minutos y que hace una sola
persona en un solo paso?"*
- Sí → es una **tarea**.
- No, pero puedo dibujarlo como una secuencia de pasos con flechas → es un
  **procedimiento**.
- No, es más bien el nombre de "para qué existe esta parte del área" → es
  un **proceso**.

## Jerarquía

```
Proceso (5-10 en toda el área)
  └─ Procedimiento (2-8 por proceso)
        └─ Tarea (las filas de tu inventario, dentro de cada paso)
```

Ver `metodologia-diagrama-por-capas.md` para cómo convertir esto en
diagramas manejables, y `ejemplo-diagrama-flujo.md` para un ejemplo
dibujado.

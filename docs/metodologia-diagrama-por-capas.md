# Metodología: diagrama por capas (en vez de un diagrama gigante)

Objetivo: entender y mostrar qué hace el área, separando lo que **se hace**,
lo que **debería hacerse** y las **mejoras** propuestas — y usar eso como
evidencia para pedir más personal.

## Paso 1 — Inventario en planilla, no en el diagrama

Antes de dibujar nada, volcá todo en una planilla (ver
`plantilla-inventario-tareas.csv`). El diagrama es para *comunicar*, la
planilla es para *calcular y convencer*. Columnas clave:

- Proceso / Procedimiento / Tarea (los tres niveles, ver glosario).
- **Objetivo (por qué se hace)**: la razón de negocio de esa tarea/
  procedimiento. Si no se puede responder "para qué sirve esto", es
  candidato a revisar si realmente hace falta, o falta documentar por qué
  se hace. Sin esto, un diagrama es solo una lista de pasos sin sentido.
- Estado: `Se hace` / `Debería hacerse (falta)` / `Mejora futura`.
- Responsable actual (si lo tiene).
- Frecuencia (por pedido, por día, por semana).
- Tiempo estimado por ejecución (minutos) — **medido, no adivinado**. Un
  tiempo estimado a ojo puede arruinar todo el cálculo de horas-persona;
  mejor dejarlo en blanco que poner un número sin confirmar.
- Volumen mensual (cuántas veces se ejecuta por mes).
- Horas-persona/mes = tiempo × volumen (esta columna es la que arma el
  caso de dotación — solo calcularla cuando el tiempo esté confirmado).
- Por qué no se hace hoy (si aplica): falta de tiempo, falta de gente,
  falta de definición, falta de sistema, etc.

### Horas disponibles por persona (dato real, no genérico)

Para comparar contra las horas-persona/mes que demandan las tareas, hay
que usar el horario real del equipo, no un número de manual:

- Lunes a viernes: 8:00 a 17:00 (9 horas) menos 1 hora de descanso =
  **8 horas efectivas/día** × 5 días = 40 hs.
- Sábados: 8:00 a 12:00 = **4 horas**.
- Total: **44 horas/semana** → **≈ 191 horas/mes** por persona (44 ×
  4,33 semanas promedio por mes).

Ese ≈191 es el número contra el que se compara la demanda de horas de
cada persona, no un genérico de "8x5".

Llenar esta planilla es el 80% del trabajo real. El diagrama después sale
casi solo.

## Paso 2 — Mapa macro de procesos (1 solo diagrama)

Un diagrama chico con una caja por **proceso** (5-10 cajas), mostrando solo
el flujo general entre ellos. Sin tareas, sin roles, sin detalle. Este es
el único diagrama "de toda el área" y sirve como índice: cada caja puede
tener un link al diagrama detallado de ese proceso.

## Paso 3 — Un diagrama por procedimiento, con carriles por persona

Para cada procedimiento, un diagrama de flujo con **swimlanes** (un carril
horizontal o vertical por persona/rol). Esto es lo que realmente sirve
para pedir personal, porque se ve de un vistazo:

- Carriles sobrecargados (una sola persona con 15 pasos mientras otra
  tiene 2).
- Pasos que están en el carril de "nadie" (tareas que deberían hacerse
  pero no tienen responsable — el hueco que justifica la vacante).
- Cuellos de botella (todo pasa por una sola persona).

## Paso 4 — Código de colores para las 3 categorías

Usá el mismo color en todos los diagramas y en la planilla:

- 🟩 Verde: se hace hoy.
- 🟥 Rojo: debería hacerse y no se hace (el "gap" — tu argumento principal).
- 🟦 Azul: mejora propuesta para el crecimiento del área (no es urgente,
  es la visión a futuro).

## Paso 5 — De los "rojos" a la cuenta de personal

Para cada tarea marcada en rojo (o para las sobrecargas del Paso 3):

1. Sumá las horas-persona/mes que demandaría (columna de la planilla).
2. Sumá las horas-persona/mes disponibles hoy en el equipo (personas ×
   horas laborales/mes).
3. La diferencia, dividida por las horas-persona/mes de una persona, te da
   el número de puestos que necesitás pedir. Esto es un número, no una
   sensación — es lo que un jefe/gerente puede aprobar.

## Resumen del orden de trabajo

1. Llenar la planilla de inventario (todas las tareas: se hacen, deberían
   hacerse, mejoras).
2. Agrupar tareas en procedimientos, y procedimientos en procesos.
3. Dibujar el mapa macro (1 diagrama).
4. Dibujar un diagrama por procedimiento con swimlanes y colores.
5. Calcular horas-persona necesarias vs. disponibles → número de puestos.

Ver `ejemplo-diagrama-flujo.md` para un ejemplo dibujado con datos
genéricos de logística, a modo de plantilla visual.

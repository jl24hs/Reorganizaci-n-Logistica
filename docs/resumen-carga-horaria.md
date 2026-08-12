# Carga horaria de AB y RM — pendiente de recalcular con datos validados

**Corrección (12/08/2026):** la primera versión de este documento calculaba
horas-persona/mes a partir de la columna "Tiempo" de la hoja "Procesos
Diarios". El jefe de área confirmó que esos tiempos no están calculados
correctamente, así que **esos totales se retiraron** de la planilla
(`docs/plantilla-inventario-tareas.csv` — la columna Horas-persona/mes
ahora dice "No calcular aun" en las filas que venían de esa fuente).

No hay que perder lo bueno de ese trabajo: la clasificación de cada tarea
en **Proceso / Procedimiento / Tarea**, y quién es responsable (AB, RM, o
compartida), sigue siendo válida y quedó cargada. Lo que falta no es la
estructura — es la **descripción real** de cada tarea (qué implica
hacerla, con qué pasos) y un **tiempo medido de verdad**, no estimado.

## Por qué no calcular horas todavía

Calcular horas-persona con tiempos que no son confiables da un número que
parece preciso pero no lo es — y ese es justamente el tipo de dato que
puede jugar en contra si se usa para pedir personal y alguien lo
cuestiona. Mejor no tener el número todavía que tener uno incorrecto.

## Cómo se va a construir el número correcto

1. **Descripción completa por tarea**, al estilo del instructivo del
   TOP10 (que sí tiene el paso a paso). Para cada tarea del catálogo,
   necesitamos: qué hay que hacer exactamente, con qué herramientas/
   sistemas, y qué dispara que se ejecute.
2. **Tiempo medido, no estimado** — una vez que la descripción está
   clara, se puede cronometrar o pedirle a AB/RM que midan 1-2
   ejecuciones reales de cada tarea (o de las más grandes/frecuentes,
   para empezar).
3. Con eso sí se recalcula horas-persona/mes con confianza.

## Próximo paso

Antes de tocar más números, conviene ir tarea por tarea (o proceso por
proceso) completando la descripción real. ¿Empezamos por algún proceso en
particular, o preferís que te muestre la lista completa de tareas que
quedaron con menos descripción para elegir por dónde arrancar?

# Reporte Semanal de Faltantes de Stock

Módulo custom para Odoo 19, pensado para 24hs SECURITY, con 2 depósitos:
**SDQ** (Sede Duarte Quirós) y **NCS** (Nuevocentro).

## Qué calcula

Para cada producto y depósito configurado:

1. **Consumo real**: suma de `stock.move.line.quantity` (estado `done`) de
   los *picking types* marcados como "consumo real" del depósito, dentro de
   la ventana configurada (`period_days`, por defecto 90 días).
   - El consumo se lee de `stock.move.line`, **no** de `sale.order`.
   - El traslado interno SDQ → NCS (`SSTKNSTK`) es reabastecimiento, no
     consumo, y no debe configurarse como picking type de consumo.
2. **Consumo promedio diario** = consumo real / `period_days`.
3. **Stock actual** = `qty_available` del producto en el contexto del
   depósito.
4. **Días de cobertura** = stock actual / consumo promedio diario.
5. **Faltante** = cobertura < `threshold_days` (umbral configurable).

Solo se generan líneas para pares producto/depósito con consumo real >0 en
la ventana elegida (sin historial de consumo no hay cobertura calculable).

## Defecto D1 (salidas de NCS mal clasificadas)

Mientras el defecto D1 no esté confirmado como corregido, parte de las
salidas de NCS pueden estar registradas bajo `NRMACCST` en vez de
`NSTKCCST`. Para no subestimar el consumo:

1. En **Faltantes de Stock > Configuración > Depósitos**, en la fila de
   NCS, cargá `NRMACCST` en el campo "Picking types adicionales (defecto
   D1)" (además de `NSTKCCST` en "Picking types de consumo real").
2. En **Configuración > Ajustes generales**, dejá activo "Incluir salidas
   mal clasificadas (defecto D1)".
3. Una vez que se confirme que el defecto ya no ocurre (o que los datos
   históricos fueron corregidos), desactivá esa opción para que el reporte
   deje de sumar `NRMACCST` como consumo.

Esto permite recalcular el histórico con o sin el workaround sin tocar
código: es un toggle en la configuración general.

## Configuración inicial

1. Instalar el módulo.
2. **Configuración > Ajustes generales**: revisar `period_days`,
   `threshold_days` y opcionalmente agregar usuarios a "Notificar por
   faltantes a" (reciben un mensaje en el chatter del reporte cuando hay
   faltantes).
3. **Configuración > Depósitos**: crear una fila por depósito (SDQ, NCS) y
   asignar sus picking types reales:
   - SDQ → consumo real: `SSTKCCST`
   - NCS → consumo real: `NSTKCCST`; fallback D1: `NRMACCST`
4. El reporte se genera automáticamente todos los viernes (cron
   `Faltantes de stock: generar reporte semanal`). También se puede
   generar/regenerar manualmente desde un registro de **Reportes** con el
   botón "Generar / Regenerar líneas".

## Notas de implementación

- Usa `_read_group` (API de agregación recomendada desde Odoo 17) en vez
  del `read_group` clásico.
- El cron corre semanalmente anclado a un viernes; si se reinstala el
  módulo mucho después de esa fecha, ajustar el campo `nextcall` del cron
  al próximo viernes deseado.
- No se testeó contra una instancia real de Odoo (no disponible en este
  entorno): validar el nombre exacto de los picking types (`SDQ`, `NCS`,
  `SSTKNSTK`, `NSTKCCST`, `SSTKCCST`, `NRMACCST`) y el campo `quantity` en
  `stock.move.line` antes de usar en producción.

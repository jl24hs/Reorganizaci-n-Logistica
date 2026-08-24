{
    'name': 'Reporte Semanal de Faltantes de Stock',
    'version': '19.0.1.0.0',
    'summary': 'Cobertura de stock por producto/depósito y alertas de faltantes (SDQ / NCS)',
    'description': """
Reporte semanal de faltantes de stock (24hs SECURITY)
======================================================

Calcula, por producto y depósito, el consumo real a partir de
``stock.move.line`` (no de ``sale.order``), el stock actual y los días
de cobertura (stock actual / consumo promedio diario). Genera una
alerta cuando la cobertura cae por debajo de un umbral configurable.

Puntos clave del cálculo:

* El consumo real de cada depósito se toma de los tipos de operación
  configurados en "Faltantes de Stock > Configuración > Depósitos"
  (por defecto NSTKCCST para NCS y SSTKCCST para SDQ). El traslado
  interno SDQ -> NCS (SSTKNSTK) no se cuenta como consumo, es
  reabastecimiento.
* Workaround para el defecto D1: mientras las salidas de NCS puedan
  quedar mal clasificadas bajo NRMACCST en lugar de NSTKCCST, se puede
  sumar ese tipo de operación como "fallback" por depósito y activar/
  desactivar el workaround desde la configuración general una vez que
  el defecto esté confirmado como corregido.
* Se ejecuta automáticamente todos los viernes vía ``ir.cron`` y
  notifica a los usuarios configurados cuando hay productos en
  faltante.
""",
    'author': '24hs SECURITY',
    'category': 'Inventory/Inventory',
    'license': 'LGPL-3',
    'depends': ['stock', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'views/shortage_settings_views.xml',
        'views/warehouse_config_views.xml',
        'views/shortage_report_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': False,
}

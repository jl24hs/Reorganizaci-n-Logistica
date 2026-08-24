# -*- coding: utf-8 -*-
from odoo import fields, models


class StockShortageWarehouseConfig(models.Model):
    _name = 'stock.shortage.warehouse.config'
    _description = 'Picking types de consumo real por depósito (para el reporte de faltantes)'
    _rec_name = 'warehouse_id'

    warehouse_id = fields.Many2one(
        'stock.warehouse', string='Depósito', required=True, ondelete='cascade')
    consumption_picking_type_ids = fields.Many2many(
        'stock.picking.type',
        'stock_shortage_wh_config_consumption_rel',
        'config_id', 'picking_type_id',
        string='Picking types de consumo real',
        help='Tipos de operación cuyas líneas de stock.move.line representan '
             'salidas/ventas reales de este depósito, p. ej. NSTKCCST para '
             'NCS y SSTKCCST para SDQ. NO incluir el traslado interno de '
             'reabastecimiento (SSTKNSTK): ese es entrada/salida entre '
             'depósitos, no consumo.',
    )
    d1_fallback_picking_type_ids = fields.Many2many(
        'stock.picking.type',
        'stock_shortage_wh_config_fallback_rel',
        'config_id', 'picking_type_id',
        string='Picking types adicionales (defecto D1)',
        help='Tipos de operación donde, por el defecto D1, pueden haber '
             'quedado salidas mal clasificadas (p. ej. NRMACCST para NCS). '
             'Se suman al consumo solo si "Incluir salidas mal clasificadas '
             '(defecto D1)" está activo en la configuración general.',
    )

    _sql_constraints = [
        ('warehouse_uniq', 'unique(warehouse_id)',
         'Ya existe una configuración para este depósito.'),
    ]

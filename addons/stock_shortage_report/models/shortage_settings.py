# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StockShortageSettings(models.Model):
    _name = 'stock.shortage.settings'
    _description = 'Configuración del reporte de faltantes de stock'

    name = fields.Char(default='Configuración', required=True)
    period_days = fields.Integer(
        string='Días de historial para consumo promedio',
        default=90, required=True,
        help='Ventana (en días) de stock.move.line usada para calcular el '
             'consumo promedio diario por producto/depósito.',
    )
    threshold_days = fields.Float(
        string='Umbral de cobertura (días)',
        default=7.0, required=True,
        help='Si los días de cobertura de un producto caen por debajo de '
             'este valor, se marca como faltante.',
    )
    apply_d1_workaround = fields.Boolean(
        string='Incluir salidas mal clasificadas (defecto D1)',
        default=True,
        help='El defecto D1 hace que parte de las salidas de NCS queden '
             'registradas bajo NRMACCST en vez de NSTKCCST. Mientras no se '
             'confirme el fix, active esta opción para que esos '
             'stock.move.line también se sumen al consumo real de NCS '
             '(configurando NRMACCST como picking type "fallback" del '
             'depósito NCS). Desactívela una vez confirmado que el defecto '
             'ya no ocurre, para no inflar el consumo con datos históricos '
             'ya migrados.',
    )
    notify_user_ids = fields.Many2many(
        'res.users', string='Notificar por faltantes a',
        help='Usuarios que reciben una notificación cuando el reporte '
             'semanal detecta productos con cobertura por debajo del '
             'umbral.',
    )

    @api.constrains('period_days')
    def _check_period_days(self):
        for rec in self:
            if rec.period_days <= 0:
                raise ValidationError(
                    'Los días de historial deben ser mayores a cero.')

    @api.model
    def get_settings(self):
        """Devuelve el registro único de configuración, creándolo si hace falta."""
        settings = self.search([], limit=1)
        if not settings:
            settings = self.create({})
        return settings

# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import _, api, fields, models


class StockShortageReport(models.Model):
    _name = 'stock.shortage.report'
    _description = 'Reporte semanal de faltantes de stock'
    _inherit = ['mail.thread']
    _order = 'date_generated desc'

    name = fields.Char(required=True, default=lambda self: _('Nuevo'))
    date_generated = fields.Datetime(required=True, default=fields.Datetime.now)
    period_days = fields.Integer(string='Días de historial usados')
    threshold_days = fields.Float(string='Umbral de cobertura usado (días)')
    line_ids = fields.One2many(
        'stock.shortage.report.line', 'report_id', string='Líneas')
    shortage_count = fields.Integer(
        string='Productos en faltante', compute='_compute_shortage_count')

    @api.depends('line_ids.is_shortage')
    def _compute_shortage_count(self):
        for rec in self:
            rec.shortage_count = len(rec.line_ids.filtered('is_shortage'))

    @api.model
    def _cron_generate_weekly_report(self):
        report = self.create({
            'name': _('Faltantes de stock - %s') % fields.Date.context_today(self),
        })
        report.action_generate_lines()
        report._notify_shortages()
        return report

    def action_generate_lines(self):
        self.ensure_one()
        settings = self.env['stock.shortage.settings'].get_settings()
        self.period_days = settings.period_days
        self.threshold_days = settings.threshold_days
        self.line_ids.unlink()

        date_from = fields.Datetime.now() - timedelta(days=settings.period_days)
        wh_configs = self.env['stock.shortage.warehouse.config'].search([])

        line_vals = []
        for wh_config in wh_configs:
            warehouse = wh_config.warehouse_id
            picking_types = wh_config.consumption_picking_type_ids
            if settings.apply_d1_workaround:
                picking_types |= wh_config.d1_fallback_picking_type_ids
            if not picking_types:
                continue

            results = self.env['stock.move.line']._read_group(
                domain=[
                    ('state', '=', 'done'),
                    ('date', '>=', date_from),
                    ('picking_id.picking_type_id', 'in', picking_types.ids),
                ],
                groupby=['product_id'],
                aggregates=['quantity:sum'],
            )
            for product, qty_consumed in results:
                if not product or not qty_consumed:
                    continue
                qty_on_hand = product.with_context(
                    warehouse=warehouse.id).qty_available
                avg_daily = qty_consumed / settings.period_days
                coverage_days = qty_on_hand / avg_daily
                line_vals.append({
                    'report_id': self.id,
                    'warehouse_id': warehouse.id,
                    'product_id': product.id,
                    'qty_on_hand': qty_on_hand,
                    'qty_consumed': qty_consumed,
                    'avg_daily_consumption': avg_daily,
                    'coverage_days': coverage_days,
                    'is_shortage': coverage_days < settings.threshold_days,
                })
        self.env['stock.shortage.report.line'].create(line_vals)

    def _notify_shortages(self):
        self.ensure_one()
        settings = self.env['stock.shortage.settings'].get_settings()
        if not settings.notify_user_ids:
            return
        shortages = self.line_ids.filtered('is_shortage').sorted('coverage_days')
        if not shortages:
            return

        rows = ''.join(
            '<tr><td>%s</td><td>%s</td><td>%.2f</td><td>%.2f</td></tr>' % (
                line.warehouse_id.display_name,
                line.product_id.display_name,
                line.coverage_days,
                line.qty_on_hand,
            )
            for line in shortages
        )
        body = _(
            '<p>El reporte semanal de faltantes de stock detectó %s producto(s) '
            'por debajo del umbral de cobertura (%.2f días).</p>'
            '<table border="1" cellpadding="4" cellspacing="0">'
            '<tr><th>Depósito</th><th>Producto</th><th>Días de cobertura</th>'
            '<th>Stock actual</th></tr>%s</table>'
        ) % (len(shortages), settings.threshold_days, rows)
        self.message_post(
            body=body,
            partner_ids=settings.notify_user_ids.partner_id.ids,
            subtype_xmlid='mail.mt_comment',
        )


class StockShortageReportLine(models.Model):
    _name = 'stock.shortage.report.line'
    _description = 'Línea de faltante de stock (por producto/depósito)'
    _order = 'coverage_days asc'

    report_id = fields.Many2one(
        'stock.shortage.report', required=True, ondelete='cascade')
    warehouse_id = fields.Many2one('stock.warehouse', required=True, readonly=True)
    product_id = fields.Many2one('product.product', required=True, readonly=True)
    qty_on_hand = fields.Float(string='Stock actual', readonly=True)
    qty_consumed = fields.Float(
        string='Consumo en el período', readonly=True,
        help='Suma de stock.move.line (quantity) de los picking types de '
             'consumo real del depósito, durante la ventana configurada.')
    avg_daily_consumption = fields.Float(
        string='Consumo promedio diario', readonly=True)
    coverage_days = fields.Float(
        string='Días de cobertura', readonly=True,
        help='Stock actual / consumo promedio diario.')
    is_shortage = fields.Boolean(
        string='En faltante', readonly=True, default=False)

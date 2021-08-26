from odoo import _, api, fields, models

class ResCountryState(models.Model):
    _inherit = 'res.country.state'
    _description = 'Res Country State'
    
    active = fields.Boolean(default=True)

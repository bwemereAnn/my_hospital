from odoo import models, fields, api, _


class Patients(models.Model):
    _inherit = 'res.partner'
    _description = 'Patients of an hospital'


    is_patient = fields.Boolean(string='Is patient?')
    birthdate = fields.Date(string='Birthdate')
    age = fields.Integer(string='Age')




class Doctor(models.Model):
    _inherit = 'res.users'
    _description = 'Doctor of an hospital'

    is_doctor = fields.Boolean(string='Is Doctor?')



class TheAppointments(models.Model):
    _name = 'the.appointments'
    _description = 'Appointments of an hospital'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Appointment Id', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('res.partner', string='Patient', readonly=True, domain=[('is_patient', '=', True)])
    patient_age = fields.Integer('Age')
    notes = fields.Text(string='Notes')
    app_date = fields.Date(string='Date Time', required=True)


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('the.appointments.sequence') or _('New')
        result = super(TheAppointments, self).create(vals)
        return result


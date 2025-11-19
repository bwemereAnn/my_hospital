from odoo import models, fields, api, _


class Patients(models.Model):
    _inherit = 'res.partner'
    _description = 'Patients of an hospital'

    is_patient = fields.Boolean(string='Is patient?')
    birthdate = fields.Date(string='Birthdate')
    age = fields.Integer(string='Age')
    appointment_ids = fields.Many2many('the.appointments', "patient_id",
                                       string='Appointments')
    app_count = fields.Integer(string='App.Count', compute='get_app_count')

    def get_appointments(self):
        action = {
            'name': 'appointments',
            'res_model': 'the.appointments',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
            'domain': [('patient_id', '=', self.id)],
        }
        return action

    def get_app_count(self):
        count = self.env["the.appointments"].search(
            [('patient_id', '=', self.id)])
        self.app_count = count


class Doctor(models.Model):
    _inherit = 'res.users'
    _description = 'Doctor of an hospital'

    is_doctor = fields.Boolean(string='Is Doctor?')


class TheAppointments(models.Model):
    _name = 'the.appointments'
    _description = 'Appointments of an hospital'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Appointment Id', required=True, copy=False,
                       readonly=True, index=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one('res.partner', string='Patient',
                                 domain=[('is_patient', '=', True)])
    patient_age = fields.Integer('Age', related='patient_id.age',
                                 readonly=True, )
    notes = fields.Text(string='Notes')
    app_date = fields.Date(string='Date Time', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], 'Status', default='draft', readonly=True)
    doctors_notes = fields.Text(string='Doctors Notes')
    doctor_id = fields.Many2one('res.users',string='Doctor', domain=[('is_doctor', '=', True)])
    prescriptions_ids = fields.Many2many('the.prescriptions', "prescriptions_id",)


    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})


    def action_cancel(self):
        self.write({'state': 'cancel'})

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'the.appointments.sequence') or _('New')
        result = super(TheAppointments, self).create(vals)
        return result


class Prescriptions(models.Model):
    _name = 'the.prescriptions'
    _description = 'Prescriptions of an hospital'

    name = fields.Char(string='Medecine name')
    notes = fields.Text(string='Notes')
    appointment_id = fields.Many2one('the.appointments', string='Appointments')

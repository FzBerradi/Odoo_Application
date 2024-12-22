from odoo import models, fields

class Student(models.Model):
    _name = 'studentmanagement.student'
    _description = 'Student Management'

    lastName = fields.Char(string='Lastname', required=True)
    firstName = fields.Char(string='Firstname', required=True)
    dateOfBirth = fields.Date(string='DateOfBirth', required=True)
    email = fields.Char(string='Email', required=True)
    cin = fields.Char(string='CIN', required=True)
    cne = fields.Char(string='CNE', required=True)
    phoneNumber = fields.Char(string='PhoneNumber', required=True)
    paid = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Paid', required=True)
    department_id = fields.Many2one('studentmanagement.department', string="Department")
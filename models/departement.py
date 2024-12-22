# models/department.py
from odoo import models, fields

class Department(models.Model):
    _name = 'studentmanagement.department'
    _description = 'Department Management'

    name = fields.Char(string='Department Name', required=True)
    description = fields.Text(string='Description')
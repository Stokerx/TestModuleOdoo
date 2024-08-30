from odoo import models, fields

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject'
    
    name = fields.Char(string='Name', required=True)
    credits = fields.Integer(string='Credits', required=True)
    max_students = fields.Integer(string='Max Students')
    active = fields.Boolean(string='Activated', default=True)
    student_ids = fields.Many2many('school.student', string='Students')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')

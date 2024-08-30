from odoo import models, fields, api
from datetime import date

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'
    
    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birthdate', required=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    final_exam_grade = fields.Float(string='Final Exam Grade')
    subject_ids = fields.Many2many('school.subject', string='Subjects')
   

    @api.depends('birth_date')
    def _compute_age(self):
        for student in self:
            if student.birth_date:
                student.age = (date.today() - student.birth_date).days // 365
            else:
                student.age = 0
    
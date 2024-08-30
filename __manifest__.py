{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'School Management',
    'description': """
    el modulo para administrar el sistema de colegio de la institucion para los incluyendo los estudiantes, profesores, cursos, notas, etc.
    """,
    'category': 'Education',
    'author': 'Rodrigo Luna',
    'depends': ['base'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/school_student_views.xml',
        'views/school_teacher_views.xml',
        'views/school_subject_views.xml',
        'views/school_menu.xml',
    ],
    
}
"""
Imports
"""
import services.grade_average_service as grade_service


homework_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3': 81,
}


# use of the fully qualified package
grade_service.calculate_homework(homework_assignment_grades)
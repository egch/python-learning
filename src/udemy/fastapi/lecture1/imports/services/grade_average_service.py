def calculate_homework(homework_assignment_grades):
    sum_of_grades = 0
    for homework in homework_assignment_grades.values():
        sum_of_grades += homework
    final_grade = sum_of_grades / len(homework_assignment_grades)
    print(final_grade) # 88.66666666666667
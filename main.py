from models.mentor.Lecturer import Lecturer
from models.mentor.Reviewer import Reviewer
from models.student.Student import Student


def calculate_average_grade_by_course_to_lecturers(lecturers: list[Lecturer], course_name: str):
    sum = 0
    count = 0
    for lecturer in lecturers:
        lecturer_grades = lecturer.get_grades()
        if course_name in lecturer_grades:
            grade = lecturer_grades[course_name]
            sum = sum + grade
            count = count + 1
    average_grade = 0
    if count != 0:
        average_grade = sum / count
    return average_grade


def calculate_average_grade_by_course_to_students(students: list[Student], course_name: str):
    sum = 0
    count = 0
    for student in students:
        student_grades = student.get_grades()
        if course_name in student_grades:
            grade = student_grades[course_name]
            sum = sum + grade
            count = count + 1
    average_grade = 0
    if count != 0:
        average_grade = sum / count
    return average_grade


def main():
    best_student = Student("Joel", "Embiid", "M")
    best_student.add_course_in_progress("Python")
    best_student.add_course_in_progress("Java")
    best_student.add_finished_courses("ML")

    not_best_student = Student("Lebron", "James", "M")
    not_best_student.add_course_in_progress('Python')

    almost_best_student = Student("Stephen", "Curry", "M")
    almost_best_student.add_course_in_progress("Python")

    cool_lecturer = Lecturer('Some', 'Buddy')
    cool_lecturer.add_course("Python")

    not_so_cool_lecturer = Lecturer("Vince", "Carter")
    not_so_cool_lecturer.add_course("Python")

    bad_lecturer = Lecturer("Jason", "Tatum")
    bad_lecturer.add_course("Python")

    cool_reviewer = Reviewer('Some', 'Buddy')
    cool_reviewer.add_course("Python")
    cool_reviewer.rate_home_work(best_student, "Python", 10)
    cool_reviewer.rate_home_work(not_best_student, "Python", 8)
    cool_reviewer.rate_home_work(almost_best_student, "Python", 9)
    cool_reviewer + "Java"

    students = [best_student, almost_best_student, not_best_student]

    print("Средняя оценка студентов за курс Python от проверяющих: ",
          calculate_average_grade_by_course_to_students(students, "Python"))

    best_student.rate_lecturer("Python", cool_lecturer, 10)
    best_student.rate_lecturer("Python", not_so_cool_lecturer, 7)
    best_student.rate_lecturer("Python", bad_lecturer, 4)

    lecturers = [cool_lecturer, not_so_cool_lecturer, bad_lecturer]

    print("Средняя оценка лекторов за курс Python от студентов: ",
          calculate_average_grade_by_course_to_lecturers(lecturers, "Python"))

    print("Лучше ли первый студент второго? ", best_student > not_best_student)

    print()

    print(cool_lecturer)

    print()

    print(best_student)

    print()

    print("Имя студента: ", best_student.get_name())
    print("Имя преподавателя: ", cool_lecturer.get_name())
    print("Оценки лектора по курсам: ", cool_lecturer.get_grades())
    print("Оценки студента по курсам: ", best_student.get_grades())


main()

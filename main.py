from models.mentor.Lecturer import Lecturer
from models.mentor.Reviewer import Reviewer
from models.student.Student import Student


def main():
    best_student = Student("Joel", "Embiid", "M")
    cool_lecturer = Lecturer('Some', 'Buddy')
    cool_reviewer = Reviewer('Some', 'Buddy')
    cool_reviewer.rate_home_work(best_student, "Python", 10)

    best_student.add_course_in_progress("Python")
    cool_lecturer.add_course("Python")
    best_student.rate_lecturer("Python", cool_lecturer, 10)

    print("Имя студента: ", best_student.get_name())
    print("Имя преподавателя: ", cool_lecturer.get_name())
    print("Оценки лектора по курсам: ", cool_lecturer.get_grades())
    print("Оценки студента по курсам: ", best_student.get_grades())


main()

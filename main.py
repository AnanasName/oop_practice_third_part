from models.mentor.Lecturer import Lecturer
from models.mentor.Reviewer import Reviewer
from models.student.Student import Student


def main():
    best_student = Student("Joel", "Embiid", "M")
    cool_lecturer = Lecturer('Some', 'Buddy')
    cool_reviewer = Reviewer('Some', 'Buddy')
    cool_reviewer.rate_home_work(best_student, "Python", 10)

    print("Имя студента: ", best_student.get_name())
    print("Имя преподавателя: ", cool_lecturer.get_name())
    print("Оценки студента по курсам: ", best_student.get_grades())


main()

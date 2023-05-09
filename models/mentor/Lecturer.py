from models.mentor.base.Mentor import Mentor


class Lecturer(Mentor):

    def __init__(self, name: str, surname: str, ):
        super().__init__(name, surname)
        self.__grades = {}

    def set_grade(self, course_name: str, grade: int):
        if self.get_courses_attached().__contains__(course_name):
            self.__grades[course_name] = grade

    def get_grades(self):
        return self.__grades

    def do_lecture(self):
        print("Do My Work")

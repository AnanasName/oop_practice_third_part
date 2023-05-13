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

    def __calculate_average_grade(self) -> float:
        elements_sum = 0
        elements_number = 0

        for key in self.__grades.keys():
            elements_sum = elements_sum + self.__grades[key]
            elements_number = elements_number + 1

        if (elements_number != 0):
            average_grade = elements_sum / elements_number
        else:
            average_grade = 0.0

        return average_grade

    def __str__(self):
        return f"Имя: {self._name}\nФамилия: {self._surname}\nСредняя оценка за лекции: {self.__calculate_average_grade()}"

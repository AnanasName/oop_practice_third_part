class Student:
    def __init__(self, name: str, surname: str, gender: str):
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__finished_courses = []
        self.__courses_in_progress = []
        self.__grades = {}

    def add_courses(self, course_name):
        self.__finished_courses.append(course_name)

    def set_grade(self, course_name: str, grade: int):
        self.__grades[course_name] = grade

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_finished_courses(self):
        return self.__finished_courses

    def get_courses_in_progress(self):
        return self.__courses_in_progress

    def get_grades(self):
        return self.__grades

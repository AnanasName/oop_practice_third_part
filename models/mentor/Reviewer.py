from models.mentor.base.Mentor import Mentor
from models.student import Student


class Reviewer(Mentor):

    def rate_home_work(self, student: Student, course: str, grade: int):
        student.set_grade(course, grade)

from abc import ABC


class Mentor(ABC):
    def __init__(self, name: str, surname: str):
        self.__name = name
        self.__surname = surname
        self.__courses_attached = []

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_courses_attached(self):
        return self.__courses_attached
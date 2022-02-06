from __future__ import annotations
from abc import ABC, abstractmethod


class Person(ABC):
    """clase abstract"""

    @abstractmethod
    def person_method(self):
        """interface method"""
        raise NotImplementedError


class Student(Person):

    def __init__(self):
        self.name = 'Dan'

    def person_method(self):
        """metodo sobrescrito"""
        return f'im a student'


class Teacher(Person):

    def __init__(self):
        self.name = 'Ivan'

    def person_method(self):
        """metodo sobrescrito"""
        return f'Im a teacher'

p1 = Student()

print(p1.person_method())

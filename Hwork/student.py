from human import Human

class Student(Human):
    def __init__(self, gender, age, name, surname, record_book):
        super().__init__(gender, age, name, surname)
        self.record_book = record_book

    def __str__(self):
        return f"Student: Gender: {self.gender}, Age: {self.age}, Name:{self.name}, Surname:{self.surname}, Record_book: {self.record_book}"

    def __eq__(self, other):
        return str(self.surname) == str(other.surname)

    def __hash__(self):
        return hash(str(self))

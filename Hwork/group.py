from student import Student
from group_limit import GroupLimitException

class Group:
    def __init__(self, number, student_limit = 10):
        self.number = number
        self.group = set()
        self.student_limit = student_limit

    def add_student(self, student):
        if len(self.group) > self.student_limit:
            raise GroupLimitException("The limit щof students is exceeded")
        if isinstance(student, Student):
            self.group.add(student)

    def delete_student(self, surname):
        self.group = {student for student in self.group if student.surname != surname}

    def find_student(self, surname):
        for student in self.group:
            if student.surname == surname:
                return student

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n {all_students} '


class Human:
    def __init__(self, gender, age, name, surname):
        self.gender = gender
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Human: Gender: {self.gender}, Age: {self.age}, Name: {self.name}, Surname: {self.surname}'

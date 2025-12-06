from src.udemy.fastapi.oop.people.person import Person


class Student(Person):
    def __init__(self, name, age, degree):
        super().__init__(name, age)
        self.degree = degree
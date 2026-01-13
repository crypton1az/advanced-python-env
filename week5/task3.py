class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return "I am a person"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.__student_id = student_id  # encapsulation

    def info(self):
        return "I am a student"


p = Person("Alex")
s = Student("Bob", 123)

print(p.info())
print(s.info())

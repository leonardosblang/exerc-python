class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print('O nome : ' + self.name)


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__id = id

    def print_id(self):
        print('A matrícula é : ' + self.id)

    # create a that prints age
    def print_age(self):
        print('A idade é do aluno é : ' + str(self.age))


class Professor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print_age(self):
        print('A idade do professor é : ' + str(self.age))


def print_age(person):
    person.print_age()


student = Student('João', 20)
professor = Professor('Maria', 30)
print_age(student)
print_age(professor)

import datetime


class Person:
    Number_person = 1

    def __init__(self, name, family, gender, age):
        self.name = name
        self.family = family
        self.gender = gender
        self.age = age
        self.created_at = datetime.datetime.now()
        Person.Number_person += 1

    def info(self):
        print("Name is:", self.name)
        print("Family is:", self.family)
        print("Gender is:", self.gender)
        print("Age is:", self.age)

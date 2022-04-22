import datetime


class Person:
    def __init__(self, name, family, gender, age):
        self.name = name
        self.family = family
        self.gender = gender
        self.age = age
        self.created_at = datetime.datetime.now()

    def info(self):
        print("Name is:", self.name)
        print("Family is:", self.family)
        print("Gender is:", self.gender)
        print("Age is:", self.age)

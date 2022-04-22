from models.person import Person


class Teacher(Person):
    Number_teacher = 0

    def __init__(self, name, family, gender, age, code):
        super().__init__(name, family, gender, age)
        self.employ_code = code
        Teacher.Number_teacher += 1

from models.student import Student
from models.college import College
from models.teacher import Teacher
from models.lesson import Lesson
from models.person import Person

if __name__ == '__main__':
    # colleges
    col1 = College('Math')
    col2 = College('Computer')
    col3 = College('Science')
    col4 = College('Mechanic')

    # Teachers
    t1 = Teacher("Dr Ali", "Amiri", "man", 46, code=135)
    t2 = Teacher("Dr Mohammad", "Mohammadi", "man", 65, code=2135)
    t3 = Teacher("Dr Reza", "Setayesh", "man", 35, code=25653)
    t4 = Teacher("Dr Zahra", "Ahadi", "woman", 29, code=3265)

    # Lesson
    l1 = Lesson("Mathematics 1", 3, t1, col1)
    l2 = Lesson("Mathematics 2", 3, t1, col1)

    l3 = Lesson("operating system", 4, t2, col2)
    l4 = Lesson("Network", 3, t2, col2)

    l5 = Lesson("Virology", 4, t3, col3)
    l6 = Lesson("Laboratory 2", 3, t3, col3)

    l7 = Lesson("Fluids", 3, t1, col4)
    l8 = Lesson("Static", 4, t1, col4)

    # Students
    s1 = Student(name='Samna', family='Rafiee', gender='man', age='26', code=985625, field="computer science",
                 college=col2)
    s1.add_Lesson(l1)
    s1.add_Lesson(l3)
    s1.add_Lesson(l4)
    s1.add_Lesson(l3)
    s1.add_Lesson(l5)

    s1.lessons_info()
    s1.lessons[0].set_score(20)
    s1.lessons_info()
    print('################################')
    print("Number of Person is:", Person.Number_person)
    print("Number of Student is:", Student.number_student)
    print("Number of Teacher is:", Teacher.Number_teacher)

from models.person import Person


class Student(Person):
    def __init__(self, name, family, gender, age, code, field, college):
        super().__init__(name, family, gender, age)
        self.code = code  # Student Code
        self.field = field
        self.college = college
        self.lessons = []

    # Add New Lesson to Student's Lessons.
    def add_Lesson(self, lesson):
        if lesson.college == self.college:
            if lesson not in self.lessons:
                self.lessons.append(lesson)
                print(f"Lesson '{lesson.title}' Added.")
            else:
                print(f"You have already added this lesson ('{lesson.title}').")
        else:
            print(f"You Can't Select a Lesson from other College.")

    # Show information of all lessons' student.
    def lessons_info(self):
        print(f"Information on '{self.name} {self.family}' lessons:")
        for i, lesson in enumerate(self.lessons):
            print('--------------------------------------------')
            print(
                f"#{i + 1}, Lesson: {lesson.title}, Teacher: {lesson.teacher.name} {lesson.teacher.family}, Score: {lesson.get_score()}")

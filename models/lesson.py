from models.college import College


class Lesson:
    def __init__(self, title, units, teacher, college):
        self.title = title
        self.units = units
        self.teacher = teacher
        self.college = college
        self._score = None

    # Set Score
    def set_score(self, score):
        self._score = score

    # Get Score
    def get_score(self):
        return self._score

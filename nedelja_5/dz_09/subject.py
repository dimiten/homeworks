class Subject:

    def __init__(self, name: str, subject_id: int, grade=5):
        self.name = name
        self.subject_id = subject_id
        self.grade = grade

    def show_subject(self):
        return f"Name of subject: {self.name}, subject id: {self.subject_id}"

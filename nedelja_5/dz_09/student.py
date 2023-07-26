from subject import Subject


class Student:

    def __init__(self, name: str, surname: str, index: int, subjects=None):
        if subjects is None:
            subjects = {}
        self.name = name
        self.surname = surname
        self.index = index
        # self.major = major  Nikako nisam mogao da u klasu Student importujem klasu Major(uvek mi da gresku)
        self.subjects = subjects

    def add_new_subject_to_student(self, subject: Subject, grade: int):
        self.subjects[subject.name] = grade

    def all_passed_subjects(self):
        list_passed_subject = []
        for subject in self.subjects:
            if self.subjects[subject] > 5:
                list_passed_subject.append(subject)
        return list_passed_subject

    def average_grade_of_student(self):
        list_passed_subjects = self.all_passed_subjects()
        sum_of_grades = 0
        if len(list_passed_subjects) > 0:
            for passed_subject in list_passed_subjects:
                sum_of_grades += self.subjects[passed_subject]
            return round(sum_of_grades / len(list_passed_subjects), 2)
        else:
            return 0

    def show_student(self):
        return f"Name: {self.name}, Surname: {self.surname}, Index: {self.index}"

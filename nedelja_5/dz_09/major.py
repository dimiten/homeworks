from student import Student
from subject import Subject


class Major:

    def __init__(self, name: str, module: str, subjects: [], students=None):
        if students is None:
            students = []
        self.name = name
        self.module = module
        self.subjects = subjects
        self.students = students

    def add_new_student_to_major(self, student: Student):
        self.students.append(student)

    def add_new_subject_to_major(self, subject: Subject):
        self.subjects.append(subject)

    def subjects_no_student_passed(self):
        list_of_failed_subjects = []
        for student in self.students:
            for subject in student.subjects:
                if student.subjects[subject] < 6:
                    list_of_failed_subjects.append(subject)

        list_of_passed_subjects = []
        for student in self.students:
            for subject in student.subjects:
                if student.subjects[subject] >= 6:
                    list_of_passed_subjects.append(subject)

        return set(list_of_failed_subjects) - set(list_of_passed_subjects)

    def subject_with_highest_grade(self):
        grade = 5
        subject_ = ""
        for student in self.students:
            for subject in student.subjects:
                if student.subjects[subject] > grade:
                    subject_ = subject
                    grade = student.subjects[subject]
        return subject_

from major import Major


class Faculty:

    def __init__(self, majors=None, students=None, subjects=None):
        if subjects is None:
            subjects = []
        if students is None:
            students = []
        if majors is None:
            majors = []
        self.majors = majors
        self.students = students
        self.subjects = subjects

    def add_major(self, major: Major):
        self.majors.append(major)

    def student_with_highest_grades(self):
        global best_student
        grade = 0
        for student in self.students:
            if student.average_grade_of_student() > grade:
                grade = student.average_grade_of_student()
                best_student = student
        return best_student

    def student_least_passed_subjects(self):
        student_passed = {}
        for student in self.students:
            student_passed[student] = len(student.all_passed_subjects())
        return min(student_passed, key=student_passed.get)

    def students_passed_all_subjects(self):
        list_students = []
        for student in self.students:
            if len(student.subjects) == len(student.all_passed_subjects()) and len(student.subjects) != 0:
                list_students.append(student)
        return list_students

    def major_by_percentage(self):
        num_of_students = 0
        for major in self.majors:
            num_of_students += len(major.students)
        num_student_major = {}
        for major in self.majors:
            num_student_major[major.name] = round(len(major.students) / num_of_students, 2) * 100
        return num_student_major

    def students_on_major(self, major_: Major):
        for major in self.majors:
            if major_ == major:
                return major.students

    def best_student_on_major(self, major_: Major):
        global best_student
        students_on_major = self.students_on_major(major_)
        grade = 0
        for student in students_on_major:
            if student.average_grade_of_student() > grade:
                grade = student.average_grade_of_student()
                best_student = student
        return best_student



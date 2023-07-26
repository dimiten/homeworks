from faculty import Faculty
from major import Major
from student import Student
from subject import Subject


subject_1 = Subject("subject_1", 1)
subject_2 = Subject("subject_2", 2)
subject_3 = Subject("subject_3", 3)
list_of_subjects_1 = [subject_1, subject_2, subject_3]

subject_4 = Subject("subject_4", 4)
subject_5 = Subject("subject_5", 5)
subject_6 = Subject("subject_6", 6)
list_of_subjects_2 = [subject_4, subject_5, subject_6]

list_of_all_subjects = list_of_subjects_1 + list_of_subjects_2

major_1 = Major("Major_1", "Module_1", list_of_subjects_1)
major_2 = Major("Major_2", "Module_2", list_of_subjects_2)
list_of_majors = [major_1, major_2]

student_1 = Student("name_1", "surname_1", 1)
student_2 = Student("name_2", "surname_2", 2)
list_of_students = [student_1, student_2]


major_1.students = list_of_students

student_3 = Student("name_3", "surname_3", 3)
major_1.add_new_student_to_major(student_3)  # a

subject_7 = Subject("subject_7", 7)
major_1.add_new_subject_to_major(subject_7)  # b

student_1.add_new_subject_to_student(subject_1, 6)  # c
student_1.add_new_subject_to_student(subject_2, 6)
student_1.add_new_subject_to_student(subject_3, 10)

student_2.add_new_subject_to_student(subject_1, 7)  # c
student_2.add_new_subject_to_student(subject_2, 6)
student_2.add_new_subject_to_student(subject_3, 8)

student_4 = Student("name_4", "surname_4", 4)
major_2.add_new_student_to_major(student_4)

faculty_1 = Faculty(list_of_majors, list_of_students, list_of_all_subjects)

# def main():
#     while True:
#         print("a) add new student to a major\n"
#               "b) add new subject to a major\n"
#               "c) add new subject to a student\n"
#               "d) list of all passed subjects of a student\n"
#               "e) average grade of a student\n"
#               "f) info of student(s) with the highest average grade\n"
#               "g) info of student(s) with the least passed subjects\n"
#               "h) all students that passed all subjects\n"
#               "i) distribution of students in different majors, in percent\n"
#               "j) all students on chosen major\n"
#               "k) the best student on the chosen major\n"
#               "l) all subjects that no student has passed\n"
#               "m) subject with the highest average grade\n"
#               "n) End the program\n")
#
#         choice = input("Choose a letter from a list above: ")
#
#         match choice:
#             case "a":
#                 print("test")
#             case "b":
#                 print("test")
#             case "c":
#                 print("test")
#             case "d":
#                 print("test")
#             case "e":
#                 print("test")
#             case "f":
#                 print("test")
#             case "g":
#                 print("test")
#             case "h":
#                 print("test")
#             case "i":
#                 print("test")
#             case "j":
#                 print("test")
#             case "k":
#                 print("test")
#             case "l":
#                 print("test")
#             case "m":
#                 print("test")
#             case "n":
#                 print("End of program")
#                 break
#             case other:
#                 print("Invalid input. Choose a letter from a-k!")


if __name__ == "__main__":
    pass

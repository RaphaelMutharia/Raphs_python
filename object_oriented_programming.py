class Student:
    student_name=""
    student_age=0
    student_marks=0

    def __init__(self):
        print("Constructor called")

    def set_student_name(self,name):
        self.student_name=name

    def display_student_name(self):
        print("Student Name:", self.student_name)

    def set_student_age(self,age):
        self.student_age=age

    def display_student_age(self):
       print("Student age:", self.student_age)



student1=Student()
student1.set_student_name("Raph")
student1.display_student_name()
student1.set_student_age("18")
student1.display_student_age()



class Person:
    age=""
    name=""
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def printPerson(self):
     print("The details of the person are:",self.name, self.age)



#child class
class Student(Person):
    uniform=""
    def __init__(self, name, age, uniform):
        super().__init__(name, age)
        self.uniform = uniform
    def printStudent(self):
            print("The details of the person are:",self.name, self.age, self.uniform)

student1 = Student("John", 30, "khaki")
student1.printPerson()


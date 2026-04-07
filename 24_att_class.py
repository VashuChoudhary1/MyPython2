class Student:
    college_name = "MDU" #class attribute
    PI = 3.1

    def __init__(self,name,cgpa):
        self.name = name #instance - invoke only name of object
        self.cgpa = cgpa
        self.PI = 3.14 #instance attribute have high priority

stu1 = Student("rahul",9)
print(stu1.name)
print(stu1.college_name)
print(Student.college_name)
print(Student.PI)
print(stu1.PI)
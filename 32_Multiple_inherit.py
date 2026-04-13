class Teacher:
    def __init__(self,salary):
        self.salary = salary

class Student:
    def __init__(self,cgpa):
        self.cgpa = cgpa

class TA(Teacher, Student): #multiple inheritance
    def __init__(self, salary, cgpa , name):
        super().__init__(salary)
        Student.__init__(self,cgpa)
        self.name = name

ta1 = TA(150_000, 9.3,"Radha")
print(ta1.salary,ta1.cgpa,ta1.name)
    
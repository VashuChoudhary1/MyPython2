class Student:
    def __init__(self,name,age): #parametric constructor
        self.name = name
        self.age = age

    def getcgpa(self):
        return self.age
    
stu1 = Student("vashu",18)
stu2 = Student("pandit",24)

print(f"{stu1.age} has cgpa = {stu1.getcgpa()}")

#one parameter - unified
class Student:
    subj = "python" #attribute
    def __init__(self): # self - it stpring current instance of class -using current parameter of class
        print("constructor is called")


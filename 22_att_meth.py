#class contains 1.properties(attributes), 2.behaviours(methods)
#in prev class - subject , college , year are properties

#_init_method - initialize our object- called everytime automaticallly when we crete obj
class Student:
    subj = "python" #attribute
    def __init__(self, name): # self - it stpring current instance of class -using current parameter of class
        self.name = name
        print("constructor is called")

#stu1 = Student()
stu2 = Student("vashu")
print(stu2.name)
#many forms
#multiple functions - same name
#operator overloading 
#function overriding - inheritance - redefining parent class function in child class
#duck typing
class Employee:
    def get_designation(self):
        print("designation = Employee")
class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()
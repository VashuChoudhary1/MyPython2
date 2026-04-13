#inheritanc - parent class - child class
class Employee:
    start_time = "10 am"
    end_time = "6 pm"

    def change_time(self,new_end_time):
        self.end_time = new_end_time


#child class inherited properties from parent class
class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject
    

t1 = Teacher("Math")
print(t1.subject)
print(t1.end_time)
t1.change_time("4pm")
print(t1.end_time)
    
#Protected - when we want to private attribute but give access to sub class
#Private - when we want to private attr. as well as don't want to give access to sub class
#1.Single Level Inheritance - Employee - Adminstration
#2. Multi Level Inheritance - Employee - Teacher - Admin
class Employee:
    start_time = "9 am"
    end_time = "6 pm"

class Teacher(Employee):
    def __init__(self, subject):
        self.subject =  subject

class Admin(Teacher):
    def __init__(self, role):
        self.role = role
    
class Account(Admin):
    def __init__(self, salary,role):
        super().__init__(role) #invoke constructor of parent class
        self.salary = salary
    
acc1 = Account(50000,"HR")
print(acc1.role,acc1.salary,acc1.start_time)

staff1 = Admin("manager")
print(staff1.role,staff1.start_time,staff1.end_time)
       
        
        
#walks like a duck and quacks like a duck = duck
class Teacher():
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Accountant")

t1 = Accountant()
t1.get_designation()

t2= Teacher()
t2.get_designation()
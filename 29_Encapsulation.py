#wrapping up of data and funvtion into single unit - like capsule
#data hiding 
#attribute - public - inside class and outside class, protected - inside class as well as by sub class , private-inside class

class BankAccount:
    def __init__(self,name,balance,pin):
        self.name = name
        self._balance = balance #protected attribute
        self.__pin = pin #private - data mangling - we can't acces outside of class

    def get_pin(self): #we have to create getter function to access private value
        return self.__pin

    def set_newPin(self,newPin):
        self.__pin = newPin

acc1 = BankAccount("Vashu",100_0000,1234)
acc1.get_pin()
acc1.set_newPin(4567)
print(acc1.name,acc1._balance,acc1.get_pin())

#protected attribute can be accessed outside of class , but as developer we must decide we don't use attribute

















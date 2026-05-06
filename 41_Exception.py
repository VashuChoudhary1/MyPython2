#Exception handling - to hanle error in code
#first we create try block - code in which error can come 
#second we create except block - check for particular exception like x/0 
#we have many built in exceptions like ZeroDivisionError - if any no is divided by 0
#and then we create else block - when there is no error then else block executes
try:
    x = int(input("enter x: "))
    ans = 10/x    

except ZeroDivisionError:
    print(f"Number is divided by Zero here ")

except ValueError:
    print("You write invalid input only int value")

    

else:
    print(f"Answer : {ans}")
    print(f"ans = {ans}")

finally:
    print("Code End Here !")

#We also have one more keyword - final 
#final -  when exception is throught or not , no matter but it should be executed
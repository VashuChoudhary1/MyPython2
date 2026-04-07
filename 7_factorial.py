def cal_factorial(n):
    fact =1
    for i in range(1,n+1):
        fact *= i
    return fact

n = int(input("enter n"))
print(cal_factorial(n))
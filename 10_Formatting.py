#format function - format() - introduce by python3 - place holder{} , placement value
# f- string
a = 5
b= 10
sum = a+b
#normal formatting
print("sum is {}".format(sum))
print("language is {}".format("python"))
print("sum of {} & {} is {}".format(a,b,sum))

#index based formatting
print("sum of {1} & {0} is {2}".format (a,b,sum))

#value based formatting
print("values of var {a} & {b}".format(a=5,b=6))

print("My Name is {a} , and my brother name is {b}".format(a="Vashu", b = "Dev"))


#F-Strings
# we can directly definr value in {}
x = 10
y=20
print(f"summ of {x} & {y} is {x + y}")
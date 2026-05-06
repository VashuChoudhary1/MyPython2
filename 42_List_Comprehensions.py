# output for item in iterable if condition
# when we want to print any list

#option 1 using for loop
squares = []
for i in range(6):
    squares.append(i*i)

print(squares)

#Using List Comprehensions
sq = [ i*i for i in range(6) ]
print(sq)

#Print square only for odd numbers
sq2 = [ i*i for i in range(8) if(i%2 == 0)]
print(sq2)

# for n in value we want 0 , if value <0 else value

nums = [-2,-3,5,2,-8]
nums = [0 if val<0 else val for val in nums]
print(nums)

words = [ "hello","python","programming","learn"]
#print(words[0].upper)
words = [val.upper() for val in words]
print(words)
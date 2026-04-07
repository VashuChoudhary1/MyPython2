#methods are just like functions

values = [1,2,3,5,6]
#append(val) - add one element at the end
values.append(7)
print(values)

#insert(idx , val) - insert element at index
values.insert(3,4)
print(values)

#sort() - aeeanges in increasing order
nums = [1,3,4,0,10,7]
nums.sort()
print(nums)

#decreasing order
nums.sort(reverse=True)
print(nums)

#reverse() - reverse order
values.reverse()
print(values)
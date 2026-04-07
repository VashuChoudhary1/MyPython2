#for loop
nums = [1,2,3,10,4]
for val in nums:
    print(val)

#linear search
array = [1,3,4,6,8,10,12,5]
x = 8
idx = 0
for val in array:
    if(val == x):
        print(f"x found at idx = {idx}")
        break
    idx+=1
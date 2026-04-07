tup = (1,2,3,4,2,5)

sum =0
for val in tup:
    sum += val
print(f"sum of numvers is {sum}")

#index(val) - returns 1st occurence idx
print(tup.index(2))

#count(val) - counts total occurences

print(tup.count(2))
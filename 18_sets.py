#collection of unique elements
#set can be mutable , but elements are immmutable
#duplicate is counted as single
# {} are used in dict as well as in set , when we write empty {} it is read as dict
s={1,2,2,2,3,4}
s.add(5)
print(type(s))
print(len(s))
print(s)
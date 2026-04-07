#Given a list of tuples with info(name, subject):
#list all unique course, list students enrolled in english , create dictionary (students, set of course)

info = {
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
}

unique_course = set()
for tup in info:
   # print(tup[0])#name
    print(tup[1])#course
    unique_course.add(tup[1])

print(unique_course)

for name, course in info:
    print(name,course)

for name,course in info:
    if(course== "English"):
        print(name)


dict = {}
for name,course in info:
    if(dict.get(name)== None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
    
print(dict)
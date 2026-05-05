#All Modes are like -

#r - read,
#  w - writing ,
#  x - creates new & open for writing, 
# a - writing,appends at end
# b - binary mode , 
# t - text mode , 
# + - opend disk file for update (r & w)

#f = open("36_sample.txt","a")
#f.write(" \n New Text is added to original text \n via append function - a")

#f2 = open("37_sample.txt","x") ##creates new file
#f2.write("Text in new sample fine via x ")

# diff b/w x and w is - w ,overwrites the existing file and create new but x through an error if that file is already present.
#we also can use combination of modes rd, wrmlike
# imp is r+ , w+ , a+
#in r+ - in it when we try to write after read , new word overrite the old characters from starting and all other remain same for reading

f3 = open("37_sample.txt","r+")
f3.write("123")
print(f3.read())

# in a+ - characters are just add at the end of old text
f4 = open("37_sample.txt","a+")
f4.write("567")
print(f4.read())

#in w+ it overwrites all data 
f5 = open("37_sample.txt","w+")
f5.write("10, 11, 12")
print(f5.read())

f3.close()
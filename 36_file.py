#We first open a file , then hold that file data in function 
#then read that function and print data

f = open("36_sample.txt","r") #return file object
f1 = open("36_sample.txt","w") #return file object
data = f.read()
print(data)
print(type(data))
data2 = f.readline()
print(data2)

f1.write("Text to overwrite \n the complete data") #it changes all text from txt file


f.close()
#we always should close the file 


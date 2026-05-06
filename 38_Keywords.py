#As when we open an file we have to close it ,so that it can't get corrupted
#To perform this in simple ways we use with keyword
with open("37_sample.txt","r") as f: #we take f as variable - file object
   # print(f.read())
    data = f.read()
    print(len(data))
data = True
line = 1
with open("40_word_ans.txt","r") as f:
    while data:
        data = f.readline()

        if("Python" in data):
           print("word found")
           print(f"word found at line number {line}")
           break

        
        print(data)
        line +=1



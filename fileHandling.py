'''
# Open a file and read its content

# f = open("file.txt")
# data = f.read()
# print(data)
# # f.write("aa e aa e ee aa aa")
# f.close()

# Open a file and write to it

# st = "Hello brother, you are amazing"
 
# f = open("myfile.txt", "w")
# f.write(st)
# f.close()

# Using readlines() and readline()

# lines = f.readlines()
# print(lines, type(lines))              # type: list

# line1 = f.readline()    # type: str
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()

# print(line1, line2, line3, line4)
# print(type(line1))

# Effective way to print the above lines(Using loops)

# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()

# f.close()

# Append mode

# st = "\nWhat's up, What's up?"
# f = open("myfile.txt", "a")
# f.write(st)
# f.close()

# using with Statement

# with open("file.txt") as f:
#     print(f.read())             #you dont need to explicitly close the file'
'''

#     -------------------PRACTICE QUESTIONS------------------------

#1: Wap to read the text from a given file "poems.txt" and find out whether it contains the word "Twinkle"

f = open("poems.txt", "r")
content = f.read()

if("Twinkle" in content):
    print("Twinkle word is present in the file.")
else:
    print("Twinkle word is not present in the file")

f.close()

#2: The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file "highScore.txt" which is either blank or contains the previous High_Score. wap to update the hi-score whenever the game() function breaks the high-Score 

import random

def game():
    print("You are playing the game: ")
    score = random.randint(1,101)
    #fetching high-score
    with open("highScore.txt", "r") as f:
         high_score = f.read()
         if(high_score != ""):
             high_score = int(high_score)
         else:
             high_score = 0
        
    print(f"Your Score = {score}")
    if(score>high_score):
        with open("highScore.txt", "w") as f:
            f.write(str(score))

    return score   

game()

#3: Wap to generate multiplication tables from 2 to 20 and write it to the diffferent files. place these files in a folder for a 13 year old

def generateTable(n):
    table = ""
    for i in range(1,11):
        table = table + f"{n} X {i} = {n*i}\n"
    with open(f"Tables/table{n}.txt", "w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)

#4: A file contains a word "donkey" multiple times. wap which replaces this word with #### by updating the same file

content = ""
with open("donkey.txt", "r") as f:
    content = f.read()

word = "donkey"
st = "####"
contentNew = content.replace(word, st)

with open("donkey.txt", "w") as f:
    f.write(contentNew)

        
#5: wap to mine a log file and find out whether it contains 'python' and in which line it is present

with open("log.txt") as f:
    lines = f.readlines()
# print(lines)
lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes, python is present. Line no. {lineno}")
        break
    lineno += 1

else:
    print("no, python is not present")

#6: Wap to find out whether a file is identical and matches the content of another file

with open("file.txt") as f:
    content1 = f.read()

with open("poems.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes, identical hai")
else:
    print("No, Identical nahi hai")











   
# Chapter-6: Conditional statements

#1: Wap to find the greatest of four numbers entered by the user

a = int(input("Enter no. 1: "))
b = int(input("Enter no. 2: "))
c = int(input("Enter no. 3: "))
d = int(input("Enter no. 4: "))

if(a>b and a>c and a>d):
    print(f"{a} is the greatest")

elif(b>c and b>a and b>d):
    print(f"{b} is the greatest")

elif(c>a and c>b and c>d):
    print(f"{c} is the greatest")

else:
    print(f"{d} is the greatest")

#2: Wap to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

hindi = float(input("Marks in hindi: "))
english = float(input("Marks in english: "))
maths = float(input("Marks in maths: "))
total = hindi+english+maths
percent = total/3  #Assuming each subject to be of 100 marks

if(percent>=40 and hindi>=33 and english>=33 and maths>=33):
    print("Passed!!!")
else:
    print("Failed!!!")

#3: Wap to to find whether a given username contains less than 10 characters or not
username = input("Enter your userName: ")

if(len(username)<10):
    print("The username contains less than 10 characters.")

elif(len(username)==10):
    print("The username contains exactly 10 characters.")

else:
    print("The username contains more than 10 characters.")

#4: Wap which finds out whether a given name is present in a list or not

l = ["Aditya", "Abhinav", "Manuj", "Rahul", "Punit", "Anzar"]

findName = input("Enter name to search: ")

if(findName in l):
    print(f"{findName} is present in the list at {l.index(findName)} index")
else:
    print(f"{findName} is not present in the list.")

#5:Wap to calculate the grade of a student from his marks

totalMarks = int(input("Enter your total marks of all subjects: "))
fullMarks = int(input("Enter full marks of all subjects: "))
percent = totalMarks/fullMarks*100

if(percent>=90):
    print("Grade: Excellent!")
elif(percent>=80):
    print("Grade: 'A'")
elif(percent>=70):
    print("Grade: 'B'")
elif(percent>=60):
    print("Grade: 'C'")
elif(percent>=50):
    print("Grade: 'D'")
elif(percent<50):
    print("Grade: 'E'")

#6: A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Wap to detect these spams

k = "Make a lot of money"
l = "buy now"
m = "subscribe this"
n = "click this"

msg = input("Type message here: ")

if(k in msg) or (l in msg) or (m in msg) or (n in msg):
    print("This comment is a spam!")
else:
    print("This comment is not a spam comment")



   


# Chapter-12: Advanced Python 1

#1: Wap to open three files 1.txt, 2.txt, 3.txt if any of these files are not present, a message without exiting the program must be printed prompting the same

# files = ["1.txt", "2.txt", "3.txt"]

# for file in files:
#     try:
#         with open(file, "r") as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f"File '{file}' not found.")

# print("Done")


#2: Wap to print third, fifth and seventh element from a list using enumerate function

listOfNum = [1,2,3,4,5,6,7,8,9,10]

for index, item in enumerate(listOfNum, start=1):
    if index in [3,5,7]:
        print(f"{index}th element is {item}")

#3: Write a list comprehension to print a list which contains the multiplication table of a user entered number

n = int(input("Enter the number to get the table of: "))

table = [n*i for i in range(1,11)]
print(table)

#4: Wap to display a/b where a and b are integers, if b=0, display infinite by handling the 'ZeroDivisionError'.

try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(f"a/b = {a/b}")
except ZeroDivisionError as e:
    print("a/b = infinite")

#5: Store the multiplication table generated in #3 in a file named Tables.txt

with open("fileoftable.txt", "a") as f:
    f.write(f"Table of {n}:\n{table}\n")


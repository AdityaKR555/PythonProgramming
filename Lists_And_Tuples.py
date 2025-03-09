# Chapter-4: Lists and Tuples

#1: Wap to store seven fruits in a list entered by the user

fruits = []
f1 = input("Enter fruit One name: ")
f2 = input("Enter fruit Two name: ")
f3 = input("Enter fruit Three name: ")
f4 = input("Enter fruit Four name: ")
f5 = input("Enter fruit Five name: ")
f6 = input("Enter fruit Six name: ")
f7 = input("Enter fruit Seven name: ")
fruits.append(f1)
fruits.append(f2)
fruits.append(f3)
fruits.append(f4)
fruits.append(f5)
fruits.append(f6)
fruits.append(f7)
print(fruits)

#2: Wap to accept marks of six students and display them in sorted manner

marks = []
student1 = int(input("Enter 1st Student marks: "))
student2 = int(input("Enter 2nd Student marks: "))
student3 = int(input("Enter 3rd Student marks: "))
student4 = int(input("Enter 4th Student marks: "))
student5 = int(input("Enter 5th Student marks: "))
student6 = int(input("Enter 6th Student marks: "))
marks.append(student1)
marks.append(student2)
marks.append(student3)
marks.append(student4)
marks.append(student5)
marks.append(student6)
marks.sort()
print(marks)

#3: Check that a tuple type cannot be changed
tuple = (33, 44, "Aditya", 77)
tuple[2] = "Chotu"   #tuples are immutable like strings, their values cannot be changed
print(tuple)         #throws error   

#4: Wap to sum a list of Four numbers
numbers = [10,20,30,40]
summ = numbers[0]+numbers[1]+numbers[2]+numbers[3]
print(summ)
# or simply we can just use the sum(list) function
print(sum(numbers))

#5: Wap to count the numbers of zeros in the following tuple

tup = (7,8,9,0,0,9,32,0)
n = tup.count(0)
print(f"No of times 0 occurs in the tuple = {n}")




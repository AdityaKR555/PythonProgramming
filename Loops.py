# Chapter-7: Loops

#1: Wap to print multiplication table of a given no. using for loop

number = int(input("Enter a number to print table of: "))
for i in range(1,11):
    print(f"{number} * {i} = {number*i}")

#2: Wap to greet all the person names stored in a list 'l' and starts with S

l = ["Aditya", "Sanjeev", "Sanjay", "Sejal", "Shah Rukh", "Rahul", "Harry"]
for i in l:
    if(i.startswith("S")):
        print(f"Hello, {i} have a nice day")


#3: Attempt ques-1 with while loop

number = int(input("Enter a number to print table of: "))
k = 1
while(k<=10):
    print(f"{number} * {k} = {number*k}")
    k+=1

#4: Wap to find out whether a no. is prime or not

isPrime = True
number = int(input("Enter a number to find out it's prime or not: "))
half = int(number/2)
for i in range(2,half):
    if(number%i==0):
        isPrime = False

print(f"{number} is prime: {isPrime}")

import math

number = int(input("Enter a number to check if it's prime: "))

# Handle edge cases
if number < 2:
    print(f"{number} is not a prime number.")
else:
    isPrime = True
    for i in range(2, int(math.sqrt(number)) + 1):  # Checking up to sqrt(number)
        if number % i == 0:
            isPrime = False
            break  # No need to check further

    print(f"{number} is prime: {isPrime}")


#5: Wap to find the sum of first n natural numbers using while loop

limit = int(input("Enter limit: "))
x = 1
sum = 0
while(x<=limit):
    sum+=x
    x+=1
print("Sum = ",sum)

# #6: Wap to find factorial of a number using for loop

factorial = 1
number = int(input("Enter a number to factorial of: "))
for i in range(1,number+1):
    factorial = factorial*i
print(f"Factorial of {number} is {factorial}")

'''#7:
 Wap to print *
             ***
            *****   star pattern for n=3 '''

n = 3
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print("")

'''#8: 
    Wap to print *
                 **
                 *** for n = 3 '''

for i in range(1,n+1):
    print("*"*(i))

'''#9: 
      Wap to print ***
                   * *
                   *** for n = 3 '''

for i in range(1,n+1):
    if(i == 1 or i == n):
        print("*"*(n), end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")
    

#10: Print multiplication table in reverse order
n = 10
for i in range(10,0,-1):
    print(f"{n} X {i} = {n*i}")

#or 
# for i in range(1,11):
#     print(f"{n} X {11-i} = {n*(11-i)}")    
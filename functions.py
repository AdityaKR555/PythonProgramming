# Chapter-8: Functions and Recursions

# def avg():
#     a = int(input("enter no. 1: "))
#     b = int(input("enter no. 2: "))
#     print((a+b)/2)

# avg()


# #1: Wap using functions to find greatest of three numbers

def greatest(a,b,c):
    if(a>b and a>c):
        greatest = a
    elif(b>a and b>c):
        greatest = b
    else:
        greatest = c
    return greatest

print("Greatest no. is: ", greatest(78,89,32))

# #2: Wap to convert fahrenhite to celcius

def convert(f):
    return 5*(f-32)/9


f = int(input("Enter temperature in fahrenhite: "))
c = round(convert(f), 2)
print(c,"degree celcius")

# #3: Prevent print() function to print a new line

print("Hello....", end="")
print("Sir....")


#4: Write a recursive function to calculate the sum of first n natural numbers

def sum_of_natural_numbers(n):
    if(n == 1):
        return 1
    sum = n + sum_of_natural_numbers(n-1)
    return sum

limit = int(input("Enter limit: "))
ans = sum_of_natural_numbers(limit)
print(f"Sum of natural numbers till {limit} is {ans}")

''' #5: Write a function to print first n lines of the following pattern:-
                                ***
                                **
                                *                                       '''

def pattern(NumOflines):
    
    if(NumOflines == 0):
        return 
    print("*"*NumOflines)
    pattern(NumOflines-1)


lines = int(input("Enter no. of lines: "))
pattern(lines)

#6: Write a function that converts inches to cm

def inch_to_cm(inch):
    return 2.54*inches

inches = int(input("Enter value(in inches): "))
print(f"{inches} inches = {inch_to_cm(inches)} cm")

#7: Write a function to remove a given word from a list ad strip it at the same time

def remove_word(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Aditya", "Aayushi", "Ayush", "Aditi", "sh"]
print(remove_word(l,"sh"))


#8: Write a function to print multiplication table of a given number

def table(number):
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")

number = int(input("Enter number to print table of: "))
table(number)



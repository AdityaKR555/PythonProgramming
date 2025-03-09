#1: find sum of digits of a number

n = int(input("Enter the number: "))
m = n
sum = 0
while(n>0):
    sum = sum + (n%10)
    n = n//10
print(f"Sum of digits of {m} is {sum}")

#2: find product of digits of a number

n = int(input("Enter the number: "))
product = 1
while(n>0):
    product = product * (n%10)
    n = n//10
print("Product = ", product)

#3: find sum of square of digits of a number

n = int(input("Enter the number: "))
sum = 0
while(n>0):
    x = n%10
    sum = sum + x*x
    n = n//10
print(f"Sum of square of digits is {sum}")

#4: find sum of cube of digits of a number

n = int(input("Enter the number: "))
sum = 0
while(n>0):
    sum = sum + (n%10)**3
    n = n//10
print(f"Sum of digits of {m} is {sum}")

#5: find whether a number is armstrong or not

n = int(input("Enter the number to check whether its armstrong or not: "))
m = n
sum = 0
x = len(str(n))
while(n>0):
    sum = sum + (n%10)**x
    n = n//10
if(m == sum):
    print(f"Yes, {m} is a armstrong number.")
else:
    print(f"No, {m} is not armstrong number.")

#6: Find reverse of a given number

n = int(input("Enter the number: "))
reverse = 0
while n>0:
    # x = n%10
    reverse = reverse*10 + n%10
    n = n//10   
print(reverse) 

#7: Check whether a number is palindrome or not

n = int(input("Enter the number: "))
m = n
reverse = 0
while n>0:
    reverse = reverse*10 + n%10
    n = n//10 
if(m == reverse):
    print("Palindrome!")
else:
    print("Not a palindrome")

#8: find sum of even digits and product of odd digits of a given number

n = int(input("Enter the number: "))
sum = 0
product = 1
while n>0:
    ld = n%10
    if(ld%2==0):
        sum = sum + ld
    else:
        product = product * ld
    
    n = n//10
print(f"Sum of even numbers = {sum}")
print(f"Product of odd numbers = {product}")


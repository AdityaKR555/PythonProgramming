#lambda
'''
square = lambda x : x*x
cube = lambda x : x*x*x

print(square(5))
print(cube(5))

#join
a = ["Anupriya", "Sumit", "Aayushi"]
final = " loves ".join(a)
print(final)

#format
a = "{} is a good {}".format("Aditya", "boy")
b = "{1} is a good {0}".format("Aditya", "boy")
print(a)
print(b)

#map
l = [1,2,3,4,5]
sqList = map(square, l)
print(sqList)
print(list(sqList))

#filter
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

#reduce
from functools import reduce
sum = lambda a,b : a+b
print(reduce(sum, l))
'''

#3: Print table of 7 in vertical which is stored in a list
#mulTable = ["7","14","21","28","35","42","49","56","63","70"]
mulTable = [str(7*i) for i in range(0,11)]
verticalTable = "\n".join(mulTable)
print(verticalTable)

#4: Wap to filter a list of numbers which are divisible by 5.
numList = [1,2,3,4,5,13,15,130,150,135,545]
def divByFive(n):
    if(n%5 == 0):
        return True
    return False
x = filter(divByFive, numList)
print(list(x))

#5: Wap to find the maximum of the numbers in a list using the reduce function
from functools import reduce
# def maxNum(l):
    # max = l[0]
    # for i in l:
    #     if i > max:
    #         max = i
    # return max
def maxNum(a,b):
    if(a>b):
        return a
    return b

l = [5,10,15,20]
print(reduce(maxNum, l))
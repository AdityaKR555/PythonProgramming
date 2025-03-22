# Chapter-10: Object oriented programming

# class Employee:
#     name = "Aditya"
#     salary = 1700000

# akr = Employee()
# print(akr.name, akr.salary)
# akr.name = "Aditya kumar rai"
# print(akr.name, akr.salary)

#1: Create a class "programmer" for storing information of few programmers working at microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getInfo(self):
        print(f"Name = {self.name}, Company = {self.company}, salary = {self.salary}")

aditya = Programmer("Aditya", 1200000)
ayush = Programmer("Ayush", 600000)

aditya.getInfo()
ayush.getInfo()

#2: Write a class "Calculator" capable of finding square, cube and square root of a number

class Calculator:

    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num*self.num
    
    def cube(self):
        return self.num**3
    
    def sqrroot(self):
        return self.num**(1/2)
    
a = Calculator(4)
print("Square root: ", a.sqrroot())
print("Cube: ", a.cube())
print("Square: ", a.square())

#3: Add a static method in #2, to greet user with hello

class Calculator2:

    @staticmethod
    def greet():
        print("Hello, user!")

a = Calculator2()
a.greet()

#4: Write a class Train which has methods to book a ticket, get status(no of seats) and get fare information of train runnning under Indian Railways

from random import randint

class Train:

    def __init__(self, trainNo, fro, to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to
    
    def book(self):
        print(f"Ticket is booked in train no. {self.trainNo} from {self.fro} to {self.to}.")

    def getStatus(self):
        print(f"Train no. {self.trainNo} is running on time")

    def getFare(self):
        print(f"Ticket fare in {self.trainNo} from {self.fro} to {self.to} is {randint(800,3000)}")

rajdhani = Train(13479, "New-Delhi", "Barauni jn.")
rajdhani.book()
rajdhani.getFare()
rajdhani.getStatus()



    

    

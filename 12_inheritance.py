# # Chapter-11: Inheritance

# #1: Create a class(2-D vector) and use it to create another class representing a 3-D vector.

# # class Two_D_Vector:
# #     def __init__(self,i,j):
# #         self.i = i
# #         self.j = j

# #     def show(self):
# #         print(f"The vector is {self.i}i + {self.j}j")
        
# # class Three_D_Vector(Two_D_Vector):
# #     def __init__(self,i,j,k):
# #         super().__init__(i,j)
# #         self.k = k

# #     def show(self):
# #         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

# # a = Two_D_Vector(5,10)
# # b = Three_D_Vector(5,10,15)

# # a.show()
# # b.show()

# #2: Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'.

# class Animal:
#     def __init__(self,name):
#         self.name = name 

# class Pets(Animal):
#     def __init__(self, name):
#         super().__init__(name)

# class Dog(Pets):
#     def __init__(self, name):
#         super().__init__(name)

#     def bark(self):
#         print(f"{self.name} is barking...")

# cat = Animal("xyz")
# puppy = Pets("Diana")
# doggy = Dog("kutta")
# doggy.bark()
# print(cat.name, puppy.name, doggy.name)

# #3: Create a class 'Employee' and add salary and increment properties to it, Write a method 'salaryAfterIncrement' with a @property decorator with a setter which changes the value of increment based on the salary

# class Employee:
#     def __init__(self, salary, increment):
#         self.salary = salary
#         self.increment = increment  # Increment is a percentage (e.g., 10 for 10%)

#     @property
#     def salaryAfterIncrement(self):
#         """Calculates the new salary after applying the increment."""
#         return self.salary + (self.salary * self.increment / 100)

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, new_increment):
#         """Sets a new increment based on the updated salary."""
#         self.increment = (new_increment - self.salary) * 100 / self.salary

# # Example Usage
# emp = Employee(50000, 10)
# print("Current Salary:", emp.salary)
# print("Salary After Increment:", emp.salaryAfterIncrement)

# # Updating increment based on a new salary
# emp.salaryAfterIncrement = 60000  # Setting new salary to 60000
# print("Updated Increment:", emp.increment)
# print("New Salary After Increment:", emp.salaryAfterIncrement)


# #4: Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.

# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i
    
#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         return Complex(self.r * c2.r - self.i * c2.i, self.r * c2.i + self.i * c2.r)

#     def __str__(self):
#         return f"{self.r} + {self.i}i"
    
# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# print(c1 + c2)
# print(c1 * c2)

#5: Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them

# class Vector:
    
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result
    
#     def __mul__(self, other):
#         result = self.x*other.x + self.y*other.y + self.z*other.z
#         return result
    
#     def __str__(self):
#         return f"Vector({self.x}, {self.y}, {self.z})"
    
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)

# print(v1 + v2)
# print(v1 * v2)

#6: Write __str__() method to print the vector as 7i + 8j + 10k

class Vector2:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
v4 = Vector2(3, 4, 5)
print(v4)

#7: Override the ___len__() method on vector of #5 to display the dimension of the vector

class Vector:
    
    def __init__(self, list):
        self.list = list
      
    def __len__(self):
        return len(self.list)

v1 = Vector([1, 2, 3])
print(len(v1))
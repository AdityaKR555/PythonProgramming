# Chapter-5: Dictionaries and sets

#1: Wap to create a dictionary of hindi words with values as their English translatio. provide user with an option to look it up

dictionary = {
    "madad" : "Help",
    "kursi" : "Chair",
    "kutta" : "Dog"
}
x = input("Enter word you want to know meaning of: ")
print(dictionary[x])

#2: Wap to input eight numbers from the user and display all the unique numbers(once)

s = set()
x = int(input("Enter number: "))
s.add(x)
x = int(input("Enter number: "))
s.add(x)
x = int(input("Enter number: "))
s.add(x)
x = int(input("Enter number: "))
s.add(x)
x = int(input("Enter number: "))
s.add(x)
x = int(input("Enter number: "))
s.add(x)
x = int(input("Enter number: "))
s.add(x)
x = int(input("Enter number: "))
s.add(x)

print(s)  # printing set s

#3: Can we have a set with 18(int) and '18'(str) as a value in it

set = {3,4,7,9,18,"akr","18"}
print(set)                      # so, YES we can have them as a value in a set

#4: Length of the following set

st = set()
st.add(20)
st.add(20.0)
st.add('20')
print(st, len(st))            # Length = 2 that means it considers same magnitude equal for int and float

#5: Type of ss
ss = {}
print(type(ss))          # Type = dictionary, To declare: Empty dict = {} , Empty set = set()

#6: Create a empty dictionary. Allow 4 friends to enter their favourite language as value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})

name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})

name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})

name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})

print(d)



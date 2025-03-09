a = "Aditya"
print(a[0:5])
print(a[-6:-1])
print(a[2:])    #same as a[2:length-1]
print(a[:6])    #same as a[0:6]

#1: display a user entered name followed by good afternoon

name = (input("Enter your name: "))
print("Good Afternoon,",name)  #can also write as print(f"Good Afternoon, {name}") :f string

#2: Fill a letter template

letter = '''
       Dear <|Name|>
       You are selected!
       <|Date|>
       '''
date = input("Enter date: ")
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))

#3: Detect double space in a string and replace it with single space

sent = "i am learning  python right  now"
print(f"double space at index : {sent.find("  ")}")
print(sent.replace("  ", " "))

#4: format a letter using space sequence characters

letter2 = "  Dear Aditya,\n\tThis python course is nice.\n\tThanks!" #escape sequence characters are added
print(letter2)


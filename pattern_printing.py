# i = 1
# while(i<=5):
#     j = 1
#     while(j<=i):
#         print("*", end="")
#         j = j+1
#     print("")
#     i = i+1

'''
    *
   **
  ***
 ****
*****
'''

# Method-1

# i = 5
# while(i>=1):
#     j = 1
#     while(j<=5):
#         if(j>=i):
#             print("*", end="")
#         else:
#             print(" ", end="")
#         j = j+1
#     print("")
#     i = i-1

# Method-2

i = 1
while(i<=5):
    j = 1
    while(j<=5):
        if(j>5-i):
            print("*", end="")
        else:
            print(" ", end="")
        j = j+1
    print("")
    i = i+1
    


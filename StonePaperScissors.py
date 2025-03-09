# import random
# choices = ['r', 'p', 's']


# print("\nWelcome to Stone, Paper and Scissors Game: ")
# print("\tRules\nChoose R for Rock\nChoose P for Paper,and\nChoose S for scissor")
# print("Press 1 to exit the game...")

# while(True):
#     userInput = input("Your Choice: ")
#     compInput = random.choice(choices)

#     if(userInput == '1'):
#         break
 
#     elif(not(userInput == 'r' or userInput == 'p' or userInput == 's')):
#         print("Invalid Choice...")
#         continue
    
#     elif(compInput == userInput):
#         print("DRAW!!!")

#     elif (userInput=='r' and compInput=='s') or (userInput=='p' and compInput=='r') or (userInput=='s' and compInput=='p'):
#         print("You WON!!!")

#     else:
#         print("you LOSE!!!")
# print("GAME OVER!")

import random

choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

print("\nWelcome to Rock, Paper, Scissors Game!")
print("\tRules:")
print("Choose 'R' for Rock")
print("Choose 'P' for Paper")
print("Choose 'S' for Scissors")
print("Press '1' to exit the game.")

while True:
    userInput = input("\nYour Choice: ")

    if userInput == '1':  # Check before converting to lowercase
        break

    userInput = userInput.lower()  # Convert only if it's not '1'

    if userInput not in choices:
        print("Invalid Choice. Please enter R, P, or S.")
        continue

    compInput = random.choice(list(choices.keys()))  # Random choice from dictionary

    print(f"\nYou chose {choices[userInput]}. Computer chose {choices[compInput]}.")

    if compInput == userInput:
        print("🚩 It's a DRAW!")

    elif (userInput == 'r' and compInput == 's') or (userInput == 'p' and compInput == 'r') or (userInput == 's' and compInput == 'p'):
        print("🎉 You WON!")

    else:
        print("😢 You LOSE!")

print("GAME OVER! Thanks for playing! 🎮")



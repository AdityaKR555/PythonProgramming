# GAME-2: THE PERFECT GUESS

import random

n = random.randint(1,100)
a = -1
guesses = 0
print("Guess a number between 1 and 100")
while(a != n):
    a = int(input("Guess the number: "))
    if(a > n):
        print("Lower number please")
    elif(a < n):
        print("Higher number please")
    guesses += 1

print(f"You have guessed the correct number {n} in {guesses} attempts")
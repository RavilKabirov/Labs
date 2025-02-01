import random

name = input("Hello! What is your name?")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
s = random.randint(1, 20)
d = 0
while(True):
    a = int(input())
    if(a < s):
        print("Your guess is too low.")
        print("Take a guess.")
        d += 1
    elif(a > s):
        print("Your guess is too high.")
        print("Take a guess.")
        d += 1
    else:
        print(f"Good job, {name}! You guessed my number in {d + 1} guesses!")
        break
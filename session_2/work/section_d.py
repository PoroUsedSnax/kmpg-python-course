from random import randint, choice
from math import floor

i = 0
while i < 10:
    print(randint(1, 10))
    i += 1

guess = int(input("Guess my number: "))
num = randint(1, 10)
while guess != num:
    guess = int(input("Wrong number, try again!: "))

print("Wow lucky number " + str(num) + "!")

width = int(input("Input a rectangle width: "))
height = int(input("Input a rectangle height: "))

print(str(floor((width * height) / 10000)) + "m2")

i = 0
password = input("What is your password?: ")
while i < 4:
    if password == "qwerty123":
        print("You have successfully logged in")
        break
    elif i == 3:
        print("System Locked!")
        break
    else:
        input("Password failure, try again: ")
        i += 1
    
userInput = None
aiInput = None
plays = 0
score = []

while plays < 3:
    userInput = input("Rock, Paper or Scissors?: ")
    aiInput = choice(["Rock", "Paper", "Scissors"])
    plays += 1
    if "Rock" in userInput:
        if "Rock" in aiInput:
            score.append("Draw")
        elif "Paper" in aiInput:
            score.append("Loss")
        else:
            score.append("Win")
    elif "Paper" in userInput:
        if "Rock" in aiInput:
            score.append("Win")
        elif "Paper" in aiInput:
            score.append("Draw")
        else:
            score.append("Loss")
    else:
        if "Rock" in aiInput:
            score.append("Loss")
        elif "Paper" in aiInput:
            score.append("Win")
        else:
            score.append("Draw")
print(score)
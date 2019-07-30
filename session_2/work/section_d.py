from random import randint
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
    


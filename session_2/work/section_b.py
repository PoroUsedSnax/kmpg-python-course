username = input("What is your name?: ")

if username == "Alice":
    print("Hello, Alice")
elif username == "Bob":
    print("You're not Bob! I'm Bob")
else:
    print("You must be Charlie")

age = int(input("What is your age?: "))

if age < 11:
    print("You're too young to go to this school")
elif age >= 11 and age <= 16:
    print("You can come to this school")
elif age > 16:
    print("You're too old to go to this school")
elif age == 0:
    print("You're not born yet!")

month = input("Input a month: ")

if month == "March" or month == "April" or month == "May":
    print("Is in spring")
elif month == "June" or month == "July" or month == "August":
    print("Is in Summer")
elif month == "September" or month == "October" or month == "November":
    print("Is in Autumn")
elif month == "December" or month == "January" or month == "February":
    print("Is in Winter")

num1 = int(input("Input a number: "))
num2 = int(input("Input a second number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Even")
elif num1 % 2 == 1 and num2 % 2 == 1:
    print("Odd")
else:
    print(str(num1 + num2))
 
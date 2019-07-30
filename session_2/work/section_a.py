username = input("What is your name?\n")

if username == "Bob":
    print("Welcome Bob!")

if username != "Alice":
    print("You're not Alice!")

password = input("What is your password?\n")

if password == "qwerty123":
    print("You have successfully logged in")
else:
    print("Password failure")

number = int(input("Input a number\n"))

if number % 2 != 1:
    print("Even")
else:
    print("Odd")

num1 = int(input("Insert a number\n"))
num2 = int(input("Insert a second number\n"))

if (num1 + num2) > 21:
    print("Bust")
else:
    print("Safe")
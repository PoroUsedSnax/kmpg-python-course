list = []
for num in range(1, 101):
    list.append(num)

print(str(list) + "\n")

list = []
for num in range(1, 101, 2):
    list.append(num)

print(str(list) + "\n")

list = []
for num in range(1896, 2020, 4):
    list.append(num)

print(str(list) + "\n")

list = []
for num in range(1, 101):
    if num % 3 == 0:
        list.append("Fizz")
    elif num % 5 == 0:
        list.append("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        list.append("FizzBuzz")
    else:
        list.append(num)

print(list)
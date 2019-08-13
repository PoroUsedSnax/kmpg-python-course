def print_name():
    print("Mark")

print_name()

def hello(name):
    print("Hello, " + name)

hello("Mark")

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(hello(name))

def is_odd(x):
    if (x % 2) == 1:
        return True
    else:
        return False

print(is_odd(1))
print(is_odd(2))

def reverse(string):
    print(string[::-1])

reverse("Hello")
reverse("Hello my name is John")
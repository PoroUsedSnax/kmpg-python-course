# [fit] IHF: Code
## Python — Session 1

---

# [fit] What is programming?

---

# [fit] What is Python?

---

# [fit] What's it used for?

---

# [fit] Who uses it?

---

# Racing with Python

---

# Hello, World!

---

# Hello, World! — Example
```python
print("Hello, World!")
```

---

# Naming Python Files

---

# Naming Python Files

```
<what_the_script_does>.py
```
---

# Naming Python Files

```
hello_world.py
number_guess.py
tic_tac_toe.py
calculate_totals.py
send_emails.py
```

---

# Running a Python Script

---

# Running a Python Script

[.code-highlight: 1]
[.code-highlight: 3]
```
$ python <name_of_file.py>

$ python hello_world.py
```

---

# Running a Python Script

[.code-highlight: 1]
[.code-highlight: all]
```
$ python hello_world.py
Hello, World!
$
```

---

# Text Editor

---

# Hello, world!
#### Code:

```python
print("Hello, <your name here>")
```

#### To Run:

```
$ python <file_name.py>
```

---

# Variables

---

# Variables

```python
<variable_name> = <value>
```

---

# Variables

- Any mix of letters, numbers and some special characters
- Must start with a letter
- Keep lowercase
- Use underscore where there are spaces

---

# Variables

```python
name = "Charlie"
age = 27
left_to_pay = 29.99
has_paid = False
```

---

# Data Types

---

# Strings

---

# Strings

```python
name = "Alice"
address = "123 Station Road"
favourite_food = "Pizza"
```

---

# Escaping

---

# Escaping

```
\" = Double Quote
\n = New line
\t = Tab
```

---
# Escaping

```python
favourite_food = "Pizza from \"Dough N' Sauce\""
shopping_list = "Apples\nBread\nMilk\nEggs"
```

---

# [fit]Coding Time
## Section A

---

# Integers

---

# Integers

```python
age = 17
days_in_january = 31
bottles_sitting_on_the_wall = 99
```

----

# Floats

----

# Floats

```python
price = 12.99
percent = 34.57
pi = 3.1415
```

---

# Boolean

---

# Boolean

```python
has_paid = True
vip = False
```

---

# None

---

# None

```python
last_film_seen = None
items_in_basket = None
```

---

# Numerical Operators

---

# Numerical Operators

| Operator | Action | Example |
| --- | --- | --- |
| + | Addition | `1 + 2` |
| - | Subtraction | `3 - 1` |
| * | Multiplication | `3 * 7` |
| / | Division | `9 / 3` |
| ** | Exponent | `4 ** 2` |
| % | Modulus (remainer) | `10 % 3` |

---

# Numerical Operators

```python
print(1 + 2)
print(5 - 3)
print(3 * 7)
print(49 / 7)
print(4 ** 2)
print(10 % 3)
```

---

# Numerical Operators

[.code-highlight: 1-2]
[.code-highlight: 3]
```python
x = 3
y = 6
area = x * y
```

---

# Concatenation

---

# Concatenation

[.code-highlight: 1-2]
[.code-highlight: 3]
[.code-highlight: 1,5]
[.code-highlight: 1-3,6]
```python
first_name = "Bob"
last_name = "Jones"
full_name = first_name + " " + last_name

print("Hello " + first_name)
print("Good morning, " + full_name)
```

---

# Order of Operations

---

# Order of Operations

| | | |
| --- |--- | --- |
| Highest | () | Brackets |
| | ** | Exponent |
| | * | Multiplication |
| | / | Division |
| | + | Addition |
| Lowest | - | Subtraction |

---

# Order of Operations

[.code-highlight: 1]
[.code-highlight: 3]
```python
sum = 4 + 5 * 2

correct_sum = (4 + 5) * 2
```

---

# [fit]Coding Time
## Section B

---

# Comments

---

# Comments

[.code-highlight: 1-2]
[.code-highlight: 4]
```python
# The total including VAT
total = sub_total + vat

has_paid = False # If the user has paid or not
```

---
# Casting

---

# Casting — Integers

```python
x = int(1)   # x will be 1
y = int(2.6) # y will be 2
z = int("3") # z will be 3
```

---

# Casting — Floats

```python
w = float(4)     # w will be 4.0
x = float(5.6)   # x will be 5.6
y = float("6")   # y will be 6.0
z = float("7.3") # z will be 7.3
```

---

# Casting — Strings

```python
x = str("abc8") # x will be 'abc8'
y = str(9)      # y will be '9'
z = str(10.0)   # z will be '10.0'
```

---

# Length

---

# Length

[.code-highlight: 1-2]
[.code-highlight: 4]
```python
name = "Alice"
name_length = len(name) # 5

sentence_length = len("Hello, World!") #13
```
---

# Index

---

# Index


| H | e | l | l | o |
| --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 |

---

# Index

| C | h | a | r | l | i | e |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |


```python
name = "Charlie"
print(name[0]) # Prints 'C'
print(name[1]) # Prints 'h'
```

---

# Input

---

# Input

[.code-highlight: 1-2]
[.code-highlight: 4-6]
```python
name = input("What's your name? ")
print("Hello " + name)

age = int(input("How old are you? "))
age_in_10_years = age + 10
print("In 10 years you will be " + str(age_in_10_years))
```

---

# Upper/Lower

---

# Upper/Lower

[.code-highlight: 1-2]
[.code-highlight: 4]
```python
name = "Alice"
print(name.upper())

print("HeLlO".lower())
```

---

# [fit]Coding Time
## Section C

---

# Exercises

Finish off any exercises you did not complete in the session

---

### Further Help

## [fit]DL-UKIHFCode@kpmg.co.uk

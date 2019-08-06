fruits = ["Apples", "Cherries", "Pears", "Pineapples", "Peaches", "Mango"]
print(fruits)

fruits.append("Grapes")
print(fruits)

fruits[2] = "Strawberries"
print(fruits)

del fruits[0]
print(fruits)

print(len(fruits))

for fruit in fruits:
    print(fruit)
    
fruits.sort()
print(fruits)
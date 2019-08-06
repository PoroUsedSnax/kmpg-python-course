people = []
name = input("Enter a persons name: ")
while len(name) != 0:
    age = input("Enter the person's age: ")
    people.append({
        "Name": name,
        "Age": age
    })
    name = input("Enter another person's name: ")
print(people)
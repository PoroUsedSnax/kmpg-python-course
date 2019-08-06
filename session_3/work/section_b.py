apple = {
    "Type": "Bramley", 
    "Price": 0.39,
    "Colour": "Green"
}
print(apple)

apple["BestBeforeDate"] = "07/08/2019"
print(apple)

apple["Price"] = 0.41
print(apple)

apple["OnOffer"] = True
print(apple)

for value in apple:
    print(str(value) + " = " + str(apple[value]))

del (apple["OnOffer"])
print(apple)

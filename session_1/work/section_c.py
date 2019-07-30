has_paid = True
vip = False
x = 4
y = 7
area = x*y
word = 'python'
name = input('What is your name?')
age = int(input('What is your age?\n'))
town = input('What is your home town?')

print(has_paid)
print('rectangle of length ' + str(x) + ' and height ' + str(y) + ' has an area of ' + str(area))
print(len(word))
print(word[0] + word[2])
print('Hello, ' + name + ', you are currently ' + str(age) + ', you will be ' + str(age + 15) + ' in 15 years')
print(town.upper())
print('Has Paid?: ' + str(has_paid) + '\nVIP?: ' + str(vip))
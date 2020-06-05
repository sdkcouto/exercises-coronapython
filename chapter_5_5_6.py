#Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#• If the person is less than 2 years old, print a message that the person is a baby.

age = 2
if age < 2:
    print('you are a baby')
#• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

age = 3
if age >= 2 and age < 4:
    print('you are a toddler')

#• If the person is at least 4 years old but less than 13, print a message that the person is a kid.

age = 10
if age >= 4 and age < 13:
    print('you are a kid')

#• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

age = 15
if age >= 13 and age < 20:
    print('you are a teenager')

#• If the person is at least 20 years old but less than 65, print a message that the person is an adult.

age = 35
if age >= 20 and age < 65:
    print('you are an adult')

#• If the person is age 65 or older, print a message that the person is an elder.

age = 65
if age >= 65:
    print('you are an elder')

ages = [2,3,10,15,33,65]
for age in ages:
    if age < 2:
        print('you are a baby')
    elif age >= 2 and age < 4:
        print('you are a toddler')
    elif age >= 4 and age < 13:
        print('you are a kid')
    elif age >= 13 and age < 20:
        print('you are a teenager')
    elif age >= 20 and age < 65:
        print('you are an adult')
    elif age >= 65:
        print('you are an elder')




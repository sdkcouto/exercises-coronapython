# People: Start with the program you wrote for Exercise 6-1 (page 102). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

info_0 = {'first_name' : ' Thales',
    'last_name' : 'Silva',
    'age' : '30',
    'city' : 'Rio de janeiro'
    }

info_1 = {'first_name' : 'Thais',
    'last_name' : 'Dantas',
    'age' : '28',
    'city' : 'Salvador'
    }

info_2 = {'first_name' : 'Pedro',
    'last_name' : 'Damasceno',
    'age' : '29',
    'city' : 'Salvador'
    }

people = [info_0, info_1, info_2]

for p in people:
    print(p)


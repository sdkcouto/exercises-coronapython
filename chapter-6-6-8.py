# Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

pet_0 = {'kind' : 'dog',
    'owner' : 'Juliana'
    }

pet_1 = {'kind' : 'cat',
    'owner' : 'Ana'
    }

pet_2 = {'kind' : 'fish',
    'owner' : 'Joao'
    }

pets = [pet_0, pet_1, pet_2]
for p in pets:
    print(p)
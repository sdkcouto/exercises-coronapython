#Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favorite_number = {'flavio' : ['24', '12'],
     'joao' : ['69', '32'],
      'matheus' : ['420', '42'],
       'dudu' : ['120', '11'],
        'pedro' : ['0', '16']
        }
for number in favorite_number.items():
    print(number)

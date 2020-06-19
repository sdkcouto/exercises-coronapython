# Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.

import json

favorite_number = input("what are your favourite numbers? ")

file_name = 'favorite_numbers.json'
with open(file_name,'w') as f_name:
    json.dump(favorite_number,f_name)

with open(file_name) as f_number:
    f_number = json.load(f_number)
    print("I know your favorite number! It’s " + f_number + ".")
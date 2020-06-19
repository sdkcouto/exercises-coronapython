#Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”

import json

favorite_number = input("what are your favourite numbers? ")

file_name = 'favorite_numbers.json'
with open(file_name,'w') as f_name:
    json.dump(favorite_number,f_name)

with open(file_name) as f_number:
    f_number = json.load(f_number)
    print("I know your favorite number! It’s " + f_number + ".")


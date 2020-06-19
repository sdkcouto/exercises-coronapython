#Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
file_name = 'guest.txt'

with open(file_name,'w') as file_object:
    file_object.write(input('What is your name? '))
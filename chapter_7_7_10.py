#Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

results = {}
poll_active = True
while poll_active:
    names = input('What is your name? ')
    places = input('Where would you wish to go? ')
    results[names] = places
    repeat = input('Would  you like to let anyone else participate? (yes or no) ')
    if repeat == 'no':
        poll_active = False
print('This are the results:')
for name, place in results.items():
    print(name + ' would like to travel to ' + place)

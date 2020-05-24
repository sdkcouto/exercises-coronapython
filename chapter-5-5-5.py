#3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

#• If the alien is green, print a message that the player earned 5 points.

alien = 'green'
if alien == 'green':
    print("You just eaned 5 points")

#• If the alien is yellow, print a message that the player earned 10 points.

alien = 'yellow'
if alien == 'green':
    print("You just eaned 5 points")
elif alien == 'yellow':
    print('You just earned 10 points')
#• If the alien is red, print a message that the player earned 15 points.

alien = 'red'
if alien == 'green':
    print("You just eaned 5 points")
elif alien == 'yellow':
    print('You just earned 10 points')
elif alien == 'red':
    print('You just earned 15 points')
    
#• Write three versions of this program, making sure each message is printed for the appropriate color alien.
aliens = ['red', 'green', 'yellow']
for alien in aliens:
    if alien == 'green':
        print("You just eaned 5 points")
    elif alien == 'yellow':
        print('You just earned 10 points')
    elif alien == 'red':
        print('You just earned 15 points')
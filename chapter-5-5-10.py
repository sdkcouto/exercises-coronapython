#Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.

#• Make a list of five or more usernames called current_users.

current_users = ['Andre', 'Dudu', 'Thales', 'Pedro', 'Matheus']

#• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.

new_users = ['Flavio', 'Anderson', 'Thais', 'Pedro', 'Andre']

#• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.

current_users = ['Andre', 'Dudu', 'Thales', 'Pedro', 'Matheus']
new_users = ['Flavio', 'Anderson', 'Thais', 'Pedro', 'Andre']
for new_user in new_users:
    if new_user in current_users:
        print('You will need to enter a new username. ')
    else:
        print('Username avaliable')


#• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.

current_users = ['Andre', 'Dudu', 'Thales', 'Pedro', 'Matheus']
new_users = ['Flavio', 'Anderson', 'Thais', 'PEDRO', 'andre']
for new_user in new_users:
    if new_user in current_users or new_user.title() in current_users or new_user.lower() in current_users or new_user.upper() in current_users :
        print('You will need to enter a new username. ')
    else:
        print('Username avaliable')

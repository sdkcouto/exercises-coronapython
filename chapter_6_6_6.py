#Use the code in favorite_languages.py (page 104).

#• Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
names = ['thales', 'andre', 'flavio', 'sarah']
favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

#• Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

for name in names:
    if name in favorite_languages.keys():
           print(name + ' , thank you for responding.')
    else:
           print(name + ' , please take the poll.')
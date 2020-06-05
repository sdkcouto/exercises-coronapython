#Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.

favorite_fruits = ['banana','apple','grape']

#• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

favorite_fruits = ['banana','apple','grape']
for fruit in favorite_fruits:
    if fruit == 'banana':
        print('I love bananas!')
    if fruit == 'grape':
        print('I love grapes!')
    if fruit == 'apple':
        print('I love apples')
    if fruit == 'orange':
        print('I dont like oranges')
    if fruit == 'strawberry':
        print('I dont like strawberries')
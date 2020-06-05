#No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['tuna', 'pastrami', 'blt', 'pastrami', 'pastrami']
finished_sandwiches = []
print('The deli ran out of pastrami')

while sandwich_orders:
    if 'pastrami' in sandwich_orders: 
        sandwich_orders.remove('pastrami')
    else:
        sandwich = sandwich_orders.pop()    
        print('Your ' + sandwich + ' sandwich was made.' )
        finished_sandwiches.append(sandwich)
print('\nThe following sandwiches have been confirmed.')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

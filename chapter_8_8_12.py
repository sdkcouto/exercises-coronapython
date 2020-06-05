# Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time

def make_sandwich(*sandwiches):
    print('\nThis are the sandwiches that we have: ')
    for sandwich in sandwiches:
        print("-" + sandwich)

make_sandwich('tuna')
make_sandwich('tuna','pastrami')
make_sandwich('blt', 'pastrami', 'cheese')
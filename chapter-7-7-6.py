#7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:

#• Use a conditional test in the while statement to stop the loop.

pizza_toppings = 'Please, enter a pizza topping: '
pizza_toppings += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(pizza_toppings)
    if message == 'quit':
        print('Have a nice day')
    else:
        print(message + ' added to the pizza.')

#• Use an active variable to control how long the loop runs.

pizza_toppings = 'Please, enter a pizza topping: '
pizza_toppings += "\nEnter 'quit' to end the program. "
active = True
while active:
    pizza_topping = input(pizza_toppings)
    if pizza_topping == 'quit':
        active = False
    else:
        print(pizza_topping + ' added to the pizza.')

#• Use a break statement to exit the loop when the user enters a 'quit' value.

pizza_toppings = 'Please, enter a pizza topping: '
pizza_toppings += "\nEnter 'quit' to end the program. "
while True:
    pizza_topping = input(pizza_toppings)
    if pizza_topping == 'quit':
        break
    else:
        print(pizza_topping + ' added to the pizza.')


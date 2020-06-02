#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

pizza_toppings = 'Please, enter a pizza topping: '
while True:
    pizza_topping = input(pizza_toppings)
    if pizza_topping == 'quit':
        break
    else:
        print(pizza_topping + ' added to the pizza.')
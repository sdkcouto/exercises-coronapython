# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
pizza = ["Tuna", "Pepperoni", "Brazilian"]
friend_pizzas = ["Pepperoni","Margherita","Four cheese"]
#
# • Add a new pizza to the original list.
pizza.append("Catupiry")
#
# • Add a different pizza to the list friend_pizzas.
friend_pizzas.append("Palmito")
#
# • Prove that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
print("My favorite pizza are: ")
for i in pizza:
    print(i)

print("My friends favorite pizza are: ")
for p in friend_pizzas:
    print(p)
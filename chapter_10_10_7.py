#Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

print("Give me two numbers to add")
print("press 'q' to quit ")

while True:
    number_0 = input("enter first number = ")
    if number_0 == 'q':
        break
    number_1 = input("enter second number= ")
    if number_1 == 'q':
        break
    try:
        answer = int(number_0) + int(number_1)
    except ValueError:
        print("I cant add something that is not a number")
    else:
        print(answer)
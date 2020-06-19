#Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

number_0 = input("enter first number = ")
number_1 = input("enter second number = ")
try:
    answer = int(number_0) + int(number_1)
    print(answer)
except ValueError:
    print("I cant add something that is not a number")
    

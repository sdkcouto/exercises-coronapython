# 4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8:
#
# • Use four spaces for each indentation level. Set your text editor to insert four spaces every time you press TAB, if you haven’t already done so (see Appendix B for instructions on how to do this).
#
# • Use less than 80 characters on each line, and set your editor to show a vertical guideline at the 80th character position.
#
# • Don’t use blank lines excessively in your program files.

# Exercise 4-7
number = range(3,30,3)
for n in number:
    print(n)

# Exercise 4-9
cubes = [value**3 for value in range(1,11)]
print(cubes)

# Exercise 4-12
pizza = ["Tuna", "Pepperoni", "Brazilian"]
friend_foods = pizza[:]

print("My favorite pizzas are: ")
for i in pizza:
    print(i)

print("My friend’s favorite foods are: ")
for i in friend_foods:
    print(i)
# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# Exercise 4-9
cubes= [value**3 for value in range(1,11)]
print(cubes)
# 
# • Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
print("The first three items in the list are: "+ str(cubes[0:3]))
# 
# • Print the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
print("Three items from the middle of the list are: " + str(cubes[4:7]))
#
# • Print the message, The last three items in the list are:. Use a slice to print the last three items in the list.
print("The last three items in the list are: " + str(cubes[-3:]))
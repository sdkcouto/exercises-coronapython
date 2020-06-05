#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

#• Store the numbers 1 through 9 in a list.
numbers = range(1,10)
#• Loop through the list.
for n in numbers:
    print(n)
#• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
numbers = range(1,10)
for n in numbers:
    if n == 1:
        print('1st')
    elif n == 2:
        print('2nd')
    elif n == 3:
        print('3rd')
    else:
        print(str(n) + "th")

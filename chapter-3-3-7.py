# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
#
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

# Exercise 3-6
presidents = ["Lula", "Bolsonaro", "Putin"]
print("hey "+ presidents[0] + ", i am making dinner, pleae come?")
print("hey "+ presidents[1] + ", i am making dinner, pleae come?")
print("hey "+ presidents[2] + ", i am making dinner, pleae come?")

print("Hey " + presidents[2] + " can't make it.")

presidents.remove(presidents[2])
presidents.insert(2,"Temer")

print("Hey " + presidents[0] + " i am making dinner, please come!")
print("Hey " + presidents[1] + " i am making dinner, please come!")
print("Hey " + presidents[2] + " i am making dinner, please come!")
print("I found a bigger table")
presidents.insert(0,"FHC")
presidents.insert(1,"Dilma")
presidents.append("Collor")
print("Hey " + presidents[0] + " i am making dinner, please come!")
print("Hey " + presidents[1] + " i am making dinner, please come!")
print("Hey " + presidents[2] + " i am making dinner, please come!")
print("Hey " + presidents[3] + " i am making dinner, please come!")
print("Hey " + presidents[4] + " i am making dinner, please come!")
print("Hey " + presidents[5] + " i am making dinner, please come!")
print("Sorry, i coulndt get the table. I can only invite two people")
wontcome = presidents.pop()
print("Sorry " + wontcome + ", i dont have space for you!")
wontcome = presidents.pop()
print("Sorry " + wontcome + ", i dont have space for you!")
wontcome = presidents.pop()
print("Sorry " + wontcome + ", i dont have space for you!")
wontcome = presidents.pop()
print("Sorry " + wontcome + ", i dont have space for you!")
print("Hey " + presidents[1] + ", you can come!")
print("Hey " + presidents[0] + ", you can come!")
del presidents[1]
del presidents[0]
print(presidents)
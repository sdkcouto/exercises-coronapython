# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46), use len() to print a message indicating the number of people you are inviting to dinner.

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

print("The number of people i am inviting is " + str(len(presidents)))
# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

# Exercise 3-9
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

print(sorted(presidents))
presidents.sort(reverse=True)
print(presidents)
print(sorted(presidents,reverse=True))
presidents.reverse()
print(presidents)
print("The number of people i am inviting is " + str(len(presidents)))
# 3-11. Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.

# Exercise 3-10
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
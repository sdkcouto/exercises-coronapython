# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
foods = ("arroz","feijao", "batata", "macarrao", "cachorro")
#
# • Use a for loop to print each food the restaurant offers.
for i in foods:
    print(i)
#
# • Try to modify one of the items, and make sure that Python rejects the change.
#foods[2] = "arroz"
#
# • The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
new_food=["batata frita", "vegetais"]
for n in range(0,3):
    new_food.append(foods[n])

for n in new_food:
    print(n)

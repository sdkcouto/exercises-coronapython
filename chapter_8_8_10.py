#Great Magicians: Start with a copy of your program from Exercise 8-9. Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to see that the list has actually been modified.

def show_magicians(great_magicians):
    for magician in great_magicians:
        print(magician)

def make_great(magicians_names,great_magicians):
    while magicians_names:
        g_magician = magicians_names.pop()
        g_magician = 'Great ' +  g_magician
        great_magicians.append(g_magician)
        

magicians_names = ['houdini','david blane', 'chris angel']
great_magicians = []

show_magicians(magicians_names)
make_great(magicians_names,great_magicians)
show_magicians(great_magicians)

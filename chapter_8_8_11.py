#Unchanged Magicians: Start with your work from Exercise 8-10. Call the function make_great() with a copy of the list of magicians’ names. Because the original list will be unchanged, return the new list and store it in a separate list. Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.

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

make_great(magicians_names[:],great_magicians)
show_magicians(great_magicians)
show_magicians(magicians_names)
#Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name + ".")
        print("And it's a " + self.cuisine_type + " restaurant.")
    
    def open_restaurant(self):
        print(self.restaurant_name + ", it is open now.")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        self.flavors = ['vanilla','chcolate','mint']
        super().__init__(restaurant_name,cuisine_type)
    
    def ice_cream_flavors(self):
        print("These are the ice cream flavors: ")
        for flavor in self.flavors:
            print( flavor)

my_icecreamflavor = IceCreamStand('sorveteria da ribeira', 'ice cream shop')
my_icecreamflavor.ice_cream_flavors()

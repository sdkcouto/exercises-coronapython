# helper file for chapter_9_9_10.py

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
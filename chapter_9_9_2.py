#Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name + ".")
        print("And it's a " + self.cuisine_type + " restaurant.")
    
    def open_restaurant(self):
        print(self.restaurant_name + ", it is open now.")

my_restaurant = Restaurant('Pizza hut', 'pizzaria')
your_restaurant = Restaurant('Tche Picanhas','BBQ')
her_restaurant = Restaurant('Fushimi','sushi bar')

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
her_restaurant.describe_restaurant()
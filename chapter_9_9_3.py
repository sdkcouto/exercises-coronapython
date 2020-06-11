#Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.

#Create several instances representing different users, and call both methods for each user.

class User():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + ". " + self.age + " years old, " + self.gender + ".")
        
    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + ".")

user1 = User('matheus','dantas','29','male')
user2 = User('Pedro', 'damasceno','29','male')
user3 = User('thais','dantas','28','female')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

#Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

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

class Admin(User):
    def __init__(self,first_name,last_name,age,gender):
        self.privileges = ["can add post","can ban user","can add post","can delete post"]
        super().__init__(first_name,last_name,age,gender)
        
    def show_privileges(self):
        print("These are the user's privileges: ")
        for privilege in self.privileges:
            print(privilege)

my_Admin = Admin('Andre','Faria', '31','male')
my_Admin.show_privileges()
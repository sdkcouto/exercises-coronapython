# helper file for chapter_9_9_11.py and chapter_9_9_12.py
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


class Privileges:
    
    def __init__(self,privileges =["can add post","can ban user","can add post","can delete post"]):
        self.privileges = privileges
        
    def show_privileges(self):
        print("These are the user's privileges: ")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    
    def __init__(self,first_name,last_name,age,gender):
        super().__init__(first_name,last_name,age,gender)
        self.privileges = Privileges()
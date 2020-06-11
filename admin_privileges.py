# helper file for chapter_9_9_12.py 
import user_solo

class Privileges:
    
    def __init__(self,privileges =["can add post","can ban user","can add post","can delete post"]):
        self.privileges = privileges
        
    def show_privileges(self):
        print("These are the user's privileges: ")
        for privilege in self.privileges:
            print(privilege)

class Admin(user_solo.User):
    
    def __init__(self,first_name,last_name,age,gender):
        super().__init__(first_name,last_name,age,gender)
        self.privileges = Privileges()


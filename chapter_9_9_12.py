#Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
from user import User
import admin_privileges 
your_admin = admin_privileges.Admin('Flavio','faria','28','male')
your_admin.privileges.show_privileges()
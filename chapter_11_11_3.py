# Employee: Write a class called Employee. The __init__() method should take in a first name, a last name, and an annual salary, and store each of these as attributes. Write a method called give_raise() that adds $5000 to the annual salary by default but also accepts a different raise amount.

#Write a test case for Employee. Write two test methods, test_give_default_raise() and test_give_custom_raise(). Use the setUp() method so you don’t have to create a new employee instance in each test method. Run your test case, and make sure both tests pass.

import unittest

class Employee():
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_raise(self,raise_amount = 5000):
        self.salary += raise_amount
        

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee_1 = Employee('pedro','barros',12000)

    def test_give_default_raise(self):
        self.employee_1.get_raise()
        self.assertEqual(self.employee_1.salary,17000)
    
    def test_give_custom_raise(self):
        self.employee_1.get_raise(6000)
        self.assertEqual(self.employee_1.salary,18000)


unittest.main()
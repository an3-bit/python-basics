#OOP-based on objects-classes-data-functions
#class-blueprint for creating an object
#object-instance of a class
#attribute-variable inside an object that stores data
#method-functions inside a class that defines behaviour
#__init__: a construct that initializes an object
#self-refers to current object instance
from django.contrib.auth.decorators import login_required


# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def display_info(self):
#         print(f"{self.year} {self.brand} {self.model}")
# car1=Car("Toyota","avensis",2023)
# car2=Car("Mercedes","G-wagon",2022)
# car1.display_info()
# car2.display_info()
#four pillars of OOP
#data hiding-restriction direct access to data(encapsulation)
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number=account_number
#         self.balance=balance
#     def deposit(self, amount):
#         self.balance+=amount
#         print(f"Deposited {amount} is successful. \n New Balance: {self.balance}")
#     def get_balance(self):
#         return self.balance
# account=BankAccount("123456", 500000)
# account.deposit(400000)
# print(account.get_balance())
#inheritance(code reusability)
class Animal:
    def __init__(self, name):
        self.name=name
    def make_sound(self):
        print("Animal makes a sound")
class Cow(Animal):
    def make_sound(self):
        print("Moows! Moows!")
cow1=Cow("kerubo")
cow1.make_sound()
#polymorphism(multiple forms)
#abstraction-hiding complexity



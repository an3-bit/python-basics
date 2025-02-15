#OOP-based on objects-classes-data-functions
#class-blueprint for creating an object
#object-instance of a class
#attribute-variable inside an object that stores data
#method-functions inside a class that defines behaviour
#__init__: a construct that initializes an object
#self-refers to current object instance
# from django.contrib.auth.decorators import login_required
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
# class Animal:
#     def __init__(self, name):
#         self.name=name
#     def make_sound(self):
#         print("Animal makes a sound")
# class Cow(Animal):
#     def make_sound(self):
#         print("Moows! Moows!")
# cow1=Cow("kerubo")
# cow1.make_sound()
#polymorphism(multiple forms)
#abstraction-hiding complexity

# class Car:
#     def __init__(self,brand,model,mileage,year):
#         self.brand=brand
#         self.model=model
#         self.mileage=mileage
#         self.year=year
#     def display_info(self):
#         print(f"{self.brand} \n{self.model} \n{self.mileage} \n{self.year}")
# car1=Car("Toyota","corola",530,2021)
# car2=Car("Mercedes","SUV",200,2023)
# car1.display_info()
# car2.display_info()
#
# class BankAccount:
#     def __init__(self,account_name,account_number,balance):
#         self.account_name=account_name
#         self.account_number=account_number
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#         print(f"The {amount} has been deposited successfully. \n The new balance is: {self.__balance}")
#     def withdraw(self,amount):
#         if amount > self.__balance:
#             print("Insufficient balance! Please withdraw a lesser amount.")
#         else:
#             self.__balance-=amount
#             print(f"The {amount} has been withdrawn successfully. \n Remaining balance is: {self.__balance}")
#     def get_balance(self):
#         return self.__balance
# #user input
# name=input("Enter account name: ")
# initial_balance=int(input("Initial balance: "))
#
# account=BankAccount("Alice",123456,500000)
# #hint
# #choices
# #if choice == "yes":#
#
# deposit_amount=int(input("Enter deposit amount: "))
# account.deposit(deposit_amount)
#
# choice= input("Do you want to withdraw? (yes/no): ").strip().lower()
# if choice == "yes":
#     withdraw_amount=int(input(" Enter amount to withdraw: "))
#     account.withdraw(withdraw_amount)
# else:
#     print("Transaction completed successfully.")
# print(f"The final balance for {account.account_name}: {account.get_balance()}")
#inheritance
# Parent class
class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Name: {self.name}"


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return f"Salary: {self.salary}"


class Manager(Person, Employee):
    def __init__(self, name, salary, department):
        # Initialize attributes from parent classes
        Person.__init__(self, name)
        Employee.__init__(self, salary)
        self.department = department

    def get_department(self):
        return f"Department: {self.department}"


# Creating an instance of Manager
manager = Manager("Peter", 75000, "HR")

# Displaying manager information
print(manager.info())
print(manager.get_salary())
print(manager.get_department())


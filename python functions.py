#reusable block of code
#built-in fns
from operator import add

from win32gui import FlashWindowEx

# fruits=["pineapples","watermelons","oranges"]
# #user-defined fns
# def greet(name):
#     print(f"Hello, {name} Welcome to today's lesson.")
# greet("Alice")
# greet("Charles")
# lambda fns
# add=lambda x,y:x+y
# print(add(5,6))
# lambda arguments:expression
# def name():
#     print("alice", "kate")
# name()
# def sum(a,b):
#     return a+b
# result=add(9,10)
# print(f"Sum: {result}")
# def car(name="Honda"):
#     print(f"I like {name}")
#
# car("Ford Wild Truck")

#variable length arguments
# def add_numbers(*args):
#     return sum(args)
# print(add_numbers(2,4,5,6,8,9))
#
# def multiply(x,y):
#     return x*y
# print(multiply(4,20))
#keyword arguments
# # def display_info(**kwargs):
# #     for key, value in kwargs.items():
#         print(f"{key}:{value}")
# display_info(name="Alice", age=24, estate="Rongai")
#
# def max_of_three_numbers(a,b,c):
# #     return max(a,b,c)
# print(max_of_three_numbers(40,45,70))
# #checking a number if it is even or odd
# # def check_number(n):
# #     if n
# def greetings(name):
#     print(f"Hello {name}, Good Morning, Good afternoon")
# greetings("Andrew")
#
# def add(a,b):
#     return a+b
# result=add(9,17)
# print(result)

# def greet(name="Guest"):
#     print(f"Hello {name}")
# # greet()
# greet("Sarah")

# def multiplication(x,y):
#     return x*y
# print(multiplication(6,10))

# def add_numbers(*args):
#     return sum(args)
# print(add_numbers(2,4,6,7,9,8))

# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
# display_info(name="John", age=23,country="Kenya")

#check if a number is prime
# def is_prime(n):
#     if n <2:
#         return False
#     for i range(2, int(n**0.5)+1):
#         if n% i ==0:
#             return False
#     return  True
def check_number(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(check_number(7))
print(check_number(8))

# names=[]
# for i in range(5):
#     name=input("Enter name: ")
#     names.append(name)
#     names.sort()
# print(f"The names are alphatecal order: {names}")
# longest_name=max(names, key=len)
# print(f"The longest name is: {longest_name}")
#tuples
# cities=("Nairobi","Kirinyaga","Kijabe","Mombasa","Keroka")
# user_city=input("Enter a city: ")
# if user_city in cities:
#     print(f"{user_city} is at index {cities.index(user_city)}")
# else:
#     print("City is not found.")
#modifying a tuple
# fruits=("apple","oranges","kiwi")
# fruit_list=list(fruits)
# fruit_list[0]="straberry"
# fruits=tuple(fruit_list)
# print(fruits)
from python_lists import students

# numbers=(1,2,3,4,40,23,45)
# number_list=list(numbers)
# number_list.append(100)
# numbers=tuple(number_list)
# print(numbers)

# students=("Jane","Kamau","Githau","Mary")
# student_list=list(students)
# student_list.append("Joyce")
# students=tuple(student_list)
# print(students)

# student={
#     "name":"Kim Njau",
#     "admission no.": 1999,
#     "age": 22,
#     "course": "Data science"
# }
#
# for key, value in student.items():
#     print(f"{key}:{value}")
#example 1
# sentence=input("Enter a sentence: ")
# words=sentence.split()
# word_count={}
# for word in words:
#     word_count[word]=word_count.get(word, 0)+1
# print("Word Frequencies:", word_count)
#example 2
# grades={
#     "Alice":"B",
#     "John":"A",
#     "Clinton":"C"
# }
# name=input("Enter student name: ").capitalize()
#
# if name in grades:
#     print(f"{name}'s grade is {grades[name]}")
# cars=["ford ranger","mercedes benz","honda","subaru"]
# numbers=[1,20,56,78,89,33,45]
# mixed_list=[1,2,3,"greetings","bananas"]
# print(cars[-1])
# numbers[1]=400
# print(numbers)
# mixed_list.append("oranges")
# print(mixed_list)
# mixed_list.insert(0, "strawberry")
# print(mixed_list)
# more_fruits=["mangoes","cherries"]
# mixed_list.extend(more_fruits)
# print(mixed_list)
# mixed_list.remove("greetings")
# print(mixed_list)
# mixed_list.pop(0)
# print(mixed_list)
# for car in cars:
#     print(car)
# if "subaru" in cars:
#     print("Subaru is present.")
# # else:
# #     print("The car is not there!")
# numbers.sort()
#
#
#
# print(numbers[-3:])
numbers=[]
for i in range(5):
    number=int (input("Enter a number:"))
    numbers.append(number)
print(f"Numbers entered are: {numbers}")
print("Sum of the numbers is:", sum(numbers))
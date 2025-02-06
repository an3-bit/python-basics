# fruits=("apples","oranges","bananas")
# mixed_tuple=(10, "hello",20,"andrew")
# print(mixed_tuple[0])
# print(fruits[2])
# print(fruits[0:2])
# print(fruits[:2])
# print(fruits[1:])
# fruits_list=list(fruits)
# fruits_list.append("Strawberry")
# fruits=tuple(fruits_list)
# print(fruits)
# for fruit in fruits:
#     print(fruit)
# person=("Alice",25,"Teacher","Mother")
# name, age, job, family=person
# print(name)
# print(age)

# cities=("Nairobi","Kisumu","Mombasa","Nakuru","Eldoret")
# user_city=input("Enter a city: ").capitalize()
# if user_city in cities:
#     print(f"{user_city} is at index {cities.index(user_city)}")
# else:
#     print("Oh! sorry, city is no there! please try again another city.")
#dictionaries
# car={
#     "name":"ford ranger",
#     "manufacturer":"ford",
#     "model":2.5,
#     "year":2024,
#     "type":"manual"
# }
# car["paint"]="brown"
#
# del car["year"]
# print(car)
student={
    "name":"Kimani Mworia",
    "reg. no.":"EMCQ/01735/2022",
    "course":"Software Engineering"
}
person={
    "name":"John Doe",
    "age":23
}
# print(student.get("name"))
student["grade"]="A"
# print(student)
person["age"]=24
# print(person)
del person["age"]
# print(person)
student.pop("reg. no.")
# print(student)
# student.popitem()
# print(student)
# for key in student:
#     print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(f"{key}:{value}")
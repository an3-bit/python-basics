# names=[]
# for i in range(5):
#     name=input("Enter name: ")
#     names.append(name)
#     names.sort()
# print(f"The names are alphatecal order: {names}")
# longest_name=max(names, key=len)
# print(f"The longest name is: {longest_name}")
#tuples
cities=("Nairobi","Kirinyaga","Kijabe","Mombasa","Keroka")
user_city=input("Enter a city: ")
if user_city in cities:
    print(f"{user_city} is at index {cities.index(user_city)}")
else:
    print("City is not found.")
#creating a list
fruits=["apple", "oranges","mangoes"]
more_fruits=["pears","avocadoes","grapes"]
numbers=[10,25,13,4,35]
students=["andrew","Handson","Peter", "Elijah"]
#accesing elements from a list
print(fruits[0])
print(fruits[-1])
print(fruits[1])
print(students[-1])
print(students[1])
print(students[2])
#modifying a list
numbers[1]=20
print(numbers)
#adding elements to a list
fruits.append("banana")
print(fruits)
fruits.insert(0,"cherry")
print(fruits)
fruits.extend(more_fruits)
print(fruits)
fruits.remove("mangoes")
print(fruits)
fruits.pop(0)
print(fruits)
del fruits[1]
print(fruits)
#looping through a list
for fruit in fruits:
    print(fruit[0])
for i in range(len(fruits)):
    if i ==3:
        print(fruits[3])
#check if an item exists in a list
if "strawberry" in fruits:
    print("Strawberry is in the list")
elif "strawberry" not in fruits:
    print("Strawberry is not in the list")
fruits.append("strawberry")
print(fruits)
#sorting and reversing a list
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
#list slicing
print(numbers[:3])
print(numbers[-3:])
#list comprehension
evens= [i for i in numbers if i %2 ==0]
print(evens)

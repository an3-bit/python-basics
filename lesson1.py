#operators
# arithemic: +,-,*,/,%,**,5*10**-5,//
# comparison: x==5,!=,>,<,=>,<=
# logical operators: and,or, not, x>0 or x<5
# assignment: =, +=, -=, *=
# memebership: in, not in a in apple
# identity: is, is not x is y x is not y

# #control flow statements (if, elif, else)
# number=int(input("Enter a number: "))
# if number>0:
#     print("Positive number")
# elif number==0:
#     print("zero")
# else:
#     print("negative number")
# #
# user_grade = input("Please enter your score: ")
# if not user_grade.isnumeric():
#     print("Please enter a valid number.")
#     exit(0)
#
# score = int(user_grade)
#
# if score >=78:
#     print("A")
# elif 71 <= score <=77:
#     print("A-")
# elif 64 <= score <=70:
#     print("B+")
# elif 54 <= score <= 60:
#     print("B")
# elif 45 <= score <= 56:
#     print("C+")
# else:
#     print("C")
# loops
# for loop-used when iterating over a sequence(list, string, range)
# cars=["honda","mercedes benz", "ford ranger","nissan "]
# for car in cars:
#     print(car)

# while loop-used when repeating a task as long as the condition is true
# number=5
# while number >0:
#     print(number)
#     number -=1

# for char in "Andrew":
#     print(char)

# for num in range(1,20):
#     print(num)

response=""
while response.upper() != "YES":
    response=input("Enter 'YES' to stop: ")
print("Thank you!")
#ask the user to enter a number
starting_number=int(input("Enter the starting number: "))
ending_number=int(input("Enter the ending number: "))
#validation that the starting number is less than the ending number using a while loop
while starting_number >= ending_number:
    print("Invalid number! The starting number must be less than the ending number.")
    starting_number=int(input("Enter the starting number: "))
    ending_number = int(input("Enter the ending number: "))
#USE A FOR LOOP TO PRINT THE EVEN NUMBERS
print(f"\nEven numbers between {starting_number} and {ending_number} are: ")
for num in range(starting_number, ending_number+1):
    if num % 2 ==0:
        print(num)
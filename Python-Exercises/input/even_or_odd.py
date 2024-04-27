# program that prompts the user to enter a number and then prints whether it is even or odd.

number = int(input("Enter the number: "))

if number % 2 == 0:
    print("The number is even number.")
else:
    print("The number is an odd number.")
# program that checks if a given number is divisible by both 2 and 3.

number = int(input("Enter number: "))

if (number % 2 == 0 and number % 3 == 0):
    print("Number is divisible by both 2 and 3.")
else:
    print("Number is not divisible by 2 and 3.")
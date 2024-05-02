# Define a custom exception class called CustomError. Write a Python program that raises this custom error when a user enters a negative number. Implement error handling to catch this custom error and print a message to the user.

class CustomError(Exception):
    pass

try:
    num = int(input("Enter a non-negative number: "))
    if num < 0:
        raise CustomError("Negative numbers are not allowed.")
    print("Number is:", num)
except CustomError as e:
    print("CustomError:", e)



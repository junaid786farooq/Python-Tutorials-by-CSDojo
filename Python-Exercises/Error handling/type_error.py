#  function called multiply that takes two parameters a and b and returns their product. Implement error handling to catch the TypeError if either a or b is not a numeric type and print a message to the user.

def multiply(a, b):
    try:
        return print("Product:", a * b)
    except TypeError:
        print("Error: Both arguments must be numeric..")

while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        break
    except ValueError:
        print("Error: Please enter a numeric value..:)!")

multiply(a, b)
# a lambda function called square that takes a single parameter x and returns the square of x. Test the lambda function by calling it with different values.

# Input validation for numeric value
while True:
    try:
        num = int(input("Enter number for square: "))
        break
    except ValueError:
        print("Please input a valid numeric value!")

# Define and use the lambda function by square thi input
square = lambda x : x ** 2

print(f"Square of {num} = {square(num)}")
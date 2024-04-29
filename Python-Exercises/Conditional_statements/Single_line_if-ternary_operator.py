# program that takes a number as input from the user and prints "Even" if the number is even, and "Odd" if the number is odd, using a single-line if/ternary operator.

# <var> = <var> if <condition> else <var2>

num = int(input("Enter a number: "))

result = "Even" if num%2 == 0 else "Odd"

print(result)


# <var> if <condition> else <string>

food = input("Enter name of food: ").lower()

print("Sweet") if food == "cake" or food == "jalabi" else print("Not sweet")
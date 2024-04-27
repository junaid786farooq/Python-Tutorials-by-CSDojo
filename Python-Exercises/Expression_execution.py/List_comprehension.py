# program that uses list comprehensions to generate a list of squares of numbers from 1 to 10.

squares = [x ** 2 for x in range(1, 11)]

# for x in range(1, 11):
#     squares.append(x**2)

print("Squares:", squares)
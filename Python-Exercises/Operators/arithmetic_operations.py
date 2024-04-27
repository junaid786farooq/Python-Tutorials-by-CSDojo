# program that takes two numbers as input and performs arithmetic operations (addition, subtraction, multiplication, division) on them.

num1  = int(input("Enter first number: "))
num2  = int(input("Enter second number: "))

addition = num1 + num2

subtraction = num1 - num2

multiplication = num1 * num2

division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
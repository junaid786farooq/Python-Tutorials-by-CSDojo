# program that calculates the factorial of a given number using recursion.

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return (num * factorial(num - 1))
    
num = 5
result = factorial(num)

print(f"The factorial of {num} is:", result)

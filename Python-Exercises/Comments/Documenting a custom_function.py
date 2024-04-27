# program that documents the purpose and usage of a custom function using comments.

# This is a function to find factorial of a number.
def factorial(n):
    """
    calculate the factorial of given number

    parameters:
        n (int): the number whose factorial can be calculated

    returns: 
        int: The factorial of given number
    """
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * factorial (n - 1))
    
# Pass argument in function
print(factorial(7))
    
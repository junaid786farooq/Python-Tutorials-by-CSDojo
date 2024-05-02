# recursive function called fibonacci that returns the nth number in the Fibonacci sequence. Test the function with different values of n.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n -1) + fibonacci(n - 2)

print(fibonacci(7))

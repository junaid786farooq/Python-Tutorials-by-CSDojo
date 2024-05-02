#  recursive function called sum_of_digits that calculates the sum of the digits of a positive integer n. Test the function with different values of n.

def sum_of_digit(n):
    if n == 0:
        return 0
    else:

        last_digit = n % 10

        return last_digit + (sum_of_digit(n // 10))

   
print(sum_of_digit(1234))
print(sum_of_digit(12345))
print(sum_of_digit(123456))
# program that takes a floating-point number input from the user and converts it to an integer, rounding down to the nearest whole number, then prints the result.

import decimal

float_num = float(input("Enter floating point number: "))
num =  round(float_num)
number = int(num)

print(number)
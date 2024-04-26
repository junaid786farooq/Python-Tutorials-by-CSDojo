# Program that converts temperature from Celsius to Fahrenheit and vice versa, storing the temperature values in variables.

temp_fahrenheit = int(input("What is the temperature outside? in Fahrenheit: "))


temp_celsius = (temp_fahrenheit - 32) * 5/9

print("The temperature outside is", temp_celsius, "degrees Celsius")


temp_in_fahrenheit = (temp_celsius * 9/5) + 32

print("The temperature outside is", temp_in_fahrenheit, "degrees Fahrenheit")
